'''
File: External_interrupt.py
Project: button
File Created: Monday, 28th December 2020 3:03:43 pm
Author: chengzhu.zhou
-----
Last Modified: Monday, 28th December 2020 3:03:47 pm
Modified By: chengzhu.zhou
-----
Copyright 2020 - 2020 quectel
'''
from machine import ExtInt
import utime as time
'''
EC600SCN平台引脚对应关系如下：
GPIO1 – 引脚号71
GPIO2 – 引脚号72
GPIO3 – 引脚号73
GPIO4 – 引脚号74
GPIO5 – 引脚号75
GPIO6 – 引脚号76
GPIO7 – 引脚号77
'''
# 参考自  http://qpy.quectel.com/wiki/#/zh-cn/api/?id=extint
state = 2


def callBack(args):
    global state
    print("###interrupt  %d ###" % args)
    state = state - 1


def main():
    # 映射GPIO71的下降沿触发回调函数
    extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, callBack)
    # 等待按键按下，触发
    while state:
        time.sleep_ms(10)
        pass
    # 停止映射外部中断
    extint.disable()
    print("The main function has exited")


if __name__ == "__main__":
    main()
