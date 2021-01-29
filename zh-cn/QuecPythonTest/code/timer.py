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
