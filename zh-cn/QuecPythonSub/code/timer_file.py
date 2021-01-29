import log
from machine import Timer


log.basicConfig(level=log.INFO)  # 设置日志输出级别
Timer_Log = log.getLogger("Quectel")  # 获取logger对象

log_print_num = 5
state = 1
timer0 = Timer(Timer.Timer1)


# 创建一个执行函数，并将timer实例传入
def timer_test(t):
    global log_print_num
    global state
    Timer_Log.info('log_print_num is %d' % log_print_num)
    log_print_num -= 1
    if log_print_num <= 0:
        Timer_Log.info('timer exit')
        state = 0
        timer0.stop()  # 结束该定时器实例

timer0.start(period=1000, mode=timer0.PERIODIC, callback=timer_test)  # 启动定时器

while state:
    pass
