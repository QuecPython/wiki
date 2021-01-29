# QuecPython Audio模块开发

## API简介

本文以EC600S-CN模块为例，主要介绍QuecPython Audio模块中Audio 的使用。该模块可以用于播放mp3 、wav等格式的文件，包含的API有：

- ​	**audio.Audio(device)**
- ​	**aud.play(priority, breakin, filename)**
- ​	**aud.stop()**
- ​	**aud.setCallback(usrFun)**
- ​	**aud.getState()**
- ​	**aud.getVolume()**
- ​	**aud.setVolume(vol)**

具体的API 详解请参考[QuecPython-audio - 音频播放](https://python.quectel.com/wiki/api/#audio)

本文档适用于移远通信如下模块：

- EC100Y-CN
- EC600S-CN



## 使用Audio播放声音

本文所示代码使用的硬件版本为 EC600S-CN V1.1。 开发板播放声音需要外接喇叭， 具体的喇叭参数以及连接方法请参考《音频播放小实验手册》。 



### 播放mp3 

1. 将随包的 example_maonv.mp3 的文件下载进开发板。

2. 然后将下面的代码烧录进去。

```python
# -*- coding: UTF-8 -*-

import utime as time
import audio
from machine import Pin


def example_audio_mp3():
    '''
    外接喇叭播放录音文件，参数选择0
    '''
    aud = audio.Audio(0)
    '''
    使能外接喇叭播放
    '''
    Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)
    # U: 表示用户目录， GUI下载工具会将文件下载到 /usr 文件下
    aud.play(2, 1, "U:/example_maonv.mp3")
    pass


if __name__ == "__main__":
    example_audio_mp3()

```

3. 运行python 脚本即可。

   

### 播放wav文件

1. 将随包的example_haixiu.wav 的文件下载进开发板。
2. 将以下代码烧录进入开发板。

```python
# -*- coding: UTF-8 -*-

import utime as time
import audio
from machine import Pin


def example_audio_wav():
    '''
    外接喇叭播放录音文件，参数选择0
    '''
    aud = audio.Audio(0)
    '''
    使能外接喇叭播放
    '''
    Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)
    # U: 表示用户目录， GUI下载工具会将文件下载到 /usr 文件下
    aud.play(2, 1, "U:/example_haixiu.wav")
    pass


if __name__ == "__main__":
    example_audio_wav()

```



### 播放过程中切换音量

以上我们展示了基本的播放操作。 下面我们展示如何在播放过程中切换音量。添加一个回调函数， 判断播放状态。

```python
# -*- coding: UTF-8 -*-

import utime as time
import urandom as random
import audio
from machine import Pin

exited = True


def audio_cb(event):
    global exited
    # 7表示播放完毕
    if event == 7:
        exited = False
        print('audio-play finish.')


def example_audio_mp3():
    global exited
    '''
    外接喇叭播放录音文件，参数选择0
    '''
    aud = audio.Audio(0)
    '''
    使能外接喇叭播放
    '''
    Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)
    aud.setCallback(audio_cb)
    for i in range(3):  # 演示3次
        # U: 表示用户目录， GUI下载工具会将文件下载到 /usr 文件下
        aud.play(2, 1, "U:/example_maonv.mp3")
        while exited:
            aud.setVolume(random.randint(6, 11))
            time.sleep_ms(500)
        exited = True

    print("example_audio_mp3 has exit")


if __name__ == "__main__":
    example_audio_mp3()

```

## 配套代码

<!-- * [下载代码和音频文件](zh-cn/QuecPythonSub/code/Audio.zip)  -->

 <a href="zh-cn/QuecPythonSub/code/Audio.zip" target="_blank">下载代码和音频文件</a>