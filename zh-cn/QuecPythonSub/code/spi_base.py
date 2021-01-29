# -*- coding: UTF-8 -*-

from machine import SPI
import utime

def spi_test():
    spi_obj = SPI(1, 0, 1)
    r_data = bytearray(5)
    data = b"world"
    # print(data)
    ret = spi_obj.write_read(r_data, data, 5)
    if ret is None:
        print('----------', ret)
    print('#########', r_data)


if __name__ == '__main__':
    while True:
        spi_test()
        utime.sleep(1)
