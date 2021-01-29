from machine import Pin
gpio1 = Pin(GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
import utime
i = 1

# GPIOn 整型。引脚号。
	# 引脚对应关系如下：
	# GPIO1–引脚号 22
	# GPIO2–引脚号 23
	# GPIO3–引脚号 178
	# GPIO4–引脚号 199
	# GPIO5–引脚号 204
# direction 整型。
	# IN 输入模式
	# OUT 输出模式
# pullMode 整型。
	# PULL_DISABLE 浮空模式
	# PULL_PU 上拉模式
	# PULL_PD 下拉模式
# level 整型。引脚电平。
	# 0 设置引脚为低电平
	# 1 设置引脚为高电平
	
while i<100:
	gpio1.write(0)
	utime.sleep(1)
	gpio1.write(1)
	utime.sleep(1)
	i += 1