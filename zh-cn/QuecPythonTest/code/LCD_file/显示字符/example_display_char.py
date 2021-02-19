# -*- coding: UTF-8 -*-


import utime

'''
如果用户使用的固件版本中没有checkNet库，请将checkNet.mpy文件上传到模块的usr目录，
并将 import checkNet 改为 from usr import checkNet
'''
import checkNet
from usr import st7789v

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_ST7789V_LCD_Example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)
lcd_st7789v = st7789v.ST7789V(240, 240)


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
    '''######################【User code star】###################################################'''
    fc = 0x0000  # 字体颜色 黑色 可根据需要修改
    bc = 0xffff  # 背景颜色 白色 可根据需要修改

    # 8x16 ASCII字符显示
    lcd_st7789v.lcd_show_ascii(0, 0, 8, 16, 'A', fc, bc)
    lcd_st7789v.lcd_show_ascii(8, 0, 8, 16, 'b', fc, bc)
    lcd_st7789v.lcd_show_ascii(16, 0, 8, 16, '$', fc, bc)
    lcd_st7789v.lcd_show_ascii(24, 0, 8, 16, '8', fc, bc)

    # 16x24 ASCII字符显示
    lcd_st7789v.lcd_show_ascii(0, 20, 16, 24, 'A', fc, bc)
    lcd_st7789v.lcd_show_ascii(16, 20, 16, 24, 'b', fc, bc)
    lcd_st7789v.lcd_show_ascii(32, 20, 16, 24, '$', fc, bc)
    lcd_st7789v.lcd_show_ascii(48, 20, 16, 24, '8', fc, bc)

    # 16x16 汉字显示
    lcd_st7789v.lcd_show_chinese(0, 50, 16, 16, '移', fc, bc)
    lcd_st7789v.lcd_show_chinese(16, 50, 16, 16, '远', fc, bc)
    lcd_st7789v.lcd_show_chinese(32, 50, 16, 16, '通', fc, bc)
    lcd_st7789v.lcd_show_chinese(48, 50, 16, 16, '信', fc, bc)

    # # 16x24 汉字显示
    lcd_st7789v.lcd_show_chinese(0, 70, 16, 24, '移', fc, bc)
    lcd_st7789v.lcd_show_chinese(16, 70, 16, 24, '远', fc, bc)
    lcd_st7789v.lcd_show_chinese(32, 70, 16, 24, '通', fc, bc)
    lcd_st7789v.lcd_show_chinese(48, 70, 16, 24, '信', fc, bc)

    '''######################【User code end 】###################################################'''
