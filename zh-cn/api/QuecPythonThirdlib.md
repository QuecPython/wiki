### 第三方库

#### aLiYun - 阿里云服务

模块功能：阿里云物联网套件客户端功能,目前的产品节点类型仅支持“设备”，设备认证方式支持“一机一密和“一型一密”。

> **aLiYun(productKey, productSecret, DeviceName, DeviceSecret)**

配置阿里云物联网套件的产品信息和设备信息。

* 参数

| 参数          | 类型   | 说明                                                         |
| :------------ | :----- | ------------------------------------------------------------ |
| productKey    | string | 产品标识                                                     |
| productSecret | string | 可选参数，默认为None，productSecret，产品密钥<br />一机一密认证方案时，此参数传入None<br/>一型一密认证方案时，此参数传入真实的产品密钥 |
| DeviceName    | string | 设备名称                                                     |
| DeviceSecret  | string | 可选参数,默认为Non，设备密钥（一型一密认证方案时此参数传入None） |

* 返回值

返回aLiYun连接对象。



> **aLiYun.setMqtt(clientID, clean_session, keepAlive)**

设置MQTT数据通道的参数

**需要注意的是，当进行阿里云的一型一密连接的时候，会在本地生成secret.json的文件用以保存设备的设备密钥，如果重刷固件或者删除，再进行连接的时候会因为没有secret.json而报错，所以重刷固件或者删除了secert.json文件，需要手动新建secret.json文件，下面secret.json文件的模板**

```
{
  "Test01": "9facf9aba414ec9eea7c10d8a4cb69a0"
}
# Test01 : 设备名
# "9facf9aba414ec9eea7c10d8a4cb69a0" 设备密钥
```



* 参数

| 参数          | 类型   | 说明                                                         |
| :------------ | :----- | ------------------------------------------------------------ |
| clientID      | string | 自定义阿里云连接id                                           |
| clean_session | bool   | 可选参数，一个决定客户端类型的布尔值。 如果为True，那么代理将在其断开连接时删除有关此客户端的所有信息。 如果为False，则客户端是持久客户端，当客户端断开连接时，订阅信息和排队消息将被保留。默认为False |
| keepAlive     | int    | 通信之间允许的最长时间段（以秒为单位）,默认为300，范围（60-1200） |

* 返回值

成功返回整型值0，失败返回整型值-1。



> **aLiYun.setCallback(sub_cb)**

注册回调函数。

* 参数

| 参数   | 类型     | 说明     |
| :----- | :------- | -------- |
| sub_cb | function | 回调函数 |

* 返回值

无



> **aLiYun.subscribe(topic,qos)**

订阅mqtt主题。

* 参数

| 参数  | 类型   | 说明                                                         |
| :---- | :----- | ------------------------------------------------------------ |
| topic | string | topic                                                        |
| qos   | int    | MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker |

* 返回值

成功返回整型值0，失败返回整型值-1。



> **aLiYun.publish(topic,msg, qos=0)**

发布消息。

* 参数

| 参数  | 类型   | 说明                                                         |
| :---- | :----- | ------------------------------------------------------------ |
| topic | string | topic                                                        |
| msg   | string | 需要发送的数据                                               |
| qos   | int    | MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker |

* 返回值 

成功返回整型值0，失败返回整型值-1。



> **aLiYun.start()**

运行连接。

* 参数

无

* 返回值

无



> **aLiYun.disconnect()**

关闭连接。

* 参数

无

* 返回值

无



**使用示例**

```python
'''
@Author: Pawn
@Date: 2020-09-28
@Description: example for module aLiYun
@FilePath: example_aliyun_file.py
'''
import log
import utime
import checkNet
from aLiYun import aLiYun

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_AliYin_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)


# 设置日志输出级别
log.basicConfig(level=log.INFO)
aliYun_log = log.getLogger("ALiYun")

productKey = ""  # 产品标识(参照阿里云应用开发指导)
productSecret = None  # 产品密钥（使用一机一密认证时此参数传入None，参照阿里云应用开发指导)
DeviceName = ""  # 设备名称(参照阿里云应用开发指导)
DeviceSecret = ""  # 设备密钥（使用一型一密认证此参数传入None，免预注册暂不支持，需先在云端创建设备，参照阿里云应用开发指导)

state = 5

# 回调函数
def sub_cb(topic, msg):
    global state
    aliYun_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    state -= 1


if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        aliYun_log.info('Network connection successful!')
        # 创建aliyun连接对象
        ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret)

        # 设置mqtt连接属性
        clientID = ""  # 自定义字符（不超过64）
        ali.setMqtt(clientID, clean_session=False, keepAlive=300)

        # 设置回调函数
        ali.setCallback(sub_cb)
        topic = ""  # 云端自定义或自拥有的Topic
        # 订阅主题
        ali.subscribe(topic)
        # 发布消息
        ali.publish(topic, "hello world")
        # 运行
        ali.start()

        while 1:
            if state:
                pass
            else:
                ali.disconnect()
                break
    else:
        aliYun_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

```



#### TenCentYun- 腾讯云服务

模块功能：腾讯云物联网套件客户端功能,目前的产品节点类型仅支持“设备”，设备认证方式支持“一机一密和“动态注册认证”。

> **TXyun(productID, devicename, devicePsk, ProductSecret)**

配置阿里云物联网套件的产品信息和设备信息。

* 参数

| 参数          | 类型   | 说明                                                         |
| :------------ | :----- | ------------------------------------------------------------ |
| productID     | string | 产品标识（唯一ID）                                           |
| ProductSecret | string | 可选参数，默认为None，productSecret，产品密钥<br />一机一密认证方案时，此参数传入None<br/>一型一密认证方案时，此参数传入真实的产品密钥 |
| devicename    | string | 设备名称                                                     |
| devicePsk     | string | 可选参数,默认为Non，设备密钥（一型一密认证方案时此参数传入None） |

* 返回值

返回TXyun连接对象。



> **TXyun.setMqtt(clean_session, keepAlive)**

设置MQTT数据通道的参数

* 参数

| 参数          | 类型 | 说明                                                         |
| :------------ | :--- | ------------------------------------------------------------ |
| clean_session | bool | 可选参数，一个决定客户端类型的布尔值。 如果为True，那么代理将在其断开连接时删除有关此客户端的所有信息。 如果为False，则客户端是持久客户端，当客户端断开连接时，订阅信息和排队消息将被保留。默认为False |
| keepAlive     | int  | 通信之间允许的最长时间段（以秒为单位）,默认为300，范围（60-1000），建议300以上 |

* 返回值

成功返回整型值0，失败返回整型值-1。



> **TXyun.setCallback(sub_cb)**

注册回调函数。

* 参数

| 参数   | 类型     | 说明                                       |
| :----- | :------- | ------------------------------------------ |
| sub_cb | function | 设置消息回调函数，当服务端响应时触发该方法 |

* 返回值

无



> **TXyun.subscribe(topic,qos)**

订阅mqtt主题。

* 参数

| 参数  | 类型   | 说明                                                         |
| :---- | :----- | ------------------------------------------------------------ |
| topic | string | topic                                                        |
| qos   | int    | MQTT消息服务质量（默认0，可选择0或1）MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker |

* 返回值

成功返回整型值0，失败返回整型值-1。



> **TXyun.publish(topic,msg, qos=0)**

发布消息。

* 参数

| 参数  | 类型   | 说明                                                         |
| :---- | :----- | ------------------------------------------------------------ |
| topic | string | topic                                                        |
| msg   | string | 需要发送的数据                                               |
| qos   | int    | MQTT消息服务质量（默认0，可选择0或1）MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker |

* 返回值 

成功返回整型值0，失败返回整型值-1。



> **TXyun.start()**

运行连接。

* 参数

无

* 返回值

无



> **TXyun.disconnect()**

关闭连接。

* 参数

无

* 返回值

无



**使用示例**

```python
from TenCentYun import TXyun
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_TencentYun_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
txyun_log = log.getLogger("TenCentYun")

'''
腾讯云物联网套件客户端功能
'''
productID = ""  # 产品标识（参照接入腾讯云应用开发指导）
devicename = ""   # 设备名称（参照接入腾讯云应用开发指导）
devicePsk = ""   # 设备密钥（一型一密认证此参数传入None， 参照接入腾讯云应用开发指导）
ProductSecret = None   # 产品密钥（一机一密认证此参数传入None，参照接入腾讯云应用开发指导）

tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)  # 创建连接对象
state = 5

def sub_cb(topic, msg):   # 云端消息响应回调函数
    global state
    txyun_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    state -= 1


if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        txyun_log.info('Network connection successful!')

        tenxun.setMqtt()  # 设置mqtt
        tenxun.setCallback(sub_cb)   # 设置消息回调函数
        topic = ""  # 输入自定义的Topic
        tenxun.subscribe(topic)   # 订阅Topic
        tenxun.start()
        tenxun.publish(topic, "hello world")   # 发布消息

        while 1:
            if state:
                pass
            else:
                tenxun.disconnect()
                break
    else:
        txyun_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

```



#### request - HTTP

模块功能：HTTP客户端的相关功能函数。

> **request.get(url, data, headers,decode,sizeof,ssl_params)**

发送GET请求。

* 参数

| 参数    | 类型   | 说明                                                         |
| ------- | ------ | ------------------------------------------------------------ |
| url     | string | 网址                                                         |
| data    | json   | （可选参数）附加到请求的正文，json类型，默认为None           |
| headers | dict   | （可选参数）请求头，默认为None                               |
| decode  | bool   | （可选参数）True 将响应的内容解码返回str类型  False 关闭解码返回bytes类型 默认True(仅配合response.content使用) |
| sizeof  | int    | （可选参数）读取缓冲区的数据块大小 默认255 个字节 数值越大读取的速度越快（如果设置过大可能就会有丢失数据的可能性，建议255-4096） |
| ssl_params | dict   | （可选参数）SSL双向认证 {"cert": certificate_content, "key": private_content} 传入证书的公钥密钥 |

* 示例

```python
import request
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Requect_get_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
http_log = log.getLogger("HTTP GET")

url = "http://httpbin.org/get"

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        http_log.info('Network connection successful!')
        response = request.get(url)   # 发起http GET请求
        http_log.info(response.json())  # 以json方式读取返回
    else:
        http_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```



> **request.post(url, data, headers,decode,sizeof)**

发送POST请求。

* 参数

| 参数    | 类型   | 说明                                                         |      |
| ------- | ------ | ------------------------------------------------------------ | ---- |
| url     | string | 网址                                                         |      |
| data    | json   | （可选参数）附加到请求的正文，json类型，默认为None           |      |
| headers | dict   | （可选参数）请求头，默认为None                               |      |
| decode  | bool   | （可选参数）True 将响应的内容解码返回str类型  False 关闭解码返回bytes类型 默认True |      |
| sizeof  | int    | （可选参数）读取缓冲区的数据块大小 默认255 个字节 数值越大读取的速度越快（如果设置过大可能就会有丢失数据的可能性，建议255-4096） |      |

* 示例

```python
import request
import ujson
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Requect_post_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
http_log = log.getLogger("HTTP POST")

url = "http://httpbin.org/post"
data = {"key1": "value1", "key2": "value2", "key3": "value3"}

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        http_log.info('Network connection successful!')

        # POST请求
        response = request.post(url, data=ujson.dumps(data))   # 发送HTTP POST请求
        http_log.info(response.json())
    else:
        http_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```



> **request.put(url, data, headers,decode,sizeof)**

发送PUT请求。

* 参数

| 参数    | 类型   | 说明                                                         |
| ------- | ------ | ------------------------------------------------------------ |
| url     | string | 网址                                                         |
| data    | json   | （可选参数）附加到请求的正文，json类型，默认为None           |
| headers | dict   | （可选参数）请求头，默认为None                               |
| decode  | bool   | （可选参数）True 将响应的内容解码返回str类型  False 关闭解码返回bytes类型 默认True（注意: 只配合response.content使用） |
| sizeof  | int    | （可选参数）读取缓冲区的数据块大小 默认255 个字节 数值越大读取的速度越快（如果设置过大可能就会有丢失数据的可能性，建议255-4096） |

* 示例

```python
import request
url = "http://httpbin.org/put"
response = request.put(url)
```



> **request.head(url, data, headers,decode,sizeof)**

发送HEAD请求。

* 参数

| 参数    | 类型   | 说明                                                         |
| ------- | ------ | ------------------------------------------------------------ |
| url     | string | 网址                                                         |
| data    | json   | （可选参数）附加到请求的正文，json类型，默认为None           |
| headers | dict   | （可选参数）请求头，默认为None                               |
| decode  | bool   | （可选参数）True 将响应的内容解码返回str类型  False 关闭解码返回bytes类型 默认True |
| sizeof  | int    | （可选参数）读取缓冲区的数据块大小 默认255 个字节 数值越大读取的速度越快（如果设置过大可能就会有丢失数据的可能性，建议255-4096） |

* 示例

```python
import request
url = "http://httpbin.org/head"
response = request.head(url)
print(response.headers)
```

**Response类方法说明**

> **response =request.get(url)**

| 方法             | 说明                                                   |
| ---------------- | ------------------------------------------------------ |
| response.content | 返回响应内容的生成器对象（使用方法详见下面的使用示例） |
| response.text    | 返回文本方式响应内容的生成器对象                       |
| response.json()  | 返回响应的json编码内容并转为dict类型                   |



**request使用示例**

```python
import request
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Requect_SSL_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
http_log = log.getLogger("HTTP SSL")
# https请求
url = "https://myssl.com"

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        http_log.info('Network connection successful!')

        response = request.get(url)  # 支持ssl
        for i in response.text:
            print(i)
    else:
        http_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```



#### log - 日志

模块功能：系统日志记录,分级别日志工具。

> **log.basicConfig(level)**

设置日志输出级别,  设置日志输出级别, 默认为log.INFO，系统只会输出 level 数值大于或等于该 level 的的日志结果。

* 参数

| 参数     | 参数类型 | 说明                  |
| -------- | -------- | --------------------- |
| CRITICAL | 常量     | 日志记录级别的数值 50 |
| ERROR    | 常量     | 日志记录级别的数值 40 |
| WARNING  | 常量     | 日志记录级别的数值 30 |
| INFO     | 常量     | 日志记录级别的数值 20 |
| DEBUG    | 常量     | 日志记录级别的数值 10 |
| NOTSET   | 常量     | 日志记录级别的数值 0  |

* 示例

```python
import log
log.basicConfig(level=log.INFO)
```



> **log.getLogger(name)**

获取logger对象，如果不指定name则返回root对象，多次使用相同的name调用getLogger方法返回同一个logger对象。

* 参数

| 参数 | 参数类型 | 说明     |
| ---- | -------- | -------- |
| name | string   | 日志主题 |

* 返回值

log对象。

* 示例

```python
import log
Testlog = log.getLogger("TestLog")
```



> **log.debug(tag, msg)**

输出debug级别的日志。

* 参数

| 参数 | 参数类型 | 说明                         |
| ---- | -------- | ---------------------------- |
| tag  | string   | 模块或功能名称，作为日志前缀 |
| msg  | string   | 可变参数，日志内容           |

* 返回值

无

* 示例 

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.debug("Test message: %d(%s)", 100, "foobar")
```



> **log.info(tag,msg)**

输出info级别的日志。

* 参数

| 参数 | 参数类型 | 说明                         |
| ---- | -------- | ---------------------------- |
| tag  | string   | 模块或功能名称，作为日志前缀 |
| msg  | string   | 可变参数，日志内容           |

* 返回值

无

* 示例

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.info("Test message: %d(%s)", 100, "foobar")
```



> **log.warning(tag,msg)**

输出warning级别的日志。

* 参数

| 参数 | 参数类型 | 说明                         |
| ---- | -------- | ---------------------------- |
| tag  | string   | 模块或功能名称，作为日志前缀 |
| msg  | string   | 可变参数，日志内容           |

* 返回值

无

* 示例

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.warning("Test message: %d(%s)", 100, "foobar")
```



> **log.error(tag,msg)**

输出error级别的日志。

* 参数

| 参数 | 参数类型 | 说明                         |
| ---- | -------- | ---------------------------- |
| tag  | string   | 模块或功能名称，作为日志前缀 |
| msg  | string   | 可变参数，日志内容           |

* 返回值

无

* 示例

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.error("Test message: %d(%s)", 100, "foobar")
```



> **log.critical(tag,msg)**

输出critical级别的日志。

* 参数

| 参数 | 参数类型 | 说明                         |
| ---- | -------- | ---------------------------- |
| tag  | string   | 模块或功能名称，作为日志前缀 |
| msg  | string   | 可变参数，日志内容           |

* 返回值

无

* 示例

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.critical("Test message: %d(%s)", 100, "foobar")
```



**log使用示例**

```python
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Log_example"
PROJECT_VERSION = "1.0.0"

# 设置日志输出级别
log.basicConfig(level=log.ERROR)
# 获取logger对象，如果不指定name则返回root对象，多次使用相同的name调用getLogger方法返回同一个logger对象
log = log.getLogger("error")

if __name__ == '__main__':
    log.error("Test error message!!")
	log.debug("Test debug message!!")
    log.critical("Test critical message!!")
    log.info("Test info message!!")
    log.warning("Test warning message!!")
```



#### umqtt - MQTT

模块功能:提供创建MQTT客户端发布订阅功能。

```
QoS级别说明
在MQTT协议中，定义了三个级别的QoS，分别是：
QoS0 – 最多一次，是最低级别；发送者发送完消息之后，并不关心消息是否已经到达接收方；
QoS1 – 至少一次，是中间级别；发送者保证消息至少送达到接收方一次；
QoS2 – 有且仅有一次，是最高级别；保证消息送达且仅送达一次。
```



> **MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0, ssl=False, ssl_params={})**

构建mqtt连接对象。

* 参数

| 参数       | 参数类型 | 说明                                                         |
| ---------- | -------- | ------------------------------------------------------------ |
| client_id  | string   | 客户端 ID，具有唯一性                                        |
| server     | string   | 服务端地址，可以是 IP 或者域名                               |
| port       | int      | 服务器端口（可选）。 默认为1883，请注意，MQTT over SSL/TLS的默认端口是8883 |
| user       | string   | （可选) 在服务器上注册的用户名                               |
| password   | string   | （可选) 在服务器上注册的密码                                 |
| keepalive  | int      | （可选）客户端的keepalive超时值。 默认为0，范围（60~1200）s  |
| ssl        | bool     | （可选）是否使能 SSL/TLS 支持                                |
| ssl_params | string   | （可选）SSL/TLS 参数                                         |

* 返回值 

mqtt对象。



> **MQTTClient.set_callback(callback)**

设置回调函数，收到消息时会被调用。

* 参数 

| 参数     | 参数类型 | 说明         |
| -------- | -------- | ------------ |
| callback | function | 消息回调函数 |

* 返回值

无



> **MQTTClient.set_last_will(topic,msg,retain=False,qos=0)**

设置要发送给服务器的遗嘱，客户端没有调用disconnect()异常断开，则发送通知到客户端。

* 参数

| 参数   | 参数类型 | 说明                                         |
| ------ | -------- | -------------------------------------------- |
| topic  | string   | 遗嘱主题                                     |
| msg    | string   | 遗嘱的内容                                   |
| retain | bool     | retain = True boker会一直保留消息，默认False |
| qos    | int      | 消息服务质量(0~2)                            |

* 返回值

无



> **MQTTClient.connect(clean_session=True)**

与服务器建立连接，连接失败会导致MQTTException异常。

* 参数

| 参数          | 参数类型 | 说明                                                         |
| ------------- | -------- | ------------------------------------------------------------ |
| clean_session | bool     | 可选参数，一个决定客户端类型的布尔值。 如果为True，那么代理将在其断开连接时删除有关此客户端的所有信息。 如果为False，则客户端是持久客户端，当客户端断开连接时，订阅信息和排队消息将被保留。默认为False |

* 返回值

无



> **MQTTClient.disconnect()**

与服务器断开连接。

* 参数

无

* 返回值

无



> **MQTTClient.ping()**

当keepalive不为0且在时限内没有通讯活动，会主动向服务器发送ping包,检测保持连通性，keepalive为0则不开启。

* 参数

无

* 返回值

无



> **MQTTClient.publish(topic,msg, retain=False, qos=0)**

发布消息。

* 参数

| 参数   | 类型   | 说明                                                         |
| :----- | :----- | ------------------------------------------------------------ |
| topic  | string | 消息主题                                                     |
| msg    | string | 需要发送的数据                                               |
| retain | bool   | 默认为False, 发布消息时把retain设置为true，即为保留信息。<br />MQTT服务器会将最近收到的一条RETAIN标志位为True的消息保存在服务器端, 每当MQTT客户端连接到MQTT服务器并订阅了某个topic，如果该topic下有Retained消息，那么MQTT服务器会立即向客户端推送该条Retained消息 <br />特别注意：MQTT服务器只会为每一个Topic保存最近收到的一条RETAIN标志位为True的消息！也就是说，如果MQTT服务器上已经为某个Topic保存了一条Retained消息，当客户端再次发布一条新的Retained消息，那么服务器上原来的那条消息会被覆盖！ |
| qos    | int    | MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker |

* 返回值

无



> **MQTTClient.subscribe(topic,qos)**

订阅mqtt主题。

* 参数

| 参数  | 类型   | 说明                                                         |
| :---- | :----- | ------------------------------------------------------------ |
| topic | string | topic                                                        |
| qos   | int    | MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker |

* 返回值

无



> **MQTTClient.check_msg()**

检查服务器是否有待处理消息。

* 参数

无

* 返回值

无



> **MQTTClient.wait_msg()**

阻塞等待服务器消息响应。

* 参数

无

* 返回值

无



**示例代码**

```python
'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2020-04-24 17:06:08
@Description: example for module umqtt
@FilePath: example_mqtt_file.py
'''
from umqtt import MQTTClient
import utime
import log
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_MQTT_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
mqtt_log = log.getLogger("MQTT")


state = 0

def sub_cb(topic, msg):
    global state
    mqtt_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    state = 1


if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        mqtt_log.info('Network connection successful!')

        # 创建一个mqtt实例
        c = MQTTClient("umqtt_client", "mq.tongxinmao.com", 18830)
        # 设置消息回调
        c.set_callback(sub_cb)
        #建立连接
        c.connect()
        # 订阅主题
        c.subscribe(b"/public/TEST/quecpython")
        mqtt_log.info("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic" )
        # 发布消息
        c.publish(b"/public/TEST/quecpython", b"my name is Quecpython!")
        mqtt_log.info("Publish topic: /public/TEST/quecpython, msg: my name is Quecpython")

        while True:
            c.wait_msg()  # 阻塞函数，监听消息
            if state == 1:
                break
        # 关闭连接
        c.disconnect()
    else:
        mqtt_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

```



#### ntptime - NTP对时

模块功能：该模块用于时间同步。

> **ntptime.host**

返回当前的ntp服务器，默认为"ntp.aliyun.com"。



> **ntptime.sethost(host)**

设置ntp服务器。

* 参数

| 参数 | 类型   | 说明          |
| :--- | :----- | ------------- |
| host | string | ntp服务器地址 |

* 返回值

成功返回整型值0，失败返回整型值-1。



> **ntptime.settime()**

同步ntp时间。

* 参数

无

* 返回值

成功返回整型值0，失败返回整型值-1。



**ntptime使用示例**

```python
'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module ntptime
@FilePath: example_ntptime_file.py
'''
import ntptime
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_NTP_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
ntp_log = log.getLogger("NtpTime")

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        ntp_log.info('Network connection successful!')

        # 查看默认ntp服务
        ntp_log.info(ntptime.host)
        # 设置ntp服务
        ntptime.sethost('pool.ntp.org')

        # 同步ntp服务时间
        ntptime.settime()
    else:
        ntp_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```



#### system - 环境配置

模块功能：用于配置系统环境的参数以及功能

适配版本：EC100Y(V0009)及以上；EC600S(V0002)及以上。



> ​	**system.replSetEnable(flag)**

交互保护设置，设置开启交互保护后所有外部指令以及代码都无法执行，为不可逆操作，请确认后开启，默认不开启。

* 参数

| 参数 | 类型 | 说明                         |
| :--- | :--- | ---------------------------- |
| flag | int  | 0 : 不开启（默认）；1 ：开启 |

* 返回值

成功返回整型值0；

**使用示例**

```python
import system

system.replSetEnable(1)  # 开启交互保护
```



#### ussl-SSL算法

ssl加密算法套件支持

|                        算法套件                        |
| :----------------------------------------------------: |
| TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 (0xcca9) |
|   TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (0xccaa)   |
|  TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (0xcca8)  |
|    TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 (0xc02c)    |
|     TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (0xc030)     |
|      TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 (0x009f)      |
|       TLS_ECDHE_ECDSA_WITH_AES_256_CCM (0xc0ad)        |
|         TLS_DHE_RSA_WITH_AES_256_CCM (0xc09f)          |
|    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 (0xc024)    |
|     TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (0xc028)     |
|      TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 (0x006b)      |
|     TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA (0xc00a)      |
|      TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (0xc014)       |
|       TLS_DHE_RSA_WITH_AES_256_CBC_SHA (0x0039)        |
|      TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8 (0xc0af)       |
|        TLS_DHE_RSA_WITH_AES_256_CCM_8 (0xc0a3)         |
| TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc087)  |
|  TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc08b)   |
|   TLS_DHE_RSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc07d)    |
| TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 (0xc073)  |
|  TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 (0xc077)   |
|   TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256 (0x00c4)    |
|     TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA (0x0088)     |
|    TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (0xc02b)    |
|     TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (0xc02f)     |
|      TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 (0x009e)      |
|       TLS_ECDHE_ECDSA_WITH_AES_128_CCM (0xc0ac)        |
|         TLS_DHE_RSA_WITH_AES_128_CCM (0xc09e)          |
|    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 (0xc023)    |
|     TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (0xc027)     |
|      TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 (0x0067)      |
|     TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA (0xc009)      |
|      TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (0xc013)       |
|       TLS_DHE_RSA_WITH_AES_128_CBC_SHA (0x0033)        |
|      TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8 (0xc0ae)       |
|        TLS_DHE_RSA_WITH_AES_128_CCM_8 (0xc0a2)         |
| TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc086)  |
|  TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc08a)   |
|   TLS_DHE_RSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc07c)    |
| TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 (0xc072)  |
|  TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 (0xc076)   |
|   TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 (0x00be)    |
|     TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA (0x0045)     |
|        TLS_RSA_WITH_AES_256_GCM_SHA384 (0x009d)        |
|           TLS_RSA_WITH_AES_256_CCM (0xc09d)            |
|        TLS_RSA_WITH_AES_256_CBC_SHA256 (0x003d)        |
|         TLS_RSA_WITH_AES_256_CBC_SHA (0x0035)          |
|     TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384 (0xc032)      |
|     TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384 (0xc02a)      |
|       TLS_ECDH_RSA_WITH_AES_256_CBC_SHA (0xc00f)       |
|    TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384 (0xc02e)     |
|    TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384 (0xc026)     |
|      TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA (0xc005)      |
|          TLS_RSA_WITH_AES_256_CCM_8 (0xc0a1)           |
|     TLS_RSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc07b)      |
|     TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256 (0x00c0)      |
|       TLS_RSA_WITH_CAMELLIA_256_CBC_SHA (0x0084)       |
|   TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc08d)   |
|   TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384 (0xc079)   |
|  TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 (0xc089)  |
|  TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 (0xc075)  |
|        TLS_RSA_WITH_AES_128_GCM_SHA256 (0x009c)        |
|           TLS_RSA_WITH_AES_128_CCM (0xc09c)            |
|        TLS_RSA_WITH_AES_128_CBC_SHA256 (0x003c)        |
|         TLS_RSA_WITH_AES_128_CBC_SHA (0x002f)          |
|     TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256 (0xc031)      |
|     TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256 (0xc029)      |
|       TLS_ECDH_RSA_WITH_AES_128_CBC_SHA (0xc00e)       |
|    TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256 (0xc02d)     |
|    TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256 (0xc025)     |
|      TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA (0xc004)      |
|          TLS_RSA_WITH_AES_128_CCM_8 (0xc0a0)           |
|     TLS_RSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc07a)      |
|     TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256 (0x00ba)      |
|       TLS_RSA_WITH_CAMELLIA_128_CBC_SHA (0x0041)       |
|   TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc08c)   |
|   TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256 (0xc078)   |
|  TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 (0xc088)  |
|  TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 (0xc074)  |
|       TLS_EMPTY_RENEGOTIATION_INFO_SCSV (0x00ff)       |