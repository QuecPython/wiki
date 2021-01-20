'''
File: pwm_demo.py
Project: pwm
File Created: Wednesday, 23rd December 2020 11:21:14 am
Author: chengzhu.zhou
-----
Last Modified: Tuesday, 29th December 2020 4:38:49 pm
Modified By: chengzhu.zhou
-----
Copyright 2020 - 2020 quectel
'''


from misc import PWM
import utime as time
"""
PWM号
注：EC100YCN平台，支持PWM0-PWM5，对应引脚如下：
PWM0 – 引脚号19
PWM1 – 引脚号18
PWM2 – 引脚号16
PWM3 – 引脚号17
PWM4 – 引脚号23
PWM5 – 引脚号22
注：EC600SCN平台，支持PWM0-PWM5，对应引脚如下：
PWM0 – 引脚号52
PWM1 – 引脚号53
PWM2 – 引脚号57
PWM3 – 引脚号56
PWM4 – 引脚号70
PWM5 – 引脚号69
"""


def main():
    # config cysle 200ms , config high voltage 100ms ,
    # in other words , config duty cycle as %50
    pwm_obj = PWM(PWM.PWM0, PWM.ABOVE_MS, 100, 200)
    #
    pwm_obj.open()
    time.sleep(10)
    pwm_obj.close()
    print("pwm Demo run successfully")
    pass


if __name__ == "__main__":
    main()
