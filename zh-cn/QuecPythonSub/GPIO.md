# EC600S GPIO及IO中断开发

文档主要基于EC600S介绍如何使用QuecPython_GPIO，GPIO通常用于连接驱动LED、蜂鸣器、继电器等等，同样也可以用来读取KEY、开关状态、外部IC的引脚电平状态等等。通过本文你将了解到GPIO的所有设置参数及使用方法。

##  硬件描述

目前开放共10个GPIO，其他的GPIO逐渐开放，各个GPIO口连接位置如下表所示：

GPIO1 – 模组的Pin10 
GPIO2 – 模组的Pin11 
GPIO3 – 模组的Pin12 
GPIO4 – 模组的Pin13 
GPIO5 – 模组的Pin14 
GPIO6 – 模组的Pin15 
GPIO7 – 模组的Pin16 
GPIO8 – 模组的Pin39 
GPIO9 – 模组的Pin40 
GPIO10 – 模组的Pin48

![](media/9351c08c142de93cfa88095688ab7535.png)

##  软件设计

### 创建gpio对象

gpio = Pin(GPIOn, direction, pullMode, level)

函数原型：Pin(GPIOn, direction, pullMode,level)，返回一个pgio对象，用于操作读写IO状态。

| 参数      | 类型 | 说明                                                         |
| --------- | ---- | ------------------------------------------------------------ |
| GPIOn     | int  | GPIO1 – 模组的Pin10  GPIO2 – 模组的Pin11<br/> GPIO3 – 模组的Pin12  GPIO4 – 模组的Pin13 <br/>GPIO5 – 模组的Pin14  GPIO6 – 模组的Pin15 <br/>GPIO7 – 模组的Pin16  GPIO8 – 模组的Pin39 <br/>GPIO9 – 模组的Pin40  GPIO10 – 模组的Pin48 |
| direction | int  | IN – 输入模式，OUT – 输出模式                                |
| pullMode  | int  | PULL_DISABLE – 浮空模式<br/> PULL_PU – 上拉模式 <br/>PULL_PD – 下拉模式 |
| level     | int  | 0 - 设置引脚为低电平, 1- 设置引脚为高电平                    |

### 获取Pin脚电平

state= gpio.read()

函数原型：read()，返回对应创建gpio对象的Pin脚输入电平状态。

| 参数  | 类型 | 说明             |
|-------|------|------------------|
| state | int  | 0低电平，1高电平 |

### 设置Pin脚电平

ret = gpio.Pin.write(value)

函数原型：write(value)，设置对应创建gpio对象的Pin脚输出电平状态，返回设置结果。

| 参数  | 类型 | 说明                                                                                    |
|-------|------|-----------------------------------------------------------------------------------------|
| value | int  | 0 -当PIN脚为输出模式时，设置当前Pin脚输出低 1 -当PIN脚为输出模式时，设置当前Pin脚输出高 |
| ret   | int  | 0成功 -1失败                                                                            |

## 交互操作

使用QPYcom工具和模组进行交互，示例如下：

![](media/5c3518e6007b37481d75644bb6fc3659.png)

注意：

1.  import Pin即为让Pin模块在当前空间可见。

2.  只有import Pin模块，才能使用Pin内的函数和变量。

## 下载验证

下载.py文件到模组运行，代码如下：

```python
from machine import Pin   
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0) 
ret = gpio1.write(1) 
print(ret) 
ret = gpio1.read() 
print(ret) 
ret = gpio1.write(0) 
print(ret) 
ret = gpio1.read() 
print(ret)
```


<!-- * [下载代码](code/GPIO.py)  -->

 <a href="zh-cn/QuecPythonSub/code/GPIO.py" target="_blank">下载代码</a>

## 外部中断\_基本概述

认识了普通的GPIO之后，接着介绍外部中断，普通GPIO可以随时查询Pin引脚的电平状态，但却不能及时发现电平的变化，而外部中断就能完美的解决这个问题。若设定了上升沿触发外部中断时，当电平从低电平上升到高电平瞬间，就会触发外部中断，从而在电平变化时立马执行回调函数。

## 软件设计

### 创建extint对象：

extint = ExtInt(GPIOn, mode, pull, callback)

函数原型：ExtInt(GPIOn, mode, pull,callback)，返回一个extint对象，用于使能、禁止中断响应。

| 参数     | 类型     | 说明                                                         |
| -------- | -------- | ------------------------------------------------------------ |
| GPIOn    | int      | GPIO1 – 模组的Pin10 GPIO2 – 模组的Pin11 <br/>GPIO3 – 模组的Pin12 GPIO4 – 模组的Pin13 <br/>GPIO5 – 模组的Pin14 GPIO6 – 模组的Pin15 <br/>GPIO7 – 模组的Pin16 GPIO8 – 模组的Pin39 <br/>GPIO9 – 模组的Pin40 GPIO10 – 模组的Pin48 |
| mode     | int      | IRQ_RISING – 上升沿触发 <br/>IRQ_FALLING – 下降沿触发 <br/>IRQ_RISING_FALLING – 上升和下降沿触发 |
| pull     | int      | PULL_DISABLE – 浮空模式<br/>PULL_PU – 上拉模式 <br/>PULL_PD – 下拉模式 |
| callback | function | 中断触发回调函数                                             |

### 允许中断

ret = extint.enable()

函数原型：enable()，设置对应创建extint对象的中断响应，返回设置结果。

| 参数 | 类型 | 说明         |
|------|------|--------------|
| ret  | int  | 0成功 -1失败 |

### 禁止中断

ret = extint.disable()

函数原型：disable()，设置对应创建extint对象的中断响应，返回设置结果。

| 参数 | 类型 | 说明         |
|------|------|--------------|
| ret  | int  | 0成功 -1失败 |

## 交互操作

使用QPYcom工具和模组进行交互，示例如下：

![](media/2d5c069c492cc483e86f32f3fe88480a.png)

注意：回调函数fun(args)中的args，是引脚中断后返回的内部GPIO行号，一般用不上，但也要设置。

## 下载验证

下载.py文件到模组运行，代码如下：

```
from machine import ExtInt 
import utime    
def fun1(args):  
	print(args)  
	print("1111111111111111111111")   
def fun2(args):  
	print(args)  
	print("222222222222222222222")   
extint1 = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun1) extint1.enable()  
extint2 = ExtInt(ExtInt.GPIO2, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun2) extint2.enable()  
while True:  
	utime.sleep_ms(200)  
	print("。。。。。。。。。")  
```

注意：回调函数fun(args)中的args，是引脚中断后返回的内部GPIO行号，一般用不上，但必须设置。


<!-- * [下载代码](code/ExtInt.py)  -->

 <a href="zh-cn/QuecPythonSub/code/ExtInt.py" target="_blank">下载代码</a>

## 名词解释

低电平：通常用0来表示低电平

高电平：通常用1来表示高电平

上升沿：从低电平上升到高电平的边沿

下降沿：从高电平上升到低电平的边沿

回调函数：一个普通函数，在满足设定条件下被触发执行这个函数

浮空：Pin引脚直出，没有默认电平，处于不稳定状态

上拉：Pin引脚内部有个电阻拉到VCC，默认为高电平

下拉：Pin引脚内部有个电阻拉到GND，默认为低电平

输入：Pin引脚的电平状态随外部变化

输出：Pin引脚的电平驱动外围电路

中断：停止执行当前的程序去执行另一段程序，这个过程叫中断