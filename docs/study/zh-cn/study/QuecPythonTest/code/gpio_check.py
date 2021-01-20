import log
import _thread
import utime
from machine import Pin
from machine import Timer
from machine import ExtInt


Time_mun_low = 0
key_time = 0
key_short = 10
key_log = 500
key_out = 3000
state = 1
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_PU, 1)
gpio2 = Pin(Pin.GPIO2, Pin.OUT, Pin.PULL_PU, 1)
log.basicConfig(level=log.NOTSET)
KEY_log = log.getLogger("KEY")
def Time1_fun(args):
    global Time_mun_low
    Time_mun_low += 1

def I_C_fun(args):
    global Time_mun_low
    global key_time
    if gpio1.read() == 0:
        Time_mun_low = 0
    elif gpio1.read() == 1:
        key_time = Time_mun_low
    else:
        pass

def Input_Capture():
    KEY_log.debug("I_C start!")
    global state
    global key_time
    timer1 = Timer(Timer.Timer1) #定时器1
    timer1.start(period=1, mode=timer1.PERIODIC, callback=Time1_fun)
    extint1 = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_RISING_FALLING, ExtInt.PULL_PU, I_C_fun)
    extint1.enable()
    while True:
        if gpio2.read() == 0:
            utime.sleep_ms(10)
            if gpio2.read() == 0:
                KEY_log.info("GPIO2 levels:{}".format(gpio2.read()))
                break
        if key_time != 0:
            KEY_log.info("key_time:{}ms".format(key_time))
            if key_time <= key_short:
                pass
            elif key_short < key_time <= key_log:
                print(" key short input ")
            elif key_log < key_time <= key_out:
                print(" key log input ")
            else:
                print(" key out ")
                pass
            key_time = 0
    state = 0
    KEY_log.debug("I_C end!")
if __name__ == "__main__":
    KEY_log.info("in_capture thread start")
    _thread.start_new_thread(Input_Capture, ())
    while True:
        if state == 0:
            KEY_log.info("in_capture thread end")
            break
        else:
            pass