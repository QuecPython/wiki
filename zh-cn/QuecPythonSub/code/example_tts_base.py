

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
