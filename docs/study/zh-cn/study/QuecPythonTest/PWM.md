## PWM输出实验

本文档主要基于 EC600 介绍如何使用 QuecPython 类库 API 来快速开开发使用 **pwm** 功能。 EC600 拥有   6 个 pwm 外设。  暂时还没有引脚重映射的功能。只能将外设固定对应的引脚使用。

1. PWM0 –  引脚号 52 

1. PWM1 –  引脚号 53 

1. PWM2 –  引脚号 57 

1. PWM3 –  引脚号 56 

1. PWM4 –  引脚号 70 

1. PWM5 –  引脚号 69 

   

### 使用说明

#### pwm 创建对象

示例代码参考以下代码清单：

```
from misc import PWM
pwm0 = PWM(PWM.PWMn,PWM.ABOVE_xx,highTime,cycleTime) 
```

| 参数         | 参数类型      | 参数说明                               |
| ------------ | ------------- | -------------------------------------- |
| PWM.PWMn     | PWM.PWM0      | PWM0                                   |
|              | PWM.PWM1      | PWM1                                   |
|              | PWM.PWM2      | PWM2                                   |
|              | PWM.PWM3      | PWM3                                   |
| PWM.ABOVE_xx | PWM.ABOVE_MS  | ms 级  取值 (0,1023)                   |
|              | PWM.ABOVE_1US | us 级  取值 (0,157)                    |
|              | PWM.ABOVE_10U | Sus 级  取值 (1,1575)                  |
| highTime     | int           | ms 级时：单位 ms<br> us 级时：单位 us  |
| cycleTime    | int           | ms 级时：单位 ms <br/>us 级时：单位 us |

#### pwm.open 打开设备

开启 PWM 输出。 

参数 ： 无 

返回值 ： 成功返回整型 0，失败返回整型 -1。 

#### pwm.cloes  关闭设备 

关闭 PWM 输出。 

参数 ： 无 

返回值 ： 成功返回整型 0，失败返回整型 -1。 



### 代码示例

```python
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

```



代码串讲：   将 PWM0 设备  设置为周期 200ms，  高电平为 100ms 的输出。  运行代码，使用示波器抓取 PWM 0  对应的 52 号引脚电压。可得到如下图案。

![Quectel-QuecPythonPwm输出小实验_01](media/Quectel-QuecPythonPwm输出小实验_01.png)

### 配套代码

[下载代码](code/pwm_demo.py)