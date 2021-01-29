# -*- coding: UTF-8 -*-


import utime

'''
如果用户使用的固件版本中没有checkNet库，请将checkNet.mpy文件上传到模块的usr目录，
并将 import checkNet 改为 from usr import checkNet
'''
import checkNet
from machine import LCD
from usr import image

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_ILI9225_LCD_Example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

lcd = LCD()


def ili9225_display_on(args):
    print('ili9225_display_on')
    lcd.lcd_write_cmd(0x07, 1)
    lcd.lcd_write_data(0x1017, 2)


def ili9225_display_off(args):
    print('ili9225_display_off')
    lcd.lcd_write_cmd(0x07, 1)
    lcd.lcd_write_data(0x1004, 2)


def ili9225_display_area(args):
    xstart = args[0]
    ystart = args[1]
    xend = args[2]
    yend = args[3]
    print('area',xstart,ystart,xend,yend)
    lcd.lcd_write_cmd(0x36, 1)
    lcd.lcd_write_data(xend, 2)
    lcd.lcd_write_cmd(0x37, 1)
    lcd.lcd_write_data(xstart, 2)
    lcd.lcd_write_cmd(0x38, 1)
    lcd.lcd_write_data(yend, 2)
    lcd.lcd_write_cmd(0x39, 1)
    lcd.lcd_write_data(ystart, 2)
    lcd.lcd_write_cmd(0x20, 1)
    lcd.lcd_write_data(xstart, 2)
    lcd.lcd_write_cmd(0x21, 1)
    lcd.lcd_write_data(ystart, 2)
    lcd.lcd_write_cmd(0x22, 1)
    lcd.lcd_write_cmd(0xff, 1)


'''
设置光标位置
'''
def lcd_set_cursor(x, y):
    pos_tuple = (x, y, x, y)
    ili9225_display_area(pos_tuple)


ILI9225_INIT_TUPLE = (
    0,1,0x02,
    1,2,0x01,0x00,
    0,1,0x01,
    1,2,0x01,0x1C,
    0,1,0x03,
    1,2,0x10,0x30,
    0,1,0x08,
    1,2,0x08,0x08,
    0,1,0x0B,
    1,2,0x11,0x00,
    0,1,0x0C,
    1,2,0x00,0x00,
    0,1,0x0F,
    1,2,0x14,0x01,
    0,1,0x15,
    1,2,0x00,0x00,
    0,1,0x20,
    1,2,0x00,0x00,
    0,1,0x21,
    1,2,0x00,0x00,
    0,1,0x10,
    1,2,0x08,0x00,
    0,1,0x11,
    1,2,0x1F,0x3F,
    0,1,0x12,
    1,2,0x01,0x21,
    0,1,0x13,
    1,2,0x00,0x0F,
    0,1,0x14,
    1,2,0x43,0x49,
    0,1,0x30,
    1,2,0x00,0x00,
    0,1,0x31,
    1,2,0x00,0xDB,
    0,1,0x32,
    1,2,0x00,0x00,
    0,1,0x33,
    1,2,0x00,0x00,
    0,1,0x34,
    1,2,0x00,0xDB,
    0,1,0x35,
    1,2,0x00,0x00,
    0,1,0x36,
    1,2,0x00,0xAF,
    0,1,0x37,
    1,2,0x00,0x00,
    0,1,0x38,
    1,2,0x00,0xDB,
    0,1,0x39,
    1,2,0x00,0x00,
    0,1,0x50,
    1,2,0x00,0x01,
    0,1,0x51,
    1,2,0x20,0x0B,
    0,1,0x52,
    1,2,0x00,0x00,
    0,1,0x53,
    1,2,0x04,0x04,
    0,1,0x54,
    1,2,0x0C,0x0C,
    0,1,0x55,
    1,2,0x00,0x0C,
    0,1,0x56,
    1,2,0x01,0x01,
    0,1,0x57,
    1,2,0x04,0x00,
    0,1,0x58,
    1,2,0x11,0x08,
    0,1,0x59,
    1,2,0x05,0x0C,
    0,1,0x07,
    1,2,0x10,0x17,
    0,1,0x22,
)

LCD_INIT_DATA = bytearray(ILI9225_INIT_TUPLE)


if __name__ == '__main__':
    '''
    手动运行本例程时，可以去掉该延时，如果将例程文件名改为main.py，希望开机自动运行时，需要加上该延时,
    否则无法从CDC口看到下面的 poweron_print_once() 中打印的信息
    '''
    #utime.sleep(5)
    #checknet.poweron_print_once()

    '''
    如果用户程序包含网络相关代码，必须执行 wait_network_connected() 等待网络就绪（拨号成功）；
    如果是网络无关代码，可以屏蔽 wait_network_connected()
    '''
    # checknet.wait_network_connected()

    # 用户代码
    image_data = bytearray(image.image_buf)
    '''######################【User code star】###################################################'''
    ret = lcd.lcd_init(LCD_INIT_DATA, 176, 220, 13000, 1, 4, 0, ili9225_display_area, ili9225_display_on, ili9225_display_off, None)
    print('lcd.lcd_init ret = {}'.format(ret))
   # '''清屏，设置白色'''
    
    
    #lcd.lcd_clear(0xf800)
    '''
    要显示的图片像素为 99*100，下面设置显示图片的起始坐标位置为（70，70），结束坐标为（168，169）
    lcd.lcd_write(data, x_start, y_start, x_end, y_end)
    要注意：显示图片时，坐标的设置和图片像素之间必须满足如下关系，这里以 99*100 像素为例说明：
    x_end - x_start + 1 = 99
    y_end - y_start + 1 = 100
    '''
    lcd.lcd_write(image_data, 0, 0, 127, 127)

    '''######################【User code end 】###################################################'''
