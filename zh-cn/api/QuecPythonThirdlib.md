#### aLiYun - 阿里云服务

##### 配置阿里云物联网套件的产品信息和设备信息。

模块功能：阿里云物联网套件客户端功能,目前的产品节点类型仅支持“设备”，设备认证方式支持“一机一密和“一型一密”。

注意：BC25PA平台不支持模块功能。

> **aLiYun(productKey, productSecret, DeviceName, DeviceSecret, MqttServer)**

配置阿里云物联网套件的产品信息和设备信息。

* 参数

| 参数          | 类型   | 说明                                                         |
| :------------ | :----- | ------------------------------------------------------------ |
| productKey    | string | 产品标识                                                     |
| productSecret | string | 可选参数，默认为None，productSecret，产品密钥<br />一机一密认证方案时，此参数传入None<br/>一型一密认证方案时，此参数传入真实的产品密钥 |
| DeviceName    | string | 设备名称                                                     |
| DeviceSecret  | string | 可选参数,默认为Non，设备密钥（一型一密认证方案时此参数传入None） |
| MqttServer    | string | 可选参数,需要连接的服务器名称,默认为"{productKey}.iot-as-mqtt.cn-shanghai.aliyuncs.com" |

* 返回值

返回aLiYun连接对象。

##### 设置MQTT数据通道的参数

> **aLiYun.setMqtt(clientID, clean_session, keepAlive=300,reconn=True)**

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
| reconn        | bool   | （可选）控制是否使用内部重连的标志，默认开启为True           |

* 返回值

成功返回整型值0，失败返回整型值-1。

##### 注册回调函数

> **aLiYun.setCallback(sub_cb)**

注册回调函数。

* 参数

| 参数   | 类型     | 说明     |
| :----- | :------- | -------- |
| sub_cb | function | 回调函数 |

* 返回值

无

##### 设置异常回调函数

> **aLiYun.error_register_cb(callback)**

设置异常回调函数，aliyun以及umqtt内部线程异常时通过回调返回error信息，该方法在设置不使用内部重连的情况下才可触发回调

* 参数 

| 参数     | 参数类型 | 说明         |
| -------- | -------- | ------------ |
| callback | function | 异常回调函数 |

* 返回值

无

异常回调函数示例

```python
from aLiYun import aLiYun

def err_cb(err):
    print("thread err:")
    print(err)

ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret)
ali.error_register_cb(err_cb)
```



##### 订阅mqtt主题

> **aLiYun.subscribe(topic,qos)**

订阅mqtt主题。

* 参数

| 参数  | 类型   | 说明                                                         |
| :---- | :----- | ------------------------------------------------------------ |
| topic | string | topic                                                        |
| qos   | int    | MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker |

* 返回值

成功返回整型值0，失败返回整型值-1。

##### 发布消息

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

##### 运行连接

> **aLiYun.start()**

运行连接。

* 参数

无

* 返回值

无

##### 关闭连接

> **aLiYun.disconnect()**

关闭连接。

* 参数

无

* 返回值

无

##### 发送Ping包

> **aLiYun.ping()**

发送心跳包

* 参数

无

* 返回值

无

##### 获取阿里云连接状态

> **aLiYun.getAliyunSta()**

获取阿里云连接状态

注意：BG95平台不支持该API。

* 参数

无

* 返回值

0 ：连接成功

1：连接中

2：服务端连接关闭

-1：连接异常



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

注意：BC25PA平台不支持模块功能。

##### 配置腾讯云物联网套件的产品信息和设备信息

> **TXyun(productID, devicename, devicePsk, ProductSecret)**

配置腾讯云物联网套件的产品信息和设备信息。

* 参数

| 参数          | 类型   | 说明                                                         |
| :------------ | :----- | ------------------------------------------------------------ |
| productID     | string | 产品标识（唯一ID）                                           |
| ProductSecret | string | 可选参数，默认为None，productSecret，产品密钥<br />一机一密认证方案时，此参数传入None<br/>一型一密认证方案时，此参数传入真实的产品密钥 |
| devicename    | string | 设备名称                                                     |
| devicePsk     | string | 可选参数,默认为Non，设备密钥（一型一密认证方案时此参数传入None） |

* 返回值

返回TXyun连接对象。

##### 设置MQTT数据通道的参数

> **TXyun.setMqtt(clean_session, keepAlive=300,reconn=True)**

设置MQTT数据通道的参数

* 参数

| 参数          | 类型 | 说明                                                         |
| :------------ | :--- | ------------------------------------------------------------ |
| clean_session | bool | 可选参数，一个决定客户端类型的布尔值。 如果为True，那么代理将在其断开连接时删除有关此客户端的所有信息。 如果为False，则客户端是持久客户端，当客户端断开连接时，订阅信息和排队消息将被保留。默认为False |
| keepAlive     | int  | 通信之间允许的最长时间段（以秒为单位）,默认为300，范围（60-1000），建议300以上 |
| reconn        | bool | （可选）控制是否使用内部重连的标志，默认开启为True           |

* 返回值

成功返回整型值0，失败返回整型值-1。

##### 注册回调函数

> **TXyun.setCallback(sub_cb)**

注册回调函数。

* 参数

| 参数   | 类型     | 说明                                       |
| :----- | :------- | ------------------------------------------ |
| sub_cb | function | 设置消息回调函数，当服务端响应时触发该方法 |

* 返回值

无

##### 设置异常回调函数

> **TXyun.error_register_cb(callback)**

设置异常回调函数，腾讯云以及umqtt内部线程异常时通过回调返回error信息，该方法在设置不使用内部重连的情况下才可触发回调

* 参数 

| 参数     | 参数类型 | 说明         |
| -------- | -------- | ------------ |
| callback | function | 异常回调函数 |

* 返回值

无

异常回调函数示例

```python
from TenCentYun import TXyun

def err_cb(err):
    print("thread err:")
    print(err)

tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)
tenxun.error_register_cb(err_cb)
```



##### 订阅mqtt主题

> **TXyun.subscribe(topic,qos)**

订阅mqtt主题。

* 参数

| 参数  | 类型   | 说明                                                         |
| :---- | :----- | ------------------------------------------------------------ |
| topic | string | topic                                                        |
| qos   | int    | MQTT消息服务质量（默认0，可选择0或1）MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker |

* 返回值

成功返回整型值0，失败返回整型值-1。

##### 发布消息

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

##### 运行连接

> **TXyun.start()**

运行连接。

* 参数

无

* 返回值

无

##### 关闭连接

> **TXyun.disconnect()**

关闭连接。

* 参数

无

* 返回值

无

##### 发送Ping包

> **TXyun.ping()**

发送心跳包

* 参数

无

* 返回值

无

##### 获取腾讯云连接状态

> **TXyun.getTXyunsta()**

获取腾讯云连接状态

注意：BG95平台不支持该API。

* 参数

无

* 返回值

0 ：连接成功

1：连接中

2：服务端连接关闭

-1：连接异常



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

注意：BC25PA平台不支持模块功能。

##### 发送GET请求

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

##### 发送POST请求

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

* Content-Type（内容类型）说明

  当使用POST方法提交数据时，对于提交的数据主要有如下四种形式：

  - application/x-www-form-urlencoded：form表单数据被编码为key/value格式发送到服务器（表单默认的提交数据的格式）
  - multipart/form-data ： 需要在表单中进行文件上传时，就需要使用该格式
  - application/json： JSON数据格式
  - application/octet-stream ： 二进制流数据（如常见的文件下载）

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

##### 文件上传

> **request.post(url, files, headers)**

使用POST方法完成文件上传到FTP，目前仅支持以 “multipart/form-data” 形式上传，headers默认为“multipart/form-data”。

* 参数

| 参数    | 类型   | 说明                                                         |
| ------- | ------ | ------------------------------------------------------------ |
| url     | string | 服务地址                                                     |
| files   | dict   | 该dict类型参数里面需包含“filepath(设备文件路径)”和“filename(文件名)” |
| headers | dict   | （可选参数）请求头，默认为None，使用上传文件时默认Content-Type为“multipart/form-data”，目前仅支持“multipart/form-data” |

* 示例

```python
import request

url = ''   # FTP服务地址，需要输入已存在的文件路径，例如：http://upload.file.com/folder
files = {"filepath":"usr/upload.json", "filename":"upload.json"}

response = request.post(url, files=files)

'''
也可手动传入headers,但目前上传文件仅支持"multipart/form-data",示例如下

header = {'Content-Type': 'multipart/form-data', 'charset': 'UTF-8'}
response = post(url, files=files, headers=header)
print(response.status_code)
'''
print(response.status_code)  # 查看状态码
```

##### 发送PUT请求

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

##### 发送HEAD请求

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

##### Response类方法说明

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
        '''
        PS： 
        1.使用返回的response对象以text/content/json()等方式读取一次数据后无法再次读取
        2.response.text和response.content方法返回的是一个迭代器对象（可迭代对象（Iterable）：可以使用for循环遍历出所有元素的都可以称为可迭代对			象）,因考虑到请求返回的内容过大所以采用返回迭代器的方式来处理，可使用for循环遍历返回的结果，示例如下
        '''
		# response.text
        response = request.get(url)  # 支持ssl
        for i in response.text:  # response.text为迭代器对象
            print(i)
        # response.content
        response = request.get(url)  # 支持ssl
        for i in response.content: # response.content为迭代器对象
            print(i)
       	# response.json
        url = "http://httpbin.org/post"
		data = {"key1": "value1", "key2": "value2", "key3": "value3"}
        response = request.post(url, data=ujson.dumps(data))   # 发送HTTP POST请求
        print(response.json())
    else:
        http_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```



#### log - 日志

模块功能：系统日志记录,分级别日志工具。

##### 设置日志输出级别

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

##### 获取logger对象

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

##### 设置日志输出位置

> **log.set_output(out)**

设置日志输出的位置, 目前只支持uart和usys.stdout

- 参数

| 参数 | 类型     | 说明                      |
| ---- | -------- | ------------------------- |
| out  | iterator | uart类型或者是usys.stdout |

- 返回值
  - None
- 示例

```python
import log
log.basicConfig(level=log.INFO)
Testlog = log.getLogger("TestLog")

# 设置输出到debug口
from machine import UART
uart = UART(UART.UART0, 115200, 8, 0, 1, 0)

log.set_output(uart)

Testlog.info("this is a Test log") # 会输出带对应的uart口

# 从uart口切换成交互口输出
import usys
log.set_output(usys.stdout)

Testlog.info("this is a Test log") # 会输出到交互口
```

##### 输出debug级别的日志

> **log.debug(msg)**

输出debug级别的日志。

* 参数

| 参数 | 参数类型 | 说明               |
| ---- | -------- | ------------------ |
| msg  | string   | 可变参数，日志内容 |

* 返回值

无

* 示例 

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.debug("Test message: %d(%s)", 100, "foobar")
```

##### 输出info级别的日志

> **log.info(msg)**

输出info级别的日志。

* 参数

| 参数 | 参数类型 | 说明               |
| ---- | -------- | ------------------ |
| msg  | string   | 可变参数，日志内容 |

* 返回值

无

* 示例

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.info("Test message: %d(%s)", 100, "foobar")
```

##### 输出warning级别的日志

> **log.warning(msg)**

输出warning级别的日志。

* 参数

| 参数 | 参数类型 | 说明               |
| ---- | -------- | ------------------ |
| msg  | string   | 可变参数，日志内容 |

* 返回值

无

* 示例

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.warning("Test message: %d(%s)", 100, "foobar")
```

##### 输出error级别的日志

> **log.error(msg)**

输出error级别的日志。

* 参数

| 参数 | 参数类型 | 说明               |
| ---- | -------- | ------------------ |
| msg  | string   | 可变参数，日志内容 |

* 返回值

无

* 示例

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.error("Test message: %d(%s)", 100, "foobar")
```

##### 输出critical级别的日志

> **log.critical(msg)**

输出critical级别的日志。

* 参数

| 参数 | 参数类型 | 说明               |
| ---- | -------- | ------------------ |
| msg  | string   | 可变参数，日志内容 |

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

##### 构建mqtt连接对象

> **MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0, ssl=False, ssl_params={},reconn=True,version=4)**

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
| reconn     | bool     | （可选）控制是否使用内部重连的标志，默认开启为True           |
| version    | int      | （可选）选择使用mqtt版本,version=3开启MQTTv3.1，默认version=4开启MQTTv3.1.1 |

* 返回值 

mqtt对象。

##### 设置回调函数

> **MQTTClient.set_callback(callback)**

设置回调函数，收到消息时会被调用。

* 参数 

| 参数     | 参数类型 | 说明         |
| -------- | -------- | ------------ |
| callback | function | 消息回调函数 |

* 返回值

无

##### 设置异常回调函数

> **MQTTClient.error_register_cb(callback)**

设置异常回调函数，umqtt内部线程异常时通过回调返回error信息，该方法在设置不使用内部重连的情况下才可触发回调

* 参数 

| 参数     | 参数类型 | 说明         |
| -------- | -------- | ------------ |
| callback | function | 异常回调函数 |

* 返回值

无

异常回调函数示例

```python
from umqtt import MQTTClient

def err_cb(err):
    print("thread err:")
    print(err)
    
c = MQTTClient("umqtt_client", "mq.tongxinmao.com", 18830)
c.error_register_cb(err_cb)
```

##### 设置要发送给服务器的遗嘱

> **MQTTClient.set_last_will(topic,msg,retain=False,qos=0)**

设置要发送给服务器的遗嘱，客户端没有调用disconnect()异常断开，则发送通知到客户端。

* 参数

| 参数   | 参数类型 | 说明                                         |
| ------ | -------- | -------------------------------------------- |
| topic  | string   | 遗嘱主题                                     |
| msg    | string   | 遗嘱的内容                                   |
| retain | bool     | retain = True boker会一直保留消息，默认False |
| qos    | int      | 消息服务质量(0~1)                            |

* 返回值

无

##### 与服务器建立连接

> **MQTTClient.connect(clean_session=True)**

与服务器建立连接，连接失败会导致MQTTException异常。

* 参数

| 参数          | 参数类型 | 说明                                                         |
| ------------- | -------- | ------------------------------------------------------------ |
| clean_session | bool     | 可选参数，一个决定客户端类型的布尔值。 如果为True，那么代理将在其断开连接时删除有关此客户端的所有信息。 如果为False，则客户端是持久客户端，当客户端断开连接时，订阅信息和排队消息将被保留。默认为False |

* 返回值

成功返回0，失败则抛出异常

##### 与服务器断开连接

> **MQTTClient.disconnect()**

与服务器断开连接。

* 参数

无

* 返回值

无

##### 关闭Socket

> **MQTTClient.close()**

释放socket资源,(注意区别disconnect方法，close只释放socket资源，disconnect包含线程等资源)

注意：该方法仅用于在自己实现重连时使用，具体请参照mqtt重连示例代码，正常关闭mqtt连接请使用disconnect。

* 参数

无

* 返回值

无

##### 发送ping包

> **MQTTClient.ping()**

当keepalive不为0且在时限内没有通讯活动，会主动向服务器发送ping包,检测保持连通性，keepalive为0则不开启。

* 参数

无

* 返回值

无

##### 发布消息

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

##### 订阅mqtt主题

> **MQTTClient.subscribe(topic,qos)**

订阅mqtt主题。

* 参数

| 参数  | 类型   | 说明                                                         |
| :---- | :----- | ------------------------------------------------------------ |
| topic | string | topic                                                        |
| qos   | int    | MQTT消息服务质量（默认0，可选择0或1）0：发送者只发送一次消息，不进行重试  1：发送者最少发送一次消息，确保消息到达Broker |

* 返回值

无

##### 检查服务器是否有待处理消息

> **MQTTClient.check_msg()**

检查服务器是否有待处理消息。

* 参数

无

* 返回值

无

##### 阻塞等待服务器消息响应

> **MQTTClient.wait_msg()**

阻塞等待服务器消息响应。

* 参数

无

* 返回值

无

##### 获取mqtt连接状态

> **MQTTClient.get_mqttsta()**

获取mqtt连接状态

注意：BG95平台不支持该API。

PS：如果用户调用了 disconnect() 方法之后，再调用 MQTTClient.get_mqttsta() 会返回-1，因为此时创建的对象资源等都已经被释放。

* 参数

无

* 返回值

0 ：连接成功

1：连接中

2：服务端连接关闭

-1：连接异常



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

**MQTT断网异常重连示例**

特别说明：

1.下面示例代码中mqtt的reconn参数用于控制使用或关闭umqtt内部的重连机制，默认为True，使用内部重连机制。

2.如需测试或使用外部重连机制可参考此示例代码，测试前需将reconn=False,否则默认会使用内部重连机制！

```python
'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2021-05-25 17:06:08
@Description: example for module umqtt
@FilePath: example_mqtt_file.py
'''
'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
import utime
import log
import net
import _thread
import checkNet
import dataCall
from umqtt import MQTTClient

PROJECT_NAME = "QuecPython_MQTT_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 调用disconnect后会通过该状态回收线程资源
TaskEnable = True
# 设置日志输出级别
log.basicConfig(level=log.INFO)
mqtt_log = log.getLogger("MQTT")


# 封装mqtt，使其可以支持更多自定义逻辑
class MqttClient():
    '''
    mqtt init
    '''

    # 说明：reconn该参数用于控制使用或关闭umqtt内部的重连机制，默认为True，使用内部重连机制。
    # 如需测试或使用外部重连机制可参考此示例代码，测试前需将reconn=False,否则默认会使用内部重连机制！
    def __init__(self, clientid, server, port, user=None, password=None, keepalive=0, ssl=False, ssl_params={},
                 reconn=True):
        self.__clientid = clientid
        self.__pw = password
        self.__server = server
        self.__port = port
        self.__uasename = user
        self.__keepalive = keepalive
        self.__ssl = ssl
        self.__ssl_params = ssl_params
        self.topic = None
        self.qos = None
        # 网络状态标志
        self.__nw_flag = True
        # 创建互斥锁
        self.mp_lock = _thread.allocate_lock()
        # 创建类的时候初始化出mqtt对象
        self.client = MQTTClient(self.__clientid, self.__server, self.__port, self.__uasename, self.__pw,
                                 keepalive=self.__keepalive, ssl=self.__ssl, ssl_params=self.__ssl_params,
                                 reconn=reconn)

    def connect(self):
        '''
        连接mqtt Server
        '''
        self.client.connect()
        # 注册网络回调函数，网络状态发生变化时触发
        flag = dataCall.setCallback(self.nw_cb)
        if flag != 0:
            # 回调注册失败
            raise Exception("Network callback registration failed")

    def set_callback(self, sub_cb):
        '''
        设置mqtt回调消息函数
        '''
        self.client.set_callback(sub_cb)

    def error_register_cb(self, func):
        '''
        注册一个接收umqtt内线程异常的回调函数
        '''
        self.client.error_register_cb(func)

    def subscribe(self, topic, qos=0):
        '''
        订阅Topic
        '''
        self.topic = topic  # 保存topic ，多个topic可使用list保存
        self.qos = qos  # 保存qos
        self.client.subscribe(topic, qos)

    def publish(self, topic, msg, qos=0):
        '''
        发布消息
        '''
        self.client.publish(topic, msg, qos)

    def disconnect(self):
        '''
        关闭连接
        '''
        global TaskEnable
        # 关闭wait_msg的监听线程
        TaskEnable = False
        # 关闭之前的连接，释放资源
        self.client.disconnect()

    def reconnect(self):
        '''
        mqtt 重连机制(该示例仅提供mqtt重连参考，根据实际情况调整)
        PS：1.如有其他业务需要在mqtt重连后重新开启，请先考虑是否需要释放之前业务上的资源再进行业务重启
            2.该部分需要自己根据实际业务逻辑添加，此示例只包含mqtt重连后重新订阅Topic
        '''
        # 判断锁是否已经被获取
        if self.mp_lock.locked():
            return
        self.mp_lock.acquire()
        # 重新连接前关闭之前的连接，释放资源(注意区别disconnect方法，close只释放socket资源，disconnect包含mqtt线程等资源)
        self.client.close()
        # 重新建立mqtt连接
        while True:
            net_sta = net.getState()  # 获取网络注册信息
            if net_sta != -1 and net_sta[1][0] == 1:
                call_state = dataCall.getInfo(1, 0)  # 获取拨号信息
                if (call_state != -1) and (call_state[2][0] == 1):
                    try:
                        # 网络正常，重新连接mqtt
                        self.connect()
                    except Exception as e:
                        # 重连mqtt失败, 5s继续尝试下一次
                        self.client.close()
                        utime.sleep(5)
                        continue
                else:
                    # 网络未恢复，等待恢复
                    utime.sleep(10)
                    continue
                # 重新连接mqtt成功，订阅Topic
                try:
                    # 多个topic采用list保存，遍历list重新订阅
                    if self.topic is not None:
                        self.client.subscribe(self.topic, self.qos)
                    self.mp_lock.release()
                except:
                    # 订阅失败，重新执行重连逻辑
                    self.client.close()
                    utime.sleep(5)
                    continue
            else:
                utime.sleep(5)
                continue
            break  # 结束循环
        # 退出重连
        return True

    def nw_cb(self, args):
        '''
        dataCall 网络回调
        '''
        nw_sta = args[1]
        if nw_sta == 1:
            # 网络连接
            mqtt_log.info("*** network connected! ***")
            self.__nw_flag = True
        else:
            # 网络断线
            mqtt_log.info("*** network not connected! ***")
            self.__nw_flag = False

    def __listen(self):
        while True:
            try:
                if not TaskEnable:
                    break
                self.client.wait_msg()
            except OSError as e:
                # 判断网络是否断线
                if not self.__nw_flag:
                    # 网络断线等待恢复进行重连
                    self.reconnect()
                # 在socket状态异常情况下进行重连
                elif self.client.get_mqttsta() != 0 and TaskEnable:
                    self.reconnect()
                else:
                    # 这里可选择使用raise主动抛出异常或者返回-1
                    return -1

    def loop_forever(self):
        _thread.start_new_thread(self.__listen, ())

if __name__ == '__main__':
    '''
    手动运行本例程时，可以去掉该延时，如果将例程文件名改为main.py，希望开机自动运行时，需要加上该延时,
    否则无法从CDC口看到下面的 poweron_print_once() 中打印的信息
    '''
    utime.sleep(5)
    checknet.poweron_print_once()
    '''
    如果用户程序包含网络相关代码，必须执行 wait_network_connected() 等待网络就绪（拨号成功）；
    如果是网络无关代码，可以屏蔽 wait_network_connected()
    【本例程必须保留下面这一行！】
    '''
    checknet.wait_network_connected()

    def sub_cb(topic, msg):
        # global state
        mqtt_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    
    c = MqttClient("umqtt_client_753", "mq.tongxinmao.com", 18830, reconn=False)
    
    def err_cb(error):
        '''
        接收umqtt线程内异常的回调函数
        '''
    	mqtt_log.info(error)
    	c.reconnect() # 可根据异常进行重连
        
    # c = MqttClient("umqtt_client_753", "mq.tongxinmao.com", 18830, reconn=False)
    # 设置消息回调
    c.set_callback(sub_cb)
    # 设置异常回调
    c.error_register_cb(err_cb)
    # 建立连接
    c.connect()
    # 订阅主题
    c.subscribe(b"/public/TEST/quecpython758")
    mqtt_log.info("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic")
    # 发布消息
    c.publish(b"/public/TEST/quecpython758", b"my name is Quecpython!")
    mqtt_log.info("Publish topic: /public/TEST/quecpython758, msg: my name is Quecpython")
    # 监听mqtt消息
    c.loop_forever()
    # 等待5s接收消息
    # PS:如果需要测试重连，包括服务器断开连接等情况，请注释掉c.disconnect()和utime.sleep(5)
    # utime.sleep(5)
    # 关闭连接
    # c.disconnect()
```



#### ntptime - NTP对时

模块功能：该模块用于时间同步。

注意：BC25PA平台电信卡开卡时需要说明SIM卡须支持此类业务，移动联通一般不限制(开卡时需要和运营商确认)。

##### 返回当前的ntp服务器

> **ntptime.host**

返回当前的ntp服务器，默认为"ntp.aliyun.com"。

##### 设置ntp服务器

> **ntptime.sethost(host)**

设置ntp服务器。

* 参数

| 参数 | 类型   | 说明          |
| :--- | :----- | ------------- |
| host | string | ntp服务器地址 |

* 返回值

成功返回整型值0，失败返回整型值-1。

##### 同步ntp时间

> **ntptime.settime(timezone=0)**

同步ntp时间。

* 参数

| 参数     | 类型   | 说明          |
| :------- | :----- | ------------- |
| timezone | int    | 默认为0, 范围 (-12~12) |

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



> ​	**system.replSetEnable(flag，**kw_args)**

交互保护设置，可变参API

1、只有一个参数flag时：

0表示关闭，1表示开启，2表示查询当前加密状态；设置开启交互保护后所有外部指令以及代码都无法执行，为不可逆操作，请确认后开启，默认不开启。

2、有两个参数时：

表示交互保护可通过密码开启和关闭(少数平台不支持密码保护功能，所以当遇到不支持的平台，输入密码会直接报错。如：BC25,600M)

* 参数

| 参数 | 类型 | 说明                         |
| :--- | :--- | ---------------------------- |
| flag | int  | 0 : 不开启（默认）；1 ：开启；2：查询加密状态|
| kw_args | str  | password，可为空|

* 返回值

成功返回整型值0；

失败返回整型值-1或者是errorlist

如果是查询加密状态，返回值：
-1：查询失败
1：repl enable
2：repl enable but The password has already been set
3：repl refuse
4：repl-protection by password



> ​	**system.replChangPswd(old_password,new_password)**

更改交互保护密码

* 参数

|     参数     | 类型 | 说明                         |
|     :---     | :--- | ---------------------------- |
| old_password | str  | 旧密码 长度限制：6-12字节    |
| new_password | str  | 新密码 长度限制：6-12字节    |

* 返回值

成功返回整型值0；

失败返回整型值-1或者是errorlist

**使用示例**

```python
>>>import system

>>> system.replSetEnable(1,password='miamia123')//开机首次设置密码并开启交互保护，可设置任意长度在6-12位之间的密码内容
0
>>>                                            //设置成功，交互口被锁，需要输入密码才能正常使用
Please enter password:
>>> ******                                     //密码错误
Incorrect password, please try again:
>>> ********                                   //密码错误
Incorrect password, please try again:
>>> *********                                  //密码正确，可正常交互
REPL enable
>>> system.replSetEnable(2)
2
>>>


>>> system.replSetEnable(1,password='miamia') //已经设置过密码，如果需要重新锁住交互口，需要输入正确密码
Incorrect password!
-1
>>> system.replSetEnable(1,password='miamia123')
0
>>> 
Please enter password:                        //交互口重新锁住
>>> miamia123
*********
REPL enable
>>> system.replSetEnable(2)
2



>>> system.replChangPswd(old_password='miamia123',new_password='123456') //change password
0
>>> system.replSetEnable(1,password='miamia123')                         //更改密码成功之后，继续用老密码锁交互口，提示密码不正确
Incorrect password!
-1
>>> system.replSetEnable(1,password='123456')                            //新密码重新加锁交互口，成功
0
>>> 
Please enter password:
>>> ******
REPL enable



>>> system.replSetEnable(0,password='123456')          //取消密码保护（取消加密保护之后可使用任意新密码重新加锁交互口）

0
>>> 
>>> system.replSetEnable(2)                            //查询状态为repl enable
1
>>> system.replSetEnable(0)                           //默认就已经是0
0
>>>system.replSetEnable(1)                            //开启交互保护
>>>
REPL refuse
>>>
```



#### ql_fs - 高级文件操作

模块功能: 用于文件的高级操作

适配版本:BC25不支持



##### **导入ql_fs**

> **import ql_fs**



##### **查看文件或文件夹是否存在**

> **ql_fs.path_exists(file_path)**

查看文件或文件夹是否存在

- 参数

| 参数      | 类型   | 说明                   |
| --------- | ------ | ---------------------- |
| file_path | string | 文件或文件夹的绝对路径 |

- 返回值

存在返回 True, 不存在返回False



**使用示例**

```python
import ql_fs
ret = ql_fs.path_exists("/usr/xxx.py")
print(ret)

# 存在打印True 不存在 False
```



##### 获取文件所在文件夹路径

> **ql_fs.path_dirname(file_path)**

返回文件和文件夹所在的文件夹路径

- 参数

| 参数      | 类型   | 说明                   |
| --------- | ------ | ---------------------- |
| file_path | string | 文件或文件夹的绝对路径 |

- 返回值
  - string类型的路径地址



**使用示例**

```python
import ql_fs
ret = ql_fs.path_dirname("/usr/bin")
print(ret)

# 打印结果如下
# /usr
```



##### 创建文件夹

> **ql_fs.mkdirs(dir_path)**

递归式创建文件夹, 传入文件夹路径

- 参数

| 参数     | 类型   | 说明                     |
| -------- | ------ | ------------------------ |
| dir_path | string | 所要创建的文件夹绝对路径 |

- 返回值
  - None



**使用示例**

```python
import ql_fs

ql_fs.mkdirs("usr/a/b")
```



##### 删除文件夹



> **ql_fs.rmdirs(dir_path)**

输出文件夹, 传入文件夹路径

- 参数

| 参数     | 类型   | 说明                     |
| -------- | ------ | ------------------------ |
| dir_path | string | 所要删除的文件夹绝对路径 |

- 返回值
  - None



**使用示例**

```python
import ql_fs

ql_fs.rmdirs("usr/a/b")
```



##### 获取文件大小

> **ql_fs.path_getsize(file_path)**

传入文件路径, 返回文件所占的字节数

- 参数

| 参数      | 类型   | 说明     |
| --------- | ------ | -------- |
| file_path | string | 文件路径 |

- 返回值
  - int类型的数字, 单位是字节



**使用示例**

```python
import ql_fs

ql_fs.path_getsize('usr/system_config.json')
```



##### 创建文件

> **ql_fs.touch(file, data)**

创建文件或者更新文件数据, 默认是json文件也可传入文本文件更新, 会自动创建文件夹然后创建或更新文件的内容

- 参数

| 参数 | 类型   | 说明                   |
| :--- | ------ | ---------------------- |
| file | string | 文件绝对路径           |
| data | dict   | 目前只支持创建json文件 |

- 返回值
  - int类型
  - 0为成功
  - -1则失败



**使用示例**

```python
import ql_fs
data = {
    "test":1
}
# 创建或更新json文件
ql_fs.touch("/usr/bin/config.json", data)

```



##### 读取json文件

> **ql_fs.read_json(file)**

读取json文件并返回

- 参数

| 参数 | 类型   | 说明                   |
| ---- | ------ | ---------------------- |
| file | string | 所要读取的json文件路径 |

- 返回值
  - 读取成功
    - 返回dict类型
  - 失败
    - 返回None



**使用示例**

```python
import ql_fs

data = ql_fs.read_json("/usr/system_config.json")
```



##### 文件拷贝

> **ql_fs.file_copy(dst, src)**

将文件从原路径拷贝到目标路径

- 参数

| 参数 | 类型   | 说明     |
| ---- | ------ | -------- |
| dst  | string | 目标路径 |
| src  | string | 原路径   |

- 返回值
  - True代表拷贝成功



**使用示例**

```python
import ql_fs

ql_fs.file_copy("usr/a.json", "usr/system_config.json")
```





#### Queue - 普通队列

模块功能: 用于线程间通信

##### 初始化队列

> **from queue import Queue**
>
> **q = Queue(maxsize=100)**

- 参数

| 参数    | 类型 | 说明                            |
| ------- | ---- | ------------------------------- |
| maxsize | int  | 默认长度是100, 设置最大队列长度 |

- 返回值
  - Queue对象



##### 往队列放入数据

往队列中塞入数据

> **q.put(data)**

- 参数

| 参数 | 类型 | 说明                                                     |
| ---- | ---- | -------------------------------------------------------- |
| data | void | 插入的数据, 可以为空不传, 不传则可认识是放松了一个空信号 |

- 返回值
  - True 为成功
  - False 为失败



##### 获取数据

从队列中获取数据, 这里需要注意一下获取数据这块的是阻塞获取

> **q.get()**

- 参数
  - 无
- 返回值
  - 为队列中的数据, 如果是空信号则会获取为None



##### 查看队列是否为空

> **q.empty()**

- 参数
  - 无
- 返回值
  - True则为空
  - False则不为空



##### 查看队列中存在的数据个数

> **q.size()**

- 参数
  - 无
- 返回值
  - int类型的当前数据长度



##### 使用示例

```python
import _thread
from queue import Queue

# 初始化队列  默认长度100
q = Queue()


def get():
    while True:
        # 阻塞获取
        data = q.get()
        print("data = {}".format(data))

# 线程去阻塞
_thread.start_new_thread(get, ())
q.put("this is a test msg")

```



#### sys_bus会话总线

用于消息的订阅和发布广播, 多线程处理等, 类似于内部的mqtt

##### 订阅topic

> **import sys_bus**
>
> **sys_bus.subscribe(topic, handler)**

- 参数

| 参数    | 类型       | 说明                                                         |
| ------- | ---------- | ------------------------------------------------------------ |
| topic   | string/int | 所需要订阅的topic                                            |
| handler | func       | 处理函数, 当有对应topic过来时, 会对应调用其中的处理函数去处理<br>handler 需要有两个参数(topic, msg) |

- 返回值
  - None



##### 发布topic消息

发布消息, 对应订阅的topic将收到并多线程对此消息处理, 

> **sys_bus.publish(topic , msg)**

- 参数

| 参数  | 类型       | 说明           |
| ----- | ---------- | -------------- |
| topic | string/int | topic          |
| msg   | void       | 任一类型的数据 |

- 返回值
  - None



##### 查看会话总线注册表

查看订阅注册表, 注册表中有所有topic和订阅的函数

> **sys_bus.sub_table(topic=None)**

- 参数

| 参数  | 类型       | 说明                                                         |
| ----- | ---------- | ------------------------------------------------------------ |
| topic | string/int | 可以不传<br>传表示查看此topic的注册表<br>不传表示查看所有的topic的注册表 |

- 返回值
  - dict / list类型的订阅函数列表或注册表



##### 解除订阅

解除订阅订阅的topic, 或者对应topic下的某个函数

> **sys_bus.unsubscribe(topic , cb=None)**

| 参数  | 类型       | 说明                              |
| ----- | ---------- | --------------------------------- |
| topic | string/int | 对应的topic                       |
| cb    | function   | 要删除的订阅函数, 不传则删除topic |

当cb不传时只传入topic时删除topic和从topic下所有的订阅函数,  如果传了cb则删除订阅topic下面订阅列表中的对应的cb函数

- 返回值

True 删除成功, False删除失败



##### 使用示例

```python
import sys_bus


def test(topic, msg):
    print("test ... topic = {} msg = {}".format(topic, msg))

# 订阅
sys_bus.subscribe("test", test)
# 发布
sys_bus.publish("test", "this is a test msg")

#  test ... topic = test msg = this is a test msg

# 解绑对应test topic下的订阅的test函数
sys_bus.unsubscribe("test", test)

# 解绑对应test topic下的所有订阅函数
sys_bus.unsubscribe("test")
```





#### uasyncio协程

[uasyncio文档中心](https://python.quectel.com/doc/doc/Advanced_development/zh/QuecPythonThird/asyncio.html)



#### uwebsocket使用

模块: 主要用于websocket连接使用



##### 客户端连接

> **import uwebsocket**
>
> **ws_client = uwebsocket.Client.connect(uri, headers=None, debug=False)**

- 参数

| 参数    | 类型 | 说明                                                         |
| ------- | ---- | ------------------------------------------------------------ |
| uri     | str  | websocket的连接地址, 一般以"ws://xxx/"或"wss://xxx/"形式存在 |
| headers | dict | 额外需要添加的headers, 用于除了标准连接头之外,  允许用户自己传额外的头部 |
| debug   | bool | 默认False, 当为True的情况下, 会输出日志                      |



##### send发送数据

> **ws_client.send(msg)**

- 参数

| 参数 | 类型 | 说明           |
| ---- | ---- | -------------- |
| msg  | str  | 需要发送的数据 |

- 返回值

无



##### recv接收数据

> **ws_client.recv()**

- 参数

无

- 返回值

| 返回值 | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| result | str  | 返回的结果, 就是recv的结果, 当接受空值或None的时候, 为连接被关闭 |



##### 关闭连接

> **ws_client.close()**

- 参数

无

- 返回值

无



##### 使用示例

```python
from usr import uwebsocket
import _thread


def recv(cli):
    while True:
        # 死循环接收数据
        recv_data = cli.recv()
        print("recv_data = {}".format(recv_data))
        if not recv_data:
            # 服务器关闭连接或客户端关闭连接
            print("cli close")
            client.close()
            break


# 创建客户端, debug=True输出日志, ip和端口需要自己填写, 或者是域名
client = uwebsocket.Client.connect('ws://xxx/', debug=True)

# 线程接收数据
_thread.start_new_thread(recv, (client,))

# 发送数据
client.send("this is a test msg")

```




#### ussl-SSL算法

* 注意
  BC25PA平台不支持模块功能。

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
