'''
File: i2c_aht10.py
Project: i2c
File Created: Monday, 28th December 2020 5:17:28 pm
Author: chengzhu.zhou
-----
Last Modified: Tuesday, 29th December 2020 9:01:35 pm
Modified By: chengzhu.zhou
-----
Copyright 2020 - 2020 quectel
'''

import log
from machine import I2C
import utime as time
"""
1. calibration
2. Trigger measurement
3. read data
"""

# API  手册 http://qpy.quectel.com/wiki/#/zh-cn/api/?id=i2c
# AHT10 说明书
#  https://server4.eca.ir/eshop/AHT10/Aosong_AHT10_en_draft_0c.pdf


class aht10class():
    i2c_log = None
    i2c_dev = None
    i2c_addre = None

    # Initialization command
    AHT10_CALIBRATION_CMD = 0xE1
    # Trigger measurement
    AHT10_START_MEASURMENT_CMD = 0xAC
    # reset
    AHT10_RESET_CMD = 0xBA

    def write_data(self, data):
        self.i2c_dev.write(self.i2c_addre,
                           bytearray(0x00), 0,
                           bytearray(data), len(data))
        pass

    def read_data(self, length):
        r_data = [0x00 for i in range(length)]
        r_data = bytearray(r_data)
        self.i2c_dev.read(self.i2c_addre,
                          bytearray(0x00), 0,
                          r_data, length,
                          0)
        return list(r_data)

    def aht10_init(self, addre=0x38, Alise="Ath10"):
        self.i2c_log = log.getLogger(Alise)
        self.i2c_dev = I2C(I2C.I2C1, I2C.STANDARD_MODE)  # 返回i2c对象
        self.i2c_addre = addre
        self.sensor_init()
        pass

    def aht10_transformation_temperature(self, data):
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
        

    def sensor_init(self):
        # calibration
        self.write_data([self.AHT10_CALIBRATION_CMD, 0x08, 0x00])
        time.sleep_ms(300)  # at last 300ms
        pass

    def ath10_reset(self):
        self.write_data([self.AHT10_RESET_CMD])
        time.sleep_ms(20)  # at last 20ms

    def Trigger_measurement(self):
        # Trigger data conversion
        self.write_data([self.AHT10_START_MEASURMENT_CMD, 0x33, 0x00])
        time.sleep_ms(200)  # at last delay 75ms
        # check has success
        r_data = self.read_data(6)
        # check bit7
        if (r_data[0] >> 7) != 0x0:
            print("Conversion has error")
        else:
            self.aht10_transformation_temperature(r_data[1:6])


def i2c_aht10_test():
    ath_dev = aht10class()
    ath_dev.aht10_init()

    # 测试十次
    for i in range(10):
        ath_dev.Trigger_measurement()
        time.sleep(1)


if __name__ == "__main__":
    i2c_aht10_test()
