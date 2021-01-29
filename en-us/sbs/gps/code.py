from machine import UART
import utime
import modem
import _thread
uart = UART(2,115200,8,0,1,0)

def gngga():
	while True:
		#获取当前 RTC 时间
		time = utime.localtime( )
		#获取设备 IMET
		imei = modem.getDevImei( )
		if uart.any() > 0:
			buf = uart.read(uart.any())
			buf = str(buf,"utf8" )
			try :
				gngga1 = buf.split("$GNGGA,")[1].split("\r\n" )[0].split(",")
				# UTC 时间，hhmmss.sss,时分秒格式
				time_gps = gngga1[0]
				#纬度 ddmm.mmmm,度分格式前导位数不足则补 0
				_latitude = float(gngga1[1])
				#经度 dddmm.mmmm,度分格式前导位数不足则补 0
				_longitude = float(gngga1[3])
				# UTC 时间转化
				_Clock = int(time[0:2])
				_Minute = time[2:4]
				_Second = time[4:6]
				_Clock =_Clock + 8
				#防止超过 24 小时
				if (_Clock >= 24):
					_Clock = _Clock % 24
					#最终获得时间
					Effect_time = str(_clock) + ':' +_Minute + ':' +_Second
					#最终获得纬度
					Effect_latitude = int(_latitude / 100)+ ((_latitude % 100) / 60)
					#最终获得经度
					Effect_longitude = int(_longitude / 100) +((_longitude % 100)/ 60)
					print( '当前时间:',time)
					print( 'GPS 时间:',Effect_time)
					print('设备 IMET',imei)
					print(gngga1[2],'',str(Effect_latitude ))
					print(gngga1[4],'',str(Effect_longitude ))
					utime.sleep(2)
			except:
				print('数据格式有误或数据受损')
				continue

def run():
	_thread.start_new_thread(gngga, ())
run()