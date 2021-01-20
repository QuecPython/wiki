import _thread  # 导入线程模块
import utime  # 导入定时模块
import log  # 导入log模块
from machine import UART  # 导入UART模块

# 测试该示例代码需要配置uart

# 设置日志输出级别
log.basicConfig(level=log.INFO)
uart_log = log.getLogger("UART")

state = 1


def uartWrite():
    count = 10
    # 配置uart
    uart = UART(UART.UART1, 115200, 8, 0, 1, 0)
    while count:
        write_msg = "Hello count={}".format(count)
        # 发送数据
        uart.write(write_msg)
        uart_log.info("Write msg :{}".format(write_msg))
        utime.sleep(1)
        count -= 1
    uart_log.info("uartWrite end!")


def UartRead():
    global state
    uart = UART(UART.UART1, 115200, 8, 0, 1, 0)
    while 1:
        # 返回是否有可读取的数据长度
        msgLen = uart.any()
        # 当有数据时进行读取
        if msgLen:
            msg = uart.read(msgLen)
            # 初始数据是字节类型（bytes）,将字节类型数据进行编码
            utf8_msg = msg.decode()
            # str
            uart_log.info("UartRead msg: {}".format(utf8_msg))
        else:
            continue
    state = 0


def run():
    # 创建一个线程来监听接收uart消息
    _thread.start_new_thread(UartRead, ())


if __name__ == "__main__":
    uartWrite()
    run()
    while 1:
        if state:
            pass
        else:
            break
