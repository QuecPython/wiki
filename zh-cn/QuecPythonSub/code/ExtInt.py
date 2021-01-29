from machine import ExtInt
import utime


def fun1(args):
    print(args)
    print("1111111111111111111111")


def fun2(args):
    print(args)
    print("222222222222222222222")


extint1 = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun1)
extint1.enable()

extint2 = ExtInt(ExtInt.GPIO2, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun2)
extint2.enable()

while True:
    utime.sleep_ms(200)
    print("。。。。。。。。。")
