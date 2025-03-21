
# 逻辑文件


import sys
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtWidgets import QApplication, QMainWindow
from datetime import datetime
#from PyQt5.QtWebEngineWidgets import *
from UI_upper import Ui_MainWindow
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QVBoxLayout
import csv

# from PyQt5 import QtCore

# QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 屏幕自适应

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置实例
        self.CreateItems()
        # 设置信号与槽
        self.CreateSignalSlot()

    # 设置实例
    def CreateItems(self):
        # Qt 串口类
        self.com = QSerialPort()
        # Qt 定时器类
        # self.timer = QTimer(self) #初始化一个定时器
        # self.timer.timeout.connect(self.ShowTime) #计时结束调用operate()方法
        # self.timer.start(100) #设置计时间隔 100ms 并启动

    # 设置信号与槽
    def CreateSignalSlot(self):
        self.open_serial.clicked.connect(self.Com_Open_Button_clicked)
        self.close_serial.clicked.connect(self.Com_Close_Button_clicked)
        self.send_setting.clicked.connect(self.SendButton_clicked)
        self.refresh_port.clicked.connect(self.Com_Refresh_Button_Clicked)
        self.send_close_sys.clicked.connect(self.Sys_Close_Button_clicked)
        self.send_open_sys.clicked.connect(self.Sys_Open_Button_clicked)

        #self.textEdit.toPlainText()

    # 串口刷新
    def Com_Refresh_Button_Clicked(self):
        self.ports_list.clear()  # 清空当前的串口列表
        self.msg_log.clear()  # 清空日志区
        successful_ports = []  # 用于记录成功打开的端口

        for i in range(1, 15):  # 扫描接口 1 到 14
            port_name = f"COM{i}"  # 生成串口名
            self.com.setPortName(port_name)  # 设置串口名称
            # 尝试打开串口
            if self.com.open(QSerialPort.ReadWrite):
                successful_ports.append(port_name)  # 记录成功的端口
                self.ports_list.addItem(port_name)  # 添加到 ComboBox
                self.msg_log.insertPlainText(f"Opened: {port_name}\n")  # 记录到日志
                self.com.close()  # 关闭串口
        # 输出记录的成功端口信息
        if successful_ports:
            self.msg_log.insertPlainText("Successfully opened ports:\n" + "\n".join(successful_ports) + "\n")
        else:
            self.msg_log.insertPlainText("No ports could be opened.\n")

    def Com_Open_Button_clicked(self):
        self.ports_list.update()  # 强制更新 ComboBox
        comName = self.ports_list.currentText()
        if not comName:
            self.msg_log.insertPlainText("No COM port selected.\n")
            return
        self.msg_log.insertPlainText(f"Attempting to open: {comName}\n")
        # 尝试获取波特率并处理可能的错误
        try:
            comBaud = int(self.baud_set_text.toPlainText())  # 使用 toPlainText() 方法获取输入
            self.msg_log.insertPlainText(f"Baud rate set to: {comBaud}\n")
        except ValueError:
            self.msg_log.insertPlainText("Invalid baud rate selected.\n")
            return
            # 打开串口逻辑
        self.com.setPortName(comName)  # 设置串口名称
        if self.com.open(QSerialPort.ReadWrite):
            self.msg_log.insertPlainText(f"Opened {comName} successfully.\n")
        else:
            self.msg_log.insertPlainText(f"Failed to open {comName}: {self.com.errorString()}\n")
        self.close_serial.setEnabled(True)
        self.open_serial.setEnabled(False)
        self.refresh_port.setEnabled(False)
        self.ports_list.setEnabled(False)
        # self.Com_Baud_Combo.setEnabled(True)
        self.Com_isOpenOrNot_Label.setText('  已打开')
        self.msg_log.insertPlainText('\n')

    def Com_Send_Data(self, byte_data):
        # 检查 byte_data 是否为字节类型且长度为 5
        if not isinstance(byte_data, (bytes, bytearray)) or len(byte_data) != 5:
            self.msg_log.insertPlainText("发送数据格式错误，必须为 5 字节数据。\n")
            return
        try:
            # 检查串口是否已经打开
            if not self.com.isOpen():
                self.com.setPortName(self.ports_list.currentText())
                if not self.com.open(QSerialPort.ReadWrite):
                    self.msg_log.insertPlainText(f"无法打开串口 {self.com.portName()}: {self.com.errorString()}\n")
                    return
                self.com.setBaudRate(9600)  # 设置波特率
            bytes_written = self.com.write(byte_data)  # 发送字节数据
            if bytes_written == -1:
                self.msg_log.insertPlainText("发送数据失败: " + self.com.errorString() + "\n")
            else:
                self.msg_log.insertPlainText("发送数据成功: " + str(byte_data) + "\n")
        except ValueError as e:
            self.msg_log.insertPlainText(f"数据转换错误: {e}\n")
        except Exception as e:
            self.msg_log.insertPlainText(f"发送数据时发生错误: {e}\n")

    # 发送按钮按下
    def SendButton_clicked(self):
        ### 获取adc频率设置 ###
        try:
            freq_value = self.Freq_set.toPlainText().strip()  # 获取并去除空格
            self.msg_log.insertPlainText(f"输入的adc采样频率值: {freq_value}kHz.\n")  # 调试信息
            if not freq_value.isdigit():  # 检查是否为正整数
                raise ValueError("频率必须是一个有效的正整数")
            freq_value = int(freq_value)
            if freq_value <= 0:
                raise ValueError("频率必须是一个正的非零整数")
            f_scan_code = int(25000 / freq_value)
            if f_scan_code < 0:
                raise ValueError("计算出的扫描代码无效，可能是由于频率设置错误")
            data_f_scan_code = hex((0xfc << 32) | (f_scan_code << 0))
            data_f_scan_code = data_f_scan_code[2:]  # 去掉 '0x' 前缀
            # 确保生成的十六进制字符串为偶数长度
            if len(data_f_scan_code) % 2 != 0:
                data_f_scan_code = '0' + data_f_scan_code  # 补全为偶数长度
            byte_data_f_scan_code = bytes.fromhex(data_f_scan_code)  # 转换为字节
        except ValueError as ve:
            self.msg_log.insertPlainText(f"输入错误: {ve}\n")
            return
        except Exception as e:
            self.msg_log.insertPlainText(f"发生错误: {e}\n")
            return
        ### 获取pct频率设置 ###
        try:
            freq_pct_value = self.Freq_set_pct.toPlainText().strip()  # 获取并去除空格
            self.msg_log.insertPlainText(f"输入的pct频率值: {freq_pct_value}kHz.\n")  # 调试信息
            if not freq_pct_value.isdigit():  # 检查是否为正整数
                raise ValueError("频率必须是一个有效的正整数")
            freq_pct_value = int(freq_pct_value)
            if freq_pct_value <= 0:
                raise ValueError("频率必须是一个正的非零整数")
            f_scan_pct_code = int(250 / freq_pct_value)
            if f_scan_pct_code < 0:
                raise ValueError("计算出的扫描代码无效，可能是由于频率设置错误")
            data_f_scan_pct_code = hex((0xa5 << 32) | (f_scan_pct_code << 0))
            data_f_scan_pct_code = data_f_scan_pct_code[2:]  # 去掉 '0x' 前缀
            # 确保生成的十六进制字符串为偶数长度
            if len(data_f_scan_pct_code) % 2 != 0:
                data_f_scan_pct_code = '0' + data_f_scan_pct_code  # 补全为偶数长度
            byte_data_f_scan_pct_code = bytes.fromhex(data_f_scan_pct_code)  # 转换为字节
        except ValueError as ve:
            self.msg_log.insertPlainText(f"输入错误: {ve}\n")
            return
        except Exception as e:
            self.msg_log.insertPlainText(f"发生错误: {e}\n")
            return
        ### 获取dac频率设置 ###
        try:
            freq_scan_value = self.Freq_set_scan.toPlainText().strip()  # 获取并去除空格
            self.msg_log.insertPlainText(f"输入的scan步进频率值: {freq_scan_value}kHz.\n")  # 调试信息
            if not freq_scan_value.isdigit():  # 检查是否为正整数
                raise ValueError("频率必须是一个有效的正整数")
            freq_scan_value = int(freq_scan_value)
            if freq_scan_value <= 0:
                raise ValueError("频率必须是一个正的非零整数")
            f_scan_dac_code = int(25000 / freq_scan_value)
            if f_scan_dac_code < 0:
                raise ValueError("计算出的扫描代码无效，可能是由于频率设置错误")
            data_f_scan_dac_code = hex((0xcf << 32) | (f_scan_dac_code << 0))
            data_f_scan_dac_code = data_f_scan_dac_code[2:]  # 去掉 '0x' 前缀
            # 确保生成的十六进制字符串为偶数长度
            if len(data_f_scan_dac_code) % 2 != 0:
                data_f_scan_dac_code = '0' + data_f_scan_dac_code  # 补全为偶数长度
            byte_data_f_scan_dac_code = bytes.fromhex(data_f_scan_dac_code)  # 转换为字节
        except ValueError as ve:
            self.msg_log.insertPlainText(f"输入错误: {ve}\n")
            return
        except Exception as e:
            self.msg_log.insertPlainText(f"发生错误: {e}\n")
            return
        ### 设备参数计算 ###
        Voltage_transcode = 5000/(0xffff) # each_code /mV
        ### 获取ad0的数据 拼成指令帧 ###
        ad0_thre = int(float(self.AD0_thre_text.toPlainText()) * 1000 / Voltage_transcode)
        ad_threshold = hex((0xa0 << 32) | (ad0_thre << 0))
        ad_threshold = ad_threshold[2:]
        byte_ad_threshold = bytes.fromhex(ad_threshold)
        ### 获取da2的数据 拼成指令帧 ###
        # B0 min max
        da2_min = int(float(self.DA2min_text.toPlainText()) * 1000 / Voltage_transcode)
        da2_max = int(float(self.DA2max_text.toPlainText()) * 1000 / Voltage_transcode)
        data_da2_minmax = hex((0xb0 << 32) | (da2_min << 16) | (da2_max << 0))
        data_da2_minmax = data_da2_minmax[2:]
        byte_data_da2_minmax = bytes.fromhex(data_da2_minmax)
        # B5 00 00 step
        da2_step = int(float(self.DA2step_text.toPlainText()) * 1000 / Voltage_transcode)
        data_da2_step = hex((0xb5 << 32) | (0 << 16) | (da2_step << 0))
        data_da2_step = data_da2_step[2:]
        byte_data_da2_step = bytes.fromhex(data_da2_step)
        # B9 00 00 delta
        # da2_delta = int(float(self.DA2delta_text.toPlainText()) * 1000 / Voltage_transcode)
        # data_da2_delta = hex((0xb9 << 32) | (0 << 16) | (da2_delta << 0))
        # data_da2_delta = data_da2_delta[2:]
        # byte_data_da2_delta = bytes.fromhex(data_da2_delta)
        ### 获取da0的数据 拼成指令帧 ###
        # D1 min max
        da0_min = int(float(self.DA0min_text.toPlainText()) * 1000 / Voltage_transcode)
        da0_max = int(float(self.DA0max_text.toPlainText()) * 1000 / Voltage_transcode)
        data_da0_minmax = hex((0xd1 << 32) | (da0_min << 16) | (da0_max << 0))
        data_da0_minmax = data_da0_minmax[2:]
        byte_data_da0_minmax = bytes.fromhex(data_da0_minmax)
        # D6 00 00 step
        da0_step = int(float(self.DA0step_text.toPlainText()) * 1000 / Voltage_transcode)
        data_da0_step = hex((0xd6 << 32) | (0 << 16) | (da0_step << 0))
        data_da0_step = data_da0_step[2:]
        byte_data_da0_step = bytes.fromhex(data_da0_step)
        ### 获取da1的数据 拼成指令帧 ###
        # E2 min max
        da1_min = int(float(self.DA1min_text.toPlainText()) * 1000 / Voltage_transcode)
        da1_max = int(float(self.DA1max_text.toPlainText()) * 1000 / Voltage_transcode)
        data_da1_minmax = hex((0xe2 << 32) | (da1_min << 16) | (da1_max << 0))
        data_da1_minmax = data_da1_minmax[2:]
        byte_data_da1_minmax = bytes.fromhex(data_da1_minmax)
        # E8 00 00 step
        da1_step = int(float(self.DA1step_text.toPlainText()) * 1000 / Voltage_transcode)
        data_da1_step = hex((0xe8 << 32) | (0 << 16) | (da1_step << 0))
        data_da1_step = data_da1_step[2:]
        byte_data_da1_step = bytes.fromhex(data_da1_step)

        # 配置发送
        # 清空接收缓冲区
        if self.com.isOpen():
            self.com.clear()  # 使用 clear() 可以清空输入和输出缓冲区
        else:
            print("串口未打开！")
        # 发送 #
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.msg_log.insertPlainText(f'时间: {current_time}')
        self.msg_log.insertPlainText('\n')
        self.Com_Send_Data(byte_data_f_scan_code)
        self.Com_Send_Data(byte_data_f_scan_dac_code)
        self.Com_Send_Data(byte_data_f_scan_pct_code)

        self.Com_Send_Data(byte_ad_threshold)

        self.Com_Send_Data(byte_data_da2_minmax)
        self.Com_Send_Data(byte_data_da2_step)
        # self.Com_Send_Data(byte_data_da2_delta)

        self.Com_Send_Data(byte_data_da0_minmax)
        self.Com_Send_Data(byte_data_da0_step)

        self.Com_Send_Data(byte_data_da1_minmax)
        self.Com_Send_Data(byte_data_da1_step)

        ### 接收返回数据 ###
        QTimer.singleShot(1000, self.Com_Receive_Data)
        self.msg_log.insertPlainText('\n')
        self.msg_log.insertPlainText('配置结束，等待开启系统...\n\n')

    # 串口接收数据
    def Com_Receive_Data(self):
        #correct_ret =
        try:
            rxData = bytes(self.com.readAll())
        except:
            QMessageBox.critical(self, '严重错误', '串口接收数据错误')
        #if(rxData == )
        self.msg_log.insertPlainText(f'返回数据: {rxData}\n\n')

    # 关闭按钮按下
    def Com_Close_Button_clicked(self):
        self.com.close()
        self.close_serial.setEnabled(False)
        self.open_serial.setEnabled(True)
        self.refresh_port.setEnabled(True)
        self.ports_list.setEnabled(True)
        # self.Com_Baud_Combo.setEnabled(True)
        self.Com_isOpenOrNot_Label.setText('  已关闭')
        self.msg_log.insertPlainText("串口关闭")
        self.msg_log.insertPlainText('\n')

    # 系统关闭按钮按下
    def Sys_Close_Button_clicked(self):
        sys_close = hex((0xee << 32) | (0x11 << 24) | (0xee << 16) | (0x11 << 8) | (0xee << 0))
        sys_close = sys_close[2:]
        byte_sys_close = bytes.fromhex(sys_close)
        self.Com_Send_Data(byte_sys_close)
        ### 接收返回数据 ###
        QTimer.singleShot(500, self.Com_Receive_Data)
        self.send_open_sys.setEnabled(True)
        self.send_close_sys.setEnabled(True)

    # 系统打开按钮按下
    def Sys_Open_Button_clicked(self):
        sys_open = hex((0x55 << 32) | (0x33 << 24) | (0x55 << 16) | (0x33 << 8) | (0x55 << 0))
        sys_open = sys_open[2:]
        byte_sys_open = bytes.fromhex(sys_open)
        self.Com_Send_Data(byte_sys_open)
        self.send_open_sys.setEnabled(False)
        self.send_close_sys.setEnabled(True)
        ### 开启UDP接收 ###
        self.Udp_open_after_sys_start()
        ### 数据接收成功--关闭系统 ###
        self.send_open_sys.setEnabled(True)
        self.send_close_sys.setEnabled(True)
        # QTimer.singleShot(1000, self.Sys_Close_Button_clicked)

    # 建立UDP连接
    def Udp_open_after_sys_start(self):
        try:
            # 获取并打印输入
            local_ip = self.local_ip_text.toPlainText()
            local_port = self.local_port_text.toPlainText()

            self.msg_log.insertPlainText(f"Local IP: {local_ip}\n")
            self.msg_log.insertPlainText(f"Local Port: {local_port}\n")
            # 输入有效性检查
            import socket
            # 检查IP地址格式
            socket.inet_aton(local_ip)  # 对于IPv4地址
            # 检查端口号
            local_port = int(local_port)
            if local_port < 1 or local_port > 65535:
                raise ValueError("Port number must be between 1 and 65535.")
            # 实例化UDP套接字
            self.sock = QUdpSocket(self)
            # 使用QHostAddress转换IP地址
            host_address = QHostAddress(local_ip)
            # 绑定UDP套接字
            if not self.sock.bind(host_address, local_port):
                raise Exception("Failed to bind UDP socket.")
            self.sock.readyRead.connect(self.read_data_slot)
            self.msg_log.insertPlainText("UDP socket opened successfully.\n")
        except socket.error as e:
            print(f"Invalid address: {e}")
            self.msg_log.insertPlainText("Invalid IP address format.\n")
        except ValueError as e:
            print(f"Invalid input: {e}")
            self.msg_log.insertPlainText(f"Invalid port: {e}\n")
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.msg_log.insertPlainText(f"Error: {e}\n")

    # 数据读取操作
    def read_data_slot(self):
        freq_value = self.Freq_set.toPlainText().strip()  # 获取并去除空格
        freq_value = int(freq_value) # 单位:kHz
        time_per_node = (1000/freq_value)/1000000 # 单位:s
        # 计算需要接收的数据量 # # 计算数据报的数量 #
        counter_to_time = int(self.local_storage_time.toPlainText()) * freq_value * 20
        using_counter = 0
        storage_array = []
        while using_counter < counter_to_time:
            if self.sock.hasPendingDatagrams():
                datagram, host, port = self.sock.readDatagram(self.sock.pendingDatagramSize())
                # tmp_str = datagram.hex()
                # print(tmp_str)
                try:
                    # message = 'Received info: \nHost: {}\nPort: {}\n\n'.format(host.toString(), port)
                    for i in range(1,51,1): # 1234 XXXX XXXX 5678 XXXX XXXX XXXX XXXX
                        single_msg = datagram[(i - 1)*16: i*16]
                        node_num_t   = float(int.from_bytes(single_msg[2:6], byteorder='big') * time_per_node) # 单位:s
                        node_AD0   = float(int.from_bytes(single_msg[8:10],  byteorder='big') * 5 / 0xffff) # 单位:V
                        node_DA2   = float(int.from_bytes(single_msg[10:12], byteorder='big') * 5 / 0xffff)
                        node_DA0   = float(int.from_bytes(single_msg[12:14], byteorder='big') * 5 / 0xffff)
                        node_DA1   = float(int.from_bytes(single_msg[14:16], byteorder='big') * 5 / 0xffff)
                        storage_array.append([node_num_t,node_AD0,node_DA2,node_DA0,node_DA1])
                    using_counter = using_counter + 1
                except Exception as e:
                    print(f"Error decoding datagram: {e}")
        self.sock.close()
        self.msg_log.insertPlainText('数据接收完毕\n\n')
        # 将全部数据写入文件 #
        time_now = datetime.now().strftime('%Y%m%d-%H%M%S')
        str_file_to_save = self.local_storage_text.toPlainText()
        with open(f"{str_file_to_save}/{time_now}_recv_data.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            # 先写入columns_name
            writer.writerow(["time/s", "ad/V", "da2/V", "da0/V", "da1/V"])
            # 写入多行用writerows
            non_empty_rows = [row for row in storage_array if row]
            writer.writerows(non_empty_rows)
        self.msg_log.insertPlainText('数据存储完毕\n\n')
        self.msg_log.insertPlainText(f'数据存储位置:{str_file_to_save}/{time_now}_recv_data.csv"\n\n')
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())