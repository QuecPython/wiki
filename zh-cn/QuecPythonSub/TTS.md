# QuecPython TTS模块开发使用说明

本文主要介绍QuecPython Audio模块中TTS模块的使用。 TTS是语音合成应用的一种，它将储存于电脑中的文件，如帮助文件或者[网页](https://baike.baidu.com/item/网页/99347)转换成自然语音输出。TTS不仅能帮助有[视觉障碍](https://baike.baidu.com/item/视觉障碍/5582072)的人阅读计算机上的信息，更能增加[文本文档](https://baike.baidu.com/item/文本文档/557654)的可读性。TTS应用包括语音驱动的邮件以及声音敏感系统，并常与声音识别程序一起使用。

## api介绍

移远通信为您提供的TTS API 支持音量设置、播放语速设置等，包含的API有：

- **tts = audio.TTS(device)**

- **tts.close()**

- **tts.play(priority, breakin, mode, str)**

- **tts.setCallback(usrFun)**

- **tts.getVolume()**

- **tts.setVolume(vol)**
- **tts.getSpeed()**
- **tts.setSpeed(speed)**
- **tts.getState()**
- **tts.stop()**

具体的API 详解请参考[QuecPython-audio - 音频播放-TTS](https://python.quectel.com/wiki/api/#tts)

本文档适用于移远通信如下模块：

- EC100Y-CN
- EC600S-CN



## 使用TTS播放声音

本文所示代码使用的硬件版本为 EC600S-CN V1.1。 开发板播放声音需要外接喇叭， 具体的喇叭参数以及连接方法请参考《音频播放实验》。

 

## 交互小实验

### 播放TTS

```python
import audio
from machine import Pin
tts = audio.TTS(0)
Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)
tts.play(1, 1, 2, '1111111111111111')
```



### 设置音量

```python
import audio
from machine import Pin
tts=audio.TTS(0)
tts.setVolume(5)
Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)
tts.play(1, 1, 2, '12345')
```



### 设置播放语速

```python
import audio
from machine import Pin
tts=audio.TTS(0)
tts.setSpeed(9)
Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)
tts.play(1, 1, 2, '12345')
```



## 实验代码

分别尝试使用不同的声音和语速播放。

```python
'''
Author: chengzhu.zhou
LastEditTime: 2021-01-16 12:23:44
Description: Copyright 2020 - 2020 quectel
'''

import audio
import utime as time
from machine import Pin


def play(tts, strList):
    for Str in strList:
        while tts.getState():
            time.sleep_ms(5)
        tts.play(1, 1, 2, Str)
    pass

# https://python.quectel.com/wiki/#/zh-cn/api/?id=audio-%e9%9f%b3%e9%a2%91%e6%92%ad%e6%94%be


def test_tts_base():
    '''
    外接喇叭播放录音文件，参数选择0
    '''
    tts = audio.TTS(0)
    '''
    使能外接喇叭
    '''
    Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)
    for i in range(1, 9):
        # 循坏播放,增加声音
        tts.setVolume(i)
        play(tts, ['12345', '你好'])
    tts.setVolume(5)
    for i in range(1, 9):
        # 循环增加语速
        tts.setSpeed(i)
        play(tts, ['hello world', 'hello 移远'])
    print("test_tts_base has exited")


if __name__ == "__main__":
    test_tts_base()

```

## 配套代码

<!-- * [下载代码](code/example_tts_base.py) -->
 <a href="zh-cn/QuecPythonSub/code/example_tts_base.py" target="_blank">下载代码</a>