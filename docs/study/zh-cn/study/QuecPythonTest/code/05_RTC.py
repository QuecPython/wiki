# 实验1：	RTC实验
# API资料参考连接：  https://python.quectel.com/wiki/#/zh-cn/api/?id=rtc


from machine import RTC

rtc = None  # 定义全局变量
year = 0   # 定义全局变量
month = 0  # 定义全局变量
day = 0  # 定义全局变量
week = 0  # 定义全局变量
hour = 0  # 定义全局变量
minute = 0  # 定义全局变量
second = 0  # 定义全局变量


def readTime():
    global rtc  # 声明全部变量
    if rtc is None:  # 判断是否已经被创建
        rtc = RTC()  # 创建一个RTC对象
    time = rtc.datetime()  # 读RTC时间
    global year, month, day, week, hour, minute, second  # 声明全部变量
    year = time[0]  # 提取变量
    month = time[1]  # 提取变量
    day = time[2]  # 提取变量
    week = time[3]  # 提取变量
    hour = time[4]  # 提取变量
    minute = time[5]  # 提取变量
    second = time[6]  # 提取变量


def setTime(year, month, day, hour, minute, second):
    global rtc  # 声明全部变量
    if rtc is None:  # 判断是否已经被创建
        rtc = RTC()  # 创建一个RTC对象
    rtc.datetime([year, month, day, 0, hour, minute, second, 0])  # 设置RTC时间


def main():
    readTime()  # 读时间
    print(year, month, day, week, hour, minute, second,)  # 打印信息

    # 设置时间
    setTime(year - 1, month - 1, day - 1, hour - 1, minute - 1, second - 1)
    readTime()  # 读时间
    print(year, month, day, week, hour, minute, second, )  # 打印信息


if __name__ == "__main__":
    main()
