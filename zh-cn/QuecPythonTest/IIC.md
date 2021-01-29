## IIC 实验

本文档主要基于 EC600 介绍如何使用 QuecPython 类库 API 来快速开发使用 I2C 功能。 EC600 拥有 1 个 I2C 板载 外设。连接着加速度传感器和温湿度传感器。

### 使用说明

#### I2C 创建对象

```
from machine import I2C 
i2c_obj = I2C(I2Cn, MODE) 
```



| 参数 | 类型 | 说明                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| I2Cn | int  | i2c  通路索引号 :<br> I2C.I2C0 : 0  （EC100Y）<br/> I2C.I2C1 : 1  （EC600S） |
| MODE | int  | i2c  的工作模式 : <br/>I2C.STANDARD_MODE : 0  标准模式 <br/>I2C.FAST_MODE  ： 1  快速模式 |



#### read 读取数据

```
I2C.read(slaveaddress, addr,addr_len, r_data, datalen, delay) 
```

| 参数         | 类型      | 说明                              |
| ------------ | --------- | --------------------------------- |
| slaveaddress | int       | i2c  设备地址                     |
| addr         | int       | i2c  寄存器地址                   |
| addr_len     | int       | 寄存器地址长度                    |
| r_data       | bytearray | 接收数据的字节数组                |
| datalen      | int       | 字节数组的长度                    |
| delay        | int       | 延时，数据转换缓冲时间（单位 ms） |



#### write 写数据

```
I2C.write(slaveaddress, addr, addr_len, data, datalen) 
```

| 参数         | 类型      | 说明            |
| ------------ | --------- | --------------- |
| slaveaddress | int       | i2c  设备地址   |
| addr         | int       | i2c  寄存器地址 |
| addr_len     | int       | 寄存器地址长度  |
| data         | bytearray | 写入的数据      |
| datalen      | int       | 写入数据的长度  |



### 代码示例

写板载加速度传感器的寄存器，  并且回读。

```python
'''
File: i2c_base.py
Project: i2c
File Created: Wednesday, 30th December 2020 3:09:07 pm
Author: chengzhu.zhou
-----
Last Modified: Thursday, 7th January 2021 7:20:51 pm
Modified By: chengzhu.zhou
-----
Copyright 2021 - 2021 quectel
'''
from machine import I2C
'''
I2C使用示例 
'''

# 参考 http://qpy.quectel.com/wiki/#/zh-cn/api/?id=i2c
# 设置日志输出级别


def test_i2c():
    i2c_dev = I2C(I2C.I2C1, I2C.STANDARD_MODE)
    addres = 0x19
    LIS2DH12_WHO_AM_I = 0x0F  # 板载三轴加速度传感器 身份寄存器
    r_data = bytearray([0x00])  # 存储数据
    i2c_dev.read(addres, bytearray(LIS2DH12_WHO_AM_I), 1,
                 r_data, 1, 1)
    print("read data lis2dh12 who_am_i reg 0x{0:02x}".format(list(r_data)[0]))
    # 读写寄存器
    LIS2DH12_CTRL_REG2 = 0x21  #
    w_data = [0x04]  # 想要写的数据
    print("write 0x04 to 0x21")
    i2c_dev.write(addres, bytearray(LIS2DH12_CTRL_REG2), 1,
                  bytearray(w_data), len(w_data))
    i2c_dev.read(addres, bytearray(LIS2DH12_CTRL_REG2), 1,
                 r_data, 1, 1)
    print("read 0x{0:02x} from 0x{1:02x}".format(
        list(r_data)[0], LIS2DH12_CTRL_REG2))
    print("test_i2c funcation has exited")
    pass
    
if __name__ == "__main__":
    test_i2c()
```

### 配套代码

<!-- * [下载代码](code/i2c_base.py) -->
 <a href="zh-cn/QuecPythonTest/code/i2c_base.py" target="_blank">下载代码</a>