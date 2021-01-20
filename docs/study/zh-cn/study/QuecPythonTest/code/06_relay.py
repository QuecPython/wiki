# 实验1：	继电器实验
# API资料参考连接：  https://python.quectel.com/wiki/#/zh-cn/api/?id=pin


from machine import Pin
import utime


IOdictRead = {}  # 记录已经初始化的GPIO口
IOdictWrite = {}  # 记录已经初始化的GPIO口


def GPIO_Read(gpioX, Pull=Pin.PULL_DISABLE, level=1):
    if IOdictWrite.get(gpioX, None):
        del IOdictWrite[gpioX]
    gpioIO = IOdictRead.get(gpioX, None)
    if gpioIO:
        return gpioIO.read()
    else:
        IOdictRead[gpioX] = (Pin(gpioX, Pin.IN, Pull, level))
        gpioIO = IOdictRead.get(gpioX, None)
        return gpioIO.read()


def GPIO_Write(gpioX, level, Pull=Pin.PULL_DISABLE):
    if IOdictRead.get(gpioX, None):
        del IOdictRead[gpioX]
    gpioIO = IOdictWrite.get(gpioX, None)
    if gpioIO:
        gpioIO.write(level)
    else:
        IOdictWrite[gpioX] = (Pin(gpioX, Pin.OUT, Pull, level))
        gpioIO = IOdictWrite.get(gpioX, None)
        gpioIO.write(level)


Relay_1 = Pin.GPIO3  # 定义 继电器 引脚
Relay_2 = Pin.GPIO4  # 定义 继电器 引脚


def relayIO_On(gpioX):  # 某个引脚置0
    GPIO_Write(gpioX, 0)


def relayIO_Off(gpioX):  # 某个引脚置1
    GPIO_Write(gpioX, 1)


KEY_1 = Pin.GPIO1  # 定义 按键 引脚
KEY_2 = Pin.GPIO2  # 定义 按键 引脚


def readKey():  # 读取按键，返回按键值
    if (GPIO_Read(KEY_1) == low):  # 判断是否为低电平
        utime.sleep_ms(20)  # 防抖
        if (GPIO_Read(KEY_1) == low):  # 判断是否为低电平
            return KEY_1  # 返回按键值
    elif (GPIO_Read(KEY_2) == low):  # 判断是否为低电平
        utime.sleep_ms(20)  # 防抖
        if (GPIO_Read(KEY_2) == low):  # 判断是否为低电平
            return KEY_2  # 返回按键值
    else:
        return None  # 返回 空


while True:
    if(readKey() == KEY_1):  # 判断是否 KEY_1 被按下
        relayIO_On(Relay_1)  # Relay_1 ON
        relayIO_Off(Relay_2)  # Relay_2 OFF
    elif (readKey() == KEY_1):  # 判断是否 KEY_1 被按下
        relayIO_Off(Relay_1)  # Relay_1 OFF
        relayIO_On(Relay_2)  # Relay_2 ON
