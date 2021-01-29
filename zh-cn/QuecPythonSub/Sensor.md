#  QuecPython Sensor调试流程

本篇文章主要简介传感器的调试流程，当我们拿到一个新的开发板以后，需要经过怎样的步骤才能调试通一个传感器。下面我们以 调试EC600S V1.1 版本的板载温湿度传感器为例。一步一步确定怎么调试一个传感器。

## 开发分析步骤

### 分析原理图

想要调试传感器，第一件事，分析原理图，确定传感器的型号，参数，引脚等配置。

打开[EC600S 开发板 原理图](https://python.quectel.com/download.html#others)。 

![image-20210121141307016](media/image-20210121141307016.png)

可以看到温湿度传感器型号为 AHT10 ,  6个引脚。 通过SDA SCL引脚和外部通信。

###  查阅数据手册

![image-20210121141532781](media/image-20210121141532781.png)

​	搜索**AHT10 datesheet filetype:pdf**   关键词。 找到datasheet. 推荐使用  **必应**  **谷歌**等搜索引擎。

​    最终找到[aht10规格书v1_1（20191015）.pdf](http://www.aosong.com/userfiles/files/media/aht10%E8%A7%84%E6%A0%BC%E4%B9%A6v1_1%EF%BC%8820191015%EF%BC%89.pdf)

​    查阅datasheet。 我们可以查阅到以下基本信息信息。

    1. AHT10，新一代温湿度传感器
       2. 数字输出，I2C接口。
       3. 引脚定义



![image-20210121142652639](media/image-20210121142652639.png)

还需要提一句的是，当我们想要在开发板上确定芯片的引脚序号时，芯片周围有小白点的引脚就是1号引脚。

然后引脚顺序为逆时针旋转。



### 确定数据交互

知道具体参数以后，需要通过总线和传感器交互数据。具体关于I2C总线的知识不在本篇文章中讲解，建议 [I²C（IIC）总线协议详解—完整版](https://zhuanlan.zhihu.com/p/149364473)。

阅读数据手册。确定传感器的开发流程。以下步骤都是在传感器上电以后的操作。

1. 上电后要等待40ms，读取温湿值之前，首 先要看状态字的校准使能位Bit[3]是否为 1 ，如 果 不 为1 ，要 发 送**0XE1**命 令 （ 初 始 化），此命令参数有两个字节，第一个字节 为**0x08**，第二个字节为**0x00**。
2. 直接发送等待7 5 m s待测量完成，忙状态**Bit[7]**为 0，然后可以读取六个字节（发**0X71**即可以 读取）。命令（触发测量），此命令 参数有两个字节，第一个字节为**0x33**，第二 个字节为**0x00**。
3. 等待75ms待测量完成，忙状态**Bit[7]**为 0，然后可以读取六个字节（发**0X71**即可以 读取）。
4. 计算温湿度值。

![image-20210121144624090](media/image-20210121144624090.png)

```
write: 0x70 0xac 0x33 0x00
```



![image-20210121144644579](media/image-20210121144644579.png)

```
write: 0x71  
read: 6个字节
```

将6个字节读取出来。

## 开发过程

上面我们确定了传感器的初始化，以及使能命令。 下面我们来写程序，使能传感器。

### 声明变量

```python
from machine import I2C
import utime as time
# 声明一个I2C 对象
i2c_dev = I2C(I2C.I2C1, I2C.STANDARD_MODE)
i2c_addre = 0x38
```

### 读写函数

```python
def read_data(length):
    r_data = [0x00 for i in range(length)]
    r_data = bytearray(r_data)
    i2c_dev.read(i2c_addre,
                 bytearray(0x00), 0x0,
                 r_data, length,
                 0)
    return list(r_data)


def write_data(data):
    i2c_dev.write(i2c_addre,
                  bytearray(0x00), 0,
                  bytearray(data), len(data))

```

### 初始化函数,触发检测函数

```python
def init():
    # 设置校准位
    write_data([0xE1, 0x08, 0x00])
    time.sleep_ms(300)  # at last 300ms


def trigger_measure():
    write_data([0xac, 0x33, 0x00])
    pass
```

### 温度转换函数

```python
def aht10_transformation_temperature(data):
    r_data = data
    #　根据数据手册的描述来转化温度
    humidity = (r_data[0] << 12) | (
        r_data[1] << 4) | ((r_data[2] & 0xF0) >> 4)
    humidity = (humidity/(1 << 20)) * 100.0
    print("current humidity is {0}%".format(humidity))
    temperature = ((r_data[2] & 0xf) << 16) | (
        r_data[3] << 8) | r_data[4]
    temperature = (temperature * 200.0 / (1 << 20)) - 50
    print("current temperature is {0}°C".format(temperature))


def read_temperature():
    r_data = read_data(6)
    print(r_data)
    aht10_transformation_temperature(r_data[1:6])
    pass
```

### 运行

```python
init()
while True:
    trigger_measure()
    time.sleep_ms(100)
    read_temperature()
    time.sleep_ms(500)
```

### 完整代码

```python
from machine import I2C
import utime as time
# 声明一个I2C 对象
i2c_dev = I2C(I2C.I2C1, I2C.STANDARD_MODE)
i2c_addre = 0x38


def read_data(length):
    r_data = [0x00 for i in range(length)]
    r_data = bytearray(r_data)
    i2c_dev.read(i2c_addre,
                 bytearray(0x00), 0x0,
                 r_data, length,
                 0)
    return list(r_data)


def write_data(data):
    i2c_dev.write(i2c_addre,
                  bytearray(0x00), 0,
                  bytearray(data), len(data))


def init():
    # 设置校准位
    write_data([0xE1, 0x08, 0x00])
    time.sleep_ms(300)  # at last 300ms


def trigger_measure():
    write_data([0xac, 0x33, 0x00])
    pass

# 温湿度转换函数


def aht10_transformation_temperature(data):
    r_data = data
    #　根据数据手册的描述来转化温度
    humidity = (r_data[0] << 12) | (
        r_data[1] << 4) | ((r_data[2] & 0xF0) >> 4)
    humidity = (humidity/(1 << 20)) * 100.0
    print("current humidity is {0}%".format(humidity))
    temperature = ((r_data[2] & 0xf) << 16) | (
        r_data[3] << 8) | r_data[4]
    temperature = (temperature * 200.0 / (1 << 20)) - 50
    print("current temperature is {0}°C".format(temperature))


def read_temperature():
    r_data = read_data(6)
    print(r_data)
    aht10_transformation_temperature(r_data[1:6])
    pass


init()
while True:
    trigger_measure()
    time.sleep_ms(100)
    read_temperature()
    time.sleep_ms(500)

```


<!-- * [下载代码](code/example_sensor_base.py) -->
 <a href="zh-cn/QuecPythonSub/code/example_sensor_base.py" target="_blank">下载代码</a>