# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_upper.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1590, 901)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 130, 341, 311))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.open_serial = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.open_serial.setGeometry(QtCore.QRect(210, 130, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.open_serial.setFont(font)
        self.open_serial.setObjectName("open_serial")
        self.close_serial = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.close_serial.setGeometry(QtCore.QRect(210, 220, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.close_serial.setFont(font)
        self.close_serial.setObjectName("close_serial")
        self.refresh_port = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.refresh_port.setGeometry(QtCore.QRect(210, 40, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.refresh_port.setFont(font)
        self.refresh_port.setObjectName("refresh_port")
        self.ports_list = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.ports_list.setGeometry(QtCore.QRect(40, 60, 111, 41))
        self.ports_list.setObjectName("ports_list")
        self.label_portselect = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_portselect.setGeometry(QtCore.QRect(43, 21, 111, 41))
        self.label_portselect.setObjectName("label_portselect")
        self.Com_isOpenOrNot_Label = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.Com_isOpenOrNot_Label.setGeometry(QtCore.QRect(40, 210, 111, 41))
        self.Com_isOpenOrNot_Label.setObjectName("Com_isOpenOrNot_Label")
        self.label_portbaud = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_portbaud.setGeometry(QtCore.QRect(40, 100, 101, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_portbaud.sizePolicy().hasHeightForWidth())
        self.label_portbaud.setSizePolicy(sizePolicy)
        self.label_portbaud.setObjectName("label_portbaud")
        self.baud_set_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.baud_set_text.setGeometry(QtCore.QRect(40, 140, 111, 41))
        self.baud_set_text.setObjectName("baud_set_text")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(400, 129, 751, 401))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.DA2min_text = QtWidgets.QTextEdit(self.groupBox)
        self.DA2min_text.setGeometry(QtCore.QRect(10, 50, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA2min_text.setFont(font)
        self.DA2min_text.setObjectName("DA2min_text")
        self.label_DA2_min = QtWidgets.QLabel(self.groupBox)
        self.label_DA2_min.setGeometry(QtCore.QRect(13, 19, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_DA2_min.setFont(font)
        self.label_DA2_min.setObjectName("label_DA2_min")
        self.DA2_max_text = QtWidgets.QLabel(self.groupBox)
        self.DA2_max_text.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA2_max_text.setFont(font)
        self.DA2_max_text.setObjectName("DA2_max_text")
        self.DA2_step_text = QtWidgets.QLabel(self.groupBox)
        self.DA2_step_text.setGeometry(QtCore.QRect(10, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA2_step_text.setFont(font)
        self.DA2_step_text.setObjectName("DA2_step_text")
        self.send_setting = QtWidgets.QPushButton(self.groupBox)
        self.send_setting.setGeometry(QtCore.QRect(550, 120, 151, 61))
        self.send_setting.setObjectName("send_setting")
        self.DA2max_text = QtWidgets.QTextEdit(self.groupBox)
        self.DA2max_text.setGeometry(QtCore.QRect(7, 151, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA2max_text.setFont(font)
        self.DA2max_text.setObjectName("DA2max_text")
        self.DA2step_text = QtWidgets.QTextEdit(self.groupBox)
        self.DA2step_text.setGeometry(QtCore.QRect(10, 250, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA2step_text.setFont(font)
        self.DA2step_text.setObjectName("DA2step_text")
        self.label_DA0_min = QtWidgets.QLabel(self.groupBox)
        self.label_DA0_min.setGeometry(QtCore.QRect(153, 19, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_DA0_min.setFont(font)
        self.label_DA0_min.setObjectName("label_DA0_min")
        self.DA0min_text = QtWidgets.QTextEdit(self.groupBox)
        self.DA0min_text.setGeometry(QtCore.QRect(150, 50, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA0min_text.setFont(font)
        self.DA0min_text.setObjectName("DA0min_text")
        self.DA0max_text = QtWidgets.QTextEdit(self.groupBox)
        self.DA0max_text.setGeometry(QtCore.QRect(147, 151, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA0max_text.setFont(font)
        self.DA0max_text.setObjectName("DA0max_text")
        self.DA0_max_text = QtWidgets.QLabel(self.groupBox)
        self.DA0_max_text.setGeometry(QtCore.QRect(150, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA0_max_text.setFont(font)
        self.DA0_max_text.setObjectName("DA0_max_text")
        self.DA1min_text = QtWidgets.QTextEdit(self.groupBox)
        self.DA1min_text.setGeometry(QtCore.QRect(280, 50, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA1min_text.setFont(font)
        self.DA1min_text.setObjectName("DA1min_text")
        self.DA1max_text = QtWidgets.QTextEdit(self.groupBox)
        self.DA1max_text.setGeometry(QtCore.QRect(277, 151, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA1max_text.setFont(font)
        self.DA1max_text.setObjectName("DA1max_text")
        self.DA1_max_text = QtWidgets.QLabel(self.groupBox)
        self.DA1_max_text.setGeometry(QtCore.QRect(280, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA1_max_text.setFont(font)
        self.DA1_max_text.setObjectName("DA1_max_text")
        self.label_DA1_min = QtWidgets.QLabel(self.groupBox)
        self.label_DA1_min.setGeometry(QtCore.QRect(283, 19, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_DA1_min.setFont(font)
        self.label_DA1_min.setObjectName("label_DA1_min")
        self.label_port_2 = QtWidgets.QLabel(self.groupBox)
        self.label_port_2.setGeometry(QtCore.QRect(180, 340, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_port_2.setFont(font)
        self.label_port_2.setObjectName("label_port_2")
        self.DA0_delta_text = QtWidgets.QLabel(self.groupBox)
        self.DA0_delta_text.setGeometry(QtCore.QRect(150, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA0_delta_text.setFont(font)
        self.DA0_delta_text.setObjectName("DA0_delta_text")
        self.DA0step_text = QtWidgets.QTextEdit(self.groupBox)
        self.DA0step_text.setGeometry(QtCore.QRect(150, 250, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA0step_text.setFont(font)
        self.DA0step_text.setObjectName("DA0step_text")
        self.DA1step_text = QtWidgets.QTextEdit(self.groupBox)
        self.DA1step_text.setGeometry(QtCore.QRect(280, 250, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA1step_text.setFont(font)
        self.DA1step_text.setObjectName("DA1step_text")
        self.DA1_delta_text = QtWidgets.QLabel(self.groupBox)
        self.DA1_delta_text.setGeometry(QtCore.QRect(280, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA1_delta_text.setFont(font)
        self.DA1_delta_text.setObjectName("DA1_delta_text")
        self.DA2_step_text_2 = QtWidgets.QLabel(self.groupBox)
        self.DA2_step_text_2.setGeometry(QtCore.QRect(10, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA2_step_text_2.setFont(font)
        self.DA2_step_text_2.setObjectName("DA2_step_text_2")
        self.DA2delta_text = QtWidgets.QTextEdit(self.groupBox)
        self.DA2delta_text.setGeometry(QtCore.QRect(10, 340, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DA2delta_text.setFont(font)
        self.DA2delta_text.setObjectName("DA2delta_text")
        self.send_close_sys = QtWidgets.QPushButton(self.groupBox)
        self.send_close_sys.setGeometry(QtCore.QRect(550, 220, 151, 51))
        self.send_close_sys.setObjectName("send_close_sys")
        self.send_open_sys = QtWidgets.QPushButton(self.groupBox)
        self.send_open_sys.setGeometry(QtCore.QRect(550, 320, 151, 51))
        self.send_open_sys.setObjectName("send_open_sys")
        self.freq_label = QtWidgets.QLabel(self.groupBox)
        self.freq_label.setGeometry(QtCore.QRect(560, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.freq_label.setFont(font)
        self.freq_label.setObjectName("freq_label")
        self.Freq_set = QtWidgets.QTextEdit(self.groupBox)
        self.Freq_set.setGeometry(QtCore.QRect(557, 51, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Freq_set.setFont(font)
        self.Freq_set.setObjectName("Freq_set")
        self.msg_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.msg_log.setGeometry(QtCore.QRect(1170, 130, 371, 511))
        self.msg_log.setObjectName("msg_log")
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setGeometry(QtCore.QRect(120, 60, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_port.setFont(font)
        self.label_port.setObjectName("label_port")
        self.label_msg_log = QtWidgets.QLabel(self.centralwidget)
        self.label_msg_log.setGeometry(QtCore.QRect(1280, 70, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_msg_log.setFont(font)
        self.label_msg_log.setObjectName("label_msg_log")
        self.label_port_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_port_3.setGeometry(QtCore.QRect(510, 60, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_port_3.setFont(font)
        self.label_port_3.setObjectName("label_port_3")
        self.groupBox_net = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_net.setGeometry(QtCore.QRect(30, 549, 1121, 121))
        self.groupBox_net.setAutoFillBackground(True)
        self.groupBox_net.setTitle("")
        self.groupBox_net.setObjectName("groupBox_net")
        self.dst_ip_text = QtWidgets.QTextEdit(self.groupBox_net)
        self.dst_ip_text.setGeometry(QtCore.QRect(70, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dst_ip_text.setFont(font)
        self.dst_ip_text.setObjectName("dst_ip_text")
        self.label_dst_ip = QtWidgets.QLabel(self.groupBox_net)
        self.label_dst_ip.setGeometry(QtCore.QRect(10, 10, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_dst_ip.setFont(font)
        self.label_dst_ip.setObjectName("label_dst_ip")
        self.label_dst_port = QtWidgets.QLabel(self.groupBox_net)
        self.label_dst_port.setGeometry(QtCore.QRect(10, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_dst_port.setFont(font)
        self.label_dst_port.setObjectName("label_dst_port")
        self.dst_port_text = QtWidgets.QTextEdit(self.groupBox_net)
        self.dst_port_text.setGeometry(QtCore.QRect(70, 70, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dst_port_text.setFont(font)
        self.dst_port_text.setObjectName("dst_port_text")
        self.label_local_port = QtWidgets.QLabel(self.groupBox_net)
        self.label_local_port.setGeometry(QtCore.QRect(280, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_local_port.setFont(font)
        self.label_local_port.setObjectName("label_local_port")
        self.local_port_text = QtWidgets.QTextEdit(self.groupBox_net)
        self.local_port_text.setGeometry(QtCore.QRect(340, 70, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.local_port_text.setFont(font)
        self.local_port_text.setObjectName("local_port_text")
        self.label_local_ip = QtWidgets.QLabel(self.groupBox_net)
        self.label_local_ip.setGeometry(QtCore.QRect(280, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_local_ip.setFont(font)
        self.label_local_ip.setObjectName("label_local_ip")
        self.local_ip_text = QtWidgets.QTextEdit(self.groupBox_net)
        self.local_ip_text.setGeometry(QtCore.QRect(340, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.local_ip_text.setFont(font)
        self.local_ip_text.setObjectName("local_ip_text")
        self.label_local_storage = QtWidgets.QLabel(self.groupBox_net)
        self.label_local_storage.setGeometry(QtCore.QRect(580, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_local_storage.setFont(font)
        self.label_local_storage.setObjectName("label_local_storage")
        self.local_storage_text = QtWidgets.QTextEdit(self.groupBox_net)
        self.local_storage_text.setGeometry(QtCore.QRect(730, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.local_storage_text.setFont(font)
        self.local_storage_text.setObjectName("local_storage_text")
        self.label_storage_time = QtWidgets.QLabel(self.groupBox_net)
        self.label_storage_time.setGeometry(QtCore.QRect(580, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_storage_time.setFont(font)
        self.label_storage_time.setObjectName("label_storage_time")
        self.local_storage_time = QtWidgets.QTextEdit(self.groupBox_net)
        self.local_storage_time.setGeometry(QtCore.QRect(730, 70, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.local_storage_time.setFont(font)
        self.local_storage_time.setObjectName("local_storage_time")
        self.label_portselect_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_portselect_2.setGeometry(QtCore.QRect(30, 660, 631, 71))
        self.label_portselect_2.setObjectName("label_portselect_2")
        self.label_net_modu = QtWidgets.QLabel(self.centralwidget)
        self.label_net_modu.setGeometry(QtCore.QRect(30, 480, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_net_modu.setFont(font)
        self.label_net_modu.setObjectName("label_net_modu")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1590, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ControlSys"))
        self.open_serial.setText(_translate("MainWindow", "打开串口"))
        self.close_serial.setText(_translate("MainWindow", "关闭串口"))
        self.refresh_port.setText(_translate("MainWindow", "刷新串口"))
        self.label_portselect.setText(_translate("MainWindow", "选择串口"))
        self.Com_isOpenOrNot_Label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_portbaud.setText(_translate("MainWindow", "波特率设置"))
        self.baud_set_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">9600</span></p></body></html>"))
        self.DA2min_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_DA2_min.setText(_translate("MainWindow", "DA2_min/V"))
        self.DA2_max_text.setText(_translate("MainWindow", "DA2_max/V"))
        self.DA2_step_text.setText(_translate("MainWindow", "DA2_step/V"))
        self.send_setting.setText(_translate("MainWindow", "确认配置"))
        self.DA2max_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8</p></body></html>"))
        self.DA2step_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_DA0_min.setText(_translate("MainWindow", "DA0_min/V"))
        self.DA0min_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">1</span></p></body></html>"))
        self.DA0max_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8</p></body></html>"))
        self.DA0_max_text.setText(_translate("MainWindow", "DA0_max/V"))
        self.DA1min_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">1</span></p></body></html>"))
        self.DA1max_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8</p></body></html>"))
        self.DA1_max_text.setText(_translate("MainWindow", "DA1_max/V"))
        self.label_DA1_min.setText(_translate("MainWindow", "DA1_min/V"))
        self.label_port_2.setText(_translate("MainWindow", "单位/V 范围 0~10V"))
        self.DA0_delta_text.setText(_translate("MainWindow", "DA0_step/V"))
        self.DA0step_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.DA1step_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.DA1_delta_text.setText(_translate("MainWindow", "DA1_step/V"))
        self.DA2_step_text_2.setText(_translate("MainWindow", "DA2_delta/V"))
        self.DA2delta_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.send_close_sys.setText(_translate("MainWindow", "关闭系统"))
        self.send_open_sys.setText(_translate("MainWindow", "打开系统"))
        self.freq_label.setText(_translate("MainWindow", "Freq/kHz"))
        self.Freq_set.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\',\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_port.setText(_translate("MainWindow", "串口设置"))
        self.label_msg_log.setText(_translate("MainWindow", "通信日志"))
        self.label_port_3.setText(_translate("MainWindow", "系统配置"))
        self.dst_ip_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'Times New Roman\';\">192.168.5.12</span></p></body></html>"))
        self.label_dst_ip.setText(_translate("MainWindow", "仪器IP"))
        self.label_dst_port.setText(_translate("MainWindow", "仪器端口"))
        self.dst_port_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2599</p></body></html>"))
        self.label_local_port.setText(_translate("MainWindow", "本地端口"))
        self.local_port_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2599</p></body></html>"))
        self.label_local_ip.setText(_translate("MainWindow", "本机IP"))
        self.local_ip_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'Times New Roman\';\">192.168.0.3</span></p></body></html>"))
        self.label_local_storage.setText(_translate("MainWindow", "文件存储路径"))
        self.local_storage_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'Times New Roman\';\">D:\\recvdata</span></p></body></html>"))
        self.label_storage_time.setText(_translate("MainWindow", "存储时间/s"))
        self.local_storage_time.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">60</p></body></html>"))
        self.label_portselect_2.setText(_translate("MainWindow", "注意！请在开启系统前配置好网络信息与文件路径，否则将无法存下数据"))
        self.label_net_modu.setText(_translate("MainWindow", "系统数据传输"))
