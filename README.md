# DriverContorl_for_Chem_3Dscan_FPGA
用于三维电化学成像的FPGA开发板的控制上位机（串口+网口）

### 完成功能

1、使用串口通讯完成指令发送与接收（包含帧头与返回值校验，可设置系统的各项指标）

2、开启系统后接收UDP协议回传回来的监测数据（固定长度数据报，接收固定数据报数量）

### 文件说明

UI_upper.ui 界面UI文件；

serialport 功能主函数；

UI_upper.py 界面UI的py文件；

CMD_Pyinstall.txt 一键打包命令；

### 开发平台

IDE：PyCharm + PyQt5库

语言：Python 3.9

### 参考资料

###### 开发软件与库的配置（如何转换ui->py，安装pyqt5库等）：https://zhuanlan.zhihu.com/p/469526603

###### 串口参考github库：https://github.com/Oslomayor/PyQt5-SerialPort-Stable.git