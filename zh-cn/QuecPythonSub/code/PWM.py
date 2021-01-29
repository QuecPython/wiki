from misc import PWM
import utime

pwm = PWM(PWM.PWM5, 10, 20)
pwm.open()

highTime = 10
dir = 1

while 1:
    if dir:
        highTime += 2
        if highTime >= 20:
            dir = 0
    else:
        highTime -= 2
        if highTime <= 2:
            dir = 1
    PWM(PWM.PWM5, highTime, 20)
    utime.sleep_ms(100)