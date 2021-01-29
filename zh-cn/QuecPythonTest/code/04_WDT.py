# 实验1：	独立看门狗实验
# API资料参考连接：  https://python.quectel.com/wiki/#/zh-cn/api/?id=wdt


from machine import WDT
import utime

wdt = None  # 定义全部变量


def Watchdog():  # 2秒钟内调用喂狗函数，否则系统复位
    global wdt  # 声明全部变量
    if wdt is None:
        wdt = WDT(2)  # 启动看门狗，间隔时长 单位 秒
    wdt.feed()  # 喂狗


def func_1():
    utime.sleep_ms(1000)  # 延时1秒
    print('功能函数 1')


def func_2():
    utime.sleep_ms(1000)  # 延时1秒
    print('功能函数 2')


def func_3():
    utime.sleep_ms(1000)  # 延时1秒
    print('功能函数 3')
    Watchdog()  # 2秒钟内调用喂狗函数
    utime.sleep_ms(1000)  # 延时1秒
    print('功能函数 3_2')


def func_4():
    utime.sleep_ms(1000)
    print('功能函数 4')
    Watchdog()  # 2秒钟内调用喂狗函数
    print('尝试在5s后喂狗')
    utime.sleep_ms(5000)  # 延时5秒
    Watchdog()
    print('来不及喂狗，系统已经复位')


def main():
    print('喂狗')
    Watchdog()  # 2秒钟内调用喂狗函数
    func_1()  # 用户程序
    print('喂狗')
    Watchdog()  # 2秒钟内调用喂狗函数
    func_2()  # 用户程序
    print('喂狗')
    Watchdog()  # 2秒钟内调用喂狗函数
    func_3()  # 用户程序
    print('喂狗')
    Watchdog()  # 2秒钟内调用喂狗函数
    func_4()  # 用户程序


if __name__ == "__main__":
    main()
