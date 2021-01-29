# 实验1：	跑马灯
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


LED1 = Pin.GPIO1  # 定义LED引脚
LED2 = Pin.GPIO2  # 定义LED引脚
LED3 = Pin.GPIO3  # 定义LED引脚
LED4 = Pin.GPIO4  # 定义LED引脚
LED5 = Pin.GPIO5  # 定义LED引脚


def IO_On(gpioX):  # 某个引脚置0
    GPIO_Write(gpioX, 0)  # 调用写函数


def IO_Off(gpioX):  # 某个引脚置1
    GPIO_Write(gpioX, 1)  # 调用写函数


def IO_All_Off():  # 全部引脚置1
    IO_Off(LED1)
    IO_Off(LED2)
    IO_Off(LED3)
    IO_Off(LED4)
    IO_Off(LED5)


def main():
    while True:
        IO_All_Off()  # 灭
        IO_On(LED1)  # 亮
        utime.sleep_ms(200)  # 延时
        IO_All_Off()  # 灭
        IO_On(LED2)  # 亮
        utime.sleep_ms(200)  # 延时
        IO_All_Off()  # 灭
        IO_On(LED3)  # 亮
        utime.sleep_ms(200)  # 延时
        IO_All_Off()  # 灭
        IO_On(LED4)  # 亮
        utime.sleep_ms(200)  # 延时
        IO_All_Off()  # 灭
        IO_On(LED5)  # 亮
        utime.sleep_ms(200)  # 延时


if __name__ == "__main__":
    main()
