import base64
import hashlib
import io
import json
import time

from PyQt5.Qt import pyqtSignal
from PyQt5.Qt import QObject
from PyQt5.Qt import QHostAddress
from PyQt5.Qt import QTcpSocket

from .error import BricktonError


class Client(QObject):
    '''Handles socket.'''

    # Emitted Signals
    comm_update = pyqtSignal([str], name='communication_update')
    chat_update = pyqtSignal([dict], name='chat_update')
    client_connected = pyqtSignal(name='client_connected')
    handshake_succeded = pyqtSignal(name='handshake_succeeded')
    handshake_failed = pyqtSignal(name='handshake_failed')
    msg_ready = pyqtSignal([dict], name='msg_ready')
    comm_error = pyqtSignal(name='comm_error')

    # Signals listened to
    # data_ready = pyqtSignal([str, dict], name='data_ready')
    
    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._parent = parent
        self._km = parent.key_manager
        self._codec = parent.codec
        self._VERSION = parent.VERSION
        self._qsocket = QTcpSocket(self)
        self._bytestream = None
        self._other_party = None
        self._this_party = None
        self._ip_address = None
        self._port = None
        self._setup()
    
    def _setup(self):
        # Ready read
        self._qsocket.readyRead.connect(self._on_ready_read)
        # On connection
        self._qsocket.connected.connect(self._on_connection)
        # On disconnection
        self._qsocket.disconnected.connect(self._on_disconnection)
        # Prime the json generator
        self._msg_buffer = self._add_to_buffer()
        self._msg_buffer.send(None)
        # Connect self.msg_ready
        self.msg_ready.connect(self._dispatch_msg)
        # COnnect connection to _client_handshake_1 to start it off.
        self._qsocket.connected.connect(self._client_handshake_1)
        # Connect error to emit socket update.
        self._qsocket.error.connect(self._on_error)

    def _on_connection(self):
        name = str(self._qsocket.peerName())
        address = self._qsocket.peerAddress().toString()
        self.comm_update.emit('Connected to ' +
                              name +
                              ' (' + address + ')' + '.')
        
    def _on_disconnection(self):
        self.comm_update.emit('Connection terminated.')
        self.comm_error.emit()

    def _on_error(self):
        self.comm_update.emit(self._qsocket.errorString() + '.')
        self.comm_error.emit()
        
    def _on_ready_read(self):
        data = self._qsocket.read(4096)
        self._msg_buffer.send(data)
        # Re-emit readyRead, quasi-recursive.
        if self._qsocket.bytesAvailable():
            self._qsocket.readyRead.emit()

    def _add_to_buffer(self):
        '''Generator created in _setup. Issues data via signal.'''
        # Set up constants.
        opener = '{' #123
        closer = '}' #125
        single_quote = '\'' # 39
        double_quote = '\"' # 34
        self._bytestream = io.BytesIO()
        inside_double_quote = False
        inside_single_quote = False
        opener_count = 0
        closer_count = 0
        # Repeat this loop until end of time.
        while True:
            # Given via generator.send method.
            raw_data = yield
            data = raw_data.decode('utf-8')
            for character in data:
                if character == single_quote:
                    # If True, False. If False, True.
                    inside_single_quote = not inside_single_quote
                if character == double_quote:
                    inside_double_quote = not inside_double_quote
                if inside_single_quote or inside_double_quote:
                    pass
                else:
                    if character == opener:
                        opener_count += 1
                    if character == closer:
                        closer_count += 1
                    if opener_count == closer_count:
                        # Write final character to bytestream
                        self._bytestream.write(character.encode())
                        # Complete JSON message.
                        json_msg = self._bytestream.getvalue().decode('utf-8')
                        msg = json.loads(json_msg)
                        self.msg_ready.emit(msg)
                        # Reset because it's a new message now.
                        self._bytestream = io.BytesIO()
                        inside_double_quote = False
                        inside_single_quote = False
                        opener_count = 0
                        closer_count = 0
                        # Back to "while True" loop
                        continue
                # Write to bytestream
                self._bytestream.write(character.encode())

    def connect_(self, identity, ip_address, port, numeric=True):
        self.comm_update.emit('Connecting.')
        self._this_party = identity
        # If connected, disconnect.
        try:
            if self._qsocket.state == 3:
                self._qsocket.disconnectFromHost()
        except AttributeError:
            pass
        # Connect to host
        if numeric:
            self._qsocket.connectToHost(QHostAddress(ip_address), int(port))
        else:
            self._qsocket.connectToHost(ip_address, int(port))          

    def _dispatch_msg(self, msg_dict):
        '''Route message to correct function.'''
        msg_type = msg_dict['metadata']['type']
        routing_dict = {'text': self._recv_text,
                        'file': None,
                        'server_handshake_1': self._client_handshake_2,
                        'server_handshake_2': self._client_handshake_3}
        function_to_use = routing_dict[msg_type]
        function_to_use(msg_dict)

    def _client_handshake_1(self):
        # Client sends client handshake 1 with list of keys (first msg).
        key_list = [key.name for key in self._km.get_all_keys()]
        data_dict = {'key_list': key_list}
        client_msg_1 = self._create_json_msg('client_handshake_1', data_dict)
        self._qsocket.write(client_msg_1.encode())
    
    def _client_handshake_2(self, msg_dict):
        self._other_party = msg_dict['metadata']['sender']
        shared_keys = msg_dict['data']['shared_keys']
        client_shared_key_data = [self._km.get_key_data(key)
                                  for key
                                  in shared_keys]
        data_dict = {'client_shared_key_data': client_shared_key_data}
        client_msg_2 = self._create_json_msg('client_handshake_2', data_dict)
        self._qsocket.write(client_msg_2.encode())

    def _client_handshake_3(self, msg_dict):
        '''No message.'''
        # Server sends server handshake 2.
        harmonized_data = msg_dict['data']['harmonized_data']
        if not harmonized_data:
            self.comm_update.emit('No shared keys.')
            self._qsocket.disconnectFromHost()
            return False
        for item in harmonized_data:
            if item['sender'] == self._this_party:
                self._km.add_to_outbound(item['name'])
            if item['sender'] == self._other_party:
                self._km.add_to_inbound(item['name'])
        self.handshake_succeded.emit()
        self.comm_update.emit('Client-side handshake complete.')

    def _recv_text(self, msg):
        ciphertext = msg['data']['ciphertext']
        cipherhash = msg['data']['cipherhash']
        plaintext = self._codec.decode(ciphertext, cipherhash)
        msg['plaintext'] = plaintext
        msg['source'] = self._other_party
        self.chat_update.emit(msg)
                 
    def send_text(self, text_data):
        data_bytes = text_data.encode('utf-8')
        ciphertext, cipherhash = self._codec.encode(data_bytes)
        data_dict = {'ciphertext': base64.b64encode(ciphertext).decode(),
                     'cipherhash': base64.b64encode(cipherhash).decode()}
        msg = self._create_json_msg('text', data_dict)
        self._qsocket.write(msg.encode())
        self.chat_update.emit({'source': self._this_party,
                               'content': text_data})
    
    def _send_file(self, file_object):
        pass

    def _recv_file(self, output_path):
        pass

    def _create_json_msg(self, msg_type, data_dict):
        '''Create msg based on template (must be json serialize-able).'''
        base = {'metadata': {'brickton_version': self._VERSION,
                             'sender': self._this_party,
                             'receiver': self._other_party,
                             'timestamp': '{0:.7f}'.format(time.time()),
                             'encoding': 'base64',
                             'type': msg_type},
                'data':{}}
        # Types to check against.
        types = ['text',
                 'file',
                 'server_handshake_1',
                 'server_handshake_2', 
                 'client_handshake_1',
                 'client_handshake_2']
        # Type error checking.
        if not msg_type in types:
            raise BricktonError('Message type not valid.')
        # Keys by type.
        keys_by_type = {'text': ['ciphertext', 'cipherhash'],
                        'file': ['ciphertext', 'cipherhash', 'ciphername'],
                        'server_handshake_1': ['shared_keys'],
                        'server_handshake_2': ['harmonized_data'], 
                        'client_handshake_1': ['key_list'],
                        'client_handshake_2': ['client_shared_key_data']}
        # Keys by type error checking.
        for key in data_dict.keys():
            if not key in keys_by_type[msg_type]:
                raise BricktonError('Improper data for message type supplied.')
        # Populate data dict.
        for key, value in data_dict.items():
            base['data'][key] = value
        # Create and return msg as json.
        msg_string = json.dumps(base)
        return msg_string

    def stop(self):
        self._qsocket.close()
        self.terminate()

