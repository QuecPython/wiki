# 实验1：	AliyunCloud 实验
# API资料参考连接：  https://python.quectel.com/wiki/api/#umqtt-mqtt


from umqtt import MQTTClient
import modem

CLIENT_ID = b'22222|securemode=3,signmethod=hmacsha1|'
SERVER = b'a1llZotKkCm.iot-as-mqtt.cn-shanghai.aliyuncs.com'
PORT = 1883
USER = b'22222&a1llZotKkCm'
PASSWORD = b'CD31C5E9C8633B174A6E9C2A97D04FCD8EF73BB4'

IMEI = None  # modem.getDevImei()
SUB_TOPIC = '/broadcast/a1llZotKkCm/{}'
PUB_TOPIC = SUB_TOPIC


def GetDevImei():
    global IMEI
    IMEI = modem.getDevImei()
    print('IMEI:{}'.format(IMEI))


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
    c.publish(PUB_TOPIC.format(IMEI), b"test publish")

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
