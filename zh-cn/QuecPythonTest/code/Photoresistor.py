'''
File: Photoresistor.py
Project: adc
File Created: Thursday, 24th December 2020 5:44:08 pm
Author: chengzhu.zhou
-----
Last Modified: Wednesday, 30th December 2020 10:10:33 am
Modified By: chengzhu.zhou
-----
Copyright 2020 - 2020 quectel
'''


from misc import ADC
import utime as time
import _thread

# unit as Ω
def Voltage_to_Resistance(Volt):
    #
    Va = 2 * Volt
    resistance = (2 * 4700 * 40200 * Va)/(2 * 4700 * (3300 - Va) - (40200 * Va))
    return resistance


def Photoresistor_thread(delay, retryCount):
    # creat a adc device
    AdcDevice = ADC()
    while retryCount:
        retryCount = retryCount - 1
        # get ADC.ADC0 value
        adcvalue = AdcDevice.read(ADC.ADC0)
        print("get ADC.ADC0 Voltage value as {0}mv".format(adcvalue))
        # Converted to resistance
        resistance = Voltage_to_Resistance(adcvalue)
        print("Photoresistor  resistance as  {0}Ω".format(resistance))
        time.sleep(delay)
    pass


if __name__ == "__main__":
    # creat a thread Convert ADC to Voltage
    _thread.start_new_thread(Photoresistor_thread, (1, 10))
    print("creent main thread has exit")


