'''
File: uart_demo1.py
Project: uart
File Created: Wednesday, 23rd December 2020 3:33:56 pm
Author: chengzhu.zhou
-----
Last Modified: Wednesday, 23rd December 2020 3:34:15 pm
Modified By: chengzhu.zhou
-----
Copyright 2020 - 2020 quectel
'''

from machine import UART
import utime as time
"""
端口号
EC100YCN平台与EC600SCN平台,UARTn作用如下：
UART0 - DEBUG PORT
UART1 – BT PORT
UART2 – MAIN PORT
UART3 – USB CDC PORT
"""


def main():
    """
    config uart Baud rate as 115200,data bits as 8bit, Do not use parity,
    Stop bit as 0bit,Do not use Flow control，
    UART(UART.UARTn, buadrate, databits, parity, stopbits, flowctl)
    """
    uart = UART(UART.UART2, 115200, 8, 0, 1, 0)
    # write string
    delay = 100
    for i in range(2):
        # write string
        uart.write("hello world\r\n")
        # write string and & integer
        uart.write("delay num as {0}ms\r\n".format(delay))
        # write float
        uart.write("π as {0}\r\n".format(3.14159))
        # read something
        read_btyes = 6
        uart.write("please input {0} bytes:\r\n".format(read_btyes))
        while True:
            if uart.any() > read_btyes:
                break
            else:
                time.sleep_ms(10)
        # !!! Before reading buffer, please make sure there is data in buffer
        input_date = uart.read(read_btyes)
        uart.write("The data you entered is {0}\r\n".format(input_date))
        time.sleep_ms(delay)

if __name__ == "__main__":
    main()
