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
