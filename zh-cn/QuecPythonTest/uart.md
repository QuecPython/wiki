## 串口实验

本片文章主要简介 EC600S 串口硬件资源，介绍 quecpython串口 API， 以及实现一个 demo程序 展示怎样使用串口。

### 硬件资源

EC600 包含了 4 个串口外设，  分别命名为

- DEBUG PORT 

- BT PORT 

- MAIN PORT 

- USB CDC PORT 

  

### 软件资源

#### 创建 uart 对象  – uart

**uart = UART(UART.UARTn, buadrate, databits, parity, stopbits, flowctl)**

| 参数     | 类型 | 说明                                                         |
| -------- | ---- | ------------------------------------------------------------ |
| UARTn    | int  | 端口号   EC600SCN平台,UARTn作用如下：   <br>UART0 - DEBUG PORT<br/>UART1 – BT PORT<br/>UART2 – MAIN PORT<br/>UART3 – USB CDC PORT |
| buadrate | int  | 波特率，常用波特率都支持，如4800、9600、19200、38400、57600、115200、230400等 |
| databits | int  | 数据位（5~8）                                                |
| parity   | int  | 奇偶校验（0 – NONE，1 – EVEN，2 - ODD）                      |
| stopbits | int  | 停止位（1~2）                                                |
| flowctl  | int  | 硬件控制流（0 – FC_NONE， 1 – FC_HW）                        |



#### 查看 buffer 容量  – any

**uart.any()**

功能 ：返回接收缓存器中有多少字节的数据未读

参数 ： 无 

返回值 ： 返回接收缓存器中有多少字节的数据未读



#### 读取 buffer – read

**uart.read(nbytes)**

功能 ： 从串口读取数据

参数 ：

|参数 |类型 |说明 |
| - | - | - |
|nbytes |int |要读取的字节数|
返回值：返回读取的数据



#### 写数据  – write

**uart.write(data)**

功能 ：发送数据到串口

参数 ：

| 参数 | 类型   | 说明       |
| ---- | ------ | ---------- |
| data | string | 发送的数据 |

返回值：返回发送的字节数



#### 关闭 uart 对象  – close

**uart.close() **

功能 ：关闭串口

参数 ：无

返回值 ：成功返回整型 0，失败返回整型 -1 

  

### 实验步骤

#### 实验环境准备

首先将 EC600 开发板上面的 TXD1  和 RXD1，焊上排针  ，使用杜邦线连接到 USB 转串口模块上。

![Quectel-QuecPython串口小实验_01](media/Quectel-QuecPython串口小实验_01.png)

使用另外一个串口终端上位机（比如 xshell）接受消息。 接下来我们将使用 MAIN PORT  串口打印消息。



#### 交互实验

```python
>>> from machine import UART
"""
端口号
EC100YCN平台与EC600SCN平台,UARTn映射如下：
UART0 - DEBUG PORT
UART1 – BT PORT
UART2 – MAIN PORT
UART3 – USB CDC PORT
"""
>>> uart1 = UART(UART.UART2, 115200, 8, 0, 1, 0) 
>>> uart1.any()
10
>>> uart1.read(5)
b’12345’
>>> uart1.any()
5
```



### 实验代码

```python
'''
File: example_uart_base.py.py
Project: uart
File Created: Wednesday, 23rd December 2020 3:33:56 pm
Author: chengzhu.zhou
-----
Last Modified: Wednesday, 23rd December 2020 3:34:15 pm
Modified By: chengzhu.zhou
-----
Copyright 2020 - 2020 quectel
'''

from machine import UART
import utime as time
"""
端口号
EC100YCN平台与EC600SCN平台,UARTn映射如下：
UART0 - DEBUG PORT
UART1 – BT PORT
UART2 – MAIN PORT
UART3 – USB CDC PORT
"""


def main():
    """
    config uart Baud rate as 115200,data bits as 8bit, Do not use parity,
    Stop bit as 0bit,Do not use Flow control，
    UART(UART.UARTn, buadrate, databits, parity, stopbits, flowctl)
    """
    uart = UART(UART.UART2, 115200, 8, 0, 1, 0)
    # write string
    delay = 100
    for i in range(2):
        # write string
        uart.write("hello world\r\n")
        # write string and & integer
        uart.write("delay num as {0}ms\r\n".format(delay))
        # write float
        uart.write("π as {0}\r\n".format(3.14159))
        # read something
        read_btyes = 6
        uart.write("please input {0} bytes:\r\n".format(read_btyes))
        while True:
            if uart.any() > read_btyes:
                break
            else:
                time.sleep_ms(10)
        # !!! Before reading buffer, please make sure there is data in buffer
        input_date = uart.read(read_btyes)
        uart.write("The data you entered is {0}\r\n".format(input_date))
        time.sleep_ms(delay)

if __name__ == "__main__":
    main()


```

### 配套代码


<!-- * [下载代码](code/uart_demo1.py) -->
 <a href="zh-cn/QuecPythonTest/code/uart_demo1.py" target="_blank">下载代码</a>