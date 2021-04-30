### QuecPython类库

#### example - 执行python脚本

模块功能：提供方法让用户可以在命令行或者代码中执行python脚本。

> example.exec(filePath)

执行指定的python脚本文件。

* 参数 

| 参数     | 参数类型 | 参数说明                       |
| -------- | -------- | ------------------------------ |
| filePath | string   | 要执行python脚本文件的绝对路径 |

* 返回值

无

* 示例

```python
# 假设有文件test.py,内容如下

def myprint():
    count = 10
    while count > 0:
        count -= 1
        print('##### test #####')

myprint()

#将test.py文件上传到模块中，进入命令行执行如下代码
>>> uos.listdir('/usr/')
['apn_cfg.json', 'test.py']
>>> import example
>>> example.exec('/usr/test.py')
# 执行结果如下

##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
```



#### dataCall - 数据拨号

模块功能：提供数据拨号相关接口。

> **dataCall.start(profileIdx, ipType, apn, username, password, authType)**

启动拨号，进行数据链路激活。

* 参数

| 参数       | 参数类型 | 参数说明                                                     |
| ---------- | -------- | ------------------------------------------------------------ |
| profileIdx | int      | PDP索引，取值1-8，一般设置为1，设置其他值可能需要专用apn与密码才能设置成功 |
| ipType     | int      | IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6                         |
| apn        | string   | apn名称，可为空，最大长度不超过63字节                        |
| username   | string   | apn用户名，可为空，最大长度不超过15字节                      |
| password   | string   | apn密码，可为空，最大长度不超过15字节                        |
| authType   | int      | 加密方式，0-不加密，1-PAP，2-CHAP                            |

* 返回值

成功返回整型值0，失败返回整型值-1。

* 示例 

```python
>>> import dataCall
>>> dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
0
```



> **dataCall.setApn(profileIdx, ipType, apn, username, password, authType)**

用户apn信息配置接口，用户调用该接口后，会在用户分区目录下创建user_apn.json文件，用于保存用户apn信息，并使用该apn信息启动拨号，进行数据链路激活。

* 参数

| 参数       | 参数类型 | 参数说明                                                     |
| ---------- | -------- | ------------------------------------------------------------ |
| profileIdx | int      | PDP索引，取值1-8，一般设置为1，设置其他值可能需要专用apn与密码才能设置成功 |
| ipType     | int      | IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6                         |
| apn        | string   | apn名称，可为空，最大长度不超过63字节                        |
| username   | string   | apn用户名，可为空，最大长度不超过15字节                      |
| password   | string   | apn密码，可为空，最大长度不超过15字节                        |
| authType   | int      | 加密方式，0-不加密，1-PAP，2-CHAP                            |

* 返回值

成功返回整型值0，失败返回整型值-1。

* 示例

```python
>>> import dataCall
>>> dataCall.setApn(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
0
```



> **dataCall.setCallback(usrFun)**

注册用户回调函数，当网络状态发生变化，比如断线、上线时，会通过该回调函数通知用户。

* 参数

| 参数   | 参数类型 | 参数说明                     |
| ------ | -------- | ---------------------------- |
| usrFun | function | 用户回调函数，函数形式见示例 |

* 返回值

注册失败返回整型-1，成功返回整型0。

* 示例

```python
>>> import dataCall
>>> import net

>>> def nw_cb(args):
		pdp = args[0]
		nw_sta = args[1]
		if nw_sta == 1:
			print("*** network %d connected! ***" % pdp)
		else:
			print("*** network %d not connected! ***" % pdp)
			
>>> dataCall.setCallback(nw_cb)
0
>>> net.setModemFun(4)  # 进入飞行模式
0
>>> *** network 1 not connected! *** # 进入飞行模式导致断网，通过回调告知用户
>>> net.setModemFun(1)  # 退出飞行模式
0
>>> *** network 1 connected! *** # 退出飞行模式，自动拨号，等待联网成功，通过回调告知用户
```



> **dataCall.getInfo(profileIdx, ipType)**

获取数据拨号信息，包括连接状态、IP地址、DNS等。

* 参数

| 参数       | 参数类型 | 参数说明                             |
| ---------- | -------- | ------------------------------------ |
| profileIdx | int      | PDP索引，取值1-8                     |
| ipType     | int      | IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6 |

* 返回值

错误返回整型-1，成功返回拨号信息，返回格式根据ipType的不同而有所区别：
ipType =0，返回值格式如下：

`(profileIdx, ipType, [nwState, reconnect, ipv4Addr, priDns, secDns])`

`profileIdx`：PDP索引，取值1-8

`ipType`：IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6

`nwState`：拨号结果，0-失败，1-成功

`reconnect`：重拨标志

`ipv4Addr`：ipv4地址

`priDns`：dns信息

`secDns`：dns信息

ipType =1，返回值格式如下：

`(profileIdx, ipType, [nwState, reconnect, ipv6Addr, priDns, secDns])`

`profileIdx`：PDP索引，取值1-8

`ipType`：IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6

`nwState`：拨号结果，0-失败，1-成功

`reconnect`：重拨标志

`ipv6Addr`：ipv6地址

`priDns`：dns信息

`secDns`：dns信息

ipType =2，返回值格式如下：

`(profileIdx, ipType, [nwState, reconnect, ipv4Addr, priDns, secDns], [nwState, reconnect, ipv6Addr, priDns, secDns])`

* 示例

```python
>>> import dataCall
>>> dataCall.getInfo(1, 0)
(1, 0, [1, 0, '10.91.44.177', '58.242.2.2', '218.104.78.2'])
```

注：返回值 `(1, 0, [0, 0, '0.0.0.0', '0.0.0.0', '0.0.0.0'])` 表示当前没有拨号或者拨号没有成功。

**使用示例**

```python
import dataCall
import net
import utime
import checkNet

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_DataCall_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)


state = 1
'''
dataCall.setCallback()
用户回调函数，当网络状态发生变化，比如断线、上线时，会通过该回调函数通知用户。
'''
# 定义回调函数
def nw_cb(args):
    global state
    pdp = args[0]   # pdp索引
    nw_sta = args[1]  # 网络连接状态 0未连接， 1已连接
    if nw_sta == 1:
        print("*** network %d connected! ***" % pdp)
    else:
        print("*** network %d not connected! ***" % pdp)
    state -= 1


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

    # 注册回调函数
    dataCall.setCallback(nw_cb)

    # 进入飞行模式模拟触发
    net.setModemFun(4)
    utime.sleep(2)

    # 退出飞行模式再次模拟触发回调
    net.setModemFun(1)

    while 1:
        if state:
            pass
        else:
            break

```



#### cellLocator - 基站定位

模块功能：提供基站定位接口，获取坐标信息。

> **cellLocator.getLocation(serverAddr, port, token, timeout, profileID)**

获取基站坐标信息。

* 参数

| 参数       | 参数类型 | 参数说明                                                     |
| ---------- | -------- | ------------------------------------------------------------ |
| serverAddr | string   | 服务器域名，长度必须小于255 bytes，目前仅支持 “www.queclocator.com” |
| port       | int      | 服务器端口，目前仅支持 80 端口                               |
| token      | string   | 密钥，16位字符组成，需要申请                                 |
| timeout    | int      | 设置超时时间，范围1-300s，默认300s                           |
| profileID  | int      | PDP索引，范围1-8                                             |

* 返回值

功返回度格式经纬度坐标信息，返回格式：`(latitude, longtitude, accuracy)`，`(0.0, 0.0, 0)`表示未获取到有效坐标信息；失败返回错误码说明如下：

-1 – 初始化失败

-2 – 服务器地址过长（超过255字节）

-3 – 密钥长度错误，必须为16字节

-4 – 超时时长超出范围，支持的范围（1~300）s

-5 – 指定的PDP网络未连接，请确认PDP是否正确

-6 – 获取坐标出错

* 示例

```python
>>> import cellLocator
>>> cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
(117.1138, 31.82279, 550)
# 上面使用的密钥仅为测试密钥
```



#### sim - SIM卡

模块功能：提供sim卡操作相关API，如查询sim卡状态、iccid、imsi等。

注意：能成功获取IMSI、ICCID、电话号码的前提是SIM卡状态为1，可通过sim.getStatus()查询。

> **sim.getImsi()**

获取sim卡的imsi。

* 参数

无

* 返回值

成功返回string类型的imsi，失败返回整型-1。

* 示例

```python
>>> import sim
>>> sim.getImsi()
'460105466870381'
```



> **sim.getIccid()**

获取sim卡的iccid。

* 参数

无

* 返回值

成功返回string类型的iccid，失败返回整型-1。

* 示例

```python
>>> sim.getIccid()
'89860390845513443049'
```



> **sim.getPhoneNumber()**

获取sim卡的电话号码。

* 参数

无

* 返回值

成功返回string类型的phone number，失败返回整型-1。

* 示例

```python
>>> sim.getPhoneNumber()
'+8618166328752'
```



> **sim.getStatus()**

获取sim卡的状态。

* 参数

无

* 返回值

| 返回值 | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| 0      | SIM was removed.                                             |
| 1      | SIM is ready.                                                |
| 2      | Expecting the universal PIN./SIM is locked, waiting for a CHV1 password. |
| 3      | Expecting code to unblock the universal PIN./SIM is blocked, CHV1 unblocking password is required. |
| 4      | SIM is locked due to a SIM/USIM personalization check failure. |
| 5      | SIM is blocked due to an incorrect PCK; an MEP unblocking password is required. |
| 6      | Expecting key for hidden phone book entries.                 |
| 7      | Expecting code to unblock the hidden key.                    |
| 8      | SIM is locked; waiting for a CHV2 password.                  |
| 9      | SIM is blocked; CHV2 unblocking password is required.        |
| 10     | SIM is locked due to a network personalization check failure. |
| 11     | SIM is blocked due to an incorrect NCK; an MEP unblocking password is required. |
| 12     | SIM is locked due to a network subset personalization check failure. |
| 13     | SIM is blocked due to an incorrect NSCK; an MEP unblocking password is required. |
| 14     | SIM is locked due to a service provider personalization check failure. |
| 15     | SIM is blocked due to an incorrect SPCK; an MEP unblocking password is required. |
| 16     | SIM is locked due to a corporate personalization check failure. |
| 17     | SIM is blocked due to an incorrect CCK; an MEP unblocking password is required. |
| 18     | SIM is being initialized; waiting for completion.            |
| 19     | Use of CHV1/CHV2/universal PIN/code to unblock the CHV1/code to unblock the CHV2/code to unblock the universal PIN/ is blocked. |
| 20     | Invalid SIM card.                                            |
| 21     | Unknow status.                                               |



> **sim.enablePin(pin)**

启用sim卡PIN码验证，开启后需要输入正确的PIN验证成功后，sim卡才能正常使用。只有3次输入PIN码机会，3次都错误，sim卡被锁定，需要PUK来解锁。

* 参数

| 参数 | 参数类型 | 参数说明                                      |
| ---- | -------- | --------------------------------------------- |
| pin  | string   | PIN码，一般默认是‘1234’，最大长度不超过15字节 |

* 返回值

成功返回整型0，失败返回整型-1。

* 示例

```python
>>> sim.enablePin("1234")
0
```



> **sim.disablePin(pin)**

关闭sim卡PIN码验证。

* 参数

| 参数 | 参数类型 | 参数说明                                      |
| ---- | -------- | --------------------------------------------- |
| pin  | string   | PIN码，一般默认是‘1234’，最大长度不超过15字节 |

* 返回值

成功返回整型0，失败返回整型-1。

* 示例

```python
>>> sim.disablePin("1234")
0
```



> **sim.verifyPin(pin)**

sim卡PIN码验证。需要在调用sim.enablePin(pin)成功之后，才能进行验证，验证成功后，sim卡才能正常使用。

* 参数

| 参数 | 参数类型 | 参数说明                                      |
| ---- | -------- | --------------------------------------------- |
| pin  | string   | PIN码，一般默认是‘1234’，最大长度不超过15字节 |

* 返回值

验证成功返回整型0，验证失败返回整型-1。

* 示例

```python
>>> sim.verifyPin("1234")
0
```



> **sim.unblockPin(puk, newPin)**

sim卡解锁。当多次错误输入 PIN/PIN2 码后，SIM 卡状态为请求 PUK/PUK2 时，输入 PUK/PUK2 码和新的 PIN/PIN2 码进行解锁，puk码输入10次错误，SIM卡将被永久锁定自动报废。

* 参数

| 参数   | 参数类型 | 参数说明                                 |
| ------ | -------- | ---------------------------------------- |
| puk    | string   | PUK码，长度8位数字，最大长度不超过15字节 |
| newPin | string   | 新PIN码，最大长度不超过15字节            |

* 返回值

解锁成功返回整型0，解锁失败返回整型-1。

* 示例

```python
>>> sim.unblockPin("12345678", "0000")
0
```



> **sim.changePin(oldPin, newPin)**

更改sim卡PIN码。

* 参数

| 参数   | 参数类型 | 参数说明                        |
| ------ | -------- | ------------------------------- |
| oldPin | string   | 旧的PIN码，最大长度不超过15字节 |
| newPin | string   | 新的PIN码，最大长度不超过15字节 |

* 返回值

更改成功返回整型0，更改失败返回整型-1。

* 示例

```python
>>> sim.changePin("1234", "4321")
0
```



> **sim.readPhonebook(storage, start, end, username)**

获取 SIM 卡上指定电话本中的一条或多条电话号码记录。

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| storage  | int      | 需要读取电话号码记录的电话本存储位置，可选参数如下：<br/>0 – DC，1 – EN，2 – FD，3 – LD，4 – MC，5 – ME，6 – MT，7 – ON，<br/>8 – RC，9 – SM，10 – AP，11 – MBDN，12 – MN，13 – SDN，14 – ICI，15 - OCI |
| start    | int      | 需要读取电话号码记录的起始编号，start为 0 表示不使用编号获取电话号码记，start应小于等于end |
| end      | int      | 需要读取电话号码记录的结束编号，必须满足：end - start <= 20  |
| username | string   | 当 start为 0 时有效，电话号码中的用户名，暂不支持中文，最大长度不超过30字节<br/>注意：按username进行匹配时，并不是按完整的单词进行匹配，只要电话簿中已有记录的name是以username开头，那么就会匹配上 |

* 返回值

读取失败返回整型-1，成功返回一个元组，包含读取记录，格式如下：

`(record_number, [(index, username, phone_number), ... , (index, username, phone_number)])`

返回值参数说明：

`record_number` – 读取的记录数量，整型

`index` – 在电话簿中的索引位置，整型

`username` – 姓名，string类型

`phone_number` – 电话号码，string类型

* 示例

```python
>>> sim.readPhonebook(9, 1, 4, "")
(4,[(1,'Tom','15544272539'),(2,'Pony','15544272539'),(3,'Jay','18144786859'),(4,'Pondy','15544282538')])
>>> sim.readPhonebook(9, 0, 0, "Tom")
(1, [(1, 'Tom', '18144786859')])
>>> sim.readPhonebook(9, 0, 0, "Pony")
(1, [(2, 'Pony', '17744444444')])
>>> sim.readPhonebook(9, 0, 0, "Pon") #注意，这里只要是包含了‘pon’,都会被匹配上
(2, [(2, 'Pony', '17744444444'),(4,'Pondy','15544282538')])
```



> **sim. writePhonebook(storage, index, username, number)**

写入一条电话号码记录。

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| storage  | int      | 需要读取电话号码记录的电话本存储位置，可选参数如下：<br/>0 – DC，1 – EN，2 – FD，3 – LD，4 – MC，5 – ME，6 – MT，7 – ON，<br/>8 – RC，9 – SM，10 – AP，11 – MBDN，12 – MN，13 – SDN，14 – ICI，15 - OCI |
| index    | int      | 需要写入电话号码记录的在电话簿中的编号，范围1~500            |
| username | string   | 电话号码的用户名，长度范围不超过30字节，暂不支持中文名       |
| number   | string   | 电话号码，最大长度不超过20字节                               |

* 返回值

写入成功返回整型0，写入失败返回整型-1。

示例

```python
>>> sim.writePhonebook(9, 1, 'Tom', '18144786859')
0
```


#### voiceCall - 电话功能

模块功能：该模块提供电话功能相关接口。

说明：4G only的版本必须打开volte才能正常使用电话功能。



> **voiceCall.setAutoAnswer(seconds)**

设置自动应答时间。

* 参数 

| 参数        | 参数类型 | 参数说明                                                     |
| ----------- | -------- | ------------------------------------------------------------ |
| seconds     | int      | 自动应答时间，单位/s 范围：0-255)                            |

* 返回值

成功返回整型0，失败返回整型-1。

* 示例

```python
>>> import voiceCall
>>> voiceCall.setAutoAnswer(5)
0
```



> **voiceCall.callStart(phonenum)**

拨打电话。

* 参数 

| 参数        | 参数类型 | 参数说明                                                     |
| ----------- | -------- | ------------------------------------------------------------ |
| phonenum    | string   | 接收方电话号码                                               |

* 返回值

成功返回整型0，失败返回整型-1。

* 示例

```python
>>> voiceCall.callStart("13855169092")
0
```



> **voiceCall.callAnswer()**

接听电话。

* 参数 

无

* 返回值

成功返回整型0，失败返回整型-1。

* 示例

```python
>>> voiceCall.callAnswer()
0
```



> **voiceCall.callEnd()**

挂断电话。

* 参数 

无

* 返回值

成功返回整型0，失败返回整型-1。

* 示例

```python
>>> voiceCall.callEnd()
0
```


> **voiceCall.setCallback(usrFun))**

注册监听回调函数。在接听、挂断电话时会收到回调。

* 参数 

| 参数        | 参数类型 | 参数说明                                                     |
| ----------- | -------- | ------------------------------------------------------------ |
| usrFun      | function | 监听回调函数，                      |

* 返回值

成功返回整型0，失败返回整型-1。

* 示例

```python
def voice_callback(args):
     if args[0] == 4106:
         print('voicecall is waiting')
     elif args[0] == 4105:
         print('voicecall disconnect')
     elif args[0] == 4104:
         print('voicecall connected, CallNO.: ', args[6])
     elif args[0] == 4103:
         print('voicecall incoming call, PhoneNO.: ', args[6])

>>> voiceCall.setCallback(voice_callback)
0
>>> voiceCall.callStart('10086')
0
```


#### sms - 短信功能

模块功能：该模块提供短信功能相关接口。

说明：当前QuecPython底层为非volte版本，暂不支持电信发送短信。



> **sms.sendTextMsg(phoneNumber, msg, codeMode)**

发送TEXT类型的消息。

* 参数 

| 参数        | 参数类型 | 参数说明                                                     |
| ----------- | -------- | ------------------------------------------------------------ |
| phoneNumber | string   | 接收方手机号码，最大长度不超过20字节                         |
| msg         | string   | 待发送消息，长度不超过140个字节                              |
| codeMode    | string   | 使用的字符编码方式<br/>'GSM' - GSM编码方式<br/>'UCS2' - UCS2编码方式<br/>注意：<br/>（1）GSM编码方式用于发送英文短信；<br/>（2）UCS2编码方式可以用于发送中文短信以及英文短信。 |

* 返回值

发送成功返回整型0，失败返回整型-1。

* 示例

```python
# -*- coding: UTF-8 -*-
import sms

sms.sendTextMsg('18158626517', '这是一条中文测试短信！', 'UCS2')
sms.sendTextMsg('18158626517', 'Hello, world.', 'GSM')
sms.sendTextMsg('18158626517', '这是一条夹杂中文与英文的测试短信,hello world!', 'UCS2')
```



> **sms.sendPduMsg(phoneNumber, msg, codeMode)**

发送PDU类型的消息。

* 参数

| 参数        | 参数类型 | 参数说明                                                     |
| ----------- | -------- | ------------------------------------------------------------ |
| phoneNumber | string   | 接收方手机号码，最大长度不超过20字节                         |
| msg         | string   | 待发送消息，长度不超过140个字节                              |
| codeMode    | string   | 使用的字符编码方式<br/>'GSM' - GSM编码方式<br/>'UCS2' - UCS2编码方式<br/>注意：<br/>（1）GSM编码方式用于发送英文短信；<br/>（2）UCS2编码方式可以用于发送中文短信以及英文短信。 |

* 返回值

发送成功返回整型0，失败返回整型-1。

* 示例

```python
# -*- coding: UTF-8 -*-
import sms

if __name__ == '__main__':
    sms.sendPduMsg('18158626517', 'send pdu msg by GSM mode.', 'GSM')
    sms.sendPduMsg('18158626517', 'send pdu msg by UCS2 mode.', 'UCS2')
    sms.sendPduMsg('18158626517', '这是一条中文测试短信！通过PDU-UCS2模式', 'UCS2')   
```



> **sms.deleteMsg(index)**

删除指定索引的消息。

参数

| 参数  | 参数类型 | 参数说明                                                     |
| ----- | -------- | ------------------------------------------------------------ |
| index | int      | 需删除短信的索引号<br/>如果设置短信存储在SIM卡，则范围0~49<br/>如果设置短信存储在ME，则范围0~179，注意，当短信存储在ME时，只有对应的index索引处有短信存在，才能删除成功，否则删除会失败 |

返回值

删除成功返回整型0，失败返回整型-1。

示例

```python
>>> import sms
>>> sms.deleteMsg(0)
0
```



> **sms.setSaveLoc(mem1, mem2, mem3)**

设置短信存储位置。开机默认存储位置为SIM卡。一般SIM卡最大可存储50条短信，用户在使用时，如果短信存储在SIM卡中，要注意及时清理历史短信，防止SIM卡存储短信满了导致收不到新的短信。

* 参数

| 参数 | 参数类型 | 参数说明                                                     |
| ---- | -------- | ------------------------------------------------------------ |
| mem1 | string   | 读取和删除消息所在的位置，支持如下参数：<br/>"SM" - SIM消息存储<br/>"ME" - 移动设备信息存储<br/>"MT" - 暂不支持 |
| mem2 | string   | 写入和发送消息所在的位置，支持如下参数：<br/>"SM" - SIM消息存储<br/>"ME" - 移动设备信息存储<br/>"MT" - 暂不支持 |
| mem3 | string   | 接收消息的存储位置，支持如下参数：<br/>"SM" - SIM消息存储<br/>"ME" - 移动设备信息存储<br/>"MT" - 暂不支持 |

* 返回值

成功返回整型0，失败返回整型-1。

* 示例

```python
>>> import sms
>>> sms.setSaveLoc('SM', 'SM', 'SM')
0
```



> **sms.getSaveLoc()**

获取当前模块短信存储位置相关信息。

* 参数

无

* 返回值

成功返回一个元组，包含3个部分，返回值形式如下：

`([loc1, current_nums, max_nums],[loc2, current_nums, max_nums],[loc3, current_nums, max_nums])`

返回值参数说明：

`loc1` - 读取和删除消息所在的位置;

`loc2` - 写入和发送消息所在的位置；

`loc3` - 接收消息的存储位置；

`current_nums` - 当前空间已有短信数量；

`max_nums` - 当前空间最大短信存储数量；

* 示例

```python
>>> sms.getSaveLoc()
(['SM', 2, 50], ['SM', 2, 50], ['SM', 2, 50])
>>> sms.setSaveLoc('SM','ME','MT')
0
>>> sms.getSaveLoc()
(['SM', 2, 50], ['ME', 14, 180], ['MT', 2, 50])
```



> **sms.getMsgNums()**

获取短信的数量。

* 参数

  无

* 返回值

成功返回整型的短信数量值，失败返回整型-1。

* 示例

```python
>>> import sms
>>> sms.getMsgNums() # 执行本行前，先发送一条短信到模块
1
```



> **sms.searchPduMsg(index)**

以PDU方式获取短信内容。

* 参数

| 参数  | 参数类型 | 参数说明                                                     |
| ----- | -------- | ------------------------------------------------------------ |
| index | int      | 需要获取短信的索引，范围0 ~ MAX-1，MAX为模块存储短信的最大数量，取决于储存在SIM卡还是其他位置。 |

* 返回值

成功返回PDU类型的短信内容，string类型，失败返回整型-1。



> **sms.searchTextMsg(index)**

以TEXT方式获取短信内容。

* 参数

| 参数  | 参数类型 | 参数说明                     |
| ----- | -------- | ---------------------------- |
| index | int      | 需要获取短信的索引，范围0~49 |

* 返回值

成功返回TEXT类型的消息内容，返回格式如下，失败返回-1。

返回格式：(phoneNumber, msg, msgLen)

`phoneNumber` ：短信来源手机号

`msg` ：短信内容

`msgLen` ：短信消息长度

* 示例

```python
>>> import sms
>>> sms.sendPduMsg('+8618226172342', '123456789aa', 'GSM') # 自己给自己发送一条短信
>>> sms.searchPduMsg(0) # 以PDU方式获取短信内容，下面PDU格式短信需要解码后才能正常显示短信内容
'0891683110305005F0240BA19169256015F70000022141013044230B31D98C56B3DD70B97018'
>>> sms.searchTextMsg(0) # 以TEXT方式获取短信内容
('+8618226172342', '123456789aa', 22)
```



> **sms.getCenterAddr()**

获取短信中心号码。

* 参数

无

* 返回值

成功返回string类型的短信中心号码，失败返回-1。

* 示例

```python
>>> import sms
>>> sms.getCenterAddr()
'+8613800551500'
```



> **sms.setCenterAddr(addr)**

设置短信中心号码。若无特殊需求，不建议更改短信中心号码。

* 参数

| 参数 | 参数类型 | 参数说明                                       |
| ---- | -------- | ---------------------------------------------- |
| addr | string   | 需要设置的短信中心号码，最大长度不超过30字节。 |

* 返回值

设置成功返回整型0，失败返回整型-1。

* 示例

无



> **sms.getPduLength(pduMsg)**

获取指定PDU短信的长度。

参数

| 参数   | 参数类型 | 参数说明 |
| ------ | -------- | -------- |
| pduMsg | string   | PDU短信  |

返回值

成功返回整型PDU短信长度，失败返回整型-1。

示例

```python
>>> import sms
>>> sms.searchPduMsg(0)
'0891683108501505F0040D91688122162743F200000211529003332318C16030180C0683C16030180C0683E170381C0E87'
>>> sms.getPduLength(sms.searchPduMsg(0)) #注意，是获取PDU短信长度，不是上面字符串的长度
40
```



> **sms.setCallback(usrFun)**

注册监听回调函数。在发送和接收短信时，会触发该回调函数。

* 参数

| 参数   | 参数类型 | 参数说明                               |
| ------ | -------- | -------------------------------------- |
| usrFun | function | 监听回调函数，回调具体形式及用法见示例 |

* 返回值

注册成功返回整型0，失败返回整型-1。

* 示例

```python
import sms

def cb(args):
    flag = args[0]
    if flag == 0x1001:   # args[0]为0x1001时，有效参数及意义如下
        print('### msglen={},msg={}'.format(args[2], args[1]))
    elif flag == 0x1002: # args[0]为0x1002时，有效参数及意义如下
        print('$$$ numtype={:0>3d},numplan={:0>4d},len={},digits={}'.format(args[1],args[2],args[3],args[4]))
    elif flag == 0x1003: # args[0]为0x1003时，有效参数及意义如下
        print('type={}, storage={}, index={}'.format(args[1],args[2],args[3]))
    
sms.setCallback(cb)
```

回调函数中，当flag为0x1002时，参数意义说明：

| 参数名  | 描述                                                         |
| ------- | ------------------------------------------------------------ |
| numtype | TON(type-of-number)<br/>000—未知<br/>001—国际<br/>010—国内<br/>111—留作扩展 |
| numplan | NPI(numbering-plan-identification)，号码鉴别<br/>0000—未知<br/>0001—ISDN/电话号码(E.164/E.163)<br/>1111—留作扩展<br/>一般默认为0001(国际格式)，表示电话号码类型 |
| len     | 短信服务中心号码长度                                         |
| digits  | 短信服务中心号码                                             |

回调函数中，当flag为0x1003时，参数意义说明：

| 参数名  | 描述                                                         |
| ------- | ------------------------------------------------------------ |
| type    | 接收短信的类型<br>0 - SMS-DELIVER PDU<br>1 - SMS-DELIVER-REPORT PDU<br>2 - SMS-SUBMIT PDU<br>3 - SMS-SUBMIT-REPORT PDU<br>4 - SMS-STATUS-REPORT PDU<br>5 - SMS-COMMAND PDU<br>6 - CBS PDU<br>7 - LTE CBS PDU |
| storage | 短信存储位置<br>0 - BM，Broadcast message storage (in volatile memory)<br>1 - ME，ME message storage<br>2 - MT，Any of the storage locations associated with ME<br>3 - SM，SIM message storage<br>4 - SR，Status report storage |
| index   | 短信存储位置索引，从0开始                                    |



#### net - 网络相关功能

模块功能：该模块提供配置和查询网络模式信息等接口。

> **net.csqQueryPoll()**

获取csq信号强度。

* 参数

无

* 返回值

成功返回整型的csq信号强度值，失败返回整型值-1，返回值为99表示异常；

信号强度值范围0~31，值越大表示信号强度越好。

* 示例

```python
>>> import net
>>> net.csqQueryPoll()
31
```



> **net.getCellInfo()**

获取邻近 CELL 的信息。

* 参数

无

* 返回值

失败返回整型值-1，成功返回包含三种网络系统（GSM、UMTS、LTE）的信息的list，如果对应网络系统信息为空，则返回空的List。返回值格式如下：

`([(flag, cid, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, licd, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, mcc, mnc, pci, tac, earfcn, rssi),...])`

GSM网络系统返回值说明

| 参数  | 参数意义                                    |
| ----- | ------------------------------------------- |
| flag  | 返回 0 - 2， 0：present，1：inter，2：intra |
| cid   | 返回cid信息，0则为空                        |
| mcc   | 移动设备国家代码                            |
| mnc   | 移动设备网络代码                            |
| lac   | 位置区码                                    |
| arfcn | 无线频道编号                                |
| bsic  | 基站识别码                                  |
| rssi  | 接收的信号强度                              |

UMTS网络系统返回值说明

| 参数   | 参数意义                                    |
| ------ | ------------------------------------------- |
| flag   | 返回 0 - 2， 0：present，1：inter，2：intra |
| cid    | 返回cid信息，0则为空                        |
| lcid   | 区域标识号                                  |
| mcc    | 移动设备国家代码                            |
| mnc    | 移动设备网络代码                            |
| lac    | 位置区码u                                   |
| uarfcn | 无线频道编号                                |
| psc    | 基站识别码                                  |
| rssi   | 接收的信号强度                              |

LTE网络系统返回值说明

| 参数   | 参数意义                                    |
| ------ | ------------------------------------------- |
| flag   | 返回 0 - 2， 0：present，1：inter，2：intra |
| cid    | 返回cid信息，0则为空                        |
| mcc    | 移动设备国家代码                            |
| mnc    | 移动设备网络代码                            |
| pci    | 小区标识                                    |
| tac    | Tracing area code                           |
| earfcn | 无线频道编号 范围: 0 - 65535                |
| rssi   | 接收的信号强度                              |

* 示例

```python
>>> net.getCellInfo()
([], [], [(0, 14071232, 1120, 0, 123, 21771, 1300, -69), (3, 0, 0, 0, 65535, 0, 40936, -140), (3, 0, 0, 0, 65535, 0, 3590, -140), (3, 0, 0, 0, 63, 0, 40936, -112)])
```



> **net.getConfig()**

获取当前网络模式、漫游配置。

* 参数

无

* 返回值

失败返回整型值-1，成功返回一个元组，包含当前首选的网络制式与漫游打开状态。

网络制式

| 值   | 网络制式                                                     |
| ---- | ------------------------------------------------------------ |
| 0    | GSM                                                          |
| 1    | UMTS . not supported in EC100Y                               |
| 2    | GSM_UMTS, auto. not supported in EC100Y and EC200S           |
| 3    | GSM_UMTS, GSM preferred. not supported in EC100Y and EC200S  |
| 4    | SM_UMTS, UMTS preferred. not supported in EC100Y and EC200S  |
| 5    | LTE                                                          |
| 6    | GSM_LTE, auto, single link                                   |
| 7    | GSM_LTE, GSM preferred, single link                          |
| 8    | GSM_LTE, LTE preferred, single link                          |
| 9    | UMTS_LTE, auto, single link. not supported in EC100Y and EC200S |
| 10   | UMTS_LTE, UMTS preferred, single link. not supported in EC100Y and EC200S |
| 11   | UMTS_LTE, LTE preferred, single link . not supported in EC100Y and EC200S |
| 12   | GSM_UMTS_LTE, auto, single link. not supported in EC100Y and EC200S |
| 13   | GSM_UMTS_LTE, GSM preferred, single link. not supported in EC100Y and EC200S |
| 14   | GSM_UMTS_LTE, UMTS preferred, single link. not supported in EC100Y and EC200S |
| 15   | GSM_UMTS_LTE, LTE preferred, single link. not supported in EC100Y and EC200S |
| 16   | GSM_LTE, dual link                                           |
| 17   | UMTS_LTE, dual link. not supported in EC100Y and EC200S      |
| 18   | GSM_UMTS_LTE, dual link. not supported in EC100Y and EC200S  |

* 示例

```python
>>>net.getConfig ()
(8, False)
```



> **net.setConfig(mode, roaming)**

设置网络模式、漫游配置。

* 参数

| 参数    | 参数类型 | 参数说明                             |
| ------- | -------- | ------------------------------------ |
| mode    | int      | 网络制式，0~18，详见上述网络制式表格 |
| roaming | int      | 漫游开关(0：关闭， 1：开启)          |

* 返回值

设置成功返回整型值0，设置失败返回整型值-1。



> **net.getNetMode()**

获取网络配置模式。

* 参数

无

* 返回值

失败返回整型值-1，成功返回一个元组，格式为：`(selection_mode, mcc, mnc, act)`

返回值参数说明：
`selection_mode` ：方式，0 - 自动，1 - 手动
`mcc` ：移动设备国家代码
`mnc` ：移动设备网络代码
`act` ：首选网络的ACT模式

ACT模式

| 值   | ACT模式            |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | COMPACT            |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E TRAN A           |
| 10   | NONE               |

* 示例

```python
>>> net.getNetMode()
(0, '460', '46', 7)
```



> **net.getSignal()**

获取详细信号强度。

* 参数

无

* 返回值

失败返回整型值-1，成功返回一个元组，包含两个List(GW 、LTE)，返回值格式如下：

`([rssi, bitErrorRate, rscp, ecno], [rssi, rsrp, rsrq, cqi])`

返回值参数说明：

GW list：

`rssi` ：接收的信号强度

`bitErrorRate` ：误码率

`rscp` ：接收信号码功率

`ecno` ：导频信道

LTE list：

`rssi` ：接收的信号强度

`rsrp` ：下行参考信号的接收功率

`rsrq` ：下行特定小区参考信号的接收质量

`cqi` ：信道质量

* 示例

```python
>>>net.getSignal()
([99, 99, 255, 255], [-51, -76, -5, 255])
```



> **net.nitzTime()**

获取当前基站时间。

* 参数

无

* 返回值

失败返回整型值-1，成功返回一个元组，包含基站时间与对应时间戳与闰秒数（0表示不可用），格式为：

`(date, abs_time, leap_sec)`

`date` ：基站时间，string类型

`abs_time` ：基站时间的绝对秒数表示，整型

`leap_sec` ：闰秒数，整型

* 示例

```python
>>> net.nitzTime()
('20/11/26 02:13:25+32', 1606356805, 0)
```



> **net.operatorName()**

获取当前注网的运营商信息。

* 参数

无

* 返回值

失败返回整型值-1，成功返回一个元组，包含注网的运营商信息，格式为：

`(long_eons, short_eons, mcc, mnc)`

`long_eons` ：运营商信息全称，string类型

`short_eons` ：运营商信息简称，string类型

`mcc` ：移动设备国家代码，string类型

`mnc` ：移动设备网络代码，string类型

* 示例

```python
>>> net.operatorName()
('CHN-UNICOM', 'UNICOM', '460', '01')
```



> **net.getState()**

获取当前网络注册信息。

* 参数

无

* 返回值

失败返回整型值-1，成功返回一个元组，包含注网的网络注册信息，格式为：

`([voice_state, voice_lac, voice_cid, voice_rat, voice_reject_cause, voice_psc], [data_state, data _lac, data _cid, data _rat, data _reject_cause, data _psc])`

返回值参数说明：

`state` ：网络注册状态

`lac` ：位置区码

`cid` ：int类型id信息

`rat` ：注网制式

`reject_cause` ：注册被拒绝的原因

`psc` ：Primary Scrambling Code

网络注册状态

| 值   | 状态说明                                                     |
| ---- | ------------------------------------------------------------ |
| 0    | not registered, MT is not currently searching an operator to register to |
| 1    | registered, home network                                     |
| 2    | not registered, but MT is currently trying to attach or searching an operator to register to |
| 3    | registration denied                                          |
| 4    | unknown                                                      |
| 5    | registered, roaming                                          |
| 6    | egistered for “SMS only”, home network (not applicable)      |
| 7    | registered for “SMS only”, roaming (not applicable)          |
| 8    | attached for emergency bearer services only                  |
| 9    | registered for “CSFB not preferred”, home network (not applicable) |
| 10   | registered for “CSFB not preferred”, roaming (not applicable) |
| 11   | emergency bearer services only                               |

* 示例

```python
>>> net.getState()
([11, 26909, 232301323, 7, 0, 466], [0, 26909, 232301323, 7, 0, 0])
```



> **net.getCi()**

获取附近小区ID。

* 参数

无

* 返回值

成功返回一个list类型的数组，包含小区id，格式为：`[id, ……, id]`。数组成员数量并非固定不变，位置不同、信号强弱不同等都可能导致获取的结果不一样。

失败返回整型值-1。

* 示例

```python
>>> net.getCi()
[14071232, 0]
```



> **net.getMnc()**

获取附近小区的mnc。

* 参数

无

* 返回值

成功返回一个list类型的数组，包含小区mnc，格式为：`[mnc, ……, mnc]`。数组成员数量并非固定不变，位置不同、信号强弱不同等都可能导致获取的结果不一样。

失败返回整型值-1。

* 示例

```python
>>> net.getMnc()
[0, 0]
```



> **net.getMcc()**

获取附近小区的mcc。

* 参数

无

* 返回值

成功返回一个list类型的数组，包含小区mcc，格式为：`[mcc, ……, mcc]`。数组成员数量并非固定不变，位置不同、信号强弱不同等都可能导致获取的结果不一样。

失败返回整型值-1。

* 示例

```python
>>> net.getMcc()
[1120, 0]
```



> **net.getLac()**

获取附近小区的Lac。

* 参数

无

* 返回值

成功返回一个list类型的数组，包含小区lac，格式为：`[lac, ……, lac]`。数组成员数量并非固定不变，位置不同、信号强弱不同等都可能导致获取的结果不一样。

失败返回整型值-1。

* 示例

```python
>>> net.getLac()
[21771, 0]
```



> **net.getModemFun()**

获取当前工作模式模式。

* 参数

无

* 返回值

成功返回当前SIM模式：

0 ：全功能关闭

1 ：全功能开启（默认）

4 ：飞行模式

失败返回整型值-1。

* 示例

```python
>>> net.getModemFun()
1
```



> **net.setModemFun(function, rst)**

设置当前SIM模式。

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| function | int      | 设置SIM卡模式，0 - 全功能关闭， 1 - 全功能开启， 4 - 飞行模式 |
| rst      | int      | 可选参数 ，0 - 设置立即生效（默认为0），1 - 设置完重启       |

* 返回值

设置成功返回整型值0，设置失败返回整型值-1。

* 示例

```python
>>> net.setModemFun(4)
0
```



#### checkNet - 等待网络就绪

模块功能：checkNet模块主要用于【开机自动运行】的用户脚本程序，该模块提供API用来阻塞等待网络就绪，如果超时或者其他异常退出会返回错误码，所以如果用户的程序中有涉及网络相关的操作，那么在用户程序的开始应该调用 checkNet 模块中的方法以等待网络就绪。当然，用户也可以自己实现这个模块的功能。

**创建checkNet对象**

> **import checkNet**
>
> PROJECT_NAME = "QuecPython_Math_example"
> PROJECT_VERSION = "1.0.0"
> checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

* 功能

  创建checkNet对象。PROJECT_NAME 和 PROJECT_VERSION 是必须有的两个全局变量，用户可以根据自己的需要修改这两个变量的值。

* 参数

  | 参数            | 描述                       |
  | --------------- | -------------------------- |
  | PROJECT_NAME    | 用户项目名称，字符串类型   |
  | PROJECT_VERSION | 用户项目版本号，字符串类型 |

* 返回值

  无。

示例

```python
import checkNet

PROJECT_NAME = "XXXXXXXX"
PROJECT_VERSION = "XXXX"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)
```



> **checknet.poweron_print_once()**

* 功能

  开机时打印一些信息，主要用于提示用户。打印内容如下：

  PROJECT_NAME     	  : 用户项目名称
  PROJECT_VERSION 	 : 用户项目版本号
  FIRMWARE_VERSION  : 固件版本号
  POWERON_REASON   : 开机原因
  SIM_CARD_STATUS     : SIM卡状态

* 参数

  无

* 返回值

  无。

* 示例

```python 
import checkNet

PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

if __name__ == '__main__':
    # 在用户程序运行前增加下面这一句
    checknet.poweron_print_once()
	......
    
# 当用户程序开始运行时，会打印下面信息
==================================================
PROJECT_NAME     : QuecPython_Math_example
PROJECT_VERSION  : 1.0.0
FIRMWARE_VERSION : EC600UCNLBR01A01M16_OCPU_V01
POWERON_REASON   : 2
SIM_CARD_STATUS  : 1
==================================================
```



> **checknet.wait_network_connected(timeout)**

* 功能

  阻塞等待网络就绪。超时时间内，只要检测到拨号成功，则会立即返回，否则阻塞到超时时间到才会退出。

* 参数

| 参数    | 类型 | 说明                                              |
| ------- | ---- | ------------------------------------------------- |
| timeout | 整型 | 超时时间，单位秒，可设范围 [1, 3600]，默认值60s。 |

* 返回值

  返回值有2个，形式如下：

  `stagecode, subcode`

  各返回值说明如下：

  | 返回值    | 类型 | 说明                                                         |
  | --------- | ---- | ------------------------------------------------------------ |
  | stagecode | 整型 | 阶段码，表示 checkNet 模块当前在哪个阶段。<br>1 - 程序在获取SIM卡状态阶段，因为超时或者SIM卡状态异常，退出时的值；<br>2 - 程序在获取注网状态阶段，因为超时退出时的值；<br>3 - 程序在获取拨号状态阶段，返回时的值；<br>用户使用时，stagecode 正常返回值应该是3，如果是前两个值，说明是不正常的。 |
  | subcode   | 整型 | 子码，结合 stagecode 的值，来表示 checkNet 在不同阶段的具体状态。<br/>当 stagecode = 1 时：<br/>subcode 表示 SIM卡的状态，范围[0, 21]，每个值的详细说明，请参考：[https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=sim-sim%e5%8d%a1](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=sim-sim卡) <br/>中 sim.getStatus() 接口的返回值说明。<br/><br/>当 stagecode = 2 时：<br/>subcode 表示注网状态，范围[0, 11]，每个值的详细说明，请参考：[https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=net-%e7%bd%91%e7%bb%9c%e7%9b%b8%e5%85%b3%e5%8a%9f%e8%83%bd](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=net-网络相关功能)    中的 net.getState() 接口的返回值说明。<br/>subcode = -1，表示在超时时间内，获取注网状态失败；<br/>其他值参考上面链接中对应接口说明。<br/>如果在超时时间内，模块注网成功，就会进入 stagecode = 3 的阶段，不会在stagecode = 2 的阶段返回。<br/><br/>当 stagecode = 3 时：<br/>subcode = 0，表示在超时时间内，模块一直没有拨号成功；<br/>subcode = 1，表示在超时时间内，模块已经联网成功，即注网、拨号成功。 |

* 示例

```python
import checkNet

PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

if __name__ == '__main__':
    # 在用户程序运行前增加下面这一句
    stagecode, subcode = checknet.wait_network_connected(30)
    print('stagecode = {}, subcode = {}'.format(stagecode, subcode))
	......
    
# 当用户程序开始运行时，如果网络已就绪，则返回值如下：
stagecode = 3, subcode = 1
# 如果用户没有插sim卡，则返回值如下：
stagecode = 1, subcode = 0
# 如果sim卡处于被锁的状态，则返回值如下：
stagecode = 1, subcode = 2
```



**checkNet 异常返回处理**

根据前面 `checknet.wait_network_connected(timeout)` 接口返回值描述，用户可参考如下处理方式来排查和解决问题：

```python
import checkNet

PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

if __name__ == '__main__':
    # 在用户程序运行前增加下面这一句
    stagecode, subcode = checknet.wait_network_connected(30)
    print('stagecode = {}, subcode = {}'.format(stagecode, subcode))
    
    if stagecode == 1:
        # 如果 subcode = 0，说明没插卡，或者卡槽松动，需要用户去检查确认；
        # 如果是其他值，请参考官方wiki文档中关于sim卡状态值的描述，确认sim卡当前状态，然后做相应处理
    elif stagecode == 2:
        if subcode == -1:
            # 这种情况说明在超时时间内，获取注网状态API一直执行失败，在确认SIM卡可正常使用且能正常被模块识
            # 别的前提下，可联系我们的FAE反馈问题；
        elif subcode == 0:
            # 这种情况说明在超时时间内，模块一直没有注网成功，这时请按如下步骤排查问题：
            # （1）首先确认SIM卡状态是正常的，通过 sim 模块的 sim.getState() 接口获取，为1说明正常；
            # （2）如果SIM卡状态正常，确认当前信号强度，通过 net模块的 net.csqQueryPoll() 接口获取，
            #     如果信号强度比较弱，那么可能是因为当前信号强度较弱导致短时间内注网不成功，可以增加超时
            #	  时间或者换个信号比较好的位置再试试；
            # （3）如果SIM卡状态正常，信号强度也较好，但就是注不上网，请联系我们的FAE反馈问题；最好将相应
            #     SIM卡信息，比如哪个运营商的卡、什么类型的卡、卡的IMSI等信息也一并提供，必要时可以将
            #     SIM卡寄给我们来排查问题。
        else:
            # 请参考官方Wiki文档中 net.getState() 接口的返回值说明，确认注网失败原因
    elif stagecode == 3:
        if subcode == 1:
            # 这是正常返回情况，说明网络已就绪，即注网成功，拨号成功
        else:
            # 这种情况说明在超时时间内，拨号一直没有成功，请按如下步骤尝试：
            # （1）通过 sim 模块的 sim.getState() 接口获取sim卡状态，为1表示正常；
            # （2）通过 net 模块的 net.getState() 接口获取注网状态，为1表示正常；
            # （3）手动调用拨号接口尝试拨号，看看能否拨号成功，可参考官方Wiki文档中的 dataCall 模块
            #     的拨号接口和获取拨号结果接口；
            # （4）如果手动拨号成功了，但是开机拨号失败，那么可能是默认的apn配置表中没有与当前SIM卡匹配
            #     的apn，用户可通过 sim 模块的 sim.getImsi() 来获取 IMSI 码，确认IMSI的第四和第五			  #     位字符组成的数字是否在 01~13 的范围内，如果不在，说明当前默认apn配置表中无此类SIM卡对
            #     应的apn 信息，这种情况下，用户如果希望开机拨号成功，可以使用 dataCall.setApn(...)
            #     接口来设置保存用户自己的apn信息，然后开机重启，就会使用用户设置的apn来进行开机拨号；
            # （5）如果手动拨号也失败，那么请联系我们的FAE反馈问题，最好将相应SIM卡信息，比如哪个运营商
            #     的卡、什么类型的卡、卡的IMSI等信息也一并提供，必要时可以将SIM卡寄给我们来排查问题。
```



#### fota - 固件升级

模块功能：固件升级。

**创建fota对象**

> **import fota**
>
> **fota_obj = fota()**



> **fota_obj.write(bytesData, file_size)**

写入升级包数据流。

* 参数

| 参数      | 参数类型 | 参数说明                     |
| --------- | -------- | ---------------------------- |
| bytesData | bytes    | 升级包文件数据               |
| file_size | int      | 升级包文件总大小(单位：字节) |

* 返回值

写入成功返回整型值0，写入失败返回值整型值-1。



> **fota_obj.verify()**

数据校验。

* 参数

无

* 返回值

检验成功返回整型值0，校验失败返回整型值-1。

* 示例

```python
>>> fota_obj.verify()
0
```

**使用示例**

```python
'''
@Author: Pawn
@Date: 2020-07-28
@LastEditTime: 2020-11-30
@Description: example for module fota
@FilePath: example_fota_file.py
'''


import fota
import utime
import log
from misc import Power
import uos
import checkNet

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Fota_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
fota_log = log.getLogger("Fota")

# 此示例需要升级包文件（差分包等.bin文件）

def run():
    fota_obj = fota()  # 创建Fota对象
    file_size = uos.stat("/usr/FotaFile.bin")[6]  # 获取文件总字节数
    print(file_size)
    with open("/usr/FotaFile.bin", "rb")as f:   # rb模式打开.bin文件(需要制作升级包文件)
        while 1:
            c = f.read(1024)   # read
            if not c:
                break
            fota_obj.write(c, file_size)  # 写入.bin文件数据与文件总字节数

    fota_log.info("flush verify...")
    res = fota_obj.verify()  # 校验
    if res != 0:
        fota_log.error("verify error")
        return
    fota_log.info("flush power_reset...")
    utime.sleep(2)
    Power.powerRestart()   # 重启模块


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
    【本例程可以屏蔽下面这一行！】
    '''
    # checknet.wait_network_connected()

    fota_log.info("run start...")
    run()

```



#### app_fota - 用户文件升级

模块功能：用户文件升级

**创建app_fota对象**

1. 导入app_fota模块
2. 调用`new`方法创建app_fota对象

```python
import app_fota
fota = app_fota.new()
```

**下载单个文件**

> **fota.download(url, file_name)**

 - 参数

| 参数      | 参数类型 | 参数说明                 |
| --------- | -------- | ------------------------ |
| url       | str      | 待下载文件的url          |
| file_name | str      | 本地待升级文件的绝对路径 |


 - 返回值

成功返回0，否则返回-1。

**下载批量文件**

> **fota.bulk_download(info=[])**

 - 参数

| 参数 | 参数类型 | 参数说明                                                   |
| ---- | -------- | ---------------------------------------------------------- |
| info | list     | 批量下载列表，列表的元素均为包含了`url`和`file_name`的字典 |


 - 返回值
   返回下载失败的列表

 - 示例

```python
download_list = [{'url': 'http://www.example.com/app.py', 'file_name': '/usr/app.py'}, {'url': 'http://www.example.com/test.txt', 'file_name': '/usr/text.txt'}]
```

该示例中，假设`http://www.example.com/test.txt`下载失败，则该方法返回值为`[{url: 'http://www.example.com/test.txt', file_name: '/usr/text.txt'}]`

**设置升级标志**

> **fota.set_update_flag()**

 - 参数
   无

 - 返回值
   无

> 设置完成升级标志后，调用重启接口，重启后即可启动升级工作。
> 升级完成后会直接进入应用程序。

> 重启接口参考链接：http://qpy.quectel.com/wiki/#/zh-cn/api/?id=power



#### audio - 音频播放

模块功能：音频播放，支持TTS、mp3以及AMR文件播放。

##### TTS 

**创建TTS对象**

> **import audio**
> **tts = audio.TTS(device)**

* 参数

`device` ：设备类型，0 - 听筒，1 - 耳机，2 - 喇叭。

* 示例

```python
>>> import audio
>>> tts = audio.TTS(1)
```



> **tts.close()**

关闭TTS功能。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。



> **tts.play(priority, breakin, mode, str)**

语音播放，支持优先级0~4，数字越大优先级越高，每个优先级组可同时最多加入10个播放任务；播放策略说明如下：

1. 如果当前正在播放任务A，并且允许被打断，此时有高优先级播放任务B，那么会打断当前低优先级播放任务A，直接播放高优先级任务B；

2. 如果当前正在播放任务A，并且不允许被打断，此时有高优先级播放任务B，那么B播放任务将会加入到播放队列中合适的位置，等待A播放完成，再依次从队列中按照优先级从高到低播放其他任务；

3. 如果当前正在播放任务A，且不允许被打断，此时来了一个同优先级播放任务B，那么B会被加入到该优先级组播放队列队尾，等待A播放完成，再依次从队列中按照优先级从高到低播放其他任务；

4. 如果当前正在播放任务A，且允许被打断，此时来了一个同优先级播放任务B，那么会打断当前播放任务A，直接播放任务B；

5. 如果当前正在播放任务A，且任务A的优先级组播放队列中已经有几个播放任务存在，且该优先级组播放队列最后一个任务N是允许被打断的，此时如果来了一个同样优先级的播放任务B，那么任务B会直接覆盖掉任务N；也就是说，某个优先级组，只有最后一个元素是允许被打断的，即breakin为1，其他任务都是不允许被打断的；

6. 如果当前正在播放任务A，不管任务A是否允许被打断，此时来了一个优先级低于任务A的请求B，那么将B加入到B对应优先级组播放队列。

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| priority | int      | 播放优先级，支持优先级0~4，数值越大优先级越高                |
| breakin  | int      | 打断模式，0表示不允许被打断，1表示允许被打断                 |
| mode     | int      | 编码模式，1 - UNICODE16(Size end conversion)，2 - UTF-8，3 - UNICODE16(Don't convert) |
| str      | string   | 待播放字符串                                                 |

* 返回值

播放成功返回整型0；

播放失败返回整型-1；

无法立即播放，加入播放队列，返回整型1；

无法立即播放，且该请求的优先级组队列任务已达上限，无法加入播放队列，返回整型-2。

* 示例

```python
>>> import audio
>>> tts = audio.TTS(1)
#正在播放任务A，且A允许被打断，此时来了任务B，且优先级高于任务A，那么A会被#打断，直接播放B
>>> tts.play(1, 1, 2, '1111111111111111')  #任务A
0
>>> tts.play(2, 0, 2, '2222222222222222')  #任务B
0

#正在播放任务A，且A不允许被打断，此时来了任务B，且优先级高于任务A，那么B会#被加入播放队列，等待A播放完成播放B（假设播放队列之前为空）
>>> tts.play(1, 0, 2, '1111111111111111')  #任务A
0
>>> tts.play(2, 0, 2, '2222222222222222')  #任务B
1

#正在播放任务A，且A允许被打断，此时来了任务B，且优先级和A优先级一样，那么A
#会被打断，直接播放B
>>> tts.play(2, 1, 2, '2222222222222222222')  #任务A
0
>>> tts.play(2, 0, 2, '3333333333333333333')  #任务B
0

#正在播放任务A，且A不允许被打断，此时来了任务B，且优先级和A优先级一样，那么#B会被加入播放队列，等待A播放完成播放B（假设播放队列之前为空）
>>> tts.play(2, 0, 2, '2222222222222222222')  #任务A
0
>>> tts.play(2, 0, 2, '3333333333333333333')  #任务B
1

#正在播放A，且A不允许被打断，此时来了任务B，且任务B允许被打断，优先级与A相同，那么任务B会被加入到播放队列中，此时又来了一个任务C，且优先级和A、B相同，那么C会被加入播放队列中，且直接覆盖率任务B，所以A播放完成下一个播放的是C（假设播放队列之前为空）
>>> tts.play(2, 0, 2, '2222222222222222222')  #任务A
0
>>> tts.play(2, 1, 2, '3333333333333333333')  #任务B
1
>>> tts.play(2, 0, 2, '4444444444444444444')  #任务C
1

```

tts播放中文示例：

注意，python文件开头需要加上“# -*- coding: UTF-8 -*-”，如果播放的中文中有标点符号，要用英文的标点符号。

```python
# -*- coding: UTF-8 -*-
import audio

tts = audio.TTS(1)
str1 = '移联万物,志高行远' #这里的逗号是英文的逗号
tts.play(4, 0, 2, str1)
```



> **tts.setCallback(usrFun)**

注册用户的回调函数，用于通知用户TTS播放状态。注意，该回调函数中不要进行耗时以及阻塞性的操作，建议只进行简单、耗时短的操作。

* 参数

| 参数   | 参数类型 | 参数说明                     |
| ------ | -------- | ---------------------------- |
| usrFun | function | 用户回调函数，函数形式见示例 |

* 返回值

注册成功返回整型0，失败返回整型-1。

* 示例

```python
import audio

def tts_cb(event):
	if event == 2:
		print('TTS-play start.')
	elif event == 4:
		print('TTS-play finish.')

tts = audio.TTS(1)
tts.setCallback(tts_cb)
tts.play(1, 0, 2, 'QuecPython')
```

关于TTS播放回调函数参数event的几种状态值说明：

| event | 表示状态 |
| ----- | -------- |
| 2     | 开始播放 |
| 3     | 停止播放 |
| 4     | 播放完成 |



> **tts.getVolume()**

获取当前播放音量大小，音量值为0~9，0表示静音，默认值4。

* 参数

无

* 返回值

成功返回整型音量大小值，失败返回整型-1。

* 示例

```python
>>> tts.getVolume()
4
```



> **tts.setVolume(vol)**

设置播放音量大小。

* 参数

| 参数 | 参数类型 | 参数说明                       |
| ---- | -------- | ------------------------------ |
| vol  | int      | 音量值，音量值为0~9，0表示静音 |

* 返回值

成功返回整型音量值，失败返回整型-1。

* 示例

```python
>>> tts.setVolume(6)
0
```



> **tts.getSpeed()**

获取当前播放速度，速度值为0~9，值越大，速度越快，默认值4。

* 参数

无

* 返回值

成功返回当前播放速度，失败返回整型-1。

* 示例

```python
>>> tts.getSpeed()
4
```



> **tts.setSpeed(speed)**

设置TTS播放速度。

* 参数

| 参数  | 参数类型 | 参数说明                              |
| ----- | -------- | ------------------------------------- |
| speed | int      | 速度值，速度值为0~9，值越大，速度越快 |

* 返回值

成功返回整型0，失败返回整型-1。

* 示例

```python
>>> tts.setSpeed(6)
0
```



> **tts.getState()**

获取tts状态。

* 参数

无

* 返回值

0 – 整型值，表示当前无tts播放；

1 – 整型值，表示当前有tts正在播放。

* 示例

```python
>>> tts1 = audio.TTS(1)
>>> tts1.getState()
0
>>> tts1.play(1, 0, 2, '8787878787878787') 
0
>>> tts1.getState() #在上面tts播放过程中执行这句
1
```



> **tts.stop()**

停止TTS播放。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。

**使用示例**

```python
'''
@Author: Pawn
@Date: 2020-08-19
@Description: example for module TTS
@FilePath: example_tts_file.py
'''
import log
from audio import TTS
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_TTS_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
tts_Log = log.getLogger("TTS")


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
    【本例程可以屏蔽下面这一行！】
    '''
    # checknet.wait_network_connected()

    # 参数1：device （0：听筒，1：耳机，2：喇叭）
    tts = TTS(1)
    # 获取当前播放音量大小
    volume_num = tts.getVolume()
    tts_Log.info("Current TTS volume is %d" %volume_num)

    # 设置音量为6
    volume_num = 6
    tts.setVolume(volume_num)
    #  参数1：优先级 (0-4)
    #  参数2：打断模式，0表示不允许被打断，1表示允许被打断
    #  参数3：模式 （1：UNICODE16(Size end conversion)  2：UTF-8  3：UNICODE16(Don't convert)）
    #  参数4：数据字符串 （待播放字符串）
    tts.play(1, 1, 2, 'QuecPython') # 执行播放
    tts.close()   # 关闭TTS功能
```



##### Audio

**创建一个对象**

> **import audio**
>
> **aud = audio.Audio(device)**

* 参数

`device` ：设备类型，0 - 听筒，1 - 耳机，2 - 喇叭。

* 示例

```python
>>> import audio
>>> aud = audio.Audio(1)
```

> **aud.set_pa(gpio)**

设置输出的pa的gpio引脚，并开启pa功能目前支持AB类切D类，即两个上升沿的脉冲分别在1us<脉冲<12us

* 参数

| 参数 | 参数类型 | 参数说明                            |
| ---- | -------- | ----------------------------------- |
| gpio | int      | 设置输出的gpio，gpio可从Pin里面获取 |

- 返回值

设置成功返回整数1;

设置失败返回整数0;

- 示例

```python
>>> import audio
>>> from machine import Pin
>>> aud = audio.Audio(0)

>>> aud.set_pa(Pin.GPIO15)
1
#设置成功tts 和 aud播报输出aud AB类切D类脉冲
>>> aud.play(2, 1, 'U:/music.mp3')
0
```

> **aud.play(priority, breakin, filename)**

音频文件播放，支持mp3、amr和wav格式文件播放。支持优先级0~4，数字越大优先级越高，每个优先级组可同时最多加入10个播放任务，与TTS播放共用同一个播放队列。

* 参数

| 参数     | 参数类型 | 参数说明                                      |
| -------- | -------- | --------------------------------------------- |
| priority | int      | 播放优先级，支持优先级0~4，数值越大优先级越高 |
| breakin  | int      | 打断模式，0表示不允许被打断，1表示允许被打断  |
| filename | string   | 待播放的文件名称，包含文件存放路径            |

* 返回值

播放成功返回整型0；

播放失败返回整型-1；

无法立即播放，加入播放队列，返回整型1；

无法立即播放，且该请求的优先级组队列任务已达上限，无法加入播放队列，返回整型-2。

* 示例

```python
>>> import audio
>>> a = audio.Audio(1)

>>> a.play(2, 1, 'U:/music.mp3')  #文件名前面要加上路径
0
```

关于文件播放路径的说明：

用户分区路径固定为’U:/‘开头，表示用户分区的根目录，如果用户在根目录下新建audio目录，并将音频文件存放在根目录下的audio目录，那么播放接口中，传入的路径参数应该是：'U:/audio/music.mp3'。

* 说明

由于TTS和音频文件播放共用同一个播放队列，所以TTS中设置的播放优先级、打断模式不仅仅是和其他TTS播放任务比较，还会和音频文件播放任务的优先级和打断模式比较，反之，音频文件播放中设置的播放优先级与打断模式对TTS任务同样是有效的。



> **aud.stop()**

停止音频文件播放。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。



> **aud.setCallback(usrFun)**

注册用户的回调函数，用于通知用户音频文件播放状态。注意，该回调函数中不要进行耗时以及阻塞性的操作，建议只进行简单、耗时短的操作。

* 参数

| 参数   | 参数类型 | 参数说明                     |
| ------ | -------- | ---------------------------- |
| usrFun | function | 用户回调函数，函数形式见示例 |

* 返回值

注册成功返回整型0，失败返回整型-1。

* 示例

```python
import audio

def audio_cb(event):
	if event == 0:
		print('audio-play start.')
	elif event == 7:
		print('audio-play finish.')

aud = audio.Audio(1)
aud.setCallback(audio_cb)
aud.play(1, 0, 'U:/test.mp3')
```

关于audio播放回调函数参数event的几种状态值说明：

| event | 表示状态 |
| ----- | -------- |
| 0     | 开始播放 |
| 7     | 播放完成 |



> **aud.getState()**

获取audio初始化状态。

* 参数

无

* 返回值

audio初始化未完成返回整型值-1，初始化完成返回整型值0。



> **aud.getVolume()**

获取audio音量大小，默认值7。

* 参数

无

* 返回值

返回整型音量值。



> **aud.setVolume(vol)**

设置audio音量大小。

* 参数

| 参数 | 参数类型 | 参数说明                                   |
| ---- | -------- | ------------------------------------------ |
| vol  | int      | 音量等级，范围（1~11），数值越大，音量越大 |

* 返回值

设置成功返回整型0，失败返回整型-1。

* 示例

```python
>>> aud.setVolume(6)
0
>>> aud.getVolume()
6
```



##### Record

适配版本：EC100Y(V0009)及以上；EC600S(V0003)及以上。

**创建一个对象**

> **import audio**
>
> **record = audio.Record()**

* 参数

  无

* 返回值

返回 *-1* 表示创建失败 ; 若返回对象 ,则表示创建成功 。

* 示例

```python
import audio 
record_test = audio.Record()
```



> **record.start(file_name,seconds)**

开始录音。

* 参数

| 参数      | 参数类型 | 参数说明               |
| --------- | -------- | ---------------------- |
| file_name | str      | 录音文件名             |
| seconds   | int      | 需要录制时长，单位：秒 |

* 返回值

 0： 成功

-1:  文件覆盖失败

-2：文件打开失败

-3: 文件正在使用

-4：通道设置错误（只能设置0或1）

-5：定时器资源申请失败

-6 ：音频格式检测错误；

-7 ：该文件已经由其他对象创建了。

* 示例

```python
record_test.start(“test.wav”,40)	#录制wav格式
record_test.start(“test.amr”,40)	#录制amr格式
record_test.start(“test”,40)	#录制amr格式
```



> **record.stop()**

停止录音。

* 参数

无

* 返回值

无

* 示例

```python
record_test.stop()
```



> **record. getFilePath(file_name)**

读取录音文件的路径。

* 参数

  *file\_name*： 

  字符串 ,录音文件名 。

* 返回值

String：录音文件的路径

* 示例

```python
record_test.getFilePath(“test.wav”)
```



> **record.getData(file_name，offset, size)**

读取录音数据。

* 参数

| 参数      | 参数类型 | 参数说明             |
| --------- | -------- | -------------------- |
| file_name | str      | 录音文件名           |
| offset    | int      | 读取数据的偏移量     |
| size      | int      | 读取大小 ：需小于10K |

* 返回值

-1：读取数据错误

-2：文件打开失败

-3：偏移量设置错误

-4：文件正在使用

-5：设置超出文件大小（offset+size > file_size）

-6：读取size 大于10K

-7： 内存不足10K

-8： 文件不属于该对象

bytes:返回数据

* 示例

```python
record_test.getData(“test.amr”,0, 44) 
```



> **record.getSize(file_name)**

读取录音文件大小。

* 参数

| 参数      | 参数类型 | 参数说明   |
| --------- | -------- | ---------- |
| file_name | str      | 录音文件名 |



* 返回值

若获取成功,返回文件大小 ，

wav格式时，此值会比返回callback返回值大44 bytes（44 bytes为文件头）；

amr格式时，此值会比返回callback返回值大6 bytes（6 bytes为文件头）；否则 

*-1*  获取文件 大小 失败 ； 

*-2*  文件打开失败 ； 

*-3*  文件正在使用 ；

-4 文件不属于该对象

* 示例

```python
record_test.getSize(“test.amr”)
```



> **record.Delete(file_name/无参数)**

删除录音文件。

* 参数

*file\_name*： 

字符串 ,录音文件名 。

注意：当无参数传入时，删除该对象下所有录音文件

* 返回值

 0：成功

-1：文件不存在 

-2：文件正在使用

-3 :  文件不属于该对象

* 示例

```python
record_test.Delete(“test.amr”)
record_test.Delete()
```



> **record.exists(file_name)**

判断录音文件是否存在。

* 参数

| 参数     | 参数类型 | 参数说明   |
| -------- | -------- | ---------- |
| ile_name | str      | 录音文件名 |



* 返回值

true：   文件存在

false：  文件不存在

-1 文件不属于该对象

* 示例

```python
record_test.exists(“test.amr”)
```



> **record.isBusy()**

判断是否正在录音

* 参数

无

* 返回值

0： idle

1:  busy

* 示例

```python
record_test.isBusy()
```



> **record.end_callback(callback)**

设置录音结束回调

* 参数

| 参数     | 参数类型 | 参数说明 |
| -------- | -------- | -------- |
| callback | api      | 回调api  |



* 返回值

0： 成功

other: 失败  

* 示例

```python
def record_callback(para): 
	print("file_name:",para[0])   # 返回文件路径 
    print("audio_len:",para[1])   # 返回录音长度 
    print("audio_state:",para[2])  
    # 返回录音状态 -1: error 0:start 3:  成功 
record_test.end_callback(record_callback)
```



> **record.gain(code_gain,dsp_gain)**

查看该对象下录音文件列表

* 参数

| 参数      | 参数类型 | 参数说明               |
| --------- | -------- | ---------------------- |
| code_gain | int      | 上行编解码器增益 [0,4] |
| dsp_gain  | int      | 上行数字增益 [-36,12]  |



* 返回值

0: 成功

* 示例

```python
record_test.gain(4,12)
```



> **record.list_file()**

查看该对象下录音文件列表

* 参数

无

* 返回值

*str*  字符串。录音文件列表  

* 示例

```python
record_test.list_file()
```



**示例代码**

```python
import utime
import audio
from machine import Pin


flag = 1
'''
外接喇叭播放录音文件，参数选择0
'''
aud = audio.Audio(0)
tts = audio.TTS(0)

aud.setVolume(11)
'''
(EC600S)外接喇叭播放录音文件，需要下面这一句来使能
(EC100Y不需要执行下面这一句)
'''
# audio_EN = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)


def record_callback(args):
    global flag
    print('file_name:{}'.format(args[0]))
    print('file_size:{}'.format(args[1]))
    print('record_sta:{}'.format(args[2]))

    record_sta = args[2]
    if record_sta == 3:
        print('The recording is over, play it')
        tts.play(1, 0, 2, '录音结束,准备播放录音文件')
        aud.play(1, 0, record.getFilePath())
        flag = 0
    elif record_sta == -1:
        print('The recording failure.')
        tts.play(1, 0, 2, '录音失败')
        flag = 0

record = audio.Record()
record.end_callback(record_callback)
record.start('recordfile.wav', 10)

while 1:
    if flag:
        pass
    else:
        break
```



#### misc - 其他

模块功能：提供关机、软件重启、PWM以及ADC相关功能。

##### Power

关机以及软件重启。

> **from misc import Power**
>
> **Power.powerDown()**

模块关机。

* 参数

无

* 返回值

无



> **Power.powerRestart()**

模块重启。

* 参数

无

* 返回值

无



> **Power. powerOnReason()**

获取模块启动原因。

* 参数

无

* 返回值

返回int数值，解释如下：

1：正常电源开机 

2：重启 

3：VBAT 

4：RTC定时开机

5：Fault 

6：VBUS

0：未知



> **Power. powerDownReason()**

获取模块上次关机原因。

* 参数

无

* 返回值

1：正常电源关机

2：电压过高

3：电压偏低

4：超温

5：WDT

6：VRTC 偏低

0：未知



> **Power. getVbatt()**

获取电池电压，单位mV。

* 参数

无

* 返回值

int类型电压值。

* 示例

```python
>>> Power.getVbatt()
3590
```



##### PWM

**常量说明**

| 常量     | 说明 |
| -------- | ---- |
| PWM.PWM0 | PWM0 |
| PWM.PWM1 | PWM1 |
| PWM.PWM2 | PWM2 |
| PWM.PWM3 | PWM3 |



**创建一个pwm对象**

> **from misc import PWM**
>
> **pwm = PWM(PWM.PWMn,PWM.ABOVE_xx, highTime, cycleTime)**

* 参数

| 参数      | 参数类型 | 参数说明                                                     |
| --------- | -------- | ------------------------------------------------------------ |
| PWMn      | int      | PWM号<br/>注：EC100YCN平台，支持PWM0-PWM3，对应引脚如下：<br/>PWM0 – 引脚号19<br/>PWM1 – 引脚号18<br/>PWM2 – 引脚号23<br/>PWM3 – 引脚号22<br/>注：EC600SCN平台，支持PWM0-PWM3，对应引脚如下：<br/>PWM0 – 引脚号52<br/>PWM1 – 引脚号53<br/>PWM2 – 引脚号70<br/>PWM3 – 引脚号69 |
| ABOVE_xx  | int      | PWM.ABOVE_MS				ms级取值范围：(0,1023]<br/>PWM.ABOVE_1US				us级取值范围：(0,157]<br/>PWM.ABOVE_10US				us级取值范围：(1,1575]<br/>PWM.ABOVE_BELOW_US			ns级 取值(0,1024] |
| highTime  | int      | ms级时，单位为ms<br/>us级时，单位为us<br/>ns级别：需要使用者计算<br/>               频率 = 13Mhz / cycleTime<br/>               占空比 = highTime/ cycleTime |
| cycleTime | int      | ms级时，单位为ms<br/>us级时，单位为us<br/>ns级别：需要使用者计算<br/>             频率 = 13Mhz / cycleTime<br/>             占空比 = highTime/ cycleTime |

* 示例

```python
>>> from misc import PWM
>>> pwm1 = PWM(PWM.PWM1, PWM.BOVE_MS, 100, 200)
```



> **pwm.open()**

开启PWM输出。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。



> **pwm.close()**

关闭PWM输出。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。



**使用示例**

```python
# PWM使用示例

from misc import PWM
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_PWM_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

'''
* 参数1：PWM号
        注：EC100YCN平台，支持PWM0~PWM3，对应引脚如下：
        PWM0 – 引脚号19
        PWM1 – 引脚号18
        PWM2 – 引脚号23
        PWM3 – 引脚号22

        注：EC600SCN平台，支持PWM0~PWM3，对应引脚如下：
        PWM0 – 引脚号52
        PWM1 – 引脚号53
        PWM2 – 引脚号70
        PWM3 – 引脚号69
* 参数2：high_time
        高电平时间，单位ms
* 参数3：cycle_time
        pwm整个周期时间，单位ms
'''
# 需要配合外设或者使用杜邦线短接对应引脚测试

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
    【本例程可以屏蔽下面这一行！】
    '''
    # checknet.wait_network_connected()

    pwm = PWM(PWM.PWM0, PWM.ABOVE_MS, 100, 200)  # 初始化一个pwm对象
    pwm.open()  # 开启PWM输出
    utime.sleep(10)
    pwm.close()  # 关闭pwm输出
```



##### ADC

**常量说明**

| 常量     | 说明     |
| -------- | -------- |
| ADC.ADC0 | ADC通道0 |
| ADC.ADC1 | ADC通道1 |



**创建一个ADC对象**

> **from misc import ADC**
>
> **adc = ADC()**

* 示例

```python
>>> from misc import ADC
>>> adc = ADC()
```



> **adc.open()**

ADC功能初始化。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。



> **adc.read(ADCn)**

读取指定通道的电压值，单位mV。

* 参数

| 参数 | 参数类型 | 参数说明                                                     |
| ---- | -------- | ------------------------------------------------------------ |
| ADCn | int      | ADC通道<br/>EC100Y平台支持ADC0，ADC1，对应引脚如下<br/>ADC0 – 引脚号39<br/>ADC1 – 引脚号81<br/>EC600S平台支持ADC0，对应引脚如下<br/>ADC0 – 引脚号19<br/>ADC1 – 引脚号20 |

* 返回值

成功返回指定通道电压值，错误返回整型-1。

* 示例

```python
>>>adc.read(ADC.ADC0)  #读取ADC通道0电压值
613
>>>adc.read(ADC.ADC1)  #读取ADC通道1电压值
605
```



> **adc.close()**

关闭ADC。

* 参数

无

* 返回值

0关闭成功，-1关闭失败。



#### modem - 设备相关

模块功能：设备信息获取。

> **modem.getDevImei()**

获取设备的IMEI。

* 参数

无

返回值

成功返回string类型设备的IMEI，失败返回整型值-1。

* 示例

```python
>>> import modem
>>> modem.getDevImei()
'866327040830317'
```



> **modem.getDevModel()**

获取设备型号。

* 参数

无

* 返回值

成功返回string类型设备型号，失败返回整型值-1。

* 示例

```python
>>> modem.getDevModel()
'EC100Y'
```



> **modem.getDevSN()**

获取设备序列号。

* 参数

无

* 返回值

成功返回string类型设备序列号，失败返回整型值-1。

* 示例

```python
>>> modem.getDevSN()
'D1Q20GM050038341P'
```



> **modem.getDevFwVersion()**

获取设备固件版本号。

* 参数

无

* 返回值

成功返回string类型固件版本号，失败返回整型值-1。

* 示例

```python
>>> modem.getDevFwVersion()
'EC100YCNAAR01A01M16_OCPU_PY'
```



> **modem.getDevProductId()**

获取设备的制造商ID。

* 参数

无

* 返回值

成功返回设备制造商ID，失败返回整型值-1。

* 示例

```python
>>> modem.getDevProductId()
'Quectel'
```



#### machine - 硬件相关功能

模块功能:  包含与特定电路板上的硬件相关的特定功能。该模块中的大多数功能允许直接和不受限制地访问和控制系统上的硬件。

##### Pin

类功能：GPIO读写操作。

**常量说明**

| 常量             | 适配平台                   | 说明      |
| ---------------- | ------------------------ | -------- |
| Pin.GPIO1        | EC600S / EC600N / EC100Y | GPIO1    |
| Pin.GPIO2        | EC600S / EC600N / EC100Y | GPIO2    |
| Pin.GPIO3        | EC600S / EC600N / EC100Y | GPIO3    |
| Pin.GPIO4        | EC600S / EC600N / EC100Y | GPIO4    |
| Pin.GPIO5        | EC600S / EC600N / EC100Y | GPIO5    |
| Pin.GPIO6        | EC600S / EC600N / EC100Y | GPIO6    |
| Pin.GPIO7        | EC600S / EC600N / EC100Y | GPIO7    |
| Pin.GPIO8        | EC600S / EC600N / EC100Y | GPIO8    |
| Pin.GPIO9        | EC600S / EC600N / EC100Y | GPIO9    |
| Pin.GPIO10       | EC600S / EC600N / EC100Y | GPIO10   |
| Pin.GPIO11       | EC600S / EC600N / EC100Y | GPIO11   |
| Pin.GPIO12       | EC600S / EC600N / EC100Y | GPIO12   |
| Pin.GPIO13       | EC600S / EC600N / EC100Y | GPIO13   |
| Pin.GPIO14       | EC600S / EC600N / EC100Y | GPIO14   |
| Pin.GPIO15       | EC600S / EC600N / EC100Y | GPIO15   |
| Pin.GPIO16       | EC600S / EC600N / EC100Y | GPIO16   |
| Pin.GPIO17       | EC600S / EC600N / EC100Y | GPIO17   |
| Pin.GPIO18       | EC600S / EC600N / EC100Y | GPIO18   |
| Pin.GPIO19       | EC600S / EC600N / EC100Y | GPIO19   |
| Pin.GPIO20       | EC600S / EC600N          | GPIO20   |
| Pin.GPIO21       | EC600S / EC600N          | GPIO21   |
| Pin.GPIO22       | EC600S / EC600N          | GPIO22   |
| Pin.GPIO23       | EC600S / EC600N          | GPIO23   |
| Pin.GPIO24       | EC600S / EC600N          | GPIO24   |
| Pin.GPIO25       | EC600S / EC600N          | GPIO25   |
| Pin.GPIO26       | EC600S / EC600N          | GPIO26   |
| Pin.GPIO27       | EC600S / EC600N          | GPIO27   |
| Pin.GPIO28       | EC600S / EC600N          | GPIO28   |
| Pin.GPIO29       | EC600S / EC600N          | GPIO29   |
| Pin.IN           | --                       | 输入模式 |
| Pin.OUT          | --                       | 输出模式 |
| Pin.PULL_DISABLE | --                       | 浮空模式 |
| Pin.PULL_PU      | --                       | 上拉模式 |
| Pin.PULL_PD      | --                       | 下拉模式 |

**GPIO对应引脚号说明**

文档中提供的GPIO引脚号对应的为模块外部的引脚编号，例如EC600S下GPIO1对应引脚号22，这里的引脚号22为模块外部的引脚编号。可参考提供的硬件资料查看模块外部的引脚编号。

**创建gpio对象**

> **gpio = Pin(GPIOn, direction, pullMode, level)**

* 参数

| 参数      | 类型 | 说明                                                         |
| :-------- | :--- | ------------------------------------------------------------ |
| GPIOn     | int  | 引脚号<br />EC100YCN平台引脚对应关系如下（引脚号为外部引脚编号）：<br />GPIO1 – 引脚号22<br />GPIO2 – 引脚号23<br />GPIO3 – 引脚号38<br />GPIO4 – 引脚号53<br />GPIO5 – 引脚号54<br />GPIO6 – 引脚号104<br />GPIO7 – 引脚号105<br />GPIO8 – 引脚号106<br />GPIO9 – 引脚号107<br />GPIO10 – 引脚号178<br />GPIO11 – 引脚号195<br />GPIO12 – 引脚号196<br />GPIO13 – 引脚号197<br />GPIO14 – 引脚号198<br />GPIO15 – 引脚号199<br />GPIO16 – 引脚号203<br />GPIO17 – 引脚号204<br />GPIO18 – 引脚号214<br />GPIO19 – 引脚号215<br />EC600SCN/EC600NCN平台引脚对应关系如下（引脚号为模块外部引脚编号）：<br />GPIO1 – 引脚号10<br />GPIO2 – 引脚号11<br />GPIO3 – 引脚号12<br />GPIO4 – 引脚号13<br />GPIO5 – 引脚号14<br />GPIO6 – 引脚号15<br />GPIO7 – 引脚号16<br />GPIO8 – 引脚号39<br />GPIO9 – 引脚号40<br />GPIO10 – 引脚号48<br />GPIO11 – 引脚号58<br />GPIO12 – 引脚号59<br />GPIO13 – 引脚号60<br />GPIO14 – 引脚号61<br />GPIO15 – 引脚号62<br/>GPIO16 – 引脚号63<br/>GPIO17 – 引脚号69<br/>GPIO18 – 引脚号70<br/>GPIO19 – 引脚号1<br/>GPIO20 – 引脚号3<br/>GPIO21 – 引脚号49<br/>GPIO22 – 引脚号50<br/>GPIO23 – 引脚号51<br/>GPIO24 – 引脚号52<br/>GPIO25 – 引脚号53<br/>GPIO26 – 引脚号54<br/>GPIO27 – 引脚号55<br/>GPIO28 – 引脚号56<br/>GPIO29 – 引脚号57 |
| direction | int  | IN – 输入模式，OUT – 输出模式                                |
| pullMode  | int  | PULL_DISABLE – 浮空模式<br />PULL_PU – 上拉模式<br />PULL_PD – 下拉模式 |
| level     | int  | 0 - 设置引脚为低电平, 1- 设置引脚为高电平                    |

* 示例

```python
from machine import Pin
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
```



> **Pin.read()**

获取PIN脚电平。

* 参数 

无

* 返回值

PIN脚电平，0-低电平，1-高电平。



> **Pin.write(value)**

设置PIN脚电平,设置高低电平前需要保证引脚为输出模式。

* 参数

| 参数  | 类型 | 说明                                                         |
| ----- | ---- | ------------------------------------------------------------ |
| value | int  | 0 - 当PIN脚为输出模式时，设置当前PIN脚输出低;  <br />1 - 当PIN脚为输出模式时，设置当前PIN脚输出高 |

* 返回值

设置成功返回整型值0，设置失败返回整型值-1。

* 示例

```python
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
>>> gpio1.write(1)
0
>>> gpio1.read()
1
```

**使用示例**

```python
# Pin使用示例

from machine import Pin
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Pin_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

'''
* 参数1：引脚号
        EC100YCN平台引脚对应关系如下：
        GPIO1 – 引脚号22
        GPIO2 – 引脚号23
        GPIO3 – 引脚号38
        GPIO4 – 引脚号53
        GPIO5 – 引脚号54
        GPIO6 – 引脚号104
        GPIO7 – 引脚号105
        GPIO8 – 引脚号106
        GPIO9 – 引脚号107
        GPIO10 – 引脚号178
        GPIO11 – 引脚号195
        GPIO12 – 引脚号196
        GPIO13 – 引脚号197
        GPIO14 – 引脚号198
        GPIO15 – 引脚号199
        GPIO16 – 引脚号203
        GPIO17 – 引脚号204
        GPIO18 – 引脚号214
        GPIO19 – 引脚号215

        EC600SCN/EC600NCN平台引脚对应关系如下：
        GPIO1 – 引脚号10
        GPIO2 – 引脚号11
        GPIO3 – 引脚号12
        GPIO4 – 引脚号13
        GPIO5 – 引脚号14
        GPIO6 – 引脚号15
        GPIO7 – 引脚号16
        GPIO8 – 引脚号39
        GPIO9 – 引脚号40
        GPIO10 – 引脚号48
        GPIO11 – 引脚号58
        GPIO12 – 引脚号59
        GPIO13 – 引脚号60
        GPIO14 – 引脚号61
        GPIO15 – 引脚号62
        GPIO16 – 引脚号63
        GPIO17 – 引脚号69
        GPIO18 – 引脚号70
        GPIO19 – 引脚号1
        GPIO20 – 引脚号3
        GPIO21 – 引脚号49
        GPIO22 – 引脚号50
        GPIO23 – 引脚号51
        GPIO24 – 引脚号52
        GPIO25 – 引脚号53
        GPIO26 – 引脚号54
        GPIO27 – 引脚号55
        GPIO28 – 引脚号56
        GPIO29 – 引脚号57
* 参数2：direction
        IN – 输入模式
        OUT – 输出模式
* 参数3：pull
        PULL_DISABLE – 禁用模式
        PULL_PU – 上拉模式
        PULL_PD – 下拉模式
* 参数4：level
        0 设置引脚为低电平
        1 设置引脚为高电平
'''
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)

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
    【本例程可以屏蔽下面这一行！】
    '''
    # checknet.wait_network_connected()

    gpio1.write(1) # 设置 gpio1 输出高电平
    val = gpio1.read() # 获取 gpio1 的当前高低状态
    print('val = {}'.format(val))

```



##### UART

类功能：uart串口数据传输。

**常量说明**

| 常量       | 说明  |
| ---------- | ----- |
| UART.UART0 | UART0 |
| UART.UART1 | UART1 |
| UART.UART2 | UART2 |
| UART.UART3 | UART3 |



**创建uart对象**

> **uart = UART(UART.UARTn, buadrate, databits, parity, stopbits, flowctl)**

* 参数

| 参数     | 类型 | 说明                                                         |
| :------- | :--- | ------------------------------------------------------------ |
| UARTn    | int  | 端口号<br />EC100YCN平台与EC600SCN平台,UARTn作用如下：<br />UART0 - DEBUG PORT<br />UART1 – BT PORT<br />UART2 – MAIN PORT<br />UART3 – USB CDC PORT |
| buadrate | int  | 波特率，常用波特率都支持，如4800、9600、19200、38400、57600、115200、230400等 |
| databits | int  | 数据位（5~8）                                                |
| parity   | int  | 奇偶校验（0 – NONE，1 – EVEN，2 - ODD）                      |
| stopbits | int  | 停止位（1~2）                                                |
| flowctl  | int  | 硬件控制流（0 – FC_NONE， 1 – FC_HW）                        |

* 示例

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
```



> **uart.any()**

返回接收缓存器中有多少字节的数据未读。

* 参数

无

* 返回值

返回接收缓存器中有多少字节的数据未读。

* 示例

```python
>>> uart.any()
20 #表示接收缓冲区中有20字节数据未读
```



> **uart.read(nbytes)**

从串口读取数据。

* 参数

| 参数   | 类型 | 说明           |
| ------ | ---- | -------------- |
| nbytes | int  | 要读取的字节数 |

* 返回值

返回读取的数据。



> **uart.write(data)**

发送数据到串口。

* 参数

| 参数 | 类型   | 说明       |
| ---- | ------ | ---------- |
| data | string | 发送的数据 |

* 返回值

返回发送的字节数。



> **uart.close()**

关闭串口。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。



**UART使用示例**

```python
"""
运行本例程，需要通过串口线连接开发板的 MAIN 口和PC，在PC上通过串口工具
打开 MAIN 口，并向该端口发送数据，即可看到 PC 发送过来的消息。
"""
import _thread
import utime
import log
from machine import UART
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_UART_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

'''
 * 参数1：端口
        注：EC100YCN平台与EC600SCN平台，UARTn作用如下
        UART0 - DEBUG PORT
        UART1 – BT PORT
        UART2 – MAIN PORT
        UART3 – USB CDC PORT
 * 参数2：波特率
 * 参数3：data bits  （5~8）
 * 参数4：Parity  （0：NONE  1：EVEN  2：ODD）
 * 参数5：stop bits （1~2）
 * 参数6：flow control （0: FC_NONE  1：FC_HW）
'''


# 设置日志输出级别
log.basicConfig(level=log.INFO)
uart_log = log.getLogger("UART")

state = 5


def uartWrite():
    count = 10
    # 配置uart
    uart = UART(UART.UART2, 115200, 8, 0, 1, 0)
    while count:
        write_msg = "Hello count={}".format(count)
        # 发送数据
        uart.write(write_msg)
        uart_log.info("Write msg :{}".format(write_msg))
        utime.sleep(1)
        count -= 1
    uart_log.info("uartWrite end!")


def UartRead():
    global state
    uart = UART(UART.UART2, 115200, 8, 0, 1, 0)
    while 1:
        # 返回是否有可读取的数据长度
        msgLen = uart.any()
        # 当有数据时进行读取
        if msgLen:
            msg = uart.read(msgLen)
            # 初始数据是字节类型（bytes）,将字节类型数据进行编码
            utf8_msg = msg.decode()
            # str
            uart_log.info("UartRead msg: {}".format(utf8_msg))
            state -= 1
            if state == 0:
                break
        else:
            continue



def run():
    # 创建一个线程来监听接收uart消息
    _thread.start_new_thread(UartRead, ())


if __name__ == "__main__":
    '''
    手动运行本例程时，可以去掉该延时，如果将例程文件名改为main.py，希望开机自动运行时，需要加上该延时,
    否则无法从CDC口看到下面的 poweron_print_once() 中打印的信息
    '''
    utime.sleep(5)
    checknet.poweron_print_once()
    '''
    如果用户程序包含网络相关代码，必须执行 wait_network_connected() 等待网络就绪（拨号成功）；
    如果是网络无关代码，可以屏蔽 wait_network_connected()
    【本例程可以屏蔽下面这一行！】
    '''
    # checknet.wait_network_connected()

    uartWrite()
    run()
    while 1:
        if state:
            pass
        else:
            break

# 运行结果示例
'''
INFO:UART:Write msg :Hello count=8
INFO:UART:Write msg :Hello count=7
INFO:UART:Write msg :Hello count=6
INFO:UART:Write msg :Hello count=5
INFO:UART:Write msg :Hello count=4
INFO:UART:Write msg :Hello count=3
INFO:UART:Write msg :Hello count=2
INFO:UART:Write msg :Hello count=1
INFO:UART:uartWrite end!
INFO:UART:UartRead msg: read msg 1

INFO:UART:UartRead msg: read msg 2

INFO:UART:UartRead msg: read msg 3
'''

```



##### Timer

类功能：硬件定时器。

PS:使用该定时器时需注意：定时器0-3，每个在同一时间内只能执行一件任务，且多个对象不可使用同一个定时器。

**常量说明**

| 常量           | 说明                       |
| -------------- | -------------------------- |
| Timer.Timer0   | 定时器0                    |
| Timer.Timer1   | 定时器1                    |
| Timer.Timer2   | 定时器2                    |
| Timer.Timer3   | 定时器3                    |
| Timer.ONE_SHOT | 单次模式，定时器只执行一次 |
| Timer.PERIODIC | 周期模式，定时器循环执行   |



**创建Timer对象**

> **timer = Timer(Timern)**

创建Timer对象。

* 参数

| 参数   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| Timern | int  | 定时器号<br />支持定时器Timer0~Timer3（使用该定时器时需注意：定时器0-3，每个在同一时间内只能执行一件任务，且多个对象不可使用同一个定时器。） |

* 示例

```python
>>> from machine import Timer
>>> timer1 = Timer(Timer.Timer1)  # 使用该定时器时需注意：定时器0-3，每个在同一时间内只能执行一件任务，且多个对象不可使用同一个定时器。
```



> **timer.start(period, mode, callback)**

启动定时器。

* 参数

| 参数     | 类型     | 说明                                                         |
| -------- | -------- | ------------------------------------------------------------ |
| period   | int      | 中断周期，单位毫秒，大于等于1                                |
| mode     | int      | 运行模式<br />Timer.ONE_SHOT  单次模式，定时器只执行一次<br />Timer.PERIODIC    周期模式，循环执行 |
| callback | function | 定时器执行函数                                               |

* 返回值

启动成功返回整型值0，失败返回整型值-1。

* 示例

```python
// 使用该定时器时需注意：定时器0-3，每个在同一时间内只能执行一件任务，且多个对象不可使用同一个定时器。
>>> def fun(args):
        print(“###timer callback function###”)
>>> timer.start(period=1000, mode=timer.PERIODIC, callback=fun)
0
###timer callback function###
###timer callback function###
###timer callback function###
……
```



> **timer.stop()**

关闭定时器。

* 参数

无

* 返回值

成功返回整型值0，失败返回整型值-1。



**Timer使用示例**

```python
'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module timer
@FilePath: example_timer_file.py
'''
import log
import utime
from machine import Timer
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Timer_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
Timer_Log = log.getLogger("Timer")

num = 0
state = 1
# 注：EC100YCN支持定时器Timer0~Timer3
t = Timer(Timer.Timer1)

# 创建一个执行函数，并将timer实例传入
def timer_test(t):
	global num
	global state
	Timer_Log.info('num is %d' % num)
	num += 1
	if num > 10:
		Timer_Log.info('num > 10, timer exit')
		state = 0
		t.stop()   # 结束该定时器实例


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
	【本例程可以屏蔽下面这一行！】
	'''
	# checknet.wait_network_connected()

	t.start(period=1000, mode=t.PERIODIC, callback=timer_test)   # 启动定时器

	while state:
		pass
```



##### ExtInt

类功能：用于配置I/O引脚在发生外部事件时中断。

**常量说明**

| 常量             | 适配平台        | 说明     |
| ---------------- | --------------- | -------- |
| Pin.GPIO1        | EC600S / EC100Y | GPIO1    |
| Pin.GPIO2        | EC600S / EC100Y | GPIO2    |
| Pin.GPIO3        | EC600S / EC100Y | GPIO3    |
| Pin.GPIO4        | EC600S / EC100Y | GPIO4    |
| Pin.GPIO5        | EC600S / EC100Y | GPIO5    |
| Pin.GPIO6        | EC600S / EC100Y | GPIO6    |
| Pin.GPIO7        | EC600S / EC100Y | GPIO7    |
| Pin.GPIO8        | EC600S / EC100Y | GPIO8    |
| Pin.GPIO9        | EC600S / EC100Y | GPIO9    |
| Pin.GPIO10       | EC600S / EC100Y | GPIO10   |
| Pin.GPIO11       | EC600S / EC100Y | GPIO11   |
| Pin.GPIO12       | EC600S / EC100Y | GPIO12   |
| Pin.GPIO13       | EC600S / EC100Y | GPIO13   |
| Pin.GPIO14       | EC600S / EC100Y | GPIO14   |
| Pin.GPIO15       | EC100Y          | GPIO15   |
| Pin.GPIO16       | EC100Y          | GPIO16   |
| Pin.GPIO17       | EC100Y          | GPIO17   |
| Pin.GPIO18       | EC100Y          | GPIO18   |
| Pin.GPIO19       | EC100Y          | GPIO19   |
| Pin.IN           | --              | 输入模式 |
| Pin.OUT          | --              | 输出模式 |
| Pin.PULL_DISABLE | --              | 浮空模式 |
| Pin.PULL_PU      | --              | 上拉模式 |
| Pin.PULL_PD      | --              | 下拉模式 |

**创建ExtInt对象**

> **extint = ExtInt(GPIOn, mode, pull, callback)**

* 参数

| 参数     | 类型 | 说明                                                         |
| :------- | :--- | ------------------------------------------------------------ |
| GPIOn    | int  | 引脚号<br />EC100YCN平台引脚对应关系如下（引脚号为外部引脚编号）：<br />GPIO1 – 引脚号22<br />GPIO2 – 引脚号23<br />GPIO3 – 引脚号38<br />GPIO4 – 引脚号53<br />GPIO5 – 引脚号54<br />GPIO6 – 引脚号104<br />GPIO7 – 引脚号105<br />GPIO8 – 引脚号106<br />GPIO9 – 引脚号107<br />GPIO10 – 引脚号178<br />GPIO11 – 引脚号195<br />GPIO12 – 引脚号196<br />GPIO13 – 引脚号197<br />GPIO14 – 引脚号198<br />GPIO15 – 引脚号199<br />GPIO16 – 引脚号203<br />GPIO17 – 引脚号204<br />GPIO18 – 引脚号214<br />GPIO19 – 引脚号215<br />EC600SCN平台引脚对应关系如下（引脚号为模块外部引脚编号）：<br />GPIO1 – 引脚号10<br />GPIO2 – 引脚号11<br />GPIO3 – 引脚号12<br />GPIO4 – 引脚号13<br />GPIO5 – 引脚号14<br />GPIO6 – 引脚号15<br />GPIO7 – 引脚号16<br />GPIO8 – 引脚号39<br />GPIO9 – 引脚号40<br />GPIO10 – 引脚号48<br />GPIO11 – 引脚号58<br />GPIO12 – 引脚号59<br />GPIO13 – 引脚号60<br />GPIO14 – 引脚号61 |
| mode     | int  | 设置触发方式<br /> IRQ_RISING – 上升沿触发<br /> IRQ_FALLING – 下降沿触发<br /> IRQ_RISING_FALLING – 上升和下降沿触发 |
| pull     | int  | PULL_DISABLE – 浮空模式<br />PULL_PU – 上拉模式 <br />PULL_PD  – 下拉模式 |
| callback | int  | 中断触发回调函数                                             |

* 示例

```python
>>> from machine import ExtInt
>>> def fun(args):
        print(“###interrupt  %d ###” %args)
>>> extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
```



> **extint.enable()**

使能extint对象外部中断，当中断引脚收到上升沿或者下降沿信号时，会调用callback执行 。

* 参数

无

* 返回值

使能成功返回整型值0，使能失败返回整型值-1。



> **extint.disable()**

禁用与extint对象关联的中断 。

* 参数

无

* 返回值

使能成功返回整型值0，使能失败返回整型值-1。



> **extint.line()**

返回引脚映射的行号。

* 参数

无

* 返回值

引脚映射的行号。

* 示例

```python
>>> extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
>>> ext.line()
32
```



##### RTC

类功能：提供获取设置rtc时间方法。

**创建RTC对象**

> **from machine import RTC**
>
> **rtc = RTC()**



> **rtc.datetime([year, month, day, week, hour, minute, second, microsecond])**

设置和获取RTC时间，不带参数时，则用于获取时间，带参数则是设置时间；设置时间的时候，参数week不参于设置，microsecond参数保留，暂未使用，默认是0。

* 参数

| 参数        | 类型 | 说明                                                         |
| ----------- | ---- | ------------------------------------------------------------ |
| year        | int  | 年                                                           |
| month       | int  | 月，范围1~12                                                 |
| day         | int  | 日，范围1~31                                                 |
| week        | int  | 星期，设置时间时，该参数不起作用，保留；获取时间时该参数有效 |
| hour        | int  | 时，范围0~23                                                 |
| minute      | int  | 分，范围0~59                                                 |
| second      | int  | 秒，范围0~59                                                 |

| microsecond | int  | 微秒，保留参数，暂未使用，设置时间时该参数写0即可            |

* 返回值

获取时间时，返回一个元组，包含日期时间，格式如下：

`[year, month, day, week, hour, minute, second, microsecond]`

设置时间时，设置成功返回整型值0，设置失败返回整型值-1 。

* 示例

```python
>>> from machine import RTC
>>> rtc = RTC()
>>> rtc.datetime()
(2020, 9, 11, 5, 15, 43, 23, 0)
>>> rtc.datetime([2020, 3, 12, 1, 12, 12, 12, 0])
0
>>> rtc.datetime()
(2020, 3, 12, 4, 12, 12, 14, 0)
```



##### I2C

类功能：用于设备之间通信的双线协议。

**常量说明**

| 常量              |                   |
| ----------------- | ----------------- |
| I2C.I2C0          | i2c 通路索引号: 0 |
| I2C.I2C1          | i2c 通路索引号: 1 |
| I2C.STANDARD_MODE | 标准模式          |
| I2C.FAST_MODE     | 快速模式          |

**创建I2C对象**

> **from machine import I2C**
>
> **i2c_obj = I2C(I2Cn,  MODE)**

**参数说明**

| 参数 | 类型 | 说明                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| I2Cn | int  | i2c 通路索引号:<br />I2C.I2C0 : 0  （EC100Y）<br />I2C.I2C1 : 1  （EC600S） |
| MODE | int  | i2c 的工作模式:<br />I2C.STANDARD_MODE : 0 标准模式<br />I2C.FAST_MODE ： 1 快速模式 |

- 示例

```python
from machine import I2C

i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # 返回i2c对象
```



> **I2C.read(slaveaddress, addr,addr_len, r_data, datalen, delay)**

从 I2C 总线中读取数据。

**参数说明**

| 参数         | 类型      | 说明                             |
| ------------ | --------- | -------------------------------- |
| slaveaddress | int       | i2c 设备地址                     |
| addr         | int       | i2c 寄存器地址                   |
| addr_len     | int       | 寄存器地址长度                   |
| r_data       | bytearray | 接收数据的字节数组               |
| datalen      | int       | 字节数组的长度                   |
| delay        | int       | 延时，数据转换缓冲时间（单位ms） |

* 返回值

成功返回整型值0，失败返回整型值-1。



> **I2C.write(slaveaddress, addr, addr_len, data, datalen)**

从 I2C 总线中写入数据。

**参数说明**

| 参数         | 类型      | 说明           |
| ------------ | --------- | -------------- |
| slaveaddress | int       | i2c 设备地址   |
| addr         | int       | i2c 寄存器地址 |
| addr_len     | int       | 寄存器地址长度 |
| data         | bytearray | 写入的数据     |
| datalen      | int       | 写入数据的长度 |

* 返回值

成功返回整型值0，失败返回整型值-1。



**使用示例**

需要连接设备使用！

```python
import log
from machine import I2C
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_I2C_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

'''
I2C使用示例
'''

# 设置日志输出级别
log.basicConfig(level=log.INFO)
i2c_log = log.getLogger("I2C")


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
    【本例程可以屏蔽下面这一行！】
    '''
    # checknet.wait_network_connected()

    I2C_SLAVE_ADDR = 0x1B  # i2c 设备地址
    WHO_AM_I = bytearray({0x02, 0})   # i2c 寄存器地址，以buff的方式传入，取第一个值，计算一个值的长度

    data = bytearray({0x12, 0})   # 输入对应指令
    i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # 返回i2c对象
    i2c_obj.write(I2C_SLAVE_ADDR, WHO_AM_I, 1, data, 2) # 写入data

    r_data = bytearray(2)  # 创建长度为2的字节数组接收
    i2c_obj.read(I2C_SLAVE_ADDR, WHO_AM_I, 1, r_data, 2, 0)   # read
    i2c_log.info(r_data[0])
    i2c_log.info(r_data[1])


```



##### SPI

类功能：串行外设接口总线协议。

适配版本：EC100Y(V0009)及以上；EC600S(V0002)及以上。

**创建SPI对象**

> **spi_obj = SPI(port, mode, clk)**

**参数说明**

| 参数 | 类型 | 说明                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| port | int  | 通道选择[0,1]                                                |
| mode | int  | SPI 的工作模式(模式0最常用):<br />时钟极性CPOL: 即SPI空闲时，时钟信号SCLK的电平（0:空闲时低电平; 1:空闲时高电平）<br /> 0 : CPOL=0, CPHA=0<br /> 1 : CPOL=0, CPHA=1<br /> 2:  CPOL=1, CPHA=0<br /> 3:  CPOL=1, CPHA=1 |
| clk  | int  | 时钟频率<br /> 0 : 812.5kHz<br /> 1 : 1.625MHz<br /> 2 : 3.25MHz<br /> 3 : 6.5MHz<br /> 4 : 13MHz<br /> 5 :  26MH |

- 示例

```python
from machine import SPI

spi_obj = SPI(1, 0, 1)  # 返回spi对象
```



> **SPI.write(data, datalen)**

写入数据。

**参数说明**

| 参数    | 类型  | 说明           |
| ------- | ----- | -------------- |
| data    | bytes | 写入的数据     |
| datalen | int   | 写入的数据长度 |

* 返回值

失败返回整型值-1。



> **SPI.read(recv_data, datalen)**

读取数据。

**参数说明**

| 参数      | 类型      | 说明               |
| --------- | --------- | ------------------ |
| recv_data | bytearray | 接收读取数据的数组 |
| datalen   | int       | 读取数据的长度     |

* 返回值

失败返回整型值-1。



> **SPI.write_read(r_data，data, datalen)**

写入和读取数据。

**参数说明**

| 参数    | 类型      | 说明               |
| ------- | --------- | ------------------ |
| r_data  | bytearray | 接收读取数据的数组 |
| data    | bytes     | 发送的数据         |
| datalen | int       | 读取数据的长度     |

* 返回值

失败返回整型值-1。

**使用示例**

需要配合外设使用！

```python
import log
from machine import SPI
import utime
import checkNet

'''
SPI使用示例
适配版本：EC100Y(V0009)及以上；EC600S(V0002)及以上
'''

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_SPI_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

spi_obj = SPI(0, 0, 1)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
spi_log = log.getLogger("SPI")


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
    【本例程可以屏蔽下面这一行！】
    '''
    # checknet.wait_network_connected()

    r_data = bytearray(5)  # 创建接收数据的buff
    data = b"world"  # 写入测试数据

    ret = spi_obj.write_read(r_data, data, 5)  # 写入数据并接收
    spi_log.info(r_data)

```



##### LCD

类功能：该模块提供对LCD显示屏的控制

适配版本：EC100Y(V0009)及以上；EC600S(V0002)及以上。

**创建LCD对象**

> **lcd = LCD() **

**参数说明**

无

- 示例

```python
from machine import LCD 
lcd = LCD()   # 创建lcd对象
```



> **lcd.lcd_init(lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness)  **

初始化LCD

- 参数

| 参数               | 类型      | 说明                                                         |
| ------------------ | --------- | ------------------------------------------------------------ |
| lcd_init_data      | bytearray | 传入 LCD 的配置命令                                          |
| lcd_width          | int       | LCD 屏幕的宽度。宽度不超过 500                               |
| lcd_hight          | int       | LCD 屏幕的高度。高度不超过 500                               |
| lcd_clk            | int       | LCD SPI 时钟。SPI 时钟为 6.5K/13K/26K/52K                    |
| data_line          | int       | 数据线数。参数值为 1 和 2。                                  |
| line_num           | int       | 线的数量。参数值为 3 和 4。                                  |
| lcd_type           | int       | 屏幕类型。0：rgb；1：fstn                                    |
| lcd_invalid        | bytearray | 传入LCD 区域设置的配置命令                                   |
| lcd_display_on     | bytearray | 传入LCD 屏亮的配置命令                                       |
| lcd_display_off    | bytearray | 传入LCD 屏灭的配置命令                                       |
| lcd_set_brightness | bytearray | 传入LCD屏亮度的配置命令。设置为 None表示由 LCD_BL_K 控制亮度（有些屏幕是由寄存器控制屏幕亮度，有 些是通过 LCD_BL_K 控制屏幕亮度） |

* 返回值

  
   0  	 成功 
  
  -1  	已经初始化 
  
  -2  	参数错误（为空或过大（大于 1000 像素点）） 
  
  -3  	缓存申请失败
  
  -5  	配置参数错误 




> **lcd.lcd_clear(color) **

清除屏幕。

- 参数

| 参数  | 类型   | 说明             |
| ----- | ------ | ---------------- |
| color | 16进制 | 需要刷屏的颜色值 |

* 返回值

成功返回0， 失败返回-1。



> **lcd.lcd_write(color_buffer,start_x,start_y,end_x,end_y) **

区域写屏。 

- 参数

| 参数         | 类型      | 说明               |
| ------------ | --------- | ------------------ |
| Color_buffer | bytearray | 屏幕的颜色值缓存。 |
| start_x      | int       | 起始 x 坐标        |
| start_y      | int       | 起始 y 坐标        |
| end_x        | int       | 结束 x 坐标        |
| end_y        | int       | 结束 y 坐标        |

* 返回值

  0   	成功 

  -1  	屏幕未初始化

  -2  	宽度和高度设置错误 

  -3  	数据缓存为空 



> **lcd. lcd_brightness(level)  **

设置屏幕亮度等级。

- 参数

| 参数  | 类型      | 说明                                                         |
| ----- | --------- | ------------------------------------------------------------ |
| level | bytearray | 亮度等级。此处会调用 lcd.lcd_init()中的 lcd_set_brightness回调。若该参数为 None，亮度调节则由 背光亮度调节引脚来控制 |

* 返回值

成功返回0， 失败返回-1。



> **lcd.lcd_display_on()**

打开屏显 。调用此接口后调用 lcd.lcd_init()中的 lcd_display_on 回调。 

- 参数

无

* 返回值

成功返回0， 失败返回-1。



> **lcd.lcd_display_off()**

关闭屏显 。调用此接口后调用 lcd.lcd_init()中的 lcd_display_off 回调。 

- 参数

无

* 返回值

成功返回0， 失败返回-1。



> **lcd.lcd_write_cmd(cmd_value, cmd_value_len)**

写入命令。

- 参数

| 参数          | 类型   | 说明       |
| ------------- | ------ | ---------- |
| cmd_value     | 16进制 | 命令值     |
| cmd_value_len | int    | 命令值长度 |

* 返回值

成功返回0， 失败返回其他值。



> **lcd.lcd_write_data(data_value, data_value_len)**

写入数据。

- 参数

| 参数           | 类型   | 说明       |
| -------------- | ------ | ---------- |
| data_value     | 16进制 | 数据值     |
| data_value_len | int    | 数据值长度 |

* 返回值

成功返回0， 失败返回其他值。



> **lcd.lcd_show(file_name, start_x,start_y,width,hight)**

采用读文件方式，显示图片。

该文件是由Image2Lcd工具生成的bin文件。若勾选包含图像头文件，则width和hight无需填写

- 参数

| 参数      | 类型   | 说明                                           |
| --------- | ------ | ---------------------------------------------- |
| file_name | 文件名 | 需要显示的图片                                 |
| start_x   | int    | 起始x坐标                                      |
| start_y   | int    | 起始y坐标                                      |
| width     | int    | 图片宽度（若图片文件包含的头信息，则该处不填） |
| hight     | int    | 图片高度（若图片文件包含的头信息，则该处不填） |

* 返回值

成功返回0， 失败返回其他值。



**使用示例**

需要配合LCD屏使用，如下代码以 ili9225 为例！

```python
from machine import LCD 
#一般屏幕设置有两种方式：
#一：分两次写：高八位和低八位
XSTART_H = 0xf0
XSTART_L = 0xf1
YSTART_H = 0xf2
YSTART_L = 0xf3
XEND_H = 0xE0
XEND_L = 0xE1
YEND_H = 0xE2
YEND_L = 0xE3
#二：一次写一个short
XSTART = 0xD0
XEND = 0xD1
YSTART = 0xD2
YEND = 0xD3


init_data = (0,1,0x02, 1,2,0x01,0x00, 0,1,0x01, 1,2,0x01,0x1C, 0,1,0x03, 1,2,0x10,0x30, 0,1,0x08, 1,2,0x08,0x08, 0,1,0x0B, 1,2,0x11,0x00, 0,1,0x0C, 1,2,0x00,0x00, 0,1,0x0F, 1,2,0x14,0x01, 0,1,0x15, 1,2,0x00,0x00, 0,1,0x20, 1,2,0x00,0x00, 0,1,0x21, 1,2,0x00,0x00, 0,1,0x10, 1,2,0x08,0x00, 0,1,0x11, 1,2,0x1F,0x3F, 0,1,0x12, 1,2,0x01,0x21, 0,1,0x13, 1,2,0x00,0x0F, 0,1,0x14, 1,2,0x43,0x49, 0,1,0x30, 1,2,0x00,0x00, 0,1,0x31, 1,2,0x00,0xDB, 0,1,0x32, 1,2,0x00,0x00, 0,1,0x33, 1,2,0x00,0x00, 0,1,0x34, 1,2,0x00,0xDB, 0,1,0x35, 1,2,0x00,0x00, 0,1,0x36, 1,2,0x00,0xAF, 0,1,0x37, 1,2,0x00,0x00, 0,1,0x38, 1,2,0x00,0xDB, 0,1,0x39, 1,2,0x00,0x00, 0,1,0x50, 1,2,0x00,0x01, 0,1,0x51, 1,2,0x20,0x0B, 0,1,0x52, 1,2,0x00,0x00, 0,1,0x53, 1,2,0x04,0x04, 0,1,0x54, 1,2,0x0C,0x0C, 0,1,0x55, 1,2,0x00,0x0C, 0,1,0x56, 1,2,0x01,0x01, 0,1,0x57, 1,2,0x04,0x00, 0,1,0x58, 1,2,0x11,0x08, 0,1,0x59, 1,2,0x05,0x0C, 0,1,0x07, 1,2,0x10,0x17, 0,1,0x22)

display_on_data = (
0,1,0x07,
1,2,0x10,0x17,
)
display_off_data = (
0,1,0x07,
1,2,0x10,0x04,
)
invalid_data = (
    0,1,0x36,
    1,2,XEND,
    0,1,0x37,
    1,2,XSTART,
    0,1,0x38,
    1,2,YEND,
    0,1,0x39,
    1,2,YSTART,
    0,1,0x20,
    1,2,XSTART,
    0,1,0x21,
    1,2,YSTART,
    0,1,0x22,
)

lcd = LCD()
init_list = bytearray(init_data)
display_on_list = bytearray(display_on_data)
display_off_list = bytearray(display_off_data)
invalid_list = bytearray(invalid_data)

    
lcd.lcd_init(init_list, 176,220,13000,1,4,0,invalid_list,display_on_list,display_off_list,None)

Color_buffer =(0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f) 

Color_buffer = bytearray(Color_buffer) 

lcd.lcd_write(Color_buffer,10,10,20,20)
lcd.lcd_clear(0xf800) # 红色

lcd.show("lcd_test.bin",0,0)	#该lcd_test.bin 中包含图像头数据
lcd.show("lcd_test1.bin",0,0,126,220) #该lcd_test1.bin 中没有包含图像头数据
```




##### WDT 

模块功能：APP应用程序发生异常不执行时进行系统重启操作

> ​	**wdt = WDT(period)**

创建软狗对象。

- 参数

| 参数   | 类型 | 说明                       |
| :----- | :--- | -------------------------- |
| period | int  | 设置软狗检测时间，单位(s） |

* 返回值

返回软狗对象



> ​	**wdt.feed()**

喂狗

- 参数

无

* 返回值

无



> ​	**wdt.stop()**

关闭软狗功能

- 参数

无

* 返回值

无



**使用示例**

```PYTHON
'''
@Author: Pawn
@Date: 2020-08-12
@LastEditTime: 2020-08-12 17:06:08
@Description: example for module timer
@FilePath: example_wdt.py
'''

from machine import WDT
from machine import Timer
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_WDT_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

timer1 = Timer(Timer.Timer1)

def feed(t):
    wdt.feed()


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
    【本例程可以屏蔽下面这一行！】
    '''
    # checknet.wait_network_connected()

    wdt = WDT(20)  # 启动看门狗，间隔时长
    timer1.start(period=15000, mode=timer1.PERIODIC, callback=feed)  # 使用定时器喂狗

    # wdt.stop()

```



#### qrcode- 二维码显示

模块功能：根据输入的内容，生成对应的二维码。

> ​	qrcode.show(qrcode_str,magnification,start_x,start_y,Background_color,Foreground_color)

创建wake_lock锁  +++还有放大

- 参数

| 参数             | 类型   | 说明                           |
| :--------------- | :----- | ------------------------------ |
| qrcode_str       | string | 二维码内容                     |
| magnification    | int    | 放大倍数[1,6]                  |
| start_x          | int    | 二维码显示起始x坐标            |
| start_y          | int    | 二维码显示起始y坐标            |
| Background_color | int    | 前景色（不设置即默认为0xffff） |
| Foreground_color | int    | 背景色（不设置即默认为0x0000） |

* 返回值

0：成功

-1：生成二维码失败

-2：放大失败

-3：显示失败



#### pm - 低功耗

模块功能：在无业务处理时使系统进入休眠状态，进入低功耗模式。

> ​	**lpm_fd = pm.create_wakelock(lock_name, name_size)**

创建wake_lock锁

- 参数

| 参数      | 类型   | 说明            |
| :-------- | :----- | --------------- |
| lock_name | string | 自定义lock名    |
| name_size | int    | lock_name的长度 |

* 返回值

成功返回wakelock的标识号，否则返回-1。



> ​	**pm.delete_wakelock(lpm_fd)**

删除wake_lock锁

- 参数

| 参数   | 类型 | 说明                   |
| :----- | :--- | ---------------------- |
| lpm_fd | int  | 需要删除的锁对应标识id |

* 返回值

成功返回0。



> ​	**pm.wakelock_lock(lpm_fd)**

加锁

- 参数

| 参数   | 类型 | 说明                             |
| :----- | :--- | -------------------------------- |
| lpm_fd | int  | 需要执行加锁操作的wakelock标识id |

* 返回值

成功返回0，否则返回-1。



> ​	**pm.wakelock_unlock(lpm_fd)**

释放锁

- 参数

| 参数   | 类型 | 说明                               |
| :----- | :--- | ---------------------------------- |
| lpm_fd | int  | 需要执行释放锁操作的wakelock标识id |

* 返回值

成功返回0，否则返回-1。



> ​	**pm.autosleep(sleep_flag)**

自动休眠模式控制

- 参数

| 参数       | 类型 | 说明                           |
| :--------- | :--- | ------------------------------ |
| sleep_flag | int  | 0，关闭自动休眠；1开启自动休眠 |

* 返回值

成功返回0。



> ​	**pm.get_wakelock_num()**

获取已创建的锁数量

- 参数

无

* 返回值

返回已创建wakelock锁的数量。



**使用示例**

模拟测试，实际开发请根据业务场景选择使用！

```python
import pm
import utime

# 创建wakelock锁
lpm_fd = pm.create_wakelock("test_lock", len("test_lock"))
# 设置自动休眠模式
pm.autosleep(1)

# 模拟测试，实际开发请根据业务场景选择使用
while 1:
    utime.sleep(20)  # 休眠
    res = pm.wakelock_lock(lpm_fd)
    print("ql_lpm_idlelock_lock, g_c1_axi_fd = %d" %lpm_fd)
    print("unlock  sleep")
    utime.sleep(20)
    res = pm.wakelock_unlock(lpm_fd)
    print(res)
    print("ql_lpm_idlelock_unlock, g_c1_axi_fd = %d" % lpm_fd)
    num = pm.get_wakelock_num()  # 获取已创建锁的数量
    print(num)
```



#### ure - 正则

模块功能：提供通过正则表达式匹配数据（ps：此re模块目前支持的操作符较少，部分操作符暂不支持）

**支持操作符：**

| **字符** | **说明**                                       |
| -------- | ---------------------------------------------- |
| ‘.’      | 匹配任意字符                                   |
| ‘[]’     | 匹配字符集合，支持单个字符和一个范围，包括负集 |
| ‘^’      | 匹配字符串的开头。                             |
| ‘$’      | 匹配字符串的结尾。                             |
| ‘?’      | 匹配零个或前面的子模式之一。                   |
| ‘*’      | 匹配零个或多个先前的子模式。                   |
| ‘+’      | 匹配一个或多个先前的子模式。                   |
| ‘??’     | 非贪婪版本的 ? ，匹配0或1                      |
| ‘*?’     | 非贪婪版本的*，匹配零个或多个                  |
| ‘+?’     | 非贪婪版本的+，匹配一个或多个                  |
| ‘\|’     | 匹配该操作符的左侧子模式或右侧子模式。         |
| ‘\d’     | 数字匹配                                       |
| ‘\D’     | 非数字匹配                                     |
| '\s'     | 匹配空格                                       |
| '\S'     | 匹配非空格                                     |
| ‘\w’     | 匹配”单词字符” (仅限ASCII)                     |
| ‘\W’     | 匹配非“单词字符”（仅限ASCII）                  |

**不支持：**

- 重复次数 (`{m,n}`)
- 命名组 (`(?P<name>...)`)
- 非捕获组(`(?:...)`)
- 更高级的断言(`\b`, `\B`)
- 特殊字符转义，如 `\r`, `\n` - 改用Python自己的转义。



> ​	**ure.compile(regex)**

compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

- 参数

| 参数  | 类型   | 说明       |
| :---- | :----- | ---------- |
| regex | string | 正则表达式 |

* 返回值

返回 regex 对象



> ​	**ure.match(regex, string)**

将正则表达式对象 与 string 匹配，匹配通常从字符串的起始位置进行

- 参数

| 参数   | 类型   | 说明                 |
| :----- | :----- | -------------------- |
| regex  | string | 正则表达式           |
| string | string | 需要匹配的字符串数据 |

* 返回值

匹配成功返回一个匹配的对象，否则返回None。



> ​	**ure.search(regex, string)**

re.search 扫描整个字符串并返回第一个成功的匹配。

- 参数

| 参数   | 类型   | 说明                 |
| :----- | :----- | -------------------- |
| regex  | string | 正则表达式           |
| string | string | 需要匹配的字符串数据 |

* 返回值

匹配成功返回一个匹配的对象，否则返回None。



**Match 对象**

匹配由 match() 和 serach 方法返回的对象

> ​	**match.group(index)**

匹配的整个表达式的字符串

- 参数

| 参数  | 类型 | 说明                                                         |
| :---- | :--- | ------------------------------------------------------------ |
| index | int  | 正则表达式中，group()用来提出分组截获的字符串, index=0返回整体，根据编写的正则表达式进行获取，当分组不存在时会抛出异常 |

* 返回值

返回匹配的整个表达式的字符串



> ​	**match.groups()**

匹配的整个表达式的字符串

- 参数

无

* 返回值

返回一个包含该匹配组的所有子字符串的元组。



> ​	**match.start(index)**

返回匹配的子字符串组的起始原始字符串中的索引。

- 参数

| 参数  | 类型 | 说明                                 |
| :---- | :--- | ------------------------------------ |
| index | int  | index 默认为整个组，否则将选择一个组 |

* 返回值

返回匹配的子字符串组的起始原始字符串中的索引。



> ​	**match.end(index)**

返回匹配的子字符串组的结束原始字符串中的索引。

- 参数

| 参数  | 类型 | 说明                                 |
| :---- | :--- | ------------------------------------ |
| index | int  | index 默认为整个组，否则将选择一个组 |

* 返回值

返回匹配的子字符串组的结束原始字符串中的索引。



**使用示例**

```python
import ure

res = '''
$GNRMC,133648.00,A,3149.2969,N,11706.9027,E,0.055,,311020,,,A,V*18
$GNGGA,133648.00,3149.2969,N,11706.9027,E,1,24,1.03,88.9,M,,M,,*6C
$GNGLL,3149.2969,N,11706.9027,E,133648.00,A,A*7A
$GNGSA,A,3,31,26,11,194,27,195,08,09,03,193,04,16,1.41,1.03,0.97,1*31
'''

r = ure.search("GNGGA(.+?)M", res)
print(r.group(0))
```

####  wifiScan

**判断当前平台是否支持 wifiScan**

> **wifiScan.support()**

* 功能：

  判断当前平台是否支持 wifiScan 功能。

* 参数：

  无

* 返回值：

  支持返回True，不支持返回False。

* 示例：

```python 
>>> import wifiScan
>>> wifiScan.support()
True
```



**开启或者关闭 wifiScan 功能**

> **wifiScan.control(option)**

* 功能：

  控制开启或者关闭 wifiScan 功能。

* 参数：

| 参数   | 类型 | 说明                                             |
| ------ | ---- | ------------------------------------------------ |
| option | 整型 | 0 - 关闭 wifiscan 功能<br>1 - 开启 wifiscan 功能 |

* 返回值：

  执行成功返回整型0，失败返回整型-1。

* 示例：

```python
>>> wifiScan.control(1) # 开启 wifiScan 功能
0
>>> wifiScan.control(0) # 关闭 wifiScan 功能
0
```



**获取 wifiScan 的当前状态**

> **wifiScan.getState()**

* 功能：

  获取当前平台 wifiScan 的状态，是开启还是关闭。200U/600U 平台默认关闭，使用wifiscan功能之前应该使用`wifiScan.control(1)` 开启该功能。

* 参数：

  无

* 返回值：

  wifiScan 功能已开启返回 True，功能未开启返回 False。

* 示例：

```python
>>> wifiScan.getState()
True
```



**获取当前 wifiScan 功能配置**

> **wifiScan.getConfig()**

* 功能：

  获取 wifiScan 功能配置参数。

* 参数：

  无

* 返回值：

  成功返回一个元组，失败返回整型 -1，返回元组形式如下：

  `(timeout, round, max_bssid_num, scan_timeout, priority)`

  | 返回值        | 类型 | 说明                                                         |
  | ------------- | ---- | ------------------------------------------------------------ |
  | timeout       | 整型 | 该超时时间参数是上层应用的超时，当触发超时会主动上报已扫描到的热点信息，若在超时前扫描到设置的热点个数或达到底层扫频超时时间会自动上报热点信息。该参数设置范围为4-255秒。 |
  | round         | 整型 | 该参数是wifi扫描轮，达到扫描轮数后，会结束扫描并获取扫描结果。该参数设置范围为1-3轮次。 |
  | max_bssid_num | 整型 | 该参数是wifi扫描热点最大个，若底层扫描热点个数达到设置的最大个数，会结束扫描并获取扫描结果。该参数设置范围为4-30个。 |
  | scan_timeout  | 整型 | 该参数是底层wifi扫描热点超时时间，若底层扫描热点时间达到设置的超时时间，会结束扫描并获取扫描结果。该参数设置范围为1-255秒。 |
  | priority      | 整型 | 该参数是wifi扫描业务优先级设置，0为ps优先，1为wifi优先。ps优先时，当有数据业务发起时会中断wifi扫描。Wifi优先时，当有数据业务发起时，不会建立RRC连接，保障wifi扫描正常执行，扫描结束后才会建立RRC连接。 |

* 示例：

```python
>>> wifiScan.getConfig()
(6, 1, 5, 1, 0)
```



**设置当前 wifiScan 功能配置**

> **wifiScan.setConfig(timeout, round, max_bssid_num, scan_timeout, priority)**

* 功能：

  设置 wifiScan 功能配置参数。

* 参数：

  | 参数          | 类型 | 说明                                                         |
  | ------------- | ---- | ------------------------------------------------------------ |
  | timeout       | 整型 | 该超时时间参数是上层应用的超时，当触发超时会主动上报已扫描到的热点信息，若在超时前扫描到设置的热点个数或达到底层扫频超时时间会自动上报热点信息。该参数设置范围为4-255秒。 |
  | round         | 整型 | 该参数是wifi扫描轮，达到扫描轮数后，会结束扫描并获取扫描结果。该参数设置范围为1-3轮次。 |
  | max_bssid_num | 整型 | 该参数是wifi扫描热点最大个，若底层扫描热点个数达到设置的最大个数，会结束扫描并获取扫描结果。该参数设置范围为4-30个。 |
  | scan_timeout  | 整型 | 该参数是底层wifi扫描热点超时时间，若底层扫描热点时间达到设置的超时时间，会结束扫描并获取扫描结果。该参数设置范围为1-255秒。 |
  | priority      | 整型 | 该参数是wifi扫描业务优先级设置，0为ps优先，1为wifi优先。ps优先时，当有数据业务发起时会中断wifi扫描。Wifi优先时，当有数据业务发起时，不会建立RRC连接，保障wifi扫描正常执行，扫描结束后才会建立RRC连接。 |

* 返回值：

  成功返回整型0，失败返回整型-1。

* 示例：

```python
>>> wifiScan.setConfig(5, 2, 6, 3, 0)
0
```



**注册回调函数**

> **wifiScan.setCallback(usrFun)**

* 功能：

  注册用户回调函数。当用户使用异步接口扫描时，需要注册回调函数，扫描结果通过回调函数返回给用户。

* 参数：

  | 参数   | 类型     | 说明         |
  | ------ | -------- | ------------ |
  | usrFun | function | 用户回调函数 |

* 返回值：

  注册成功返回整型0，失败返回整型-1。

* 示例：

```python
def usr_cb(args):
	print('wifi list:{}'.format(args))
wifiScan.setCallback(usr_cb)
```



**启动 wifiScan 扫描-异步接口**

> **wifiScan.asyncStart()**

* 功能：

  开始 wifiScan 扫描功能，扫描结果通过用户注册的回调函数返回。

* 参数：

  无

* 返回值：

  执行成功返回整型0，失败返回整型-1。

* 示例：

```python
def usr_cb(args):
	print('wifi list:{}'.format(args))
wifiScan.setCallback(usr_cb)

wifiScan.asyncStart()

'''
执行结果：
wifi list:(2, [('F0:B4:29:86:95:C7': -79),('44:00:4D:D5:26:E0', -92)])
'''
```



**启动 wifiScan 扫描-同步接口**

> **wifiScan.start()**

* 功能：

  开始 wifiScan 扫描功能，扫描结束后直接返回扫描结果，由于是同步接口，所以扫描未结束时，程序会阻塞在该接口中，阻塞时间一般在0~2秒。

* 参数：

  无

* 返回值：

  成功返回扫描结果，失败或者错误返回整型-1。成功时返回值形式如下：

  `（wifi_nums, [(mac, rssi), ... , (mac, rssi)]）`

  | 参数      | 类型   | 说明                |
  | --------- | ------ | ------------------- |
  | wifi_nums | 整型   | 搜索到的 wifi 数量  |
  | mac       | 字符串 | 无线接入点的MAC地址 |
  | rssi      | 整型   | 信号强度            |

* 示例：

```python
>>> wifiScan.start()
(2, [('F0:B4:29:86:95:C7': -79),('44:00:4D:D5:26:E0', -92)])
```



