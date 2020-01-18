# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brickton_main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 912)
        MainWindow.setMinimumSize(QtCore.QSize(667, 702))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/brickton_logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_bar = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_bar.setAutoFillBackground(False)
        self.tab_bar.setObjectName("tab_bar")
        self.c_tab = QtWidgets.QWidget()
        self.c_tab.setObjectName("c_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.c_tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.c_chat_output = QtWidgets.QTextBrowser(self.c_tab)
        self.c_chat_output.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.c_chat_output.setObjectName("c_chat_output")
        self.gridLayout_2.addWidget(self.c_chat_output, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.c_send_button = QtWidgets.QPushButton(self.c_tab)
        self.c_send_button.setObjectName("c_send_button")
        self.gridLayout.addWidget(self.c_send_button, 0, 1, 1, 1)
        self.c_upload_button = QtWidgets.QPushButton(self.c_tab)
        self.c_upload_button.setObjectName("c_upload_button")
        self.gridLayout.addWidget(self.c_upload_button, 1, 1, 1, 1)
        self.c_chat_input = QtWidgets.QTextEdit(self.c_tab)
        self.c_chat_input.setObjectName("c_chat_input")
        self.gridLayout.addWidget(self.c_chat_input, 0, 0, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.c_role_label_2 = QtWidgets.QLabel(self.c_tab)
        self.c_role_label_2.setObjectName("c_role_label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.c_role_label_2)
        self.c_role_line = QtWidgets.QLineEdit(self.c_tab)
        self.c_role_line.setReadOnly(True)
        self.c_role_line.setObjectName("c_role_line")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.c_role_line)
        self.c_local_label = QtWidgets.QLabel(self.c_tab)
        self.c_local_label.setObjectName("c_local_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.c_local_label)
        self.c_foreign_label = QtWidgets.QLabel(self.c_tab)
        self.c_foreign_label.setObjectName("c_foreign_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.c_foreign_label)
        self.c_current_label = QtWidgets.QLabel(self.c_tab)
        self.c_current_label.setObjectName("c_current_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.c_current_label)
        self.c_current_line = QtWidgets.QLineEdit(self.c_tab)
        self.c_current_line.setReadOnly(True)
        self.c_current_line.setObjectName("c_current_line")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.c_current_line)
        self.c_remaining_label = QtWidgets.QLabel(self.c_tab)
        self.c_remaining_label.setObjectName("c_remaining_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.c_remaining_label)
        self.c_remaining_line = QtWidgets.QLineEdit(self.c_tab)
        self.c_remaining_line.setReadOnly(True)
        self.c_remaining_line.setObjectName("c_remaining_line")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.c_remaining_line)
        self.c_ip_label = QtWidgets.QLabel(self.c_tab)
        self.c_ip_label.setObjectName("c_ip_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.c_ip_label)
        self.c_ip_line = QtWidgets.QLineEdit(self.c_tab)
        self.c_ip_line.setObjectName("c_ip_line")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.c_ip_line)
        self.c_connect_button = QtWidgets.QPushButton(self.c_tab)
        self.c_connect_button.setObjectName("c_connect_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.c_connect_button)
        self.c_listen_button = QtWidgets.QPushButton(self.c_tab)
        self.c_listen_button.setObjectName("c_listen_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.c_listen_button)
        self.c_console = QtWidgets.QTextBrowser(self.c_tab)
        self.c_console.setObjectName("c_console")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.c_console)
        self.c_port_line = QtWidgets.QLineEdit(self.c_tab)
        self.c_port_line.setObjectName("c_port_line")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.c_port_line)
        self.c_port_label = QtWidgets.QLabel(self.c_tab)
        self.c_port_label.setObjectName("c_port_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.c_port_label)
        self.c_local_combo = QtWidgets.QComboBox(self.c_tab)
        self.c_local_combo.setObjectName("c_local_combo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.c_local_combo)
        self.c_foreign_combo = QtWidgets.QComboBox(self.c_tab)
        self.c_foreign_combo.setObjectName("c_foreign_combo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.c_foreign_combo)
        self.gridLayout_2.addLayout(self.formLayout, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tab_bar.addTab(self.c_tab, "")
        self.k_tab = QtWidgets.QWidget()
        self.k_tab.setObjectName("k_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.k_tab)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.k_sortby_label = QtWidgets.QFormLayout()
        self.k_sortby_label.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.k_sortby_label.setObjectName("k_sortby_label")
        self.k_listsender_label = QtWidgets.QLabel(self.k_tab)
        self.k_listsender_label.setObjectName("k_listsender_label")
        self.k_sortby_label.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.k_listsender_label)
        self.k_listsender_line = QtWidgets.QLineEdit(self.k_tab)
        self.k_listsender_line.setReadOnly(True)
        self.k_listsender_line.setObjectName("k_listsender_line")
        self.k_sortby_label.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.k_listsender_line)
        self.k_listreceived_label = QtWidgets.QLabel(self.k_tab)
        self.k_listreceived_label.setObjectName("k_listreceived_label")
        self.k_sortby_label.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.k_listreceived_label)
        self.k_listreceiver_line = QtWidgets.QLineEdit(self.k_tab)
        self.k_listreceiver_line.setReadOnly(True)
        self.k_listreceiver_line.setObjectName("k_listreceiver_line")
        self.k_sortby_label.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.k_listreceiver_line)
        self.k_listremaining_label = QtWidgets.QLabel(self.k_tab)
        self.k_listremaining_label.setObjectName("k_listremaining_label")
        self.k_sortby_label.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.k_listremaining_label)
        self.k_listremaining_line = QtWidgets.QLineEdit(self.k_tab)
        self.k_listremaining_line.setReadOnly(True)
        self.k_listremaining_line.setObjectName("k_listremaining_line")
        self.k_sortby_label.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.k_listremaining_line)
        self.k_sender_combo = QtWidgets.QComboBox(self.k_tab)
        self.k_sender_combo.setObjectName("k_sender_combo")
        self.k_sortby_label.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.k_sender_combo)
        self.k_receiver_combo = QtWidgets.QComboBox(self.k_tab)
        self.k_receiver_combo.setObjectName("k_receiver_combo")
        self.k_sortby_label.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.k_receiver_combo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.k_sortby_label.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.k_sender_label = QtWidgets.QLabel(self.k_tab)
        self.k_sender_label.setObjectName("k_sender_label")
        self.k_sortby_label.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.k_sender_label)
        self.k_receiver_label = QtWidgets.QLabel(self.k_tab)
        self.k_receiver_label.setObjectName("k_receiver_label")
        self.k_sortby_label.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.k_receiver_label)
        self.k_sortby_label_2 = QtWidgets.QLabel(self.k_tab)
        self.k_sortby_label_2.setObjectName("k_sortby_label_2")
        self.k_sortby_label.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.k_sortby_label_2)
        self.k_timestamp_line = QtWidgets.QLineEdit(self.k_tab)
        self.k_timestamp_line.setReadOnly(True)
        self.k_timestamp_line.setObjectName("k_timestamp_line")
        self.k_sortby_label.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.k_timestamp_line)
        self.k_datestamp_label = QtWidgets.QLabel(self.k_tab)
        self.k_datestamp_label.setObjectName("k_datestamp_label")
        self.k_sortby_label.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.k_datestamp_label)
        self.k_party1_label = QtWidgets.QLabel(self.k_tab)
        self.k_party1_label.setObjectName("k_party1_label")
        self.k_sortby_label.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.k_party1_label)
        self.k_party2_label = QtWidgets.QLabel(self.k_tab)
        self.k_party2_label.setObjectName("k_party2_label")
        self.k_sortby_label.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.k_party2_label)
        self.k_export1_combo = QtWidgets.QComboBox(self.k_tab)
        self.k_export1_combo.setObjectName("k_export1_combo")
        self.k_sortby_label.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.k_export1_combo)
        self.k_export2_combo = QtWidgets.QComboBox(self.k_tab)
        self.k_export2_combo.setObjectName("k_export2_combo")
        self.k_sortby_label.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.k_export2_combo)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.k_sortby_label.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.k_export_label = QtWidgets.QLabel(self.k_tab)
        self.k_export_label.setObjectName("k_export_label")
        self.k_sortby_label.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.k_export_label)
        self.k_import_button = QtWidgets.QPushButton(self.k_tab)
        self.k_import_button.setObjectName("k_import_button")
        self.k_sortby_label.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.k_import_button)
        self.k_keyinfo_label = QtWidgets.QLabel(self.k_tab)
        self.k_keyinfo_label.setObjectName("k_keyinfo_label")
        self.k_sortby_label.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.k_keyinfo_label)
        self.k_export_button = QtWidgets.QPushButton(self.k_tab)
        self.k_export_button.setObjectName("k_export_button")
        self.k_sortby_label.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.k_export_button)
        self.gridLayout_3.addLayout(self.k_sortby_label, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.k_browser_label = QtWidgets.QLabel(self.k_tab)
        self.k_browser_label.setObjectName("k_browser_label")
        self.verticalLayout_2.addWidget(self.k_browser_label)
        self.k_listkey_list = QtWidgets.QListWidget(self.k_tab)
        self.k_listkey_list.setObjectName("k_listkey_list")
        self.verticalLayout_2.addWidget(self.k_listkey_list)
        self.k_console_label = QtWidgets.QLabel(self.k_tab)
        self.k_console_label.setObjectName("k_console_label")
        self.verticalLayout_2.addWidget(self.k_console_label)
        self.k_console_textedit = QtWidgets.QTextEdit(self.k_tab)
        self.k_console_textedit.setReadOnly(True)
        self.k_console_textedit.setObjectName("k_console_textedit")
        self.verticalLayout_2.addWidget(self.k_console_textedit)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.k_generate_button = QtWidgets.QPushButton(self.k_tab)
        self.k_generate_button.setObjectName("k_generate_button")
        self.gridLayout_6.addWidget(self.k_generate_button, 3, 1, 1, 1)
        self.k_genparty1_label = QtWidgets.QLabel(self.k_tab)
        self.k_genparty1_label.setObjectName("k_genparty1_label")
        self.gridLayout_6.addWidget(self.k_genparty1_label, 1, 0, 1, 1)
        self.k_random_combo = QtWidgets.QComboBox(self.k_tab)
        self.k_random_combo.setObjectName("k_random_combo")
        self.gridLayout_6.addWidget(self.k_random_combo, 2, 3, 1, 1)
        self.k_genparty1_line = QtWidgets.QLineEdit(self.k_tab)
        self.k_genparty1_line.setObjectName("k_genparty1_line")
        self.gridLayout_6.addWidget(self.k_genparty1_line, 1, 1, 1, 1)
        self.k_genparty2_label = QtWidgets.QLabel(self.k_tab)
        self.k_genparty2_label.setObjectName("k_genparty2_label")
        self.gridLayout_6.addWidget(self.k_genparty2_label, 1, 2, 1, 1)
        self.k_genparty2_line = QtWidgets.QLineEdit(self.k_tab)
        self.k_genparty2_line.setObjectName("k_genparty2_line")
        self.gridLayout_6.addWidget(self.k_genparty2_line, 1, 3, 1, 1)
        self.k_gennum_label = QtWidgets.QLabel(self.k_tab)
        self.k_gennum_label.setObjectName("k_gennum_label")
        self.gridLayout_6.addWidget(self.k_gennum_label, 2, 0, 1, 1)
        self.k_cancel_button = QtWidgets.QPushButton(self.k_tab)
        self.k_cancel_button.setObjectName("k_cancel_button")
        self.gridLayout_6.addWidget(self.k_cancel_button, 3, 0, 1, 1)
        self.k_gensource_label = QtWidgets.QLabel(self.k_tab)
        self.k_gensource_label.setObjectName("k_gensource_label")
        self.gridLayout_6.addWidget(self.k_gensource_label, 2, 2, 1, 1)
        self.k_generate_label = QtWidgets.QLabel(self.k_tab)
        self.k_generate_label.setObjectName("k_generate_label")
        self.gridLayout_6.addWidget(self.k_generate_label, 0, 1, 1, 1)
        self.k_gennum_spinbox = QtWidgets.QSpinBox(self.k_tab)
        self.k_gennum_spinbox.setObjectName("k_gennum_spinbox")
        self.gridLayout_6.addWidget(self.k_gennum_spinbox, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_6, 2, 0, 1, 2)
        self.k_genprogress_bar = QtWidgets.QProgressBar(self.k_tab)
        self.k_genprogress_bar.setEnabled(True)
        self.k_genprogress_bar.setProperty("value", 0)
        self.k_genprogress_bar.setObjectName("k_genprogress_bar")
        self.gridLayout_3.addWidget(self.k_genprogress_bar, 1, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tab_bar.addTab(self.k_tab, "")
        self.o_tab = QtWidgets.QWidget()
        self.o_tab.setObjectName("o_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.o_tab)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.o_sender_combo = QtWidgets.QComboBox(self.o_tab)
        self.o_sender_combo.setObjectName("o_sender_combo")
        self.gridLayout_5.addWidget(self.o_sender_combo, 4, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 13, 1, 1, 1)
        self.o_selectencode_line = QtWidgets.QLineEdit(self.o_tab)
        self.o_selectencode_line.setObjectName("o_selectencode_line")
        self.gridLayout_5.addWidget(self.o_selectencode_line, 7, 1, 1, 1)
        self.o_decode_button = QtWidgets.QPushButton(self.o_tab)
        self.o_decode_button.setObjectName("o_decode_button")
        self.gridLayout_5.addWidget(self.o_decode_button, 1, 0, 1, 1)
        self.o_encode_button = QtWidgets.QPushButton(self.o_tab)
        self.o_encode_button.setObjectName("o_encode_button")
        self.gridLayout_5.addWidget(self.o_encode_button, 8, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 0, 3, 1, 1)
        self.o_selectdecode_button = QtWidgets.QPushButton(self.o_tab)
        self.o_selectdecode_button.setObjectName("o_selectdecode_button")
        self.gridLayout_5.addWidget(self.o_selectdecode_button, 0, 0, 1, 1)
        self.o_sender_label = QtWidgets.QLabel(self.o_tab)
        self.o_sender_label.setObjectName("o_sender_label")
        self.gridLayout_5.addWidget(self.o_sender_label, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.o_selectdecode_line = QtWidgets.QLineEdit(self.o_tab)
        self.o_selectdecode_line.setObjectName("o_selectdecode_line")
        self.gridLayout_5.addWidget(self.o_selectdecode_line, 0, 1, 1, 1)
        self.o_encode_line = QtWidgets.QLineEdit(self.o_tab)
        self.o_encode_line.setText("")
        self.o_encode_line.setObjectName("o_encode_line")
        self.gridLayout_5.addWidget(self.o_encode_line, 8, 1, 1, 1)
        self.o_selectencode_button = QtWidgets.QPushButton(self.o_tab)
        self.o_selectencode_button.setObjectName("o_selectencode_button")
        self.gridLayout_5.addWidget(self.o_selectencode_button, 7, 0, 1, 1)
        self.o_console_text = QtWidgets.QTextBrowser(self.o_tab)
        self.o_console_text.setObjectName("o_console_text")
        self.gridLayout_5.addWidget(self.o_console_text, 0, 2, 9, 1)
        self.o_recipient_combo = QtWidgets.QComboBox(self.o_tab)
        self.o_recipient_combo.setObjectName("o_recipient_combo")
        self.gridLayout_5.addWidget(self.o_recipient_combo, 5, 1, 1, 1)
        self.o_recipient_label = QtWidgets.QLabel(self.o_tab)
        self.o_recipient_label.setObjectName("o_recipient_label")
        self.gridLayout_5.addWidget(self.o_recipient_label, 5, 0, 1, 1, QtCore.Qt.AlignLeft)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 3, 0, 1, 1)
        self.tab_bar.addTab(self.o_tab, "")
        self.verticalLayout.addWidget(self.tab_bar)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.brickton_icon_label = QtWidgets.QLabel(self.centralwidget)
        self.brickton_icon_label.setMinimumSize(QtCore.QSize(111, 51))
        self.brickton_icon_label.setMaximumSize(QtCore.QSize(111, 51))
        self.brickton_icon_label.setText("")
        self.brickton_icon_label.setPixmap(QtGui.QPixmap(":/data/brickton_logo.jpg"))
        self.brickton_icon_label.setScaledContents(True)
        self.brickton_icon_label.setObjectName("brickton_icon_label")
        self.gridLayout_4.addWidget(self.brickton_icon_label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionApplication = QtWidgets.QAction(MainWindow)
        self.actionApplication.setObjectName("actionApplication")
        self.actionDfd = QtWidgets.QAction(MainWindow)
        self.actionDfd.setObjectName("actionDfd")
        self.actionAsdf = QtWidgets.QAction(MainWindow)
        self.actionAsdf.setObjectName("actionAsdf")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_bar.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Brickton"))
        self.c_send_button.setText(_translate("MainWindow", "Send Message"))
        self.c_upload_button.setText(_translate("MainWindow", "Upload File"))
        self.c_role_label_2.setText(_translate("MainWindow", "Role"))
        self.c_local_label.setText(_translate("MainWindow", "Local ID"))
        self.c_foreign_label.setText(_translate("MainWindow", "Foreign ID"))
        self.c_current_label.setText(_translate("MainWindow", "Current Key"))
        self.c_remaining_label.setText(_translate("MainWindow", "Remaining"))
        self.c_ip_label.setText(_translate("MainWindow", "IP Address"))
        self.c_connect_button.setText(_translate("MainWindow", "Connect"))
        self.c_listen_button.setText(_translate("MainWindow", "Listen"))
        self.c_port_label.setText(_translate("MainWindow", "Port"))
        self.tab_bar.setTabText(self.tab_bar.indexOf(self.c_tab), _translate("MainWindow", "Communicate"))
        self.k_listsender_label.setText(_translate("MainWindow", "Sender"))
        self.k_listreceived_label.setText(_translate("MainWindow", "Receiver"))
        self.k_listremaining_label.setText(_translate("MainWindow", "Remaining"))
        self.k_sender_label.setText(_translate("MainWindow", "Sender"))
        self.k_receiver_label.setText(_translate("MainWindow", "Receiver"))
        self.k_sortby_label_2.setText(_translate("MainWindow", "Sort By"))
        self.k_datestamp_label.setText(_translate("MainWindow", "Created"))
        self.k_party1_label.setText(_translate("MainWindow", "Party 1"))
        self.k_party2_label.setText(_translate("MainWindow", "Party 2"))
        self.k_export_label.setText(_translate("MainWindow", "Export"))
        self.k_import_button.setText(_translate("MainWindow", "Import"))
        self.k_keyinfo_label.setText(_translate("MainWindow", "Key Info"))
        self.k_export_button.setText(_translate("MainWindow", "Export"))
        self.k_browser_label.setText(_translate("MainWindow", "Key Browser"))
        self.k_console_label.setText(_translate("MainWindow", "Console"))
        self.k_generate_button.setText(_translate("MainWindow", "Generate"))
        self.k_genparty1_label.setText(_translate("MainWindow", "Party 1    "))
        self.k_genparty2_label.setText(_translate("MainWindow", "Party 2    "))
        self.k_gennum_label.setText(_translate("MainWindow", "# of pairs"))
        self.k_cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.k_gensource_label.setText(_translate("MainWindow", "Source"))
        self.k_generate_label.setText(_translate("MainWindow", "Generate"))
        self.tab_bar.setTabText(self.tab_bar.indexOf(self.k_tab), _translate("MainWindow", "Keys"))
        self.o_decode_button.setText(_translate("MainWindow", "Decode"))
        self.o_encode_button.setText(_translate("MainWindow", "Encode"))
        self.o_selectdecode_button.setText(_translate("MainWindow", "Select File To Decode"))
        self.o_sender_label.setText(_translate("MainWindow", "Sender"))
        self.o_selectencode_button.setText(_translate("MainWindow", "Select File To Encode"))
        self.o_recipient_label.setText(_translate("MainWindow", "<html><head/><body><p>Recipient</p></body></html>"))
        self.tab_bar.setTabText(self.tab_bar.indexOf(self.o_tab), _translate("MainWindow", "Offline"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionApplication.setText(_translate("MainWindow", "Application"))
        self.actionDfd.setText(_translate("MainWindow", "dfd\\"))
        self.actionAsdf.setText(_translate("MainWindow", "asdf"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

from . import brickton_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
