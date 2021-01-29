## 定时器中断实验 

### 基本概述

本文档主要基于EC600介绍如何使用QuecPython类库API来快速开发使用定时器功能。

### 使用说明

#### Timer创建对象

from machine import Timer

timer = Timer(Timern)

| 常量         | 说明    |
| ------------ | ------- |
| Timer.Timer0 | 定时器0 |
| Timer.Timer1 | 定时器1 |
| Timer.Timer2 | 定时器2 |
| Timer.Timer3 | 定时器3 |

#### start启动定时器

timer.start(period, mode, callback)

| 参数     | 类型     | 说明                                                         |
| -------- | -------- | ------------------------------------------------------------ |
| period   | int      | 中断周期，单位毫秒，大于等于1                                |
| mode     | int      | 运行模式 Timer.ONE_SHOT 单次模式，定时器只执行一次 Timer.PERIODIC 周期模式，循环执行 |
| callback | function | 定时器执行函数                                               |

返回值

启动成功返回整型值0，失败返回整型值-1。

#### stop停止定时器

关闭定时器。

参数:无

返回值:

成功返回整型值0，失败返回整型值-1。

### 实验设计

#### 实验步骤

1. 分配一个定时器。

2. 定义一个回调函数， 配置成为1秒回调一次。

3. 在回调函数里面设置，回调10次。关闭定时器。

#### 实验代码

```
'''File: timer.py

Project: timer

File Created: Monday, 28th December 2020 2:44:33 pm

Author: chengzhu.zhou

-----

Last Modified: Friday, 8th January 2021 9:19:55 am

Modified By: chengzhu.zhou

-----

Copyright 2021 - 2021 quectel

'''

# refs for http://qpy.quectel.com/wiki/#/zh-cn/api/?id=timer

from machine import Timer

import utime as time



# 创建一个执行函数，并将timer实例传入

num = 0

state = 1



def CallBack(t):

	global num

	global state

	print('num is %d' % num)

	num += 1

	if num > 10:

		print('num > 10, timer exit')

		state = 0

		t.stop()



def main():

	# 创建一个定时器对象

	T = Timer(Timer.Timer1)

	# 设置周期为1秒，

	T.start(period=1000, mode=Timer.PERIODIC, callback=CallBack) # 启动定时器

	# wait

	while state:

		time.sleep_ms(1)

		pass

	T.stop() # 结束该定时器实例

	print("The main function has exited")



if __name__ == "__main__":

	main()
```

### 配套代码

<!-- * [下载代码](code/timer.py) -->
 <a href="zh-cn/QuecPythonTest/code/timer.py" target="_blank">下载代码</a>