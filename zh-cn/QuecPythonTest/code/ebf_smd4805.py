'''
File: EBF_SMD4805.py
Project: others
File Created: Wednesday, 6th January 2021 2:16:52 pm
Author: chengzhu.zhou
-----
Last Modified: Wednesday, 6th January 2021 2:56:42 pm
Modified By: chengzhu.zhou
-----
Copyright 2021 - 2021 quectel
'''

"""
参考资料
1. API
https://python.quectel.com/wiki/#/zh-cn/api/?id=pwm
https://python.quectel.com/wiki/#/zh-cn/api/?id=pin
2. 模块资料
https://item.taobao.com/item.htm?ft=t&id=543053172983
步进电机驱动器 + 42步进电机
2.1 模块开发资料
https://ebf-products.readthedocs.io/zh_CN/latest/module/motor/ebf-msd4805.html
"""

"""
引脚连接
| 电机         | EC600开发板           | 对应的函数标号 |
| ---------- | ------------------ | ------- |
| ENA- （GPIO） | GPIO81   (引脚号16)   | GPIO7   |
| DIR- (GPIO) | GPIO77 （引脚号15）     | GPIO6   |
| PUL- （PWM）  | GPIO2_1V8  (引脚号70) | PWM2    |
| ENA+   DIR+  PUL+ |       1V8(电源)        |  无      |
"""




from misc import PWM
from machine import Pin
import utime as time
import urandom as random
import log
def delay_500us():
    for i in range(600):
        pass


def delay_250us():
    for i in range(310):
        pass


ENABLE_MOTOR = 0x1
DISABLE_MOTOR = 0x0

DIR_CLOCKWISE = 0x1
DIR_ANTI_CLOCKWISE = 0x0


class ebf_smd4805():

    dev_log = None

    # 步进电机的参数
    sm_para_step = None  # 步进角度
    # 控制器的参数
    env_pin = None  # 使能引脚
    dir_pin = None  # 方向引脚
    pul_pwm = None  # 脉冲输出引脚
    ctrl_divstep = None  # 细分参数，具体请参考控制器手册

    def init(self, step, divstep):
        self.dev_log = log.getLogger("ebf_smd4805")
        self.env_pin = Pin(Pin.GPIO7, Pin.OUT, Pin.PULL_DISABLE, 0)
        self.dir_pin = Pin(Pin.GPIO6, Pin.OUT, Pin.PULL_DISABLE, 0)
        # 配置电机的参数
        self.sm_para_step = step
        # 配置控制器的参数
        self.ctrl_divstep = divstep

    def reset(self):
        self.env_pin.write(DISABLE_MOTOR)
        self.dir_pin.write(DIR_ANTI_CLOCKWISE)
        if self.pul_pwm is not None:
            self.pul_pwm.close()

    # 根据频率 初始化PWM
    def outputpwm(self, HZ, duty_cycle):
        # 将HZ 转化为 us 级别
        cycleTime = int(1000000/HZ)
        highTime = int(cycleTime * duty_cycle)
        return highTime, cycleTime

    # 根据速度,设置PWM的输出
    def enable_pwm(self, speed):
        # 1. 首先根据步进电机的步进角度，计算旋转一圈需要多少个脉冲
        Count_pulse = int(360/self.sm_para_step)
        self.dev_log.debug("sm motor step as {0}".format(Count_pulse))
        # 2. 根据控制器的细分参数，计算控制器控制步进电机旋转一圈，需要多少的脉冲
        Count_pulse = int(Count_pulse * self.ctrl_divstep)
        # 3. 最后计算出1秒旋转speed圈,需要多少个脉冲 , 换句话说 就是频率
        Count_pulse = int(Count_pulse * speed)
        # 4. 初始化PWM, 默认占空比%50
        highTime, cycleTime = self.outputpwm(Count_pulse, 0.1)
        self.dev_log.debug(
            """config  frequency  is {0}HZ,cycleTime {1}us, hightime {2}us"""
            .format(Count_pulse, cycleTime, highTime))
        self.pul_pwm = PWM(PWM.PWM2, PWM.ABOVE_10US,
                           int(highTime), int(cycleTime))
        self.pul_pwm.open()
        pass

    def disable_pwm(self):
        self.pul_pwm.close()
        pass

    # speed 为速度， 每秒多少圈
    # Duration 为持续时间， ms
    # dir 表示方向
    def run(self, speed, Duration, dir=DIR_CLOCKWISE):
        self.dir_pin.write(dir)
        self.dev_log.info(
            "Configure the motor to rotate {0} revolutions per second".format(speed))
        self.enable_pwm(speed)
        self.env_pin.write(1)
        # delay
        for i in range(int(Duration * 4)):
            delay_250us()
        self.env_pin.write(0)

        self.reset()
        pass


def test_ebf_smd4805():
    log.basicConfig(level=log.DEBUG)
    # log.basicConfig(level=log.INFO)
    ebf_smd4805_dev = ebf_smd4805()
    ebf_smd4805_dev.init(step=1.8, divstep=2)
    for i in range(2, 10):
        ebf_smd4805_dev.run(i, Duration=1000, dir=DIR_CLOCKWISE)
    print("test_ebf_smd4805  Function exit,!!!")
    pass


if __name__ == "__main__":
    # creat a thread Check key status
    test_ebf_smd4805()
