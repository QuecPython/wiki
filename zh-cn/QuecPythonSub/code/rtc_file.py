from machine import RTC
rtc = RTC()
rtc_before_set = rtc.datetime()  # 查询日期时间
print(rtc_before_set)  # 打印时间
rtc.datetime([2020, 3, 12, 1, 12, 12, 12, 0])  # 设置时间
rtc_after_set = rtc.datetime()  # 查询日期时间
print(rtc_after_set)  # 打印时间
