## 串口实验

主要简介 EC600S  串口硬件资源，  介绍 quecpython串口 API，  以及实现一个 demo程序 展示怎样使用串口。

### 硬件资源 

EC600 包含了 4 个串口外设，  分别命名为

- DEBUG PORT 

- BT PORT 

- MAIN PORT 

- USB CDC PORT 

  

### 软件资源 

#### 创建 uart 对象   - uart

> **uart = UART(UART.UARTn, buadrate, databits, parity, stopbits, flowctl) **

| 参数     | 类型 | 说明                                                         |
| -------- | ---- | ------------------------------------------------------------ |
| UARTn    | int  | 端口号   EC600SCN平台,UARTn作用如下：   <br>UART0 - DEBUG PORT<br/>UART1 – BT PORT<br/>UART2 – MAIN PORT<br/>UART3 – USB CDC PORT |
| buadrate | int  | 波特率，常用波特率都支持，如4800、9600、19200、<br/>38400、57600、115200、230400等 |
| databits | int  | 数据位（5~8）                                                |
| parity   | int  | 奇偶校验（0 – NONE，1 – EVEN，2 - ODD）                      |
| stopbits | int  | 停止位（1~2）                                                |
| flowctl  | int  | 硬件控制流（0 – FC_NONE， 1 – FC_HW）                        |



#### 查看 buffer 容量  – any 

> **uart.any() **

功能 ：返回接收缓存器中有多少字节的数据未读。

参数 ： 无 

返回值 ： 返回接收缓存器中有多少字节的数据未读。



#### 读取 buffer – read 

> **uart.read(nbytes)**

功能 ： 从串口读取数据。

参数 ：

| 参数   | 类型 | 说明           |
| ------ | ---- | -------------- |
| nbytes | int  | 要读取的字节数 |

返回值：返回读取的数据。



#### 写数据  – write 

> **uart.write(data) **

功能 ：发送数据到串口。

参数 ：

| 参数 | 类型   | 说明       |
| ---- | ------ | ---------- |
| data | string | 发送的数据 |

返回值：返回发送的字节数。



#### 关闭 uart 对象  – close 

> **uart.close() **

功能 ：关闭串口。

参数 ：无

返回值 ：成功返回整型 0，失败返回整型 -1。 

  

### 实验步骤

#### 实验环境准备

首先将 EC600 开发板上面的 TXD1  和 RXD1，焊上排针  ，使用杜邦线连接到 USB 转串口模块上。

![Quectel-QuecPython串口小实验_01](media/Quectel-QuecPython串口小实验_01.png)

使用另外一个串口终端上位机（比如 xshell）接受消息。 接下来我们将使用 MAIN PORT  串口打印消息。



#### 交互实验

```
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0) #串口1
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
File: timer.py
Project: timer
File Created: Monday, 28th December 2020 2:44:33 pm
Author: chengzhu.zhou
-----
Last Modified: Friday, 8th January 2021 9:19:55 am
Modified By: chengzhu.zhou
-----
Copyright 2021 - 2021 quectel
'''

# refs for http://qpy.quectel.com/wiki/#/zh-cn/api/?id=timer
from machine import Timer
import utime as time


# 创建一个执行函数，并将timer实例传入
num = 0
state = 1


def CallBack(t):
    global num
    global state
    print('num is %d' % num)
    num += 1
    if num > 10:
        print('num > 10, timer exit')
        state = 0
        t.stop()


def main():
    # 创建一个定时器对象
    T = Timer(Timer.Timer1)
    # 设置周期为1秒，
    T.start(period=1000, mode=Timer.PERIODIC, callback=CallBack)   # 启动定时器
    # wait
    while state:
        time.sleep_ms(1)
        pass
    T.stop()   # 结束该定时器实例
    print("The main function has exited")


if __name__ == "__main__":
    main()

```

### 配套代码

[下载代码](code/uart_demo1.py)