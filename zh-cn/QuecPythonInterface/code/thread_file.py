import _thread
import utime
import log
from machine import UART  # 导入UART模块

# 设置日志输出级别
log.basicConfig(level=log.INFO)
uart_log = log.getLogger("Thread")

state = 1
msglen = 0
count = 10
uart = UART(UART.UART2, 115200, 8, 0, 1, 0)

def uartwrite():
    global count
    while count:
        write_msg = "Quectel count={}".format(count)  # 发送数据
        uart.write(write_msg)
        uart_log.info("write msg :{}".format(write_msg))
        utime.sleep(1)
        count -= 1
        if count == 0:
            break
    uart_log.info("uartWrite end!")


def uartread():
    global state
    global msglen
    while 1:
        utime.sleep_ms(10)
        msgLen = uart.any()   # 返回是否有可读取的数据长度
        if msgLen:
            msg = uart.read(msgLen)  # 当有数据时进行读取
            utf8_msg = msg.decode()  # 初始数据是字节类型（bytes）,将字节类型数据进行编码,转STR
            uart_log.info("uartread msg: {}".format(utf8_msg))
            state = 0
            break
        else:
            continue

def run():
    _thread.start_new_thread(uartread, ())  # 创建一个线程来监听接收uart消息
    _thread.start_new_thread(uartwrite, ())


if __name__ == "__main__":
    run()
    while 1:
        if state:
            pass
        else:
            break
