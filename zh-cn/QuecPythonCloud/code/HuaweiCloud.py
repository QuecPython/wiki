# 实验1：	HuaweiCloud 实验
# API资料参考连接：  https://python.quectel.com/wiki/api/#umqtt-mqtt


from umqtt import MQTTClient

CLIENT_ID = b'5fbbb784b4ec2202e982e643_868540050954037_0_0_2021011909'
SERVER = b'a15fbbd7ce.iot-mqtts.cn-north-4.myhuaweicloud.com'
PORT = 1883
USER = b'5fbbb784b4ec2202e982e643_868540050954037'
PASSWORD = b'8001a12405743199b3396943a2ed397286117a9ebab4f5dfda8dd6fafe341d94'

DEVICE_ID = '5fbbb784b4ec2202e982e643_868540050954037'

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
    c.connect()
    # 订阅主题
    c.subscribe('$oc/devices/{}/sys/messages/down'.format(DEVICE_ID))

    msg = b'''{
        "services": [{
            "service_id": "WaterMeterControl",
            "properties": {
                "state": "T:15c,  H: 85% "
            },
            "event_time": "20151212T121212Z"
        }
        ]
    }'''

    # 发布消息
    c.publish('$oc/devices/{}/sys/properties/report'.format(DEVICE_ID), msg)

    while True:
        c.wait_msg()
        if state == 1:
            break

    # 关闭连接
    c.disconnect()


def main():
    MQTT_Init()


if __name__ == "__main__":
    main()
