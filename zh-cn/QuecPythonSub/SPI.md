# QuecPython SPI总线开发

## API简介

本文以EC600S-CN模块为例，主要介绍QuecPython machine模块中SPI的使用。该模块包含的API有：

-  **machine.SPI(port, mode, clk)**

-  **SPI.wtite(data,datalen)**

-  **SPI.read(data,datalen)**

-  **SPI.write_read(r_data,data, datalen)**

  

具体的API 详解请参考[QuecPython-machine - spi](https://python.quectel.com/wiki/api/#spi)

本文档适用于移远通信如下模块：

- EC100Y-CN
- EC600S-CN

## SPI简介

SPI，是英语Serial Peripheral interface的缩写，顾名思义就是串行外围设备接口。是Motorola首先在其MC68HCXX系列处理器上定义的。SPI接口主要应用在 EEPROM，FLASH，实时时钟，AD转换器，还有数字信号处理器和数字信号解码器之间。SPI，是一种高速的，全双工，同步的通信总线，并且在芯片的管脚上只占用四根线，节约了芯片的管脚，同时为PCB的布局上节省空间，提供方便，正是出于这种简单易用的特性，现在越来越多的芯片集成了这种通信协议。



## SPI特点

### 采用主-从模式(Master-Slave) 的控制方式

SPI 规定了两个 SPI 设备之间通信必须由主设备 (Master) 来控制次设备 (Slave). 一个 Master 设备可以通过提供 Clock 以及对 Slave 设备进行片选 (Slave Select) 来控制多个 Slave 设备, SPI 协议还规定 Slave 设备的 Clock 由 Master 设备通过 SCK 管脚提供给 Slave 设备, Slave 设备本身不能产生或控制 Clock, 没有 Clock 则 Slave 设备不能正常工作



### 采用同步方式(Synchronous)传输数据

Master 设备会根据将要交换的数据来产生相应的时钟脉冲(Clock Pulse), 时钟脉冲组成了时钟信号(Clock Signal) , 时钟信号通过时钟极性 (CPOL) 和 时钟相位 (CPHA) 控制着两个 SPI 设备间何时数据交换以及何时对接收到的数据进行采样, 来保证数据在两个设备之间是同步传输的.

![](media\SPI_1.jpg)

### 数据交换(Data Exchanges)

​		SPI 设备间的数据传输之所以又被称为数据交换, 是因为 SPI 协议规定一个 SPI 设备不能在数据通信过程中仅仅只充当一个 "发送者(Transmitter)" 或者 "接收者(Receiver)". 在每个 Clock 周期内, SPI 设备都会发送并接收一个 bit 大小的数据, 相当于该设备有一个 bit 大小的数据被交换了. 一个 Slave 设备要想能够接收到 Master 发过来的控制信号, 必须在此之前能够被 Master 设备进行访问 (Access). 所以, Master 设备必须首先通过 SS/CS pin 对 Slave 设备进行片选, 把想要访问的 Slave 设备选上. 在数据传输的过程中, 每次接收到的数据必须在下一次数据传输之前被采样. 如果之前接收到的数据没有被读取, 那么这些已经接收完成的数据将有可能会被丢弃, 导致 SPI 物理模块最终失效. 因此, 在程序中一般都会在 SPI 传输完数据后, 去读取 SPI 设备里的数据, 即使这些数据(Dummy Data)在我们的程序里是无用的。

### SPI有四种传输模式

上升沿、下降沿、前沿、后沿触发。当然也有MSB和LSB传输方式.

![](media\spi_2.jpg)



### SPI只有主模式和从模式之分。

没有读和写的说法，因为实质上每次SPI是主从设备在交换数据。也就是说，你发一个数据必然会收到一个数据；你要收一个数据必须也要先发一个数据。





## 使用SPI进行通信

本文所示代码使用的硬件版本为 EC600S-CN V1.1。 

```python
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

```

## 配套代码


<!-- * [下载代码](code/spi_base.py) -->
 <a href="zh-cn/QuecPythonSub/code/spi_base.py" target="_blank">下载代码</a>