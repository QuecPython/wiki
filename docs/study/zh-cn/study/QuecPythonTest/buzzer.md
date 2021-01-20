## 蜂鸣器实验

### 基本概述

本片文章主要简介使用EC600S GPIO 来驱动外部蜂鸣器模块。

#### 硬件资源

淘宝链接：
<https://detail.tmall.com/item.htm?id=41251333522&spm=2013.1.1997525049.3.ffec2c43XoQVcT>

淘宝： 无源频率可控

![](media/8aab25aa717d0a0be57094d08fc53b28.png)

### 使用说明

无源蜂鸣器通过PWM开关三极管驱动。 我们只需要电源，以及2k~5K 的pwm方波即可。

### 实验步骤

#### 实验环境准备

 **引脚连接**

按照下面的链接方式链接引脚

| **蜂鸣器** | **EC600开发板**   | **对应的函数标号** |
| ---------- | ----------------- | ------------------ |
| IO (PWM)   | GPIO81 (引脚号16) | PWM2               |
| VCC        | 5_5V电源          | 无                 |
| GND        | 地                | 无                 |

#### 实验代码

```
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

# API https://python.quectel.com/wiki/#/zh-cn/api/?id=pwm

# 蜂鸣器模块 https://detail.tmall.com/item.htm?id=41251333522
无源蜂鸣器-频率可控版

"""

pwm0 = PWM(PWM.PWMn,PWM.ABOVE_xx,highTime,cycleTime)

注：EC600SCN平台，支持PWM0-PWM3，对应引脚如下：

PWM0 – 引脚号52

PWM1 – 引脚号53

PWM2 – 引脚号70

PWM3 – 引脚号69

"""

"""

| 蜂鸣器 | EC600开发板 | 对应的函数标号 |

| ---------- | ------------------ | ------- |

| IO (PWM) | GPIO81 (引脚号16) | PWM2 |

| VCC | 3_3V电源 | 无 |

| GND | 地 | 无 |

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

				# 建议输出2000~5000HZ 的PWM波形

				# 范围可以自己选择， 0~1

				duty_cycle = random.uniform(0.1, 0.8)

				HZ = random.randint(2000, 5000)

				outputpwm(HZ, duty_cycle, 500)

				time.sleep_ms(1500)

		pass



if __name__ == "__main__":

		# creat a thread Check key status

		test_Buzzer()

将代码下载运行，可以听到蜂鸣器产生随机的声音。
```

### 配套代码

[下载代码](code/pwm_buzzer.py)