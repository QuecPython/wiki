
# 参考 https://python.quectel.com/wiki/#/zh-cn/api/?id=power 文档
# http://qpy.quectel.com/wiki/#/zh-cn/api/?id=timer
# 使用定时器，定时关机
from machine import Timer
from misc import Power
import utime as time


def CallBack(t):
    Power.powerDown()


def test_power_module():
    # 创建一个定时器对象
    T = Timer(Timer.Timer1)
    # period 单位为 ms
    T.start(period=5000, mode=Timer.ONE_SHOT, callback=CallBack)   # 启动定时器
    # wait
    while True:
        time.sleep_ms(1)
    print("The main function has exited")


if __name__ == "__main__":
    test_power_module()
