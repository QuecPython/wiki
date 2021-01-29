from machine import Timer

def func(args):
	print('###timer callback function###')
	
timer = Timer(Timer.Timer1)
timer.start(period=1000, mode=timer.PERIODIC, callback=func)