### 定时器 使用指导

#### 定时器功能 

**定时器基本功能** 

定时器可用于多种任务。目前，仅实现了最简单的情况，即定时调用函数，当前移远通信提供的定时器可实现单次和周期性调用函数两种模式。当到达定时器周期时，会触发事件。通过使用回调函数，定时器事件可调用一个Python 函数。

**定时器功能示例** 

将开发板接入电脑，之后，参考《Quectel_QuecPython_基础操作说明》文档进行操作，下面以
EC100Y-CN 模块为例进行说明。

![](media/782cd2c870c62e6f022cca4e47c7c806.jpg)

>   图 **1**：模块接入电脑

>   创建 test.py 文件，在文件内导入 QuecPython 中的 Timer 类，Timer 类在 Machine
>   模块中。编写定时器代码，如下所示：

```
from machine import Timer

def func(args):

	print('###timer callback function###')

	timer = Timer(Timer.Timer1)

	timer.start(period=1000, mode=timer.PERIODIC, callback=func)
```



>   将 test.py
>   文件上传到开发板内，上传方法详见《Quectel_QuecPython_基础操作说明》。

>   程序运行结果，如下所示：

```
>>> import example

>>> example.exec('test.py')

>>> ###timer callback function###

	###timer callback function###

	###timer callback function###

	###timer callback function###

	###timer callback function###

	###timer callback function###

	###timer callback function### 
	
	###timer callback function###
	
timer.stop() 0

>>>
```



#### **QuecPython** 中的定时器 

**Timer 类中的常量** 

| 常量           | 说明                       |
| -------------- | -------------------------- |
| Timer.Timer0   | 定时器 0                   |
| Timer.Timer1   | 定时器 1                   |
| Timer.Timer2   | 定时器 2                   |
| Timer.Timer3   | 定时器 3                   |
| Timer.ONE_SHOT | 单次模式，定时器只执行一次 |
| Timer.PERIODIC | 周期模式，定时器循环执行   |

#### Timer 类中的方法 

**timer = Timer** 

>   该函数用于创建一个 timer 对象。使用定时器相关函数 *timer.start* 和
>   *timer.stop* 之前，需先使用该函数

>   实例化对象，即创建 Timer 对象。

- 函数原型

  timer = Timer(Timern)

- 参数

  *Timern*：常量。定时器号。EC100Y-CN 和 EC600S-CN
  模块支持的定时器为：Timer0~Timer3。 ⚫ 返回值

  返回 timer 对象。

**timer.start** 

>   该函数用于启动定时器。

- 函数原型

  timer.start(period, mode, callback)

- 参数

  *period*：整型。中断周期，单位：毫秒。

  *mode*：

  常量。定时器运行模式，如下：

  Timer.ONE_SHOT 单次模式，定时器只执行一次

  Timer.PERIODIC 周期模式，循环执行

  *callback*： 回调函数，定时执行的函数。

- 返回值

  0 定时器启动成功。 -1 定时器启动失败。

**timer.stop** 

>   该函数用于关闭定时器。

- 函数原型

  timer.stop()

- 参数

  无。

- 返回值

  0 定时器关闭成功。 -1 定时器关闭失败。


#### 附录 

>   表 **1**：术语缩写

| 术语 | 英文全称                          | 中文全称         |
| ---- | --------------------------------- | ---------------- |
| API  | Application Programming Interface | 应用程序编程接口 |

