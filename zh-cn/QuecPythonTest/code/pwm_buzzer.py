'''
File: pwm_buzzer.py
Project: pwm
File Created: Wednesday, 30th December 2020 5:02:46 pm
Author: chengzhu.zhou
-----
Last Modified: Wednesday, 30th December 2020 5:02:48 pm
Modified By: chengzhu.zhou
-----
Copyright 2020 - 2020 quectel
'''
from misc import PWM
import utime as time
import urandom as random
import log
#  API https://python.quectel.com/wiki/#/zh-cn/api/?id=pwm
#  蜂鸣器模块 https://detail.tmall.com/item.htm?id=41251333522 无源蜂鸣器-频率可控版
"""
pwm0 = PWM(PWM.PWMn,PWM.ABOVE_xx,highTime,cycleTime)
注：EC600SCN平台，支持PWM0-PWM3，对应引脚如下：
PWM0 – 引脚号52
PWM1 – 引脚号53
PWM2 – 引脚号70
PWM3 – 引脚号69
"""

"""
| 蜂鸣器         | EC600开发板           | 对应的函数标号 |
| ---------- | ------------------ | ------- |
| IO (PWM)	|  GPIO81   (引脚号16)  | PWM2   |
| VCC 		| 3_3V电源    		| 无   	|
| GND  		| 地 				| 无    |
"""
buzzer_log = log.getLogger("buzzer_test")


# Duration 为 ms
def outputpwm(HZ, duty_cycle, Duration):
    # 将HZ 转化为 10us 级别
    cycleTime = int((10000000/HZ)/10)
    highTime = int(cycleTime * duty_cycle)
    buzzer_log.debug(
        """out put pin70 cycleTime {0} * 10us,
         highTime {1} * 10us, Duration of {2}"""
        .format(cycleTime, highTime, Duration))
    pwm1 = PWM(PWM.PWM2, PWM.ABOVE_10US, highTime, cycleTime)
    pwm1.open()
    time.sleep_ms(Duration)
    pwm1.close()
    pass


def test_Buzzer():
    log.basicConfig(level=log.DEBUG)
    for i in range(10):
        #  建议输出2000~5000HZ 的PWM波形
        # 范围可以自己选择， 0~1
        duty_cycle = random.uniform(0.1, 0.8)
        HZ = random.randint(2000, 5000)
        outputpwm(HZ, duty_cycle, 500)
        time.sleep_ms(1500)
    pass


if __name__ == "__main__":
    # creat a thread Check key status
    test_Buzzer()
