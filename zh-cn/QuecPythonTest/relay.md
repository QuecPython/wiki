<!-- ## DMA实验 -->

<!-- ## PWM DAC实验-->

## 继电器实验 

文档主要介绍如何操作继电器，继电器是电子行业中最常用的控制设备之一，许多设备通常都需要用低压控制高压，如5V 控制220V，以保障操作人员的安全。下面主要从硬件设计和软件设计方面讲解，通过阅读本文，您将了解到继电器的操作原理和验证实验理论。

### 硬件描述

模组的 GPIO 输出电压为1.8V，为了能够稳定地控制继电器，搭配电压转换电路，可用电压转换IC，也可以直接用三极管，然后用三极管驱动继电器。高电平三极管导通，继电器吸合；低电平三极管截止，继电器断开。

<span><div style="text-align: center;">
![](media/ef40a9163b85d808df2488e08c09d482.jpg)

</div></span>

### 软件设计

找到和继电器连接的 GPIO 口，初始化 GPIO 后，控制继电器通断，就是控制 GPIO的高低电平变化，要继电器吸合，就往 GPIO 写入 1，要断开，就往 GPIO 写入
0，这样轻易的实现我们的目的了。

以下示例代码，初始化 GPIO，包括一个读函数、一个写函数。

```python
IOdictRead = {} # 记录已经初始化的GPIO口
IOdictWrite = {} # 记录已经初始化的GPIO口

def GPIO_Read(gpioX, Pull=Pin.PULL_DISABLE, level=1):
    if IOdictWrite.get(gpioX, None):
    del IOdictWrite[gpioX]
    gpioIO = IOdictRead.get(gpioX, None)
    if gpioIO:
    	return gpioIO.read()
    else:
        IOdictRead[gpioX] = (Pin(gpioX, Pin.IN, Pull, level))
        gpioIO = IOdictRead.get(gpioX, None)
        return gpioIO.read()

def GPIO_Write(gpioX, level, Pull=Pin.PULL_DISABLE):
	if IOdictRead.get(gpioX, None):
    	del IOdictRead[gpioX]
    gpioIO = IOdictWrite.get(gpioX, None)
    if gpioIO:
    	gpioIO.write(level)
    else:
        IOdictWrite[gpioX] = (Pin(gpioX, Pin.OUT, Pull, level))
        gpioIO = IOdictWrite.get(gpioX, None)
        gpioIO.write(level)
```

定义了两个继电器的 GPIO 口，

```python
Relay_1 = Pin.GPIO3 # 定义继电器引脚
Relay_2 = Pin.GPIO4 # 定义继电器引脚
def relayIO_On(gpioX): # 某个引脚置0
	GPIO_Write(gpioX, 0)
def relayIO_Off(gpioX): # 某个引脚置1
	GPIO_Write(gpioX, 1)
```

定义了两个按键的GPIO 口，用按键操作继电器的吸合、断开

```python
KEY_1 = Pin.GPIO1 # 定义按键引脚
KEY_2 = Pin.GPIO2 # 定义按键引脚

def readKey(): # 读取按键，返回按键值
	if (GPIO_Read(KEY_1) == low): # 判断是否为低电平
		utime.sleep_ms(20) # 防抖
		if (GPIO_Read(KEY_1) == low): # 判断是否为低电平
			return KEY_1 # 返回按键值
	elif (GPIO_Read(KEY_2) == low): # 判断是否为低电平
		utime.sleep_ms(20) # 防抖
		if (GPIO_Read(KEY_2) == low): # 判断是否为低电平
			return KEY_2 # 返回按键值
	else:
		return None # 返回空
```

主函数，无限循环检测按键是否被按下，某个按键按下后两个继电器互换跳动。

```python
while True:
	if(readKey() == KEY_1): # 判断是否KEY_1 被按下
		relayIO_On(Relay_1) # Relay_1 ON
		relayIO_Off(Relay_2) # Relay_2 OFF
	elif (readKey() == KEY_1): # 判断是否KEY_1 被按下
		relayIO_Off(Relay_1) # Relay_1 OFF
		relayIO_On(Relay_2) # Relay_2 ON
```

接下来就可以下载验证了，python 代码不需要编译，直接通过 QPYcom 工具把.py文件下载到模块中运行。

### 下载验证

>   下载.py 文件到模组运行：

<span><div style="text-align: center;">
![](media/466a7209f9edc319f3ef2f6f9786ba0c.jpg)

</div></span>

下载之后，代码在延时的时候自动进入休眠，功耗降低。

### 配套代码

<!-- * [下载代码](code/06_relay.py) -->
 <a href="zh-cn/QuecPythonTest/code/06_relay.py" target="_blank">下载代码</a>