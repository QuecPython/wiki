# QuecPython 小实验

***以上实验均可在模块中直接运行***

***

## 跑马灯实验



## 蜂鸣器实验

### 基本概述

本片文章主要简介使用EC600S GPIO 来驱动外部蜂鸣器模块。

#### 硬件资源

淘宝链接：
<https://detail.tmall.com/item.htm?id=41251333522&spm=2013.1.1997525049.3.ffec2c43XoQVcT>

淘宝： 无源频率可控

![](C:\Users\rivern.yuan\Desktop\new wiki\付俊臣\小实验文档\Quectel-QuecPython蜂鸣器小实验\media\8aab25aa717d0a0be57094d08fc53b28.png)

### 使用说明

无源蜂鸣器通过PWM开关三极管驱动。 我们只需要电源，以及2k\~5K 的pwm方波即可。

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

\-----

Last Modified: Wednesday, 30th December 2020 5:02:48 pm

Modified By: chengzhu.zhou

\-----

Copyright 2020 - 2020 quectel

'''

from misc import PWM

import utime as time

import urandom as random

import log

\# API https://python.quectel.com/wiki/\#/zh-cn/api/?id=pwm

\# 蜂鸣器模块 https://detail.tmall.com/item.htm?id=41251333522
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

\| 蜂鸣器 \| EC600开发板 \| 对应的函数标号 \|

\| ---------- \| ------------------ \| ------- \|

\| IO (PWM) \| GPIO81 (引脚号16) \| PWM2 \|

\| VCC \| 3_3V电源 \| 无 \|

\| GND \| 地 \| 无 \|

"""

buzzer_log = log.getLogger("buzzer_test")



\# Duration 为 ms

def outputpwm(HZ, duty_cycle, Duration):

\# 将HZ 转化为 10us 级别

​		cycleTime = int((10000000/HZ)/10)

​		highTime = int(cycleTime \* duty_cycle)

​		buzzer\_log.debug(

​				"""out put pin70 cycleTime {0} \* 10us,

​				highTime {1} \* 10us, Duration of {2}"""

​				.format(cycleTime, highTime, Duration))

​				pwm1 = PWM(PWM.PWM2, PWM.ABOVE_10US, highTime, cycleTime)

​		pwm1.open()

​		time.sleep\_ms(Duration)

​		pwm1.close()

​		pass



def test\_Buzzer():

​		log.basicConfig(level=log.DEBUG)

​		for i in range(10):

​				# 建议输出2000\~5000HZ 的PWM波形

​				# 范围可以自己选择， 0\~1

​				duty_cycle = random.uniform(0.1, 0.8)

​				HZ = random.randint(2000, 5000)

​				outputpwm(HZ, duty_cycle, 500)

​				time.sleep\_ms(1500)

​		pass



if \__name_\_ == "__main__":

​		# creat a thread Check key status

​		test\_Buzzer()

将代码下载运行，可以听到蜂鸣器产生随机的声音。
```



## 按键输入实验




## 串口实验

* <a href="串口实验.pdf" target="_blank">点此下载 PDF</a>

<object data="串口实验.pdf" type="application/pdf" style="min-height:100vh;width:100%">
    <p>It appears you don't have a PDF plugin for this browser.
    No biggie... you can <a href="串口实验.pdf">click here to download the PDF file.</a></p>
</object>

<!-- ## 外部中断实验

## 独立看门狗实验

## 定时器中断实验 -->

## PWM输出实验

* <a href="PWM输出实验.pdf" target="_blank">点此下载 PDF</a>

<object data="PWM输出实验.pdf" type="application/pdf" style="min-height:100vh;width:100%">
    <p>It appears you don't have a PDF plugin for this browser.
    No biggie... you can <a href="PWM输出实验.pdf">click here to download the PDF file.</a></p>
</object>

<!--## LCD触摸屏显示实验

## 待机唤醒实验

## RTC实验

## 内部温湿度传感器实验 -->

## 光敏传感器实验

* <a href="光敏传感器实验.pdf" target="_blank">点此下载 PDF</a>

<object data="光敏传感器实验.pdf" type="application/pdf" style="min-height:100vh;width:100%">
    <p>It appears you don't have a PDF plugin for this browser.
    No biggie... you can <a href="光敏传感器实验.pdf">click here to download the PDF file.</a></p>
</object>

<!-- ## 加速度传感器实验

## ADC实验

## IIC 实验

## SPI 实验

## 音频播放实验 -->

## 录音实验

* <a href="录音实验.pdf" target="_blank">点此下载 PDF</a>

<object data="录音实验.pdf" type="application/pdf" style="min-height:100vh;width:100%">
    <p>It appears you don't have a PDF plugin for this browser.
    No biggie... you can <a href="录音实验.pdf">click here to download the PDF file.</a></p>
</object>

<!-- ## 输入捕获实验

## 步进电机驱动实验

## DMA实验

## PWM DAC实验

## 继电器实验 -->
