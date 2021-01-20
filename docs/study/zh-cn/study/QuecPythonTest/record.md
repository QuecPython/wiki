## 录音实验

文档主要基于 EC600S 介绍如何使用 QuecPython  的录音功能 。同时说明录音功能的相关 API 的用法。 硬件描述 。

### 硬件设计

录音功能的硬件设计电路如下：

![Quectel_QuecPython_录音实验说明_01](media/Quectel_QuecPython_录音实验说明_01.png)

																	图1 录音模块电路原理图

![Quectel_QuecPython_录音实验说明_02](media/Quectel_QuecPython_录音实验说明_02.png)

																	图2 开发板录音硬件

注意事项 

（1）  焊接 MIC 时，要注意区分正负极，咪头正负极区分方法如下：

咪头两个引脚中，有 铜皮连接到了外壳 的那个引脚 就是负极，或者用万用表量， 与外壳连通的引脚 就是负极。

![Quectel_QuecPython_录音实验说明_03](media/Quectel_QuecPython_录音实验说明_03.png)

																	图3  咪头正负极说明

（2）  外接喇叭播放录音文件时，请使用规格型号为 4Ω 3W 的喇叭。 

### 软件设计

#### 录音 API 说明

**创建对象**

> ***import audio*** 
>
> ***record_obj = audio.Reocrd(filename, callback)*** 

参数说明：

**filename**  ：保存录音的文件名

**callback**  ：录音回调函数，用于通知用户录音结果、录音文件大小以及文件名 回调函数形式如下：

```python
def record_callback(args):  
    print('file_name:{}'.format(args[0]))  
    print('file_size:{}'.format(args[1]))  
    print('record_sta:{}'.format(args[2]))  
```



**开始录音**

> ***record_obj.start(seconds)*** 

参数说明：

**seconds**  ：指定录音时长，单位 s 

返回值： 

**0**  ：正常

**-1**  ： 文件覆盖失败

**-2**  ： 文件打开失败

**-3**  ： 文件正在使用

**-4**  ： 通道设置错误（只能设置 0 或 1） 

**-5**  ： 定时器资源申请失败



**停止录音**

> ***record_obj.stop()*** 

参数说明：无参数 。 

返回值： 无返回值 。 



**判断录音文件是否存在**

> ***record_obj.exists()*** 

参数说明：无参数 

返回值： 

**true**  ：文件存在

**false**  ：文件不存在



**获取录音文件保存的路径**

> ***record_obj.getFilePath()*** 

参数说明：无参数 。 

返回值： 返回 string 类型的录音文件保存路径。



**读取录音数据**

> ***record_obj.getData(offset, size)*** 

参数说明：

**offset**  ：偏移位置

**size**  ：读取的长度，单位字节

返回值： 正常返回读取的数据 ，失败返回错误码，如下

**-1**  ： 读取数据错误

**-2**  ： 文件打开失败

**-3**  ： 偏移量设置错误

**-4**  ： 文件正在使用

**-5**  ： 设置超出文件大小（ offset+size > file_size） 



**读取录音文件大小**

> ***record_obj.getSize()*** 

参数说明：无参数 。 

返回值： 

成功返回录音文件大小（ 此文件有 44byte 的文件头，所以比创建对象传入回调的值大 44），单位字节，失败返回错误码，如下

**-1**  ：获取文件 size 失败 **-2**  ： 文件打开失败

**-3**  ： 文件正在使用



**删除录音文件**

> ***record_obj.Delete()*** 

参数说明：无参数 。 

返回值： 

**0**  ：删除成功

**-1**  ：文件不存在

**-2**  ：文件正在使用



**判断是否正在处理录音**

> ***record_obj.isBusy()*** 

参数说明：无参数 。 

返回值： 

**0**  ：idle 

**1**  ：busy 



### 下载验证

#### 实验代码 

```python
# -*- coding: UTF-8 -*-

import utime
import checkNet
import audio
from machine import Pin
'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Record_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

'''
外接喇叭播放录音文件，参数选择0
'''
aud = audio.Audio(0)
tts = audio.TTS(0)

'''
外接喇叭播放录音文件，需要下面这一句来使能
'''
audio_EN = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)


def record_callback(args):
    print('file_name:{}'.format(args[0]))
    print('file_size:{}'.format(args[1]))
    print('record_sta:{}'.format(args[2]))

    record_sta = args[2]
    if record_sta == 3:
        print('The recording is over, play it')
        tts.play(1, 0, 2, '录音结束,准备播放录音文件')
        aud.play(1, 0, record.getFilePath())
    elif record_sta == -1:
        print('The recording failure.')
        tts.play(1, 0, 2, '录音失败')


if __name__ == '__main__':
    '''
    手动运行本例程时，可以去掉该延时，如果将例程文件名改为main.py，希望开机自动运行时，需要加上该延时,
    否则无法从CDC口看到下面的 poweron_print_once() 中打印的信息
    '''
    # utime.sleep(5)
    checknet.poweron_print_once()

    '''
    如果用户程序包含网络相关代码，必须执行 wait_network_connected() 等待网络就绪（拨号成功）；
    如果是网络无关代码，可以屏蔽 wait_network_connected()
    '''
    # checknet.wait_network_connected()

    # 用户代码
    '''######################【User code star】########################################'''
    print('the recording will begin in 2 seconds. Please be ready!')
    utime.sleep(2)
    print('start recording!')
    record = audio.Record('recordfile.wav', record_callback)
    record.start(10)
    '''######################【User code end 】########################################'''

```

### 配套代码

[下载代码](code/record.py)