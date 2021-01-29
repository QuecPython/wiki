from machine import Pin


gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
ret = gpio1.write(1)
print(ret)
ret = gpio1.read()
print(ret)
ret = gpio1.write(0)
print(ret)
ret = gpio1.read()
print(ret)
