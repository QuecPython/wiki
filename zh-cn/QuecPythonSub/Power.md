# Quecpython Power开关机开发

本文主要介绍QuecPython Power 模块的使用。 Power模块提供关机、软件重启、电压检测功能，可以用作远程关机等操作，包含的API有：

- **Power.powerDown()**
- **Power.powerRestart()**
- **Power. powerOnReason()**
- **Power. powerDownReason()**
- **Power. getVbatt()**

具体的API 详解请参考 [QuecPython-misc - 其他-Power](https://python.quectel.com/wiki/api/#power)

本文档适用于移远通信如下模块：

- EC100Y-CN
- EC600S-CN



## 交互使用

```python
>>> from misc import Power
>>> Power. powerDownReason()
1
>>> Power.powerDown()
>>> from misc import Power
>>> Power. powerDownReason()
1
>>> Power.po
powerDown    powerDownReason powerOnReason  powerRestart   
>>> Power.powerOnReason()
```



## 实验代码

执行脚本以后，使用定时中断设置5秒以后睡眠。

```python
# 使用定时器，定时关机
from machine import Timer
from misc import Power
import utime as time


def CallBack(t):
    Power.powerDown()


def test_power_module():
    # 创建一个定时器对象
    T = Timer(Timer.Timer1)
    # period 单位为 ms
    T.start(period=5000, mode=Timer.ONE_SHOT, callback=CallBack)   # 启动定时器
    # wait
    while True:
        time.sleep_ms(1)
    print("The main function has exited")

    
if __name__ == "__main__":
    test_power_module()
    
```

## 配套代码
 
<!-- * [下载代码](code/power_base.py) -->
 <a href="zh-cn/QuecPythonSub/code/power_base.py" target="_blank">下载代码</a>