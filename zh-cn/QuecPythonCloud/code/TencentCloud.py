# 实验1：	TencentCloud 实验
# API资料参考连接：  https://python.quectel.com/wiki/api/#umqtt-mqtt


from umqtt import MQTTClient
import modem

CLIENT_ID = b'X3Z30XABBU001'
SERVER = b'X3Z30XABBU.iotcloud.tencentdevices.com'
PORT = 1883
USER = b'X3Z30XABBU001;12010126;M8STP;1647306844'
PASSWORD = b'e181d0cfaf5540c8e3f173a6e88efa1f3d34db2db7a9ff845aedc67f48d9d607;hmacsha256'

IMEI = None  # modem.getDevImei()
SUB_TOPIC = 'X3Z30XABBU/{}/data'
PUB_TOPIC = SUB_TOPIC


def GetDevImei():
    global IMEI
    # IMEI = modem.getDevImei()
    IMEI= '001'
    print(IMEI)


state = 0


def sub_cb(topic, msg):
    global state
    print(
        "Subscribe Recv: Topic={},Msg={}".format(
            topic.decode(),
            msg.decode()))
    state = 1


def MQTT_Init():
    # 创建一个mqtt实例
    c = MQTTClient(
        client_id=CLIENT_ID,
        server=SERVER,
        port=PORT,
        user=USER,
        password=PASSWORD,
        keepalive=30)  # 必须要 keepalive=30 ,否则连接不上
    # 设置消息回调
    c.set_callback(sub_cb)
    # 建立连接
    try:
        c.connect()
    except Exception as e:
        print('!!!,e=%s' % e)
        return
    # c.connect()
    # 订阅主题
    c.subscribe(SUB_TOPIC.format(IMEI))
    # 发布消息
    Payload = '{"DeviceName":"{}","msg":"test publish"}'.format(IMEI)
    c.publish(PUB_TOPIC.format(IMEI), Payload)

    while True:
        c.wait_msg()
        if state == 1:
            break

    # 关闭连接
    c.disconnect()


def main():
    GetDevImei()
    MQTT_Init()


if __name__ == "__main__":
    main()
