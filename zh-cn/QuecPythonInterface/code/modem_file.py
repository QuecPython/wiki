import modem
import log

state = 1
log.basicConfig(level=log.INFO)   # 设置日志输出级别

log = log.getLogger("QuecPython")

def modem_msg():
    global state
    modem_Imei = modem.getDevImei()
    modem_DevModel = modem.getDevModel()
    modem_DevSN = modem.getDevSN()
    modem_DevFwVersion = modem.getDevFwVersion()
    modem_DevProductId = modem.getDevProductId()
    log.info("modem_Imei:{}".format(modem_Imei))
    log.info("modem_DevModel:{}".format(modem_DevModel))
    log.info("modem_DevSN:{}".format(modem_DevSN))
    log.info("modem_DevFwVersion:{}".format(modem_DevFwVersion))
    log.info("modem_DevProductId:{}".format(modem_DevProductId))
    state = 0

if __name__ == "__main__":
    modem_msg()
    while 1:
        if state:
            pass
        else:
            break
