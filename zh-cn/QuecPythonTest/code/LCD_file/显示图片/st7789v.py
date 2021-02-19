# -*- coding: UTF-8 -*-

import log
from machine import LCD

class ST7789V():
    def __init__(self, width, hight):
        self.lcdlog = log.basicConfig()
        self.lcdlog = log.getLogger("LCD")
        self.lcdlog.setLevel(log.DEBUG)
        self.lcd = LCD()
        self.lcd_w = width
        self.lcd_h = hight

        self.st7789v_init_data = (
            2, 1, 120,
            0, 0, 0x11,
            2, 1, 120,
            0, 1, 0x36,
            1, 1, 0x00,
            0, 1, 0x3A,
            1, 1, 0x05,
            0, 0, 0x21,
            0, 5, 0xB2,
            1, 1, 0x05,
            1, 1, 0x05,
            1, 1, 0x00,
            1, 1, 0x33,
            1, 1, 0x33,
            0, 1, 0xB7,
            1, 1, 0x23,
            0, 1, 0xBB,
            1, 1, 0x22,
            0, 1, 0xC0,
            1, 1, 0x2C,
            0, 1, 0xC2,
            1, 1, 0x01,
            0, 1, 0xC3,
            1, 1, 0x13,
            0, 1, 0xC4,
            1, 1, 0x20,
            0, 1, 0xC6,
            1, 1, 0x0F,
            0, 2, 0xD0,
            1, 1, 0xA4,
            1, 1, 0xA1,
            0, 1, 0xD6,
            1, 1, 0xA1,
            0, 14, 0xE0,
            1, 1, 0x70,
            1, 1, 0x06,
            1, 1, 0x0C,
            1, 1, 0x08,
            1, 1, 0x09,
            1, 1, 0x27,
            1, 1, 0x2E,
            1, 1, 0x34,
            1, 1, 0x46,
            1, 1, 0x37,
            1, 1, 0x13,
            1, 1, 0x13,
            1, 1, 0x25,
            1, 1, 0x2A,
            0, 14, 0xE1,
            1, 1, 0x70,
            1, 1, 0x04,
            1, 1, 0x08,
            1, 1, 0x09,
            1, 1, 0x07,
            1, 1, 0x03,
            1, 1, 0x2C,
            1, 1, 0x42,
            1, 1, 0x42,
            1, 1, 0x38,
            1, 1, 0x14,
            1, 1, 0x14,
            1, 1, 0x27,
            1, 1, 0x2C,
            0, 0, 0x29,

            0, 1, 0x36,
            1, 1, 0x00,

            0, 4, 0x2a,
            1, 1, 0x00,
            1, 1, 0x00,
            1, 1, 0x00,
            1, 1, 0xef,

            0, 4, 0x2b,
            1, 1, 0x00,
            1, 1, 0x00,
            1, 1, 0x00,
            1, 1, 0xef,

            0, 0, 0x2c,
        )
        ret = self.lcd.lcd_init(bytearray(self.st7789v_init_data), self.lcd_w, self.lcd_h, 13000, 1, 4, 0, self.lcd_set_display_area, self.lcd_display_on, self.lcd_display_off, None)
        self.lcdlog.info('lcd.lcd_init ret = {}'.format(ret))
        '''清屏，设置白色'''
        self.lcd.lcd_clear(0xFFFF)

    def lcd_display_on(self):
        pass

    def lcd_display_off(self):
        pass

    def lcd_set_display_area(self, args):
        xstart = args[0]
        ystart = args[1]
        xend = args[2]
        yend = args[3]

        # Row Start
        self.lcd.lcd_write_cmd(0x2a, 1)
        self.lcd.lcd_write_data((xstart >> 8) & 0xff, 1)
        self.lcd.lcd_write_data((xstart & 0xff), 1)
        self.lcd.lcd_write_data((xend >> 8) & 0xff, 1)
        self.lcd.lcd_write_data((xend & 0xff), 1)

        # Column Start
        self.lcd.lcd_write_cmd(0x2b, 1)
        self.lcd.lcd_write_data((ystart >> 8) & 0xff, 1)
        self.lcd.lcd_write_data((ystart & 0xff), 1)
        self.lcd.lcd_write_data((yend >> 8) & 0xff, 1)
        self.lcd.lcd_write_data((yend & 0xff), 1)

        self.lcd.lcd_write_cmd(0x2C, 1)
        self.lcd.lcd_write_cmd(0xff, 1)

    '''
    单个字符显示，包括汉字和ASCII
    x - x轴坐标
    y - y轴坐标
    xsize - 字体宽度
    ysize - 字体高度
    ch_buf - 存放汉字字模的元组或者列表
    fc - 字体颜色，RGB565
    bc - 背景颜色，RGB565
    '''
    def lcd_show_char(self, x, y, xsize, ysize, ch_buf, fc, bc):
        rgb_buf = []
        t1 = xsize // 8
        t2 = xsize % 8
        if t2 != 0:
            xsize = (t1 + 1) * 8
        for i in range(0, len(ch_buf)):
            for j in range(0, 8):
                if (ch_buf[i] << j) & 0x80 == 0x00:
                    rgb_buf.append(bc >> 8)
                    rgb_buf.append(bc & 0xff)
                else:
                    rgb_buf.append(fc >> 8)
                    rgb_buf.append(fc & 0xff)
        self.lcd.lcd_write(bytearray(rgb_buf), x, y, x + xsize - 1, y + ysize - 1)

    '''
    ASCII字符显示,目前支持8x16、16x24的字体大小，
    如果需要其他字体大小需要自己增加对应大小的字库数据，并
    在下面函数中增加这个对应字库的字典。
    x - x轴显示起点
    y - y轴显示起点
    xsize - 字体宽度
    ysize - 字体高度
    ch - 待显示的ASCII字符
    fc - 字体颜色，RGB565
    bc - 背景颜色，RGB565
    '''
    def lcd_show_ascii(self, x, y, xsize, ysize, ch, fc, bc):
        ascii_dict = {}
        if xsize == 8 and ysize == 16:
            ascii_dict = fonts.ascii_8x16_dict
        elif xsize == 16 and ysize == 24:
            ascii_dict = fonts.ascii_16x24_dict

        for key in ascii_dict:
            if ch == key:
                self.lcd_show_char(x, y, xsize, ysize, ascii_dict[key], fc, bc)

    '''
    汉字显示,目前支持16x16、16x24、24x24的字体大小，
    如果需要其他字体大小需要自己增加对应大小的字库数据，并
    在下面函数中增加这个对应字库的字典。
    x - x轴显示起点
    y - y轴显示起点
    xsize - 字体宽度
    ysize - 字体高度
    ch - 待显示的ASCII字符
    fc - 字体颜色，RGB565
    bc - 背景颜色，RGB565
    '''
    def lcd_show_chinese(self, x, y, xsize, ysize, ch, fc, bc):
        hanzi_dict = {}
        if xsize == 16 and ysize == 16:
            hanzi_dict = fonts.hanzi_16x16_dict
        elif xsize == 16 and ysize == 24:
            hanzi_dict = fonts.hanzi_16x24_dict
        elif xsize == 24 and ysize == 24:
            hanzi_dict = fonts.hanzi_24x24_dict

        for key in hanzi_dict:
            if ch == key:
                self.lcd_show_char(x, y, xsize, ysize, hanzi_dict[key], fc, bc)

    '''
    图片显示，只需要传入显示的起点坐标和图片的宽高（注意是图片宽高，不是终点坐标）
    image_data - 存放待显示图片的RGB数据
    x - x轴显示起点
    y - y轴显示起点
    width - 图片宽度
    heigth - 图片高度
    '''
    def lcd_show_image(self, image_data, x, y, width, heigth):
        self.lcd.lcd_write(bytearray(image_data), x, y, x + width - 1, y + heigth - 1)


    def get_rgb565_color(self, r, g, b):
        return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | ((b & 0xF8) >> 3)
