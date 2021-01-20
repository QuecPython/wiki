import utime
import log
import _thread
from machine import ExtInt
from machine import Pin

count_num = 0
low_ratio = 0
count_high_num = 0
count_low_num1 = 0
count_low_num2 = 0

log.basicConfig(level=log.INFO)
Testlog = log.getLogger("Quectel")
gpio1 = Pin(Pin.GPIO1, Pin.IN, Pin.PULL_DISABLE, 0)

def fun(args):
    gpio1_data = gpio1.read()
    global count_low_num1
    global count_low_num2
    global count_high_num
    global low_ratio
    global count_num
    if gpio1_data == 0:
        Testlog.info("GPIO_data:{}".format(gpio1_data))
        if count_low_num1 == 0 and count_high_num == 0 and count_low_num1 != count_num:
            count_num = 0
            count_low_num1 = count_num
            Testlog.info("count_num reset")
        elif count_high_num != 0:
            if count_low_num2 == 0:
                count_low_num2 = count_num
                Testlog.info("count_low_num1:{}ms".format(count_low_num1))
                Testlog.info("count_low_num2:{}ms".format(count_low_num2))
                low_ratio = (count_high_num-count_low_num1)/(count_low_num2-count_low_num1)
                print('low_ratio: {:.2%}'.format(low_ratio))
            else:
                pass
        else:
            pass
    elif gpio1_data == 1:
        Testlog.info("GPIO_data:{}".format(gpio1_data))
        if count_low_num2 == 0 and count_num != 0 and count_high_num != count_num:
            count_high_num = count_num
            Testlog.info("count_high_num:{}ms".format(count_high_num))
        elif count_low_num2 != 0 and count_high_num != count_num:
            count_low_num1 = 0
            count_low_num2 = 0
            count_high_num = 0
            Testlog.info("count_high_num count_low_num1_2 reset")
        else:
            pass
    else:
        pass
def extint_gpio1():
    Testlog.debug("thread start")
    global extint
    extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, fun)

def time_num():
    global count_num
    while True:
        utime.sleep_us(1)
        count_num += 1

if __name__ == "__main__":
    Testlog.info("main start")
    _thread.start_new_thread(extint_gpio1, ())
    _thread.start_new_thread(time_num,())
    while True:
        pass
