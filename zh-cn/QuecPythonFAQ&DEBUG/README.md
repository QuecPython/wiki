# QuecPython FAQ&DEBUG


## QuecPython FAQ&Debug文档

- 详见文档《QuecPython FAQ&Debug文档》

 <a href="zh-cn/QuecPythonFAQ&Debug/QuecPython_FAQ&Debug.pdf" target="_blank">下载PDF</a>

## QuecPython 救砖处理

- 如何解决：详见文档《Quectel QuecPython_QPYcom工具使用说明_V1.0.pdf》

## QuecPython main.py文件使用

- 如何使用main.py&使用过程中问题解决

1. 现象：上传py文件且文件名为main.py到模块后无法任何执行指令（包括上传文件等）

 

1. 导致原因：模块在开机后会自动寻找运行文件名为main.py的脚本文件，如果main.py中存在while，for(,,)这种循环语句，会导致程序阻塞，串口被占用，无法进行其他操作
2. 如何解决：目前版本只能通过重刷固件解决，建议在测试阶段尽量不要使用main.py作为入口文件，可使用start.py或其它命名来手动拉起项目，避免重刷固件。



## QuecPython MQTT连接异常处理

- 导致原因： MQTT服务端会有心跳检测机制，一段时间内设备与云端没有通信活动会主动断开连接

- 尝试解决方向：连接断开是依据配置mqtt时的超时值keepalive，在超出活动时间后会主动断开连接，我们可以根据设置keepalive活动时间使用定时器在活动时间超出前主动向云端发送ping包，服务端返回的数据包无需客户处理。

## QuecPython 驱动安装失败问题解决

- 现象：安装EC100Y-CN 所需驱动Quectel_ASR_Series_UMTS&LTE_Windows_USB_Driver_Customer_V1.0.3.zip 后，发现在 Windows7 下未正常识别出模块的指令交互串口。

- 导致原因：Windows7 下无法使用 Microsoft 的 USB 串行设备驱动程序。

- 如何解决：详见文档《EC100Y-CN_windows7 安装 USB 驱动指令交互串口未识别解决方法 V1.0.pdf》



## QuecPython apn_cfg.json文件解析



