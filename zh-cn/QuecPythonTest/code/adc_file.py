from misc import ADC  # 导入ADC模块
import utime    # 导入定时模块
read_time = 5   # 设定读取次数
adc = ADC()
while read_time:
    adc.open()
    read_data = adc.read(ADC.ADC0)
    print(read_data)
    adc.close()
    read_time -= 1
    utime.sleep(1)  # 延时1S
