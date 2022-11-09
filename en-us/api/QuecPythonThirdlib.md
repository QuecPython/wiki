#### aLiYun - Alibaba Cloud Service

Note: The BC25PA platform does not support this module function.

##### Configure the Product and Device Information of Alibaba Cloud loT  Suite

Function : This module provides Alibaba Cloud loT suite client function. The current product node type only supports "device" and device authentication mode supports "unique-certificate-per-device authentication" and "unique-certificate-per-product authentication".

> **aLiYun(productKey, productSecret, DeviceName, DeviceSecret, MqttServer)**

Configure the product and device information of Alibaba Cloud loT suite.

* Parameter

| Parameter     | Type   | Description                                                  |
| :------------ | :----- | ------------------------------------------------------------ |
| productKey    | string | The unique identifier of a product                           |
| productSecret | string | The product secret which is optional. Default: None.<br />In unique-certificate-per-device authentication, input None (Cannot be an empty string).<br/>In unique-certificate-per-product authentication, input the real product key. |
| DeviceName    | string | Device name                                                  |
| DeviceSecret  | string | Device key which is optional. Default: None.（In unique-certificate-per-product authentication, input None） |
| MqttServer    | string | Optional parameter, the name of the server to be connected to, the default is "{productKey}.iot-as-mqtt.cn-shanghai.aliyuncs.com" |

- Return Value

  - Return the Alibaba Cloud connection object.

##### Set the Parameters of the MQTT Data Channel

> **aLiYun.setMqtt(clientID, clean_session, keepAlive=300,reconn=True)**

Set the parameters of the MQTT data channel.

**It should be noted that when in unique-certificate-per-product authentication of Alibaba Cloud, a secret json file is generated locally to save the device key . If re-flashing  the firmware or deleting, the error is reported when connecting again because there is no secret.json file. So the secret.json file need to be created manually after re-flashing or deleting it. The template of secret.json file is as follows:**

```
{
  "Test01": "9facf9aba414ec9eea7c10d8a4cb69a0"
}
# Test01 : Device name
# "9facf9aba414ec9eea7c10d8a4cb69a0" Device key
```



* Parameter

| Parameter     | Type   | Description                                                  |
| ------------- | ------ | ------------------------------------------------------------ |
| clientID      | string | Customized Alibaba Cloud connection ID                       |
| clean_session | bool   | A Boolean value that determines the client type which is optional. If it is True, the agent deletes all information about this client when it disconnects from the client. If it is False, the client is a persistent client. When the client disconnects, subscription information and queued messages are reserved. Default: False. |
| keepAlive     | int    | The maximum time allowed between communications (Unit: second). Default: 300, Range: 60–1200. |
| reconn        | bool   | （Optional）Specifies whether to use the internal reconnection flag.  Default: True. |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.

##### Register the Callback Function

> **aLiYun.setCallback(sub_cb)**

Register the callback function.

* Parameter

| Parameter | Type     | Description           |
| --------- | -------- | --------------------- |
| sub_cb    | function | The callback function |

* Return Value
  * None

##### Set the Exception Callback Function

> **aLiYun.error_register_cb(callback)**

Set the exception callback function. When the internal threads of Alibaba Cloud and UMQTT  are abnormal, the error information will be returned through the callback. This method can trigger the callback when the internal reconnection is not used.

* Parameter 

| Parameter | Type     | Description                     |
| --------- | -------- | ------------------------------- |
| callback  | function | The exception callback function |

* Return Value
  * None

The exception callback function example

```python
from aLiYun import aLiYun

def err_cb(err):
    print("thread err:")
    print(err)

ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret)
ali.error_register_cb(err_cb)
```



##### Subscribe to MQTT Topics

> **aLiYun.subscribe(topic,qos)**

Subscribe to MQTT topics.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| topic     | string | The subscribed topic                                         |
| qos       | int    | MQTT message service quality. (Default: 0. It can be 0 or 1). 0: The sender sends the message at most once.  1: The sender sends the message at least once to guarantee that the message will be transferred successfully to the broker. |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.

##### Publish the Message

> **aLiYun.publish(topic,msg, qos=0)**

Publish the message.

* Parameter

| Parameter | Type   | Descrption                                                   |
| :-------- | :----- | ------------------------------------------------------------ |
| topic     | string | The published topic                                          |
| msg       | string | The data to be sent                                          |
| qos       | int    | MQTT message service quality. (Default: 0. It can be 0 or 1). 0: The sender sends the message at most once.  1: The sender sends the message at least once to guarantee that the message will be transferred successfully to the broker. |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.

##### Run the Connection

> **aLiYun.start()**

Run the connection.

* Parameter
  * None

* Return Value
  * None

##### Close the Connection

> **aLiYun.disconnect()**

Close the connection.

* Parameter
  * None

* Return Value
  * None

##### Send Ping Package

> **aLiYun.ping()**

Send Ping Package

* Parameter
  * None

* Return Value
  * None

##### Get Alibaba Cloud Connection Status

> **aLiYun.getAliyunSta()**

Get Alibaba Cloud connection status.

Note: The BG95 platform does not support this API.

* Parameter
  * None

* Return Value
  * 0 : Connected
  * 1:  Connecting
  * 2:  Server connection is closed 
  * -1: Disconnected



* Example

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
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
'''
PROJECT_NAME = "QuecPython_AliYin_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)


# Set the log output level
log.basicConfig(level=log.INFO)
aliYun_log = log.getLogger("ALiYun")

productKey = ""  # The unique indentifier of a product (Please refer to application note for Alibaba Cloud)
productSecret = None  # Product key（Input None in unique-certificate-per-device authentication. Please refer to application note for Alibaba Cloud)
DeviceName = ""  # Device name (Please refer to application note for Alibaba Cloud)
DeviceSecret = ""  # Device key (Input None in unique-certificate-per-product authentication. Pre-registration-free is not supported temporarily, please create a device in Alibaba cloud platform first. Please refer to application note for Alibaba Cloud)

state = 5

# Callback function
def sub_cb(topic, msg):
    global state
    aliYun_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    state -= 1


if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        aliYun_log.info('Network connection successful!')
        # Creat Alibaba Cloud connection object
        ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret)

        # Creat MQTT connection property
        clientID = ""  # Customized string（within 64）
        ali.setMqtt(clientID, clean_session=False, keepAlive=300)

        #Set the callback function
        ali.setCallback(sub_cb)
        topic = ""  # Cloud customized or self-owned Topic
        # Subscribe to the topic
        ali.subscribe(topic)
        # Publish the message
        ali.publish(topic, "hello world")
        # Run the connection
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



#### TenCentYun- Tencent Cloud Service

Function: This module provides Tencent Cloud loT suite client function. The current product node type only supports "device" and device authentication mode supports "unique-certificate-per-device authentication" and "unique-certificate-per-product authentication".

Note: The BC25PA platform does not support this module function.

##### Configure the Product and Device Information of Tentent Cloud loT Suite.

> **TXyun(productID, devicename, devicePsk, ProductSecret)**

Configure the product and device information of Tencent Cloud loT suite.

* Parameter

| Parameter     | Type   | Description                                                  |
| :------------ | :----- | ------------------------------------------------------------ |
| productID     | string | The unique identifier of a product                           |
| ProductSecret | string | The product key which is optional. Default: None.<br />In unique-certificate-per-device authentication, input None .<br/>In unique-certificate-per-product authentication, input the real product key. |
| devicename    | string | Device name                                                  |
| devicePsk     | string | Device key which is optional. Default: None.（In unique-certificate-per-product authentication, input None） |

* Return Value

  * Return the Tencent Cloud connection object.

##### Set the Parameters of the MQTT Data Channel.

> **TXyun.setMqtt(clean_session, keepAlive=300,reconn=True)**

Set the parameters of the MQTT data channel.

* Parameter

| parameter     | Type | Description                                                  |
| ------------- | ---- | ------------------------------------------------------------ |
| clean_session | bool | A Boolean value that determines the client type which is optional. If it is True, the agent deletes all information about this client when it disconnects from the client. If it is False, the client is a persistent client. When the client disconnects, subscription information and queued messages are reserved. Default: False. |
| keepAlive     | int  | The maximum time allowed between communications. Range: 60–1000; Unit: second; Default: 300. It is recommended to be above 300. |
| reconn        | bool | (Optional）Specifies whether to use the internal reconnection flag. The default value is True. |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.

##### Register the Callback Function

> **TXyun.setCallback(sub_cb)**

Register the callback function.

* parameter 

| parameter | Type     | Description                                                  |
| --------- | -------- | ------------------------------------------------------------ |
| sub_cb    | function | Set the message callback function, which is triggered when the server responds |

* Return Value

  * None

##### Set the exception callback function

> **TXyun.error_register_cb(callback)**

Set the exception callback function. When the internal threads of Tencent Cloud and UMQTT  are abnormal, the error information will be returned through the callback. This method can trigger the callback when the internal reconnection is not used.

* Parameter 

| Parameter | Type     | Description                     |
| --------- | -------- | ------------------------------- |
| callback  | function | The exception callback function |

* Return Value

  * None

The exception callback function example

```python
from TenCentYun import TXyun

def err_cb(err):
    print("thread err:")
    print(err)

tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)
tenxun.error_register_cb(err_cb)
```



##### Subscribe to MQTT Topics

> **TXyun.subscribe(topic,qos)**

Subscribe to MQTT topics.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| topic     | string | The subscribed topic                                         |
| qos       | int    | MQTT message service quality. (Default: 0. It can be 0 or 1). 0: The sender sends the message at most once.  1: The sender sends the message at least once to guarantee that the message will be transferred successfully to the broker. |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.

##### Publish the Message

> **TXyun.publish(topic,msg, qos=0)**

Publish the message.

* Return Value

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| topic     | string | The published topic                                          |
| msg       | string | The data to be sent                                          |
| qos       | int    | MQTT message service quality. (Default: 0. It can be 0 or 1). 0: The sender sends the message at most once.  1: The sender sends the message at least once to guarantee that the message will be transferred successfully to the broker. |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.

##### Run the Connection

> **TXyun.start()**

Run the connection.

* Parameter

  * None

* Return Value

  * None

##### Close the Connection

> **TXyun.disconnect()**

Close the connection.

* Parameter

  * None

* Return Value

  * None

##### Send Ping Package

> **TXyun.ping()**

Send Ping package.

* Parameter

  * None

* Return Value

  * None

##### Get Tencent Cloud Connection Status

> **TXyun.getTXyunsta()**

Get Tencent Cloud connection status.

Note: The BG95 platform does not support this API.

* Parameter

  * None

* Return Value
  * 0 : Connected
  * 1:  Connecting
  * 2:  Server connection is closed 
  * -1: Disconnected



* Example

```python
from TenCentYun import TXyun
import log
import utime
import checkNet


'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
'''
PROJECT_NAME = "QuecPython_TencentYun_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Set the log output level
log.basicConfig(level=log.INFO)
txyun_log = log.getLogger("TenCentYun")

'''
Tencent Cloud loT Suite client function
'''
productID = ""  # The unique indentifier of a product (Please refer to access application note for Tencent Cloud)
devicename = ""   # Device name (Please refer to access application note for Tencent Cloud)
devicePsk = ""   # Device key (Input None in unique-certificate-per-device authentication. Please refer to access application note for Tencent Cloud)
ProductSecret = None   # Product key (Input None in unique-certificate-per-product authentication. Please refer to access application note for Tencent Cloud)

tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)  # Creat the Tencent Cloud connection object
state = 5

def sub_cb(topic, msg):   # Response to the callback function
    global state
    txyun_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    state -= 1


if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        txyun_log.info('Network connection successful!')

        tenxun.setMqtt()  # Set MQTT
        tenxun.setCallback(sub_cb)   # Set messages callback function
        topic = ""  # Input the customized topic
        tenxun.subscribe(topic)   # Subscribe to the topic
        tenxun.start()
        tenxun.publish(topic, "hello world")   # Publish the message

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

Function: This module provides HTTP Client related Functions.

Note: The BC25PA platform does not support this module function.

##### Send the GET Request

> **request.get(url, data, headers,decode,sizeof,ssl_params)**

Send the GET request

* Parameter

| Parameter | Type | Description                                              |
| ------- | ------ | ------------------------------------------------------------ |
| url     | string | The string URL of the request.                           |
| data    | json   | (Optional).The body attached to the request in JSON format. Default: None.Default: None. |
| headers | dict   | (Optional). HTTP headers. Default: None. |
| decode  | bool   | （Optional）True decode the response content and return the str type. False turn off decoding and return bytes type. Default: True. (It is only used with response content). |
| sizeof  | int    | （Optional. Read the data in the buffer. Default: 255. Unit: byte.  The larger the value, the faster the reading speeding. （ It is recommended to 255-4096 bytes because there may be the possibility of data loss if  data setting  is too large.) |
| ssl_params | dict   | （Optional）SSL Two-way authentication {"cert": certificate_content, "key": private_content} public key of the digital certificate. |

* Example

```python
import request
import log
import utime
import checkNet


'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
'''
PROJECT_NAME = "QuecPython_Requect_get_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Set the log output level
log.basicConfig(level=log.INFO)
http_log = log.getLogger("HTTP GET")

url = "http://httpbin.org/get"

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        http_log.info('Network connection successful!')
        response = request.get(url)   # Send HTTP GET request
        http_log.info(response.json())  # Read the return value in json format
    else:
        http_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```

##### Send the POST Request

> **request.post(url, data, headers,decode,sizeof)**

Send the POST request

* Parameter

| Parameter | Type   | Description                                                  |      |
| --------- | ------ | ------------------------------------------------------------ | ---- |
| url       | string | The string URL of the request                                |      |
| data      | json   | (Optional). The body attached to the request in JSON format. Default: None. |      |
| headers   | dict   | (Optional). HTTP headers. Default: None.                     |      |
| decode    | bool   | （Optional）True decode the response content and return the str type. False turn off decoding and return bytes type. Default: True. (It is only used with response content). |      |
| sizeof    | int    | （Optional. Read the data in the buffer. Default: 255. Unit: byte.  The larger the value, the faster the reading speeding. （ It is recommended to 255-4096 bytes because there may be the possibility of data loss if  data setting  is too large.) |      |

* Content-Type explanation:

  When using the POST method to submit data, the submitted data mainly has the following four forms:

  - application/x-www-form-urlencoded：The form data is encoded in key/value format and sent to the server (the default format of the submitted data in the form)
  - multipart/form-data ： When you need to upload files in the form, you need to use this format
  - application/json： JSON data format
  - application/octet-stream ：Binary stream data (such as common file downloads)

* Example

```python
import request
import ujson
import log
import utime
import checkNet


'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
'''
PROJECT_NAME = "QuecPython_Requect_post_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Set the log output level
log.basicConfig(level=log.INFO)
http_log = log.getLogger("HTTP POST")

url = "http://httpbin.org/post"
data = {"key1": "value1", "key2": "value2", "key3": "value3"}

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        http_log.info('Network connection successful!')

        # POST request
        response = request.post(url, data=ujson.dumps(data))   # Send HTTP POST request
        http_log.info(response.json())
    else:
        http_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```

##### File Upload

> **request.post(url, files, headers)**

Use the POST method to upload files to FTP. Currently, only uploads in the form of "multipart/form-data" are supported, and the default headers are "multipart/form-data".

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| url       | string | Service address                                              |
| files     | dict   | The dict type parameter must contain "filepath (device file path)" and "filename (file name)" |
| headers   | dict   | (Optional parameter) The request header, the default is None, and the default Content-Type is "multipart/form-data" when uploading files. Currently, only "multipart/form-data" is supported. |

* Example

```python
import request

url = ''   # FTP service address, you need to enter an existing file path, for example: http://upload.file.com/folder
files = {"filepath":"usr/upload.json", "filename":"upload.json"}

response = request.post(url, files=files)

'''
You can also manually pass in headers, but currently upload files only support "multipart/form-data", the example is as follows:

header = {'Content-Type': 'multipart/form-data', 'charset': 'UTF-8'}
response = post(url, files=files, headers=header)
print(response.status_code)
'''
print(response.status_code)  # status code
```

##### Send PUT Request

> **request.put(url, data, headers,decode,sizeof)**

Send PUT request.

* parameter

| parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| url       | string | The string URL of the request.                               |
| data      | json   | （Optional）The body attached to the request in JSON format. Default None. |
| headers   | dict   | （Optional）HTTP headers. Default: None.                     |
| decode    | bool   | （Optional）True decode the response content and return the str type. False turn off decoding and return bytes type. Default: True. (It is only used with response content). |
| sizeof    | int    | （Optional. Read the data in the buffer. Default: 255. Unit: byte.  The larger the value, the faster the reading speeding. （ It is recommended to 255-4096 bytes because there may be the possibility of data loss if  data setting  is too large.) |

* Example

```python
import request
url = "http://httpbin.org/put"
response = request.put(url)
```

##### Send the HEAD Request

> **request.head(url, data, headers,decode,sizeof)**

Send the HEAD request

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| url       | string | The string URL of the request.                               |
| data      | json   | （Optional）The body attached to the request in JSON format. Default: None. |
| headers   | dict   | （Optional）HTTP headers. Default: None.                     |
| decode    | bool   | （Optional）True decode the response content and return the str type. False turn off decoding and return bytes type. Default: True. |
| sizeof    | int    | （Optional. Read the data in the buffer. Default: 255. Unit: byte.  The larger the value, the faster the reading speeding. （ It is recommended to 255-4096 bytes because there may be the possibility of data loss if  data setting  is too large.) |

* Example

```python
import request
url = "http://httpbin.org/head"
response = request.head(url)
print(response.headers)
```

##### Response Class

> **response =request.get(url)**

| Function         | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| response.content | Returns the content of the response.（For details of usage, please refer to the following example) |
| response.text    | Returns the text content of the response in Unicode.         |
| response.json()  | Returns the JSON encoded content of the  response and converts it to dict type. |

**Request example**

```python
import request
import log
import utime
import checkNet


'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
'''
PROJECT_NAME = "QuecPython_Requect_SSL_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Set the log output level
log.basicConfig(level=log.INFO)
http_log = log.getLogger("HTTP SSL")
# https request
url = "https://myssl.com"

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        http_log.info('Network connection successful!')
        '''
        PS： 
        1.After using the returned response object to read the data once in text/content/json() etc., it cannot be read again
        2.The response.text and response.content methods return an iterator object (Iterable: All elements that can be traversed 		   by a for loop can be called an iterable object), because the content returned by the request is considered too So we 		  use the method of returning iterator to deal with, you can use the for loop to traverse the returned results, the 			  example is as follows
        '''
		# response.text
        response = request.get(url)  # Support ssl
        for i in response.text:  # response.content is an iterator object
            print(i)
        # response.content
        response = request.get(url)
        for i in response.content: # response.content is an iterator object
            print(i)
       	# response.json
        url = "http://httpbin.org/post"
		data = {"key1": "value1", "key2": "value2", "key3": "value3"}
        response = request.post(url, data=ujson.dumps(data))   # Send HTTP POST request
        print(response.json())
    else:
        http_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```



#### log - Log Facility

Function：This module defines functions and classes which implement a flexible event logging system for applications and libraries..

##### Set Log Output Level

> **log.basicConfig(level)**

Set the threshold for this logger to level. Logging messages which are less severe than level will be ignored. And default is log.INFO.

* Parameter

| Parameter | Type      | Description                               |
| --------- | --------- | ----------------------------------------- |
| CRITICAL  | constants | The numeric value of logging level is 50. |
| ERROR     | constants | The numeric value of logging level is 40. |
| WARNING   | constants | The numeric value of logging level is 30. |
| INFO      | constants | The numeric value of logging level is 20. |
| DEBUG     | constants | The numeric value of logging level is 10. |
| NOTSET    | constants | The numeric value of logging level is 0.  |

* Example

```python
import log
log.basicConfig(level=log.INFO)
```

##### Get logger

> **log.getLogger(name)**

Return a logger with the specified name. If name is None,  return a logger which is the root logger with the hierarchy. All calls to this function with a given name return the same logger instance.

* parameter

| parameter | Type   | Description |
| --------- | ------ | ----------- |
| name      | string | Log name    |

* Return Value

  * Logger

* Example

```python
import log
Testlog = log.getLogger("TestLog")
```

##### Set log output location

> **log.set_output(out)**

Set the log output location. Currently, only uART and usys. Stdout are supported

- parameter

| parameter | Type     | Description          |
| --------- | -------- | -------------------- |
| out       | iterator | uart or usys. stdout |

- Return Value
  - None
- Example

```python
import log
log.basicConfig(level=log.INFO)
Testlog = log.getLogger("TestLog")

# Set the output to the debug port
from machine import UART
uart = UART(UART.UART0, 115200, 8, 0, 1, 0)

log.set_output(uart)

Testlog.info("this is a Test log") # Output with the corresponding UART port

# Switch from uART port to interactive port output
import usys
log.set_output(usys.stdout)

Testlog.info("this is a Test log") # Output to the interface
```

##### 

##### Output Log Debug

> **log.debug(tag, msg)**

Output log debug.

* Parameter 

| Parameter | Type   | Description                                |
| --------- | ------ | ------------------------------------------ |
| tag       | string | Module or function name, as the log prefix |
| msg       | string | The log content                            |

* Return Value

  * None

* Example 

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.debug("Test message: %d(%s)", 100, "foobar")
```

##### Output Log Info

> **log.info(tag,msg)**

Output log info.

* Parameter

| Parameter | Type   | Description                                |
| --------- | ------ | ------------------------------------------ |
| tag       | string | Module or function name, as the log prefix |
| msg       | string | The log content                            |

* Return Value

  * None

* Example

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.info("Test message: %d(%s)", 100, "foobar")
```

##### Output Log Warning 

> **log.warning(tag,msg)**

Output log warning.

* Parameter

| Parameter | Type   | Description                                |
| --------- | ------ | ------------------------------------------ |
| tag       | string | Module or function name, as the log prefix |
| msg       | string | The log content                            |

* Return Value

  * None

* Example

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.warning("Test message: %d(%s)", 100, "foobar")
```

##### Output Log Error

> **log.error(tag,msg)**

Output log error.

* Parameter

| Parameter | Type   | Description                                |
| --------- | ------ | ------------------------------------------ |
| tag       | string | Module or function name, as the log prefix |
| msg       | string | The log content                            |

* Return Value

  * None

* Example

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.error("Test message: %d(%s)", 100, "foobar")
```

##### Output Log Critical

> **log.critical(tag,msg)**

Output log critical.

* Parameter 

| Parameter | Type   | Description                                |
| --------- | ------ | ------------------------------------------ |
| tag       | string | Module or function name, as the log prefix |
| msg       | string | The log content                            |

* Return Value

  * None

* Example

```python
import log
Testlog = log.getLogger("TestLog")
Testlog.critical("Test message: %d(%s)", 100, "foobar")
```



**Log Example**

```python
import log
import utime
import checkNet


'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
'''
PROJECT_NAME = "QuecPython_Log_example"
PROJECT_VERSION = "1.0.0"

# Set the log output level
log.basicConfig(level=log.ERROR)
# Get a logger with the specified name or, if name is None, return a logger which is the root logger of the hierarchy. All calls to this function with a given name return the same logger instance.
log = log.getLogger("error")

if __name__ == '__main__':
    log.error("Test error message!!")
	log.debug("Test debug message!!")
    log.critical("Test critical message!!")
    log.info("Test info message!!")
    log.warning("Test warning message!!")
```



#### umqtt - MQTT

Function: This module provides the MQTT client publishing and subscription function. 

```
Description of QoS
In MQTT Protocol，QoS is defined as the following:
QoS0 – At most once (The lowest level. The sending does not care whether the message has reached the receiver after sending a message.)
QoS1 – At least once (The middle level. The sender guarantee that the message reaches the receiver at least once.)
QoS2 – Exactly once (The highst level. The sender guarantee that the message reaches the receiver and exactly once.)
```

##### Create the MQTT Object

> **MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0, ssl=False, ssl_params={},reconn=True,version=4)**

Create the MQTT object.

* Parameter

| Parameter  | Type   | Description                                                  |
| ---------- | ------ | ------------------------------------------------------------ |
| client_id  | string | The unique identifier of client.                             |
| server     | string | Server address, which can be IP or domain name.              |
| port       | int    | (Optional) The server port, the default is 1883, and the default  port of MQTT over SSL/TLS is 8883. |
| user       | string | (Optional) The user name registered on the server.           |
| password   | string | (Optional) The password registered on the server.            |
| keepalive  | int    | (Optional). The keep-alive timeout value of the client. The default is 60 seconds. Range: 60-1200. Default value: 60. Unit: seconds. |
| ssl        | bool   | (Optional). Enable or disable SSL/TLS support.               |
| ssl_params | string | (Optional) SSL/TLS parameters.                               |
| reconn     | bool   | (Optional）Specifies whether to use the internal reconnection flag. The default value is True. |
| version    | int    | （Optional）Choose MQTT versions. If version number is 3, enabling MQTT v3.1. If version number is 4, enabling MQTT v3.1.1. The default version number is 4. |

* Return Value

  * MQTT object

##### Set the Callback Function

> **MQTTClient.set_callback(callback)**

Set a callback function, which will be called when a message is received.

* Parameter

| Parameter | Type     | Description                   |
| --------- | -------- | ----------------------------- |
| callback  | function | The message callback function |

* Return Value

  * None

##### Set the Exception Callback Function

> **MQTTClient.error_register_cb(callback)**

Set the exception callback function. When the internal threads of UMQTT  is abnormal, the error information will be returned through the callback. This method can trigger the callback when the internal reconnection is not used.

* Parameter

| Parameter | Type     | Description                     |
| --------- | -------- | ------------------------------- |
| callback  | function | The exception callback function |

* Return Value

  * None

The exception callback function example

```python
from umqtt import MQTTClient

def err_cb(err):
    print("thread err:")
    print(err)
    
c = MQTTClient("umqtt_client", "mq.tongxinmao.com", 18830)
c.error_register_cb(err_cb)
```

##### Set the Will to be Sent to the Server

> **MQTTClient.set_last_will(topic,msg,retain=False,qos=0)**

Set the will to be sent to the server. If the disconnection occurred abnormally without calling disconnect(), the notification will be released.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| topic     | string | The will topic.                                              |
| msg       | string | The will content.                                            |
| retain    | bool   | If True, broker will retain the message. The default value False. |
| qos       | int    | MQTT message service quality. It can be 0 or 1.              |

* Return Value

  * None

##### Establish a Connection with the Server

> **MQTTClient.connect(clean_session=True)**

Establish a connection with the server. Failure to connect will lead to an MQTT Exception.

* Parameter

| Parameter     | Type | Description                                                  |
| ------------- | ---- | ------------------------------------------------------------ |
| clean_session | bool | A Boolean value that determines the client type which is optional. If it is True, the agent deletes all information about this client when it disconnects from the client. If it is False, the client is a persistent client. When the client disconnects, subscription information and queued messages are reserved. Default: False. |

* Return Value

  * Return 0 if the execution is successful, otherwise return  ERROR.

##### Disconnect from the Server

> **MQTTClient.disconnect()**

Disconnect from the server.

* Parameter

  * None

* Return Value

  * None

##### Close Socket

> **MQTTClient.close()**

Release socket recourses, (Note: Closing the Socket only releases socket recourses, but disconnecting the socket releases the recourses including thread recourses and so on.)

PS: This method is only used in active reconnection, please refer to the reconnection sample code for more details.  To close the MQTT connection normally, please use disconnect method.

* Parameter

  * None

* Return Value

  * None

##### Send Ping Package

> **MQTTClient.ping()**

When the keep-alive time is not 0 and there is no communication within the time limit, a Ping package is sent to the server to detect  connectivity. If the keep-alive time is 0, it is disabled.

* Parameter

  * None

* Return Value

  * None

##### Publish the Message

> **MQTTClient.publish(topic,msg, retain=False, qos=0)**

Publish the message.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| topic     | string | The published topic                                          |
| msg       | string | The data to be sent.                                         |
| retain    | bool   | The default is False. Set retain to True when publishing a message, which is to retain the information.<br />MQTT server will save the recently received message with the RETAIN flag as True on the server side. Whenever the MQTT client connects to the MQTT server and subscribes to a topic, if there is a retained message under the topic, then The MQTT server will immediately push the Retained message to the client. <br />Note:  MQTT server only save the recently received message with the RETAIN flag as True for each topic! In other words, if a retained message has been saved for a topic on the MQTT server, when the client publishes a new retained message again, the original message on the server will be overwritten. |
| qos       | int    | MQTT message service quality. (Default: 0. It can be 0 or 1). 0: The sender sends the message at most once.  1: The sender sends the message at least once to guarantee that the message will be transferred successfully to the broker. |

* Return Value

  * None

##### Subscribe to MQTT Topics

> **MQTTClient.subscribe(topic,qos)**

Subscribe to MQTT topics.

* Parameter

| Parameter | Type   | Description                                                  |
| :-------- | :----- | ------------------------------------------------------------ |
| topic     | string | The subscribed topic                                         |
| qos       | int    | MQTT message service quality. (Default: 0. It can be 0 or 1). 0: The sender sends the message at most once.  1: The sender sends the message at least once to guarantee that the message will be transferred successfully to the broker. |

* Return Value

  * None

##### Check the Pending Message

> **MQTTClient.check_msg()**

Check whether the server has the pending messages.

* Parameter

  * None

* Return Value

  * None

##### Block Waiting for Server Message Response

> **MQTTClient.wait_msg()**

Block waiting for server message response.

* Parameter

  * None

* Return Value

  * None

##### Get MQTT Connection Status

> **MQTTClient.get_mqttsta()**

Get MQTT connection status.

Note: The BG95 platform does not support this API.

PS: After users use the disconnect() method, and then  -1 is returned if MQTTClient.get_mqttsta() is called because the created object resources have been released at this time. 

* Parameter

  * None

* Return Value
  * 0 : Connected
  * 1:  Connecting
  * 2:  Server connection is closed 
  * -1: Disconnected



**Example**

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
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
'''
PROJECT_NAME = "QuecPython_MQTT_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Set the log output level
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

        # Create a MQTT example
        c = MQTTClient("umqtt_client", "mq.tongxinmao.com", 18830)
        # Set the message callback
        c.set_callback(sub_cb)
        #Establish a connection
        c.connect()
        # Subscribe to the topic
        c.subscribe(b"/public/TEST/quecpython")
        mqtt_log.info("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic" )
        # Publish the message
        c.publish(b"/public/TEST/quecpython", b"my name is Quecpython!")
        mqtt_log.info("Publish topic: /public/TEST/quecpython, msg: my name is Quecpython")

        while True:
            c.wait_msg()  # Wait for the function and listen to the message
            if state == 1:
                break
        # Close the connection
        c.disconnect()
    else:
        mqtt_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

```

**Example of MQTT disconnection and reconnection**

Characteristics：

1. The parameter reconn of MQTT in the sample code below controls enabling or disabling the internal reconnection mechanism. If it is True, enabling the internal reconnection mechanism. (Default: True.) 

2. If testing or using the external reconnection mechanism, please refer to the following sample code. Before testing, please set reconn to be False, otherwise the internal reconnection mechanism will be enabled.

```python
'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2021-05-25 17:06:08
@Description: example for module umqtt
@FilePath: example_mqtt_file.py
'''
'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
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

# After calling disconnect method, thread recources will be recycled through this status.
TaskEnable = True
# Set the log output level
log.basicConfig(level=log.INFO)
mqtt_log = log.getLogger("MQTT")


# Encapsulate MQTT to support more customized logic.
class MqttClient():
    '''
    mqtt init
    '''

    # Characteristics：The parameter reconn of MQTT in the sample code below controls enabling or disabling the internal reconnection mechanism. If it is True, enabling the internal reconnection mechanism. (Default: True.) 
    # If testing or using the external reconnection mechanism, please refer to the following sample code. Before testing, please set reconn to be False, otherwise the internal reconnection mechanism will be enabled.
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
        # Network status flag
        self.__nw_flag = True
        # Creat a mutex lock
        self.mp_lock = _thread.allocate_lock()
        # Initialize MQTT object before creating
        self.client = MQTTClient(self.__clientid, self.__server, self.__port, self.__uasename, self.__pw,
                                 keepalive=self.__keepalive, ssl=self.__ssl, ssl_params=self.__ssl_params,
                                 reconn=reconn)

    def connect(self):
        '''
        Connect MQTT Server
        '''
        self.client.connect()
        # Register the network callback function, which is triggered when the network status changes.
        flag = dataCall.setCallback(self.nw_cb)
        if flag != 0:
            # Callback registration failed
            raise Exception("Network callback registration failed")

    def set_callback(self, sub_cb):
        '''
        Set MQTT callback message function
        '''
        self.client.set_callback(sub_cb)

    def error_register_cb(self, func):
        '''
        Register a callback function to receive the thread error in umqtt.
        '''
        self.client.error_register_cb(func)

    def subscribe(self, topic, qos=0):
        '''
        Subscribe to the topic
        '''
        self.topic = topic  # Save the topic and multiple topics can be saved in a list.
        self.qos = qos  # Save qos
        self.client.subscribe(topic, qos)

    def publish(self, topic, msg, qos=0):
        '''
        Publish the message
        '''
        self.client.publish(topic, msg, qos)

    def disconnect(self):
        '''
        Close the connection
        '''
        global TaskEnable
        # Close the listening thread for wait_msg
        TaskEnable = False
        # Close the previous connection and release the resources
        self.client.disconnect()

    def reconnect(self):net
        '''
        MQTT reconnection mechanism (This example only provides a reference for MQTT reconnection, which can be adjusted according to the actural situation.)
        PS：1. If there are other services that need to be restarted after MQTT is reconnected, please consider whether the resources on the previous business are released before restarting business.
            2.This part needs to be added according to the actural business logic. This example only includes re-subscribing to topic after MQTT reconnects.
        '''
        # Detemine whether the lock has been acquired
        if self.mp_lock.locked():
            return
        self.mp_lock.acquire()
        # Close the previous connection before revonnection and then release the resources. (Closing the Socket only releases socket recourses, but disconnecting the socket releases the recourses including thread recourses and so on.)
        self.client.close()
        # Reestablish a MQTT connection
        while True:
            net_sta = net.getState()  # Get network registration information
            if net_sta != -1 and net_sta[1][0] == 1:
                call_state = dataCall.getInfo(1, 0)  # Get dial information
                if (call_state != -1) and (call_state[2][0] == 1):
                    try:
                        # The network is normal and the MQTT is reconnected
                        self.connect()
                    except Exception as e:
                        # Failed to reconnect MQTT and try to connect again after 5 s
                        self.client.close()
                        utime.sleep(5)
                        continue
                else:
                    # Waiting for the network recovery
                    utime.sleep(10)
                    continue
                # Reconnect MQTT successfully and subscribe to the topic
                try:
                    # The multiple topics are saved in a list. Edit the list and re-subscribe
                    if self.topic is not None:
                        self.client.subscribe(self.topic, self.qos)
                    self.mp_lock.release()
                except:
                    # Fail to subscribe. Retry to connect
                    self.client.close()
                    utime.sleep(5)
                    continue
            else:
                utime.sleep(5)
                continue
            break  # End the loop
        # Exit the reconection
        return True

    def nw_cb(self, args):
        '''
        dataCall Network callback
        '''
        nw_sta = args[1]
        if nw_sta == 1:
            # Network connected
            mqtt_log.info("*** network connected! ***")
            self.__nw_flag = True
        else:
            # Network disconnected
            mqtt_log.info("*** network not connected! ***")
            self.__nw_flag = False

    def __listen(self):
        while True:
            try:
                if not TaskEnable:
                    break
                self.client.wait_msg()
            except OSError as e:
                # Detemine whether the network is disconnected
                if not self.__nw_flag:
                    # The network is disconnected and waiting for recovery to reconnect
                    self.reconnect()
                # Reconnect when the socket status is abnormal
                elif self.client.get_mqttsta() != 0 and TaskEnable:
                    self.reconnect()
                else:
                    # Choose to use raise and return ERROR actively or -1.
                    return -1

    def loop_forever(self):
        _thread.start_new_thread(self.__listen, ())

if __name__ == '__main__':
    '''
    When running this routine manually, please removethis delay. If changing the routine file name to main.py, please add this delay when you want to start running automatically.
    Otherwise the information printed in the following  poweron_print_once() from the CDC port cannot be saw.
    '''
    utime.sleep(5)
    checknet.poweron_print_once()
    '''
    If the user program contains network-related code, wait_network_connected() must be executed to wait for the network to be ready (Dail-up is successful)
    If it is network-independent code, wait_network_connected() can be blocked.
    【This routine must retain the following line!】
    '''
    checknet.wait_network_connected()

    def sub_cb(topic, msg):
        # global state
        mqtt_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    
    c = MqttClient("umqtt_client_753", "mq.tongxinmao.com", 18830, reconn=False)
    
    def err_cb(error):
        '''
        Receive the exception callback function in umqtt thread
        '''
    	mqtt_log.info(error)
    	c.reconnect() # Reconnect according to the exception
        
    # c = MqttClient("umqtt_client_753", "mq.tongxinmao.com", 18830, reconn=False)
    # Set message callback
    c.set_callback(sub_cb)
    # Set exception callback
    c.error_register_cb(err_cb)
    # Establish a connection
    c.connect()
    # Subscribe to the topic
    c.subscribe(b"/public/TEST/quecpython758")
    mqtt_log.info("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic")
    # Publish the message
    c.publish(b"/public/TEST/quecpython758", b"my name is Quecpython!")
    mqtt_log.info("Publish topic: /public/TEST/quecpython758, msg: my name is Quecpython")
    # Listen to the MQTT message
    c.loop_forever()
    # Receive the message after 5 s
    # PS: If the reconnected need to be tested, including server disconnection, please comment out c.disconnect() and utime.sleep(5)
    # utime.sleep(5)
    # Close the connection
    # c.disconnect()
```



#### ntptime - NTP Time Synchronization

Function: This module provides the interface fir time synchronization.

Note: When opening the BC25PA platform telecommunications card, you need to state that the SIM card must support such services, which is generally not restricted by China Mobile Unicom (you need to confirm with the operator when opening the card).

##### Return the Current NTP Server Address

> **ntptime.host**

  Return the current NTP server address, default is "ntp.aliyun.com".

##### Set the NTP Server

> **ntptime.sethost(host)**

Set the NTP Server.

* Parameter

| Parameter | Type   | Description        |
| --------- | ------ | ------------------ |
| host      | string | NTP server address |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.

##### Synchronize NTP Time

> **ntptime.settime(timezone=0)**

Synchronize NTP time.

* Parameter

| Parameter | Type   | Description        |
| --------- | ------ | ------------------ |
| timezone  | int    | Default: 0, Range: -12 ~ 12 |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.



**NTPtime Example**

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
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
'''
PROJECT_NAME = "QuecPython_NTP_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Set the log output level
log.basicConfig(level=log.INFO)
ntp_log = log.getLogger("NtpTime")

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        ntp_log.info('Network connection successful!')

        # View the default NTP service
        ntp_log.info(ntptime.host)
        # Set NTP service
        ntptime.sethost('pool.ntp.org')

        # Sybchronize the NTP service time
        ntptime.settime()
    else:
        ntp_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))
```



#### system - Set system

Function: This module sets the parameters and functions of system

Applicable modules: EC100Y(V0009) and above; EC600S(V0002) and above.



> ​	**system.replSetEnable(flag，**kw_args)**

Set interactive protect. After setting to enable interactive protect, all external commands and codes cannot be executed. It is an irreversible operation. Please enable it after confirmation. The default is Disable.
（The parameter [Password] is not supported in BC25 and 600M paltform）
* Parameter

| Parameter | Type | Description                       |
| --------- | ---- | --------------------------------- |
| flag      | int  | 0 : Disable（default)；1 ：Enable |
| kw_args   | str  | password，it can be NULL          |

* Return Value

  * Return 0 if the execution is successful.
  * if the parameter of flag is 2, return values means current repl states:
     -1：failed
      1：repl enable
	  2：repl enable but The password has already been set
      3：repl refuse
      4：repl-protection by password



> ​	**system.replChangPswd(old_password,new_password)**

change repl-protetion password

* 参数

|   Parameter  | Type | Description                       |
| old_password | str  | old password len:6-12byte         |
| new_password | str  | new password len:6-12byte         |

* Return Value

  * Return 0 if the execution is successful.

**Example**

```python
>>>import system

>>> system.replSetEnable(1,password='miamia123')
0
>>> 
Please enter password:
>>> ******
Incorrect password, please try again:
>>> ********
Incorrect password, please try again:
>>> *********
REPL enable
>>> system.replSetEnable(2)
2
>>>


>>> system.replSetEnable(1,password='miamia')
Incorrect password!
-1
>>> system.replSetEnable(1,password='miamia123')
0
>>> 
Please enter password:
>>> miamia123
*********
REPL enable
>>> system.replSetEnable(2)
2



>>> system.replChangPswd(old_password='miamia123',new_password='123456') //change password
0
>>> system.replSetEnable(1,password='miamia123')
Incorrect password!
-1
>>> system.replSetEnable(1,password='123456')
0
>>> 
Please enter password:
>>> ******
REPL enable



>>> system.replSetEnable(0,password='123456')

0
>>> 
>>> system.replSetEnable(2)
1
>>> system.replSetEnable(0)
0
>>>system.replSetEnable(1)
>>>
REPL refuse
>>>
```



####  ql_fs - advanced file operations

Module function: used for advanced operation of files

Adaptation version: not supported by bc25



##### **import QL_ fs**

> **import ql_fs**



##### **check whether the file or folder exists**

> **ql_fs.path_exists(file_path)**

Check whether the file or folder exists

- Parameter

|Parameter | type | description|
| --------- | ------ | ---------------------- |
| file_ Path | string | absolute path of file or folder|

- Return Value

  * Returns true if it exists and false if it does not exist



**Use Example**

```python
import ql_fs
ret = ql_fs.path_exists("/usr/xxx.py")
print(ret)

#Print true does not exist false
```



##### Get the path of the folder where the file is located

> **ql_fs.path_dirname(file_path)**

Returns the folder path where files and folders are located

- Parameter

|Parameter | type | description|
| --------- | ------ | ---------------------- |
| file_ Path | string | absolute path of file or folder|

- Return Value
  - Path address of type string



**Use Example**

```python
import ql_fs
ret = ql_fs.path_dirname("/usr/bin")
print(ret)

#The printing results are as follows
# /usr
```



##### Create folder

> **ql_fs.mkdirs(dir_path)**

Create a folder recursively and pass in the folder path

- Parameter

|Parameter | type | description|
| -------- | ------ | ------------------------ |
| dir_ Path | string | absolute path of the folder to be created|

- Return Value

  - None



**Use Example**

```python
import ql_fs

ql_fs.mkdirs("usr/a/b")
```



##### Delete folder



> **ql_fs.rmdirs(dir_path)**

Output folder, incoming folder path

- Parameter

|Parameter | type | description|
| -------- | ------ | ------------------------ |
| dir_ Path | string | absolute path of the folder to be deleted|

- Return Value

  - None



**Use Example**

```python
import ql_fs

ql_fs.rmdirs("usr/a/b")
```



##### Get file size

> **ql_fs.path_getsize(file_path)**

Pass in the file path and return the number of bytes occupied by the file

- Parameter

|Parameter | type | description|
| --------- | ------ | -------- |
| file_ Path | string | file path|

- Return Value

  - A number of type int in bytes



**Use Example**

```python
import ql_fs

ql_fs.path_getsize('usr/system_config.json')
```



##### Create file

> **ql_fs.touch(file, data)**

Create files or update file data. The default is JSON files. Text files can also be imported for updating. Folders will be created automatically, and then the contents of files will be created or updated

- Parameter

|Parameter | type | description|
| ---- | ------ | ---------------------- |
|File | string | absolute path of file|
|Data | Dict | currently only supports the creation of JSON files|

- Return Value
  - Int type
  - 0 is successful
  - 1 failed



**Use Example**

```python
import ql_fs
data = {
    "test":1
}
#Create or update JSON files
ql_fs.touch("/usr/bin/config.json", data)

```



##### Read JSON file

> **ql_fs.read_json(file)**

Read the JSON file and return

- Parameter

|Parameter | type | description|
| ---- | ------ | ---------------------- |
|File | string | JSON file path to be read|

- Return Value
  - Read successful
    - Return dict type
  - Fail
    - Return to none



**Use Example**

```python
import ql_fs

data = ql_fs.read_json("/usr/system_config.json")
```



##### File copy

> **ql_fs.file_copy(dst, src)**

Copy the file from the original path to the destination path

- Parameter

|Parameter | type | description|
| ---- | ------ | -------- |
|DST | string | target path|
|SRC | string | original path|

- Return Value
  - True means the copy was successful



**Use Example**

```python
import ql_fs

ql_fs.file_copy("usr/a.json", "usr/system_config.json")
```





#### Queue - normal queue

Module function: used for inter thread communication

##### Initialize queue

> **from queue import Queue**
>
> **q = Queue(maxsize=100)**

- Parameter

|Parameter | type | description|
| ------- | ---- | ------------------------------- |
|Maxsize | int | the default length is 100. Set the maximum queue length|

- Return Value
  - Queue object



##### Put data into the queue

Stuff data into the queue

> **q.put(data)**

- Parameter

|Parameter | type | description|
| ---- | ---- | -------------------------------------------------------- |
|Data | void | the inserted data can be empty. If it is not transmitted, it can be recognized that it is relaxing an empty signal|

- Return Value
  - True is success
  - False is failure



##### Get data

Get data from the queue. Here, you need to pay attention to the block acquisition in getting data

> **q.get()**

- Parameter
  - None

- Return Value
  - It is the data in the queue. If it is an empty signal, it will be obtained as none



##### Check whether the queue is empty

> **q.empty()**

- Parameter
  - None

- Return Value
  - True is null
  - False is not empty



##### View the number of data in the queue

> **q.size()**

- Parameter
  - None

- Return Value
  - Current data length of type int



##### Use Example

```python
import _thread
from queue import Queue

#Default length of initialization queue: 100
q = Queue()


def get():
    while True:
        #Blocking acquisition
        data = q.get()
        print("data = {}".format(data))

#Thread deblocking
_thread.start_new_thread(get, ())
q.put("this is a test msg")

```



####  sys_bus session bus

It is used for message subscription, publishing, broadcasting, multithreading, etc., similar to the internal mqtt

##### Subscribe to topic

> **import sys_bus**
>
> **sys_bus.subscribe(topic, handler)**

- Parameter

|Parameter | type | description|
| ------- | ---------- | ------------------------------------------------------------ |
|Topic | string / int | topic to subscribe to|
|Handler | func | processing function. When there is a corresponding topic, it will call the processing function to process it accordingly. < br > handler needs two parameters (topic, MSG)|

- Return Value
  - None



##### Publish topic message

Publish a message, and the topic corresponding to the subscription will receive and process the message through multiple threads,

> **sys_bus.publish(topic , msg)**

- Parameter

|Parameter | type | description|
| ----- | ---------- | -------------- |
| topic | string/int | topic          |
|MSG | void | any type of data|

- Return Value
  - None



##### View session bus registry

Check the subscription registry, which contains all topics and subscription functions

> **sys_bus.sub_table(topic=None)**

- Parameter

|Parameter | type | description|
| ----- | ---------- | ------------------------------------------------------------ |
|Topic | string / int | can be omitted. < br > passing means viewing the registry of this topic. < br > not passing means viewing the registry of all topics|

- Return Value
  - Subscription function list or registry of type dict / list



##### Unsubscribe

Unsubscribe from the topic, or a function under the corresponding topic

> **sys_bus.unsubscribe(topic , cb=None)**

|Parameter | type | description|
| ----- | ---------- | --------------------------------- |
|Topic | string / int | corresponding topic|
|CB | function | the subscription function to be deleted. If it is not transmitted, delete topic|

When CB is not transmitted, only topic is passed in, and all subscription functions under topic and from topic are deleted. If CB is transmitted, the corresponding CB function in the subscription list under topic is deleted

- Return Value

  - True deletion succeeded, false deletion failed



##### Use Example

```python
import sys_bus


def test(topic, msg):
    print("test ... topic = {} msg = {}".format(topic, msg))

#subscribe
sys_bus.subscribe("test", test)
#release
sys_bus.publish("test", "this is a test msg")

#  test ... topic = test msg = this is a test msg

#Unbind the test function corresponding to the subscription under test topic
sys_bus.unsubscribe("test", test)

#Unbind all subscription functions under the corresponding test topic
sys_bus.unsubscribe("test")
```





#### Uasyncio collaboration

[uasyncio document center](https://python.quectel.com/doc/doc/Advanced_development/zh/QuecPythonThird/asyncio.html)



#### uwebsocket use

Module: Mainly used for websocket connection use



##### Client connection

> **import uwebsocket**
>
> **ws_client = uwebsocket.Client.connect(uri, headers=None, debug=False)**

- paramter

| parameter | type | illustrate                                                   |
| --------- | ---- | ------------------------------------------------------------ |
| uri       | str  | The connection address of websocket, generally exists in the form of "ws://xxx/" or "wss://xxx/" |
| headers   | dict | Additional headers that need to be added are used to allow users to pass additional headers in addition to the standard headers |
| debug     | bool | The default is False, when it is True, the log will be output |



##### send data

> **ws_client.send(msg)**

- paramter

| parameter | type | illustrate   |
| --------- | ---- | ------------ |
| msg       | str  | data to send |

- return value

None



##### recv data

> **ws_client.recv()**

- paramter

None

- return value

| return value | type | illustrate                                                   |
| ------------ | ---- | ------------------------------------------------------------ |
| result       | str  | The returned result is the result of recv. When a null value or None is accepted, the connection is closed. |



##### close connect

> **ws_client.close()**

- paramter

None

- return Value

None



##### Example of use

```python
from usr import uwebsocket
import _thread


def recv(cli):
    while True:
        # Infinite loop to receive data
        recv_data = cli.recv()
        print("recv_data = {}".format(recv_data))
        if not recv_data:
            # The server closes the connection or the client closes the connection
            print("cli close")
            client.close()
            break


# Create a client, debug=True to output logs, ip and port need to be filled in by yourself, or a domain name
client = uwebsocket.Client.connect('ws://xxx/', debug=True)

# Thread receives data
_thread.start_new_thread(recv, (client,))

# send data
client.send("this is a test msg")

```





#### ussl-SSL Algorithm
Note: The BC25PA platform does not support this module function.

SSL cipher suite supports the algorithm as following:

|                    Algorithm Suite                     |
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
