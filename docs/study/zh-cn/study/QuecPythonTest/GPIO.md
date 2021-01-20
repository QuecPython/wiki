## 输入捕获实验

文档主要基于 EC600S 介绍如何使用 QuecPython 的输入捕获，在日常应用中，输入捕获主要用于检测 GPIO 的电平，判断电平的时间长短；或者对于一个规律的 PWM 波形，计算占空比等等。

### 硬件描述

输入捕获主要就是检测 GPIO 口的电平时间，硬件的话，可以参考“ QuecPython GPIO 及中断开发 ”文

档。 

### 实验 1：检测 GPIO 触发时间长短

#### 实验目的

EC600S 的 PIN10 和 PIN11 外接两个按键，一个按键（ PIN10）模拟触发，进行检测，对于短时间的触 发，默认输出短按状态显示，对于长时间的触发，输出长按状态显示，如果超过一定时间的长按，默认溢 出；另外一个按键（ PIN11）用于触发，中断循环。

#### 参考代码

下载 .py 文件到模组运行，代码如下：

```python
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
    timer1 = Timer(Timer.Timer1) #定时器 1
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
```

 [下载代码](code/gpio_check.py)

#### 硬件连接

本文验证 无需外接外设。

#### 运行效果

(1）  打开 QPYcom 运行 gpio_check.py，如下图：

![QuecPython_输入捕获小实验_01](media/QuecPython_输入捕获小实验_01.png)

(2）  运行后，手动按键 1（PIN10）不同时间会输出不同的打印，尝试多次后，可以使用按键 2（PIN11） 中断循环， QPYcom 交互界面输出结果 如下 所示 ：

![QuecPython_输入捕获小实验_02](media/QuecPython_输入捕获小实验_02.png)



### 实验 2：模拟计算 PWM 波占空比

#### 实验目标

利用按键 1，简单模拟 PWM 波，由于计算占空比至少需要两个周期，所以对于按键来说，需要输入两 次触发，两次触发后，计算占空比。



#### 参考代码

下载 .py 文件到模组运行，代码如下：

```
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

```

[下载代码](code/in_capture.py)

#### 硬件连接

本文验证无需外接外设。



#### 运行效果

(1）  打开 QPYcom 运行 in_capture.py，如下图：

![QuecPython_输入捕获小实验_03](media/QuecPython_输入捕获小实验_03.png)

(2）  两次一个循环，计算占空比（如有不足，请指出）。 QPYcom 交互界面输出结果 如下所示： 

```python
import example
>>> example.exec('usr/in_capture.py')
INFO:Quectel:main start

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_num reset

INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num:6ms

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_low_num1:0ms
INFO:Quectel:count_low_num2:12ms
low_ratio: 50.00%

INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num count_low_num1_2 reset

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_num reset

INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num:5ms

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_low_num1:0ms
INFO:Quectel:count_low_num2:13ms
low_ratio: 38.46%
INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num count_low_num1_2 reset

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_num reset

INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num:5ms

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_low_num1:0ms
INFO:Quectel:count_low_num2:13ms
low_ratio: 38.46%

INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num count_low_num1_2 reset

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_num reset

INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num:3ms

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_low_num1:0ms
INFO:Quectel:count_low_num2:27ms
low_ratio: 11.11%

INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num count_low_num1_2 reset

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_num reset

INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num:6ms

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_low_num1:0ms
INFO:Quectel:count_low_num2:17ms
low_ratio: 35.29%
INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num count_low_num1_2 reset

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_num reset

INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num:4ms

INFO:Quectel:GPIO_data:0
INFO:Quectel:count_low_num1:0ms
INFO:Quectel:count_low_num2:13ms
low_ratio: 30.77%

INFO:Quectel:GPIO_data:1
INFO:Quectel:count_high_num count_low_num1_2 reset
```