
# 参考 https://python.quectel.com/wiki/#/zh-cn/api/?id=datacall-%e6%95%b0%e6%8d%ae%e6%8b%a8%e5%8f%b7

import dataCall
import net
import utime as time


g_net_status = False


def callback(args):
    pdp = args[0]
    nw_sta = args[1]
    if nw_sta == 1:
        g_net_status = True
        print("*** network %d connected! ***" % pdp)
    else:
        g_net_status = False
        print("*** network %d not connected! ***" % pdp)
        # 重新进入
        test_datacall_module()


def test_datacall_module():
    # 拨号
    ret = dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
    if ret == 0:
        print("datacall start has success")
        g_net_status = True
    # 获取IP地址等信息
    Info = dataCall.getInfo(1, 0)
    print(Info)
    print("test datacall has exit")
    pass


def test_datacall_callback():
    test_datacall_module()
    # 注册回调中断
    ret = dataCall.setCallback(callback)
    if ret == 0x00:
        print("set Callback has success")
    net.setModemFun(4)  # 进入飞行模式
    time.sleep_ms(1000)
    net.setModemFun(1)  # 重新进入正常模式
    print("test_datacall_callback funcation has exited")
    pass


if __name__ == "__main__":
    test_datacall_callback()
