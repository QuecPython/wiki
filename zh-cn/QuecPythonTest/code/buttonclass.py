'''
File: buttonclass.py
Project: button
File Created: Thursday, 24th December 2020 5:52:44 pm
Author: chengzhu.zhou
-----
Last Modified: Friday, 25th December 2020 5:30:48 pm
Modified By: chengzhu.zhou
-----
Copyright 2020 - 2020 quectel
'''


# copy from https://blog.csdn.net/qq997758497/article/details/80606710
from machine import Pin
import _thread
import utime as time


def Processing_button_fun(Alias, actionKey):
    print("{0} has {1} action".format(Alias, actionKey))
    pass


class ButtonClass():
    Alias = None
    Gpio_obj = None
    # check quiet click and long
    Status2 = None
    Status1 = None
    callbackfun = None
    timercount2 = None
    timercount1 = None
    # macro
    # readonly
    KEY_ACTION_QUIET = "quiet"
    KEY_ACTION_CLICK = "click"
    KEY_ACTION_DOUBLE = "double"
    KEY_ACTION_LONG = "long"
    # KEY_ACTION = {"quiet": "No key is generated ", "click": "Single key generation",
    #               "double": "Double click the event", "long": "There are long press events"}

    # KeyValue
    KEY_VALUE = {"press": 0, "normal": 1}

    #
    KEY_LONG_MAX_TIME = 2000

    def SetButtonStatu2(self, status="state0", time=0x00):
        self.Status2 = status
        self.timercount2 = time

    def SetButtonStatu1(self, status="state0", time=0x00):
        self.Status1 = status
        self.timercount1 = time

    def __nextstatus(self):
        pass

    def init(self, pin, callbackfun, Alias="gpio0"):
        self.Gpio_obj = Pin(pin, Pin.IN, Pin.PULL_DISABLE, 0)
        self.Alias = Alias
        self.callbackfun = callbackfun
        self.SetButtonStatu2("state0", 0x0)
        self.SetButtonStatu1("state0", 0x0)
        print("init button has success")
        pass

        # return quiet click and long
    def __button_read_key(self):
        _Status = self.Status2
        keyValue = self.Gpio_obj.read()
        if _Status == "state0":
            if keyValue == self.KEY_VALUE["press"]:
                self.SetButtonStatu2("state1", 0x00)
            return self.KEY_ACTION_QUIET

            # Software chattering elimination
        if _Status == "state1":
            if keyValue == self.KEY_VALUE["press"]:
                self.SetButtonStatu2("state2", time.ticks_ms())
            else:
                # reset status
                self.SetButtonStatu2("state0", 0x00)
            return self.KEY_ACTION_QUIET
        elif _Status == "state2":
            if keyValue == self.KEY_VALUE["normal"]:
                # has click occur
                self.SetButtonStatu2("state0", self.timercount2)
                return self.KEY_ACTION_CLICK
            else:
                difftime = time.ticks_ms() - self.timercount2
                if difftime > self.KEY_LONG_MAX_TIME:
                    self.SetButtonStatu2("state0", 0x00)
                    return self.KEY_ACTION_LONG
        elif _Status == "state3":
            # Wait for the key to release
            if keyValue == self.KEY_VALUE["normal"]:
                self.SetButtonStatu2("state0", 0x00)
        return self.KEY_ACTION_QUIET

    def polling(self):
        # check has double click
        _Status = self.Status1
        _KeyStatus = self.__button_read_key()
        retStatus = _KeyStatus
        if _Status == "state0":
            if _KeyStatus != self.KEY_ACTION_CLICK:
                retStatus = _KeyStatus
            else:
                self.SetButtonStatu1("state1", time.ticks_ms())
                # No report
                retStatus = self.KEY_ACTION_QUIET
        elif _Status == "state1":
            difftime = time.ticks_ms() - self.timercount1
            if _KeyStatus == self.KEY_ACTION_CLICK:
                # Second time detected in a short time
                self.SetButtonStatu1("state0", 0x00)
                retStatus = self.KEY_ACTION_DOUBLE
            elif difftime >= 500:
                self.SetButtonStatu1("state0", 0x00)
                retStatus = self.KEY_ACTION_CLICK
        if retStatus != self.KEY_ACTION_QUIET:
            print("{0} has {1}".format(self.Alias, retStatus))
        return retStatus


#
def button_polling_thread(delay, PinList):
    ButtonList = []
    i = 0
    # init button
    for _pin in PinList:
        _temp = ButtonClass()
        _temp.init(_pin, Processing_button_fun, "button{0}".format(i))
        ButtonList.append(_temp)
        i = i + 1
    # Polling button
    i = 10
    while i:
        for button in ButtonList:
            action = button.polling()
            if action != ButtonClass.KEY_ACTION_QUIET:
                # has press
                button.callbackfun(button.Alias, action)
                i = i - 1
        time.sleep_ms(10)
    print("button thread has exited")


if __name__ == "__main__":
    # creat a thread Check key status
    _thread.start_new_thread(button_polling_thread,
                             (1, [Pin.GPIO1, Pin.GPIO2]))
