from machine import WDT
from machine import Timer

count = 0
def feed(t):
    global count
    count += 1
    if count >= 5:
        print('停止喂狗')
        timer1.stop()
    print('喂狗')
    wdt.feed()


timer1 = Timer(Timer.Timer1)
wdt = WDT(2)  # 启动看门狗，间隔时长 单位 秒
timer1.start(period=1000, mode=timer1.PERIODIC, callback=feed)  # 使用定时器喂狗
