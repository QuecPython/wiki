## 外部中断实验

### 概述

本文档主要基于EC600介绍如何使用QuecPython类库API来快速开发使用外部中断功能。

EC600 14个 外部中断引脚。 从GPIO1~GPIO14。 具体的映射看下后文函数的讲解。

### 使用说明

#### Exint创建对象

extint = ExtInt(GPIOn, mode, pull, callback)

| 参数     | 类型 | 说明                                                         |
| -------- | ---- | ------------------------------------------------------------ |
| GPIOn    | int  | 引脚号   <br />EC100YCN平台引脚对应关系如下（引脚号为外部引脚编号）：   <br />GPIO1 – 引脚号22   <br />GPIO2 – 引脚号23   <br />GPIO3 – 引脚号38   <br />GPIO4 – 引脚号53   <br />GPIO5 – 引脚号54   <br />GPIO6 – 引脚号104   <br />GPIO7 – 引脚号105   <br />GPIO8 – 引脚号106   <br />GPIO9 – 引脚号107   <br />GPIO10 – 引脚号178   <br />GPIO11 – 引脚号195   <br />GPIO12 – 引脚号196   <br />GPIO13 – 引脚号197   <br />GPIO14 – 引脚号198   <br />GPIO15 – 引脚号199   <br />GPIO16 – 引脚号203   <br />GPIO17 – 引脚号204  <br />GPIO18 – 引脚号214   <br />GPIO19 – 引脚号215   <br />EC600SCN平台引脚对应关系如下（引脚号为模块外部引脚编号）：   <br />GPIO1 – 引脚号10   <br />GPIO2 – 引脚号11   <br />GPIO3 – 引脚号12   <br />GPIO4 – 引脚号13   <br />GPIO5 – 引脚号14   <br />GPIO6 – 引脚号15   <br />GPIO7 – 引脚号16   <br />GPIO8 – 引脚号39   <br />GPIO9 – 引脚号40   <br />GPIO10 – 引脚号48  <br />GPIO11 – 引脚号58   <br />GPIO12 – 引脚号59   <br />GPIO13 – 引脚号60   <br />GPIO14 – 引脚号61 |
| mode     | int  | 设置触发方式   <br />IRQ_RISING – 上升沿触发   <br />IRQ_FALLING – 下降沿触发   <br />IRQ_RISING_FALLING – 上升和下降沿触发 |
| pull     | int  | PULL_DISABLE – 浮空模式   <br />PULL_PU – 上拉模式  <br />PULL_PD – 下拉模式 |
| callback | int  | 中断触发回调函数                                             |

#### enable 使能外部中断

使能extint对象外部中断，当中断引脚收到上升沿或者下降沿信号时，会调用callback执行。

参数：无

返回值：使能成功返回整型值0，使能失败返回整型值-1。

#### disable 禁止外部中断

禁用与extint对象关联的中断 。

参数：无

返回值：使能成功返回整型值0，使能失败返回整型值-1。

#### line 返回映射行号 

返回引脚映射的行号。

参数：无

返回值：引脚映射的行号。

### 代码示例

将外部中断映射在GPIO71引脚上。 也就是S4按键.按下S4按键。 回调函数。

```
'''

File: External_interrupt.py

Project: button

File Created: Monday, 28th December 2020 3:03:43 pm

Author: chengzhu.zhou

-----

Last Modified: Monday, 28th December 2020 3:03:47 pm

Modified By: chengzhu.zhou

-----

Copyright 2020 - 2020 quectel

'''

from machine import ExtInt

import utime as time

'''

EC600SCN平台引脚对应关系如下：

GPIO1 – 引脚号71

GPIO2 – 引脚号72

GPIO3 – 引脚号73

GPIO4 – 引脚号74

GPIO5 – 引脚号75

GPIO6 – 引脚号76

GPIO7 – 引脚号77

'''

# 参考自 http://qpy.quectel.com/wiki/#/zh-cn/api/?id=extint

state = 2



def callBack(args):

	global state

	print("###interrupt %d ###" % args)

	state = state - 1



def main():

 	# 映射GPIO71的下降沿触发回调函数

	extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, callBack)

 	# 等待按键按下，触发

	 while state:

		time.sleep_ms(10)

		pass

	# 停止映射外部中断

	extint.disable()

	print("The main function has exited")



if __name__ == "__main__":

	main()
```

### 配套代码

[下载代码](code/External_interrupt.py)