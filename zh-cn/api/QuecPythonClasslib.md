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

##### 拨号

> **dataCall.start(profileIdx, ipType, apn, username, password, authType)**

启动拨号，进行数据链路激活。

* 参数

| 参数       | 参数类型 | 参数说明                                                     |
| ---------- | -------- | ------------------------------------------------------------ |
| profileIdx | int      | PDP索引，ASR平台范围1 - 8[volte版本默认PID最大的一路用来注册IMS，请勿重复操作]，展锐平台范围1 - 7，高通平台1-4[第二路用来注册ims,不建议修改], 一般设置为1，设置其他值可能需要专用apn与密码才能设置成功 |
| ipType     | int      | IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6                         |
| apn        | string   | apn名称，可为空，最大长度不超过63字节(EC200U/EC200A最大长度不超过64字节) |
| username   | string   | apn用户名，可为空，最大长度不超过15字节(EC200U/EC200A最大长度不超过64字节) |
| password   | string   | apn密码，可为空，最大长度不超过15字节(EC200U/EC200A最大长度不超过64字节) |
| authType   | int      | 加密方式，0-不加密，1-PAP，2-CHAP，3-PAP AND CHAP[仅高通平台支持]      |

* 返回值

成功返回整型值0，失败返回整型值-1。

* 注意

  BC25PA不支持此方法。

* 示例 

```python
>>> import dataCall
>>> dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
0
```



##### 用户apn拨号（支持设置多路用户apn）

> **dataCall.startByUserApns(apn_dict=None, filename=None)**

当用户不希望使用默认的开机拨号功能（需要关闭默认的开机自动拨号功能），需要使用自己配置的 apn 信息来拨号上网，又担心只设置一条 apn 万一写错了可能导致拨号失败上不了网，希望能设置多条 apn 信息，这样即使前面一条或几条写错了导致拨号失败，也能自动使用后面的其他 apn 来继续尝试拨号。这种情况下，就可以使用该接口来满足需求；该接口不仅支持设置多路用户 apn 信息，还支持两种方式来存放用户的 apn 信息，第一种是用户直接将自己的 apn 信息保存在字典中直接内置在代码里面；第二种是用户将自己的 apn 信息保存在 json 文件中，文件存放于usr目录或者usr的子目录。

* 参数 

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| apn_dict | 字典     | 存放用户apn信息的字典，注意格式要求，具体见示例              |
| filename | string   | 带文件路径的 json 文件名，该文件用于存放用户apn信息，注意格式要求，具体见示例；关于路径，一定是 "/usr/"开头，比如存放在usr目录下，那就是 “/usr/xxx.json” |

* 返回值

  返回一个元组，包含两个元素，形式如下：

  `(stagecode, subcode)`

  正常返回 (3,1)，其他异常返回说明见下面的返回值说明。

  返回值说明：

| 返回值    | 类型 | 说明                                                         |
| --------- | ---- | ------------------------------------------------------------ |
| stagecode | 整型 | 阶段码，表示该接口进行到哪个阶段。<br>1 - 程序在获取SIM卡状态阶段，因为SIM卡状态异常，返回时的值；<br>2 - 程序在获取注网状态阶段，因为获取注网状态失败或者注网没成功时返回的值；<br>3 - 程序在拨号阶段，返回时的值；<br>用户使用时，stagecode 正常返回值应该是3，如果是前两个值，说明是不正常的。 |
| subcode   | 整型 | 子码，结合 stagecode 的值，来表示该拨号接口在不同阶段的具体状态。<br/>当 stagecode = 1 时：<br/>subcode 表示 SIM卡的状态，范围[0, 21]，每个值的详细说明，请参考：[https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=sim-sim%e5%8d%a1](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=sim-sim卡) <br/>中 sim.getStatus() 接口的返回值说明。<br/><br/>当 stagecode = 2 时：<br/>subcode 表示注网状态，范围[0, 11]，每个值的详细说明，请参考：[https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=net-%e7%bd%91%e7%bb%9c%e7%9b%b8%e5%85%b3%e5%8a%9f%e8%83%bd](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=net-网络相关功能)    中的 net.getState() 接口的返回值说明。<br/>subcode = -1，表示获取注网状态失败；<br/>其他值参考上面链接中对应接口说明。<br/>如果模块注网成功，就会进入 stagecode = 3 的阶段，不会在stagecode = 2 的阶段返回。<br/><br>当 stagecode = 3 时：<br/>subcode = -1，表示尝试了所有的用户apn进行拨号，都拨号失败；<br>subcode = 0，表示模块在使用用户apn拨号之前，就已经拨号成功，此时可能有如下3种情况：<br>（1）用户没有关闭默认的开机自动拨号功能；<br>（2）用户在开机后自己调用相关接口拨号成功了；<br/>（3）开机后，用户已经执行过 startByUserApns() 接口拨号成功，然后再次执行该接口；<br>subcode = 1，表示使用用户的apn拨号成功。 |

* 注意

  用户apn既可以保存在字典中内置到代码里面，也可以保存到 json文件中，下面说明apn信息的保存格式：

  1、字典中apn信息保存格式说明

  （1）必须是字典的格式，即使只有一路apn相关信息，也要写成 

  {"key":  {"profileIdx": x, "ipType": x, "apn": "xxx", "username": "xxx", "password": "xxx", "authType": x}}

  （2）每一条apn信息中profileIdx、ipType、apn、username、password以及authType这几个成员都必不可少，这些参数参考dataCall.start()接口的参数说明；

  （3）由于字典是无序的结构，所以取apn信息时并不是哪条apn写在前就先取出哪个，这个是随机的；

  示例：

  ```python
  apn_infos = {
      "1": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "111111-apn", 
          "username": "111111-user", 
          "password": "111111-pwd", 
          "authType": 0
      },
      "2": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "222222-apn", 
          "username": "222222-user", 
          "password": "222222-pwd", 
          "authType": 0
      },
      "3": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "333333-apn", 
          "username": "333333-user", 
          "password": "333333-pwd", 
          "authType": 0
      }
  }
  
  ```

  2、json文件中apn信息的保存格式说明

  （1）必须是字典的格式，即使只有一路apn相关信息，也要写成 

  {"key":  {"profileIdx": x, "ipType": x, "apn": "xxx", "username": "xxx", "password": "xxx", "authType": x}}

  （2）每一条apn信息中profileIdx、ipType、apn、username、password以及authType这几个成员都必不可少，这些参数参考dataCall.start()接口的参数说明；

  ```json
  {
      "1": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "111111-apn", 
          "username": "111111-user", 
          "password": "111111-pwd", 
          "authType": 0
      },
      "2": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "222222-apn", 
          "username": "222222-user", 
          "password": "222222-pwd", 
          "authType": 0
      },
      "3": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "333333-apn", 
          "username": "333333-user", 
          "password": "333333-pwd", 
          "authType": 0
      }
  }
  ```

  3、apn信息这两种保存方式，根据用户需要，只能同时选择其中一种，并且也必须选择其中一种；

  4、由于该接口主要用于替代默认的开机拨号功能，如果用户选择使用该接口功能，那么就需要在用户脚本中首先执行该接口，等该接口返回成功后，说明拨号联网已经成功，然后再去进行其他网络业务的操作。

示例

```python
import dataCall


PROJECT_NAME = "QuecPython_DataCall_example"
PROJECT_VERSION = "1.0.0"


"""
方式一：将apn信息保存在代码中
"""
apn_infos = {
    "1": {
        "profileIdx": 1,
        "ipType": 0,
        "apn": "111111",
        "username": "111111",
        "password": "111111",
        "authType": 0
    },
    "2": {
        "profileIdx": 1,
        "ipType": 0,
        "apn": "222222",
        "username": "222222",
        "password": "222222",
        "authType": 0
    },
    "3": {
        "profileIdx": 1,
        "ipType": 0,
        "apn": "333333",
        "username": "333333",
        "password": "333333",
        "authType": 0
    }
}

if __name__ == '__main__':
    stagecode, subcode = dataCall.startByUserApns(apn_dict=apn_infos)
    if stagecode == 3:
        if subcode == 1:
            print('拨号已经成功')
        elif subcode == 0:
            print('当前已经拨号过了，请确认是否关闭了开机自动拨号或者是首次调用该接口等')
        else:
            print('已经尝试了所有的apn，都拨号失败')
    elif stagecode == 1:
        if subcode == 0:
            print('请确认是否插入SIM卡,或者卡槽是否松动')
        else:
            print('SIM 卡状态异常(状态值：{})，请确认是否欠费等'.format(subcode))
    else:
        if subcode == -1:
            print('获取注网状态失败了')
        else:
            print('设备注网异常，注网状态值：{}'.format(subcode))

# =======================================================================================
"""
方式二：将apn信息保存在json文件中
"""
apn_file_path = '/usr/apns.json'

if __name__ == '__main__':
    stagecode, subcode = dataCall.startByUserApns(filename=apn_file_path)
    if stagecode == 3:
        if subcode == 1:
            print('拨号已经成功')
        elif subcode == 0:
            print('当前已经拨号过了，请确认是否关闭了开机自动拨号或者是首次调用该接口等')
        else:
            print('已经尝试了所有的apn，都拨号失败')
    elif stagecode == 1:
        if subcode == 0:
            print('请确认是否插入SIM卡,或者卡槽是否松动')
        else:
            print('SIM 卡状态异常(状态值：{})，请确认是否欠费等'.format(subcode))
    else:
        if subcode == -1:
            print('获取注网状态失败了')
        else:
            print('设备注网异常，注网状态值：{}'.format(subcode))
```



##### 开启或关闭开机自动拨号（重启生效）

> **dataCall.poweronAutoDatacall(enable)**

用于关闭或者开启开机自动拨号功能，重启后生效。开机自动拨号默认就是开启的。

* 参数 

| 参数   | 参数类型 | 参数说明                                             |
| ------ | -------- | ---------------------------------------------------- |
| enable | int      | 0 - 关闭开机自动拨号功能<br>1 - 开启开机自动拨号功能 |

* 返回值

  无

* 注意

  该接口仅适用于平时的开发调试，因为该接口设置后需要重启才能生效；如果用户在量产中，希望关闭模组自带的开机自动拨号功能，可采取如下方案：

  步骤1：在自己的电脑上创建一个名为 system_config.json 的文件；

  步骤2：将如下内容复制到创建的 system_config.json 文件中保存；

  ```json
  {"replFlag": 0, "datacallFlag": 0}
  ```

  参数说明：

  ​	replFlag - 开启还是关闭交互功能；详情请参考官方Wiki文档——QuecPython 第三方库——system 环境配置 部分的说明；

  ​	datacallFlag - 开启还是关闭开机自动拨号功能，0表示关闭，1表示开启；

  步骤3：利用官方开发调试工具QPYCom，将 system_config.json 文件合并到固件中，必须是在模块的usr目录，就像合并main.py一样操作即可；

  步骤4：将上一步中合并成功的固件下载到模组中即可，模组开机时会自动检测 system_config.json 文件的配置。



##### 配置用户APN

> **dataCall.setApn(profileIdx, ipType, apn, username, password, authType，flag=0)**

用户apn信息配置接口，用户调用该接口后，会在用户分区目录下创建user_apn.json文件，用于保存用户apn信息，重启后则使用用户配置的apn来拨号。

* 参数

| 参数       | 参数类型 | 参数说明                                                     |
| ---------- | -------- | ------------------------------------------------------------ |
| profileIdx | int      | PDP索引，ASR平台范围1-8，展锐平台范围1-7，一般设置为1，设置其他值可能需要专用apn与密码才能设置成功 |
| ipType     | int      | IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6                         |
| apn        | string   | apn名称，可为空，最大长度不超过63字节(EC200U/EC200A最大长度不超过64字节)|
| username   | string   | apn用户名，可为空，最大长度不超过15字节(EC200U/EC200A最大长度不超过64字节)|
| password   | string   | apn密码，可为空，最大长度不超过15字节(EC200U/EC200A最大长度不超过64字节)|
| authType   | int      | 加密方式，0-不加密，1-PAP，2-CHAP，3-PAP AND CHAP(仅高通平台支持加密方式3) |
| flag       | int      | 可选参数，默认为0，表示仅创建user_apn.json文件，用于保存用户apn信息；为1时，表示创建user_apn.json文件保存用户apn信息之后，还会使用该apn信息立即进行一次拨号；不管该参数是0还是1，都不会影响重启时使用用户设置的apn进行开机拨号。 |

* 返回值

  成功返回整型值0，失败返回整型值-1。

* 注意

  BC25PA不支持此方法。

* 示例

```python
>>> import dataCall
>>> dataCall.setApn(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
0
```



##### 配置用户DNS

> **dataCall.setDnsserver(profileIdx, sim_id, priDns, secDns)**

用户自定义DNS服务器信息配置接口，用户调用该接口后，可以将默认基站分配的DNS服务器改为自定义设置的服务器，可通过获取拨号信息查询当前使用的DNS服务器。

* 参数

| 参数       | 参数类型 | 参数说明                                                     |
| ---------- | -------- | ------------------------------------------------------------ |
| profileIdx | int      | PDP索引，ASR平台范围1-8，展锐平台范围1-7，一般设置为1，设置其他值可能需要专用apn与密码才能设置成功 |
| sim_id     | int      | simid, 范围：0 or 1 ，默认为0，目前仅支持0                   |
| priDns     | string   | 需要设置的自定义DNS服务器                                    |
| secDns     | string   | 需要设置的自定义DNS服务器                                    |

* 返回值

  成功返回整型值0，失败返回整型值-1。

* 注意

  当前仅ASR/Unisoc/ASR_1803s平台支持该功能。

  更改DNS服务器后，域名解析时，将同步使用设置的DNS服务器。

* 示例

```python
>>> import dataCall
>>> dataCall.setDnsserver(1, 0, "8.8.8.8", "114.114.114.114")
0
```



##### 获取用户APN

> **dataCall.getApn(simid, profileIdx)**

获取用户APN，当只有一个参数simid时，获取的是默认承载的APN，如果用户指定了profileIdx参数，获取的是对应 profileIdx 的APN。

* 参数

| 参数       | 参数类型 | 参数说明                                           |
| ---------- | -------- | -------------------------------------------------- |
| simid      | int      | simid，范围：0/1；目前仅支持0                      |
| profileIdx | int      | 可选参数，PDP索引，ASR平台范围1-8，展锐平台范围1-7 |

* 返回值

  成功返回相应APN，失败返回整型值-1。

* 注意

  仅展锐和ASR平台支持该接口。

* 示例

```python
>>> import dataCall
>>> dataCall.getApn(0)
'cmnet'

>>> dataCall.getApn(0,2)
'hhhnet'
```



##### 注册回调函数

> **dataCall.setCallback(usrFun)**

注册用户回调函数，当网络状态发生变化，比如断线、上线时，会通过该回调函数通知用户。

* 参数

| 参数   | 参数类型 | 参数说明                     |
| ------ | -------- | ---------------------------- |
| usrFun | function | 用户回调函数，函数形式见示例 |

* 返回值

  注册失败返回整型-1，成功返回整型0。

* 注意

  BC25PA不支持此方法。

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



##### 获取拨号信息

> **dataCall.getInfo(profileIdx, ipType)**

获取数据拨号信息，包括连接状态、IP地址、DNS等。

* 参数

| 参数       | 参数类型 | 参数说明                                 |
| ---------- | -------- | ---------------------------------------- |
| profileIdx | int      | PDP索引，ASR平台范围1-8，展锐平台范围1-7 |
| ipType     | int      | IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6     |

* 返回值

  错误返回整型-1，成功返回拨号信息，返回格式根据ipType的不同而有所区别：
  ipType =0，返回值格式如下：

  `(profileIdx, ipType, [nwState, reconnect, ipv4Addr, priDns, secDns])`

  `profileIdx`：PDP索引，ASR平台范围1-8，展锐平台范围1-7

  `ipType`：IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6

  `nwState`：拨号结果，0-失败，1-成功

  `reconnect`：重拨标志

  `ipv4Addr`：ipv4地址，string类型

  `priDns`：dns信息，string类型

  `secDns`：dns信息，string类型

  ipType =1，返回值格式如下：

  `(profileIdx, ipType, [nwState, reconnect, ipv6Addr, priDns, secDns])`

  `profileIdx`：PDP索引，ASR平台范围1-8，展锐平台范围1-7

  `ipType`：IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6

  `nwState`：拨号结果，0-失败，1-成功

  `reconnect`：重拨标志

  `ipv6Addr`：ipv6地址，string类型

  `priDns`：dns信息，string类型

  `secDns`：dns信息，string类型

  ipType =2，返回值格式如下：

  `(profileIdx, ipType, [nwState, reconnect, ipv4Addr, priDns, secDns], [nwState, reconnect, ipv6Addr, priDns, secDns])`

* 示例

```python
>>> import dataCall
>>> dataCall.getInfo(1, 0)
(1, 0, [1, 0, '10.91.44.177', '58.242.2.2', '218.104.78.2'])
```

注：返回值 `(1, 0, [0, 0, '0.0.0.0', '0.0.0.0', '0.0.0.0'])` 表示当前没有拨号或者拨号没有成功。

##### 使用示例

```python
import dataCall
import net
import utime
import checkNet

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
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
    	checknet.poweron_print_once()
   
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

注意：当前仅EC600S/EC600N/EC800N/EC200U/EC600U平台支持该功能。

##### 获取坐标

> **cellLocator.getLocation(serverAddr, port, token, timeout, profileIdx)**

获取基站坐标信息。

* 参数

| 参数       | 参数类型 | 参数说明                                                     |
| ---------- | -------- | ------------------------------------------------------------ |
| serverAddr | string   | 服务器域名，长度必须小于255 bytes，目前仅支持 “www.queclocator.com” |
| port       | int      | 服务器端口，目前仅支持 80 端口                               |
| token      | string   | 密钥，16位字符组成，需要申请                                 |
| timeout    | int      | 设置超时时间，范围1-300s，默认300s                           |
| profileIdx | int      | PDP索引，ASR平台范围1-8，展锐平台范围1-7                     |

* 返回值

成功返回经纬度坐标信息，单位度，返回格式：`(longtitude, latitude, accuracy)`，`(0.0, 0.0, 0)`表示未获取到有效坐标信息；

`longtitude` ： 经度

`latitude` ：纬度

`accuracy` ：精确度，单位米

失败返回错误码说明如下：

-1 – 初始化失败

-2 – 服务器地址过长（超过255字节）

-3 – 密钥长度错误，必须为16字节

-4 – 超时时长超出范围，支持的范围（1 ~ 300）s

-5 – 指定的PDP网络未连接，请确认PDP是否正确

-6 – 获取坐标出错

* 示例

```python
>>> import cellLocator
>>> cellLocator.getLocation("www.queclocator.com", 80, "xxxxxxxxxxxxxxxx", 8, 1)
(117.1138, 31.82279, 550)
# 上面使用的密钥"xxxxxxxxxxxxxxxx"指代token，具体需要向移远申请
```



#### wifilocator - wifi定位

模块功能：提供WIFI定位接口，获取坐标信息。

注意：当前仅EC600S/EC600N/EC800N/EC200U/EC600U平台支持该功能。

##### 设置密钥

> **wifilocator(token)**

配置wifi定位套件token信息

* 参数

| 参数  | 参数类型 | 参数说明                     |
| ----- | -------- | ---------------------------- |
| token | string   | 密钥，16位字符组成，需要申请 |

* 返回值

成功返回WIFI定位对象。



##### 获取坐标

> **wifilocator.getwifilocator()**

获取坐标信息。

* 参数

  无

* 返回值

  成功返回度格式经纬度坐标信息，返回格式：`(longtitude, latitude, accuracy)`；

  `longtitude` ： 经度

  `latitude` ：纬度

  `accuracy` ：精确度，单位米

  失败返回错误码说明如下：

  -1 – 当前网络异常，请确认拨号是否正常

  -2 – 密钥长度错误，必须为16字节

  -3 – 获取坐标出错

* 示例

```python
>>> from wifilocator import wifilocator
>>> wifilocator = wifilocator("xxxxxxxxxxxxxxxx")
>>> wifilocator.getwifilocator()
(117.1152877807617, 31.82142066955567, 100)
# 上面使用的密钥"xxxxxxxxxxxxxxxx"指代token，具体需要向移远申请
```



#### atcmd - 发送AT指令

模块功能：提供发送AT指令接口。

#### 发送AT指令接口

> **atcmd.sendSync(atcmd,resp,include_str,timeout)**

*参数

|  参数   | 参数类型 | 参数说明                                      |
|  ----   | -------- | --------------------------------------------- |
| atcmd   |  string  | 需要发送的AT指令，必须包含‘\r\n’              |
| resp    |  string  | output param,获取AT指令返回的字符串内容       |
| include_str | string | 关键字                                      |
| timeout | int      | 超时时间，单位/秒                             |

* 返回值

成功返回0，失败返回error list，如下：

typedef enum HELIOS_AT_RESP_STATUS_ENUM{
	HELIOS_AT_RESP_OK = 0,
	HELIOS_AT_RESP_ERROR,
	HELIOS_AT_RESP_CME_ERROR,
	HELIOS_AT_RESP_CMS_ERROR,
	HELIOS_AT_RESP_INVALID_PARAM,
	HELIOS_AT_RESP_TIME_OUT,
	HELIOS_AT_RESP_SYS_ERROR,
}HELIOS_AT_RESP_STATUS_E;

* 示例

```python
>>> import atcmd
>>> resp=bytearray(50)
>>> atcmd.sendSync('at+cpin?\r\n',resp,'',20)
0
>>> print(resp)
bytearray(b'\r\n+CPIN: READY\r\n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

atcmd.sendSync('at+cpin\r\n',resp,'',20)
1
>>> print(resp)
bytearray(b'\r\nERROR\r\n\n
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
```



#### sim - SIM卡

模块功能：提供sim卡操作相关API，如查询sim卡状态、iccid、imsi等。

注意：能成功获取IMSI、ICCID、电话号码的前提是SIM卡状态为1，可通过sim.getStatus()查询。

##### 通用SIM访问接口

> **sim.genericAccess(simId, cmd)**

将命令APDU通过modem传递给SIM卡，然会返回响应APDU。

注意：当前仅ASR-1603平台支持。

* 参数

| 参数  | 参数类型 | 参数说明                                                     |
| ----- | -------- | ------------------------------------------------------------ |
| simId | int      | sim id, 范围：0 or 1 ，目前仅支持0                           |
| cmd   | string   | command passed on by the MT to the SIM in the format as described in GSM 51.011 |

* 返回值

  成功返回（length，响应APDU），失败返回整型-1。

* 示例

```python
>>> sim.genericAccess(0,'80F2000016')
(48, '623E8202782183027FF08410A0000000871002FF86FF9000')
>>>
```



##### 获取IMSI

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



##### 获取ICCID

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



##### 获取电话号码

> **sim.getPhoneNumber()**

获取sim卡的电话号码。

* 参数

  无

* 返回值

  成功返回string类型的phone number，失败返回整型-1。

* 注意

  BC25PA不支持此方法。

* 示例

```python
>>> sim.getPhoneNumber()
'+8618166328752'
```



##### 获取SIM卡状态

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



##### 开启PIN码验证

> **sim.enablePin(pin)**

启用sim卡PIN码验证，开启后需要输入正确的PIN验证成功后，sim卡才能正常使用。只有3次输入PIN码机会，3次都错误，sim卡被锁定，需要PUK来解锁。

* 参数

| 参数 | 参数类型 | 参数说明                                      |
| ---- | -------- | --------------------------------------------- |
| pin  | string   | PIN码，一般默认是‘1234’，最大长度不超过15字节 |

* 返回值

  成功返回整型0，失败返回整型-1。

* 注意

  BC25PA平台PIN密码最大支持八位。

* 示例

```python
>>> sim.enablePin("1234")
0
```



##### 取消PIN码验证

> **sim.disablePin(pin)**

关闭sim卡PIN码验证。

* 参数

| 参数 | 参数类型 | 参数说明                                      |
| ---- | -------- | --------------------------------------------- |
| pin  | string   | PIN码，一般默认是‘1234’，最大长度不超过15字节 |

* 返回值

  成功返回整型0，失败返回整型-1。

* 注意

  BC25PA平台PIN密码最大支持八位。

* 示例

```python
>>> sim.disablePin("1234")
0
```



##### PIN码验证

> **sim.verifyPin(pin)**

sim卡PIN码验证。需要在调用sim.enablePin(pin)成功之后，才能进行验证，验证成功后，sim卡才能正常使用。

* 参数

| 参数 | 参数类型 | 参数说明                                      |
| ---- | -------- | --------------------------------------------- |
| pin  | string   | PIN码，一般默认是‘1234’，最大长度不超过15字节 |

* 返回值

  验证成功返回整型0，验证失败返回整型-1。

* 注意

  BC25PA平台PIN密码最大支持八位。

* 示例

```python
>>> sim.verifyPin("1234")
0
```



##### SIM卡解锁

> **sim.unblockPin(puk, newPin)**

sim卡解锁。当多次错误输入 PIN/PIN2 码后，SIM 卡状态为请求 PUK/PUK2 时，输入 PUK/PUK2 码和新的 PIN/PIN2 码进行解锁，puk码输入10次错误，SIM卡将被永久锁定自动报废。

* 参数

| 参数   | 参数类型 | 参数说明                                 |
| ------ | -------- | ---------------------------------------- |
| puk    | string   | PUK码，长度8位数字，最大长度不超过15字节 |
| newPin | string   | 新PIN码，最大长度不超过15字节            |

* 返回值

  解锁成功返回整型0，解锁失败返回整型-1。

* 注意

  BC25PA平台PIN密码最大支持八位。

* 示例

```python
>>> sim.unblockPin("12345678", "0000")
0
```



##### 更改SIM卡PIN码

> **sim.changePin(oldPin, newPin)**

更改sim卡PIN码。

* 参数

| 参数   | 参数类型 | 参数说明                        |
| ------ | -------- | ------------------------------- |
| oldPin | string   | 旧的PIN码，最大长度不超过15字节 |
| newPin | string   | 新的PIN码，最大长度不超过15字节 |

* 返回值

  更改成功返回整型0，更改失败返回整型-1。

* 注意

  BC25PA平台PIN密码最大支持八位。

* 示例

```python
>>> sim.changePin("1234", "4321")
0
```



##### 读电话簿

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

* 注意

  BC25PA平台不支持此方法。

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



##### 写电话簿

> **sim. writePhonebook(storage, index, username, number)**

写入一条电话号码记录。

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| storage  | int      | 需要读取电话号码记录的电话本存储位置，可选参数如下：<br/>0 – DC，1 – EN，2 – FD，3 – LD，4 – MC，5 – ME，6 – MT，7 – ON，<br/>8 – RC，9 – SM，10 – AP，11 – MBDN，12 – MN，13 – SDN，14 – ICI，15 - OCI |
| index    | int      | 需要写入电话号码记录的在电话簿中的编号，范围1 ~ 500            |
| username | string   | 电话号码的用户名，长度范围不超过30字节，暂不支持中文名       |
| number   | string   | 电话号码，最大长度不超过20字节                               |

* 返回值

  写入成功返回整型0，写入失败返回整型-1。

* 注意

  BC25PA平台不支持此方法。

示例

```python
>>> sim.writePhonebook(9, 1, 'Tom', '18144786859')
0
```



##### 热插拔注册监听回调函数

> **sim.setCallback(usrFun)**

注册监听回调函数。响应SIM卡热插拔。

(该函数只有在SIM卡热插拔的宏打开的情况下才会存在，一般默认打开)

* 参数

| 参数   | 参数类型 | 参数说明                               |
| ------ | -------- | -------------------------------------- |
| usrFun | function | 监听回调函数，回调具体形式及用法见示例 |

* 返回值

  注册成功返回整型0，失败返回整型-1。

* 注意

  BC25PA平台不支持此方法。

* 示例

```python
import sim

def cb(args):
    simstates = args
    print('sim states:{}'.format(simstates))
    
sim.setCallback(cb)
```



##### SIM卡热插拔开关

> **sim.setSimDet(switch, triggerLevel)**

设置SIM卡热插拔相关配置。

* 参数

| 参数         | 参数类型 | 参数说明                                   |
| ------------ | -------- | ------------------------------------------ |
| switch       | int      | 开启或者关闭SIM卡热插拔功能，0:关闭 1:打开 |
| triggerLevel | int      | 高低电平配置(0/1)                          |

* 返回值

  设置成功返回整型0，设置失败返回整型-1。

* 注意

  BC25PA平台不支持此方法。

* 示例 

```python
>>> sim.setSimDet(1, 0)
0
```



##### 获取SIM卡热插拔配置

> **sim.getSimDet()**

获取SIM卡热插拔相关配置。

* 参数

  无

* 返回值

  获取失败返回整型-1，成功返回一个元组，格式如下：

  `(detenable, insertlevel)`

  返回值参数说明：

  `detenable` - 开启或者关闭SIM卡热插拔功能，0:关闭 1:打开

  `insertlevel` – 高低电平配置(0/1)

* 注意

  BC25PA平台不支持此方法。

* 示例

```python
>>> sim.getSimDet()
(1, 0)
```



##### 获取当前卡的SimId

> **sim.getCurSimid()**

获取当前卡的SimId。（仅1606平台支持）

* 参数

  无

* 返回值

  获取成功，返回当前simid(0:卡1,1:卡2)
  
  获取失败，返回整形-1

* 示例

```python
>>> sim.getCurSimid() //获取当前卡，当前是卡1
0
```



##### 切卡接口

> **sim.switchCard(simid)**

sim卡切卡接口。（仅1606平台支持）

* 参数

  | 参数   | 参数类型 | 参数说明                        |
  | ------ | -------- | ------------------------------- |
  | simid  | int      | 0:卡1  1:卡2                    |

* 返回值

  切卡动作发起成功返回整形0，切换动作发起失败返回整形-1

* 示例

```python
>>> sim.getCurSimid() //获取当前卡，当前是卡1
0
>>> sim.switchCard(1) //切到卡2
0
>>> sim.getCurSimid() //获取当前卡，成功切到卡2
1
```



##### 注册监听SIM卡切卡状态回调函数

> **sim.setSwitchcardCallback(usrFun)**

注册监听回调函数。响应SIM卡切卡动作。（仅1606平台支持）

*注意

不是所有的切卡失败都会通过回调返回：
1、目标卡不存在或者目标卡状态异常
2、目标卡是当前卡
以上情况切卡接口直接返回-1，不会走到实际切卡的流程，也就不会触发回调

如果满足切卡条件，切卡接口返回0，底层建立task走切卡流程，这个时候切卡失败或者成功，会通过callback返回

* 参数

| 参数   | 参数类型 | 参数说明                               |
| ------ | -------- | -------------------------------------- |
| usrFun | function | 监听回调函数，回调具体形式及用法见示例 |

* 返回值

  注册成功返回整型0，失败返回整型-1。

* 示例

```python

//切卡状态枚举值，目前给到python侧的数据只有：
HELIOS_SIM_SWITCH_CURRSIM_PSDC_UP（切卡成功:7）
HELIOS_SIM_SWITCH_ERROR（切卡失败:8）

typedef enum
{
	HELIOS_SIM_SWITCH_INIT = 0,
	HELIOS_SIM_SWITCH_START,
	HELIOS_SIM_SWITCH_PRESIM_PDP_DOWN,
	HELIOS_SIM_SWITCH_PRESIM_IMS_DOWN,
	HELIOS_SIM_SWITCH_PRESIM_PSDC_DOWN,
	HELIOS_SIM_SWITCH_CURRSIM_PDP_UP,
    HELIOS_SIM_SWITCH_PRESIM_IMS_UP,
	HELIOS_SIM_SWITCH_CURRSIM_PSDC_UP,
	HELIOS_SIM_SWITCH_ERROR
}HELIOS_SIM_SWITCH_STATE;

import sim

def cb(args):
    switchcard_state = args
    print('sim switchcard states:{}'.format(switchcard_state))
    
sim.setSwitchcardCallback(cb)
```



#### voiceCall - 电话功能

模块功能：该模块提供电话功能相关接口。

说明：4G only的版本必须打开volte才能正常使用电话功能。

注意：BC25PA平台不支持此功能。

##### 设置自动应答时间

> **voiceCall.setAutoAnswer(seconds)**

设置自动应答时间。

* 参数 

| 参数    | 参数类型 | 参数说明                         |
| ------- | -------- | -------------------------------- |
| seconds | int      | 自动应答时间，单位/s 范围：0-255 |

* 返回值

  成功返回整型0，失败返回整型-1。

* 示例

```python
>>> import voiceCall
>>> voiceCall.setAutoAnswer(5)
0
```



##### 拨打电话

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



##### 接听电话

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



##### 挂断电话

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



##### 设置来电自动挂断

> **voiceCall.setAutoCancel(enable)**

设置来电自动挂断（仅1803S平台支持该接口）。

* 参数 

| 参数        | 参数类型 | 参数说明                                                     |
| ----------- | -------- | ------------------------------------------------------------ |
| enable      | int      | 开启或者关闭来电自动挂断功能，1：开启，0：关闭               |

* 返回值

  成功返回整型0，失败返回整型-1。

* 示例

```python
#手机呼叫模块，默认不会自动挂断
>>> voiceCall.getAutoCancelStatus()
0

#设置自动挂断功能，手机呼叫模块，默认自动挂断
>>> voiceCall.setAutoCancel(1)
0
>>> voiceCall.getAutoCancelStatus()
1
```



##### 获取来电自动挂断使能状态

> **voiceCall.getAutoCancelStatus()**

获取来电自动挂断使能状态（仅1803S平台支持该接口）。

* 参数 

无

* 返回值

  0:默认不会自动挂断
  1:默认自动挂断

* 示例

```python
#手机呼叫模块，默认不会自动挂断
>>> voiceCall.getAutoCancelStatus()
0

#设置自动挂断功能，手机呼叫模块，默认自动挂断
>>> voiceCall.setAutoCancel(1)
0
>>> voiceCall.getAutoCancelStatus()
1
```



##### 设置DTMF音

> **voiceCall.startDtmf(dtmf, duration)**

​	设置DTMF音。

* 参数

| 参数      | 参数类型 | 参数说明                                              |
| --------  | -------- | ----------------------------------------------------- |
| dtmf      | string   | DTMF字符串。最大字符数：32个。有效字符数有：0、1、…、9、A、B、C、D、*、#     |
| duration  | int      | 持续时间。范围：100-1000；单位：毫秒。                |

* 返回值

  设置成功返回整型0，设置失败返回整型-1。

* 示例

```python
>>> voiceCall.startDtmf('A',100)
0
```



##### DTMF识别使能接口

> **voiceCall.dtmfDetEnable(enable)**

DTMF识别使能接口，默认不开启DTMF识别

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| enable   | int      | 使能开关，取值0/1,0：不开启DTMF识别，1：开启DTMF识别         |

* 返回值

  设置成功返回整型0，设置失败返回整型-1。

* 示例

见voiceCall.dtmfSetCb()接口示例



##### 设置DTMF识别回调接口

> **voiceCall.dtmfSetCb(cb)**

设置DTMF识别回调接口

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| cb       | function | 回调函数                                                     |

* 返回值

  设置成功返回整型0，设置失败返回整型-1。

* 示例

```
>>> def cb(args):
... print(args)
...
...
...
>>> voiceCall.dtmfSetCb(cb)
0
>>> voiceCall.dtmfDetEnable(1)
0

>>> voiceCall.callStart('13855169092')

0
>>>
1   //手机端按下1，callback中会收到按下的字符“1”

8   //手机端按下8

9   //手机端按下9
```



##### 设置控制呼叫转移

> **voiceCall.setFw(reason, fwmode, phonenum)**

控制呼叫转移补充业务。

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| reason   | int      | 呼叫转移的条件/原因:<br/>0 : unconditional<br/>1 : mobile busy<br/>2 : no reply<br/>3 : not reachable |
| fwmode   | int      | 对呼叫转移的控制:<br/>0 : 禁用<br/>1 : 启用<br/>2 : 查询状态<br/>3 : 注册<br/>4 : 擦除 |
| phonenum | string   | 呼叫转移的目标电话                                           |

* 返回值

  设置成功返回整型0，设置失败返回整型-1。

* 示例

  无



##### 切换语音通道

> **voiceCall.setChannel(device)**

设置通话时的声音输出通道，默认是通道0，即听筒。

* 参数

| 参数   | 参数类型 | 参数说明                                        |
| ------ | -------- | ----------------------------------------------- |
| device | int      | 输出通道<br/>0 - 听筒<br/>1 - 耳机<br/>2 - 喇叭 |

* 返回值

  设置成功返回整型0，设置失败返回整型-1。

* 示例

```python
>>> voiceCall.setChannel(2) #切换到喇叭通道
0
```



##### 获取音量大小

> **voiceCall.getVolume()**

获取电话当前音量大小。

* 参数

  无

* 返回值

  返回整型音量值。



##### 设置音量大小

> **voiceCall.setVolume(vol)**

设置电话音量大小。

* 参数

| 参数 | 参数类型 | 参数说明                                     |
| ---- | -------- | -------------------------------------------- |
| vol  | int      | 音量等级，范围（0 ~ 11），数值越大，音量越大 |

* 返回值

  设置成功返回整型0，失败返回整型-1。




##### 自动录音使能接口

> **voiceCall.setAutoRecord(enable, record_type, record_mode, filename)**

自动录音使能接口。默认关闭自动录音，自动录音使能需要在通话前设置完毕。

注：非volte版本无该接口

* 参数

| 参数        | 参数类型 | 参数说明                                                     |
| ----------- | -------- | ------------------------------------------------------------ |
| enable      | int      | 使能开关，范围：<br/>0 - 关闭自动录音接口<br/>1 - 开启自动录音功能 |
| record_type | int      | 录音文件类型，范围：<br/>0 - AMR<br/>1 - WAV                 |
| record_mode | int      | mode，范围：<br/>0 - RX<br/>1 - TX<br/>2 - MIX               |
| filename    | string   | 文件名                                                       |

* 返回值

  设置成功返回整型0，设置失败返回整型-1， 不支持该接口返回字符串"NOT SUPPORT"。

* 示例

```python
>>> voiceCall.setAutoRecord(1,0,2,'U:/test.amr')
0
```



##### 开始录音

> **voiceCall.startRecord(record_type, record_mode, filename)**

开始录音接口。

注：非volte版本无该接口

* 参数

| 参数        | 参数类型 | 参数说明                                       |
| ----------- | -------- | ---------------------------------------------- |
| record_type | int      | 录音文件类型，范围：<br/>0 - AMR<br/>1 - WAV   |
| record_mode | int      | mode，范围：<br/>0 - RX<br/>1 - TX<br/>2 - MIX |
| filename    | string   | 文件名                                         |

* 返回值

  设置成功返回整型0，设置失败返回整型-1，不支持该接口返回字符串"NOT SUPPORT"。

* 示例

```python
>>> voiceCall.startRecord(0,2,'U:/test.amr')
0
```



##### 结束录音

> **voiceCall.stopRecord()**

结束录音接口。

注：非volte版本无该接口

* 参数

  无

* 返回值

  设置成功返回整型0，设置失败返回整型-1， 不支持该接口返回字符串"NOT SUPPORT"。

* 示例

```python
>>> voiceCall.stopRecord()
0
```



##### 开始录音（流形式）

> **voiceCall.startRecordStream(record_type, record_mode, record_cb)**

开始录音接口（流形式）。

* 说明

  1、非volte版本无该接口

  2、录音流第一包数据均是对应格式文件的文件头

  3、wav格式录音流第一包数据不包含文件大小，需结束录音后自行计算

* 参数

| 参数        | 参数类型 | 参数说明                                     |
| ----------- | -------- | -------------------------------------------- |
| record_type | int      | 录音流类型，范围：<br>0 - AMR<br/>1 - WAV    |
| record_mode | int      | mode，范围<br/>0 - RX<br/>1 - TX<br/>2 - MIX |
| record_cb   | function | 回调函数                                     |

* 返回值

  设置成功返回整型0，设置失败返回整型-1，不支持该接口返回字符串"NOT SUPPORT"。

* 示例

callback函数中args定义如下
```
args[0]:stream data
args[1]:stream data len
args[2]:states

states取值如下：
typedef enum
{
	HELIOS_VC_AUD_REC_ERROR = -1,
	HELIOS_VC_AUD_REC_START = 0,
	HELIOS_VC_AUD_REC_DATA,
	HELIOS_VC_AUD_REC_PAUSE,
	HELIOS_VC_AUD_REC_FINISHED,
	HELIOS_VC_AUD_REC_DISK_FULL,
}HELIOS_VC_AUD_REC_STATE;
```

```python
>>> import voiceCall
>>> import audio

>>> f=open('usr/mia.amr','w')

>>> def cb(para):
...     if(para[2] == 1):
...         read_buf = bytearray(para[1])
...         voiceCall.readRecordStream(read_buf,para[1])
...         f.write(read_buf,para[1])
...         del read_buf
...     elif(para[2] == 3):
...         f.close()
...         
...         
... 
>>> voiceCall.callStart('13855169092')
0
>>> voiceCall.startRecordStream(0,2,cb)
0
//此处挂断电话(MO/MT侧挂断都可以)
>>> uos.listdir('usr')
['system_config.json', 'mia.amr']
>>> aud=audio.Audio(0)
>>> aud.setVolume(11)
0
>>> aud.play(2,1,'U:/mia.amr')
0
```



##### 注册监听回调函数

> **voiceCall.setCallback(usrFun))**

注册监听回调函数。在接听、挂断电话时会收到回调。

* 参数 

| 参数   | 参数类型 | 参数说明     |
| ------ | -------- | ------------ |
| usrFun | function | 监听回调函数 |

* 返回值

  成功返回整型0，失败返回整型-1。

* callback函数中的event_id枚举值

```c
typedef enum
{
	HELIOS_VC_INIT_OK_IND = 1,
	HELIOS_VC_RING_IND,
	HELIOS_VC_CONNECT_IND,
	HELIOS_VC_NOCARRIER_IND,
	HELIOS_VC_ERROR_IND,
	HELIOS_VC_CCWA_IND,
	HELIOS_VC_DIALING_IND,
	HELIOS_VC_MO_FAILED_IND,
	HELIOS_VC_HOLDING_IND,
	
	HELIOS_VC_RING_VOLTE_IND = 10,
	HELIOS_VC_CONNECT_VOLTE_IND,
	HELIOS_VC_NOCARRIER_VOLTE_IND,
	HELIOS_VC_CCWA_VOLTE_IND,
	HELIOS_VC_DIALING_VOLTE_IND,
	HELIOS_VC_ALERTING_VOLTE_IND,
	HELIOS_VC_HOLDING_VOLTE_IND
}HELIOS_VC_EVENT_ID_E;
```

* 回调函数参数说明

| event                      | 参数个数 | 参数说明                                                     |
| -------------------------- | -------- | ------------------------------------------------------------ |
| 2, 3, 9                    | 3        | args[0] ：event id<br>args[1] ：call id ( call identification number as described in 3GPP TS 22.030 subclause 4.5.5.1; this number can be used in +CHLD command operations )<br/>args[2] ：phone number |
| 4                          | 3        | args[0] ：event id<br/>args[1] ：call id ( call identification number as described in 3GPP TS 22.030 subclause 4.5.5.1; this number can be used in +CHLD command operations )<br/>args[2] ：cause |
| 6                          | 5        | args[0] ：event id<br/>args[1] ：call id ( call identification number as described in 3GPP TS 22.030 subclause 4.5.5.1; this number can be used in +CHLD command operations )<br/>args[2] ：phone number<br/>args[3] ：num type ( [129/145],129:Dialing string without international access code “+”,145:Dialing string includes international access code character “+” )<br/>args[4] ：CLI状态 |
| 7                          | 1        | args[0] ：event id                                           |
| 8                          | 4        | args[0] ：event id<br/>args[1] ：call id ( call identification number as described in 3GPP TS 22.030 subclause 4.5.5.1; this number can be used in +CHLD command operations )<br/>args[2] ：cause<br/>args[3] ：Indicates if in-band tones are available from network |
| 10, 11, 12, 13, 14, 15, 16 | 8        | args[0] ：event id<br/>args[1] ：call id ( call identification number as described in 3GPP TS 22.030 subclause 4.5.5.1; this number can be used in +CHLD command operations )<br/>args[2] ：dir(MO/MT)<br/>args[3] ：state of the call<br>args[4] ：type ( 这里一般都是0，表示voice call，语音通话业务 )<br/>args[5] ：mpty ( 判断是否是多方通话，0：call is not one of multiparty (conference) call parties，1：call is one of multiparty (conference) call parties )<br/>args[6] ：phone number<br/>args[7] ：num type ( [129/145],129:Dialing string without international access code “+”,145:Dialing string includes international access code character “+” ) |

* 示例
```python
def voice_callback(args):
     if args[0] == 10:
         print('voicecall incoming call, PhoneNO.: ', args[6])
     elif args[0] == 11:
	     print('voicecall connected, PhoneNO.: ', args[6])
     elif args[0] == 12:
	     print('voicecall disconnect')
	 elif args[0] == 13:
	     print('voicecall is waiting, PhoneNO.: ', args[6])
     elif args[0] == 14:
         print('voicecall dialing, PhoneNO.: ', args[6])
     elif args[0] == 15:
	     print('voicecall alerting, PhoneNO.: ', args[6])
     elif args[0] == 16:
	     print('voicecall holding, PhoneNO.: ', args[6])
     
>>> voiceCall.setCallback(voice_callback)
0
>>> voiceCall.callStart('10086')
0
```

* 注意
1、pyhton目前的语音通话支持的是volte call，所以示例中只给出了volte通话的内容
2、QPY_V0004_EC600N_CNLC_FW_VOLTE(2021-09-09发布)之前发布的版本都按照以下规则使用voiceCall

callback函数中的event_ID数值

```
#define QUEC_VOICE_CALL_INDICATION_BASE                          ((uint_32)(0x1000))
#define QUEC_VOLTE_INCOMING_CALL_IND                             ((uint_32)(0x0007 + QUEC_VOICE_CALL_INDICATION_BASE))
#define QUEC_VOLTE_CONNECT_CALL_IND                              ((uint_32)(0x0008 + QUEC_VOICE_CALL_INDICATION_BASE))
#define QUEC_VOLTE_DISCONNECT_CALL_IND                           ((uint_32)(0x0009 + QUEC_VOICE_CALL_INDICATION_BASE))
#define QUEC_VOLTE_WAITING_CALL_IND                              ((uint_32)(0x000A + QUEC_VOICE_CALL_INDICATION_BASE))
```

callback函数中args定义如下
args定义未改变

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
```



#### sms - 短信功能

模块功能：该模块提供短信功能相关接口。

注意：BC25PA/600M平台不支持此模块。

##### 发送TEXT类型消息

> **sms.sendTextMsg(phoneNumber, msg, codeMode)**

发送TEXT类型的消息（不支持发送空短信）。

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



##### 发送PDU类型消息

> **sms.sendPduMsg(phoneNumber, msg, codeMode)**

发送PDU类型的消息（不支持发送空短信）。

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



##### 删除消息

> **sms.deleteMsg(index)**

删除指定索引的消息。

* 参数

| 参数  | 参数类型 | 参数说明                                                     |
| ----- | -------- | ------------------------------------------------------------ |
| index | int      | 需删除短信的索引号                                           |

* 返回值

  删除成功返回整型0，失败返回整型-1。

* 示例

```python
>>> import sms
>>> sms.deleteMsg(0)
0
```



##### 设置短信存储位置

> **sms.setSaveLoc(mem1, mem2, mem3)**

设置短信存储位置。
注意：ASR平台如果要改变接收消息的存储位置，需要重置MEM2 & MEM3，展锐平台只需设定MEM3即可（具体原因和平台底部的实现有关，此处不再赘述）

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



##### 获取短信存储信息

> **sms.getSaveLoc()**

获取当前模块短信存储位置相关信息。

* 参数

  无

* 返回值

  成功返回一个元组，包含3个部分，返回值形式如下：

  `([loc1, current_nums, max_nums],[loc2, current_nums, max_nums],[loc3, current_nums, max_nums])`

  返回值参数说明：

  `loc1` - 读取和删除消息所在的位置

  `loc2` - 写入和发送消息所在的位置

  `loc3` - 接收消息的存储位置

  `current_nums` - 当前空间已有短信数量

  `max_nums` - 当前空间最大短信存储数量
  
  失败返回整形-1

* 示例

```python
>>> sms.getSaveLoc()
(['SM', 2, 50], ['SM', 2, 50], ['SM', 2, 50])
>>> sms.setSaveLoc('SM','ME','MT')
0
>>> sms.getSaveLoc()
(['SM', 2, 50], ['ME', 14, 180], ['MT', 2, 50])
```



##### 获取短信数量

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



##### PDU方式读取短信

> **sms.searchPduMsg(index)**

以PDU方式获取短信内容。

* 参数

| 参数  | 参数类型 | 参数说明                                                     |
| ----- | -------- | ------------------------------------------------------------ |
| index | int      | 需要获取短信的索引，范围0 ~ MAX-1，MAX为模块存储短信的最大数量 |

* 返回值

  成功返回PDU类型的短信内容，string类型，失败返回整型-1。



##### TEXT方式读取短信

> **sms.searchTextMsg(index)**

以TEXT方式获取短信内容。

* 参数

| 参数  | 参数类型 | 参数说明                     |
| ----- | -------- | ---------------------------- |
| index | int      | 需要获取短信的索引，范围0 ~ MAX-1，MAX为模块存储短信的最大数量 |

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



##### 获取短信中心号码

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



##### 设置短信中心号码

> **sms.setCenterAddr(addr)**

设置短信中心号码。若无特殊需求，不建议更改短信中心号码。

* 参数

| 参数 | 参数类型 | 参数说明                                       |
| ---- | -------- | ---------------------------------------------- |
| addr | string   | 需要设置的短信中心号码                         |

* 返回值

  设置成功返回整型0，失败返回整型-1。

* 示例

  无



##### 获取PDU短信长度

> **sms.getPduLength(pduMsg)**

获取指定PDU短信的长度。

* 参数

| 参数   | 参数类型 | 参数说明 |
| ------ | -------- | -------- |
| pduMsg | string   | PDU短信  |

* 返回值

  成功返回整型PDU短信长度，失败返回整型-1。

* 示例

```python
>>> import sms
>>> sms.searchPduMsg(0)
'0891683108501505F0040D91688122162743F200000211529003332318C16030180C0683C16030180C0683E170381C0E87'
>>> sms.getPduLength(sms.searchPduMsg(0)) #注意，是获取PDU短信长度，不是上面字符串的长度
40
```



##### PDU解码

> **sms.decodePdu(pduMsg, pduLen)**

PDU解码

* 参数

| 参数   | 参数类型 | 参数说明   |
| ------ | -------- | --------   |
| pduMsg | string   | PDU短信    |
| pduLen | int      | PDU码长度  |

* 返回值

  成功返回PDU解码后的内容，返回格式如下，失败返回-1。

  返回格式：(phoneNumber, msg, time, msgLen)

  `phoneNumber` ：短信来源手机号

  `msg` ：短信内容

  `time` ：收到短信的时间

  `msgLen` ：短信消息长度

* 示例

```python
>>> import sms
>>>sms.decodePdu('0891683110305005F00405A10110F000081270319043442354516C76CA77ED4FE1FF1A00320030003200315E7496328303975E6CD596C68D445BA34F2067086D3B52A863D09192FF1A4E3B52A88FDC79BB975E6CD596C68D44FF0C5171540C5B8862A47F8E597D751F6D3B3002',20)
>>>('10010', '公益短信：2021年防范非法集资宣传月活动提醒：主动远离非法集资，共同守护美好生活。', '2021-07-13 09:34:44', 118)
>>> 
```



##### 注册监听回调函数

> **sms.setCallback(usrFun)**

注册监听回调函数。

* 参数

| 参数   | 参数类型 | 参数说明                               |
| ------ | -------- | -------------------------------------- |
| usrFun | function | 监听回调函数，回调具体形式及用法见示例 |

* 返回值

  注册成功返回整型0，失败返回整型-1。

* 示例

  短信回调函数新老架构的使用方法不同，如下所示，新架构参照示例一，QPY_V0004_EC600N_CNLC_FW_VOLTE(2021-09-09发布)之前发布的版本参照示例二。

示例一：

callback中args释义如下：
```
args[0]:event id
args[1]:sms index
args[2]:sms storage
```


```python
import sms

def cb(args):
    index = args[1]
    storage = args[2]
    print('New message! storage:{},index:{}'.format(storage, index))
    
sms.setCallback(cb)
```

示例二：

```python
import sms

def cb(args):
    ind_flag = args[0]
	if ind_flag == 4097:
	    mes_buf = args[1]
		mes_len = args[2]
		print('New message! ind_flag:{},mes_buf:{},mes_len:{}'.format(ind_flag, mes_buf, mes_len))
    elif ind_flag == 4099:
	    mes_type = args[1]
		storage = args[2]
        index = args[3]
        print('New message! ind_flag:{},mes_type:{},storage:{},index:{}'.format(ind_flag, mes_type, storage, index))
	elif ind_flag == 4100:
	    mes_buf = args[1]
        print('New message! ind_flag:{},mes_buf:{}'.format(ind_flag, mes_buf))
	elif ind_flag == 4101:
		storage = args[1]
        index = args[2]
        print('New message! ind_flag:{},storage:{},index:{}'.format(ind_flag, storage, index))
    
sms.setCallback(cb)
```



#### net - 网络相关功能

模块功能：该模块提供配置和查询网络模式信息等接口。

##### 设置APN

> **net.setApn(\*args)**

设置APN，设置后需要重启或者通过 net.setModemFun(mode) 接口先切换到模式0，再切换到模式1才能生效。 

* 参数

  该接口在Qualcomm/ASR_1803s/ASR_1601/ASR_1606/Unisoc平台为可变参函数,参数个数为2或7, 其他平台参数个数固定为7：
    参数个数为2：net.setApn(apn, simid)
    参数个数为7：net.setApn(pid, iptype, apn, usrname, password, authtype, simid)
  
  具体释义形式如下：
  
| 参数    | 参数类型 | 参数说明                      |
| -----   | -------- | ----------------------------- |
| pid     | int      | PDP索引                       |
| iptype  | int      | IP类型，0-IPV4，1-IPV6，2-IPV4和IPV6   |
| apn     | string   | apn名称，可为空，最大长度不超过64字节  |
| usrname | string   | 用户名，可为空，最大长度不超过64字节   |
| password| string   | 用户名，可为空，最大长度不超过64字节   |
| authtype| int      | 加密方式，0-不加密，1-PAP，2-CHAP，3-PAP AND CHAP(CATM平台支持)|
| simid   | int      | simid，目前仅支持0<br> 0 - 卡1 <br> 1 - 卡2 |

* 返回值

  设置成功返回整型值0，设置失败返回整型值-1。

* 注意

  BC25PA平台不支持此方法。

* 示例

```python
>>> net.setApn('3gnet',0)
0
>>> net.setApn(1,1,'3gnet','mia','123',2,0)
0  
```



##### 获取当前APN

> **net.getApn(\*args)**

获取当前APN。

* 参数

  该接口在Qualcomm/ASR_1803s/ASR_1601/ASR_1606/Unisoc平台为可变参函数,参数个数为1或2, 其他平台参数个数固定为2：
    参数个数为2：net.getApn(pid, simid)
    参数个数为1：net.getApn(simid)
	
  具体释义如下：

| 参数  | 参数类型 | 参数说明                                         |
| ----- | -------- | ------------------------------------------------ |
| pid   | int      | PDP索引                                          |
| simid | int      | simid，目前仅支持0<br/> 0 - 卡1    <br/> 1 - 卡2 |

* 返回值

  1、当参数只有simid时：
    成功返回获取到的APN，失败返回整型值-1。
  2、当参数为pid, simid时：
    成功返回获取到的pdp context：(iptype, apn, usrname, password, authtype)，失败返回整型值-1。

* 注意

  BC25PA平台不支持此方法。

* 示例

```python
>>> net.getApn(0)
'3gnet'
>>> net.getApn(1,0)
(1, '3gnet', 'mia', '123', 2)
```



##### 获取csq信号强度

> **net.csqQueryPoll()**

获取csq信号强度。

* 参数

  无

* 返回值

  成功返回整型的csq信号强度值，失败返回整型值-1，返回值为99表示异常；

  信号强度值范围0 ~ 31，值越大表示信号强度越好。

* 示例

```python
>>> import net
>>> net.csqQueryPoll()
31
```



##### 获取小区信息

> **net.getCellInfo(\*args)**

获取邻近 CELL 的信息。

* 参数

  该接口在BC25平台和移芯小内存方案为可变参函数,参数个数为0或1, 其他平台参数个数固定为0：
    参数个数为0：net.getCellInfo()
    参数个数为1：net.getCellInfo(sinr_enable)
	
  | 参数    | 参数类型 | 参数说明                      |
  | -----   | -------- | ----------------------------- |
  | enable  | int      | 范围0/1, 0:表示不获取sinr 1:表示需要获取sinr|

* 返回值

  失败返回整型值-1，成功返回包含三种网络系统（GSM、UMTS、LTE）的信息的list，如果对应网络系统信息为空，则返回空的List。返回值格式如下：

  `([(flag, cid, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, licd, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, mcc, mnc, pci, tac, earfcn, rssi, rsrq, sinr),...])`

* GSM网络系统返回值说明

| 参数  | 参数意义                                                     |
| ----- | ------------------------------------------------------------ |
| flag  | 返回 0 - 3， 0：present，1：neighbor，2：neighbor_intra 3：neighbor_inter                 |
| cid   | 返回GSM网络下的cell id信息，0则为空，范围0 ~ 65535           |
| mcc   | 移动设备国家代码，范围 0 ~ 999<br>注意：EC100Y/EC600S/EC600N系列的模组，该值是用十六进制来表示，比如下面示例中的十进制数1120，用十六进制表示为0x460，表示移动设备国家代码460，其他型号模组，该值直接用十进制表示，比如移动设备国家代码460，就是用十进制的460来表示。 |
| mnc   | 移动设备网络代码，范围 0 ~ 99                                |
| lac   | 位置区码，范围 1 ~ 65534                                     |
| arfcn | 无线频道编号，范围 0 ~ 65535                                 |
| bsic  | 基站识别码，范围 0 ~ 255                                     |
| rssi  | GSM网络下，该值表示接收电平，描述接收到信号强度，99表示未知或者无法检测到，该值的计算方式如下<br/>rssi = RXLEV - 111，单位dBm，RXLEV 的范围是 0 ~ 63，所以rssi范围是 -111 ~ -48 dBm； |

* UMTS网络系统返回值说明

| 参数   | 参数意义                                                     |
| ------ | ------------------------------------------------------------ |
| flag   | 返回 0 - 3， 0：present，1：neighbor，2：neighbor_intra 3：neighbor_inter                   |
| cid    | 返回UMTS网络下的 Cell identity 信息，Cell identity = RNC_ID * 65536 + Cell_ID，Cell identity范围 0x0000000 ~ 0xFFFFFFF（注意这里是28bits）；其中RNC_ID的范围是0 ~ 4095，Cell_ID的范围是0 ~ 65535 |
| lcid   | URA ID，范围 0 ~ 65535，0表示该信息不存在                    |
| mcc    | 移动设备国家代码，范围 0 ~ 999                               |
| mnc    | 移动设备网络代码，范围 0 ~ 99                                |
| lac    | 位置区码，范围 1 ~ 65534                                     |
| uarfcn | 无线频道编号，范围 0 ~ 65535                                 |
| psc    | 基站识别码，范围 0 ~ 255                                     |
| rssi   | UMTS网络下，该值表示 CPICH/PCCPCH 接收信号码功率，范围 -5 ~ 99，单位dBm |

* LTE网络系统返回值说明

| 参数   | 参数意义                                                     |
| ------ | ------------------------------------------------------------ |
| flag   | 返回 0 - 3， 0：present，1：neighbor，2：neighbor_intra 3：neighbor_inter                   |
| cid    | 返回LTE网络下的 Cell identity 信息，Cell identity = RNC_ID * 65536 + Cell_ID，Cell identity范围 0x0000000 ~ 0xFFFFFFF（注意这里是28bits）；其中RNC_ID的范围是0 ~ 4095，Cell_ID的范围是0 ~ 65535 |
| mcc    | 移动设备国家代码，范围 0 ~ 999                               |
| mnc    | 移动设备网络代码，范围 0 ~ 99                                |
| pci    | 物理层小区标识号，0 ~ 503                                    |
| tac    | 跟踪区域码，0 ~ 65535                                        |
| earfcn | 无线频道编号，范围 0 ~ 65535                                 |
| rssi   | 接收的信号强度，在LTE网络下，表示RSRP质量（负值），是根据RSRP测量报告值换算而来，换算关系如下：<br>RSRP质量（负数）= RSRP测量报告值 - 140，单位dBm，范围 -140 ~ -44 dBm |
| rsrq  |(Reference Signal Receiving Quality):LTE参考信号接收质量(仅ASR平台数据有意义，其余平台默认0)，范围 -20 ~ -3  注：理论上rsrq的范围应该是-19.5 ~ -3，但由于计算方法问题，目前能给出的是-20 ~ -3|
| sinr   |信噪比(目前仅BC25和移芯小内存平台支持获取该参数，范围-30 ~ 30)       |

* 示例

```python
>>> net.getCellInfo()
([], [], [(0, 232301375, 1120, 17, 378, 26909, 1850, -66, -8), (3, 110110494, 1120, 17, 10, 26909, 2452, -87, -17), (3, 94542859, 1120, 1, 465, 56848, 1650, -75, -10), 
(3, 94472037, 1120, 1, 369, 56848, 3745, -84, -20)])

//bc25
>>> net.getCellInfo(1)
([], [], [(0, 17104243, 460, 4, 169, 19472, 3688, -56, -108, -3)])
>>> net.getCellInfo(0)
([], [], [(0, 17104243, 460, 4, 169, 19472, 3688, -75, -102)])
>>> net.getCellInfo()
([], [], [(0, 17104243, 460, 4, 121, 19472, 3688, -76, -105)])
```



##### 获取网络制式及漫游配置

注意：BC25PA平台不支持此方法。展锐平台不支持漫游参数配置。移芯平台仅支持LTE ONLY.

> **net.getConfig()**

获取当前网络模式、漫游配置。

* 参数

  无

* 返回值

  失败返回整型值-1，成功返回一个元组，包含当前首选的网络制式与漫游打开状态。

* 网络制式

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
| 19   | CATM,             BG95 supported                             |
| 20   | GSM_CATM,         BG95 supported                             |
| 21   | CATNB,            BG95 supported                             |
| 22   | GSM_CATNB,        BG95 supported                             |
| 23   | CATM_CATNB,       BG95 supported                             |
| 24   | GSM_CATM_CATNB,   BG95 supported                             |
| 25   | CATM_GSM,         BG95 supported                             |
| 26   | CATNB_GSM,        BG95 supported                             |
| 27   | CATNB_CATM,       BG95 supported                             |
| 28   | GSM_CATNB_CATM,   BG95 supported                             |
| 29   | CATM_GSM_CATNB,   BG95 supported                             |
| 30   | CATM_CATNB_GSM,   BG95 supported                             |
| 31   | CATNB_GSM_CATM,   BG95 supported                             |
| 32   | CATNB_CATM_GSM,   BG95 supported                             |

* 示例

```python
>>>net.getConfig ()
(8, False)
```



##### 设置网络制式及漫游配置

注意：BC25PA平台不支持此方法。展锐平台不支持漫游参数配置。移芯平台仅支持LTE ONLY.

> **net.setConfig(mode, roaming)**

设置网络模式、漫游配置。

* 参数

| 参数    | 参数类型 | 参数说明                             |
| ------- | -------- | ------------------------------------ |
| mode    | int      | 网络制式，0 ~ 24，详见上述网络制式表格 |
| roaming | int      | 漫游开关(0：关闭， 1：开启)，可选参数，不支持的平台不填写该参数即可。 |

* 返回值

  设置成功返回整型值0，设置失败返回整型值-1。




##### 获取网络配置模式

> **net.getNetMode()**

获取网络配置模式。

* 参数

  无

* 返回值

  失败返回整型值-1，成功返回一个元组，格式为：`(selection_mode, mcc, mnc, act)`

  返回值参数说明：
  `selection_mode` ：方式，0 - 自动，1 - 手动
  `mcc` ：移动设备国家代码，string类型
  `mnc` ：移动设备网络代码，string类型
  `act` ：首选网络的ACT模式

* ACT模式

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

* 注：CATM平台参照下表

| 值   | 说明               |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | GSM COMPACT        |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E_UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E_UTRAN_CA         |
| 10   | E_UTRAN_NBIOT      |
| 11   | E_UTRAN_EMTC       |
| 12   | NONE               |

* 示例

```python
>>> net.getNetMode()
(0, '460', '46', 7)
```



##### 获取详细信号强度信息

> **net.getSignal(\*args)**

获取详细信号强度。

* 参数

  该接口在非RDA平台为可变参函数,参数个数为0或1, RDA平台参数个数固定为0：
    参数个数为0：net.getSignal()
    参数个数为1：net.getSignal(sinr_enable)
	
  | 参数    | 参数类型 | 参数说明                      |
  | -----   | -------- | ----------------------------- |
  | enable  | int      | 范围0/1, 0:表示不获取sinr 1:表示需要获取sinr|

* 返回值

  失败返回整型值-1，成功返回一个元组，包含两个List(GW 、LTE)，返回值格式如下：

  `([rssi, bitErrorRate, rscp, ecno], [rssi, rsrp, rsrq, cqi, sinr])`

  返回值参数说明：

  GW list：

  `rssi` ：<br>GSM和WCDMA网络下，该值表示接收电平，描述接收到信号强度，99表示未知或者无法检测到，该值的计算方式如下<br>rssi = RXLEV - 111，单位dBm，RXLEV 的范围是 0 ~ 63；

  `bitErrorRate` ：误码率，范围 0 ~ 7，99表示未知或者无法检测到

  `rscp` ：接收信号码功率，范围 -121 ~ -25 dBm，255表示未知或者无法检测到

  `ecno` ：导频信道，范围 -24 ~ 0，255表示未知或者无法检测到

  LTE list：

  `rssi` ：接收的信号强度，范围 -140 ~ -44 dBm，99表示未知或者无法检测到

  `rsrp` ：下行参考信号的接收功率，范围 -141 ~ -44 dBm，99表示未知或者无法检测到

  `rsrq` ：下行特定小区参考信号的接收质量，范围 -20 ~ -3 dBm，值越大越好

  `cqi` ：信道质量
  
  `sinr`: 信噪比(RDA平台不支持获取该参数)

* 示例

```python
>>>net.getSignal()
([99, 99, 255, 255], [-51, -76, -5, 255])
>>>net.getSignal(0)
([99, 99, 255, 255], [-51, -76, -5, 255])
>>>net.getSignal(1)
([99, 99, 255, 255], [-51, -76, -5, 255, 18])
```



##### 获取当前基站时间

> **net.nitzTime()**

获取当前基站时间。这个时间是基站在模块开机注网成功时下发的时间。

* 参数

  无

* 返回值

  失败返回整型值-1，成功返回一个元组，包含基站时间与对应时间戳与闰秒数（0表示不可用），格式为：

  `(date, abs_time, leap_sec)`

  `date` ：基站时间，string类型，其中关于时区的部分，EC600N/EC800N系列与EC200U/EC600U系列有所区别，具体见示例。如果需要设置和获取时区，请使用utime模块的`setTimeZone(offset)`和`getTimeZone()`接口，不同平台，这两个接口的单位都是小时，具体参考utime模块的说明。

  `abs_time` ：基站时间的绝对秒数表示，整型

  `leap_sec` ：闰秒数，整型

* 示例

```python
>>> net.nitzTime() 
('21/10/26 06:08:03 8 0', 1635228483, 0) # EC600N/EC800N系列的返回值，时区单位小时，这里8即表示东八区
('20/11/26 02:13:25 +32 0', 1606356805, 0) # EC200U/EC600U系列返回值，时区单位15分钟，这里+32即表示东八区
```



##### 获取运营商信息

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



##### 获取网络注册信息

> **net.getState()**

获取当前网络注册信息。

* 参数

  无

* 返回值

  失败返回整型值-1，成功返回一个元组，包含电话和网络注册信息，元组中voice开头的表示电话注册信息，data开头的表示网络注册信息，格式为：

  `([voice_state, voice_lac, voice_cid, voice_rat, voice_reject_cause, voice_psc], [data_state, data_lac, data_cid, data_rat, data_reject_cause, data_psc])`

  返回值参数说明：

  `state` ：网络注册状态

  `lac` ：位置区码，范围 1 ~ 65534

  `cid` ：cell id，范围 0x00000000 ~ 0x0FFFFFFF

  `rat` ：access technology，即接入技术

  `reject_cause` ：注册被拒绝的原因，EC200U/EC600U/BC25PA平台该参数保留，不作为有效参数

  `psc` ：主扰码，Primary Scrambling Code，EC200U/EC600U/BC25PA平台该参数保留，不作为有效参数

* 网络注册状态` state`

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

* 接入技术 access technology

| 值   | 说明               |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | GSM COMPACT        |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E_UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E_UTRAN_CA         |
| 10   | NONE               |

* 注：CATM平台参照下表

| 值   | 说明               |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | GSM COMPACT        |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E_UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E_UTRAN_CA         |
| 10   | E_UTRAN_NBIOT      |
| 11   | E_UTRAN_EMTC       |
| 12   | NONE               |

* 示例

```python
>>> net.getState()
([11, 26909, 232301323, 7, 0, 466], [0, 26909, 232301323, 7, 0, 0])
```



##### 获取附近小区ID

> **net.getCi()**

获取附近小区ID。该接口获取结果即为`net.getCellInfo()`接口获取结果中的cid集合。

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



##### 获取服务小区ID

> **net.getServingCi()**

获取服务小区ID。（实时获取）

* 参数

  无

* 返回值

  成功返回服务小区ID。

  失败返回整型值-1。

* 示例

```python
>>> net.getServingCi()
94938399
```



##### 获取附近小区的mnc

> **net.getMnc()**

获取附近小区的mnc。该接口获取结果即为`net.getCellInfo()`接口获取结果中的mnc集合。

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



##### 获取服务小区的mnc

> **net.getServingMnc()**

获取服务小区的mnc。（实时获取）

* 参数

  无

* 返回值

  成功返回服务小区mnc。

  失败返回整型值-1。

* 示例

```python
>>> net.getServingMnc()
1
```



##### 获取附近小区的mcc

> **net.getMcc()**

获取附近小区的mcc。该接口获取结果即为`net.getCellInfo()`接口获取结果中的mcc集合。

* 参数

  无

* 返回值

  成功返回一个list类型的数组，包含小区mcc，格式为：`[mcc, ……, mcc]`。数组成员数量并非固定不变，位置不同、信号强弱不同等都可能导致获取的结果不一样。

  失败返回整型值-1。

  注意：EC100Y/EC600S/EC600N系列的模组，该值是用十六进制来表示，比如下面示例中的十进制数1120，十六进制即0x460，表示移动设备国家代码460，其他型号模组，该值直接用十进制表示，比如移动设备国家代码460，就是用十进制的460来表示。

* 示例

```python
>>> net.getMcc()
[1120, 0]
```



##### 获取服务小区的mcc

> **net.getServingMcc()**

获取服务小区的mcc。（实时获取）

* 参数

  无

* 返回值

  成功返回服务小区的mcc。

  失败返回整型值-1。

  注意：EC100Y/EC600S/EC600N系列的模组，该值是用十六进制来表示，比如下面示例中的十进制数1120，十六进制即0x460，表示移动设备国家代码460，其他型号模组，该值直接用十进制表示，比如移动设备国家代码460，就是用十进制的460来表示。

* 示例

```python
>>> net.getServingMcc()
1120
```



##### 获取附近小区的lac

> **net.getLac()**

获取附近小区的Lac。该接口获取结果即为`net.getCellInfo()`接口获取结果中的lac集合。

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



##### 获取服务小区的lac

> **net.getServingLac()**

获取服务小区的Lac。（实时获取）

* 参数

  无

* 返回值

  成功返回服务小区lac

  失败返回整型值-1。

* 示例

```python
>>> net.getServingLac()
56848
```



##### 获取当前工作模式

> **net.getModemFun()**

获取当前工作模式。

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



##### 设置当前工作模式

> **net.setModemFun(function, rst)**

设置当前SIM模式。

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| function | int      | 设置SIM卡模式<br/>0 - 全功能关闭<br/>1 - 全功能开启<br/>4 - 飞行模式 (RDA平台不支持cfun4) |
| rst      | int      | 可选参数 <br>0 - 设置立即生效（默认为0）<br/>1 - 设置完重启  |

* 返回值

  设置成功返回整型值0，设置失败返回整型值-1。

* 示例

```python
>>> net.setModemFun(4)
0
```



##### band设置与获取

##### band值对照表

| 网络制式        | band值                                                       |
| --------------- | ------------------------------------------------------------ |
| EGPRS(GSM)      | EGSM900 - 0x1<br/>DCS1800 - 0x2<br/>GSM850 - 0x4<br/>PCS1900 - 0x8 |
| LTE/eMTC/NB-IoT | BAND1 - 0x1<br/>BAND2 - 0x2<br/>BAND3 - 0x4<br/>BAND4 - 0x8<br/>BAND5 - 0x10<br/>BAND8 - 0x80<br/>BAND12 - 0x800<br/>BAND13 - 0x1000<br/>BAND18 - 0x20000<br/>BAND19 - 0x40000<br/>BAND20 - 0x80000<br/>BAND25 - 0x1000000<br/>BAND26 - 0x2000000<br/>BAND27 - 0x4000000<br/>BAND28 - 0x8000000<br/>BAND31 - 0x40000000<br/>BAND66 - 0x20000000000000000<br/>BAND71 - 0x400000000000000000<br/>BAND72 - 0x800000000000000000<br/>BAND73 - 0x1000000000000000000<br/>BAND85 - 0x1000000000000000000000<br/> |

##### BG95M3模组band支持表

| 网络制式 | 支持的BAND                                                   |
| -------- | ------------------------------------------------------------ |
| eMTC     | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B26/B27/B28/B66/B85 |
| NB-IoT   | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B28/B66/B71/B85    |
| EGPRS    | GSM850/EGSM900/DCS1800/PCS1900                               |

##### EG912NENAA模组band支持表

| 网络制式 | 支持的BAND                           |
| -------- | ------------------------------------ |
| LTE      | B1/B3/B5/B7/B8/B20/B28/B31/B72       |
| EGPRS    | EGSM900/DCS1800                      |



##### band设置

> **net.setBand(net_rat, gsm_band, band_tuple)**

* 功能

  设置需要的band，即在模组支持的前提下，锁定用户指定的band。 (当前可支持平台：CATM/EG912NENAA)

* 参数

| 参数       | 类型  | 说明                                                         |
| ---------- | ----- | ------------------------------------------------------------ |
| net_rat    | int   | 指定要设置的是哪种网络模式下的band<br>0 - 设置GSM网络的band<br>1 - 设置LTE网络的band<br>2 - 设置CATM网络的band<br>3 - 设置NB网络的band<br>注意：CATM平台不支持上述模式1，即LTE网络的band<br/>EG912NENAA仅支持上述模式0和模式1 |
| gsm_band   | int   | GSM网络的band值<br/>0x01 - GSM_EGSM900<br/>0x02 - GSM_DCS1800<br>0x04 - GSM_GSM850<br/>0x08 - GSM_PCS1900 |
| band_tuple | tuple | 设置GSM网络之外的其他网络模式的band值，是一个包含4个元素的元组，每个成员最大不能超过4字节，形式如下：<br>(band_hh, band_hl, band_lh, band_ll)<br>每个元素说明如下：<br>band_hh - band值的高8字节的高4字节<br>band_hl  - band值的高8字节的低4字节<br/>band_lh  - band值的低8字节的高4字节<br/>band_ll   - band值的低8字节的低4字节<br/>如果用户最终要设置的band值为band_value，那么计算方式如下：<br>band_hh = (band_value & 0xFFFFFFFF000000000000000000000000) >> 96 <br/>band_hl = (band_value & 0x00000000FFFFFFFF0000000000000000) >> 64 <br/>band_lh = (band_value & 0x0000000000000000FFFFFFFF00000000) >> 32 <br/>band_ll = (band_value & 0x000000000000000000000000FFFFFFFF) |

* 返回值

  设置成功返回整形0，失败返回整形-1。

* 示例

```python
import net
import utime

'''
用户可直接使用下面两个接口来设置band和获取band
'''
def set_band(net_rat, band_value):
    if net_rat == 0:
        retval = net.setBand(0, band_value, (0, 0, 0, 0))
    else:
        band_hh = (band_value & 0xFFFFFFFF000000000000000000000000) >> 96
        band_hl = (band_value & 0x00000000FFFFFFFF0000000000000000) >> 64
        band_lh = (band_value & 0x0000000000000000FFFFFFFF00000000) >> 32
        band_ll = (band_value & 0x000000000000000000000000FFFFFFFF)
        retval = net.setBand(net_rat, 0, (band_hh, band_hl, band_lh, band_ll))
    return retval


def get_band(net_rat):
    return net.getBand(net_rat)

#======================================================================================================

'''
设置GSM网络band为0xa，即 DCS1800 + PCS1900
0xa = 0x2(DCS1800) + 0x8(PCS1900)
'''
def set_gsm_band_example():
    print('Set GSM band to 0xa example:')
    gsm_band = get_band(0)
    print('GSM band value before setting:{}'.format(gsm_band))
    ret = set_band(0, 0xa)
    if ret == 0:
        print('Set GSM band successfully.')
    else:
        print('Set GSM band failed.')
    utime.sleep(1) # 设置band需要一定时间，延时一段时间再获取新的结果
    gsm_band = get_band(0)
    print('GSM band value after setting:{}'.format(gsm_band))
    return ret


'''
设置eMTC网络band为0x15，即设置 BAND1+BAND3+BAND5
0x15 = 0x1(BAND1) + 0x4(BAND3) + 0x10(BAND5)
'''
def set_camt_band_example():
    print('Set CATM band to 0x15 example:')
    catm_band = get_band(2)
    print('CATM band value before setting:{}'.format(catm_band))
    ret = set_band(2, 0x15)
    if ret == 0:
        print('Set CATM band successfully.')
    else:
        print('Set CATM band failed.')
    utime.sleep(1) # 设置band需要一定时间，延时一段时间再获取新的结果
    catm_band = get_band(2)
    print('CATM band value after setting:{}'.format(catm_band))
    return ret


'''
设置NB-IoT网络band为0x1000800000000000020011，即设置 BAND1+BAND5+BAND18+BAND71+BAND85
0x1000400000000000020011 = 0x1 + 0x10 + 0x20000 + 0x400000000000000000 + 0x1000000000000000000000
'''
def set_nb_band_example():
    print('Set NB band to 0x1000400000000000020011 example:')
    nb_band = get_band(3)
    print('NB band value before setting:{}'.format(nb_band))
    ret = set_band(3, 0x1000400000000000020011)
    if ret == 0:
        print('Set NB band successfully.')
    else:
        print('Set NB band failed.')
    utime.sleep(1) # 设置band需要一定时间，延时一段时间再获取新的结果
    nb_band = get_band(3)
    print('NB band value after setting:{}'.format(nb_band))
    return ret


def main():
    set_gsm_band_example()
    utime.sleep(1)
    set_camt_band_example()
    utime.sleep(1)
    set_nb_band_example()


if __name__ == '__main__':
    main()
    

#===================================================================================================
#运行结果
Set GSM band to 0xa example:
GSM band value before setting:0xf
Set GSM band successfully.
GSM band value after setting:0xa

Set CATM band to 0x15 example:
CATM band value before setting:0x10000200000000090e189f
Set CATM band successfully.
CATM band value after setting:0x15

Set NB band to 0x1000400000000000020011 example:
NB band value before setting:0x10004200000000090e189f
Set NB band successfully.
NB band value after setting:0x1000400000000000020011

```



##### band获取

> **net.getBand(net_rat)**

* 功能

获取当前某个网络制式下的band设置值。(当前可支持平台：CATM/EG912NENAA)

* 参数

| 参数    | 类型 | 说明                                                         |
| ------- | ---- | ------------------------------------------------------------ |
| net_rat | int  | 指定要设置的是哪种网络模式下的band<br/>0 - 设置GSM网络的band<br/>1 - 设置LTE网络的band<br/>2 - 设置CATM网络的band<br/>3 - 设置NB网络的band<br/>注意：CATM平台不支持上述模式1，即LTE网络的band<br/>EG912NENAA仅支持上述模式0和模式1 |

* 返回值

返回十六进制字符串形式的band值。

* 示例

```python
net.getBand(2)
'0x10000200000000090e189f'  # 这是字符串，用户如果需要int型，可通过int(data)来自行转换
```



##### band恢复初始值

> **net.bandRst()**

* 功能

恢复band初始设定值。(当前可支持平台：EG912NENAA)

* 参数

无

* 返回值

成功返回整形0，失败返回整形-1。

* 示例

```python
#先设置成其他band，调用该接口，看是否成功恢复成初始值
#EG912NENAA平台初始值：gsm_band:0x3(EGSM900/DCS1800 )  lte_band:0x8000000000480800D5(B1/B3/B5/B7/B8/B20/B28/B31/B72 )
net.bandRst()
0
```



#### checkNet - 等待网络就绪

模块功能：checkNet模块主要用于【开机自动运行】的用户脚本程序，该模块提供API用来阻塞等待网络就绪，如果超时或者其他异常退出会返回错误码，所以如果用户的程序中有涉及网络相关的操作，那么在用户程序的开始应该调用 checkNet 模块中的方法以等待网络就绪。当然，用户也可以自己实现这个模块的功能。

注意：当前仅EC600S/EC600N/EC800N/EC200U/EC600U/BC25PA/平台支持该功能。

##### 创建checkNet对象

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

* 示例

```python
import checkNet

PROJECT_NAME = "XXXXXXXX"
PROJECT_VERSION = "XXXX"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)
```



##### 开机打印信息

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



##### 等待网络就绪

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

* 说明

如果是2021年11月以后发布的版本，用户可不用实例化对象，即可直接使用wait_network_connected(timeout)方法，用法如下：

```python
import checkNet

if __name__ == '__main__':
    # 在用户程序运行前增加下面这一句
    stagecode, subcode = checkNet.wait_network_connected(30)
    print('stagecode = {}, subcode = {}'.format(stagecode, subcode))
	......
```



##### checkNet 异常返回处理

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
            #     的apn，用户可通过 sim 模块的 sim.getImsi() 来获取 IMSI 码，确认IMSI的第四和第五			  
            #     位字符组成的数字是否在 01 ~ 13 的范围内，如果不在，说明当前默认apn配置表中无此类SIM卡对
            #     应的apn 信息，这种情况下，用户如果希望开机拨号成功，可以使用 dataCall.setApn(...)
            #     接口来设置保存用户自己的apn信息，然后开机重启，就会使用用户设置的apn来进行开机拨号；
            # （5）如果手动拨号也失败，那么请联系我们的FAE反馈问题，最好将相应SIM卡信息，比如哪个运营商
            #     的卡、什么类型的卡、卡的IMSI等信息也一并提供，必要时可以将SIM卡寄给我们来排查问题。
```



#### fota - 固件升级

模块功能：固件升级。

##### 创建fota对象

可选择传入参数以选择下载完升级包后是否自动重启

> **import fota**
>
> **fota_obj = fota()** #下载完自动重启
>
> **fota_obj = fota(reset_disable=1)** #下载完不自动重启

##### 一键升级接口

> **fota_obj.httpDownload(url1=, url2=, callback=)**

一个接口实现固件下载和升级整个过程

- 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| url1     | str      | 待下载的第一阶段升级包的url                                  |
| url2     | str      | 待下载的第二阶段升级包的url，注：最小系统升级分为2个阶段，必须传入该参数，而差分升级、全包升级只有一个阶段，该参数禁止传入，仅EC600S/EC600N平台支持最小系统升级方式 |
| callback | function | 回调函数，显示下载进度和状态，可选择传不传入，注：非最小系统升级方式时有效 |

- 返回值

  下载成功返回整形值0，下载失败返回整形值-1。注：EC600S/EC600N平台，返回值只代表指令下发成功、失败，下载状态需通过回调反馈。BC25PA平台返回值只代表创建下载任务成功,下载过程和结果需要回调反馈。

- 示例

```python
#args[0]表示下载状态，下载成功返回整型值：0或1或2，下载失败返回整型值：非0、1、2，args[1]表示下载进度(注：EC600S/EC600N平台当下载状态是成功时表示百分比，下载状态是失败时表示错误码)
def result(args):
    print('download status:',args[0],'download process:',args[1])
    
#差分升级、全量升级    
fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)    
#最小系统升级
fota_obj.httpDownload(url1="http://www.example.com/fota1.bin",url2="http://www.example.com/fota2.bin")
```



##### 分步升级接口，写入升级包数据流

> **fota_obj.write(bytesData, file_size)**

写入升级包数据流。

* 参数

| 参数      | 参数类型 | 参数说明                     |
| --------- | -------- | ---------------------------- |
| bytesData | bytes    | 升级包文件数据               |
| file_size | int      | 升级包文件总大小(单位：字节) |

* 返回值

写入成功返回整型值0，写入失败返回值整型值-1。

* 注意

  目前支持平台：EC600S/EC600N/EC800N/EC600U/EC200U。


##### 分步升级接口，刷新缓存数据到flash

> **fota_obj.flush()**

刷新缓存数据到flash

- 参数

无

- 返回值

刷新成功返回整型值0，刷新失败返回整型值-1。

* 注意

  目前支持平台：EC600S/EC600N/EC800N/EC600U/EC200U。


##### 分步升级接口，数据校验

> **fota_obj.verify()**

数据校验。

* 参数

无

* 返回值

检验成功返回整型值0，校验失败返回整型值-1。

* 注意

  目前支持平台：EC600S/EC600N/EC800N/EC600U/EC200U。
  
* 示例

```python
>>> fota_obj.verify()
0
```

##### 设置FOTA下载APN

> fota_obj.apn_set(fota_apn=,ip_type=,fota_user=,fota_password=)

设置FOTA下载使用的APN信息。

* 参数

| 参数          | 参数类型 | 参数说明                                       |
| ------------- | -------- | ---------------------------------------------- |
| fota_apn      | str      | APN（可选择传不传入该参数）                    |
| ip_type       | int      | IP类型：0-IPV4，1-IPV6（可选择传不传入该参数） |
| fota_user     | str      | 用户名（可选择传不传入该参数）                 |
| fota_password | str      | 密码（可选择传不传入该参数）                   |

* 返回值

写入成功返回整型值0，写入失败返回值整型值-1。

* 示例

```python
>>> fota_obj.apn_set(fota_apn="CMNET",ip_type=0,fota_user="abc",fota_password="123")
0
```

* 注意

  目前支持平台：BG95。

##### 取消FOTA下载

> fota_obj.download_cancel()

取消正在进行的FOTA下载。

- 参数

无

* 返回值

取消成功返回整型值0，取消失败返回整型值-1。

* 示例

```python
import fota
import _thread
import utime

def th_func():
    utime.sleep(40) #时间根据下载包的大小来定，确保在下载完之前取消
    fota_obj.download_cancel()

def result(args):
    print('download status:',args[0],'download process:',args[1])

fota_obj = fota()
_thread.start_new_thread(th_func, ())
fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)
```

* 注意

  目前支持平台：BG95。



##### 使用示例

###### 一键升级接口

```python
#下载完自动重启

import fota
import utime
import log

# 设置日志输出级别
log.basicConfig(level=log.INFO)
fota_log = log.getLogger("Fota")

# 此示例需要升级包文件（差分包等.bin文件）。
def result(args):
    print('download status:',args[0],'download process:',args[1])
    
def run():
    fota_obj = fota()  # 创建Fota对象
    fota_log.info("httpDownload...")
    #差分升级、全量升级    
    res = fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)    
    #最小系统升级
    #res = fota_obj.httpDownload(url1="http://www.example.com/fota1.bin",url2="http://www.example.com/fota2.bin")
    if res != 0:
        fota_log.error("httpDownload error")
        return
    fota_log.info("wait httpDownload update...")
    utime.sleep(2)

if __name__ == '__main__':
    fota_log.info("run start...")
    run()    
```

```python
# 下载完不自动重启(EC600S/EC600N/EC800N/平台不支持)

# EC200A/EC200U平台/BG95平台：
import fota
from misc import Power
fota_obj = fota(reset_disable=1)
def result(args):
    print('download status:',args[0],'download process:',args[1])
fota_obj.httpDownload(url1="http://www.example.com/dfota.bin",callback=result) #期望下载完不重启
Power.powerRestart() #手动重启进行升级
```



###### 分步升级接口

- 注意

  目前支持平台：EC600S/EC600N/EC800N/EC600U/EC200U。

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

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Fota_example"
PROJECT_VERSION = "1.0.0"

# 设置日志输出级别
log.basicConfig(level=log.INFO)
fota_log = log.getLogger("Fota")

# 此示例需要升级包文件（差分包等.bin文件），且存放到文件系统中

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
	
    fota_log.info("fota image flush...")
    res = fota_obj.flush()  # 刷新
    if res != 0:
        fota_log.error("flush error")
        return
    fota_log.info("fota image verify...")
    res = fota_obj.verify()  # 校验
    if res != 0:
        fota_log.error("verify error")
        return
    fota_log.info("power_reset...")
    utime.sleep(2)
    Power.powerRestart()   # 重启模块


if __name__ == '__main__':
    fota_log.info("run start...")
    run()

```



#### app_fota - 用户文件升级

模块功能：用户文件升级


##### 创建app_fota对象

1. 导入app_fota模块
2. 调用`new`方法创建app_fota对象

```python
import app_fota
fota = app_fota.new()
```



##### 下载单个文件

> **fota.download(url, file_name)**

 - 参数

| 参数      | 参数类型 | 参数说明                 |
| --------- | -------- | ------------------------ |
| url       | str      | 待下载文件的url          |
| file_name | str      | 本地待升级文件的绝对路径 |


 - 返回值

成功返回0，否则返回-1。



##### 下载批量文件

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



##### 设置升级标志

> **fota.set_update_flag()**

 - 参数
   无

 - 返回值
   无

> 设置完成升级标志后，调用重启接口，重启后即可启动升级工作。
> 升级完成后会直接进入应用程序。

> 重启接口参考链接：https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=%e6%a8%a1%e5%9d%97%e9%87%8d%e5%90%af



#### audio - 音频播放

模块功能：音频播放，支持TTS、mp3以及AMR文件播放。

注意：BC25PA平台不支持此模块。

##### TTS 

###### 创建TTS对象

> **import audio**
>
> **tts = audio.TTS(device)**

* 参数

| 参数   | 参数类型 | 参数说明                                       |
| ------ | -------- | ---------------------------------------------- |
| device | int      | 输出通道<br>0 - 听筒<br/>1 - 耳机<br/>2 - 喇叭 |

* 示例

```python
>>> import audio
>>> tts = audio.TTS(1)
```



###### 关闭TTS功能

> **tts.close()**

关闭TTS功能。

* 参数

  无

* 返回值

  成功返回整型0，失败返回整型-1。



###### 开始TTS播放

> **tts.play(priority, breakin, mode, str)**

语音播放，支持优先级0 ~ 4，数字越大优先级越高，每个优先级组可同时最多加入10个播放任务；播放策略说明如下：

1. 如果当前正在播放任务A，并且允许被打断，此时有高优先级播放任务B，那么会打断当前低优先级播放任务A，直接播放高优先级任务B；

2. 如果当前正在播放任务A，并且不允许被打断，此时有高优先级播放任务B，那么B播放任务将会加入到播放队列中合适的位置，等待A播放完成，再依次从队列中按照优先级从高到低播放其他任务；

3. 如果当前正在播放任务A，且不允许被打断，此时来了一个同优先级播放任务B，那么B会被加入到该优先级组播放队列队尾，等待A播放完成，再依次从队列中按照优先级从高到低播放其他任务；

4. 如果当前正在播放任务A，且允许被打断，此时来了一个同优先级播放任务B，那么会打断当前播放任务A，直接播放任务B；

5. 如果当前正在播放任务A，且任务A的优先级组播放队列中已经有几个播放任务存在，且该优先级组播放队列最后一个任务N是允许被打断的，此时如果来了一个同样优先级的播放任务B，那么任务B会直接覆盖掉任务N；也就是说，某个优先级组，只有最后一个元素是允许被打断的，即breakin为1，其他任务都是不允许被打断的；

6. 如果当前正在播放任务A，不管任务A是否允许被打断，此时来了一个优先级低于任务A的请求B，那么将B加入到B对应优先级组播放队列。

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| priority | int      | 播放优先级，支持优先级0 ~ 4，数值越大优先级越高                |
| breakin  | int      | 打断模式，0表示不允许被打断，1表示允许被打断                 |
| mode     | int      | 低四位：编码模式，1 - UNICODE16(UTF-16大端模式)，2 - UTF-8，3 - UNICODE16(UTF-16小端模式)<br>高四位：WTTS模式（仅600N系列支持VOLTE的版本支持）, wtts_enable - wtts总开关，wtts_ul_enable - wtts上行使能， wtts_dl_enable - wtts下行使能 |
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

#播放UTF16BE模式的语音
>>> tts.play(1,1,1,'6B228FCE4F7F752879FB8FDC901A4FE16A2157573002')
0

#播放UTF16LE模式的语音
>>> tts.play(1,1,3,'226BCE8F7F4F2875FB79DC8F1A90E14F216A57570230')
0

#支持VOLTE的版本,可以播放tts到远端
>>> import voiceCall
>>> voiceCall.callStart('1xxxxxxxxxx')
0

#待电话接通后
#播放tts语音至通话远端
>>> tts.play(1,1,tts.wtts_enable|tts.wtts_ul_enable|2, '12345')

0
```

tts播放中文示例：

注意，python文件开头需要加上“# -*- coding: UTF-8 -*-”。

```python
# -*- coding: UTF-8 -*-
import audio

tts = audio.TTS(1)
str1 = '移联万物，志高行远' 
tts.play(4, 0, 2, str1)
```



tts播放文本标注说明：

如遇TTS播放时不能达到预期的，可以通过文本标注的方式让TTS播放符合预期。

数字播放的方式：

```python
#格式：[n*] (*=0/1/2)
#TTS引擎自动决定是以号码形式播放还是以数值的形式播放
>>> tts.play(1,1,2, '12345')
0

#TTS引擎以号码形式播放
>>> tts.play(1,1,2, '[n1]12345')
0

#TTS引擎以数值形式播放
>>> tts.play(1,1,2, '[n2]12345')
0
```



语速设置：

```python
#格式：[s*] (*=0 ~ 10)
#TTS引擎以默认语速5播放语音
>>> tts.play(1,1,2, '12345')
0

#TTS引擎以默认语速的一半播放语音
>>> tts.play(1,1,2, '[s0]12345')
0

#TTS引擎以默认语速的2倍语速播放语音
>>> tts.play(1,1,2, '[s10]12345')
0
```



语调设置：

```python
#格式：[t*] (*=0 ~ 10)
#TTS引擎以默认语调5播放语音
>>> tts.play(1,1,2, '12345')
0

#TTS引擎以默认语调基频减64Hz播放语音
>>> tts.play(1,1,2, '[t0]12345')
0

#TTS引擎以默认语调基频加128Hz播放语音
>>> tts.play(1,1,2, '[t10]12345')
0
```



汉字指定拼音：

```python
#格式：[=*] (*=拼音)
#汉字：声调用后接一位数字 1 ~ 5 分别表示阴平、阳平、上声、去声和轻声 5 个声调。
>>> tts.play(1,1,2, '乐[=le4]')
0

>>> tts.play(1,1,2, '乐[=yue4]')
0
```



###### 停止TTS播放

> **tts.stop()**

停止TTS播放。

* 参数

  无

* 返回值

  成功返回整型0，失败返回整型-1。



###### 停止队列播放

> **tts.stopAll()**

停止整个队列的播放，即当前如果正在播放TTS或者音频，并且队列中还有其他待播放内容，调用该接口后，不仅会停止当前播放的内容，还会清除这个队列的内容，不再播放任何内容。如果当前正在播放，且播放队列为空，那么调用该接口效果等同与stop()接口。

* 参数

  无

* 返回值

  成功返回整型0，失败返回整型-1。



###### 注册回调函数

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



###### 获取TTS音量大小

> **tts.getVolume()**

获取当前播放音量大小，音量值为0 ~ 9，0表示静音，默认值4。

* 参数

  无

* 返回值

  成功返回整型音量大小值，失败返回整型-1。

* 示例

```python
>>> tts.getVolume()
4
```



###### 设置TTS音量大小

> **tts.setVolume(vol)**

设置播放音量大小。

* 参数

| 参数 | 参数类型 | 参数说明                       |
| ---- | -------- | ------------------------------ |
| vol  | int      | 音量值，音量值为0 ~ 9，0表示静音 |

* 返回值

  成功返回0，失败返回整型-1。

* 示例

```python
>>> tts.setVolume(6)
0
```



###### 获取播放速度

> **tts.getSpeed()**

获取当前播放速度，速度值为0 ~ 9，值越大，速度越快，默认值4。

* 参数

  无

* 返回值

  成功返回当前播放速度，失败返回整型-1。

* 示例

```python
>>> tts.getSpeed()
4
```



###### 设置播放速度

> **tts.setSpeed(speed)**

设置TTS播放速度。

* 参数

| 参数  | 参数类型 | 参数说明                              |
| ----- | -------- | ------------------------------------- |
| speed | int      | 速度值，速度值为0 ~ 9，值越大，速度越快 |

* 返回值

  成功返回整型0，失败返回整型-1。

* 示例

```python
>>> tts.setSpeed(6)
0
```



###### 获取tts状态

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



###### 使用示例

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


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_TTS_example"
PROJECT_VERSION = "1.0.0"

# 设置日志输出级别
log.basicConfig(level=log.INFO)
tts_Log = log.getLogger("TTS")


if __name__ == '__main__':
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

###### 创建一个对象

> **import audio**
>
> **aud = audio.Audio(device)**

* 参数

| 参数   | 参数类型 | 参数说明                                       |
| ------ | -------- | ---------------------------------------------- |
| device | int      | 输出通道<br>0 - 听筒<br/>1 - 耳机<br/>2 - 喇叭 |

* 示例

```python
>>> import audio
>>> aud = audio.Audio(1)
```



###### 设置输出pa的gpio

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



###### 音频文件播放

> **aud.play(priority, breakin, filename)**

音频文件播放，支持mp3、amr和wav格式文件播放。支持优先级0 ~ 4，数字越大优先级越高，每个优先级组可同时最多加入10个播放任务，与TTS播放共用同一个播放队列。

* 参数

| 参数     | 参数类型 | 参数说明                                      |
| -------- | -------- | --------------------------------------------- |
| priority | int      | 播放优先级，支持优先级0 ~ 4，数值越大优先级越高 |
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



###### 停止音频文件播放

> **aud.stop()**

停止音频文件播放。

* 参数

  无

* 返回值

  成功返回整型0，失败返回整型-1。



###### 停止队列播放

> **aud.stopAll()**

停止整个队列的播放，即当前如果正在播放TTS或者音频，并且队列中还有其他待播放内容，调用该接口后，不仅会停止当前播放的内容，还会清除这个队列的内容，不再播放任何内容。如果当前正在播放，且播放队列为空，那么调用该接口效果等同与stop()接口。

* 参数

  无

* 返回值

  成功返回整型0，失败返回整型-1。



###### 注册回调函数

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



###### 获取audio初始化状态

> **aud.getState()**

获取audio初始化状态。

* 参数

  无

* 返回值

  audio初始化未完成返回整型值-1，初始化完成返回整型值0。



###### 获取audio音量大小

> **aud.getVolume()**

获取audio音量大小，默认值7。

* 参数

  无

* 返回值

  返回整型音量值。



###### 设置audio音量大小

> **aud.setVolume(vol)**

设置audio音量大小。

* 参数

| 参数 | 参数类型 | 参数说明                                   |
| ---- | -------- | ------------------------------------------ |
| vol  | int      | 音量等级，范围（1 ~ 11），数值越大，音量越大 |

* 返回值

  设置成功返回整型0，失败返回整型-1。

* 示例

```python
>>> aud.setVolume(6)
0
>>> aud.getVolume()
6
```



###### 音频流播放

> aud.playStream(format, buf)

音频流播放，支持mp3、amr和wav格式的音频流播放。

* 参数

| 参数   | 参数类型 | 参数说明                                                     |
| ------ | -------- | ------------------------------------------------------------ |
| format | int      | 音频流格式<br/>1- PCM（暂不支持）<br/>2 - WAVPCM<br/>3 - MP3<br/>4 - AMRNB |
| buf    | buf      | 音频流内容                                                   |

* 返回值

  播放成功返回整型0；

  播放失败返回整型-1；

  

###### 停止音频流播放

> audio_test.stopPlayStream()

停止音频流播放

* 参数

  无

* 返回值

  停止成功返回整型0；

  停止失败返回整型-1；


- 示例

  ```python
  import audio
  import utime
  
  audio_test = audio.Audio(0)
  
  size = 10*1024 # 保证一次填充的音频数据足够大以便底层连续播放
  format = 4
  
  def play_from_fs():
      file_size = uos.stat("/usr/test.amr")[6]  # 获取文件总字节数
      print(file_size)
      with open("/usr/test.amr", "rb")as f:   
          while 1:
              b = f.read(size)   # read
              if not b:
                  break
              audio_test.playStream(format, b)
              utime.sleep_ms(20)
  
  
  play_from_fs()
  utime.sleep_ms(5000) # 等待播放完成
  audio_test.stopPlayStream() # 停止本次播放以便不影响下次播放
  ```



###### Tone音播放

支持平台EC600U/EC200U/EC600N/EC800N

> aud.aud_tone_play(tone, time)

播放tone音，播放一段时间(time)后自动停止播放（注：EC600N/EC800N平台调用该接口为立即返回，EC600U/EC200U平台调用该接口为阻塞等待）

* 参数

| 参数 | 参数类型 | 参数说明                                                     |
| ---- | -------- | ------------------------------------------------------------ |
| tone | int      | tone类型<br/>0~15- 按键音(0~9、A、B、C、D、#、*)<br/>16 - 拨号音 |
| time | int      | 播放时长，单位ms<br/>0 - 不停止一直播放，只能调用aud.aud_tone_play_stop()接口才能停止（EC600N/EC800N平台持续时间无限，EC600U/EC200U平台持续大概2分钟后停止）<br/>大于0 - 播放时长time ms |

* 返回值

  播放成功返回整型0；

  播放失败返回整型-1；

  

###### 停止Tone音播放

> aud.aud_tone_play_stop()

主动停止播放tone音

* 参数

  无

* 返回值

  停止成功返回整型0；

  停止失败返回整型-1；




- 示例

```python
import audio
import utime

aud = audio.Audio(0)

# EC600U/EC200U平台
def dial_play_ec600u():
    for i in range(0,10):
        aud.aud_tone_play(16, 1000)
        utime.sleep(1)

# EC600N/EC800N平台
def dial_play_ec600n():
    for i in range(0,10):
        aud.aud_tone_play(16, 1000)
        utime.sleep(2)
        
# dial_play_ec600n()
dial_play_ec600u()
```



##### Record

注意：BC25PA平台不支持此模块。

###### 创建一个对象

> **import audio**
>
> **record = audio.Record(device)**

不带参数时，默认使用听筒播放；带参数时，设置播放的设备。

注意：带参数时，参数应与audio.audio()设置的参数一致。

* 参数

| 参数   | 参数类型 | 参数说明                                        |
| ------ | -------- | ----------------------------------------------- |
| device | int      | 输出通道<br/>0 - 听筒<br/>1 - 耳机<br/>2 - 喇叭 |

* 返回值

  返回 *-1* 表示创建失败； 若返回对象，则表示创建成功 。

* 示例

```python
import audio 
record_test = audio.Record()#不传参数，使用听筒播放
```



###### 开始录音

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

  -3： 文件正在使用

  -4：通道设置错误

  -5：定时器资源申请失败

  -6 ：音频格式检测错误

* 示例

```python
record_test.start("test.wav",40)	#录制wav格式
record_test.start("test.amr",40)	#录制amr格式
record_test.start("test",40)	#录制amr格式
```



###### 停止录音

> **record.stop()**

停止录音。

* 参数

  无

* 返回值

  成功返回整型0，失败返回整型-1。

* 示例

```python
record_test.stop()
```



###### 读取录音文件存放路径

> **record. getFilePath(file_name)**

读取录音文件的路径。

* 参数

| 参数      | 参数类型 | 参数说明   |
| --------- | -------- | ---------- |
| file_name | str      | 录音文件名 |

* 返回值

  成功返回string类型的录音文件路径，目标文件不存在返回整型-1，文件名长度为0返回整型-2。

* 示例

```python
record_test.getFilePath(“test.wav”)
```



###### 读取录音数据

> **record.getData(file_name，offset, size)**

读取录音数据。

* 参数

| 参数      | 参数类型 | 参数说明                       |
| --------- | -------- | ------------------------------ |
| file_name | str      | 录音文件名                     |
| offset    | int      | 读取数据的偏移量               |
| size      | int      | 读取大小，单位字节 ：需小于10K |

* 返回值

  成功返回录音数据，bytearray类型；

  失败返回值说明如下：

  -1：读取数据错误

  -2：文件打开失败

  -3：偏移量设置错误

  -4：文件正在使用

  -5：设置超出文件大小（offset+size > file_size）

  -6：读取size 大于10K

  -7： 内存不足10K

* 示例

```python
record_test.getData(“test.amr”,0, 44) 
```



###### 读取录音文件大小

> **record.getSize(file_name)**

读取录音文件大小。

* 参数

| 参数      | 参数类型 | 参数说明   |
| --------- | -------- | ---------- |
| file_name | str      | 录音文件名 |

* 返回值

  若获取成功,返回文件大小 （asr平台不返回文件头），单位字节：

  wav格式时，此值会比返回callback返回值大44 bytes（44 bytes为文件头）；

  amr格式时，此值会比返回callback返回值大6 bytes（6 bytes为文件头）；

  失败返回值如下： 

  -1：获取文件大小失败 ； 

  -2：文件打开失败 ； 

  -3：文件正在使用 ；

  -4：文件名长度为0；

* 示例

```python
record_test.getSize(“test.amr”)
```



###### 删除录音文件

> **record.Delete(file_name)**

删除录音文件。

* 参数

| 参数      | 参数类型 | 参数说明   |
| --------- | -------- | ---------- |
| file_name | str      | 录音文件名 |

* 返回值

   0：成功

  -1：文件不存在 

  -2：文件正在使用

* 示例

```python
record_test.Delete(“test.amr”)
```



###### 判断录音文件是否存在

> **record.exists(file_name)**

判断录音文件是否存在。

* 参数

| 参数     | 参数类型 | 参数说明   |
| -------- | -------- | ---------- |
| ile_name | str      | 录音文件名 |

* 返回值

  true：文件存在

  false：文件不存在

  -1：文件名长度为0

* 示例

```python
record_test.exists(“test.amr”)
```



###### 判断是否正在录音

> **record.isBusy()**

判断是否正在录音

* 参数

  无

* 返回值

  0：idle

  1：busy

* 示例

```python
record_test.isBusy()
```



###### 注册录音结束回调

> **record.end_callback(callback)**

设置录音结束回调

* 参数

| 参数     | 参数类型 | 参数说明 |
| -------- | -------- | -------- |
| callback | function | 回调函数 |

* 返回值

  设置成功返回整型0，失败返回整型-1。

* 示例

```python
def record_callback(para): 
	print("file_name:",para[0])   # 返回文件路径 
    print("audio_len:",para[1])   # 返回录音长度 
    print("audio_state:",para[2])  
    # 返回录音状态 -1: error 0:start 3:  成功 
record_test.end_callback(record_callback)
```

关于录音回调函数中para[2]，即录音状态的说明：

| event | 说明     |
| ----- | -------- |
| -1    | 发生错误 |
| 0     | 录音开始 |
| 3     | 录音结束 |



###### 设置录音增益

目前仅600N/800N平台支持该功能。

> **record.gain(code_gain,dsp_gain)**

设置录音增益。

* 参数

| 参数      | 参数类型 | 参数说明               |
| --------- | -------- | ---------------------- |
| code_gain | int      | 上行编解码器增益 [0,4] |
| dsp_gain  | int      | 上行数字增益 [-36,12]  |

* 返回值

  设置成功返回整型0，失败返回整型-1。

* 示例

```python
record_test.gain(4,12)
```



###### 配置amr录音DTX功能开关

目前仅600N/800N平台支持该功能。

> **record.amrEncDtx_enable(on_off)**

配置amr录音DTX功能开关

- 参数

| 参数   | 参数类型 | 参数说明                                           |
| ------ | -------- | -------------------------------------------------- |
| on_off | int      | 1: 开启DTX <br>0: 关闭DTX   <br>不传：获取当前配置 |

- 返回值

  不传参：返回当前配置

  传参：参数正确无返回，参数错误抛异常

- 示例

```python
record_test.amrEncDtx_enable(1)
```



###### 录音流

目前仅EC200U/EC600U平台支持。

> **record.stream_start(format, samplerate, time)**

录音音频流

* 参数

| 参数       | 参数类型 | 参数说明                    |
| ---------- | -------- | --------------------------- |
| format     | int      | 音频格式，目前支持 amr 格式 |
| samplerate | int      | 采样率，目前支持8K 和 16K   |
| time       | int      | 录音时长，单位 S (秒)       |

* 返回值

  成功返回整型0，失败返回整型-1。

* 示例

```python
record_test.stream_start(record_test.AMRNB, 8000, 5)
```

注意：录制音频流的同时，应及时读取音频流。目前是采用循环buf,不及时读取，会导致数据丢失



###### 读取录音流

目前仅EC200U/EC600U平台支持。

> **record.stream_read(read_buf, len)**

录音音频流

* 参数

| 参数     | 参数类型 | 参数说明      |
| -------- | -------- | ------------- |
| read_buf | buf      | 录音流保存buf |
| len      | int      | 读取的长度    |

* 返回值

  成功返回实际读取的字节数，失败返回整型-1。

* 示例

```python
read_buf = bytearray(128)
record_test.stream_read(read_buf, 128)
```

###### 录音流示例

```python
import audio
import utime
record_test = audio.Record()
audio_test = audio.Audio(0)

read_time = 5

buf = bytearray(0)

def stream_rec_cb(para):
    global buf
    if(para[0] == 'stream'):
        if(para[2] == 1):
            read_buf = bytearray(para[1])
            record_test.stream_read(read_buf,para[1])
            buf += read_buf
            del read_buf
        elif (para[2] == 3):
            audio_test.stopPlayStream()
            audio_test.playStream(record_test.AMRNB, buf)



record_test.end_callback(stream_rec_cb)
audio_test.stopPlayStream()
record_test.stream_start(record_test.AMRNB, 8000, read_time)
```



###### 使用示例

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
        aud.play(1, 0, record.getFilePath(path))
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

###### 模块关机

> **from misc import Power**
>
> **Power.powerDown()**

模块关机。

* 参数

无

* 返回值

无



###### 模块重启

> **Power.powerRestart()**

模块重启。

* 参数

无

* 返回值

无



###### 获取模块开机原因

> **Power. powerOnReason()**

获取模块启动原因。

* 参数

无

* 返回值

返回整形数值，表示开机原因，解释如下：

| 值   | 说明                             |
| ---- | -------------------------------- |
| 0    | 获取开机原因失败或者开机原因未知 |
| 1    | 按 PWRKEY 开机                   |
| 2    | 按 RESET 重启                    |
| 3    | VBAT 触发的开机                  |
| 4    | RTC 定时开机                     |
| 5    | watchdog 触发重启或异常开机      |
| 6    | VBUS 触发的开机                  |
| 7    | 充电开机                         |
| 8    | PSM 唤醒开机                     |
| 9    | 发生 Dump 后重启                 |



###### 获取模块上次关机原因

> **Power. powerDownReason()**

获取模块上次关机原因。

* 参数

无

* 返回值

返回整形数值，表示上次关机原因，解释如下：

| 值   | 说明                  |
| ---- | --------------------- |
| 0    | 原因未知              |
| 1    | 正常关机              |
| 2    | 供电电压过高导致关机  |
| 3    | 供电电压过低导致关机  |
| 4    | 温度过高导致关机      |
| 5    | 看门狗触发的关机      |
| 6    | VRTC 电压过低触发关机 |

* 注意

BC25PA平台和EC200U/EC600U平台不支持此方法。



###### 获取电池电压

> **Power. getVbatt()**

获取电池电压，单位mV。

* 参数

无

* 返回值

返回整形电压值。

* 示例

```python
>>> Power.getVbatt()
3590
```



##### PowerKey

提供power key按键回调注册功能接口。

###### 创建PowerKey对象

> from misc import PowerKey
>
> pk = PowerKey()

* 参数

  无

* 返回值

  返回一个对象




###### 注册回调函数

> pk.powerKeyEventRegister(usrFun)

* 参数

| 参数   | 参数类型 | 参数说明                                    |
| ------ | -------- | ------------------------------------------- |
| usrFun | function | 回调函数，按下或松开power key按键时触发回调 |

* 返回值

  注册成功返回整型0，失败返回整型-1。

* 注意

  EC600S/EC600N等ASR平台，对于powerkey，按下和松开时，都会触发用户注册的回调函数；

  EC200U/EC600U等展锐平台，对于powerkey，只在按键松开时才会触发回调函数，并且按键按下的时间需要维持500ms以上。

* 示例

  EC600S/EC600N平台：

```python
from misc import PowerKey

pk = PowerKey()

def pwk_callback(status):
	if status == 0:
		print('powerkey release.')
	elif status == 1:
		print('powerkey press.')
        
pk.powerKeyEventRegister(pwk_callback)
```

​		EC200U/EC600U平台：

```python
from misc import PowerKey

pk = PowerKey()

def pwk_callback(status):
	if status == 0: # 只有按键释放时才会触发回调
		print('powerkey release.')

pk.powerKeyEventRegister(pwk_callback)
```



##### PWM

注意：BC25PA平台不支持此模块。

###### 常量说明

| 常量     | 说明 | 使用平台                                                     |
| -------- | ---- | ------------------------------------------------------------ |
| PWM.PWM0 | PWM0 | EC600S / EC600N / EC100Y/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N |
| PWM.PWM1 | PWM1 | EC600S / EC600N / EC100Y/EC800N/EC600M/EC800M/EG912N         |
| PWM.PWM2 | PWM2 | EC600S / EC600N / EC100Y/EC800N/EC600M/EC800M/EG912N         |
| PWM.PWM3 | PWM3 | EC600S / EC600N / EC100Y/EC800N/EC600M/EC800M/EG912N         |



###### 创建一个pwm对象

> **from misc import PWM**
>
> **pwm = PWM(PWM.PWMn,PWM.ABOVE_xx, highTime, cycleTime)**

* 参数

| 参数      | 参数类型 | 参数说明                                                     |
| --------- | -------- | ------------------------------------------------------------ |
| PWMn      | int      | PWM号<br/>注：EC100YCN平台，支持PWM0-PWM3，对应引脚如下：<br/>PWM0 – 引脚号19<br/>PWM1 – 引脚号18<br/>PWM2 – 引脚号23<br/>PWM3 – 引脚号22<br/>注：EC600SCN/EC600N平台，支持PWM0-PWM3，对应引脚如下：<br/>PWM0 – 引脚号52<br/>PWM1 – 引脚号53<br/>PWM2 – 引脚号70<br/>PWM3 – 引脚号69<br />注：EC800N平台，支持PWM0-PWM3，对应引脚如下：<br/>PWM0 – 引脚号79<br/>PWM1 – 引脚号78<br/>PWM2 – 引脚号16<br/>PWM3 – 引脚号49<br />注：EC200UCN平台，支持PWM0，对应引脚如下：<br />PWM0 – 引脚号135<br />注：EC600UCN平台，支持PWM0，对应引脚如下：<br />PWM0 – 引脚号70<br />注：EC600M平台，支持PWM0-PWM3，对应引脚如下：<br/>PWM0 – 引脚号57<br/>PWM1 – 引脚号56<br/>PWM2 – 引脚号70<br/>PWM3 – 引脚号69<br/>注：EG915U平台，支持PWM0，对应引脚如下：<br/>PWM0 – 引脚号20<br/>注：EC800M平台，支持PWM0-PWM3，对应引脚如下：<br/>PWM0 – 引脚号83<br/>PWM1 – 引脚号78<br/>PWM2 – 引脚号16<br/>PWM3 – 引脚号49<br/>注：EG912N平台，支持PWM0-PWM3，对应引脚如下：<br/>PWM0 – 引脚号21<br/>PWM1 – 引脚号116<br/>PWM2 – 引脚号107<br/>PWM3 – 引脚号92 |
| ABOVE_xx  | int      | EC600SCN/EC600N/EC800N/EC600M/EC800M/EG912N平台:<br />PWM.ABOVE_MS				ms级取值范围：(0,1023]<br/>PWM.ABOVE_1US				us级取值范围：(0,157]<br/>PWM.ABOVE_10US				us级取值范围：(1,1575]<br/>PWM.ABOVE_BELOW_US			ns级 取值(0,1024]<br />EC200U/EC600U/EG915U平台:<br />PWM.ABOVE_MS				ms级取值范围：(0,10]<br/>PWM.ABOVE_1US				us级取值范围：(0,10000]<br/>PWM.ABOVE_10US				us级取值范围：(1,10000]<br/>PWM.ABOVE_BELOW_US			ns级 取值[100,65535] |
| highTime  | int      | ms级时，单位为ms<br/>us级时，单位为us<br/>ns级别：需要使用者计算<br/>               频率 = 13Mhz / cycleTime<br/>               占空比 = highTime/ cycleTime |
| cycleTime | int      | ms级时，单位为ms<br/>us级时，单位为us<br/>ns级别：需要使用者计算<br/>             频率 = 13Mhz / cycleTime<br/>             占空比 = highTime/ cycleTime |

* 示例

```python
>>> from misc import PWM
>>> pwm1 = PWM(PWM.PWM1, PWM.ABOVE_MS, 100, 200)
```



###### 开启PWM输出

> **pwm.open()**

开启PWM输出。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。



###### 关闭PWM输出

> **pwm.close()**

关闭PWM输出。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。



###### 使用示例

```python
# PWM使用示例

from misc import PWM
import utime


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_PWM_example"
PROJECT_VERSION = "1.0.0"

'''
* 参数1：PWM号
        注：EC100YCN平台，支持PWM0 ~ PWM3，对应引脚如下：
        PWM0 – 引脚号19
        PWM1 – 引脚号18
        PWM2 – 引脚号23
        PWM3 – 引脚号22

        注：EC600SCN平台，支持PWM0 ~ PWM3，对应引脚如下：
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
    pwm = PWM(PWM.PWM0, PWM.ABOVE_MS, 100, 200)  # 初始化一个pwm对象
    pwm.open()  # 开启PWM输出
    utime.sleep(10)
    pwm.close()  # 关闭pwm输出
```



##### ADC

###### 常量说明

| 常量     | 说明     | 适用平台                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| ADC.ADC0 | ADC通道0 | EC600S/EC600N/EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC200A/EC600M/EG915U/EC800M/EG912N |
| ADC.ADC1 | ADC通道1 | EC600U/EC200U/EC200A/EC600M/EG915U/EC800M/EG912N             |
| ADC.ADC2 | ADC通道2 | EC600U/EC200U                                                |
| ADC.ADC3 | ADC通道3 | EC600U                                                       |



###### 创建一个ADC对象

> **from misc import ADC**
>
> **adc = ADC()**

* 示例

```python
>>> from misc import ADC
>>> adc = ADC()
```



###### ADC功能初始化

> **adc.open()**

ADC功能初始化。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。



###### 读取通道电压值

> **adc.read(ADCn)**

读取指定通道的电压值，单位mV。

* 参数

| 参数 | 参数类型 | 参数说明                                                     |
| ---- | -------- | ------------------------------------------------------------ |
| ADCn | int      | ADC通道<br/>EC100Y平台对应引脚如下<br/>ADC0 – 引脚号39<br/>ADC1 – 引脚号81<br/>EC600S/EC600N平台对应引脚如下<br/>ADC0 – 引脚号19<br/>EC600M平台对应引脚如下<br/>ADC0 – 引脚号19<br/>ADC1 – 引脚号20<br/>EC800N平台对应引脚如下<br/>ADC0 – 引脚号9<br/>EC600U平台对应引脚如下<br />ADC0 – 引脚号19<br/>ADC1 – 引脚号20<br />ADC2 – 引脚号113<br />ADC3 – 引脚号114<br />EC200U平台对应引脚如下<br />ADC0 – 引脚号45<br/>ADC1 – 引脚号44<br />ADC2 – 引脚号43<br />EC200A平台对应引脚如下<br/>ADC0 – 引脚号45<br/>ADC1 – 引脚号44<br/>BG95M3平台对应引脚如下<br/>ADC0 – 引脚号24<br/>EG915U平台对应引脚如下<br/>ADC0 – 引脚号24<br/>ADC1 – 引脚号2<br/>EC800M平台对应引脚如下<br/>ADC0 – 引脚号9<br/>ADC1 – 引脚号96<br/>EG912N平台对应引脚如下<br/>ADC0 – 引脚号24<br/>ADC1 – 引脚号2 |

* 返回值

成功返回指定通道电压值，错误返回整型-1。

* 示例

```python
>>>adc.read(ADC.ADC0)  #读取ADC通道0电压值
613
>>>adc.read(ADC.ADC1)  #读取ADC通道1电压值
605
```



###### 关闭ADC

> **adc.close()**

关闭ADC。

* 参数

无

* 返回值

0关闭成功，-1关闭失败。



##### USB

提供USB插拔检测接口。

注意：当前仅EC600S/EC600N/EC800N/EC200U/EC600U平台支持该功能。

###### 创建USB对象

> from misc import USB
>
> usb = USB()

* 参数

  无

* 返回值

  无

  

###### 获取当前USB连接状态

> usb.getStatus()

* 参数

  无

* 返回值

  -1 - 获取状态失败

  0 - USB当前没有连接

  1 - USB已连接



###### 注册回调函数

> usb.setCallback(usrFun)

* 参数

| 参数   | 参数类型 | 参数说明                                                     |
| ------ | -------- | ------------------------------------------------------------ |
| usrFun | function | 回调函数，当USB插入或者拔出时，会触发回调来通知用户当前USB状态。注意：回调函数中不要进行阻塞性的操作。 |

* 返回值

  注册成功返回整型0，失败返回整型-1。

* 示例

```python
from misc import USB

usb = USB()

def usb_callback(conn_status):
	status = conn_status
	if status == 0:
		print('USB is disconnected.')
	elif status == 1:
		print('USB is connected.')
usb.setCallback(usb_callback)
```



##### USBNET

提供USB网卡功能

注意：当前仅EC600S/EC600N/EC800N/EC200U/EC600U平台支持该功能。

###### 设置USB网卡工作类型（重启生效）

> **USBNET.set_worktype(type)**

- 参数

  | 参数 | 参数类型 | 参数说明                                                     |
  | ---- | -------- | ------------------------------------------------------------ |
  | type | int      | USBNET 工作类型<br>Type_ECM – ECM 模式<br>Type_RNDIS – RNDIS模式 |

- 返回值

  设置成功返回整型0，失败返回整型-1。
  
  

###### 获取USB网卡工作类型（重启生效）

> **USBNET.get_worktype()**

* 参数

  无

* 返回值

  成功返回当前网卡模式，失败返回整型-1。返回值说明：
  
  1 - ECM模式
  
  3 - RNDIS模式



###### 获取USBNET当前状态

> **USBNET.get_status()**

* 参数

  无

* 返回值

  成功返回USBNET当前状态，失败返回整型-1。

  状态说明：

  0 - 未连接

  1 - 连接成功



###### 打开USB网卡

> **USBNET.open()**

- 参数

  无

- 返回值

  打开成功返回整型0，失败返回整型-1。



###### 关闭USB网卡

> **USBNET.close()**

- 参数

  无

- 返回值

  成功返回整型0，失败返回整型-1。



示例

```python
from misc import USBNET
from misc import Power

#work on ECM mode default
USBNET.open()

USBNET.set_worktype(USBNET.Type_RNDIS)

#reset the module
Power.powerRestart()


#After restart
from misc import USBNET

#work on RNDIS mode
USBNET.open()
```



###### 获取Nat使能情况

> **USBNET.getNat(simid, pid)**

获取某一路网卡的Nat使能情况（是否支持ipv6拨号）

（仅在EC200U/EC600U平台支持）

* 参数

| 参数  | 参数类型 | 参数说明                       |
| ----- | -------- | ------------------------------ |
| simid | int      | simid，范围：0/1 ，目前仅支持0 |
| pid   | int      | PDP索引, 展锐平台范围1-7       |

* 返回值

成功：返回Nat使能情况，整型0/1，0：使能，支持ipv6拨号；1：未使能，不支持ipv6拨号

失败：返回整型-1

* 示例

```python
from misc import USBNET
USBNET.getNat(0, 1)
0
```



###### Nat设置

> **USBNET.setNat(simid, pid, Nat)**

Nat设置，设置成功后重启生效（仅在EC200U/EC600U平台支持）
（USBNET.set_worktype()接口调用的时候会使对应的Nat值变为1，使得该pid无法IPV6拨号，所以在close USBnet后，可以使用该接口关闭NAT,使IPV6功能正常）

* 参数

| 参数  | 参数类型 | 参数说明                                           |
| ----- | -------- | -------------------------------------------------- |
| simid | int      | simid，范围：0/1，目前仅支持0                      |
| pid   | int      | PDP索引, 展锐平台范围1-7                           |
| Nat   | int      | Nat，范围：0/1；0：支持ipv6拨号；1：不支持ipv6拨号 |

* 返回值

设置成功返回整型0，设置失败返回整型-1

* 示例

```python
USBNET.setNat(0, 1, 0)
0
```



##### 分集天线配置接口

> **misc.antennaSecRXOffCtrl(\*args)**

分集天线配置、查询接口。（仅1803S平台支持该接口）

* 参数

  该接口为可变参形式：
    参数个数为0,查询：misc.antennaSecRXOffCtrl()
    参数个数为1，配置：misc.antennaSecRXOffCtrl(SecRXOff_set)
	
  |     参数      | 参数类型 | 参数说明                                              |
  |    ------     | -------- | ----------------------------------------------------- |
  | SecRXOff_set  | int      | 范围0/1, 0:不关闭分集天线 1:关闭分集天线              |

* 返回值

  查询：成功返回分集天线配置，失败返回整形值-1

  设置：成功返回整形0,失败返回整型值-1

* 示例

```python
import misc

misc.antennaSecRXOffCtrl()
0
misc.antennaSecRXOffCtrl(1)
0
misc.antennaSecRXOffCtrl()
1

```



#### modem - 设备相关

模块功能：设备信息获取。

##### 获取设备的IMEI

> **modem.getDevImei()**

获取设备的IMEI。

* 参数

  无

* 返回值

  成功返回string类型设备的IMEI，失败返回整型值-1。

* 示例

```python
>>> import modem
>>> modem.getDevImei()
'866327040830317'
```



##### 获取设备型号

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



##### 获取设备序列号

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



##### 获取固件版本号

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



##### 获取设备制造商ID

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

###### 常量说明

| 常量             | 适配平台                   | 说明      |
| ---------------- | ------------------------ | -------- |
| Pin.GPIO1        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO1    |
| Pin.GPIO2        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO2    |
| Pin.GPIO3        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO3    |
| Pin.GPIO4        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO4    |
| Pin.GPIO5        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO5    |
| Pin.GPIO6        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO6    |
| Pin.GPIO7        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO7    |
| Pin.GPIO8        | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO8    |
| Pin.GPIO9        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO9    |
| Pin.GPIO10       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO10   |
| Pin.GPIO11       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO11   |
| Pin.GPIO12       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO12   |
| Pin.GPIO13       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO13   |
| Pin.GPIO14       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO14   |
| Pin.GPIO15       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO15   |
| Pin.GPIO16       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO16   |
| Pin.GPIO17       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC800N/BC25PA/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO17   |
| Pin.GPIO18       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/EC800N/BC25PA/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO18   |
| Pin.GPIO19       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO19   |
| Pin.GPIO20       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO20   |
| Pin.GPIO21       | EC600S / EC600N/EC600U/EC200U/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO21   |
| Pin.GPIO22       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO22   |
| Pin.GPIO23       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO23   |
| Pin.GPIO24       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO24   |
| Pin.GPIO25       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO25   |
| Pin.GPIO26       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO26   |
| Pin.GPIO27       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO27   |
| Pin.GPIO28       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO28   |
| Pin.GPIO29       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO29   |
| Pin.GPIO30 | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO30 |
| Pin.GPIO31 | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO31 |
| Pin.GPIO32 | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO32 |
| Pin.GPIO33 | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO33 |
| Pin.GPIO34 | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO34 |
| Pin.GPIO35 | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO35 |
| Pin.GPIO36 | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO36 |
| Pin.GPIO37 | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO37 |
| Pin.GPIO38 | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG912N | GPIO38 |
| Pin.GPIO39 | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG912N | GPIO39 |
| Pin.GPIO40 | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG912N | GPIO40 |
| Pin.GPIO41 | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M | GPIO41 |
| Pin.GPIO42 | EC600U/EC200U/EC600M/EC800M | GPIO42 |
| Pin.GPIO43 | EC600U/EC200U/EC200A/EC600M/EC800M | GPIO43 |
| Pin.GPIO44 | EC600U/EC200U/EC200A/EC600M/EC800M | GPIO44 |
| Pin.GPIO45 | EC600U/EC200U/EC200A/EC600M | GPIO45 |
| Pin.GPIO46 | EC600U/EC200U/EC200A | GPIO46 |
| Pin.GPIO47 | EC200U/EC200A | GPIO47 |
| Pin.IN           | --                       | 输入模式 |
| Pin.OUT          | --                       | 输出模式 |
| Pin.PULL_DISABLE | --                       | 浮空模式 |
| Pin.PULL_PU      | --                       | 上拉模式 |
| Pin.PULL_PD      | --                       | 下拉模式 |



**GPIO对应引脚号说明**

文档中提供的GPIO引脚号对应的为模块外部的引脚编号，例如EC600S下GPIO1对应引脚号22，这里的引脚号22为模块外部的引脚编号。可参考提供的硬件资料查看模块外部的引脚编号。

###### 创建gpio对象

> **gpio = Pin(GPIOn, direction, pullMode, level)**

* 参数

| 参数      | 类型 | 说明                                                         |
| :-------- | :--- | ------------------------------------------------------------ |
| GPIOn     | int  | 引脚号<br />EC100YCN平台引脚对应关系如下（引脚号为外部引脚编号）：<br />GPIO1 – 引脚号22<br />GPIO2 – 引脚号23<br />GPIO3 – 引脚号38<br />GPIO4 – 引脚号53<br />GPIO5 – 引脚号54<br />GPIO6 – 引脚号104<br />GPIO7 – 引脚号105<br />GPIO8 – 引脚号106<br />GPIO9 – 引脚号107<br />GPIO10 – 引脚号178<br />GPIO11 – 引脚号195<br />GPIO12 – 引脚号196<br />GPIO13 – 引脚号197<br />GPIO14 – 引脚号198<br />GPIO15 – 引脚号199<br />GPIO16 – 引脚号203<br />GPIO17 – 引脚号204<br />GPIO18 – 引脚号214<br />GPIO19 – 引脚号215<br />EC600SCN/EC600NCN平台引脚对应关系如下（引脚号为模块外部引脚编号）：<br />GPIO1 – 引脚号10<br />GPIO2 – 引脚号11<br />GPIO3 – 引脚号12<br />GPIO4 – 引脚号13<br />GPIO5 – 引脚号14<br />GPIO6 – 引脚号15<br />GPIO7 – 引脚号16<br />GPIO8 – 引脚号39<br />GPIO9 – 引脚号40<br />GPIO10 – 引脚号48<br />GPIO11 – 引脚号58<br />GPIO12 – 引脚号59<br />GPIO13 – 引脚号60<br />GPIO14 – 引脚号61<br />GPIO15 – 引脚号62<br/>GPIO16 – 引脚号63<br/>GPIO17 – 引脚号69<br/>GPIO18 – 引脚号70<br/>GPIO19 – 引脚号1<br/>GPIO20 – 引脚号3<br/>GPIO21 – 引脚号49<br/>GPIO22 – 引脚号50<br/>GPIO23 – 引脚号51<br/>GPIO24 – 引脚号52<br/>GPIO25 – 引脚号53<br/>GPIO26 – 引脚号54<br/>GPIO27 – 引脚号55<br/>GPIO28 – 引脚号56<br/>GPIO29 – 引脚号57<br />GPIO30 – 引脚号2<br />GPIO31 – 引脚号66<br />GPIO32 – 引脚号65<br />GPIO33 – 引脚号67<br />GPIO34 – 引脚号64<br />GPIO35 – 引脚号4<br />GPIO36 – 引脚号31<br />GPIO37 – 引脚号32<br />GPIO38 – 引脚号33<br />GPIO39 – 引脚号34<br />GPIO40 – 引脚号71<br />GPIO41 – 引脚号72<br />EC600M平台引脚对应关系如下（引脚号为模块外部引脚编号）：<br />GPIO1 – 引脚号10<br />GPIO2 – 引脚号11<br />GPIO3 – 引脚号12<br />GPIO4 – 引脚号13<br />GPIO5 – 引脚号14<br />GPIO6 – 引脚号15<br />GPIO7 – 引脚号16<br />GPIO8 – 引脚号39<br />GPIO9 – 引脚号40<br />GPIO10 – 引脚号48<br />GPIO11 – 引脚号58<br />GPIO12 – 引脚号59<br />GPIO13 – 引脚号60<br />GPIO14 – 引脚号61<br />GPIO15 – 引脚号62<br/>GPIO16 – 引脚号63<br/>GPIO17 – 引脚号69<br/>GPIO18 – 引脚号70<br/>GPIO19 – 引脚号1<br/>GPIO20 – 引脚号3<br/>GPIO21 – 引脚号49<br/>GPIO22 – 引脚号50<br/>GPIO23 – 引脚号51<br/>GPIO24 – 引脚号52<br/>GPIO25 – 引脚号53<br/>GPIO26 – 引脚号54<br/>GPIO27 – 引脚号55<br/>GPIO28 – 引脚号56<br/>GPIO29 – 引脚号57<br />GPIO30 – 引脚号2<br />GPIO31 – 引脚号66<br />GPIO32 – 引脚号65<br />GPIO33 – 引脚号67<br />GPIO34 – 引脚号64<br />GPIO35 – 引脚号4<br />GPIO36 – 引脚号31<br />GPIO37 – 引脚号32<br />GPIO38 – 引脚号33<br />GPIO39 – 引脚号34<br />GPIO40 – 引脚号71<br />GPIO41 – 引脚号72<br />GPIO42 – 引脚号109<br />GPIO43 – 引脚号110<br />GPIO44 – 引脚号112<br />GPIO45 – 引脚号111<br/>EC600UCN平台引脚对应关系如下（引脚号为模块外部引脚编号）<br />GPIO1 – 引脚号61(不可与GPIO31同时为gpio)<br />GPIO2 – 引脚号58(不可与GPIO32同时为gpio)<br />GPIO3 – 引脚号34(不可与GPIO41同时为gpio)<br />GPIO4 – 引脚号60(不可与GPIO34同时为gpio)<br />GPIO5 – 引脚号69(不可与GPIO35同时为gpio)<br />GPIO6 – 引脚号70(不可与GPIO36同时为gpio)<br />GPIO7 – 引脚号123(不可与GPIO43同时为gpio)<br />GPIO8 – 引脚号118<br />GPIO9 – 引脚号9<br />GPIO10 – 引脚号1(不可与GPIO37同时为gpio)<br />GPIO11 – 引脚号4(不可与GPIO38同时为gpio)<br />GPIO12 – 引脚号3(不可与GPIO39同时为gpio)<br />GPIO13 – 引脚号2(不可与GPIO40同时为gpio)<br />GPIO14 – 引脚号54<br />GPIO15 – 引脚号57<br/>GPIO16 – 引脚号56<br/>GPIO17 – 引脚号12<br/>GPIO18 – 引脚号33(不可与GPIO42同时为gpio)<br/>GPIO19 – 引脚号124(不可与GPIO44同时为gpio)<br/>GPIO20 – 引脚号122(不可与GPIO45同时为gpio)<br/>GPIO21 – 引脚号121(不可与GPIO46同时为gpio)<br/>GPIO22 – 引脚号48<br/>GPIO23 – 引脚号39<br/>GPIO24 – 引脚号40<br/>GPIO25 – 引脚号49<br/>GPIO26 – 引脚号50<br/>GPIO27 – 引脚号53<br/>GPIO28 – 引脚号52<br/>GPIO29 – 引脚号51<br/>GPIO30 – 引脚号59(不可与GPIO33同时为gpio)<br/>GPIO31 – 引脚号66(不可与GPIO1同时为gpio)<br/>GPIO32 – 引脚号63(不可与GPIO2同时为gpio)<br/>GPIO33 – 引脚号67(不可与GPIO30同时为gpio)<br/>GPIO34 – 引脚号65(不可与GPIO4同时为gpio)<br/>GPIO35 – 引脚号137(不可与GPIO5同时为gpio)<br/>GPIO36 – 引脚号62(不可与GPIO6同时为gpio)<br/>GPIO37 – 引脚号98(不可与GPIO10同时为gpio)<br/>GPIO38 – 引脚号95(不可与GPIO11同时为gpio)<br/>GPIO39 – 引脚号119(不可与GPIO12同时为gpio)<br/>GPIO40 – 引脚号100(不可与GPIO13同时为gpio)<br/>GPIO41 – 引脚号120(不可与GPIO3同时为gpio)<br/>GPIO42 – 引脚号16(不可与GPIO18同时为gpio)<br/>GPIO43 – 引脚号10(不可与GPIO7同时为gpio)<br/>GPIO44 – 引脚号14(不可与GPIO19同时为gpio)<br/>GPIO45 – 引脚号15(不可与GPIO20同时为gpio)<br/>GPIO46 – 引脚号13(不可与GPIO21同时为gpio)<br/>EC200UCN平台引脚对应关系如下（引脚号为模块外部引脚编号）<br />GPIO1 – 引脚号27(不可与GPIO31同时为gpio)<br />GPIO2 – 引脚号26(不可与GPIO32同时为gpio)<br />GPIO3 – 引脚号24(不可与GPIO33同时为gpio)<br />GPIO4 – 引脚号25(不可与GPIO34同时为gpio)<br />GPIO5 – 引脚号13(不可与GPIO17同时为gpio)<br />GPIO6 – 引脚号135(不可与GPIO36同时为gpio)<br />GPIO7 – 引脚号136(不可与GPIO44同时为gpio)<br />GPIO8 – 引脚号133<br />GPIO9 – 引脚号3(不可与GPIO37同时为gpio)<br />GPIO10 – 引脚号40(不可与GPIO38同时为gpio)<br />GPIO11 – 引脚号37(不可与GPIO39同时为gpio)<br />GPIO12 – 引脚号38(不可与GPIO40同时为gpio)<br />GPIO13 – 引脚号39(不可与GPIO41同时为gpio)<br />GPIO14 – 引脚号5<br />GPIO15 – 引脚号141<br/>GPIO16 – 引脚号142<br/>GPIO17 – 引脚号121(不可与GPIO5同时为gpio)<br/>GPIO18 – 引脚号65(不可与GPIO42同时为gpio)<br/>GPIO19 – 引脚号64(不可与GPIO43同时为gpio)<br/>GPIO20 – 引脚号139(不可与GPIO45同时为gpio)<br/>GPIO21 – 引脚号126(不可与GPIO46同时为gpio)<br/>GPIO22 – 引脚号127(不可与GPIO47同时为gpio)<br/>GPIO23 – 引脚号33<br/>GPIO24– 引脚号31<br/>GPIO25 – 引脚号30<br/>GPIO26 – 引脚号29<br/>GPIO27 – 引脚号28<br/>GPIO28 – 引脚号1<br/>GPIO29 – 引脚号2<br/>GPIO30 – 引脚号4<br/>GPIO31 – 引脚号125(不可与GPIO1同时为gpio)<br/>GPIO32 – 引脚号124(不可与GPIO2同时为gpio)<br/>GPIO33 – 引脚号123(不可与GPIO3同时为gpio)<br/>GPIO34 – 引脚号122(不可与GPIO4同时为gpio)<br/>GPIO35 – 引脚号42<br/>GPIO36 – 引脚号119(不可与GPIO6同时为gpio)<br/>GPIO37 – 引脚号134(不可与GPIO9同时为gpio)<br/>GPIO38– 引脚号132(不可与GPIO10同时为gpio)<br/>GPIO39 – 引脚号131(不可与GPIO11同时为gpio)<br/>GPIO40 – 引脚号130(不可与GPIO12同时为gpio)<br/>GPIO41 – 引脚号129(不可与GPIO13同时为gpio)<br/>GPIO42 – 引脚号61(不可与GPIO18同时为gpio)<br/>GPIO43 – 引脚号62(不可与GPIO19同时为gpio)<br/>GPIO44 – 引脚号63(不可与GPIO7同时为gpio)<br/>GPIO45 – 引脚号66(不可与GPIO20同时为gpio)<br/>GPIO46 – 引脚号6(不可与GPIO21同时为gpio)<br/>GPIO47 – 引脚号23(不可与GPIO22同时为gpio)<br/>EC200A平台引脚对应关系如下（引脚号为模块外部引脚编号）<br/>GPIO1 – 引脚号27<br />GPIO2 – 引脚号26<br />GPIO3 – 引脚号24<br />GPIO4 – 引脚号25<br />GPIO5 – 引脚号5<br />GPIO6 – 引脚号135<br />GPIO7 – 引脚号136<br />GPIO9 – 引脚号3<br />GPIO10 – 引脚号40<br />GPIO11 – 引脚号37<br />GPIO12 – 引脚号38<br />GPIO13 – 引脚号39<br />GPIO18 – 引脚号65<br />GPIO19 – 引脚号64<br />GPIO20 – 引脚号139<br />GPIO22 – 引脚号127<br />GPIO28 – 引脚号1<br />GPIO29 – 引脚号2<br />GPIO30 – 引脚号4<br />GPIO35 – 引脚号42<br />GPIO36 – 引脚号119<br />GPIO43 – 引脚号62<br />GPIO44 – 引脚号63<br />GPIO45 – 引脚号66<br />GPIO46 – 引脚号6<br />GPIO47 – 引脚号23<br/>EC800NCN平台引脚对应关系如下（引脚号为模块外部引脚编号）<br />GPIO1 – 引脚号30<br />GPIO2 – 引脚号31<br />GPIO3 – 引脚号32<br />GPIO4 – 引脚号33<br />GPIO5 – 引脚号49<br />GPIO6 – 引脚号50<br />GPIO7 – 引脚号51<br />GPIO8 – 引脚号52<br />GPIO9 – 引脚号53<br />GPIO10 – 引脚号54<br />GPIO11 – 引脚号55<br />GPIO12 – 引脚号56<br />GPIO13 – 引脚号57<br />GPIO14 – 引脚号58<br />GPIO15 – 引脚号80<br/>GPIO16 – 引脚号81<br/>GPIO17 – 引脚号76<br/>GPIO18 – 引脚号77<br/>GPIO19 – 引脚号82<br/>GPIO20 – 引脚号83<br/>GPIO21 – 引脚号86<br/>GPIO22 – 引脚号87<br/>GPIO23 – 引脚号66<br/>GPIO24 – 引脚号67<br/>GPIO25 – 引脚号17<br/>GPIO26 – 引脚号18<br/>GPIO27 – 引脚号19<br/>GPIO28 – 引脚号20<br/>GPIO29 – 引脚号21<br />GPIO30 – 引脚号22<br />GPIO31 – 引脚号23<br />GPIO32 – 引脚号28<br />GPIO33 – 引脚号29<br />GPIO34 – 引脚号38<br />GPIO35 – 引脚号39<br />GPIO36 – 引脚号16<br />GPIO37 – 引脚号78<br />BC25PA平台引脚对应关系如下（引脚号为模块外部引脚编号）<br />GPIO1 – 引脚号3<br />GPIO2 – 引脚号4<br />GPIO3 – 引脚号5<br />GPIO4 – 引脚号6<br />GPIO5 – 引脚号16<br />GPIO6 – 引脚号20<br />GPIO7 – 引脚号21<br />GPIO8 – 引脚号22<br />GPIO9 – 引脚号23<br />GPIO10 – 引脚号25<br />GPIO11 – 引脚号28<br />GPIO12 – 引脚号29<br />GPIO13 – 引脚号30<br />GPIO14 – 引脚号31<br />GPIO15 – 引脚号32<br/>GPIO16 – 引脚号33<br/>GPIO17 – 引脚号2<br/>GPIO18 – 引脚号8<br/>BG95M3平台引脚对应关系如下（引脚号为模块外部引脚编号）<br />GPIO1 – 引脚号4<br />GPIO2 – 引脚号5<br />GPIO3 – 引脚号6<br />GPIO4 – 引脚号7<br />GPIO5 – 引脚号18<br />GPIO6 – 引脚号19<br />GPIO7 – 引脚号22<br />GPIO8 – 引脚号23<br />GPIO9 – 引脚号25<br />GPIO10 – 引脚号26<br />GPIO11 – 引脚号27<br />GPIO12 – 引脚号28<br />GPIO13 – 引脚号40<br />GPIO14 – 引脚号41<br />GPIO15 – 引脚号64<br/>GPIO16 – 引脚号65<br/>GPIO17 – 引脚号66<br />GPIO18 – 引脚号85<br />GPIO19 – 引脚号86<br />GPIO20 – 引脚号87<br />GPIO21 – 引脚号88<br />EG915U平台引脚对应关系如下（引脚号为模块外部引脚编号）：<br />GPIO1 – 引脚号4(不可与GPIO41同时为gpio)<br />GPIO2 – 引脚号5(不可与GPIO36同时为gpio)<br />GPIO3 – 引脚号6(不可与GPIO35同时为gpio)<br />GPIO4 – 引脚号7(不可与GPIO24同时为gpio)<br />GPIO5 – 引脚号18<br />GPIO6 – 引脚号19<br />GPIO7 – 引脚号1(不可与GPIO37同时为gpio)<br />GPIO8 – 引脚号38<br />GPIO9 – 引脚号25<br />GPIO10 – 引脚号26<br />GPIO11 – 引脚号27(不可与GPIO32同时为gpio)<br />GPIO12 – 引脚号28(不可与GPIO31同时为gpio)<br />GPIO13 – 引脚号40<br />GPIO14 – 引脚号41<br />GPIO15 – 引脚号64<br/>GPIO16 – 引脚号20(不可与GPIO30同时为gpio)<br/>GPIO17 – 引脚号21<br/>GPIO18 – 引脚号85<br/>GPIO19 – 引脚号86<br/>GPIO20 – 引脚号30<br/>GPIO21 – 引脚号88<br/>GPIO22 – 引脚号36(不可与GPIO40同时为gpio)<br/>GPIO23 – 引脚号37(不可与GPIO38同时为gpio)<br/>GPIO24 – 引脚号16(不可与GPIO4同时为gpio)<br/>GPIO25 – 引脚号39<br/>GPIO26 – 引脚号42(不可与GPIO27同时为gpio)<br/>GPIO27 – 引脚号78(不可与GPIO26同时为gpio)<br/>GPIO28 – 引脚号83(不可与GPIO33同时为gpio)<br/>GPIO29 – 引脚号84<br />GPIO30 – 引脚号92(不可与GPIO16同时为gpio)<br />GPIO31 – 引脚号95(不可与GPIO12同时为gpio)<br />GPIO32 – 引脚号97(不可与GPIO11同时为gpio)<br />GPIO33 – 引脚号98(不可与GPIO28同时为gpio)<br />GPIO34 – 引脚号104<br />GPIO35 – 引脚号105(不可与GPIO3同时为gpio)<br />GPIO36 – 引脚号106(不可与GPIO2同时为gpio)<br />GPIO37 – 引脚号108(不可与GPIO4同时为gpio)<br />GPIO38 – 引脚号111(不可与GPIO23同时为gpio)<br />GPIO39 – 引脚号114<br />GPIO40 – 引脚号115(不可与GPIO22同时为gpio)<br />GPIO41 – 引脚号116(不可与GPIO1同时为gpio)<br />EC800M平台引脚对应关系如下（引脚号为模块外部引脚编号）：<br />GPIO1 – 引脚号30<br />GPIO2 – 引脚号31<br />GPIO3 – 引脚号32<br />GPIO4 – 引脚号33<br />GPIO5 – 引脚号49<br />GPIO6 – 引脚号50<br />GPIO7 – 引脚号51<br />GPIO8 – 引脚号52<br />GPIO9 – 引脚号53<br />GPIO10 – 引脚号54<br />GPIO11 – 引脚号55<br />GPIO12 – 引脚号56<br />GPIO13 – 引脚号57<br />GPIO14 – 引脚号58<br />GPIO15 – 引脚号80<br/>GPIO16 – 引脚号81<br/>GPIO17 – 引脚号76<br/>GPIO18 – 引脚号77<br/>GPIO19 – 引脚号82<br/>GPIO20 – 引脚号83<br/>GPIO21 – 引脚号86<br/>GPIO22 – 引脚号87<br/>GPIO23 – 引脚号66<br/>GPIO24 – 引脚号67<br/>GPIO25 – 引脚号17<br/>GPIO26 – 引脚号18<br/>GPIO27 – 引脚号19<br/>GPIO28 – 引脚号20<br/>GPIO29 – 引脚号21<br />GPIO30 – 引脚号22<br />GPIO31 – 引脚号23<br />GPIO32 – 引脚号28<br />GPIO33 – 引脚号29<br />GPIO34 – 引脚号38<br />GPIO35 – 引脚号39<br />GPIO36 – 引脚号16<br />GPIO37 – 引脚号78<br />GPIO38 – 引脚号68<br />GPIO39 – 引脚号69<br />GPIO40 – 引脚号74<br />GPIO41 – 引脚号75<br />GPIO42 – 引脚号84<br />GPIO43 – 引脚号85<br />GPIO44 – 引脚号25<br />EG912N平台引脚对应关系如下（引脚号为模块外部引脚编号）：<br />GPIO1 – 引脚号4<br />GPIO2 – 引脚号5<br />GPIO3 – 引脚号6<br />GPIO4 – 引脚号7<br />GPIO5 – 引脚号18<br />GPIO6 – 引脚号19<br />GPIO7 – 引脚号1<br />GPIO8 – 引脚号16<br />GPIO9 – 引脚号25<br />GPIO10 – 引脚号26<br />GPIO11 – 引脚号27<br />GPIO12 – 引脚号28<br />GPIO13 – 引脚号40<br/>GPIO14 – 引脚号41<br/>GPIO15 – 引脚号64<br/>GPIO16 – 引脚号20<br/>GPIO17 – 引脚号21<br/>GPIO18 – 引脚号30<br/>GPIO19 – 引脚号34<br/>GPIO20 – 引脚号35<br/>GPIO21 – 引脚号36<br/>GPIO22 – 引脚号37<br/>GPIO23 – 引脚号38<br/>GPIO24 – 引脚号39<br/>GPIO25 – 引脚号42<br />GPIO26 – 引脚号78<br />GPIO27 – 引脚号83<br />GPIO28 – 引脚号92<br />GPIO29 – 引脚号95<br />GPIO30 – 引脚号96<br />GPIO31 – 引脚号97<br />GPIO32 – 引脚号98<br />GPIO33 – 引脚号103<br />GPIO34 – 引脚号104<br />GPIO35 – 引脚号105<br />GPIO36 – 引脚号106<br />GPIO37 – 引脚号107<br />GPIO38 – 引脚号114<br />GPIO39 – 引脚号115<br />GPIO40 – 引脚号116 |
| direction | int  | IN – 输入模式，OUT – 输出模式                                |
| pullMode  | int  | PULL_DISABLE – 浮空模式<br />PULL_PU – 上拉模式<br />PULL_PD – 下拉模式 |
| level     | int  | 0 - 设置引脚为低电平, 1- 设置引脚为高电平                    |

* 示例

```python
from machine import Pin
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
```



###### 获取引脚电平

> **Pin.read()**

获取PIN脚电平。

* 参数 

无

* 返回值

PIN脚电平，0-低电平，1-高电平。



###### 设置引脚电平

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

###### 设置输入输出模式

> **Pin.set_dir(value)**

设置PIN脚GPIO的输入输出模式。

* 参数

| 参数  | 类型 | 说明                                                         |
| ----- | ---- | ------------------------------------------------------------ |
| value | int  | 0 - (Pin.IN)设置为输入模式;  <br />1 - (Pin.OUT)设置为输出模式 |

* 返回值

设置成功返回整型值0，设置失败返回其它。

* 示例

```python
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
>>> gpio1.write(1)
0
>>> gpio1.set_dir(Pin.IN)
0
```

###### 获取输入输出模式

> **Pin.get_dir()**

获取pin脚的输入输出模式。

* 参数 

无

* 返回值

PIN模式，0-输入模式，1-输出模式。

###### 使用示例

```python
# Pin使用示例

from machine import Pin
import utime


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Pin_example"
PROJECT_VERSION = "1.0.0"

gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)

if __name__ == '__main__':
    gpio1.write(1) # 设置 gpio1 输出高电平
    val = gpio1.read() # 获取 gpio1 的当前高低状态
    print('val = {}'.format(val))

```



##### UART

类功能：uart串口数据传输。

* 注意

  BC25PA平台，仅支持UART1。

###### 常量说明

| 常量       | 说明  |
| ---------- | ----- |
| UART.UART0 | UART0 |
| UART.UART1 | UART1 |
| UART.UART2 | UART2 |
| UART.UART3 | UART3 |
| UART.UART4 | UART4 |



###### 创建uart对象

> **uart = UART(UART.UARTn, buadrate, databits, parity, stopbits, flowctl)**

* 参数

| 参数     | 类型 | 说明                                                         |
| :------- | :--- | ------------------------------------------------------------ |
| UARTn    | int  | UARTn作用如下：<br />UART0 - DEBUG PORT<br />UART1 – BT PORT<br />UART2 – MAIN PORT<br />UART3 – USB CDC PORT (BG95M3 不支持)<br />UART4 – STDOUT PORT (仅支持EC200U/EC600U/EG915U) |
| buadrate | int  | 波特率，常用波特率都支持，如4800、9600、19200、38400、57600、115200、230400等 |
| databits | int  | 数据位（5 ~ 8），展锐平台当前仅支持8位                       |
| parity   | int  | 奇偶校验（0 – NONE，1 – EVEN，2 - ODD）                      |
| stopbits | int  | 停止位（1 ~ 2）                                              |
| flowctl  | int  | 硬件控制流（0 – FC_NONE， 1 – FC_HW）                        |

- 引脚对应关系

| 平台          |                                                              |
| ------------- | ------------------------------------------------------------ |
| EC600U        | uart1:<br />TX: 引脚号124<br />RX: 引脚号123<br />uart2:<br />TX:引脚号32<br />RX:引脚号31<br />uart4:<BR />TX:引脚号103<BR />RX:引脚号104 |
| EC200U        | uart1:<br />TX: 引脚号138<br />RX: 引脚号137<br />uart2:<br />TX:引脚号67<br />RX:引脚号68<br />uart4:<BR />TX:引脚号82<BR />RX:引脚号81 |
| EC200A        | uart1:<br />TX: 引脚号63<br />RX: 引脚号66<br />uart2:<br />TX:引脚号67<br />RX:引脚号68 |
| EC600S/EC600N | uart0:<br />TX: 引脚号71<br />RX: 引脚号72<br />uart1:<br />TX: 引脚号3<br />RX: 引脚号2<br />uart2:<br />TX:引脚号32<br />RX:引脚号31 |
| EC100Y        | uart0:<br />TX: 引脚号21<br />RX: 引脚号20<br />uart1:<br />TX: 引脚号27<br />RX: 引脚号28<br />uart2:<br />TX:引脚号50<br />RX:引脚号49 |
| EC800N        | uart0:<br />TX: 引脚号39<br />RX: 引脚号38<br />uart1:<br />TX: 引脚号50<br />RX: 引脚号51<br />uart2:<br />TX:引脚号18<br />RX:引脚号17 |
| BC25PA        | uart1:<br />TX: 引脚号29<br />RX: 引脚号28                   |
| BG95M3        | uart0:<br />TX: 引脚号23<br />RX: 引脚号22<br />uart1:<br />TX:引脚号27<br />RX:引脚号28<br />uart2:<br />TX: 引脚号64<br />RX: 引脚号65 |
| EC600M        | uart0:<br />TX: 引脚号71<br />RX: 引脚号72<br />uart1(不开启流控):<br />TX: 引脚号3<br />RX: 引脚号2<br />uart1(开启流控):<br />TX: 引脚号33<br />RX: 引脚号34<br />uart2:<br />TX:引脚号32<br />RX:引脚号31 |
| EG915U        | uart1:<br />TX: 引脚号27<br />RX: 引脚号28<br />uart2:<br />TX:引脚号35<br />RX:引脚号34<br/>uart4:<br/>TX:引脚号19<br/>RX:引脚号18 |
| EC800M        | uart0:<br />TX: 引脚号39<br />RX: 引脚号38<br />uart1(不开启流控):<br />TX: 引脚号50<br />RX: 引脚号51<br />uart1(开启流控):<br />TX: 引脚号22<br />RX: 引脚号23<br />注:EC800MCN_GA uart1不可用<br />uart2:<br />TX:引脚号18<br />RX:引脚号17 |
| EG912N        | uart0:<br />TX: 引脚号23<br />RX: 引脚号22<br />uart1(不开启流控):<br />TX: 引脚号27<br />RX: 引脚号28<br/>uart1(开启流控):<br />TX: 引脚号36<br />RX: 引脚号37<br />uart2:<br />TX:引脚号34<br />RX:引脚号35 |

* 示例

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
```



###### 获取接收缓存未读数据大小

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



###### 串口读数据

> **uart.read(nbytes)**

从串口读取数据。

* 参数

| 参数   | 类型 | 说明           |
| ------ | ---- | -------------- |
| nbytes | int  | 要读取的字节数 |

* 返回值

返回读取的数据。



###### 串口发数据

> **uart.write(data)**

发送数据到串口。

* 参数

| 参数 | 类型   | 说明       |
| ---- | ------ | ---------- |
| data | buf/string  | 发送的数据 |

* 返回值

返回发送的字节数。



###### 关闭串口

> **uart.close()**

关闭串口。

* 参数

无

* 返回值

成功返回整型0，失败返回整型-1。



###### 控制485通信方向

> **uart.control_485(UART.GPIOn, direction)**

串口发送数据之前和之后进行拉高拉低指定GPIO，用来指示485通信的方向。

- 参数

| 参数      | 类型 | 说明                                                         |
| --------- | ---- | ------------------------------------------------------------ |
| GPIOn     | int  | 需要控制的GPIO引脚号，参照Pin模块的定义                      |
| direction | int  | 1 - 表示引脚电平变化为：串口发送数据之前由低拉高、发送数据之后再由高拉低<br />0 - 表示引脚电平变化为：串口发送数据之前由高拉低、发送数据之后再由低拉高 |

- 返回值

成功返回整型0，失败返回整型-1。

* 注意

  BC25PA平台不支持此方法。
- 示例

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
>>> uart1.control_485(UART.GPIO24, 1)
```

###### 设置串口数据回调

> **uart.set_callback(fun)**

串口收到数据后，会执行该回调。

- 参数

| 参数 | 类型     | 说明                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| fun  | function | 串口接收数据回调 [result, port, num]<br />result: 接收接口（0：成功， 其它：失败）<br />port: 接收端口<br />num: 返回有多少数据 |

- 返回值

成功返回整型0，失败返回整型-1。

- 示例

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
>>> 
>>>def uart_call(para):
>>>		print(para)
>>> uart1.set_callback(uart_call)
```



###### 使用示例

```python
"""
运行本例程，需要通过串口线连接开发板的 MAIN 口和PC，在PC上通过串口工具
打开 MAIN 口，并向该端口发送数据，即可看到 PC 发送过来的消息。
"""
import _thread
import utime
import log
from machine import UART


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_UART_example"
PROJECT_VERSION = "1.0.1"

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

class Example_uart(object):
    def __init__(self, no=UART.UART2, bate=115200, data_bits=8, parity=0, stop_bits=1, flow_control=0):
        self.uart = UART(no, bate, data_bits, parity, stop_bits, flow_control)
        self.uart.set_callback(self.callback)


    def callback(self, para):
        uart_log.info("call para:{}".format(para))
        if(0 == para[0]):
            self.uartRead(para[2])

    
    def uartWrite(self, msg):
        uart_log.info("write msg:{}".format(msg))
        self.uart.write(msg)

    def uartRead(self, len):
        msg = self.uart.read(len)
        utf8_msg = msg.decode()
        uart_log.info("UartRead msg: {}".format(utf8_msg))
        return utf8_msg

    def uartWrite_test(self):
        for i in range(10):
            write_msg = "Hello count={}".format(i)
            self.uartWrite(write_msg)
            utime.sleep(1)

if __name__ == "__main__":
    uart_test = Example_uart()
    uart_test.uartWrite_test()
    

# 运行结果示例
'''
INFO:UART:write msg:Hello count=0
INFO:UART:write msg:Hello count=1
INFO:UART:write msg:Hello count=2
INFO:UART:write msg:Hello count=3
INFO:UART:write msg:Hello count=4
INFO:UART:write msg:Hello count=5
INFO:UART:write msg:Hello count=6
INFO:UART:write msg:Hello count=7
INFO:UART:write msg:Hello count=8
INFO:UART:write msg:Hello count=9

INFO:UART:call para:[0, 2, 15]
INFO:UART:UartRead msg: my name is XXX


'''

```



##### Timer

类功能：硬件定时器。

PS:使用该定时器时需注意：定时器0-3，每个在同一时间内只能执行一件任务，且多个对象不可使用同一个定时器。

###### 常量说明

| 常量           | 说明                       |
| -------------- | -------------------------- |
| Timer.Timer0   | 定时器0                    |
| Timer.Timer1   | 定时器1                    |
| Timer.Timer2   | 定时器2                    |
| Timer.Timer3   | 定时器3                    |
| Timer.ONE_SHOT | 单次模式，定时器只执行一次 |
| Timer.PERIODIC | 周期模式，定时器循环执行   |



###### 创建Timer对象

> **timer = Timer(Timern)**

创建Timer对象。

* 参数

| 参数   | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| Timern | int  | 定时器号<br />支持定时器Timer0 ~ Timer3（使用该定时器时需注意：定时器0-3，每个在同一时间内只能执行一件任务，且多个对象不可使用同一个定时器。） |

* 示例

```python
>>> from machine import Timer
>>> timer1 = Timer(Timer.Timer1)  # 使用该定时器时需注意：定时器0-3，每个在同一时间内只能执行一件任务，且多个对象不可使用同一个定时器。
```



###### 启动定时器

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
>>> timer1.start(period=1000, mode=timer1.PERIODIC, callback=fun)
0
###timer callback function###
###timer callback function###
###timer callback function###
……
```



###### 关闭定时器

> **timer.stop()**

关闭定时器。

* 参数

无

* 返回值

成功返回整型值0，失败返回整型值-1。



###### 使用示例

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
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Timer_example"
PROJECT_VERSION = "1.0.0"

# 设置日志输出级别
log.basicConfig(level=log.INFO)
Timer_Log = log.getLogger("Timer")

num = 0
state = 1
# 注：EC100YCN支持定时器Timer0 ~ Timer3
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
	t.start(period=1000, mode=t.PERIODIC, callback=timer_test)   # 启动定时器
```



##### ExtInt

类功能：用于配置I/O引脚在发生外部事件时中断。



###### 创建ExtInt对象

> **extint = ExtInt(GPIOn, mode, pull, callback)**

* 参数

| 参数     | 类型 | 说明                                                         |
| :------- | :--- | ------------------------------------------------------------ |
| GPIOn    | int  | 需要控制的GPIO引脚号，参照Pin模块的定义(除BG95M3外) <br />BG95M3平台引脚对应关系如下（引脚号为模块外部引脚编号）<br />GPIO2 – 引脚号5<br />GPIO3 – 引脚号6<br />GPIO6 – 引脚号19<br />GPIO7 – 引脚号22<br />GPIO8 – 引脚号23<br />GPIO9 – 引脚号25<br />GPIO11 – 引脚号27<br />GPIO12 – 引脚号28<br />GPIO14 – 引脚号41<br />GPIO16 – 引脚号65<br/>GPIO17 – 引脚号66<br />GPIO18 – 引脚号85<br />GPIO19 – 引脚号86<br />GPIO20 – 引脚号87<br />GPIO21 – 引脚号88 |
| mode     | int  | 设置触发方式<br /> IRQ_RISING – 上升沿触发<br /> IRQ_FALLING – 下降沿触发<br /> IRQ_RISING_FALLING – 上升和下降沿触发 |
| pull     | int  | PULL_DISABLE – 浮空模式<br />PULL_PU – 上拉模式 <br />PULL_PD  – 下拉模式 |
| callback | int  | 中断触发回调函数<br />返回参数为长度为2的元组<br />args[0]: gpio号<br />args[1]: 触发沿（0：上升沿 1：下降沿） |

* 示例

```python
>>> from machine import ExtInt
>>> def fun(args):
        print('### interrupt  {} ###'.format(args)) # args[0]:gpio号 args[1]:上升沿或下降沿
>>> extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
```




###### 使能中断

> **extint.enable()**

使能extint对象外部中断，当中断引脚收到上升沿或者下降沿信号时，会调用callback执行 。

* 参数

无

* 返回值

使能成功返回整型值0，使能失败返回整型值-1。



###### 关闭中断

> **extint.disable()**

禁用与extint对象关联的中断 。

* 参数

无

* 返回值

使能成功返回整型值0，使能失败返回整型值-1。



###### 读取引脚映射行号

> **extint.line()**

返回引脚映射的行号。

* 参数

无

* 返回值

引脚映射的行号。

* 示例

```python
>>> extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
>>> extint.line()
1
```

###### 读取中断数

> **extint.read_count(is_reset)**

返回触发中断的次数。

* 参数

| 参数     | 类型 | 说明                                           |
| -------- | ---- | ---------------------------------------------- |
| is_reset | int  | 读取后是否重置计数<br />0：不重置<br />1：重置 |

* 返回值

列表 [rising_count, falling_count]

​		rising_count:	上升沿触发次数

​		falling_count：下降沿触发次数



###### 清空中断数

> **extint.count_reset()**

清空触发中断的次数。

* 参数

无

* 返回值

0：成功

其他：失败

###### 读取电平

> **extint.read_level()**

读取当前管脚电平。

* 参数

无

* 返回值

PIN脚电平，0-低电平，1-高电平



##### RTC

类功能：提供获取设置rtc时间方法，对于BC25PA平台起到从深休眠或者软件关机状态唤醒模组的功能。

###### 创建RTC对象

> **from machine import RTC**
>
> **rtc = RTC()**



###### 设置和获取RTC时间

> **rtc.datetime([year, month, day, week, hour, minute, second, microsecond])**

设置和获取RTC时间，不带参数时，则用于获取时间，带参数则是设置时间；设置时间的时候，参数week不参于设置，microsecond参数保留，暂未使用，默认是0。

* 参数

| 参数        | 类型 | 说明                                                         |
| ----------- | ---- | ------------------------------------------------------------ |
| year        | int  | 年                                                           |
| month       | int  | 月，范围1 ~ 12                                                 |
| day         | int  | 日，范围1 ~ 31                                                 |
| week        | int  | 星期，范围0 ~ 6，其中0表示周日，1 ~ 6分别表示周一到周六；设置时间时，该参数不起作用，保留；获取时间时该参数有效 |
| hour        | int  | 时，范围0 ~ 23                                                 |
| minute      | int  | 分，范围0 ~ 59                                                 |
| second      | int  | 秒，范围0 ~ 59                                                 |
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

###### 设置RTC到期时间

支持平台EC600U/EC200U/EC600N/EC800N/BC25

> **rtc.set_alarm(data_e)**

设置RTC到期时间,当到了到期时间就会调用注册的回调函数。
* 参数
| 参数        | 类型 | 说明                                                         |
| ----------- | ---- | ------------------------------------------------------------ |
| year        | int  | 年                                                           |
| month       | int  | 月，范围1 ~ 12                                                 |
| day         | int  | 日，范围1 ~ 31                                                 |
| week        | int  | 星期，范围0 ~ 6，其中0表示周日，1 ~ 6分别表示周一到周六；设置时间时，该参数不起作用，保留；获取时间时该参数有效 |
| hour        | int  | 时，范围0 ~ 23                                                 |
| minute      | int  | 分，范围0 ~ 59                                                 |
| second      | int  | 秒，范围0 ~ 59                                                 |
| microsecond | int  | 微秒，保留参数，暂未使用，设置时间时该参数写0即可            |

* 返回值
	成功: 0
	失败: -1
* 示例

```python
>>> data_e=rtc.datetime()
>>> data_l=list(data_e)
>>> data_l[6] +=30				
>>> data_e=tuple(data_l)
>>> rtc.set_alarm(data_e)
0
```

###### 注册RTC alarm回调

支持平台EC600U/EC200U/EC600N/EC800N/BC25

> rtc.register_callback(fun)

注册RTC alarm回调处理函数

* 参数

| 参数 | 类型     | 说明                  |
| ---- | -------- | --------------------- |
| fun  | function | RTC alarm回调处理函数 |

* 返回值

注册成功返回整型值0，注册失败返回整型值-1 。



###### 开关RTC alarm功能

支持平台EC600U/EC200U/EC600N/EC800N/BC25
注意:BC25PA平台只有设置回调函数,才能启动定时器.

> rtc.enable_alarm(on_off)

打开/关闭RTC alarm功能

* 参数

| 参数   | 类型 | 说明                                     |
| ------ | ---- | ---------------------------------------- |
| on_off | int  | 1-打开RTC alarm功能；0-关闭RTC alarm功能 |

* 返回值

打开/关闭成功返回整型值0，打开/关闭失败返回整型值-1 。



- 示例

```python
from machine import RTC
rtc = RTC()
def callback(args):
   print('RTC alarm')

rtc.register_callback(callback)
rtc.set_alarm([2021, 7, 9, 5, 12, 30, 0, 0])
rtc.enable_alarm(1)
```

注：EC600U/EC200U平台支持自动开机，即设置alarm功能之后将模块关机，alarm时间到了之后可以自动开机。其他平台不支持该特性。



##### I2C

类功能：用于设备之间通信的双线协议。

###### 常量说明

| 常量              |                   | 适用平台                      |
| ----------------- | ----------------- | ----------------------------- |
| I2C.I2C0          | i2c 通路索引号: 0 | EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M |
| I2C.I2C1          | i2c 通路索引号: 1 | EC600S/EC600N/EC600U/EC200U/BC25PA/BG95M3/EC600M/EG915U/EC800M/EG912N |
| I2C.I2C2          | i2c 通路索引号: 2 | BG95M3/EC600M |
| I2C.STANDARD_MODE | 标准模式 |                  |
| I2C.FAST_MODE | 快速模式      |                               |



###### 创建I2C对象

> **from machine import I2C**
>
> **i2c_obj = I2C(I2Cn,  MODE)**

* 参数说明

| 参数 | 类型 | 说明                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| I2Cn | int  | i2c 通路索引号:<br />I2C.I2C0 : 0  <br />I2C.I2C1 : 1<br />I2C.I2C2 : 2 |
| MODE | int  | i2c 的工作模式:<br />I2C.STANDARD_MODE : 0 标准模式<br />I2C.FAST_MODE ： 1 快速模式 |

- 引脚对应关系

| 平台          |                                                              |
| ------------- | ------------------------------------------------------------ |
| EC600U        | I2C0:<br />SCL: 引脚号11<br />SDA: 引脚号12<br />I2C1:<br />SCL:引脚号57<br />SDA:引脚号56 |
| EC200U        | I2C0:<br />SCL: 引脚号41<br />SDA: 引脚号42<br />I2C1:<br />SCL:引脚号141<br />SDA:引脚号142 |
| EC200A        | I2C0:<br />SCL: 引脚号41<br />SDA: 引脚号42                  |
| EC600S/EC600N | I2C1:<br />SCL:引脚号57<br />SDA:引脚号56                    |
| EC100Y        | I2C0:<br />SCL:引脚号57<br />SDA:引脚号56                    |
| BC25PA        | I2C0:<br />SCL: 引脚号23<br />SDA: 引脚号22<br />I2C1:<br />SCL:引脚号20<br />SDA:引脚号21 |
| EC800N        | I2C0:<br />SCL:引脚号67<br />SDA:引脚号66                    |
| BG95M3        | I2C0:<br />SCL: 引脚号18<br />SDA: 引脚号19<br />I2C1:<br />SCL:引脚号40<br />SDA:引脚号41<br />I2C2:<br />SCL:引脚号26<br />SDA:引脚号25 |
| EC600M        | I2C0:<br />SCL: 引脚号9<br />SDA: 引脚号64<br />I2C1:<br />SCL:引脚号57<br />SDA:引脚号56<br />I2C2:<br />SCL:引脚号67<br />SDA:引脚号65 |
| EG915U        | I2C0:<br />SCL: 引脚号103<br />SDA: 引脚号114<br />I2C1:<br />SCL:引脚号40<br />SDA:引脚号41 |
| EC800M        | I2C0:<br />SCL: 引脚号67<br />SDA: 引脚号66<br />I2C2:<br />SCL:引脚号68<br />SDA:引脚号69 |
| EG912N        | I2C1:<br />SCL: 引脚号40<br />SDA: 引脚号41                  |

- 示例

```python
from machine import I2C

i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # 返回i2c对象
```



###### 读取数据

> **I2C.read(slaveaddress, addr,addr_len, r_data, datalen, delay)**

从 I2C 总线中读取数据。

**参数说明**

| 参数         | 类型      | 说明                             |
| ------------ | --------- | -------------------------------- |
| slaveaddress | int       | i2c 设备地址                     |
| addr         | bytearray | i2c 寄存器地址                   |
| addr_len     | int       | 寄存器地址长度                   |
| r_data       | bytearray | 接收数据的字节数组               |
| datalen      | int       | 字节数组的长度                   |
| delay        | int       | 延时，数据转换缓冲时间（单位ms） |

* 返回值

成功返回整型值0，失败返回整型值-1。



###### 写入数据

> **I2C.write(slaveaddress, addr, addr_len, data, datalen)**

从 I2C 总线中写入数据。

* 参数说明

| 参数         | 类型      | 说明           |
| ------------ | --------- | -------------- |
| slaveaddress | int       | i2c 设备地址   |
| addr         | bytearray | i2c 寄存器地址 |
| addr_len     | int       | 寄存器地址长度 |
| data         | bytearray | 写入的数据     |
| datalen      | int       | 写入数据的长度 |

* 返回值

成功返回整型值0，失败返回整型值-1。



###### 使用示例

需要连接设备使用！

```python
import log
from machine import I2C
import utime


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_I2C_example"
PROJECT_VERSION = "1.0.0"

'''
I2C使用示例
'''

# 设置日志输出级别
log.basicConfig(level=log.INFO)
i2c_log = log.getLogger("I2C")


if __name__ == '__main__':
    I2C_SLAVE_ADDR = 0x1B  # i2c 设备地址
    WHO_AM_I = bytearray([0x02, 0])   # i2c 寄存器地址，以buff的方式传入，取第一个值，计算一个值的长度

    data = bytearray([0x12, 0])   # 输入对应指令
    i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # 返回i2c对象
    i2c_obj.write(I2C_SLAVE_ADDR, WHO_AM_I, 1, data, 2) # 写入data

    r_data = bytearray(2)  # 创建长度为2的字节数组接收
    i2c_obj.read(I2C_SLAVE_ADDR, WHO_AM_I, 1, r_data, 2, 0)   # read
    i2c_log.info(r_data[0])
    i2c_log.info(r_data[1])


```

##### I2C_simulation

类功能：用于gpio模拟标准i2c协议。

除了创建对象外，其它的操作（读写）均与I2C一致


###### 创建I2C_simulation对象

> **from machine import I2C_simulation**
>
> **i2c_obj = I2C_simulation(GPIO_clk,  GPIO_sda, CLK)**

* 参数说明

| 参数     | 类型 | 说明                                                  |
| -------- | ---- | ----------------------------------------------------- |
| GPIO_clk | int  | i2c的CLK引脚(需要控制的GPIO引脚号，参照Pin模块的定义) |
| GPIO_sda | int  | i2c的SDA引脚(需要控制的GPIO引脚号，参照Pin模块的定义) |
| CLK      | int  | i2c的频率 （0,1000000Hz]                              |

- 示例

```python
from machine import I2C_simulation

i2c_obj = I2C_simulation(I2C_simulation.GPIO10, I2C_simulation.GPIO11, 300)  # 返回i2c对象
```



###### 读取数据

> **I2C_simulation.read(slaveaddress, addr,addr_len, r_data, datalen, delay)**

从 I2C 总线中读取数据。

**参数说明**

| 参数         | 类型      | 说明                             |
| ------------ | --------- | -------------------------------- |
| slaveaddress | int       | i2c 设备地址                     |
| addr         | bytearray | i2c 寄存器地址                   |
| addr_len     | int       | 寄存器地址长度                   |
| r_data       | bytearray | 接收数据的字节数组               |
| datalen      | int       | 字节数组的长度                   |
| delay        | int       | 延时，数据转换缓冲时间（单位ms） |

* 返回值

成功返回整型值0，失败返回整型值-1。



###### 写入数据

> **I2C_simulation.write(slaveaddress, addr, addr_len, data, datalen)**

从 I2C 总线中写入数据。

* 参数说明

| 参数         | 类型      | 说明           |
| ------------ | --------- | -------------- |
| slaveaddress | int       | i2c 设备地址   |
| addr         | bytearray | i2c 寄存器地址 |
| addr_len     | int       | 寄存器地址长度 |
| data         | bytearray | 写入的数据     |
| datalen      | int       | 写入数据的长度 |

* 返回值

成功返回整型值0，失败返回整型值-1。



###### 使用示例

该示例是驱动AHT10获取温湿度。

```python
import log
#from machine import I2C
from machine import I2C_simulation
import utime as time
"""
1. calibration
2. Trigger measurement
3. read data
"""

# API  手册 http://qpy.quectel.com/wiki/#/zh-cn/api/?id=i2c
# AHT10 说明书
#  https://server4.eca.ir/eshop/AHT10/Aosong_AHT10_en_draft_0c.pdf


class aht10class():
    i2c_log = None
    i2c_dev = None
    i2c_addre = None

    # Initialization command
    AHT10_CALIBRATION_CMD = 0xE1
    # Trigger measurement
    AHT10_START_MEASURMENT_CMD = 0xAC
    # reset
    AHT10_RESET_CMD = 0xBA

    def write_data(self, data):
        self.i2c_dev.write(self.i2c_addre,
                           bytearray(0x00), 0,
                           bytearray(data), len(data))
        pass

    def read_data(self, length):
        print("read_data start")
        r_data = [0x00 for i in range(length)]
        r_data = bytearray(r_data)
        print("read_data start1")
        ret = self.i2c_dev.read(self.i2c_addre,
                          bytearray(0x00), 0,
                          r_data, length,
                          0)
        print("read_data start2")
        print('ret',ret)
        print('r_data:',r_data)
        return list(r_data)

    def aht10_init(self, addre=0x38, Alise="Ath10"):
        self.i2c_log = log.getLogger(Alise)
        self.i2c_dev = I2C_simulation(I2C_simulation.GPIO10, I2C_simulation.GPIO11, 300)
        self.i2c_addre = addre
        self.sensor_init()
        pass

    def aht10_transformation_temperature(self, data):
        r_data = data
        #　根据数据手册的描述来转化温度
        humidity = (r_data[0] << 12) | (
            r_data[1] << 4) | ((r_data[2] & 0xF0) >> 4)
        humidity = (humidity/(1 << 20)) * 100.0
        print("current humidity is {0}%".format(humidity))
        temperature = ((r_data[2] & 0xf) << 16) | (
            r_data[3] << 8) | r_data[4]
        temperature = (temperature * 200.0 / (1 << 20)) - 50
        print("current temperature is {0}°C".format(temperature))
        

    def sensor_init(self):
        # calibration
        self.write_data([self.AHT10_CALIBRATION_CMD, 0x08, 0x00])
        time.sleep_ms(300)  # at last 300ms
        pass


    def ath10_reset(self):
        self.write_data([self.AHT10_RESET_CMD])
        time.sleep_ms(20)  # at last 20ms

    def Trigger_measurement(self):
        # Trigger data conversion
        self.write_data([self.AHT10_START_MEASURMENT_CMD, 0x33, 0x00])
        time.sleep_ms(200)  # at last delay 75ms
        # check has success
        r_data = self.read_data(6)
        # check bit7
        if (r_data[0] >> 7) != 0x0:
            print("Conversion has error")
        else:
            self.aht10_transformation_temperature(r_data[1:6])

ath_dev = None

def i2c_aht10_test():
    global ath_dev
    ath_dev = aht10class()
    ath_dev.aht10_init()

    # 测试十次
    for i in range(5):
        ath_dev.Trigger_measurement()
        time.sleep(1)


if __name__ == "__main__":
    print('start')
    i2c_aht10_test()


```



##### SPI

类功能：串行外设接口总线协议。


###### 创建SPI对象

> **spi_obj = SPI(port, mode, clk)**

* 参数说明

| 参数 | 类型 | 说明                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| port | int  | 通道选择[0,1]                                                |
| mode | int  | SPI 的工作模式(模式0最常用):<br />时钟极性CPOL: 即SPI空闲时，时钟信号SCLK的电平（0:空闲时低电平; 1:空闲时高电平）<br /> 0 : CPOL=0, CPHA=0<br /> 1 : CPOL=0, CPHA=1<br /> 2:  CPOL=1, CPHA=0<br /> 3:  CPOL=1, CPHA=1 |
| clk  | int  | 时钟频率<br />EC600NCN/EC600SCN/EC800NCN/BG95M3/EC600M/EC800M/EG912N:<br /> 0 : 812.5kHz<br /> 1 : 1.625MHz<br /> 2 : 3.25MHz<br /> 3 : 6.5MHz<br /> 4 : 13MHz<br /> 5 :  26MHz<br /> 6：52MHz<br />EC600UCN/EC200UCN/EG915U:<br />0 : 781.25KHz<br />1 : 1.5625MHz<br />2 : 3.125MHz<br />3 : 5MHz<br />4 : 6.25MHz<br />5 : 10MHz<br />6 : 12.5MHz<br />7 : 20MHz<br />8 : 25MHz<br />9 : 33.33MHz<br />BC25PA：<br />0 ： 5MHz<br />X : XMHz  (X in [1,39]) |

- 引脚说明

| 平台          | 引脚                                                         |
| ------------- | ------------------------------------------------------------ |
| EC600U        | port0:<br />CS:引脚号4<br />CLK:引脚号1<br />MOSI:引脚号3<br />MISO:引脚号2<br />port1:<br />CS:引脚号58<br />CLK:引脚号61<br />MOSI:引脚号59<br />MISO:引脚号60 |
| EC200U        | port0:<br />CS:引脚号134<br />CLK:引脚号133<br />MOSI:引脚号132<br />MISO:引脚号131<br />port1:<br />CS:引脚号26<br />CLK:引脚号27<br />MOSI:引脚号24<br />MISO:引脚号25 |
| EC600S/EC600N | port0:<br />CS:引脚号58<br />CLK:引脚号61<br />MOSI:引脚号59<br />MISO:引脚号60<br />port1:<br />CS:引脚号4<br />CLK:引脚号1<br />MOSI:引脚号3<br />MISO:引脚号2 |
| EC100Y        | port0:<br />CS:引脚号25<br />CLK:引脚号26<br />MOSI:引脚号27<br />MISO:引脚号28<br />port1:<br />CS:引脚号105<br />CLK:引脚号104<br />MOSI:引脚号107<br />MISO:引脚号106 |
| EC800N        | port0:<br />CS:引脚号31<br />CLK:引脚号30<br />MOSI:引脚号32<br />MISO:引脚号33<br />port1:<br />CS:引脚号52<br />CLK:引脚号53<br />MOSI:引脚号50<br />MISO:引脚号51 |
| BC25PA        | port0:<br />CS:引脚号6<br />CLK:引脚号5<br />MOSI:引脚号4<br />MISO:引脚号3 |
| BG95M3        | port0:<br />CS:引脚号25<br />CLK:引脚号26<br />MOSI:引脚号27<br />MISO:引脚号28<br />port1:<br />CS:引脚号41<br />CLK:引脚号40<br />MOSI:引脚号64<br />MISO:引脚号65 |
| EC600M        | port0:<br />CS:引脚号58<br />CLK:引脚号61<br />MOSI:引脚号59<br />MISO:引脚号60<br />port1:<br />CS:引脚号4<br />CLK:引脚号1<br />MOSI:引脚号3<br />MISO:引脚号2 |
| EG915U        | port0:<br />CS:引脚号25<br />CLK:引脚号26<br />MOSI:引脚号64<br />MISO:引脚号88 |
| EC800M        | port0:<br />CS:引脚号31<br />CLK:引脚号30<br />MOSI:引脚号32<br />MISO:引脚号33</u><br />port1:<br />CS:引脚号52<br />CLK:引脚号53<br />MOSI:引脚号50<br />MISO:引脚号51 |
| EG912N        | port0:<br />CS:引脚号25<br />CLK:引脚号26<br />MOSI:引脚号27<br />MISO:引脚号28<br/>port1:<br />CS:引脚号5<br />CLK:引脚号4<br />MOSI:引脚号6<br />MISO:引脚号7 |
* 注意
  BC25PA平台不支持1、2模式。
- 示例

```python
from machine import SPI

spi_obj = SPI(1, 0, 1)  # 返回spi对象
```



###### 读取数据

> **SPI.read(recv_data, datalen)**

读取数据。

* 参数说明

| 参数      | 类型      | 说明               |
| --------- | --------- | ------------------ |
| recv_data | bytearray | 接收读取数据的数组 |
| datalen   | int       | 读取数据的长度     |

* 返回值

失败返回整型值-1。



###### 写入数据

> **SPI.write(data, datalen)**

写入数据。

* 参数说明

| 参数    | 类型  | 说明           |
| ------- | ----- | -------------- |
| data    | bytes | 写入的数据     |
| datalen | int   | 写入的数据长度 |

* 返回值

失败返回整型值-1。



###### 写入并读取数据

> **SPI.write_read(r_data，data, datalen)**

写入和读取数据。

* 参数说明

| 参数    | 类型      | 说明               |
| ------- | --------- | ------------------ |
| r_data  | bytearray | 接收读取数据的数组 |
| data    | bytes     | 发送的数据         |
| datalen | int       | 读取数据的长度     |

* 返回值

失败返回整型值-1。



###### 使用示例

需要配合外设使用！

```python
import log
from machine import SPI
import utime

'''
SPI使用示例
适配版本：EC100Y(V0009)及以上；EC600S(V0002)及以上
'''

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_SPI_example"
PROJECT_VERSION = "1.0.0"

spi_obj = SPI(0, 0, 1)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
spi_log = log.getLogger("SPI")


if __name__ == '__main__':
    r_data = bytearray(5)  # 创建接收数据的buff
    data = b"world"  # 写入测试数据

    ret = spi_obj.write_read(r_data, data, 5)  # 写入数据并接收
    spi_log.info(r_data)

```



##### LCD

类功能：该模块提供对LCD显示屏的控制

适配版本：EC100Y(V0009)及以上；EC600S(V0002)及以上。

* 注意
  BC25PA平台不支持此模块功能。
###### 创建LCD对象

> **lcd = LCD()**

* 参数说明

无

- 示例

```python
from machine import LCD 
lcd = LCD()   # 创建lcd对象
```



###### LCD初始化（接口1：设备接模块LCM接口）

> **lcd.lcd_init(lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness)**

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



###### LCD初始化（接口2：设备接模块SPI接口）

> **lcd.lcd_init(lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness, lcd_interface, spi_port, spi_mode, cs_pin, dc_pin, rst_pin)**

初始化LCD

- 参数

| 参数               | 类型      | 说明                                                         |
| ------------------ | --------- | ------------------------------------------------------------ |
| lcd_init_data      | bytearray | 传入 LCD 的配置命令                                          |
| lcd_width          | int       | LCD 屏幕的宽度。宽度不超过 500                               |
| lcd_hight          | int       | LCD 屏幕的高度。高度不超过 500                               |
| lcd_clk            | int       | SPI 时钟。见machine SPI 创建SPI对象参数说明clk               |
| data_line          | int       | 数据线数。参数值为 1 和 2。                                  |
| line_num           | int       | 线的数量。参数值为 3 和 4。                                  |
| lcd_type           | int       | 屏幕类型。0：rgb；1：fstn                                    |
| lcd_invalid        | bytearray | 传入LCD 区域设置的配置命令                                   |
| lcd_display_on     | bytearray | 传入LCD 屏亮的配置命令                                       |
| lcd_display_off    | bytearray | 传入LCD 屏灭的配置命令                                       |
| lcd_set_brightness | bytearray | 传入LCD屏亮度的配置命令。设置为 None表示由 LCD_BL_K 控制亮度（有些屏幕是由寄存器控制屏幕亮度，有 些是通过 LCD_BL_K 控制屏幕亮度） |
| lcd_interface      | int       | LCD接口类型。0：LCM接口；1：SPI接口                          |
| spi_port           | int       | 通道选择[0,1]，参照SPI部分                                   |
| spi_mode           | int       | SPI 的工作模式(模式0最常用):<br />时钟极性CPOL: 即SPI空闲时，时钟信号SCLK的电平（0:空闲时低电平; 1:空闲时高电平）<br /> 0 : CPOL=0, CPHA=0<br /> 1 : CPOL=0, CPHA=1<br /> 2:  CPOL=1, CPHA=0<br /> 3:  CPOL=1, CPHA=1 |
| cs_pin             | int       | CS引脚，见machine Pin常量说明                                |
| dc_pin             | int       | DC引脚，见machinePin常量说明                                 |
| rst_pin            | int       | RST引脚，见machinePin常量说明                                |

* 返回值


  0  	 成功 

  -1  	已经初始化 

  -2  	参数错误（为空或过大（大于 1000 像素点）） 

  -3  	缓存申请失败

  -5  	配置参数错误 



###### 清屏


> **lcd.lcd_clear(color)**

清除屏幕。

- 参数

| 参数  | 类型   | 说明             |
| ----- | ------ | ---------------- |
| color | 16进制 | 需要刷屏的颜色值 |

* 返回值

成功返回0， 失败返回-1。



###### 区域写屏

> **lcd.lcd_write(color_buffer,start_x,start_y,end_x,end_y)**

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



###### 设置屏幕亮度

> **lcd.lcd_brightness(level)**

设置屏幕亮度等级。

- 参数

| 参数  | 类型 | 说明                                                         |
| ----- | ---- | ------------------------------------------------------------ |
| level | int  | 亮度等级。此处会调用 lcd.lcd_init()中的 lcd_set_brightness回调。若该参数为 None，亮度调节则由 背光亮度调节引脚来控制<br />范围[0,5] |

* 返回值

成功返回0， 失败返回-1。



###### 打开屏显

> **lcd.lcd_display_on()**

打开屏显 。调用此接口后调用 lcd.lcd_init()中的 lcd_display_on 回调。 

- 参数

无

* 返回值

成功返回0， 失败返回-1。



###### 关闭屏显

> **lcd.lcd_display_off()**

关闭屏显 。调用此接口后调用 lcd.lcd_init()中的 lcd_display_off 回调。 

- 参数

无

* 返回值

成功返回0， 失败返回-1。



###### 写入命令

> **lcd.lcd_write_cmd(cmd_value, cmd_value_len)**

写入命令。

- 参数

| 参数          | 类型   | 说明       |
| ------------- | ------ | ---------- |
| cmd_value     | 16进制 | 命令值     |
| cmd_value_len | int    | 命令值长度 |

* 返回值

成功返回0， 失败返回其他值。



###### 写入数据

> **lcd.lcd_write_data(data_value, data_value_len)**

写入数据。

- 参数

| 参数           | 类型   | 说明       |
| -------------- | ------ | ---------- |
| data_value     | 16进制 | 数据值     |
| data_value_len | int    | 数据值长度 |

* 返回值

成功返回0， 失败返回其他值。



###### 显示图片

> **lcd.lcd_show(file_name, start_x,start_y,width,hight)**

采用读文件方式，显示图片。

该文件是由Image2Lcd工具生成的bin文件。若勾选包含图像头文件，则width和hight无需填写

也可以是jpeg格式图片

- 参数

| 参数      | 类型   | 说明                                                         |
| --------- | ------ | ------------------------------------------------------------ |
| file_name | 文件名 | 需要显示的图片                                               |
| start_x   | int    | 起始x坐标                                                    |
| start_y   | int    | 起始y坐标                                                    |
| width     | int    | 图片宽度（若图片文件包含的头信息，则该处不填，jpeg格式也不需要填） |
| hight     | int    | 图片高度（若图片文件包含的头信息，则该处不填，jpeg格式也不需要填） |

* 返回值

成功返回0， 失败返回其他值。



###### 显示jpeg图片

> **lcd.lcd_show_jpg( file_name, start_x,start_y)**

采用读文件方式，显示jpeg图片。

- 参数

| 参数      | 类型 | 说明             |
| --------- | ---- | ---------------- |
| file_name | str  | 需要显示的图片名 |
| start_x   | int  | 起始x坐标        |
| start_y   | int  | 起始y坐标        |

* 返回值

成功返回0， 失败返回其他值。



###### 使用示例

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

lcd.lcd_show("lcd_test.bin",0,0)	#该lcd_test.bin 中包含图像头数据
lcd.lcd_show("lcd_test1.bin",0,0,126,220) #该lcd_test1.bin 中没有包含图像头数据
```




##### WDT 

模块功能：APP应用程序发生异常不执行时进行系统重启操作

###### 创建wdt对象

> ​	**wdt = WDT(period)**

创建软狗对象。

- 参数

| 参数   | 类型 | 说明                       |
| :----- | :--- | -------------------------- |
| period | int  | 设置软狗检测时间，单位(s） |

* 返回值

返回软狗对象



###### 喂狗

> ​	**wdt.feed()**

喂狗

- 参数

无

* 返回值

0：成功

其它：失败



###### 关闭软狗

> ​	**wdt.stop()**

关闭软狗功能

- 参数

无

* 返回值

0：成功

其它：失败



###### 使用示例

```python
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


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_WDT_example"
PROJECT_VERSION = "1.0.0"

timer1 = Timer(Timer.Timer1)

def feed(t):
    wdt.feed()


if __name__ == '__main__':
    wdt = WDT(20)  # 启动看门狗，间隔时长
    timer1.start(period=15000, mode=timer1.PERIODIC, callback=feed)  # 使用定时器喂狗

    # wdt.stop()

```

##### KeyPad

模块功能:提供矩阵键盘接口，支持平台EC600SCN_LB/EC800N_CN_LA/EC600NCNLC/EC200U_CN_LB/EC600U_CN_LB/EC600M_CN_LA/EC800M_CN_LA/EC800M_CN_GA/EG912N_ENAA

EC200U最大支持4X3,EC600U最大支持6X6。

###### 创建keypad对象

> **keypad=machine.KeyPad(row,col)**
* 参数
| 参数   | 参数类型 | 参数说明                            |
| ------ | -------- | ----------------------------------- |
| row | int      | 大于0，不超过平台支持最大值 |
| col | int      | 大于0，不超过平台支持最大值|

注意:如果row和col均不设置,默认为4X4.

| 平台          | 最大行 | 最大列 |
| ------------- | ------ | ------ |
| EC800N/EC600N | 4      | 4      |
| EC600S        | 5      | 5      |
| EC200U        | 4      | 3      |
| EC600U        | 6      | 6      |
| EC600M        | 5      | 5      |
| EC800M        | 5      | 5      |
| EG912N        | 3      | 3      |

- 引脚说明

注意：当不使用全部引脚时，接线按行列号从小到大顺序接线，比如EC600M使用2x2矩阵键盘时，硬件使用49、51和48、50引脚。

| 平台   | 引脚                                                         |
| ------ | ------------------------------------------------------------ |
| EC600M | 行号（输出）对应引脚如下：<br/>行号0 – 引脚号49<br/>行号1 – 引脚号51<br/>行号2 – 引脚号53<br/>行号3 – 引脚号55<br/>行号4 – 引脚号56<br/>列号（输入）对应引脚如下：<br/>列号0 – 引脚号48<br/>列号1 – 引脚号50<br/>列号2 – 引脚号52<br/>列号3 – 引脚号54<br />列号4 – 引脚号57 |
| EC800M | 行号（输出）对应引脚如下：<br/>行号0 – 引脚号86<br/>行号1 – 引脚号76<br/>行号2 – 引脚号85<br/>行号3 – 引脚号82<br/>行号4 – 引脚号74<br/>列号（输入）对应引脚如下：<br/>列号0 – 引脚号87<br/>列号1 – 引脚号77<br/>列号2 – 引脚号84<br/>列号3 – 引脚号83<br/>列号4 – 引脚号75 |
| EG912N | 行号（输出）对应引脚如下：<br/>行号1 – 引脚号20<br/>行号2 – 引脚号16<br/>行号3 – 引脚号116<br/>列号（输入）对应引脚如下：<br/>列号2 – 引脚号105<br/>列号3 – 引脚号21<br/>列号4 – 引脚号1 |


* 示例：
> ```python
> >>>import machine
> >>>keypad=machine.KeyPad(2,3)		# 矩阵键盘设置为2行3列矩阵键盘
> >>>keypad=machine.KeyPad()  	 	# 不设置,默认设置为4行4列矩阵键盘
> >>>keypad=machine.KeyPad(2)  	 	# 行值设置为2,不设置列值,列值默认为4,2行4列矩阵键盘
> ```
>

###### 初始化keypad

> **keypad.init()**

初始化keypad设置。
* 参数
> 无

* 返回值

成功返回0，失败返回-1。

###### 设置回调函数

> **keypad.set_callback(usrFun)**

按键接入模组后，按放按键后触发回调函数设置。

* 参数

| 参数   | 参数类型 | 参数说明                                   |
| ------ | -------- | ------------------------------------------ |
| usrFun | function | 回调函数，当外接键盘按键按放会触发此函数。 |

注意:usrFun参数为list数据类型。

list包含三个参数。其含义如下：

list[0]: 1表示按下，0表示抬起

list[1] : row

list[2] : col

* 返回值

0

###### 解除初始化

> **keypad.deinit()**

释放初始化的资源和回调函数设置。

* 参数

无

* 返回值

成功返回0，失败返回-1。

###### 使用示例

```python
import machine
import utime
is_loop = 1
keypad=machine.KeyPad()  
keypad.init()
def userfun(l_list):
    global is_loop 
    if  l_list[0] != 1 :
        is_loop = 0
        print('will exit')
    print(l_list)
keypad.set_callback(userfun)
loop_num = 0
while is_loop == 1 and loop_num < 10:
    utime.sleep(5)
    loop_num = loop_num +1
    print(" running..... ",is_loop,loop_num)
keypad.deinit()
print('exit!')
```



#### qrcode- 二维码显示

模块功能：根据输入的内容，生成对应的二维码。

* 注意
  BC25PA平台不支持此模块功能。
  
  使用该功能前，需要初始化LCD
> ​	qrcode.show(qrcode_str,magnification,start_x,start_y,Background_color,Foreground_color)

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

##### 创建wake_lock锁

> ​	**lpm_fd = pm.create_wakelock(lock_name, name_size)**

创建wake_lock锁。

- 参数

| 参数      | 类型   | 说明            |
| :-------- | :----- | --------------- |
| lock_name | string | 自定义lock名    |
| name_size | int    | lock_name的长度 |

* 返回值

成功返回wakelock的标识号，否则返回-1。


* 注意
  BC25PA平台不支持此方法。

##### 删除wake_lock锁

> ​	**pm.delete_wakelock(lpm_fd)**

删除wake_lock锁。

- 参数

| 参数   | 类型 | 说明                   |
| :----- | :--- | ---------------------- |
| lpm_fd | int  | 需要删除的锁对应标识id |

* 返回值

成功返回0。

* 注意
  BC25PA平台不支持此方法。


##### 加锁

> ​	**pm.wakelock_lock(lpm_fd)**

- 参数

| 参数   | 类型 | 说明                             |
| :----- | :--- | -------------------------------- |
| lpm_fd | int  | 需要执行加锁操作的wakelock标识id |

* 返回值

成功返回0，否则返回-1。

* 注意
  BC25PA平台不支持此方法。


##### 释放锁

> ​	**pm.wakelock_unlock(lpm_fd)**

释放锁

- 参数

| 参数   | 类型 | 说明                               |
| :----- | :--- | ---------------------------------- |
| lpm_fd | int  | 需要执行释放锁操作的wakelock标识id |

* 返回值

成功返回0，否则返回-1。

* 注意
  BC25PA平台不支持此方法。

##### 自动休眠模式控制

> ​	**pm.autosleep(sleep_flag)**

自动休眠模式控制

- 参数

| 参数       | 类型 | 说明                           |
| :--------- | :--- | ------------------------------ |
| sleep_flag | int  | 0，关闭自动休眠；1开启自动休眠 |

* 返回值

成功返回0。



##### 获取已创建的锁数量

> ​	**pm.get_wakelock_num()**

获取已创建的锁数量

- 参数

无

* 返回值

返回已创建wakelock锁的数量。

* 注意
  BC25PA平台不支持此方法。



##### 设置PSM模式的控制时间

- 仅BC25平台支持

> **pm.set_psm_time(tau_uint,tau_time,act_uint,act_time)**  # 设置并启用PSM           <**模式1**>
>
> **pm.set_psm_time(mode)**														   # 单独设置启用或禁用    <**模式2**>


* 参数

| 参数     | 参数类型 | 参数说明                       |
| -------- | -------- | ------------------------------ |
| mode | int | 是否启用PSM:<br/>0 禁用PSM<br/>1 启用PSM<br/>2 禁用PSM并删除PSM的所有参数，如有默认值，则重置默认值。(注意此种模式禁用的情况下，如果要启用PSM必须用**模式1**，用**模式2**没有任何的意义,因为设置的TAU和ACT时间全部清零了)。 |
| tau_uint | int   | tau(T3412)定时器单位 |
| tau_time | int   | tau(T3412)定时器时间周期值 |
| act_uint | int   | act(T3324)定时器单位 |
| act_time | int   | act(T3324)定时器时间周期值 |

* tau定时器说明
|tau定时器单位值  | 类型 | 单位值说明                       |
| -------- | -------- | ------------------------------|
| 0 | int   | 10 分钟 |
| 1 | int   | 1 小时 |
| 2 | int   | 10 小时 |
| 3 | int   | 2 秒 |
| 4 | int   | 30 秒 |
| 5 | int   | 1 分钟 |
| 6 | int   | 320 小时 |
| 7 | int   | 定时器被停用 |

* act定时器单位说明
|act定时器单位值  | 类型 | 单位值说明                       |
| -------- | -------- | ------------------------------|
| 0 | int   | 2 秒 |
| 1 | int   | 1 分钟 |
| 2 | int   | 6 分钟 |
| 7 | int   | 定时器被停用 |

* 返回值

    True: 	成功
    False:	失败

* 注意
   仅BC25平台支持 

- 示例

```python
>>> import pm
>>> pm.set_psm_time(1,2,1,4)  #设置tau定时器周期为 1小时 * 2 = 2小时， act定时器周期值为 1分钟 * 4 = 4分钟。
True
>>>
```



##### 获取PSM模式的控制时间

- 仅BC25平台支持

> **pm.get_psm_time()**

* 参数d

  无

* 返回值

  成功：返回值为list类型，说明如下：
  |参数  | 类型 | 单位值说明                       |
| -------- | -------- | ------------------------------|
| list[0] | int   | mode说明: <br/>0-禁用PSM. <br/>1-启用PSM. <br/>2.禁用 PSM 并删除 PSM 的所有参数,若有默认值,则重置为默认值。 |
| list[1] | int   | tau定时器单位 |
| list[2] | int   | tau定时器时间周期值 |
| list[3] | int   | act定时器单位 |
| list[4] | int   | act定时器时间周期值 |
  失败：返回None.在禁用PSM时返回失败。
  
* 注意
    仅BC25平台支持

- 示例


```python
>>> pm.get_psm_time()

[1, 1, 1, 1, 2]


```



##### 使用示例

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

##### 支持的操作符

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



##### 编译并生成正则表达式对象

> ​	**ure.compile(regex)**

compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

- 参数

| 参数  | 类型   | 说明       |
| :---- | :----- | ---------- |
| regex | string | 正则表达式 |

* 返回值

返回 regex 对象



#####  匹配

> ​	**ure.match(regex, string)**

将正则表达式对象 与 string 匹配，匹配通常从字符串的起始位置进行

- 参数

| 参数   | 类型   | 说明                 |
| :----- | :----- | -------------------- |
| regex  | string | 正则表达式           |
| string | string | 需要匹配的字符串数据 |

* 返回值

匹配成功返回一个匹配的对象，否则返回None。



##### 查找

> ​	**ure.search(regex, string)**

ure.search 扫描整个字符串并返回第一个成功的匹配。

- 参数

| 参数   | 类型   | 说明                 |
| :----- | :----- | -------------------- |
| regex  | string | 正则表达式           |
| string | string | 需要匹配的字符串数据 |

* 返回值

匹配成功返回一个匹配的对象，否则返回None。



**Match 对象**

匹配由 match() 和 serach 方法返回的对象

##### 匹配单个字符串

> ​	**match.group(index)**

匹配的整个表达式的字符串

- 参数

| 参数  | 类型 | 说明                                                         |
| :---- | :--- | ------------------------------------------------------------ |
| index | int  | 正则表达式中，group()用来提出分组截获的字符串, index=0返回整体，根据编写的正则表达式进行获取，当分组不存在时会抛出异常 |

* 返回值

返回匹配的整个表达式的字符串


##### 使用示例

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



####  wifiScan - WiFi扫描

注意：支持wifiscan的平台: 1603/1606(不包含:600MCN_LC/800MCN_GC/800MCN_LC)/8910/8850.

##### 判断是否支持 wifiScan

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



##### 开启或关闭 wifiScan 功能

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



##### 获取 wifiScan 当前状态

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



##### 获取当前 wifiScan 功能配置

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
  | timeout       | 整型 | 该超时时间参数是上层应用的超时，当触发超时会主动上报已扫描到的热点信息，若在超时前扫描到设置的热点个数或达到底层扫频超时时间会自动上报热点信息。 |
  | round         | 整型 | 该参数是Wi-Fi扫描轮，达到扫描轮数后，会结束扫描并获取扫描结果。|
  | max_bssid_num | 整型 | 该参数是Wi-Fi扫描热点最大个，若底层扫描热点个数达到设置的最大个数，会结束扫描并获取扫描结果。|
  | scan_timeout  | 整型 | 该参数是底层Wi-Fi扫描热点超时时间，若底层扫描热点时间达到设置的超时时间，会结束扫描并获取扫描结果。|
  | priority      | 整型 | 该参数是Wi-Fi扫描业务优先级设置，0为ps优先，1为Wi-Fi优先。ps优先时，当有数据业务发起时会中断Wi-Fi扫描。Wi-Fi优先时，当有数据业务发起时，不会建立RRC连接，保障Wi-Fi扫描正常执行，扫描结束后才会建立RRC连接。 |

* 示例：

```python
>>> wifiScan.getConfig()
(6, 1, 5, 1, 0)
```



##### 设置当前 wifiScan 功能配置

> **wifiScan.setConfig(timeout, round, max_bssid_num, scan_timeout, priority)**

* 功能：

  设置 wifiScan 功能配置参数。

* 参数：

  | 参数          | 类型 | 说明                                                         |
  | ------------- | ---- | ------------------------------------------------------------ |
  | timeout       | 整型 | 该超时时间参数是上层应用的超时，当触发超时会主动上报已扫描到的热点信息，若在超时前扫描到设置的热点个数或达到底层扫频超时时间会自动上报热点信息。<br>参数范围：<br/>1603/1606平台 ：4-255秒<br/>8850/8910平台 ：120-5000毫秒 |
  | round         | 整型 | 该参数是wifi扫描轮，达到扫描轮数后，会结束扫描并获取扫描结果。<br/>参数范围：<br/>1603/1606平台 ：1-3轮次<br/>8850/8910平台 ：1-10轮次 |
  | max_bssid_num | 整型 | 该参数是wifi扫描热点最大个，若底层扫描热点个数达到设置的最大个数，会结束扫描并获取扫描结果。<br/>参数范围：<br/>1603平台 ：4-30个<br/>1606平台 ：4-10个<br/>8850/8910平台 ：1-30个 |
  | scan_timeout  | 整型 | 该参数是底层wifi扫描热点超时时间，若底层扫描热点时间达到设置的超时时间，会结束扫描并获取扫描结果。该参数设置范围为1-255秒。 |
  | priority      | 整型 | 该参数是wifi扫描业务优先级设置，0为ps优先，1为wifi优先。ps优先时，当有数据业务发起时会中断wifi扫描。Wifi优先时，当有数据业务发起时，不会建立RRC连接，保障wifi扫描正常执行，扫描结束后才会建立RRC连接。8850/8910平台不支持该参数，设置时写0即可。 |

* 返回值：

  成功返回整型0，失败返回整型-1。

* 示例：

```python
>>> wifiScan.setConfig(5, 2, 6, 3, 0)
0
```



##### 注册回调函数

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



##### 启动 wifiScan 扫描-异步接口

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



##### 启动 wifiScan 扫描-同步接口

> **wifiScan.start()**

* 功能：

  开始 wifiScan 扫描功能，扫描结束后直接返回扫描结果，由于是同步接口，所以扫描未结束时，程序会阻塞在该接口中，阻塞时间一般在0 ~ 2秒。

* 参数：

  无

* 返回值：

  成功返回扫描结果，失败或者错误返回整型-1。成功时返回值形式如下：

  `（wifi_nums, [(mac, rssi), ... , (mac, rssi)]）`

  | 参数      | 类型   | 说明                |
  | --------- | ------ | ------------------- |
  | wifi_nums | 整型   | 搜索到的 Wi-Fi 数量  |
  | mac       | 字符串 | 无线接入点的MAC地址 |
  | rssi      | 整型   | 信号强度            |

* 示例：

```python
>>> wifiScan.start()
(2, [('F0:B4:29:86:95:C7': -79),('44:00:4D:D5:26:E0', -92)])
```



#### ble - 蓝牙低功耗

模块功能：提供 BLE GATT Server 端（做从机）与 Client 端（做主机）功能，使用的是BLE 4.2版本协议。

注意：当前仅200U/600U模块支持BLE功能。

##### 开启 BLE GATT 功能

> **ble.gattStart()**

* 功能

  开启 BLE GATT 功能。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Server 综合示例
```



##### 关闭 BLE GATT 功能

> **ble.gattStop()**

* 功能

  关闭 BLE GATT 功能。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Server 综合示例
```



##### 获取 BLE GATT 状态

> **ble.getStatus()**

* 功能

  获取 BLE 的状态。

* 参数

  无

* 返回值

  0 - BLE处于停止状态

  1 - BLE已经正常开始

  -1 - 获取状态失败

* 示例

  无



##### 获取 BLE 的公共地址

> **ble.getPublicAddr()**

* 功能

  获取 BLE 协议栈正在使用的公共地址。该接口需要在BLE已经初始化完成并启动成功后才能调用，比如在回调中收到 event_id 为0的事件之后，即 start 成功后，去调用。

* 注意

  如果有出厂设置默认蓝牙MAC地址，那么该接口获取的MAC地址和默认的蓝牙MAC地址是一致的；如果没有设置，那么该接口获取的地址，将是蓝牙启动后随机生成的静态地址，因此在每次重新上电运行蓝牙时都不相同。

* 参数

  无

* 返回值

  执行成功返回bytearray类型的BLE地址，6字节，失败返回整型-1。

* 示例

```python
>>> addr = ble.getPublicAddr()
>>> print(addr)
b'\xdb3\xf5\x1ek\xac'
>>> mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
>>> print('mac = [{}]'.format(mac))
mac = [ac:6b:1e:f5:33:db]
```



##### BLE Server 初始化并注册回调函数

> **ble.serverInit(user_cb)**

* 功能

  初始化 BLE Server 并注册回调函数。

* 参数

| 参数    | 类型     | 说明     |
| ------- | -------- | -------- |
| user_cb | function | 回调函数 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

说明：

（1）回调函数的形式

```python
def ble_callback(args):
	event_id = args[0]  # 第一个参数固定是 event_id
	status = args[1] # 第二个参数固定是状态，表示某个操作的执行结果，比如ble开启成功还是失败
	......
```

（2）回调函数参数说明

​		args[0] 固定表示event_id，args[1] 固定表示状态，0表示成功，非0表示失败。回调函数的参数个数并不是固定2个，而是根据第一个参数args[0]来决定的，下表中列出了不同事件ID对应的参数个数及说明。

| event_id | 参数个数 | 参数说明                                                     |
| :------: | :------: | ------------------------------------------------------------ |
|    0     |    2     | args[0] ：event_id，表示 BT/BLE start<br>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    1     |    2     | args[0] ：event_id，表示 BT/BLE stop<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    16    |    4     | args[0] ：event_id，表示 BLE connect<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id<br/>args[3] ：addr，BT/BLE address，bytearray类型数据 |
|    17    |    4     | args[0] ：event_id，表示 BLE disconnect<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id，<br/>args[3] ：addr，BT/BLE address，bytearray类型数据 |
|    18    |    7     | args[0] ：event_id，表示 BLE update connection parameter<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id<br/>args[3] ：max_interval，最大的间隔，间隔：1.25ms，取值范围：6-3200，时间范围：7.5ms\ ~ 4s<br/>args[4] ：min_interval，最小的间隔，间隔：1.25ms，取值范围：6-3200，时间范围：7.5ms\ ~ 4s<br/>args[5] ：latency，从机忽略连接状态事件的时间。需满足：（1+latecy)\*max_interval\*2\*1.25<timeout\*10<br/>args[6] ：timeout，没有交互，超时断开时间，间隔：10ms，取值范围：10-3200ms，时间范围：100ms ~ 32s |
|    20    |    4     | args[0] ：event_id，表示 BLE connection mtu<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：handle<br/>args[3] ：mtu值 |
|    21    |    7     | args[0] ：event_id，表示 BLE server : when ble client write characteristic value or descriptor,server get the notice<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，获取数据的长度<br/>args[3] ：data，一个数组，存放获取的数据<br/>args[4] ：attr_handle，属性句柄，整型值<br/>args[5] ：short_uuid，整型值<br/>args[6] ：long_uuid，一个16字节数组，存放长UUID |
|    22    |    7     | args[0] ：event_id，表示 server : when ble client read characteristic value or descriptor,server get the notice<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，获取数据的长度<br/>args[3] ：data，一个数组，存放获取的数据<br/>args[4] ：attr_handle，属性句柄，整型值<br/>args[5] ：short_uuid，整型值<br/>args[6] ：long_uuid，一个16字节数组，存放长UUID |
|    25    |    2     | args[0] ：event_id，表示 server send notification,and recieve send end notice<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |

* 示例

```python 
def ble_callback(args):
    event_id = args[0]
    status = args[1]
    print('[ble_callback]: event_id={}, status={}'.format(event_id, status))

    if event_id == 0:  # ble start
        if status == 0:
            print('[callback] BLE start success.')
        else:
            print('[callback] BLE start failed.')
    elif event_id == 1:  # ble stop
        if status == 0:
            print('[callback] ble stop successful.')
        else:
            print('[callback] ble stop failed.')
    elif event_id == 16:  # ble connect
        if status == 0:
            print('[callback] ble connect successful.')
            connect_id = args[2]
            addr = args[3] # 这是一个bytearray类型
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))
        else:
            print('[callback] ble connect failed.')
    elif event_id == 17:  # ble disconnect
        if status == 0:
            print('[callback] ble disconnect successful.')
            connect_id = args[2]
            addr = args[3] # 这是一个bytearray类型
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))
        else:
            print('[callback] ble disconnect failed.')
            ble.gattStop()
            return
    elif event_id == 18:  # ble update connection parameter
        if status == 0:
            print('[callback] ble update parameter successful.')
            connect_id = args[2]
            max_interval = args[3]
            min_interval = args[4]
            latency = args[5]
            timeout = args[6]
            print('[callback] connect_id={},max_interval={},min_interval={},latency={},timeout={}'.format(connect_id, max_interval, min_interval, latency, timeout))
        else:
            print('[callback] ble update parameter failed.')
            ble.gattStop()
            return
    elif event_id == 20:  # ble connection mtu
        if status == 0:
            print('[callback] ble connect mtu successful.')
            handle = args[2]
            ble_mtu = args[3]
            print('[callback] handle = {:#06x}, ble_mtu = {}'.format(handle, ble_mtu))
        else:
            print('[callback] ble connect mtu failed.')
            ble.gattStop()
            return
    elif event_id == 21:  # server:when ble client write characteristic value or descriptor,server get the notice
        if status == 0:
            print('[callback] ble recv successful.')
            data_len = args[2]
            data = args[3]  # 这是一个bytearray类型
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # 这是一个bytearray类型
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv failed.')
            ble.gattStop()
            return
    elif event_id == 22:  # server:when ble client read characteristic value or descriptor,server get the notice
        if status == 0:
            print('[callback] ble recv read successful.')
            data_len = args[2]
            data = args[3]  # 这是一个bytearray类型
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # 这是一个bytearray类型
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv read failed.')
            ble.gattStop()
            return
    elif event_id == 25:  # server send notification,and recieve send end notice
        if status == 0:
            print('[callback] ble send data successful.')
        else:
            print('[callback] ble send data failed.')
    else:
        print('unknown event id.')

ble.serverInit(ble_callback)
```



##### BLE Server 资源释放

> **ble.serverRelease()**

* 功能

  BLE Server 资源释放。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见最后的综合示例
```



##### BLE Server 设置 BLE 名称

> **ble.setLocalName(code, name)**

* 功能

  设置 BLE 名称。

* 注意

  对于BLE，设备在广播时，如果希望扫描软件扫描时，能看到广播设备的名称，是需要在广播数据中包含蓝牙名称的，或者在扫描回复数据中包含设备名称。

* 参数

  | 参数 | 类型   | 说明                               |
  | ---- | ------ | ---------------------------------- |
  | code | 整型   | 编码模式<br>0 - UTF8<br/>1 - GBK   |
  | name | string | BLE 名称，名称最长不能超过29个字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
>>> ble.setLocalName(0, 'QuecPython-BLE')
0
```



##### BLE Server 设置广播参数

> **ble.setAdvParam(min_adv,max_adv,adv_type,addr_type,channel,filter_policy,discov_mode,no_br_edr,enable_adv)**

* 功能

  设置广播参数。

* 参数

  | 参数          | 类型       | 说明                                                         |
  | ------------- | ---------- | ------------------------------------------------------------ |
  | min_adv       | 无符号整型 | 最小广播间隔，范围0x0020-0x4000，计算如下：<br>时间间隔 = min_adv \* 0.625，单位ms |
  | max_adv       | 无符号整型 | 最大广播间隔，范围0x0020-0x4000，计算如下：<br/>时间间隔 = max_adv \* 0.625，单位ms |
  | adv_type      | 无符号整型 | 广播类型，取值范围如下：<br>0 - 可连接的非定向广播，默认选择<br>1 - 可连接高占空比的定向广播<br>2 - 可扫描的非定向广播<br>3 - 不可连接的非定向广播<br>4 - 可连接低占空比的定向广播 |
  | addr_type     | 无符号整型 | 本地地址类型，取值范围如下：<br>0 - 公共地址<br>1 - 随机地址 |
  | channel       | 无符号整型 | 广播通道，取值范围如下：<br>1 - 37信道<br>2 - 38信道<br>4 - 39信道<br>7 - 上述3个通道都选择，默认该选项 |
  | filter_policy | 无符号整型 | 广播过滤策略，取值范围如下：<br>0 - 处理所有设备的扫描和连接请求<br/>1 - 处理所有设备的连接请求和只处理白名单设备的扫描请求（暂不支持）<br/>2 - 处理所有设备的扫描请求和只处理白名单设备的连接请求（暂不支持）<br/>3 - 只处理白名单设备的连接和扫描请求（暂不支持） |
  | discov_mode   | 无符号整型 | 发现模式，GAP协议使用，默认为2<br/>1 - 有限可发现模式<br/>2 - 一般可发现模式 |
  | no_br_edr     | 无符号整型 | 不用BR/EDR，默认为1，如果用则为0                             |
  | enable_adv    | 无符号整型 | 使能广播，默认为1，不使能则为0                               |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
def ble_gatt_set_param():
    min_adv = 0x300
    max_adv = 0x320
    adv_type = 0  # 可连接的非定向广播，默认选择
    addr_type = 0  # 公共地址
    channel = 0x07
    filter_strategy = 0  # 处理所有设备的扫描和连接请求
    discov_mode = 2
    no_br_edr = 1
    enable_adv = 1
    ret = ble.setAdvParam(min_adv, max_adv, adv_type, addr_type, channel, filter_strategy, discov_mode, no_br_edr, enable_adv)
    if ret != 0:
        print('ble_gatt_set_param failed.')
        return -1
    print('ble_gatt_set_param success.')
    return 0
```



##### BLE Server 设置广播数据内容

> **ble.setAdvData(data)**

* 功能

  设置广播数据内容。

* 参数

  | 参数 | 类型 | 说明                                                         |
  | ---- | ---- | ------------------------------------------------------------ |
  | data | 数组 | 广播数据，广播数据最长不超过31个字节。注意该参数的类型，程序中组织好广播数据后，需要通过bytearray()来转换，然后才能传入接口，具体处理参考下面的示例。<br>关于广播数据的格式说明：<br>广播数据的内容，采用 length+type+data 的格式。一条广播数据中可以包含多个这种格式数据的组合，比如示例中就包含了两个，第一个是 "0x02, 0x01, 0x05"，0x02表示后面有两个数据，分别是0x01和0x05，0x01即type，0x05表示具体数据；第二个是ble名称长度加1（因为还要包含一个表示type的数据，所以长度需要加1）得到的长度、type 0x09以及name对应的具体编码值表示的data组成的。<br>关于type具体值代表的含义，请参考如下连接：<br/>[Generic Access Pfofile](https://btprodspecificationrefs.blob.core.windows.net/assigned-numbers/Assigned%20Number%20Types/Generic%20Access%20Profile.pdf) |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
def ble_gatt_set_data():
    adv_data = [0x02, 0x01, 0x05]
    ble_name = "Quectel_ble"
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvData(data)
    if ret != 0:
        print('ble_gatt_set_data failed.')
        return -1
    print('ble_gatt_set_data success.')
    return 0
```



##### BLE Server 设置扫描回复数据

> **ble.setAdvRspData(data)**

* 功能

  设置扫描回复数据。

* 参数

  | 参数 | 类型 | 说明                                                         |
  | ---- | ---- | ------------------------------------------------------------ |
  | data | 数组 | 扫描回复数据，数据最长不超过31个字节，注意事项和上面设置广播数据内容接口描述一致。当client设备扫描方式为积极扫描时，设置扫描回复数据才有意义。 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
def ble_gatt_set_rsp_data():
    adv_data = []
    ble_name = "Quectel_ble"
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_rsp_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvRspData(data)
    if ret != 0:
        print('ble_gatt_set_rsp_data failed.')
        return -1
    print('ble_gatt_set_rsp_data success.')
    return 0
```



##### BLE Server 增加一个服务

> **ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)**

* 功能

  增加一个服务。

* 参数

  | 参数      | 类型       | 说明                                                         |
  | --------- | ---------- | ------------------------------------------------------------ |
  | primary   | 无符号整型 | 服务类型，1为主要服务，其他为次要服务                        |
  | server_id | 无符号整型 | 服务ID，用来确定某一个服务                                   |
  | uuid_type | 无符号整型 | uuid类型<br>0 - 长UUID，128bit<br>1 - 短UUID，16bit          |
  | uuid_s    | 无符号整型 | 短UUID，2个字节（16bit），当uuid_type为0时，该值给0          |
  | uuid_l    | 数组       | 长UUID，16个字节（128bit），当uuid_type为1时，该值给 bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
def ble_gatt_add_service():
    primary = 1
    server_id = 0x01
    uuid_type = 1  # 短UUID
    uuid_s = 0x180F
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_service failed.')
        return -1
    print('ble_gatt_add_service success.')
    return 0
```



##### BLE Server 在服务里增加一个特征

> **ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)**

* 功能

  在服务里增加一个特征。

* 参数

  | 参数       | 类型       | 说明                                                         |
  | ---------- | ---------- | ------------------------------------------------------------ |
  | server_id  | 无符号整型 | 服务ID，用来确定某一个服务                                   |
  | chara_id   | 无符号整型 | 特征ID                                                       |
  | chara_prop | 无符号整型 | 特征的属性，十六进制数，可通过“或运算”同时指定多个属性，描述如下：<br>0x01 - 广播<br/>0x02 - 可读<br/>0x04 - 可写且不需要链路层应答<br/>0x08 - 可写<br/>0x10 - 通知<br/>0x20 - 指示<br/>0x40 - 认证签名写<br/>0x80 - 扩展属性 |
  | uuid_type  | 无符号整型 | uuid类型<br/>0 - 长UUID，128bit<br/>1 - 短UUID，16bit        |
  | uuid_s     | 无符号整型 | 短UUID，2个字节（16bit）                                     |
  | uuid_l     | 数组       | 长UUID，16个字节（128bit）                                   |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
def ble_gatt_add_characteristic():
    server_id = 0x01
    chara_id = 0x01
    chara_prop = 0x02 | 0x10 | 0x20  # 0x02-可读 0x10-通知 0x20-指示
    uuid_type = 1  # 短UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_characteristic failed.')
        return -1
    print('ble_gatt_add_characteristic success.')
    return 0
```



##### BLE Server 在特征里增加一个特征值

> **ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)**

* 功能

  在特征里增加一个特征值。

* 参数

  | 参数       | 类型       | 说明                                                         |
  | ---------- | ---------- | ------------------------------------------------------------ |
  | server_id  | 无符号整型 | 服务ID，用来确定某一个服务                                   |
  | chara_id   | 无符号整型 | 特征ID                                                       |
  | permission | 无符号整型 | 特征值的权限，2个字节，十六进制数，可通过“或运算”同时指定多个属性，描述如下：<br/>0x0001 - 可读权限<br/>0x0002 - 可写权限<br/>0x0004 - 读需要认证<br/>0x0008 - 读需要授权<br/>0x0010 - 读需要加密<br/>0x0020 - 读需要授权认证<br/>0x0040 - 写需要认证<br/>0x0080 - 写需要授权<br/>0x0100 - 写需要加密<br/>0x0200 - 写需要授权认证 |
  | uuid_type  | 无符号整型 | uuid类型<br/>0 - 长UUID，128bit<br/>1 - 短UUID，16bit        |
  | uuid_s     | 无符号整型 | 短UUID，2个字节（16bit）                                     |
  | uuid_l     | 数组       | 长UUID，16个字节（128bit）                                   |
  | value      | 数组       | 特征值数据                                                   |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
def ble_gatt_add_characteristic_value():
    data = []
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # 短UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    for i in range(0, 244):
        data.append(0x00)
    value = bytearray(data)
    ret = ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_value failed.')
        return -1
    print('ble_gatt_add_characteristic_value success.')
    return 0
```



##### BLE Server 在特征里增加一个特征描述

> **ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)**

* 功能

  在特征里增加一个特征描述，注意特征描述和特征值同属与一个特征。

* 参数

  | 参数       | 类型       | 说明                                                         |
  | ---------- | ---------- | ------------------------------------------------------------ |
  | server_id  | 无符号整型 | 服务ID，用来确定某一个服务                                   |
  | chara_id   | 无符号整型 | 特征ID                                                       |
  | permission | 无符号整型 | 特征值的权限，2个字节，十六进制数，可通过“或运算”同时指定多个属性：<br/>0x0001 - 可读权限<br/>0x0002 - 可写权限<br/>0x0004 - 读需要认证<br/>0x0008 - 读需要授权<br/>0x0010 - 读需要加密<br/>0x0020 - 读需要授权认证<br/>0x0040 - 写需要认证<br/>0x0080 - 写需要授权<br/>0x0100 - 写需要加密<br/>0x0200 - 写需要授权认证 |
  | uuid_type  | 无符号整型 | uuid类型<br/>0 - 长UUID，128bit<br/>1 - 短UUID，16bit        |
  | uuid_s     | 无符号整型 | 短UUID，2个字节（16bit）                                     |
  | uuid_l     | 数组       | 长UUID，16个字节（128bit）                                   |
  | value      | 数组       | 特征描述数据                                                 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
def ble_gatt_add_characteristic_desc():
    data = [0x00, 0x00]
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # 短UUID
    uuid_s = 0x2902
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    value = bytearray(data)
    ret = ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_desc failed.')
        return -1
    print('ble_gatt_add_characteristic_desc success.')
    return 0
```



##### BLE Server 增加服务完成或删除增加的服务

> **ble.addOrClearService(option, mode)**

* 功能

  增加服务完成，或者删除增加的服务。

* 参数

  | 参数   | 类型       | 说明                                                         |
  | ------ | ---------- | ------------------------------------------------------------ |
  | option | 无符号整型 | 操作类型，取值范围如下：<br>0 - 删除服务<br/>1 - 增加服务完成 |
  | mode   | 无符号整型 | 保留系统服务模式，取值范围如下：<br/>0 - 删除系统默认的GAP和GATT服务<br/>1 - 保留系统默认的GAP和GATT服务 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Server 综合示例
```



##### BLE Server 发送通知

> **ble.sendNotification(connect_id, attr_handle, value)**

* 功能

  发送通知。

* 参数

  | 参数        | 类型       | 说明                                  |
  | ----------- | ---------- | ------------------------------------- |
  | connect_id  | 无符号整型 | 连接ID                                |
  | attr_handle | 无符号整型 | 属性句柄                              |
  | value       | 数组       | 要发送的数据，发送数据长度不要超过MTU |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
参考最后的综合示例
```



##### BLE Server 发送指示

> **ble.sendIndication(connect_id, attr_handle, value)**

* 功能

  发送指示。

* 参数

  | 参数        | 类型       | 说明                                  |
  | ----------- | ---------- | ------------------------------------- |
  | connect_id  | 无符号整型 | 连接ID                                |
  | attr_handle | 无符号整型 | 属性句柄                              |
  | value       | 数组       | 要发送的数据，发送数据长度不要超过MTU |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Server 综合示例
```



##### BLE Server 开启广播

> **ble.advStart()**

* 功能

  开启广播。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。




##### BLE Server 停止广播

> **ble.advStop()**

* 功能

  停止广播。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。



##### BLE Server 综合示例

```python
# -*- coding: UTF-8 -*-

import ble
import utime


BLE_GATT_SYS_SERVICE = 0  # 0-删除系统默认的GAP和GATT服务  1-保留系统默认的GAP和GATT服务
BLE_SERVER_HANDLE = 0
_BLE_NAME = "Quectel_ble"


event_dict = {
    'BLE_START_STATUS_IND': 0,  # ble start
    'BLE_STOP_STATUS_IND': 1,   # ble stop
    'BLE_CONNECT_IND': 16,  # ble connect
    'BLE_DISCONNECT_IND': 17,   # ble disconnect
    'BLE_UPDATE_CONN_PARAM_IND': 18,    # ble update connection parameter
    'BLE_SCAN_REPORT_IND': 19,  # ble gatt client scan and report other devices
    'BLE_GATT_MTU': 20, # ble connection mtu
    'BLE_GATT_RECV_WRITE_IND': 21, # when ble client write characteristic value or descriptor,server get the notice
    'BLE_GATT_RECV_READ_IND': 22, # when ble client read characteristic value or descriptor,server get the notice
    'BLE_GATT_RECV_NOTIFICATION_IND': 23,   # client receive notification
    'BLE_GATT_RECV_INDICATION_IND': 24, # client receive indication
    'BLE_GATT_SEND_END': 25, # server send notification,and receive send end notice
}

class EVENT(dict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        raise ValueError("{} is read-only.".format(key))


event = EVENT(event_dict)


def ble_callback(args):
    global BLE_GATT_SYS_SERVICE
    global BLE_SERVER_HANDLE
    event_id = args[0]
    status = args[1]
    print('[ble_callback]: event_id={}, status={}'.format(event_id, status))

    if event_id == event.BLE_START_STATUS_IND:  # ble start
        if status == 0:
            print('[callback] BLE start success.')
            mac = ble.getPublicAddr()
            if mac != -1 and len(mac) == 6:
                addr = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(mac[5], mac[4], mac[3], mac[2], mac[1], mac[0])
                print('BLE public addr : {}'.format(addr))
            ret = ble_gatt_set_name()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_set_param()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_set_data()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_set_rsp_data()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_service()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_characteristic()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_characteristic_value()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_characteristic_desc()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_service_complete()
            if ret != 0:
                ble_gatt_close()
                return
            if BLE_GATT_SYS_SERVICE == 0:
                BLE_SERVER_HANDLE = 1
            else:
                BLE_SERVER_HANDLE = 16
            ret = ble_adv_start()
            if ret != 0:
                ble_gatt_close()
                return
        else:
            print('[callback] BLE start failed.')
    elif event_id == event.BLE_STOP_STATUS_IND:  # ble stop
        if status == 0:
            print('[callback] ble stop successful.')
            ble_status = ble.getStatus()
            print('ble status is {}'.format(ble_status))
            ble_gatt_server_release()
        else:
            print('[callback] ble stop failed.')
    elif event_id == event.BLE_CONNECT_IND:  # ble connect
        if status == 0:
            print('[callback] ble connect successful.')
            connect_id = args[2]
            addr = args[3]
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))

            ret = ble_gatt_send_notification()
            if ret == 0:
                print('[callback] ble_gatt_send_notification successful.')
            else:
                print('[callback] ble_gatt_send_notification failed.')
                ble_gatt_close()
                return
        else:
            print('[callback] ble connect failed.')
    elif event_id == event.BLE_DISCONNECT_IND:  # ble disconnect
        if status == 0:
            print('[callback] ble disconnect successful.')
            connect_id = args[2]
            addr = args[3]
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            ble_gatt_close()
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))
        else:
            print('[callback] ble disconnect failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_UPDATE_CONN_PARAM_IND:  # ble update connection parameter
        if status == 0:
            print('[callback] ble update parameter successful.')
            connect_id = args[2]
            max_interval = args[3]
            min_interval = args[4]
            latency = args[5]
            timeout = args[6]
            print('[callback] connect_id={},max_interval={},min_interval={},latency={},timeout={}'.format(connect_id, max_interval, min_interval, latency, timeout))
        else:
            print('[callback] ble update parameter failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_MTU:  # ble connection mtu
        if status == 0:
            print('[callback] ble connect mtu successful.')
            handle = args[2]
            ble_mtu = args[3]
            print('[callback] handle = {:#06x}, ble_mtu = {}'.format(handle, ble_mtu))
        else:
            print('[callback] ble connect mtu failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_RECV_WRITE_IND:
        if status == 0:
            print('[callback] ble recv successful.')
            data_len = args[2]
            data = args[3]  # 这是一个bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # 这是一个bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_RECV_READ_IND:
        if status == 0:
            print('[callback] ble recv read successful.')
            data_len = args[2]
            data = args[3]  # 这是一个bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # 这是一个bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv read failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_SEND_END:
        if status == 0:
            print('[callback] ble send data successful.')
        else:
            print('[callback] ble send data failed.')
    else:
        print('unknown event id.')


def ble_gatt_server_init(cb):
    ret = ble.serverInit(cb)
    if ret != 0:
        print('ble_gatt_server_init failed.')
        return -1
    print('ble_gatt_server_init success.')
    return 0


def ble_gatt_server_release():
    ret = ble.serverRelease()
    if ret != 0:
        print('ble_gatt_server_release failed.')
        return -1
    print('ble_gatt_server_release success.')
    return 0


def ble_gatt_open():
    ret = ble.gattStart()
    if ret != 0:
        print('ble_gatt_open failed.')
        return -1
    print('ble_gatt_open success.')
    return 0


def ble_gatt_close():
    ret = ble.gattStop()
    if ret != 0:
        print('ble_gatt_close failed.')
        return -1
    print('ble_gatt_close success.')
    return 0


def ble_gatt_set_name():
    code = 0  # utf8
    name = _BLE_NAME
    ret = ble.setLocalName(code, name)
    if ret != 0:
        print('ble_gatt_set_name failed.')
        return -1
    print('ble_gatt_set_name success.')
    return 0


def ble_gatt_set_param():
    min_adv = 0x300
    max_adv = 0x320
    adv_type = 0  # 可连接的非定向广播，默认选择
    addr_type = 0  # 公共地址
    channel = 0x07
    filter_strategy = 0  # 处理所有设备的扫描和连接请求
    discov_mode = 2
    no_br_edr = 1
    enable_adv = 1
    ret = ble.setAdvParam(min_adv, max_adv, adv_type, addr_type, channel, filter_strategy, discov_mode, no_br_edr, enable_adv)
    if ret != 0:
        print('ble_gatt_set_param failed.')
        return -1
    print('ble_gatt_set_param success.')
    return 0


def ble_gatt_set_data():
    adv_data = [0x02, 0x01, 0x05]
    ble_name = _BLE_NAME
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvData(data)
    if ret != 0:
        print('ble_gatt_set_data failed.')
        return -1
    print('ble_gatt_set_data success.')
    return 0


def ble_gatt_set_rsp_data():
    adv_data = []
    ble_name = _BLE_NAME
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_rsp_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvRspData(data)
    if ret != 0:
        print('ble_gatt_set_rsp_data failed.')
        return -1
    print('ble_gatt_set_rsp_data success.')
    return 0


def ble_gatt_add_service():
    primary = 1
    server_id = 0x01
    uuid_type = 1  # 短UUID
    uuid_s = 0x180F
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_service failed.')
        return -1
    print('ble_gatt_add_service success.')
    return 0


def ble_gatt_add_characteristic():
    server_id = 0x01
    chara_id = 0x01
    chara_prop = 0x02 | 0x10 | 0x20  # 0x02-可读 0x10-通知 0x20-指示
    uuid_type = 1  # 短UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_characteristic failed.')
        return -1
    print('ble_gatt_add_characteristic success.')
    return 0


def ble_gatt_add_characteristic_value():
    data = []
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # 短UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    for i in range(0, 244):
        data.append(0x00)
    value = bytearray(data)
    ret = ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_value failed.')
        return -1
    print('ble_gatt_add_characteristic_value success.')
    return 0


def ble_gatt_add_characteristic_desc():
    data = [0x00, 0x00]
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # 短UUID
    uuid_s = 0x2902
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    value = bytearray(data)
    ret = ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_desc failed.')
        return -1
    print('ble_gatt_add_characteristic_desc success.')
    return 0


def ble_gatt_send_notification():
    global BLE_SERVER_HANDLE
    data = [0x39, 0x39, 0x39, 0x39, 0x39]  # 测试数据
    conn_id = 0
    attr_handle = BLE_SERVER_HANDLE + 2
    value = bytearray(data)
    ret = ble.sendNotification(conn_id, attr_handle, value)
    if ret != 0:
        print('ble_gatt_send_notification failed.')
        return -1
    print('ble_gatt_send_notification success.')
    return 0


def ble_gatt_add_service_complete():
    global BLE_GATT_SYS_SERVICE
    ret = ble.addOrClearService(1, BLE_GATT_SYS_SERVICE)
    if ret != 0:
        print('ble_gatt_add_service_complete failed.')
        return -1
    print('ble_gatt_add_service_complete success.')
    return 0


def ble_gatt_clear_service_complete():
    global BLE_GATT_SYS_SERVICE
    ret = ble.addOrClearService(0, BLE_GATT_SYS_SERVICE)
    if ret != 0:
        print('ble_gatt_clear_service_complete failed.')
        return -1
    print('ble_gatt_clear_service_complete success.')
    return 0


def ble_adv_start():
    ret = ble.advStart()
    if ret != 0:
        print('ble_adv_start failed.')
        return -1
    print('ble_adv_start success.')
    return 0


def ble_adv_stop():
    ret = ble.advStop()
    if ret != 0:
        print('ble_adv_stop failed.')
        return -1
    print('ble_adv_stop success.')
    return 0


def main():
    ret = ble_gatt_server_init(ble_callback)
    if ret == 0:
        ret = ble_gatt_open()
        if ret != 0:
            return -1
    else:
        return -1
    count = 0
    while True:
        utime.sleep(1)
        count += 1
        if count % 5 == 0:
            print('##### BLE running, count = {}......'.format(count))
        if count > 120:
            count = 0
            print('!!!!! stop BLE now !!!!!')
            ble_gatt_close()
            return 0


if __name__ == '__main__':
    main()

```



##### BLE Client 初始化并注册回调函数

> **ble.clientInit(user_cb)**

* 功能

  初始化 BLE Client 并注册回调函数。

* 参数

| 参数    | 类型     | 说明     |
| ------- | -------- | -------- |
| user_cb | function | 回调函数 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

说明：

（1）回调函数的形式

```python
def ble_callback(args):
	event_id = args[0]  # 第一个参数固定是 event_id
	status = args[1] # 第二个参数固定是状态，表示某个操作的执行结果，比如ble开启成功还是失败
	......
```

（2）回调函数参数说明

​		args[0] 固定表示event_id，args[1] 固定表示状态，0表示成功，非0表示失败。回调函数的参数个数并不是固定2个，而是根据第一个参数args[0]来决定的，下表中列出了不同事件ID对应的参数个数及说明。

| event_id | 参数个数 | 参数说明                                                     |
| :------: | :------: | ------------------------------------------------------------ |
|    0     |    2     | args[0] ：event_id，表示 BT/BLE start<br>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    1     |    2     | args[0] ：event_id，表示 BT/BLE stop<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    16    |    4     | args[0] ：event_id，表示 BLE connect<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id<br/>args[3] ：addr，BT/BLE address，bytearray类型数据 |
|    17    |    4     | args[0] ：event_id，表示 BLE disconnect<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id，<br/>args[3] ：addr，BT/BLE address，bytearray类型数据 |
|    18    |    7     | args[0] ：event_id，表示 BLE update connection parameter<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：connect_id<br/>args[3] ：max_interval，最大的间隔，间隔：1.25ms，取值范围：6-3200，时间范围：7.5ms ~ 4s<br/>args[4] ：min_interval，最小的间隔，间隔：1.25ms，取值范围：6-3200，时间范围：7.5ms ~ 4s<br/>args[5] ：latency，从机忽略连接状态事件的时间。需满足：（1+latecy)\*max_interval\*2\*1.25<timeout\*10<br/>args[6] ：timeout，没有交互，超时断开时间，间隔：10ms，取值范围：10-3200，时间范围：100ms ~ 32s |
|    19    |    9     | args[0] ：event_id，表示 BLE scan report<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：event_type<br/>args[3] ：扫描到的设备名称<br/>args[4] ：设备地址类型<br/>args[5] ：设备地址，bytearray类型数据<br/>args[6] ：rssi，信号强度<br/>args[7] ：data_len，扫描的原始数据长度<br/>args[8] ：data，扫描的原始数据 |
|    20    |    4     | args[0] ：event_id，表示 BLE connection mtu<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：handle<br/>args[3] ：mtu值 |
|    23    |    4     | args[0] ：event_id，表示 client recieve notification，即接收通知<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，包含句柄等数据的原始数据，数据格式及解析见最后的综合示例程序 |
|    24    |    4     | args[0] ：event_id，表示 client recieve indication，即接收指示<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，包含indication的原始数据，数据格式及解析见最后的综合示例程序 |
|    26    |    2     | args[0] ：event_id，表示 start discover service，即开始查找服务<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    27    |    5     | args[0] ：event_id，表示 discover service，即查找到服务<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：start_handle，表示service的开始句柄<br/>args[3] ：end_handle，表示service的结束句柄<br/>args[4] ：UUID，表示service的UUID（短UUID） |
|    28    |    4     | args[0] ：event_id，表示 discover characteristic，即查找服务特征<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，包含句柄、属性、UUID等数据的原始数据，数据格式及解析见最后的综合示例程序 |
|    29    |    4     | args[0] ：event_id，表示 discover characteristic descriptor，即查找特征描述<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，包含句柄、UUID等数据的原始数据，数据格式及解析见最后的综合示例程序 |
|    30    |    2     | args[0] ：event_id，表示 write characteristic value with response，即写入特征值并需要链路层确认<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    31    |    2     | args[0] ：event_id，表示 write characteristic value without response，即写入特征值，无需链路层确认<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    32    |    4     | args[0] ：event_id，表示 read characteristic value by handle，即通过句柄来读取特征值<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，原始数据 |
|    33    |    4     | args[0] ：event_id，表示 read characteristic value by uuid，即通过UUID来读取特征值<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，原始数据 |
|    34    |    4     | args[0] ：event_id，表示 read miltiple characteristic value，即读取多个特征值<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，原始数据 |
|    35    |    2     | args[0] ：event_id，表示 wirte characteristic descriptor，即写入特征描述，需链路层确认<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败 |
|    36    |    4     | args[0] ：event_id，表示 read characteristic descriptor，即读特征描述<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：data_len，数据长度<br/>args[3] ：data，原始数据 |
|    37    |    3     | args[0] ：event_id，表示 attribute error，即属性错误<br/>args[1] ：status，表示操作的状态，0-成功，非0-失败<br/>args[2] ：errcode，错误码 |

* 示例

```
见 BLE Client 综合示例
```



##### BLE Client 资源释放

> **ble.clientRelease()**

* 功能

  BLE Client 资源释放。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 设置扫描参数

> **ble.setScanParam(scan_mode, interval, scan_window, filter_policy, addr_type)**

* 功能

  设置扫描参数。

* 参数

| 参数          | 类型       | 说明                                                         |
| ------------- | ---------- | ------------------------------------------------------------ |
| scan_mode     | 无符号整型 | 扫描模式，默认为积极扫描：<br>0 - 消极扫描<br/>1 - 积极扫描，广播端设置的扫描回复数据才会有意义 |
| interval      | 无符号整型 | 扫描间隔，范围0x0004-0x4000，计算如下：<br/>时间间隔 = interval \* 0.625，单位ms |
| scan_window   | 无符号整型 | 一次扫描的时间，范围0x0004-0x4000，计算如下：<br/>扫描时间 = scan_window\* 0.625，单位ms |
| filter_policy | 无符号整型 | 扫描过滤策略，默认为0：<br>0 - 除了不是本设备的定向广播，其他所有的广播包<br>1 - 除了不是本设备的定向广播，白名单设备的广播包<br>2 - 非定向广播，指向本设备的定向广播或使用Resolvable private address的定向广播<br/>3 - 白名单设备非定向广播，指向本设备的定向广播或使用Resolvable private address的定向广播 |
| addr_type     | 无符号整型 | 本地地址类型，取值范围如下：<br>0 - 公共地址<br>1 - 随机地址 |

* 注意

  关于参数 interval 和 scan_window 要注意的是，扫描时间 scan_window 不能大于扫描间隔 interval ，如果两者相等，则表示连续不停的扫描，此时 BLE 的 Controller 会连续运行扫描，占满系统资源而导致无法执行其他任务，所以不允许设置连续扫描。并且不建议将时间设置的太短，扫描越频繁则功耗越高。

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 开始扫描

> **ble.scanStart()**

* 功能

  开始扫描。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 停止扫描

> **ble.scanStop()**

* 功能

  停止扫描。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 扫描过滤开关

> **ble.setScanFilter(act)**

* 功能

  打开或者关闭扫描过滤开关。如果打开，那么扫描设备的广播数据时，同一个设备的广播数据只会上报一次；如果关闭，则同一个设备的所有的广播数据都会上报。默认打开过滤功能。

* 参数

  | 参数 | 类型       | 说明                                          |
  | ---- | ---------- | --------------------------------------------- |
  | act  | 无符号整型 | 0 - 关闭扫描过滤功能<br/>1 - 打开扫描过滤功能 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 建立连接

> **ble.connect(addr_type, addr)**

* 功能

  根据指定的设备地址去连接设备。

* 参数

  | 参数      | 类型       | 说明                                     |
  | --------- | ---------- | ---------------------------------------- |
  | addr_type | 无符号整型 | 地址类型<br>0 - 公共地址<br>1 - 随机地址 |
  | addr      | 数组       | BLE地址，6字节                           |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 取消正在建立的连接

> **ble.cancelConnect(addr)**

* 功能

  取消正在建立的连接。

* 参数

  | 参数 | 类型 | 说明           |
  | ---- | ---- | -------------- |
  | addr | 数组 | BLE地址，6字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
无
```



##### BLE Client 断开已建立的连接

> **ble.disconnect(connect_id)**

* 功能

  断开已建立的连接。

* 参数

  | 参数       | 类型       | 说明                           |
  | ---------- | ---------- | ------------------------------ |
  | connect_id | 无符号整型 | 连接ID，建立连接时得到的连接ID |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见综合示例
```



##### BLE Client 扫描所有的服务

> **ble.discoverAllService(connect_id)**

* 功能

  扫描所有的服务。

* 参数

  | 参数       | 类型       | 说明                           |
  | ---------- | ---------- | ------------------------------ |
  | connect_id | 无符号整型 | 连接ID，建立连接时得到的连接ID |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 扫描指定UUID的服务

> **ble.discoverByUUID(connect_id, uuid_type, uuid_s, uuid_l)**

* 功能

  扫描指定UUID的服务。

* 参数

  | 参数       | 类型       | 说明                                                         |
  | ---------- | ---------- | ------------------------------------------------------------ |
  | connect_id | 无符号整型 | 连接ID，建立连接时得到的连接ID                               |
  | uuid_type  | 无符号整型 | uuid类型<br>0 - 长UUID，128bit<br>1 - 短UUID，16bit          |
  | uuid_s     | 无符号整型 | 短UUID，2个字节（16bit），当uuid_type为0时，该值给0          |
  | uuid_l     | 数组       | 长UUID，16个字节（128bit），当uuid_type为1时，该值给 bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 扫描所有的引用

> **ble.discoverAllIncludes(connect_id, start_handle, end_handle)**

* 功能

  扫描所有的引用，start_handle和end_handle要属于同一个服务。

* 参数

  | 参数         | 类型       | 说明                             |
  | ------------ | ---------- | -------------------------------- |
  | connect_id   | 无符号整型 | 连接ID，建立连接时得到的连接ID   |
  | start_handle | 无符号整型 | 开始句柄，从这个句柄开始寻找引用 |
  | end_handle   | 无符号整型 | 结束句柄，从这个句柄结束寻找引用 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
无
```



##### BLE Client 扫描所有的特征

> **ble.discoverAllChara(connect_id, start_handle, end_handle)**

* 功能

  扫描所有的特征，start_handle和end_handle要属于同一个服务。

* 参数

  | 参数         | 类型       | 说明                             |
  | ------------ | ---------- | -------------------------------- |
  | connect_id   | 无符号整型 | 连接ID，建立连接时得到的连接ID   |
  | start_handle | 无符号整型 | 开始句柄，从这个句柄开始寻找特征 |
  | end_handle   | 无符号整型 | 结束句柄，从这个句柄结束寻找特征 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 扫描所有特征的描述

> **ble.discoverAllCharaDesc(connect_id, start_handle, end_handle)**

* 功能

  扫描所有特征的描述，start_handle和end_handle要属于同一个服务。

* 参数

  | 参数         | 类型       | 说明                                 |
  | ------------ | ---------- | ------------------------------------ |
  | connect_id   | 无符号整型 | 连接ID，建立连接时得到的连接ID       |
  | start_handle | 无符号整型 | 开始句柄，从这个句柄开始寻找特征描述 |
  | end_handle   | 无符号整型 | 结束句柄，从这个句柄结束寻找特征描述 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 读取指定UUID的特征值

> **ble.readCharaByUUID(connect_id, start_handle, end_handle, uuid_type, uuid_s, uuid_l)**

* 功能

  读取指定UUID的特征值，start_handle和end_handle必须要包含一个特征值句柄。

* 参数

  | 参数         | 类型       | 说明                                                         |
  | ------------ | ---------- | ------------------------------------------------------------ |
  | connect_id   | 无符号整型 | 连接ID，建立连接时得到的连接ID                               |
  | start_handle | 无符号整型 | 开始句柄，一定要属于同一个特征的句柄                         |
  | end_handle   | 无符号整型 | 结束句柄，一定要属于同一个特征的句柄                         |
  | uuid_type    | 无符号整型 | uuid类型<br>0 - 长UUID，128bit<br>1 - 短UUID，16bit          |
  | uuid_s       | 无符号整型 | 短UUID，2个字节（16bit），当uuid_type为0时，该值给0          |
  | uuid_l       | 数组       | 长UUID，16个字节（128bit），当uuid_type为1时，该值给 bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 读取指定句柄的特征值

> **ble.readCharaByHandle(connect_id, handle, offset, is_long)**

* 功能

  读取指定句柄的特征值。

* 参数

  | 参数       | 类型       | 说明                                                         |
  | ---------- | ---------- | ------------------------------------------------------------ |
  | connect_id | 无符号整型 | 连接ID，建立连接时得到的连接ID                               |
  | handle     | 无符号整型 | 特征值句柄                                                   |
  | offset     | 无符号整型 | 偏移位置                                                     |
  | is_long    | 无符号整型 | 长特征值标志<br>0-短特征值，一次可以读取完<br>1-长特征值，分多次读取 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 读取特征描述

> **ble.readCharaDesc(connect_id, handle, is_long)**

* 功能

  读取特征描述。

* 参数

  | 参数       | 类型       | 说明                                               |
  | ---------- | ---------- | -------------------------------------------------- |
  | connect_id | 无符号整型 | 连接ID，建立连接时得到的连接ID                     |
  | handle     | 无符号整型 | 特征描述句柄                                       |
  | is_long    | 无符号整型 | 长特征描述标志<br>0-短特征描述值<br>1-长特征描述值 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 写入特征值(需链路层应答)

> **ble.writeChara(connect_id, handle, offset, is_long, data)**

* 功能

  写入特征值，链路层需要确认。

* 参数

  | 参数       | 类型       | 说明                                                         |
  | ---------- | ---------- | ------------------------------------------------------------ |
  | connect_id | 无符号整型 | 连接ID，建立连接时得到的连接ID                               |
  | handle     | 无符号整型 | 特征值句柄                                                   |
  | offset     | 无符号整型 | 偏移位置                                                     |
  | is_long    | 无符号整型 | 长特征值标志<br>0-短特征值，一次可以读取完<br>1-长特征值，分多次读取 |
  | data       | 数组       | 特征值数据                                                   |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
无
```



##### BLE Client 写入特征值(无需链路层应答)

> **ble.writeCharaNoRsp(connect_id, handle, data)**

* 功能

  写入特征值，链路层不需要确认。

* 参数

  | 参数       | 类型       | 说明                           |
  | ---------- | ---------- | ------------------------------ |
  | connect_id | 无符号整型 | 连接ID，建立连接时得到的连接ID |
  | handle     | 无符号整型 | 特征值句柄                     |
  | data       | 数组       | 特征值数据                     |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 写入特征描述

> **ble.writeCharaDesc(connect_id, handle, data)**

* 功能

  写入特征描述。

* 参数

  | 参数       | 类型       | 说明                           |
  | ---------- | ---------- | ------------------------------ |
  | connect_id | 无符号整型 | 连接ID，建立连接时得到的连接ID |
  | handle     | 无符号整型 | 特征描述句柄                   |
  | data       | 数组       | 特征描述数据                   |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
见 BLE Client 综合示例
```



##### BLE Client 综合示例

```python
# -*- coding: UTF-8 -*-

import ble
import utime
import _thread
import checkNet
from queue import Queue

PROJECT_NAME = "QuecPython_BLE_Client_Example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

event_dict = {
    'BLE_START_STATUS_IND': 0,  # ble start
    'BLE_STOP_STATUS_IND': 1,   # ble stop
    'BLE_CONNECT_IND': 16,  # ble connect
    'BLE_DISCONNECT_IND': 17,   # ble disconnect
    'BLE_UPDATE_CONN_PARAM_IND': 18,    # ble update connection parameter
    'BLE_SCAN_REPORT_IND': 19,  # ble gatt client scan and report other devices
    'BLE_GATT_MTU': 20, # ble connection mtu
    'BLE_GATT_RECV_NOTIFICATION_IND': 23,   # client receive notification
    'BLE_GATT_RECV_INDICATION_IND': 24, # client receive indication
    'BLE_GATT_START_DISCOVER_SERVICE_IND': 26,  # start discover service
    'BLE_GATT_DISCOVER_SERVICE_IND': 27,    # discover service
    'BLE_GATT_DISCOVER_CHARACTERISTIC_DATA_IND': 28,    # discover characteristic
    'BLE_GATT_DISCOVER_CHARA_DESC_IND': 29, # discover characteristic descriptor
    'BLE_GATT_CHARA_WRITE_WITH_RSP_IND': 30,    # write characteristic value with response
    'BLE_GATT_CHARA_WRITE_WITHOUT_RSP_IND': 31, # write characteristic value without response
    'BLE_GATT_CHARA_READ_IND': 32,  # read characteristic value by handle
    'BLE_GATT_CHARA_READ_BY_UUID_IND': 33,  # read characteristic value by uuid
    'BLE_GATT_CHARA_MULTI_READ_IND': 34,    # read multiple characteristic value
    'BLE_GATT_DESC_WRITE_WITH_RSP_IND': 35, # write characteristic descriptor
    'BLE_GATT_DESC_READ_IND': 36,   # read characteristic descriptor
    'BLE_GATT_ATT_ERROR_IND': 37,   # attribute error
}

gatt_status_dict = {
    'BLE_GATT_IDLE' : 0,
    'BLE_GATT_DISCOVER_SERVICE': 1,
    'BLE_GATT_DISCOVER_INCLUDES': 2,
    'BLE_GATT_DISCOVER_CHARACTERISTIC': 3,
    'BLE_GATT_WRITE_CHARA_VALUE': 4,
    'BLE_GATT_WRITE_CHARA_DESC': 5,
    'BLE_GATT_READ_CHARA_VALUE': 6,
    'BLE_GATT_READ_CHARA_DESC': 7,
}

class EVENT(dict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        raise ValueError("{} is read-only.".format(key))


class BleClient(object):
    def __init__(self):
        self.ble_server_name = 'Quectel_ble' #目标设备ble名称
        self.connect_id = 0
        self.connect_addr = 0
        self.gatt_statue = 0
        self.discover_service_mode = 0 # 0-discover all service, 1-discover service by uuid

        self.scan_param = {
            'scan_mode' : 1, # 积极扫描
            'interval' : 0x100,
            'scan_window' : 0x50,
            'filter_policy' : 0,
            'local_addr_type' : 0,
        }

        self.scan_report_info = {
            'event_type' : 0,
            'name' : '',
            'addr_type' : 0,
            'addr' : 0, # 初始化时，用0表示无效值，实际存放bytearray
            'rssi' : 0,
            'data_len' : 0,
            'raw_data' : 0,
        }

        self.target_service = {
            'start_handle' : 0,
            'end_handle' : 0,
            'uuid_type' : 1, # 短uuid
            'short_uuid' : 0x180F, # 电池电量服务
            'long_uuid' : bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        }

        self.characteristic_list = []
        self.descriptor_list = []
        self.characteristic_count = 0   # ql_ble_gatt_chara_count
        self.chara_descriptor_count = 0 # ql_ble_gatt_chara_desc_count
        self.characteristic_index = 0   # ql_ble_gatt_chara_desc_index
        self.current_chara_index = 0    # ql_ble_gatt_cur_chara
        self.current_desc_index = 0     # ql_ble_gatt_chara_cur_desc
        self.ble_short_uuid_pair_len = 7
        self.ble_long_uuid_pair_len = 21

        ret = ble.clientInit(self.ble_client_callback)
        if ret != 0:
            print('ble client initialize failed.')
            raise ValueError("BLE Client Init failed.")
        else:
            print('ble client initialize successful.')
        print('')

    @staticmethod
    def gatt_open():
        ret = ble.gattStart()
        if ret != 0:
            print('ble open failed.')
        else:
            print('ble open successful.')
        print('')
        return ret

    @staticmethod
    def gatt_close():
        ret = ble.gattStop()
        if ret != 0:
            print('ble close failed.')
        else:
            print('ble close successful.')
        print('')
        return ret

    @staticmethod
    def gatt_get_status():
        return ble.getStatus()

    @staticmethod
    def release():
        ret = ble.clientRelease()
        if ret != 0:
            print('ble client release failed.')
        else:
            print('ble client release successful.')
        print('')
        return ret

    def set_scan_param(self):
        scan_mode = self.scan_param['scan_mode']
        interval = self.scan_param['interval']
        scan_time = self.scan_param['scan_window']
        filter_policy = self.scan_param['filter_policy']
        local_addr_type = self.scan_param['local_addr_type']
        ret = ble.setScanParam(scan_mode, interval, scan_time, filter_policy, local_addr_type)
        if ret != 0:
            print('ble client set scan-parameters failed.')
        else:
            print('ble client set scan-parameters successful.')
        print('')
        return ret

    @staticmethod
    def start_scan():
        ret = ble.scanStart()
        if ret != 0:
            print('ble client scan failed.')
        else:
            print('ble client scan successful.')
        print('')
        return ret

    @staticmethod
    def stop_scan():
        ret = ble.scanStop()
        if ret != 0:
            print('ble client failed to stop scanning.')
        else:
            print('ble client scan stopped successfully.')
        print('')
        return ret

    def connect(self):
        print('start to connect.....')
        addr_type = self.scan_report_info['addr_type']
        addr = self.scan_report_info['addr']
        if addr != 0 and len(addr) == 6:
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('addr_type : {}, addr : {}'.format(addr_type, addr_str))
            ret = ble.connect(addr_type, addr)
            if ret != 0:
                print('ble client connect failed.')
            else:
                print('ble client connect successful.')
            print('')
            return ret

    def cancel_connect(self):
        ret = ble.cancelConnect(self.scan_report_info['addr'])
        if ret != 0:
            print('ble client cancel connect failed.')
        else:
            print('ble client cancel connect successful.')
        print('')
        return ret

    def disconnect(self):
        ret = ble.disconnect(self.connect_id)
        if ret != 0:
            print('ble client disconnect failed.')
        else:
            print('ble client disconnect successful.')
        print('')
        return ret

    def discover_all_service(self):
        ret = ble.discoverAllService(self.connect_id)
        if ret != 0:
            print('ble client discover all service failed.')
        else:
            print('ble client discover all service successful.')
        print('')
        return ret

    def discover_service_by_uuid(self):
        connect_id = self.connect_id
        uuid_type = self.target_service['uuid_type']
        short_uuid = self.target_service['short_uuid']
        long_uuid = self.target_service['long_uuid']
        ret = ble.discoverByUUID(connect_id, uuid_type, short_uuid, long_uuid)
        if ret != 0:
            print('ble client discover service by uuid failed.')
        else:
            print('ble client discover service by uuid successful.')
        print('')
        return ret

    def discover_all_includes(self):
        connect_id = self.connect_id
        start_handle = self.target_service['start_handle']
        end_handle = self.target_service['end_handle']
        ret = ble.discoverAllIncludes(connect_id, start_handle, end_handle)
        if ret != 0:
            print('ble client discover all includes failed.')
        else:
            print('ble client discover all includes successful.')
        print('')
        return ret

    def discover_all_characteristic(self):
        connect_id = self.connect_id
        start_handle = self.target_service['start_handle']
        end_handle = self.target_service['end_handle']
        ret = ble.discoverAllChara(connect_id, start_handle, end_handle)
        if ret != 0:
            print('ble client discover all characteristic failed.')
        else:
            print('ble client discover all characteristic successful.')
        print('')
        return ret

    def discover_all_characteristic_descriptor(self):
        connect_id = self.connect_id
        index = self.characteristic_index
        start_handle = self.characteristic_list[index]['value_handle'] + 1

        if self.characteristic_index == (self.characteristic_count - 1):
            end_handle = self.target_service['end_handle']
            print('[1]start_handle = {:#06x}, end_handle = {:#06x}'.format(start_handle - 1, end_handle))
            ret = ble.discoverAllCharaDesc(connect_id, start_handle, end_handle)
        else:
            end_handle = self.characteristic_list[index+1]['handle'] - 1
            print('[2]start_handle = {:#06x}, end_handle = {:#06x}'.format(start_handle - 1, end_handle))
            ret = ble.discoverAllCharaDesc(connect_id, start_handle, end_handle)
        self.characteristic_index += 1
        if ret != 0:
            print('ble client discover all characteristic descriptor failed.')
        else:
            print('ble client discover all characteristic descriptor successful.')
        print('')
        return ret

    def read_characteristic_by_uuid(self):
        connect_id = self.connect_id
        index = self.current_chara_index   # 根据需要改变该值
        start_handle = self.characteristic_list[index]['handle']
        end_handle = self.characteristic_list[index]['value_handle']
        uuid_type = 1
        short_uuid = self.characteristic_list[index]['short_uuid']
        long_uuid = bytearray([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])

        ret = ble.readCharaByUUID(connect_id, start_handle, end_handle, uuid_type, short_uuid, long_uuid)
        if ret != 0:
            print('ble client read characteristic by uuid failed.')
        else:
            print('ble client read characteristic by uuid successful.')
        print('')
        return ret

    def read_characteristic_by_handle(self):
        connect_id = self.connect_id
        index = self.current_chara_index  # 根据需要改变该值
        handle = self.characteristic_list[index]['value_handle']
        offset = 0
        is_long = 0

        ret = ble.readCharaByHandle(connect_id, handle, offset, is_long)
        if ret != 0:
            print('ble client read characteristic by handle failed.')
        else:
            print('ble client read characteristic by handle successful.')
        print('')
        return ret

    def read_characteristic_descriptor(self):
        connect_id = self.connect_id
        index = self.current_desc_index  # 根据需要改变该值
        handle = self.descriptor_list[index]['handle']
        print('handle = {:#06x}'.format(handle))
        is_long = 0
        ret = ble.readCharaDesc(connect_id, handle, is_long)
        if ret != 0:
            print('ble client read characteristic descriptor failed.')
        else:
            print('ble client read characteristic descriptor successful.')
        print('')
        return ret

    def write_characteristic(self):
        connect_id = self.connect_id
        index = self.current_chara_index  # 根据需要改变该值
        handle = self.characteristic_list[index]['value_handle']
        offset = 0
        is_long = 0
        data = bytearray([0x40, 0x00])
        print('value_handle = {:#06x}, uuid = {:#06x}'.format(handle, self.characteristic_list[index]['short_uuid']))
        ret = ble.writeChara(connect_id, handle, offset, is_long, data)
        if ret != 0:
            print('ble client write characteristic failed.')
        else:
            print('ble client read characteristic successful.')
        print('')
        return ret

    def write_characteristic_no_rsp(self):
        connect_id = self.connect_id
        index = self.current_chara_index  # 根据需要改变该值
        handle = self.characteristic_list[index]['value_handle']
        data = bytearray([0x20, 0x00])
        print('value_handle = {:#06x}, uuid = {:#06x}'.format(handle, self.characteristic_list[index]['short_uuid']))
        ret = ble.writeCharaNoRsp(connect_id, handle, data)
        if ret != 0:
            print('ble client write characteristic no rsp failed.')
        else:
            print('ble client read characteristic no rsp successful.')
        print('')
        return ret

    def write_characteristic_descriptor(self):
        connect_id = self.connect_id
        index = self.current_desc_index  # 根据需要改变该值
        handle = self.descriptor_list[index]['handle']
        data = bytearray([0x01, 0x02])
        print('handle = {:#06x}'.format(handle))

        ret = ble.writeCharaDesc(connect_id, handle, data)
        if ret != 0:
            print('ble client write characteristic descriptor failed.')
        else:
            print('ble client read characteristic descriptor successful.')
        print('')
        return ret

    @staticmethod
    def ble_client_callback(args):
        global msg_queue
        msg_queue.put(args)


def ble_gatt_client_event_handler():
    global msg_queue
    old_time = 0

    while True:
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])
        if cur_time[5] != old_time and cur_time[5] % 5 == 0:
            old_time = cur_time[5]
            print('[{}]event handler running.....'.format(timestamp))
            print('')
        msg = msg_queue.get()  # 没有消息时会阻塞在这
        # print('msg : {}'.format(msg))
        event_id = msg[0]
        status = msg[1]

        if event_id == event.BLE_START_STATUS_IND:
            print('')
            print('event_id : BLE_START_STATUS_IND, status = {}'.format(status))
            if status == 0:
                print('BLE start successful.')
                ble_status = ble_client.gatt_get_status()
                if ble_status == 0:
                    print('BLE Status : stopped.')
                    break
                elif ble_status == 1:
                    print('BLE Status : started.')
                else:
                    print('get ble status error.')
                    ble_client.gatt_close()
                    break

                ret = ble_client.set_scan_param()
                if ret != 0:
                    ble_client.gatt_close()
                    break
                ret = ble_client.start_scan()
                if ret != 0:
                    ble_client.gatt_close()
                    break
            else:
                print('BLE start failed.')
                break
        elif event_id == event.BLE_STOP_STATUS_IND:
            print('')
            print('event_id : BLE_STOP_STATUS_IND, status = {}'.format(status))
            if status == 0:
                print('ble stop successful.')
            else:
                print('ble stop failed.')
                break
        elif event_id == event.BLE_CONNECT_IND:
            print('')
            print('event_id : BLE_CONNECT_IND, status = {}'.format(status))
            if status == 0:
                ble_client.connect_id = msg[2]
                ble_client.connect_addr = msg[3]
                addr = ble_client.connect_addr
                addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
                print('connect_id : {:#x}, connect_addr : {}'.format(ble_client.connect_id, addr_str))
            else:
                print('ble connect failed.')
                break
        elif event_id == event.BLE_DISCONNECT_IND:
            print('')
            print('event_id : BLE_DISCONNECT_IND, status = {}'.format(status))
            if status == 0:
                ble_client.connect_id = msg[2]
                ble_client.connect_addr = msg[3]
                addr = ble_client.connect_addr
                addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
                print('connect_id : {:#x}, connect_addr : {}'.format(ble_client.connect_id, addr_str))
            else:
                print('ble disconnect failed.')
            ble_client.gatt_close()
            break
        elif event_id == event.BLE_UPDATE_CONN_PARAM_IND:
            print('')
            print('event_id : BLE_UPDATE_CONN_PARAM_IND, status = {}'.format(status))
            if status == 0:
                connect_id = msg[2]
                max_interval = msg[3]
                min_interval = msg[4]
                latency = msg[5]
                timeout = msg[6]
                print('connect_id={},max_interval={},min_interval={},latency={},timeout={}'.format(connect_id,max_interval,min_interval,latency,timeout))
            else:
                print('ble update parameter failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_SCAN_REPORT_IND:
            if status == 0:
                # print(' ble scan successful.')

                ble_client.scan_report_info['event_type'] = msg[2]
                ble_client.scan_report_info['name'] = msg[3]
                ble_client.scan_report_info['addr_type'] = msg[4]
                ble_client.scan_report_info['addr'] = msg[5]
                ble_client.scan_report_info['rssi'] = msg[6]
                ble_client.scan_report_info['data_len'] = msg[7]
                ble_client.scan_report_info['raw_data'] = msg[8]

                device_name = ble_client.scan_report_info['name']
                addr = ble_client.scan_report_info['addr']
                rssi = ble_client.scan_report_info['rssi']
                addr_type = ble_client.scan_report_info['addr_type']
                addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
                if device_name != '' and rssi != 0:
                    print('name: {}, addr: {}, rssi: {}, addr_type: {}'.format(device_name, addr_str, rssi, addr_type))
                    print('raw_data: {}'.format(ble_client.scan_report_info['raw_data']))

                if device_name == ble_client.ble_server_name: # 扫描到目标设备后就停止扫描
                    ret = ble_client.stop_scan()
                    if ret != 0:
                        ble_client.gatt_close()
                        break

                    ret = ble_client.connect()
                    if ret != 0:
                        ble_client.gatt_close()
                        break
            else:
                print('ble scan failed.')
                ret = ble_client.stop_scan()
                if ret != 0:
                    ble_client.gatt_close()
                    break
        elif event_id == event.BLE_GATT_MTU:
            print('')
            print('event_id : BLE_GATT_MTU, status = {}'.format(status))
            if status == 0:
                handle = msg[2]
                ble_mtu = msg[3]
                print('handle = {:#06x}, ble_mtu = {}'.format(handle, ble_mtu))
            else:
                print('ble connect mtu failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_RECV_NOTIFICATION_IND:
            print('')
            print('event_id : BLE_GATT_RECV_NOTIFICATION_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('len={}, data:{}'.format(data_len, data))
                handle = (data[1] << 8) | data[0]
                print('handle = {:#06x}'.format(handle))
            else:
                print('ble receive notification failed.')
                break
        elif event_id == event.BLE_GATT_RECV_INDICATION_IND:
            print('')
            print('event_id : BLE_GATT_RECV_INDICATION_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('len={}, data:{}'.format(data_len, data))
            else:
                print('ble receive indication failed.')
                break
        elif event_id == event.BLE_GATT_START_DISCOVER_SERVICE_IND:
            print('')
            print('event_id : BLE_GATT_START_DISCOVER_SERVICE_IND, status = {}'.format(status))
            if status == 0:
                ble_client.characteristic_count = 0
                ble_client.chara_descriptor_count = 0
                ble_client.characteristic_index = 0
                ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_SERVICE

                if ble_client.discover_service_mode == 0:
                    print('execute the function discover_all_service.')
                    ret = ble_client.discover_all_service()
                else:
                    print('execute the function discover_service_by_uuid.')
                    ret = ble_client.discover_service_by_uuid()
                if ret != 0:
                    print('Execution result: Failed.')
                    ble_client.gatt_close()
                    break
            else:
                print('ble start discover service failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_DISCOVER_SERVICE_IND:
            print('')
            print('event_id : BLE_GATT_DISCOVER_SERVICE_IND, status = {}'.format(status))
            if status == 0:
                start_handle = msg[2]
                end_handle = msg[3]
                short_uuid = msg[4]
                print('start_handle = {:#06x}, end_handle = {:#06x}, short_uuid = {:#06x}'.format(start_handle, end_handle, short_uuid))
                if ble_client.discover_service_mode == 0: # discover service all
                    if ble_client.target_service['short_uuid'] == short_uuid: # 查找到所有服务后，按指定uuid查找特征值
                        ble_client.target_service['start_handle'] = start_handle
                        ble_client.target_service['end_handle'] = end_handle
                        ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC
                        print('execute the function discover_all_characteristic.')
                        ret = ble_client.discover_all_characteristic()
                        if ret != 0:
                            print('Execution result: Failed.')
                            ble_client.gatt_close()
                            break
                else:
                    ble_client.target_service['start_handle'] = start_handle
                    ble_client.target_service['end_handle'] = end_handle
                    ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC
                    print('execute the function discover_all_characteristic.')
                    ret = ble_client.discover_all_characteristic()
                    if ret != 0:
                        print('Execution result: Failed.')
                        ble_client.gatt_close()
                        break
            else:
                print('ble discover service failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_DISCOVER_CHARACTERISTIC_DATA_IND:
            print('')
            print('event_id : BLE_GATT_DISCOVER_CHARACTERISTIC_DATA_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                pair_len = data[0]
                print('pair_len={}, len={}, data:{}'.format(pair_len, data_len, data))
                if data_len > 0:
                    if ble_client.gatt_statue == gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC:
                        i = 0
                        while i < (data_len - 1) / pair_len:
                            chara_dict = {
                                'handle': (data[i * pair_len + 2] << 8) | data[i * pair_len + 1],
                                'properties': data[i * pair_len + 3],
                                'value_handle': (data[i * pair_len + 5] << 8) | data[i * pair_len + 4],
                                'uuid_type': 0,
                                'short_uuid': 0x0000,
                                'long_uuid': bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
                            }
                            print('handle={:#06x}, properties={:#x}, value_handle={:#06x}'.format(chara_dict['handle'], chara_dict['properties'], chara_dict['value_handle']))
                            if pair_len == ble_client.ble_short_uuid_pair_len:
                                chara_dict['uuid_type'] = 1
                                chara_dict['short_uuid'] = (data[i * pair_len + 7] << 8) | data[i * pair_len + 6]
                                print('short_uuid:{:#06x}'.format(chara_dict['short_uuid']))
                            elif pair_len == ble_client.ble_long_uuid_pair_len:
                                start_index = i * pair_len + 6
                                end_index = start_index + 16
                                chara_dict['uuid_type'] = 0
                                chara_dict['long_uuid'] = data[start_index : end_index]
                                print('long_uuid:{}'.format(chara_dict['long_uuid']))
                            i += 1
                            if ble_client.characteristic_count < 5:
                                ble_client.characteristic_list.append(chara_dict)
                                ble_client.characteristic_count = len(ble_client.characteristic_list)
                            print('characteristic_list len = {}'.format(ble_client.characteristic_count))
                    elif ble_client.gatt_statue == gatt_status.BLE_GATT_READ_CHARA_VALUE:
                        print('data_len = {}'.format(data_len))
                        print('pay_load = {:02x},{:02x},{:02x},{:02x}'.format(data[0], data[1], data[2], data[3]))
            else:
                print('ble discover characteristic failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_DISCOVER_CHARA_DESC_IND:
            print('')
            print('event_id : BLE_GATT_DISCOVER_CHARA_DESC_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                fmt = data[0]
                print('fmt={}, len={}, data:{}'.format(fmt, data_len, data))
                if data_len > 0:
                    i = 0
                    if fmt == 1:  # 16 bit uuid
                        while i < (data_len - 1) / 4:
                            descriptor_dict = {
                                'handle': (data[i * 4 + 2] << 8) | data[i * 4 + 1],
                                'short_uuid': (data[i * 4 + 4] << 8) | data[i * 4 + 3],
                            }
                            print('handle={:#06x}, uuid={:#06x}'.format(descriptor_dict['handle'], descriptor_dict['short_uuid']))
                            i += 1
                            if ble_client.chara_descriptor_count < 5:
                                ble_client.descriptor_list.append(descriptor_dict)
                                ble_client.chara_descriptor_count = len(ble_client.descriptor_list)
                            print('descriptor_list len = {}'.format(ble_client.chara_descriptor_count))
                if ble_client.characteristic_index == ble_client.characteristic_count:
                    print('execute the function read_characteristic_by_uuid.')
                    # ble_client.gatt_statue = gatt_status.BLE_GATT_WRITE_CHARA_VALUE
                    # ret = ble_client.write_characteristic()
                    # ret = ble_client.write_characteristic_no_rsp()

                    ble_client.gatt_statue = gatt_status.BLE_GATT_READ_CHARA_VALUE
                    ret = ble_client.read_characteristic_by_uuid()
                    # ret = ble_client.read_characteristic_by_handle()

                    # ble_client.gatt_statue = gatt_status.BLE_GATT_READ_CHARA_DESC
                    # ret = ble_client.read_characteristic_descriptor()

                    # ble_client.gatt_statue = gatt_status.BLE_GATT_WRITE_CHARA_DESC
                    # ret = ble_client.write_characteristic_descriptor()
                else:
                    print('execute the function discover_all_characteristic_descriptor.')
                    ret = ble_client.discover_all_characteristic_descriptor()
                if ret != 0:
                    print('Execution result: Failed.')
                    ble_client.gatt_close()
                    break
            else:
                print('ble discover characteristic descriptor failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_CHARA_WRITE_WITH_RSP_IND:
            print('')
            print('event_id : BLE_GATT_CHARA_WRITE_WITH_RSP_IND, status = {}'.format(status))
            if status == 0:
                if ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_VALUE:
                    pass
                elif ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_DESC:
                    pass
            else:
                print('ble write characteristic with response failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_WRITE_WITHOUT_RSP_IND:
            print('')
            print('event_id : BLE_GATT_CHARA_WRITE_WITHOUT_RSP_IND, status = {}'.format(status))
            if status == 0:
                print('write characteristic value without response successful.')
            else:
                print('write characteristic value without response failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_READ_IND:
            print('')
            # read characteristic value by handle
            print('event_id : BLE_GATT_CHARA_READ_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
                if ble_client.gatt_statue == gatt_status.BLE_GATT_READ_CHARA_VALUE:
                    # print('read characteristic value by handle.')
                    pass
            else:
                print('ble read characteristic failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_READ_BY_UUID_IND:
            print('')
            # read characteristic value by uuid
            print('event_id : BLE_GATT_CHARA_READ_BY_UUID_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
                handle = (data[2] << 8) | data[1]
                print('handle = {:#06x}'.format(handle))
            else:
                print('ble read characteristic by uuid failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_MULTI_READ_IND:
            print('')
            # read multiple characteristic value
            print('event_id : BLE_GATT_CHARA_MULTI_READ_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
            else:
                print('ble read multiple characteristic by uuid failed.')
                break
        elif event_id == event.BLE_GATT_DESC_WRITE_WITH_RSP_IND:
            print('')
            print('event_id : BLE_GATT_DESC_WRITE_WITH_RSP_IND, status = {}'.format(status))
            if status == 0:
                if ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_VALUE:
                    pass
                elif ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_DESC:
                    pass
            else:
                print('ble write characteristic descriptor failed.')
                break
        elif event_id == event.BLE_GATT_DESC_READ_IND:
            print('')
            # read characteristic descriptor
            print('event_id : BLE_GATT_DESC_READ_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
                if ble_client.gatt_statue == gatt_status.BLE_GATT_READ_CHARA_DESC:
                    # print('read characteristic descriptor.')
                    pass
            else:
                print('ble read characteristic descriptor failed.')
                break
        elif event_id == event.BLE_GATT_ATT_ERROR_IND:
            print('')
            print('event_id : BLE_GATT_ATT_ERROR_IND, status = {}'.format(status))
            if status == 0:
                errcode = msg[2]
                print('errcode = {:#06x}'.format(errcode))
                if ble_client.gatt_statue == gatt_status.BLE_GATT_DISCOVER_INCLUDES:
                    ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC
                    print('execute the function discover_all_characteristic.')
                    ret = ble_client.discover_all_characteristic()
                    if ret != 0:
                        print('Execution result: Failed.')
                        ble_client.gatt_close()
                        break
                elif ble_client.gatt_statue == gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC:
                    ble_client.gatt_statue = gatt_status.BLE_GATT_IDLE
                    print('execute the function discover_all_characteristic_descriptor.')
                    ret = ble_client.discover_all_characteristic_descriptor()
                    if ret != 0:
                        print('Execution result: Failed.')
                        ble_client.gatt_close()
                        break
            else:
                print('ble attribute error.')
                ble_client.gatt_close()
                break
        else:
            print('unknown event id : {}.'.format(event_id))

    # ble_client.release()


event = EVENT(event_dict)
gatt_status = EVENT(gatt_status_dict)
msg_queue = Queue(50)
ble_client = BleClient()


def main():
    checknet.poweron_print_once()
    print('create client event handler task.')
    _thread.start_new_thread(ble_gatt_client_event_handler, ())
    # ble.setScanFilter(0) # 关闭扫描过滤功能
    ret = ble_client.gatt_open()
    if ret != 0:
        return -1

    count = 0
    while True:
        utime.sleep(1)
        count += 1
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])
        if count % 5 == 0:
            print('[{}] BLE Client running, count = {}......'.format(timestamp, count))
            print('')
        if count > 130: # 这里设置计数是为了程序运行一会自己退出，方便测试，实际根据用户需要来处理
            count = 0
            print('!!!!! stop BLE Client now !!!!!')
            ble_status = ble_client.gatt_get_status()
            if ble_status == 1:
                ble_client.gatt_close()
            ble_client.release()
            break
        else:
            ble_status = ble_client.gatt_get_status()
            if ble_status == 0: # stopped
                print('BLE connection has been disconnected.')
                ble_client.release()
                break

if __name__ == '__main__':
    main()

```



#### bt - 经典蓝牙

模块功能：提供经典蓝牙的相关功能，支持HFP、A2DP、AVRCP、SPP。

##### 蓝牙初始化

> **bt.init(user_cb)**

* 功能

蓝牙初始化并注册回调函数。

* 参数

| 参数    | 类型     | 说明     |
| ------- | -------- | -------- |
| user_cb | function | 回调函数 |

* 返回值

执行成功返回整型0，失败返回整型-1。

说明：

（1）回调函数的形式

```python
def bt_callback(args):
	event_id = args[0]  # 第一个参数固定是 event_id
	status = args[1] # 第二个参数固定是状态，表示某个操作的执行结果是成功还是失败
	......
```

（2）回调函数参数说明

​		args[0] 固定表示event_id，args[1] 固定表示状态，0表示成功，非0表示失败。回调函数的参数个数并不是固定2个，而是根据第一个参数args[0]来决定的，下表中列出了不同事件ID对应的参数个数及说明。

| event_id | 参数个数 | 参数说明                                                     |
| :------: | :------: | ------------------------------------------------------------ |
|    0     |    2     | args[0] ：event_id，表示 BT/BLE start 事件<br>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败 |
|    1     |    2     | args[0] ：event_id，表示 BT/BLE stop<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败 |
|    6     |    6     | args[0] ：event_id，表示 BT inquiry 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：rssi，搜索到的设备的信号强度；<br/>args[3] ：device_class <br/>args[4] ：device_name，设备名称，字符串类型<br/>args[5] ：addr，搜到的蓝牙设备的mac地址 |
|    7     |    3     | args[0] ：event_id，表示 BT inquiry end 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：end_status，0 - 正常结束搜索，8 - 强制结束搜索 |
|    14    |    4     | args[0] ：event_id，表示 BT spp recv 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：data_len，收到的数据长度<br/>args[3] ：data，收到的数据，bytearray类型数据 |
|    40    |    4     | args[0] ：event_id，表示 BT HFP connect 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_connect_status，表示hfp的连接状态；<br/>                 0 - 已经断开连接<br/>                 1 - 连接中<br/>                 2 - 已经连接<br/>                 3 - 断开连接中<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    41    |    4     | args[0] ：event_id，表示 BT HFP disconnect 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_connect_status，表示hfp的连接状态；<br/>                 0 - 已经断开连接<br/>                 1 - 连接中<br/>                 2 - 已经连接<br/>                 3 - 断开连接中<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    42    |    4     | args[0] ：event_id，表示 BT HFP call status 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_call_status，表示hfp的通话状态；<br/>                 0 - 当前没有正在进行的通话<br/>                 1 - 当前至少有一个正在进行的通话<br/> args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    43    |    4     | args[0] ：event_id，表示 BT HFP call setup status 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_call_setup_status，表示hfp的call setup状态；<br/>                 0 - 表示没有电话需要接通<br/>                 1 - 表示有一个拨进来的电话还未接通<br/>                 2 - 表示有一个拨出去的电话还没有接通<br/>                 3 - 表示拨出电话的蓝牙连接的另一方正在响铃<br/> args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    44    |    4     | args[0] ：event_id，表示 BT HFP network status 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_network_status，表示AG的网络状态；<br/>                 0 - 表示网络不可用<br/>                 1 - 表示网络正常<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    45    |    4     | args[0] ：event_id，表示 BT HFP network signal 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_network_signal，表示AG的信号，范围 0~5<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    46    |    4     | args[0] ：event_id，表示 BT HFP battery level 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_battery_level，表示AG端的电池电量，范围 0~5<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    47    |    4     | args[0] ：event_id，表示 BT HFP call held status 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_call_held_status，表示hfp的call held状态；<br/>                 0 - 表示没有保持呼叫<br/>                 1 - 表示呼叫被暂停或活动/保持呼叫交换<br/>                 2 - 表示呼叫暂停，没有活动呼叫<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    48    |    4     | args[0] ：event_id，表示 BT HFP audio status 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_audio_status，表示audio连接状态；<br/>                 0 - 表示audio已经断开连接<br/>                 1 - 表示audio正在连接中<br/>                 2 - 表示audio已经连接成功<br/>                 3 - 表示audio正在断开连接<br>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    49    |    4     | args[0] ：event_id，表示 BT HFP volume type 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_volume_type<br/>                 0 - 表示volume type为speaker<br/>                 1 - 表示volume type为microphone<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    50    |    4     | args[0] ：event_id，表示 BT HFP service type 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_service_type，表示当前AG的网络服务模式；<br/>                 0 - 表示AG当前为正常网络模式<br/>                 1 - 表示AG当前处于漫游模式<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    51    |    4     | args[0] ：event_id，表示 BT HFP ring 事件，即来电时响铃事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：当前无实际意义，保留<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    52    |    4     | args[0] ：event_id，表示 BT HFP codec type 事件，即编解码模式<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：hfp_codec_type，表示当前使用哪个编解码模式；<br/>                 1 - 表示 CVDS，采用8kHz采样率<br/>                 2 - 表示mSBC，采用16kHz采样率<br/>args[3] ：addr，BT 主设备的地址，bytearray类型数据 |
|    61    |    4     | args[0] ：event_id，表示 BT SPP connect 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：spp_connect_status，表示spp的连接状态；<br/>                 0 - 已经断开连接<br/>                 1 - 连接中<br/>                 2 - 已经连接<br/>                 3 - 断开连接中<br/> args[3] ：addr，对端设备的mac地址，bytearray类型数据 |
|    62    |    4     | args[0] ：event_id，表示 BT SPP disconnect 事件<br/>args[1] ：status，表示操作的状态，0 - 成功，非0 - 失败<br/>args[2] ：spp_connect_status，表示spp的连接状态；<br/>                 0 - 已经断开连接<br/>                 1 - 连接中<br/>                 2 - 已经连接<br/>                 3 - 断开连接中<br/> args[3] ：addr，对端设备的mac地址，bytearray类型数据 |

* 示例

```python 

```



##### 蓝牙资源释放

> **bt.release()**

* 功能

  蓝牙资源释放。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### 开启蓝牙功能

> **bt.start()**

* 功能

  开启蓝牙功能。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。




##### 关闭蓝牙功能

> **bt.stop()**

* 功能

  关闭蓝牙功能。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。




##### 获取蓝牙状态

> **bt.getStatus()**

* 功能

  获取蓝牙的状态。

* 参数

  无

* 返回值

  | 返回值 | 类型 | 说明             |
  | ------ | ---- | ---------------- |
  | -1     | int  | 获取状态失败     |
  | 0      | int  | 蓝牙处于停止状态 |
  | 1      | int  | 蓝牙正常运行中   |

  

##### 获取蓝牙地址

> **bt.getLocalAddr()**

* 功能

  获取蓝牙地址。该接口需要在蓝牙已经初始化完成并启动成功后才能调用，比如在回调中收到 event_id 为0的事件之后，即 start 成功后，去调用。

* 参数

  无

* 返回值

  执行成功返回bytearray类型的蓝牙地址，6字节，失败返回整型-1。

* 示例

```python
>>> addr = bt.getLocalAddr()
>>> print(addr)
b'\xc7\xa13\xf8\xbf\x1a'
>>> mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
>>> print('mac = [{}]'.format(mac))
mac = [1a:bf:f8:33:a1:c7]
```



##### 设置蓝牙名称

> **bt.setLocalName(code, name)**

* 功能

  设置蓝牙名称。

* 参数

  | 参数 | 类型   | 说明                              |
  | ---- | ------ | --------------------------------- |
  | code | int    | 编码模式<br/>0 - UTF8<br/>1 - GBK |
  | name | string | 蓝牙名称，最大长度22字节          |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python
>>> bt.setLocalName(0, 'QuecPython-BT')
0
```



##### 获取蓝牙名称

> **bt.getLocalName()**

* 功能

  获取蓝牙名称。

* 参数

  无

* 返回值

  执行成功返回一个元组，包含名称编码模式和蓝牙名称，失败返回整型-1。

  成功返回格式：`(code, name)`

* 示例

```python
>>> bt.getLocalName()
(0, 'QuecPython-BT')
```



##### 设置蓝牙可见模式

> **bt.setVisibleMode(mode)**

* 功能

  设置蓝牙可见模式，即做从机时，被扫描时，是否可见以及可连接。

* 参数

  | 参数 | 类型 | 说明                                                         |
  | ---- | ---- | ------------------------------------------------------------ |
  | mode | int  | 0 - 不可被发现，不可被连接<br>1 - 可以被发现，但不可被连接<br>2 - 不可被发现，但可被连接<br>3 - 可以被发现，可被连接 |

* 返回值

  执行成功返回整形0，失败返回整型-1。

* 示例

```python
>>> bt.setVisibleMode(3)
0
```



##### 获取蓝牙可见模式

> **bt.getVisibleMode()**

* 功能

  获取蓝牙可见模式。

* 参数

  无

* 返回值

  执行成功返回蓝牙当前的可见模式值，失败返回整型-1。

* 示例

```python
>>> bt.getVisibleMode()
3
```



##### 开始搜索设备

> **bt.startInquiry(mode)**

* 功能

  开始搜索周边的蓝牙设备。

* 参数

  | 参数 | 类型 | 说明                                           |
  | ---- | ---- | ---------------------------------------------- |
  | mode | int  | 表示查询哪一类设备；当前直接写15，表示搜索所有 |

* 返回值

  执行成功返回整形0，失败返回整型-1。

* 示例

```python
bt.startInquiry(15)
```



##### 取消搜索设备

> **bt.cancelInquiry()**

* 功能

  取消搜索操作。

* 参数

  无

* 返回值

  执行成功返回整形0，失败返回整型-1。

* 示例

```python

```



##### 设置音频输出通道

> **bt.setChannel(channel)**

* 功能

  通过蓝牙接听电话或者播放音频时，通过该接口来设置音频输出通道。

* 参数

  | 参数    | 类型 | 说明                             |
  | ------- | ---- | -------------------------------- |
  | channel | int  | 0 - 听筒<br>1 - 耳机<br>2 - 喇叭 |

* 返回值

  执行成功返回整形0，失败返回整型-1。

* 示例

```python

```



##### HFP 功能初始化

> **bt.hfpInit()**

* 功能

HFP 功能初始化 。

* 参数

  无

* 返回值

执行成功返回整型0，失败返回整型-1。

* 示例

```python 

```



##### HFP 资源释放

> **bt.hfpRelease()**

* 功能

  HFP 资源释放。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### HFP 建立连接

> **bt.hfpConnect(addr)**

* 功能

  连接AG，建立HFP连接。

* 参数

  | 参数 | 类型 | 说明                  |
  | ---- | ---- | --------------------- |
  | addr | 数组 | AG端蓝牙地址，6个字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### HFP 断开连接

> **bt.hfpDisonnect(addr)**

* 功能

  断开HFP连接。

* 参数

  | 参数 | 类型 | 说明                  |
  | ---- | ---- | --------------------- |
  | addr | 数组 | AG端蓝牙地址，6个字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### HFP 设置通话音量

> **bt.hfpSetVolume(addr, vol)**

* 功能

  设置蓝牙通话时的音量。

* 参数

  | 参数 | 类型 | 说明                  |
  | ---- | ---- | --------------------- |
  | addr | 数组 | AG端蓝牙地址，6个字节 |
  | vol  | int  | 通话音量，范围 1-15   |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### HFP 挂断电话

> **bt.hfpRejectAfterAnswer(addr)**

* 功能

  挂断接通的电话。

* 参数

  | 参数 | 类型 | 说明                  |
  | ---- | ---- | --------------------- |
  | addr | 数组 | AG端蓝牙地址，6个字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### HFP 拒接电话

> **bt.hfpRejectCall(addr)**

* 功能

  拒接电话。

* 参数

  | 参数 | 类型 | 说明                  |
  | ---- | ---- | --------------------- |
  | addr | 数组 | AG端蓝牙地址，6个字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### HFP 接听电话

> **bt.hfpAnswerCall(addr)**

* 功能

  接听电话。

* 参数

  | 参数 | 类型 | 说明                  |
  | ---- | ---- | --------------------- |
  | addr | 数组 | AG端蓝牙地址，6个字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### HFP 开启语音助手

> **bt.hfpEnableVR(addr)**

* 功能

  开启语音助手。

* 参数

  | 参数 | 类型 | 说明                  |
  | ---- | ---- | --------------------- |
  | addr | 数组 | AG端蓝牙地址，6个字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### HFP 关闭语音助手

> **bt.hfpDisableVR(addr)**

* 功能

  关闭语音助手。

* 参数

  | 参数 | 类型 | 说明                  |
  | ---- | ---- | --------------------- |
  | addr | 数组 | AG端蓝牙地址，6个字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### HFP 三方通话控制

> **bt.hfpDisableVR(addr, cmd)**

* 功能

  三方通话控制。

* 参数

  | 参数 | 类型 | 说明                  |
  | ---- | ---- | --------------------- |
  | addr | 数组 | AG端蓝牙地址，6个字节 |
  | cmd  | int  | 控制命令              |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### HFP 示例程序

```python
# -*- coding: UTF-8 -*-

"""
示例说明：本例程提供一个通过HFP自动接听电话的功能
运行平台：EC600UCN_LB 铀开发板
运行本例程后，通过手机A搜索到设备名并点击连接；然后通过手机B拨打电话给手机A，
当手机A开始响铃震动时，设备会自动接听电话
"""
import bt
import utime
import _thread
from queue import Queue
from machine import Pin

# 如果对应播放通道外置了PA，且需要引脚控制PA开启，则需要下面步骤
# 具体使用哪个GPIO取决于实际使用的引脚
gpio11 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_DISABLE, 0)
gpio11.write(1)

BT_NAME = 'QuecPython-hfp'

BT_EVENT = {
    'BT_START_STATUS_IND': 0,           # bt/ble start
    'BT_STOP_STATUS_IND': 1,            # bt/ble stop
    'BT_HFP_CONNECT_IND': 40,           # bt hfp connected
    'BT_HFP_DISCONNECT_IND': 41,        # bt hfp disconnected
    'BT_HFP_CALL_IND': 42,              # bt hfp call state
    'BT_HFP_CALL_SETUP_IND': 43,        # bt hfp call setup state
    'BT_HFP_NETWORK_IND': 44,           # bt hfp network state
    'BT_HFP_NETWORK_SIGNAL_IND': 45,    # bt hfp network signal
    'BT_HFP_BATTERY_IND': 46,           # bt hfp battery level
    'BT_HFP_CALLHELD_IND': 47,          # bt hfp callheld state
    'BT_HFP_AUDIO_IND': 48,             # bt hfp audio state
    'BT_HFP_VOLUME_IND': 49,            # bt hfp volume type
    'BT_HFP_NETWORK_TYPE': 50,          # bt hfp network type
    'BT_HFP_RING_IND': 51,              # bt hfp ring indication
    'BT_HFP_CODEC_IND': 52,             # bt hfp codec type
}

HFP_CONN_STATUS = 0
HFP_CONN_STATUS_DICT = {
    'HFP_DISCONNECTED': 0,
    'HFP_CONNECTING': 1,
    'HFP_CONNECTED': 2,
    'HFP_DISCONNECTING': 3,
}
HFP_CALL_STATUS = 0
HFP_CALL_STATUS_DICT = {
    'HFP_NO_CALL_IN_PROGRESS': 0,
    'HFP_CALL_IN_PROGRESS': 1,
}

BT_IS_RUN = 0

msg_queue = Queue(30)


def get_key_by_value(val, d):
    for key, value in d.items():
        if val == value:
            return key
    return None

def bt_callback(args):
    global msg_queue
    msg_queue.put(args)

def bt_event_proc_task():
    global msg_queue
    global BT_IS_RUN
    global BT_EVENT
    global HFP_CONN_STATUS
    global HFP_CONN_STATUS_DICT
    global HFP_CALL_STATUS
    global HFP_CALL_STATUS_DICT

    while True:
        print('wait msg...')
        msg = msg_queue.get()  # 没有消息时会阻塞在这
        event_id = msg[0]
        status = msg[1]

        if event_id == BT_EVENT['BT_START_STATUS_IND']:
            print('event: BT_START_STATUS_IND')
            if status == 0:
                print('BT start successfully.')
                BT_IS_RUN = 1
                bt_status = bt.getStatus()
                if bt_status == 1:
                    print('BT status is 1, normal status.')
                else:
                    print('BT status is {}, abnormal status.'.format(bt_status))
                    bt.stop()
                    break

                retval = bt.getLocalName()
                if retval != -1:
                    print('The current BT name is : {}'.format(retval[1]))
                else:
                    print('Failed to get BT name.')
                    bt.stop()
                    break

                print('Set BT name to {}'.format(BT_NAME))
                retval = bt.setLocalName(0, BT_NAME)
                if retval != -1:
                    print('BT name set successfully.')
                else:
                    print('BT name set failed.')
                    bt.stop()
                    break

                retval = bt.getLocalName()
                if retval != -1:
                    print('The new BT name is : {}'.format(retval[1]))
                else:
                    print('Failed to get new BT name.')
                    bt.stop()
                    break

                # 设置蓝牙可见模式为：可以被发现并且可以被连接
                retval = bt.setVisibleMode(3)
                if retval == 0:
                    mode = bt.getVisibleMode()
                    if mode == 3:
                        print('BT visible mode set successfully.')
                    else:
                        print('BT visible mode set failed.')
                        bt.stop()
                        break
                else:
                    print('BT visible mode set failed.')
                    bt.stop()
                    break
            else:
                print('BT start failed.')
                bt.stop()
                break
        elif event_id == BT_EVENT['BT_STOP_STATUS_IND']:
            print('event: BT_STOP_STATUS_IND')
            if status == 0:
                BT_IS_RUN = 0
                print('BT stop successfully.')
            else:
                print('BT stop failed.')
            break
        elif event_id == BT_EVENT['BT_HFP_CONNECT_IND']:
            HFP_CONN_STATUS = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CONNECT_IND, {}, hfp_conn_status:{}, mac:{}'.format(status, get_key_by_value(msg[2], HFP_CONN_STATUS_DICT), mac))
            if status != 0:
                print('BT HFP connect failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_DISCONNECT_IND']:
            HFP_CONN_STATUS = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_DISCONNECT_IND, {}, hfp_conn_status:{}, mac:{}'.format(status, get_key_by_value(msg[2], HFP_CONN_STATUS_DICT), mac))
            if status != 0:
                print('BT HFP disconnect failed.')
            bt.stop()
        elif event_id == BT_EVENT['BT_HFP_CALL_IND']:
            call_sta = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CALL_IND, {}, hfp_call_status:{}, mac:{}'.format(status, get_key_by_value(msg[2], HFP_CALL_STATUS_DICT), mac))
            if status != 0:
                print('BT HFP call failed.')
                bt.stop()
                continue

            if call_sta == HFP_CALL_STATUS_DICT['HFP_NO_CALL_IN_PROGRESS']:
                if HFP_CALL_STATUS == HFP_CALL_STATUS_DICT['HFP_CALL_IN_PROGRESS']:
                    HFP_CALL_STATUS = call_sta
                    if HFP_CONN_STATUS == HFP_CONN_STATUS_DICT['HFP_CONNECTED']:
                        print('call ended, ready to disconnect hfp.')
                        retval = bt.hfpDisconnect(addr)
                        if retval == 0:
                            HFP_CONN_STATUS = HFP_CONN_STATUS_DICT['HFP_DISCONNECTING']
                        else:
                            print('Failed to disconnect hfp connection.')
                            bt.stop()
                            continue
            else:
                if HFP_CALL_STATUS == HFP_CALL_STATUS_DICT['HFP_NO_CALL_IN_PROGRESS']:
                    HFP_CALL_STATUS = call_sta
                    print('set audio output channel to 2.')
                    bt.setChannel(2)
                    print('set volume to 7.')
                    retval = bt.hfpSetVolume(addr, 7)
                    if retval != 0:
                        print('set volume failed.')
        elif event_id == BT_EVENT['BT_HFP_CALL_SETUP_IND']:
            call_setup_status = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CALL_SETUP_IND, {}, hfp_call_setup_status:{}, mac:{}'.format(status, call_setup_status, mac))
            if status != 0:
                print('BT HFP call setup failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_CALLHELD_IND']:
            callheld_status = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CALLHELD_IND, {}, callheld_status:{}, mac:{}'.format(status, callheld_status, mac))
            if status != 0:
                print('BT HFP callheld failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_NETWORK_IND']:
            network_status = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_NETWORK_IND, {}, network_status:{}, mac:{}'.format(status, network_status, mac))
            if status != 0:
                print('BT HFP network status failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_NETWORK_SIGNAL_IND']:
            network_signal = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_NETWORK_SIGNAL_IND, {}, signal:{}, mac:{}'.format(status, network_signal, mac))
            if status != 0:
                print('BT HFP network signal failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_BATTERY_IND']:
            battery_level = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_BATTERY_IND, {}, battery_level:{}, mac:{}'.format(status, battery_level, mac))
            if status != 0:
                print('BT HFP battery level failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_AUDIO_IND']:
            audio_status = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_AUDIO_IND, {}, audio_status:{}, mac:{}'.format(status, audio_status, mac))
            if status != 0:
                print('BT HFP audio failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_VOLUME_IND']:
            volume_type = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_VOLUME_IND, {}, volume_type:{}, mac:{}'.format(status, volume_type, mac))
            if status != 0:
                print('BT HFP volume failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_NETWORK_TYPE']:
            service_type = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_NETWORK_TYPE, {}, service_type:{}, mac:{}'.format(status, service_type, mac))
            if status != 0:
                print('BT HFP network service type failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_RING_IND']:
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_RING_IND, {}, mac:{}'.format(status, mac))
            if status != 0:
                print('BT HFP ring failed.')
                bt.stop()
                continue
            retval = bt.hfpAnswerCall(addr)
            if retval == 0:
                print('The call was answered successfully.')
            else:
                print('Failed to answer the call.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_CODEC_IND']:
            codec_type = msg[2]
            addr = msg[3]  # BT 主机端mac地址
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CODEC_IND, {}, codec_type:{}, mac:{}'.format(status, codec_type, mac))
            if status != 0:
                print('BT HFP codec failed.')
                bt.stop()
                continue
    print('Ready to release hfp.')
    bt.hfpRelease()
    bt.release()


def main():
    global BT_IS_RUN

    _thread.start_new_thread(bt_event_proc_task, ())

    retval = bt.init(bt_callback)
    if retval == 0:
        print('BT init successful.')
    else:
        print('BT init failed.')
        return -1
    retval = bt.hfpInit()
    if retval == 0:
        print('HFP init successful.')
    else:
        print('HFP init failed.')
        return -1
    retval = bt.start()
    if retval == 0:
        print('BT start successful.')
    else:
        print('BT start failed.')
        retval = bt.hfpRelease()
        if retval == 0:
            print('HFP release successful.')
        else:
            print('HFP release failed.')
        retval = bt.release()
        if retval == 0:
            print('BT release successful.')
        else:
            print('BT release failed.')
        return -1

    count = 0
    while True:
        utime.sleep(1)
        count += 1
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])

        if count % 5 == 0:
            if BT_IS_RUN == 1:
                print('[{}] BT HFP is running, count = {}......'.format(timestamp, count))
                print('')
            else:
                print('BT HFP has stopped running, ready to exit.')
                break


if __name__ == '__main__':
    main()

```



##### A2DP/AVRCP 功能初始化

> **bt.a2dpavrcpInit()**

* 功能

  A2DP和AVRCP功能初始化。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### A2DP/AVRCP 资源释放

> **bt.a2dpavrcpRelease()**

* 功能

  A2DP和AVRCP 资源释放。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### A2DP 断开连接

> **bt.a2dpDisconnect(addr)**

* 功能

  断开A2DP连接。

* 参数

  | 参数 | 类型 | 说明                      |
  | ---- | ---- | ------------------------- |
  | addr | 数组 | A2DP主机蓝牙地址，6个字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### A2DP 获取主机蓝牙地址

> **bt.a2dpGetAddr()**

* 功能

  获取A2DP主机蓝牙地址。

* 参数

  无

* 返回值

  执行成功返回bytearray类型的A2DP主机蓝牙地址，6字节，失败返回整型-1。

* 示例

```python

```



##### A2DP 获取A2DP连接状态

> **bt.a2dpGetConnStatus()**

* 功能

  获取A2DP连接状态。

* 参数

  无

* 返回值

  | 返回值 | 类型 | 说明         |
  | ------ | ---- | ------------ |
  | -1     | int  | 获取失败     |
  | 0      | int  | 连接已断开   |
  | 1      | int  | 正在连接中   |
  | 2      | int  | 已连接       |
  | 3      | int  | 正在断开连接 |

* 示例

```python

```



##### AVRCP 控制主机开始播放

> **bt.avrcpStart()**

* 功能

  控制主机开始播放。

* 参数

  无

* 返回值

  执行成功返回整形0，失败返回整型-1。

* 示例

```python

```



##### AVRCP 控制主机停止播放

> **bt.avrcpPause()**

* 功能

  控制主机停止播放。

* 参数

  无

* 返回值

  执行成功返回整形0，失败返回整型-1。

* 示例

```python

```



##### AVRCP 控制主机播放上一首

> **bt.avrcpPrev()**

* 功能

  控制主机播放上一首。

* 参数

  无

* 返回值

  执行成功返回整形0，失败返回整型-1。

* 示例

```python

```



##### AVRCP 控制主机播放下一首

> **bt.avrcpNext()**

* 功能

  控制主机播放下一首。

* 参数

  无

* 返回值

  执行成功返回整形0，失败返回整型-1。

* 示例

```python

```



##### AVRCP 设置主机播放音量

> **bt.avrcpSetVolume(vol)**

* 功能

  设置主机播放音量。

* 参数

  | 参数 | 类型 | 说明                  |
  | ---- | ---- | --------------------- |
  | vol  | int  | 播放音量，范围 0 - 11 |

* 返回值

  执行成功返回整形0，失败返回整型-1。

* 示例

```python

```



##### AVRCP 获取主机播放音量

> **bt.avrcpGetVolume()**

* 功能

  获取主机播放音量。

* 参数

  无

* 返回值

  执行成功返回整形音量值，失败返回整型-1。

* 示例

```python

```



##### AVRCP 获取主机播放状态

> **bt.avrcpGetPlayStatus()**

* 功能

  获取主机播放状态。

* 参数

  无

* 返回值

  | 返回值 | 类型 | 说明           |
  | ------ | ---- | -------------- |
  | -1     | int  | 获取失败       |
  | 0      | int  | 没有播放       |
  | 1      | int  | 正在播放       |
  | 2      | int  | 暂停播放       |
  | 3      | int  | 正在切换上一首 |
  | 4      | int  | 正在切换下一首 |

* 示例

```python

```



##### AVRCP 获取与主机连接状态

> **bt.avrcpGetConnStatus()**

* 功能

  通过AVRCP协议获取主机连接状态。

* 参数

  无

* 返回值

  | 返回值 | 类型 | 说明         |
  | ------ | ---- | ------------ |
  | -1     | int  | 获取失败     |
  | 0      | int  | 连接已断开   |
  | 1      | int  | 正在连接中   |
  | 2      | int  | 已连接       |
  | 3      | int  | 正在断开连接 |

* 示例

```python

```



##### A2DP/AVRCP 示例程序

```python
# -*- coding: UTF-8 -*-

"""
示例说明：本例程提供一个通过A2DP/AVRCP实现的简易蓝牙音乐播放控制功能
运行本例程后，通过手机搜索到设备名并点击连接；然后打开手机上的音乐播放软件，
回到例程运行界面，根据提示菜单输入对应的控制命令来实现音乐的播放、暂停、上一首、
下一首以及设置音量的功能
"""
import bt
import utime
import _thread
from queue import Queue
from machine import Pin

BT_STATUS_DICT = {
    'BT_NOT_RUNNING': 0,
    'BT_IS_RUNNING': 1
}

A2DP_AVRCP_CONNECT_STATUS = {
    'DISCONNECTED': 0,
    'CONNECTING': 1,
    'CONNECTED': 2,
    'DISCONNECTING': 3
}

host_addr = 0
msg_queue = Queue(10)

# 如果对应播放通道外置了PA，且需要引脚控制PA开启，则需要下面步骤
# 具体使用哪个GPIO取决于实际使用的引脚
gpio11 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_DISABLE, 0)
gpio11.write(1)


def cmd_proc(cmd):
    cmds = ('1', '2', '3', '4', '5')
    vols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')

    if cmd in cmds:
        if cmd == '5':
            while True:
                tmp = input('Please input volume: ')
                if len(tmp) != 1:
                    vol = tmp.split('Please input volume: ')[1]
                else:
                    vol = tmp
                if vol in vols:
                    return cmd, int(vol)
                else:
                    print('Volume should be in [0,11], try again.')
        else:
            return cmd, 0
    else:
        print('Command {} is not supported!'.format(cmd))
        return -1

def avrcp_play(args):
    return bt.avrcpStart()

def avrcp_pause(args):
    return bt.avrcpPause()

def avrcp_prev(args):
    return bt.avrcpPrev()

def avrcp_next(args):
    return bt.avrcpNext()

def avrcp_set_volume(vol):
    return bt.avrcpSetVolume(vol)

def bt_callback(args):
    pass

def bt_a2dp_avrcp_proc_task():
    global msg_queue

    cmd_handler = {
        '1': avrcp_play,
        '2': avrcp_pause,
        '3': avrcp_prev,
        '4': avrcp_next,
        '5': avrcp_set_volume,
    }
    while True:
        # print('wait msg...')
        msg = msg_queue.get()
        print('recv msg: {}'.format(msg))
        cmd_handler.get(msg[0])(msg[1])


def main():
    global host_addr
    global msg_queue

    _thread.start_new_thread(bt_a2dp_avrcp_proc_task, ())
    bt.init(bt_callback)
    bt.setChannel(2)
    retval = bt.a2dpavrcpInit()
    if retval == 0:
        print('BT A2DP/AVRCP initialization succeeded.')
    else:
        print('BT A2DP/AVRCP initialization failed.')
        return -1

    retval = bt.start()
    if retval != 0:
        print('BT start failed.')
        return -1

    utime.sleep_ms(1500)

    old_name = bt.getLocalName()
    if old_name == -1:
        print('Get BT name error.')
        return -1
    print('The current BT name is {}'.format(old_name[1]))
    new_name = 'QuecPython-a2dp'
    print('Set new BT name to {}'.format(new_name))
    retval = bt.setLocalName(0, new_name)
    if retval == -1:
        print('Set BT name failed.')
        return -1
    cur_name = bt.getLocalName()
    if cur_name == -1:
        print('Get new BT name error.')
        return -1
    else:
        if cur_name[1] == new_name:
            print('BT name changed successfully.')
        else:
            print('BT name changed failed.')

    visible_mode = bt.getVisibleMode()
    if visible_mode != -1:
        print('The current BT visible mode is {}'.format(visible_mode))
    else:
        print('Get BT visible mode error.')
        return -1

    print('Set BT visible mode to 3.')
    retval = bt.setVisibleMode(3)
    if retval == -1:
        print('Set BT visible mode error.')
        return -1
    count = 0
    while True:
        count += 1
        if count % 5 == 0:
            print('waiting to be connected...')
        if count >= 10000:
            count = 0
        a2dp_status = bt.a2dpGetConnStatus()
        avrcp_status = bt.avrcpGetConnStatus()
        if a2dp_status == A2DP_AVRCP_CONNECT_STATUS['CONNECTED'] and avrcp_status == A2DP_AVRCP_CONNECT_STATUS['CONNECTED']:
            print('========== BT connected! =========')
            addr = bt.a2dpGetAddr()
            if addr != -1:
                mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
                print('The BT address on the host side: {}'.format(mac))
                host_addr = addr
            else:
                print('Get BT addr error.')
                return -1
            print('Please open the music player software on your phone first.')
            print('Please enter the following options to select a function:')
            print('========================================================')
            print('1 : play')
            print('2 : pause')
            print('3 : prev')
            print('4 : next')
            print('5 : set volume')
            print('6 : exit')
            print('========================================================')
            while True:
                tmp = input('> ')
                if len(tmp) != 1:
                    cmd = tmp.split('> ')[1]
                else:
                    cmd = tmp
                if cmd == '6':
                    break
                retval = cmd_proc(cmd)
                if retval != -1:
                    msg_queue.put(retval)
            break
        else:
            utime.sleep_ms(1000)
    print('Ready to disconnect a2dp.')
    retval = bt.a2dpDisconnect(host_addr)
    if retval == 0:
        print('a2dp connection disconnected successfully')
    else:
        print('Disconnect a2dp error.')
    print('Ready to stop BT.')
    retval = bt.stop()
    if retval == 0:
        print('BT has stopped.')
    else:
        print('BT stop error.')
    bt.a2dpavrcpRelease()
    bt.release()


if __name__ == '__main__':
    main()
```



##### SPP 功能初始化

> **bt.sppInit()**

* 功能

  SPP 功能初始化。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### SPP 资源释放

> **bt.sppRelease()**

* 功能

  SPP 资源释放。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### SPP 建立连接

> **bt.sppConnect(addr)**

* 功能

  建立SPP连接。

* 参数

  | 参数 | 类型 | 说明              |
  | ---- | ---- | ----------------- |
  | addr | 数组 | 蓝牙地址，6个字节 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### SPP 断开连接

> **bt.sppDisconnect()**

* 功能

  断开SPP连接。

* 参数

  无

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### SPP 数据发送

> **bt.sppSend(data)**

* 功能

  通过SPP发送数据。

* 参数

  | 参数 | 类型 | 说明         |
  | ---- | ---- | ------------ |
  | data | 数组 | 待发送的数据 |

* 返回值

  执行成功返回整型0，失败返回整型-1。

* 示例

```python

```



##### SPP 示例程序

```python
# -*- coding: UTF-8 -*-

"""
示例说明：本例程提供一个通过SPP实现与手机端进行数据传输的功能
（1）运行之前，需要先在手机端（安卓）安装蓝牙串口APP，如BlueSPP，然后打开该软件；
（2）修改本例程中的目标设备的蓝牙名称，即 DST_DEVICE_INFO['dev_name'] 的值改为用户准备连接的手机的蓝牙名称；
（3）运行本例程，例程中会先发起搜索周边设备的操作，直到搜索到目标设备，就会结束搜索，然后向目标设备发起SPP连接请求；
（4）用户注意查看手机界面是否弹出蓝牙配对请求的界面，当出现时，点击配对；
（5）配对成功后，用户即可进入到蓝牙串口界面，发送数据给设备，设备在收到数据后会回复“I have received the data you sent.”
（6）手机端APP中点击断开连接，即可结束例程；
"""
import bt
import utime
import _thread
from queue import Queue


BT_NAME = 'QuecPython-SPP'

BT_EVENT = {
    'BT_START_STATUS_IND': 0,          # bt/ble start
    'BT_STOP_STATUS_IND': 1,           # bt/ble stop
    'BT_SPP_INQUIRY_IND': 6,           # bt spp inquiry ind
    'BT_SPP_INQUIRY_END_IND': 7,       # bt spp inquiry end ind
    'BT_SPP_RECV_DATA_IND': 14,        # bt spp recv data ind
    'BT_SPP_CONNECT_IND': 61,          # bt spp connect ind
    'BT_SPP_DISCONNECT_IND': 62,       # bt spp disconnect ind
}

DST_DEVICE_INFO = {
    'dev_name': 'HUAWEI Mate40 Pro', # 要连接设备的蓝牙名称
    'bt_addr': None
}

BT_IS_RUN = 0
msg_queue = Queue(30)


def bt_callback(args):
    global msg_queue
    msg_queue.put(args)


def bt_event_proc_task():
    global msg_queue
    global BT_IS_RUN
    global DST_DEVICE_INFO

    while True:
        print('wait msg...')
        msg = msg_queue.get()  # 没有消息时会阻塞在这
        event_id = msg[0]
        status = msg[1]

        if event_id == BT_EVENT['BT_START_STATUS_IND']:
            print('event: BT_START_STATUS_IND')
            if status == 0:
                print('BT start successfully.')
                BT_IS_RUN = 1

                print('Set BT name to {}'.format(BT_NAME))
                retval = bt.setLocalName(0, BT_NAME)
                if retval != -1:
                    print('BT name set successfully.')
                else:
                    print('BT name set failed.')
                    bt.stop()
                    continue

                retval = bt.setVisibleMode(3)
                if retval == 0:
                    mode = bt.getVisibleMode()
                    if mode == 3:
                        print('BT visible mode set successfully.')
                    else:
                        print('BT visible mode set failed.')
                        bt.stop()
                        continue
                else:
                    print('BT visible mode set failed.')
                    bt.stop()
                    continue

                retval = bt.startInquiry(15)
                if retval != 0:
                    print('Inquiry error.')
                    bt.stop()
                    continue
            else:
                print('BT start failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_STOP_STATUS_IND']:
            print('event: BT_STOP_STATUS_IND')
            if status == 0:
                BT_IS_RUN = 0
                print('BT stop successfully.')
            else:
                print('BT stop failed.')

            retval = bt.sppRelease()
            if retval == 0:
                print('SPP release successfully.')
            else:
                print('SPP release failed.')
            retval = bt.release()
            if retval == 0:
                print('BT release successfully.')
            else:
                print('BT release failed.')
            break
        elif event_id == BT_EVENT['BT_SPP_INQUIRY_IND']:
            print('event: BT_SPP_INQUIRY_IND')
            if status == 0:
                rssi = msg[2]
                name = msg[4]
                addr = msg[5]
                mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
                print('name: {}, addr: {}, rssi: {}'.format(name, mac, rssi))

                if name == DST_DEVICE_INFO['dev_name']:
                    print('The target device is found, device name {}'.format(name))
                    DST_DEVICE_INFO['bt_addr'] = addr
                    retval = bt.cancelInquiry()
                    if retval != 0:
                        print('cancel inquiry failed.')
                        continue
            else:
                print('BT inquiry failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_INQUIRY_END_IND']:
            print('event: BT_SPP_INQUIRY_END_IND')
            if status == 0:
                print('BT inquiry has ended.')
                inquiry_sta = msg[2]
                if inquiry_sta == 0:
                    if DST_DEVICE_INFO['bt_addr'] is not None:
                        print('Ready to connect to the target device : {}'.format(DST_DEVICE_INFO['dev_name']))
                        retval = bt.sppConnect(DST_DEVICE_INFO['bt_addr'])
                        if retval != 0:
                            print('SPP connect failed.')
                            bt.stop()
                            continue
                    else:
                        print('Not found device [{}], continue to inquiry.'.format(DST_DEVICE_INFO['dev_name']))
                        bt.cancelInquiry()
                        bt.startInquiry(15)
            else:
                print('Inquiry end failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_RECV_DATA_IND']:
            print('event: BT_SPP_RECV_DATA_IND')
            if status == 0:
                datalen = msg[2]
                data = msg[3]
                print('recv {} bytes data: {}'.format(datalen, data))
                send_data = 'I have received the data you sent.'
                print('send data: {}'.format(send_data))
                retval = bt.sppSend(send_data)
                if retval != 0:
                    print('send data faied.')
            else:
                print('Recv data failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_CONNECT_IND']:
            print('event: BT_SPP_CONNECT_IND')
            if status == 0:
                conn_sta = msg[2]
                addr = msg[3]
                mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
                print('SPP connect successful, conn_sta = {}, addr {}'.format(conn_sta, mac))
            else:
                print('Connect failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_DISCONNECT_IND']:
            print('event: BT_SPP_DISCONNECT_IND')
            conn_sta = msg[2]
            addr = msg[3]
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('SPP disconnect successful, conn_sta = {}, addr {}'.format(conn_sta, mac))
            bt.stop()
            continue


def main():
    global BT_IS_RUN

    _thread.start_new_thread(bt_event_proc_task, ())
    retval = bt.init(bt_callback)
    if retval == 0:
        print('BT init successful.')
    else:
        print('BT init failed.')
        return -1
    retval = bt.sppInit()
    if retval == 0:
        print('SPP init successful.')
    else:
        print('SPP init failed.')
        return -1
    retval = bt.start()
    if retval == 0:
        print('BT start successful.')
    else:
        print('BT start failed.')
        retval = bt.sppRelease()
        if retval == 0:
            print('SPP release successful.')
        else:
            print('SPP release failed.')
        return -1

    count = 0
    while True:
        utime.sleep(1)
        count += 1
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])

        if count % 5 == 0:
            if BT_IS_RUN == 1:
                print('[{}] BT SPP is running, count = {}......'.format(timestamp, count))
                print('')
            else:
                print('BT SPP has stopped running, ready to exit.')
                break


if __name__ == '__main__':
    main()
```





#### camera - 摄像扫码

模块功能：实现摄像头预览，照相机，扫码功能

注意：目前以下模块支持camera功能：EC200U系列、EC600U系列、EC600N系列，EC600S系列，EC800N系列。



##### 预览

预览功能。使用该功能前，需要初始化LCD。

###### 创建预览对象

> **import camera**
>
> **preview = camera.camPreview(model,cam_w,cam_h,lcd_w,lcd_h,perview_level)**

* 参数

| 参数          | 参数类型 | 参数说明                                                     |
| ------------- | -------- | ------------------------------------------------------------ |
| model         | int      | camera型号：<br />*0: gc032a spi*<br />*1: bf3901 spi*       |
| cam_w         | int      | camera水平分辨率                                             |
| cam_h         | int      | camera垂直分辨率                                             |
| lcd_w         | int      | LCD水平分辨率                                                |
| lcd_h         | int      | LCD垂直分辨率                                                |
| perview_level | int      | 预览等级[1,2]。<br />等级2只针对ASR平台，等级越高，图像越流畅,消耗资源越大 |

* 返回值

-1；初始化失败

若返回对象，则表示创建成功

* 示例

```python
>>> import camera
>>> preview = camera.camPreview(0,640,480,176,220,1)
```



###### 打开预览功能

**camPreview.open()**

* 参数

无

* 返回值

0：成功

其它：打开失败



###### 关闭预览功能

**camPreview.close()**

关闭预览功能。

* 参数

无

* 返回值

0：成功

其它：失败



##### 扫码识别

扫码识别功能。

###### 创建对象

**import camera**

**scan= camera.camScandecode(model,decode_level,cam_w,cam_h,perview_level,lcd_w,lcd_h)**

* 参数

| 参数          | 参数类型 | 参数说明                                                     |
| ------------- | -------- | ------------------------------------------------------------ |
| model         | int      | camera型号：<br />*0: gc032a spi*<br />*1: bf3901 spi*       |
| decode_level  | int      | 解码等级[1,2]，<br />等级2只针对ASR平台, 等级越高，识别效果越好但资源消耗越大. |
| cam_w         | int      | camera水平分辨率                                             |
| cam_h         | int      | camera垂直分辨率                                             |
| perview_level | int      | 预览等级[0,2]。<br />等级2只针对ASR平台, 等级越高，图像越流畅,消耗资源越大<br />等于0时，无lcd预览功能,无需提前初始化LCD<br />等于1或2时，必须先初始化lcd |
| lcd_w         | int      | LCD水平分辨率                                                |
| lcd_h         | int      | LCD垂直分辨率                                                |

* 返回值

-1；失败

若返回对象，则表示创建成功



###### 打开摄像头

**camScandecode.open()**

* 参数

无

* 返回值

0：成功

其它：失败



###### 关闭摄像头

**camScandecode.close()**

* 参数

无

* 返回值

0：成功

其它：关闭失败



###### 开启扫码识别功能

**camScandecode.start()**

* 参数

无

* 返回值

0：成功

其它：失败



###### 关闭扫码识别功能

**camScandecode.stop()**

* 参数

无

* 返回值

0：成功

其它：失败



###### 暂停扫码识别功能

**camScandecode.pause()**

* 参数

无

* 返回值

0：成功

其它：失败



###### 继续扫码识别功能

**camScandecode.resume()**

* 参数

无

* 返回值

0：成功

其它：失败



###### 设置识别回调

**camScandecode.callback(callback)**

* 参数

| 参数     | 参数类型 | 参数说明 |
| -------- | -------- | -------- |
| callback | api      | 回调api  |

* 返回值

0：成功

其它：失败

* 示例

```python
def callback(para):
    print(para)		#para[0] 识别结果 	0：成功 其它：失败
    				#para[1] 识别内容	
Scandecode.callback(callback) 
```

##### 照相机

照相机功能。

###### 创建对象

**import camera**

**cap= camera.camCapture(model,cam_w,cam_h,perview_level,lcd_w,lcd_h)**

* 参数

| 参数          | 参数类型 | 参数说明                                                     |
| ------------- | -------- | ------------------------------------------------------------ |
| model         | int      | camera型号：<br />*0: gc032a spi*<br />*1: bf3901 spi*       |
| cam_w         | int      | camera水平分辨率                                             |
| cam_h         | int      | camera垂直分辨率                                             |
| perview_level | int      | 预览等级[0,2]。<br />等级2只针对ASR平台，等级越高，图像越流畅,消耗资源越大。<br />等于0时，无lcd预览功能，无须提前初始化LCD<br />等于1或2时，必须先初始化lcd |
| lcd_w         | int      | LCD水平分辨率                                                |
| lcd_h         | int      | LCD垂直分辨率                                                |

* 返回值

若返回对象，则表示创建成功



###### 打开摄像头

**camCapture.open()**

* 参数

无

* 返回值

0：成功

其它：失败



###### 关闭摄像头

**camCapture.close()**

* 参数

无

* 返回值

0：成功

其它：关闭失败



###### 拍照

拍照格式为jpeg

**camCapture.start(width,  height, pic_name)**

* 参数

| 参数     | 参数类型 | 参数说明                                  |
| -------- | -------- | ----------------------------------------- |
| width    | int      | 保存图片水平分辨率                        |
| height   | int      | 保存图片垂直分辨率                        |
| pic_name | str      | 图片名。图片无需加后缀.jpeg，会自动添加。 |

* 返回值

0 ： 成功（实际还需看拍照回调）



###### 设置拍照回调

**camCapture.callback(callback)**

* 参数

| 参数     | 参数类型 | 参数说明 |
| -------- | -------- | -------- |
| callback | api      | 回调api  |

* 返回值

0：成功

其它：失败

* 示例

```python
def callback(para):
    print(para)		#para[0] 拍照结果 	0：成功 其它：失败
    				#para[1] 保存图片的名称	
camCapture.callback(callback) 
```





#### GNSS - 外置GNSS

模块功能：对L76K GPS型号进行数据获取，可以得到模块定位是否成功，定位的经纬度数据，UTC授时时间，获取GPS模块的定位模式，获取GPS模块定位使用卫星数量，获取GPS模块定位可见卫星数量，获取定位方位角，GPS模块对地速度，模块定位大地高等数据信息。目前，该模块提供的功能接口，所获取的数据都来源于从串口读出的原始GNSS数据包中的GNGGA、GNRMC和GPGSV语句。

注意：当前仅EC600S/EC600N/EC800N/200U/600U模块支持该功能。


##### 创建gnss对象

> **from gnss import GnssGetData**
>
> **gnss = GnssGetData(uartn,baudrate,databits,parity,stopbits,flowctl)**

* 参数

| 参数     | 类型 | 说明                                                         |
| :------- | :--- | ------------------------------------------------------------ |
| uartn    | int  | UARTn范围为0-3：<br />0-UART0 - DEBUG PORT<br />1-UART1 – BT PORT<br />2-UART2 – MAIN PORT<br />3-UART3 – USB CDC PORT |
| baudrate | int  | 波特率，常用波特率都支持，如4800、9600、19200、38400、57600、115200、230400等 |
| databits | int  | 数据位（5 ~ 8），展锐平台当前仅支持8位                       |
| parity   | int  | 奇偶校验（0 – NONE，1 – EVEN，2 - ODD）                      |
| stopbits | int  | 停止位（1 ~ 2）                                              |
| flowctl  | int  | 硬件控制流（0 – FC_NONE， 1 – FC_HW）                        |

* 返回值

  无

* 示例

```python
from gnss import GnssGetData
gnss = GnssGetData(1, 9600, 8, 0, 1, 0)
```



##### 读取GNSS数据并解析

> **gnss.read_gnss_data(max_retry=1, debug=0)**

* 参数

| 参数      | 类型 | 说明                                                         |
| --------- | ---- | ------------------------------------------------------------ |
| max_retry | int  | 可选参数，可不填该参数；表示当读取的GNSS无效时，自动重新读取的最大尝试次数，如果读取数据长度为0（即没有读取到数据）则直接退出；这里会进行自动重新读取的前提是，当前读取的这一包原始GNSS数据中，如果GNGGA、GNRMC和GPGSV语句有任何一种没有找到或者是找到但是数据是无效的，那么就会重新去读取下一包数据，直到GNGGA、GNRMC和GPGSV语句都找到并且数据有效或者达到最大尝试次数退出。默认为1，表示只读取一次数据。 |
| debug     | int  | 可选参数，可不填该参数，默认为0；表示在读取解析GNSS数据过程中，是否输出一些调试信息，为0表示不输出详细信息，为1表示输出详细信息，方便用户直观的看到解析结果以及进行比对；这里要注意的是，debug为0，并不是一点调试信息都不输出，而是仅仅输出一些简单的基本的信息，比如没有从原始的GNSS数据中找到对应数据或数据无效，则提示数据无效或者没有找到相关数据之类的基本信息，具体可参考示例。 |

* 返回值

  返回从串口读取的GNSS数据长度，单位字节。

* 示例

```python
#=========================================================================
gnss.read_gnss_data()	# 使用默认设置，仅读取一次，不输出详细调试信息
4224	# 读取数据成功，并解析GNGGA、GNRMC和GPGSV语句都成功，直接返回读取的原始数据长度
#=========================================================================
gnss.read_gnss_data()  # 使用默认设置，仅读取一次，不输出详细调试信息
GNGGA data is invalid. # 读取数据成功，获取的GNGGA定位数据无效
GNRMC data is invalid. # 读取数据成功，获取的GNRMC定位数据无效
648		# 返回读取的原始数据长度
#=========================================================================
gnss.read_gnss_data(max_retry=3)  # 设置最大自动读取次数为3次
Not find GPGSV data or GPGSV data is invalid.  # 第1次读取，GPGSV数据未找到或无效
continue read.        # 继续读取下一包数据
Not find GNGGA data.  # 第2次读取，没有找到GNGGA数据
Not find GNRMC data.  # 第2次读取，没有找到GNRMC数据
continue read.        # 继续尝试读取下一包
Not find GNGGA data.  # 第3次读取，没有找到GNGGA数据
Not find GNRMC data.  # 第3次读取，没有找到GNRMC数据
continue read.        # 第3次依然失败，准备继续读取，判断出已经达到最大尝试次数，退出
128
#=========================================================================
gnss.read_gnss_data(debug=1)  # 设置读取解析过程输出详细信息
GGA data : ['GNGGA', '021224.000', '3149.27680', 'N', '11706.93369', 'E', '1', '19', '0.9', '168.2', 'M', '-5.0', 'M', '', '*52']  # 输出从原始GNSS数据中匹配到并简单处理后的GNGGA数据
RMC data : ['GNRMC', '021224.000', 'A', '3149.27680', 'N', '11706.93369', 'E', '0.00', '153.28', '110122', '', '', 'A', 'V*02']  # 输出从原始GNSS数据中匹配到并简单处理后的GNRMC数据
total_sen_num = 3, total_sat_num = 12  # 输出一组完整GPGSV语句总条数和可视卫星数量
# 下面是具体的匹配到的GPGSV语句信息
[0] : ['$GPGSV', '3', '1', '12', '10', '79', '210', '35', '12', '40', '070', '43', '21', '08', '305', '31', '23', '46', '158', '43', '0*6E']
[1] : ['$GPGSV', '3', '2', '12', '24', '', '', '26', '25', '54', '125', '42', '31', '', '', '21', '32', '50', '324', '34', '0*64']
[2] : ['$GPGSV', '3', '3', '12', '193', '61', '104', '44', '194', '58', '117', '42', '195', '05', '162', '35', '199', '', '', '32', '0*54']
4224
```



##### 获取读取的原始GNSS数据

> **gnss.getOriginalData()**

该接口用于返回从串口读取的原始GNSS数据，如果用户希望拿到原始GNSS数据，自己进行处理或者进行一些数据确认，可以通过该接口来获取。该接口在每次调用`gnss.read_gnss_data(max_retry=1, debug=0)`接口后，返回的即本次读取的原始数据。

* 参数

  无

* 返回值

  返回从串口读取的原始GNSS数据，字符串类型。

* 示例

```python
data = gnss.getOriginalData()
print(data)
# 数据量较大，仅列出部分结果
00,A,3149.28094,N,11706.93869,E,0.00,153.28,110122,,,A,V*04
$GNVTG,153.28,T,,M,0.00,N,0.00,K,A*2E
$GNZDA,021555.000,11,01,2022,00,00*4D
$GPTXT,01,01,01,ANTENNA OK*35
$GNGGA,021556.000,3149.28095,N,11706.93869,E,1,24,0.6,166.5,M,-5.0,M,,*5E
$GNGLL,3149.28095,N,11706.93869,E,021556.000,A,A*47
$GNGSA,A,3,10,12,21,23,24,25,32,193,194,195,199,,1.0,0.6,0.8,1*35
$GNGSA,A,3,01,04,07,09,14,21,22,24,38,39,42,45,1.0,0.6,0.8,4*36
... 
$GNGGA,021600.000,3149.28096,N,11706.93877,E,1,25,0.6,166.4,M,-5.0,M,,*52
$GNGLL,3149.28096,N,11706.93877,E,021600.000,A,A*4B
$GNGSA,A,3,10,12,21,23,24,25,31,32,193,194,195,199,1.0,0.6,0.8,1*37
$GNGSA,A,3,01,04,07,09,$GNGGA,021601.000,3149.28096,N,11706.93878,E,1,25,0.6,166.4,M,-5.0,M,,*5C
$GNGLL,3149.2809
```



##### 检查本次读取解析结果有效性

> **gnss.checkDataValidity()**

GNSS模块提供的功能接口，所获取的数据都来源于从串口读出的原始GNSS数据包中的GNGGA、GNRMC和GPGSV语句，该接口用于检查读取的一包GNSS数据中，GNGGA、GNRMC和GPGSV语句的有效性。

* 参数

  无

* 返回值

  返回一个元组，形式为` (gga_valid, rmc_valid, gsv_valid)`

  `gga_valid` - 表示本次读取解析，是否匹配到GNGGA数据并解析成功，0表示没有匹配到GNGGA数据或数据无效，1表示有效；

  `rmc_valid` - 表示本次读取解析，是否匹配到GNRMC数据并解析成功，0表述没有匹配到GNRMC数据或数据无效，1表示有效；

  `gsv_valid` - 表示本地读取解析，是否匹配到GPGSV数据并解析成功，0表示没有匹配到GPGSV数据或数据无效，1表示有效。

  如果用户只关心定位结果，即GNGGA数据是否有效，只要gga_valid参数为1即可（或者通过gnss.isFix()接口来判断定位是否成功），不一定要三个参数都为1；解析GNRMC数据是为了获取对地速度，解析GPGSV数据是为了获取可视卫星数量以及这些卫星对应的方位角，所以用户如果不关心这些参数，可忽略rmc_valid和gsv_valid。

* 示例

```python
gnss.checkDataValidity()
(1, 1, 1)  # 说明本次读取解析，GNGGA、GNRMC和GPGSV这三种数据都匹配成功并解析成功
```



##### 检查是否定位成功

> **gnss.isFix()**

- 参数

  无

- 返回值

  1：定位成功

  0：定位失败

* 示例 

```
gnss.isFix()
1
```



##### 获取定位的UTC时间

> **gnss.getUtcTime()**

- 参数

  无

- 返回值

  成功返回UTC时间，字符串类型，失败返回整型-1。

* 示例

```python
gnss.getUtcTime()
'06:22:05.000'  # hh:mm:ss.sss
```



##### 获取GPS模块定位模式

> **gnss.getLocationMode()**

- 参数

  无

- 返回值

| 返回值 | 描述                                     |
| ------ | ---------------------------------------- |
| -1     | 获取失败，串口未读到数据或未读到有效数据 |
| 0      | 定位不可用或者无效                       |
| 1      | 定位有效,定位模式：GPS、SPS 模式         |
| 2      | 定位有效,定位模式： DGPS、DSPS 模式      |
| 6      | 估算（航位推算）模式                     |

* 示例

```python
gnss.getLocationMode()
1
```



##### 获取GPS模块定位使用卫星数量

> **gnss.getUsedSateCnt()**

- 参数

  无

- 返回值

  成功返回GPS模块定位使用卫星数量，返回值类型为整型，失败返回整型-1。

* 示例

```
gnss.getUsedSateCnt()
24
```



##### 获取GPS模块定位的经纬度信息

> **gnss.getLocation()**

- 参数

  无

- 返回值

  成功返回GPS模块定位的经纬度信息，失败返回整型-1；成功时返回值格式如下：
  
  `(longitude, lon_direction, latitude, lat_direction)`
  
  `longitude` - 经度，float型
  
  `lon_direction` - 经度方向，字符串类型，E表示东经，W表示西经
  
  `latitude` - 纬度，float型
  
  `lat_direction` - 纬度方向，字符串类型，N表示北纬，S表示南纬

* 示例

```python
gnss.getLocation()
(117.1156448333333, 'E', 31.82134916666667, 'N')
```



##### 获取GPS模块定位可见卫星数量

> **gnss.getViewedSateCnt()**

- 参数

  无

- 返回值

  成功返回GPS模块定位可见卫星数量，整型值，失败返回整型-1。

* 示例

```python
gnss.getViewedSateCnt()
12
```



##### 获取可视的GNSS卫星方位角 

> **gnss.getCourse()**

- 参数

  无

- 返回值
  返回所有可视的GNSS卫星方位角，范围：0 ~ 359，以正北为参考平面。返回形式为字典，其中key表示卫星编号，value表示方位角。要注意，value的值可能是一个整型值，也可能是''，这取决于原始的GNSS数据中GPGSV语句中方位角是否有值。返回值形式如下：

  `{key:value, ...,  key:value}`

- 示例

```python
 gnss.getCourse()
{'10': 204, '195': 162, '12': 68, '193': 105, '32': 326, '199': 162, '25': 122, '31': 247, '24': 52, '194': 116, '21': 304, '23': 159}
```




##### 获取GPS模块定位海拔高度

> **gnss.getGeodeticHeight()**

- 参数

  无

- 返回值

  成功返回浮点类型海拔高度(单位:米)，失败返回整型-1。

* 示例

```python
gnss.getGeodeticHeight()
166.5
```



##### 获取GPS模块对地速度

> **gnss.getSpeed()**

- 参数

  无

- 返回值

  成功返回GPS模块对地速度(单位:KM/h)，浮点类型，失败返回整型-1

* 示例

```python
gnss.getSpeed()
0.0
```



#### quecgnss - 内置GNSS

说明：当前仅 EC200UCNAA/EC200UCNLA/EC200UEUAA 型号支持该功能。

##### GNSS 功能初始化

> **import quecgnss**
>
> **quecgnss.init()**

* 功能

  模组内置GNSS模块功能的初始化。

* 参数

  无

* 返回值

  成功返回整形0，失败返回整形-1。



##### GNSS 工作状态获取

> **quecgnss.get_state()**

* 功能

  获取GNSS模块当前工作状态

* 参数

  无

* 返回值

| 返回值 | 类型 | 说明                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| 0      | int  | GNSS模块处于关闭状态                                         |
| 1      | int  | GNSS模块固件升级中                                           |
| 2      | int  | GNSS模块定位中，这种模式下即可开始读取GNSS定位数据，定位数据是否有效需要用户获取到定位数据后，解析对应语句来判断，比如判断GNRMC语句的status是 A 还是 V，A 表示定位有效，V 表示定位无效。 |



##### GNSS开关

> **quecgnss.gnssEnable(opt)**

* 功能

  开启或者关闭GNSS模块。如果是上电后第一次使用内置GNSS功能，一般不需要调用该接口来开启GNSS功能，直接调用init()接口即可，init() 接口在初始化时会自动开启GNSS功能。

* 参数

  | 参数 | 类型 | 说明                                  |
  | ---- | ---- | ------------------------------------- |
  | opt  | int  | 0 - 关闭GNSS功能<br/>1 - 开启GNSS功能 |

* 返回值

  成功返回整形0，失败返回整形-1。



##### GNSS定位数据获取

> **quecgnss.read(size)**

* 功能

  读取GNSS定位数据。

* 参数

  | 参数 | 类型 | 说明                           |
  | ---- | ---- | ------------------------------ |
  | size | int  | 指定读取数据的大小，单位字节。 |

* 返回值

  成功返回一个元组，失败返回整形-1。元组形式如下：

  `(size, data)`

  `size` - 实际读取数据的大小

  `data` - GNSS定位数据

##### GNSS使用示例

```python
import quecgnss


def main():
    ret = quecgnss.init()
    if ret == 0:
    	print('GNSS init ok.')
    else:
        print('GNSS init failed.')
        return -1
    data = quecgnss.read(4096)
    print(data[1].decode())
    
    quecgnss.gnssEnable(0)


if __name__ == '__main__':
    main()
    

#===================================================================================================
#运行结果
167,169,170,,,,,,,,1.773,1.013,1.455*15
$GPGSV,2,1,8,3,23,303,34,16,32,219,28,22,74,98,26,25,16,43,25*77
$GPGSV,2,2,8,26,70,236,28,31,59,12,38,32,55,127,34,4,5,,21*49
$BDGSV,2,1,8,163,51,192,32,166,70,11,31,167,52,197,32,169,59,334,31*61
$BDGSV,2,2,8,170,40,205,31,161,5,,31,164,5,,27,165,5,,29*59
$GNRMC,022326.000,A,3149.324624,N,11706.921702,E,0.000,261.541,180222,,E,A*38
$GNGGA,022326.000,3149.324624,N,11706.921702,E,1,12,1.013,-8.580,M,0,M,,*47
$GNGLL,3149.324624,N,11706.921702,E,022326.000,A,A*44
$GNGSA,A,3,31,32,3,16,22,25,26,,,,,,1.773,1.013,1.455*1C
$GNGSA,A,3,163,166,167,169,170,,,,,,,,1.773,1.013,1.455*15
$GPGSV,2,1,8,3,23,303,34,16,32,219,27,22,74,98,26,25,16,43,25*78
$GPGSV,2,2,8,26,70,236,28,31,59,12,37,32,55,127,34,4,5,,20*47
$BDGSV,2,1,8,163,51,192,32,166,70,11,31,167,52,197,32,169,59,334,31*61
$BDGSV,2,2,8,170,40,205,31,161,5,,31,164,5,,27,165,5,,29*59
$GNRMC,022327.000,A,3149.324611,N,11706.921713,E,0.000,261.541,180222,,E,A*3F
$GNGGA,022327.000,3149.324611,N,11706.921713,E,1,12,1.013,-8.577,M,0,M,,*48
$GNGLL,3149.324611,N,11706.921713,E,022327.000,A,A*43
...... # 数据较多，省略
$GNGSA,A,3,31,32,3,16,22,25,26,,,,,,1.837,1.120,1.456*11
$GNGSA,A,3,163,166,167,169,170,,,,,,,,1.837,1.120,1.456*18
$GPGSV,2,1,8,3,23,302,27,16,32,220,26,22,73,101,27,25,16,43,27*45
$GPGSV,2,2,8,26,70,237,28,31,59,13,33,32,54,128,28,4,5,,24*44
$BDGSV,2,1,8,163,51,192,33,166,71,11,35,167,52,198,33,169,59,334,34*6E
$BDGSV,2,2,8,170,40,205,32,161,5,,33,164,5,,28,165,5,,30*5F
$GNRMC,022507.000,A,3149.324768,N,11706.922344,E,0.000,261.541,180222,,E,A*31
$GNGGA,022507.000,3149.324768,N,11706.922344,E,1,12,1.120,-8.794,M,0,M,,*48
$GNGLL,3149.324768,N,11706.922344,E,022507.000,A,A*4D
$GNGSA,A,3,31,32,3,16,22,25,26,,,,,,1.837,1.120,1.455*12
$GNGSA,A,3,163,166,167,169,170,,,,,,,,1.837,1.120,1.455*1B
$GPGSV,2,1,8,3,23,302,26,16,32,220,26,22,73,101,27,25,16,43,26*45
$GPGSV,2,2,8,26,70,237,28,31,59,13,32,32,54,128,28,4,5,,24*45
$BDGSV,2,1,8,163,51,192,24,166,71,11,35,167,52,198,33,169,59,334,34*68
$BDGSV,2,2,8,170,40,205,31,161,5,,33,164,5,,28,165,5,,30*5C
$GNRMC,022508.000,A,3149.324754,N,11706.922338,E,0.002,261.541,180222,,E,A*38
$GNGGA,022508.000,3149.324754,N,11706.922338,E,1,12,1.120,-8.750,M,0,M,,*4B
$GNGLL,3149.324754,N,11706.922338,E,022508.000,A,A*46
$GNGSA,A,3,31,3

```



#### SecureData - 安全数据区

模块功能：模组提供一块裸flash区域及专门的读写接口供客户存贮重要信息，且信息在烧录固件后不丢失(烧录不包含此功能的固件无法保证不丢失)。提供一个存储和读取接口，不提供删除接口。
目前只支持EC600N系列项目

##### 数据存储

> **SecureData.Store(index,databuf,len)**

 * 参数

| 参数    | 类型      | 说明                                                         |
| :------ | :-------- | ------------------------------------------------------------ |
| index   | int       | index范围为1-16：<br />1 - 8 最大存储52字节数据<br />9 - 12 最大存储100字节数据<br />13 - 14 最大存储500字节数据<br />15 - 16 最大存储1000字节数据 |
| databuf | bytearray | 待存储的数据数组                                             |
| len     | int       | 要写入数据的长度                                             |


存储时按照databuf和len两者中长度较小的进行存储

 * 返回值

-1: 参数有误
0: 执行正常

##### 数据读取

> **SecureData.Read(index,databuf,len)**

 * 参数

| 参数    | 类型      | 说明                                            |
| :------ | :-------- | ----------------------------------------------- |
| index   | int       | index范围为1-16：<br />读取存储数据对应的索引号 |
| databuf | bytearray | 存储读取到的数据                                |
| len     | int       | 要读取数据的长度                                |

若存储的数据没有传入的len大，则返回实际存储的数据长度

 * 返回值

-2: 存储数据不存在且备份数据也不存在
-1: 参数有误
其他 :  实际读取到的数据长度

 * 示例

```python
import SecureData
# 即将存储的数据buf
databuf = '\x31\x32\x33\x34\x35\x36\x37\x38'
# 在index为1的存储区域中存储长度为8的数据databuf
SecureData.Store(1, databuf, 8)
# 定义一个长度为20的数组用于读取存储的数据
buf = bytearray(20)
# 读取index为1的存储区域中的数据至buf中,将读取到数据的长度存储在变量length中
length = SecureData.Read(1, buf, 20)
# 输出读到的数据
print(buf[:length])
```

 * 执行结果

```python
>>> import SecureData
>>> databuf = '\x31\x32\x33\x34\x35\x36\x37\x38'
>>> SecureData.Store(1, databuf, 8)
0
>>> buf = bytearray(20)
>>> length = SecureData.Read(1, buf, 20)
>>> print(buf[:length])
bytearray(b'12345678')
>>> 
```



#### nb-物联网云平台

模块功能：提供对接物联网云平台功能，提供连接物联网云平台。通过物联网云平台和模块设备的通信功能，目前支持中国电信lot物联网平台、中国电信AEP物联网平台和中国移动onenet物联网平台。quecthing版本不包含此模块。

模块名:nb(小写)

支持平台：BC25PA

介绍:其包含了两个子模块OC、AEP。此两个子模块均用lwm2m进行数据的交互。

##### OC

###### 创建OC对象

> **oc=OC(ip,port,psk)**

- 参数

| 参数 | 类型   | 说明                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| ip   | string | 物联网平台的服务器ip地址,最大长度16.                         |
| port | string | 物联网平台的服务器端口,最大长度5.                            |
| psk  | string | psk码模块用dtls协议通信会用到(现在不输入也是可以的，但是不能为空),最大长度64. |

- 示例

```python
>>> from nb import OC
>>> oc=OC("180.101.147.115","5683","763c9692c6639541e1ddcd6769fc9e33")
```

###### 连接OC云平台

> **oc.connect()**

- 参数

无

- 返回值

成功-0

失败-非0

- 示例

```python
>>> oc.connect()
0
```

###### 接收数据

> **oc.recv(data_len,data)**

- 参数

| 参数     | 类型   | 说明                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| data_len | int    | 期望接受的数据长度(注意此参数根据data的实际长度进行调整，按照data变量的容量和data_len的比较取最小值) |
| data     | string | 存储接收到的数据                                             |

- 说明

接收数据为16进制字符串，故数据长度必定是偶数。

- 返回值

成功-0

失败-非0

- 示例

```python
>>> oc.recv(6,data)
0
```

###### 发送数据

> **oc.send(data_len,data,type)**

- 参数

| 参数     | 类型   | 说明                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| data_len | int    | 期望接受的数据长度(注意此参数根据data的实际长度进行调整，按照data变量的容量和data_len的比较取最小值) |
| data     | string | 存储接收到的数据,最大支持1024字节数据。                      |
| type     | int    | 表示核心网释放与模块的RRC连接：<br/>0-无指示。<br/>1-指示该包上行数据后不期望有进一步的上行或者下行数据，核心网可立即释放  。<br/>2-指示该包上行数据后期望有对应回复的单个下行数据包，核心网在下发后立即释放  。 |

- 说明

发送数据为16进制字符串，数据长度为偶数。

- 返回值

成功-0

失败-非0

- 示例

```python
>>> print(data)
bytearray(b'313233')
>>> oc.send(6,data,0)
0
```

###### 关闭连接

- 参数

无

- 返回值

成功-True

失败-False

- 示例

```python
>>> oc.close()
True
```

##### AEP

###### 创建AEP对象

> **aep=AEP(ip,port,model,psk)**

- 参数

| 参数 | 类型   | 说明                                          |
| ---- | ------ | --------------------------------------------- |
| ip   | string | 物联网平台的服务器ip地址,最大长度16,合法ipv4. |
| port | string | 物联网平台的服务器端口,最大长度5,范围0~65536. |
| model | int | 0 设置接收数据模式为缓存模式，接收到新数据时无 URC 上报<br/>1 设置接收数据模式为直吐模式，接收到新数据时通过 URC 立即上报.<br/>2 设置接收数据模式为缓存模式，接收到新数据时仅上报指示 URC。可省略，默认为1. |
| psk  | string | 十六进制字符串型。加密设备的密钥，在平台端注册加密设备时可由平台生成或自主设置，最大支持长度 256 字节.可省略 |

- 示例

```python
>>> from nb import AEP
>>> aep=AEP("221.229.214.202","5683")
```

###### 设置回调函数

> **aep.set_event_callcb(usrfunc)**
- 参数

| 参数 | 类型   | 说明                                          |
| ---- | ------ | --------------------------------------------- |
| usrfunc  | func(data) | 发生事件时调用usrfunc |
- func(data)参数说明:
| 参数 |类型   | 说明                                          |
| ---- | ------ | --------------------------------------------- |
| data   | list | data[0]:event_id,事件类型><br/>data[1]:event_code,事件类型对应返回码><br/>data[2]:recv_data,数据><br/>data[3]:data_len,数据长度><br/> |

- 注意
    event_id,event_code,recv_data,data_len说明见本模块[事件说明](# 事件说明)。此函数，建议在连接之前进行注册，以防事件丢失。
- 

###### 连接AEP云平台

> **aep.connect(timeout)**

- 参数
    超时时间

    类型: int,超时时间,单位(ms),不输入参数则默认30s

    说明: 超时失败最坏情况阻塞时长为:15s+timeout。不支持并发操作。

- 返回值

成功-0

失败-1

- 示例

```python
>>> aep.connect(3000)
0
```
###### 查询待读取数据
> **aep.check()**

- 参数

无

- 返回值
返回云平台下发的待读取数据条数

- 示例

```python
>>> from nb import AEP
>>> aep=AEP("221.229.214.202","5683")
>>> aep.check()
0
```
###### 接收数据

> **aep.recv(data_len,data，timeout)**

- 使用说明,[model](#创建AEP对象)值对此函数的影响如下列表
| model     | 说明                                                         |
| -------- |  ------------------------------------------------------------ |
|0|为缓存模式,云平台下发数据到模组,模组不会有任何的主动提示动作,只能主动读取。|
|1|为直吐模式,云平台下发数据到模组,模组会把收到的数据直接吐到urc,set_event_callcb(usrfunc)设置的回调函数会直接接管收到的数据，以及数据长度。|
|2|为缓存模式,当无缓存数据时,云平台下发数据到模组,模组会通过回调函数usrfunc上报事件,提示有缓存数据待读取(云平台下发数据到模组,模组判断缓存为空上报事件提示有数据到达,缓存数据不为空不上报事件)|

- 参数

| 参数     | 类型   | 说明                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| data_len | int    | 期望接受的数据长度(注意此参数根据data的实际长度进行调整，按照data变量的容量和data_len的比较取最小值),非阻塞。 |
| data     | string | 存储接收到的数据。                                           |
| timeout  | int | 超时时间,单位ms,不输入则默认30s。                                       |

- 说明

接收数据为16进制字符串，故数据长度必定是偶数,非阻塞，如果无数据读取返回失败。

- 返回值

成功-0

失败-非0

- 示例

```python
>>> aep.recv(6,data)
0
```

###### 发送数据

> **aep.send(data_len,data,type,timeout)**

- 使用说明:
    在超时失败状态，阻塞时长最坏情况为:5s+timeout。不支持并发操作。
- 参数

| 参数     | 类型   | 说明                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| data_len | int    | 期望发送的数据长度(注意此参数根据data的实际长度进行调整，按照data变量的容量和data_len的比较取最小值)，非阻塞。 |
| data     | string | 待发送数据，最大支持1024字节数据。                           |
| type     | int    | 表示核心网释放与模块的RRC连接：<br/>0-发送 NON 数据并将模块发送数据所携带的 RAI 辅助释放标记设置为 0<br/>1-发送 NON 数据并将模块发送数据所携带的 RAI 辅助释放标记设置为 1<br/>2-发送 NON 数据并将模块发送数据所携带的 RAI 辅助释放标记设置为 2<br/>100-发送 CON 数据并将模块发送数据所携带的 RAI 辅助释放标记设置为 0<br/>101-发送 CON 数据并将模块发送数据所携带的 RAI 辅助释放标记设置为 1<br/>102-发送 CON 数据并将模块发送数据所携带的 RAI 辅助释放标记设置为 2 |
| timeout  | int    | 超时时间,单位ms,不输入则默认30s                              |

- RAI辅助释放标记说明
|         | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| RAI         | RAI 标记用于指示核心网释放与模块的 RRC 连接。:<br/>RAI 为 0 时，无指示。<br/>RAI 为 1 时，指示该包上行数据后不期望有进一步的上行或者下行数据，核心网可立即释放。<br/>RAI 为 2 时，指示该包上行数据后期望有对应回复的单个下行数据包，核心网在下发后立即释放。 |


- 说明

发送数据为16进制字符串，数据长度为偶数，阻塞,返回成功表示发送指令执行成功。

- 返回值

成功-0

失败-非0

- 示例

```python
>>> print(data)
bytearray(b'313233')
>>> aep.send(6,data,0)
0
```
###### 检查连接状态
> **aep.connect_check()**
- 参数

  无
- 返回值
   返回值类型:字符串
   含义如下表

  | 返回值     | 说明   |
  | -------- | ------ |
  |  UNINITIALISED |未初始化状态                   |
  |  REGISTERING |连接中                           |
  |   REJECTED_BY_SERVER |连接请求被服务器拒接     |
  |   TIMEOUT |连接超时                            |
  |   REGISTERED |已连接未订阅                     |
  |  REGISTERED_AND_OBSERVED |已连接已订阅         |
  |  DEREGISTERED |连接断开                        |
  |  RESUMPTION_FAILED DTLS |会话恢复失败          |
  |  FALIED |函数执行失败          |
  
 - 示例

```python
>>> aep.connect_check()
'UNINITIALISED\r\n'
```

###### 关闭连接
> **aep.close()**
- 参数

无

- 返回值

成功-True

失败-False

- 示例

```python
>>> aep.close()
True
```

###### 事件说明

对于本模块事件总体说明如下表:

|event_id	|event_code	|recv_data	|data_len	|说明|
| -------------- | ---------|----------|-------------|---------------------------- |
|0	|0	|NULL	|0	|modem进入psm，上报此事件。此时模组不接受下发到模组的网络数据,可通过主动发送数据打破modem侧psm状态。|
|0	|1	|NULL	|0	|modem退出psm模式，上报此事件。|
|23	|6	|NULL	|0	|深休眠唤醒恢复连接成功，上报此事件。在调用AEP.set_event_callcb(usrfunc)时上报。|
|23	|7	|NULL	|0	|深休眠唤醒恢复连接失败，可以采用断开连接，再重新连接。在调用AEP.set_event_callcb(usrfunc)时上报。|
|24	|8	|NULL	|0	|云平台下发fota升级指令后，模组开始下载差分升级包时上报此事件。|
|24	|9	|NULL	|0	|云平台下发fota升级指令时，模组fota升级结束时，上报此事件。|
|25	|10	|NULL	|0	|收到云平台的RST数据包，主动上报此事件。此情况需要断开连接，重新连接完成订阅才能正常通信。|
|27	|0	|data	|data_len	|收到云平台下发数据，在modem=1的情况下并调用set_event_callcb(usrfunc)设置了回调函数的情况下上报此事件。|
|28	|0	|NULL	|0	|收到云平台下发数据，在modem=2，并且模组无缓存数据(aep.check()返回0时，即表示无缓存数据)时上报此事件。|
|others	|0	|NULL	|0	|忽略此类事件|


###### 使用示例

示例物模型

```json
{
  "productInfo": {
    "productId": 15082482
  },
  "properties": [
    {
      "propertyId": 1,
      "identifier": "ecl",
      "propertyName": "无线信号覆盖等级",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"null\",\"min\":\"-32768\",\"len\":4,\"unitName\":\"\",\"max\":\"32767\""
    },
    {
      "propertyId": 2,
      "identifier": "pci",
      "propertyName": "物理小区标识",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"null\",\"min\":\"-32768\",\"len\":4,\"unitName\":\"\",\"max\":\"32767\""
    },
    {
      "propertyId": 3,
      "identifier": "IMEI",
      "propertyName": "IMEI",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 4,
      "identifier": "rsrp",
      "propertyName": "参考信号接收功率",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"null\",\"min\":\"-32768\",\"len\":4,\"unitName\":\"\",\"max\":\"32767\""
    },
    {
      "propertyId": 5,
      "identifier": "sinr",
      "propertyName": "信号与干扰加噪声比",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"null\",\"min\":\"-32768\",\"len\":4,\"unitName\":\"\",\"max\":\"32767\""
    },
    {
      "propertyId": 6,
      "identifier": "time",
      "propertyName": "当前时间",
      "description": null,
      "dataType": "timestamp",
      "dataSchema": "\"len\":8"
    },
    {
      "propertyId": 7,
      "identifier": "ICCID",
      "propertyName": "ICCID",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 8,
      "identifier": "cell_id",
      "propertyName": "小区位置信息",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"null\",\"min\":\"-2147483648\",\"len\":4,\"unitName\":\"\",\"max\":\"2147483647\""
    },
    {
      "propertyId": 9,
      "identifier": "velocity",
      "propertyName": "水流速",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"m/s\",\"min\":\"0\",\"len\":4,\"unitName\":\"米每秒\",\"max\":\"100\""
    },
    {
      "propertyId": 10,
      "identifier": "act_result",
      "propertyName": "指令执行结果",
      "description": null,
      "dataType": "enum",
      "dataSchema": "\"len\":1,\"enumDetail\":{\"0\":\"执行成功\",\"1\":\"执行失败\"}"
    },
    {
      "propertyId": 11,
      "identifier": "error_code",
      "propertyName": "故障",
      "description": null,
      "dataType": "enum",
      "dataSchema": "\"len\":1,\"enumDetail\":{\"0\":\"正常\",\"1\":\"传感器故障\"}"
    },
    {
      "propertyId": 12,
      "identifier": "water_flow",
      "propertyName": "水流量",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"m³/h\",\"min\":\"0\",\"len\":4,\"unitName\":\"立方米每小时\",\"max\":\"9999999\""
    },
    {
      "propertyId": 13,
      "identifier": "module_type",
      "propertyName": "模组型号",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 14,
      "identifier": "temperature",
      "propertyName": "水温",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"°C\",\"min\":\"0\",\"len\":4,\"unitName\":\"摄氏度\",\"max\":\"100\""
    },
    {
      "propertyId": 15,
      "identifier": "valve_onoff",
      "propertyName": "阀门开关",
      "description": null,
      "dataType": "enum",
      "dataSchema": "\"len\":1,\"enumDetail\":{\"0\":\"关闭\",\"1\":\"开启\"}"
    },
    {
      "propertyId": 16,
      "identifier": "battery_state",
      "propertyName": "电池状态",
      "description": null,
      "dataType": "enum",
      "dataSchema": "\"len\":1,\"enumDetail\":{\"0\":\"正常\",\"1\":\"低电量\"}"
    },
    {
      "propertyId": 17,
      "identifier": "battery_value",
      "propertyName": "电池电量",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"%\",\"min\":\"0\",\"len\":4,\"unitName\":\"百分比\",\"max\":\"100\""
    },
    {
      "propertyId": 18,
      "identifier": "terminal_type",
      "propertyName": "终端型号",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 19,
      "identifier": "back_total_flow",
      "propertyName": "反向累计流量",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"m³\",\"min\":\"0\",\"len\":4,\"unitName\":\"立方米\",\"max\":\"99999999\""
    },
    {
      "propertyId": 20,
      "identifier": "battery_voltage",
      "propertyName": "电池电压",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"V\",\"min\":\"0\",\"len\":4,\"unitName\":\"伏特\",\"max\":\"24\""
    },
    {
      "propertyId": 21,
      "identifier": "hydraulic_value",
      "propertyName": "水压值",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"MPa\",\"min\":\"0\",\"len\":4,\"unitName\":\"兆帕\",\"max\":\"10\""
    },
    {
      "propertyId": 22,
      "identifier": "hardware_version",
      "propertyName": "硬件版本",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 23,
      "identifier": "software_version",
      "propertyName": "软件版本",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 24,
      "identifier": "manufacturer_name",
      "propertyName": "厂家名称",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 25,
      "identifier": "water_consumption",
      "propertyName": "用水量",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"m³\",\"min\":\"0\",\"len\":4,\"unitName\":\"立方米\",\"max\":\"99999999\""
    },
    {
      "propertyId": 26,
      "identifier": "forward_total_flow",
      "propertyName": "正向累计流量",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"m³\",\"min\":\"0\",\"len\":4,\"unitName\":\"立方米\",\"max\":\"99999999\""
    }
  ],
  "services": [
    {
      "serviceId": 1,
      "identifier": "data_report",
      "serviceName": "业务数据上报",
      "serviceType": "DataReport",
      "description": null,
      "properties": [
        {
          "propertyId": 12,
          "serial": 1
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 1002,
      "identifier": "battery_voltage_low_alarm",
      "serviceName": "电池低电压告警",
      "serviceType": "EventReport",
      "description": null,
      "properties": [
        {
          "propertyId": 16,
          "serial": 1
        },
        {
          "propertyId": 20,
          "serial": 2
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 2,
      "identifier": "signal_report",
      "serviceName": "信号数据上报",
      "serviceType": "DataReport",
      "description": null,
      "properties": [
        {
          "propertyId": 4,
          "serial": 1
        },
        {
          "propertyId": 5,
          "serial": 2
        },
        {
          "propertyId": 2,
          "serial": 3
        },
        {
          "propertyId": 1,
          "serial": 4
        },
        {
          "propertyId": 8,
          "serial": 5
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 9001,
      "identifier": "valve_onoff_resp",
      "serviceName": "阀门开关控制响应",
      "serviceType": "CommandResponse",
      "description": null,
      "properties": [
        {
          "propertyId": 15,
          "serial": 1
        },
        {
          "propertyId": 10,
          "serial": 2
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 8001,
      "identifier": "valve_onoff_cmd",
      "serviceName": "阀门开关控制",
      "serviceType": "Command",
      "description": null,
      "properties": [
        {
          "propertyId": 15,
          "serial": 1
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 1001,
      "identifier": "error_code_report",
      "serviceName": "故障上报",
      "serviceType": "EventReport",
      "description": null,
      "properties": [
        {
          "propertyId": 11,
          "serial": 1
        },
        {
          "propertyId": 6,
          "serial": 2
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 3,
      "identifier": "info_report",
      "serviceName": "设备信息上报",
      "serviceType": "DataReport",
      "description": null,
      "properties": [
        {
          "propertyId": 24,
          "serial": 1
        },
        {
          "propertyId": 18,
          "serial": 2
        },
        {
          "propertyId": 13,
          "serial": 3
        },
        {
          "propertyId": 22,
          "serial": 4
        },
        {
          "propertyId": 23,
          "serial": 5
        },
        {
          "propertyId": 3,
          "serial": 6
        },
        {
          "propertyId": 7,
          "serial": 7
        }
      ],
      "parameters": []
    }
  ]
}
```

示例代码

```python
from nb import AEP
import utime
import ustruct

#以下5个函数需要判断如果机器是大端格式数据就不转
def aep_htons(source):
    return source & 0xffff
def aep_htoni(source):
    return source & 0xffffffff


def aep_htonl(source):
    return source & 0xffffffffffffffff

def aep_htonf(source):
    return ustruct.unpack('<I', ustruct.pack('<f', source))[0]

def aep_htond(source):
    return ustruct.unpack('Q', ustruct.pack('d', source))[0]

def HexToStr(source, t=None):
    if t:
        if not isinstance(t, int):
            raise Exception("{} is not int type".format(t))
        fmt = "%0" + str(t*2)+"x"
        return fmt%source
    else:
        if not source >> 8:
            return "%02x" % source
        elif not source >> 16:
            return "%04x" % source
        elif not source >> 32:
            return "%08x" % source
        else:
            return "%016x" % source


def StrToHex(source):
    return int(source)

#对照物模型定义，打包解包根据相应的服务id中的属性进行解析
serid_dict={'阀门开关控制':8001,
            '故障上报':1001,
            '设备信息上报':3,
            '阀门开关控制响应':9001,
            '信号数据上报':2,
            '电池低电压告警':1002,
            '业务数据上报':1
           }
dict_cmd={'数据上报':0x02,
          '事件上报':0x07,
          '无线参数上报':0x03,
          '下行指令固定':0x06,
          '指令响应':0x86
         }
send_type={'RAI_NONE':0,
            'TYpe_001':1,
            'TYpe_002':2,
            'TYpe_100':100,
            'TYpe_101':101,
            'TYpe_102':102
}
servcei_info={
    'ip':"221.229.214.202",
    'port':"5683"
}
modem_type={
    'cache_no_urc':0,
    'no_cache':1,
    'cache_have_urc':2
}
aep_event={
    'psm_event':0,
    'con_event':21,
    'send_event':22,
    'recover_event':23,
    'rst_event':25,
    'recv_event_data':27,
    'recv_event_flag':28,
}

def aep_pack_cmdtype02(service_id,data_in):
    data=HexToStr(dict_cmd['数据上报'],1)
    data+=HexToStr(service_id,2)    			#serviceid转成字符串
    if service_id == 1:
        data+=HexToStr(4,2)	                    #发送数据8.14，float类型四个字节长度,此处只举例一个情况
        data+=HexToStr(aep_htonf(data_in),4)    #float数据转成字符串
    else:
        print('not support')                    #
    return data
 
def aep_pack(cmdtype,service_id,data):
    if cmdtype == dict_cmd['数据上报']:                            #数据上报-0x02，此处只举例一个情况
        return aep_pack_cmdtype02(service_id,data)
    else:
        print('not support')

def aep_unpack_cmdtype06(data_in):
    print('-------------------unpack recv data before  ------------------')
    print(data_in)
    print(data_in[0:4])
    print(data_in[4:8])
    print(data_in[8:12])
    print(data_in[12:])
    print('-------------------unpack recv data before------------------')
    service_id  = int(str(data_in.decode()[0:4]),16)
    service_id  = aep_htons(service_id)
    task_id     = data_in[4:8]
    payload_len = int(str(data_in.decode()[8:12]),16)
    payload_len = aep_htons(payload_len)
    value = 0
    if service_id == serid_dict['阀门开关控制']:                 #物模型下发属性id=15,两个16进制字节,枚举型,0或者1
       value = int(str(data_in.decode()[12:14]),16)
       value = aep_htons(value)
    if service_id == serid_dict['故障上报']:
        pass
    if service_id == serid_dict['设备信息上报']:
        pass
    if service_id == serid_dict['阀门开关控制响应']:
        pass
    if service_id == serid_dict['信号数据上报']:
        pass
    print('-------------------unpack recv data after------------------')
    print("service_id ",service_id)
    print("task_id ",task_id)
    print("payload_len ",payload_len)
    print("payload ",value)
    print('-------------------unpack recv data after------------------')
    
def aep_unpack(data_in):
    cmdtype=StrToHex(str(data_in.decode()[:2]))
    data=data_in[2:]
    if cmdtype == dict_cmd['下行指令固定']:
        aep_unpack_cmdtype06(data)
    else:
        print('not support')



def recv():
    data=bytearray(20)	
    ret=aep.recv(18,data)
    if ret == -1:
        return
    aep_unpack(data)    
    return ret

def connect():
    ret = aep.connect()
    print('connect ',ret)

def send():
    water_flow_value=8.14
    data=aep_pack(dict_cmd['数据上报'],serid_dict['业务数据上报'],water_flow_value)
    print('send: ',data)
    print('len: ',len(data))
    data_len=len(data)
    ret = aep.send(data_len,data,send_type['RAI_NONE'])
    print('send ',ret)

def close():
    ret = aep.close()
    print('close ',ret)
    
def deal_conn(data):
    if data[1] == 0:
        print('connect CtWing success!')
    if data[1] == 3:
        print('subscription /19/0/0 success!')
        send()
    if data[1] == -1 or data[1] == 1:
        print('connect CtWing failed!')
        aep.connect_check()
def deal_recv(data):
    if data[1] == 0:
        aep_unpack(data[2])
        print('will close')
        close()
    if data[1] == 5:
        print('recv data from ctwing falied')
        
def deal_psm(data):
    if data[1] == 0:
        print('enter modem psm')
    if data[1] == 1:
        print('exit modem psm')
def deal_send(data):
    if data[1] == 4:
        print('send data to ctwing success')
    else:
        print('send data to ctwing falied')
        
def deal_rst(data):
    print('recv rst messge from platform')
    close()
def deal_recover(data):
    print('deal_recover:',data)
    
def event_cb(args):
    print('args:',args)
    if args[0] == aep_event['con_event']:
        deal_conn(args)
    if args[0] == aep_event['send_event']:
        deal_send(args)
    if args[0] == aep_event['recv_event_data'] or args[0] == aep_event['recv_event_flag']:
        deal_recv(args)
    if args[0] == aep_event['rst_event']:
        deal_rst(args)
    if args[0] == aep_event['psm_event']:
        deal_psm(args)
    if args[0] == aep_event['recover_event']:
        deal_recover(args)
    
def init():
    
    aep.set_event_callcb(event_cb)
    connect()
    
loop_num = 0

def do_task():
    init()

aep=AEP(servcei_info['ip'],servcei_info['port'],modem_type['no_cache'])
if __name__ == '__main__':
    do_task()

```



#### uping-(ICMP)ping包

模块功能: 模拟发送icmp-ping包



##### ping

- 注意事项

这里可能会存在异常, 由于host地址无法简历socket连接的异常

通过初始化参数中的`COUNT`和`INTERVAL`来周期性的发送Ping包机制

> **import uping**
>
> **up = uping.ping(HOST, SOURCE=None, COUNT=4, INTERVAL=1000, SIZE=64, TIMEOUT=5000, quiet=False)**

- 参数

| 参数     | 类型 | 说明                                                         |
| -------- | ---- | ------------------------------------------------------------ |
| HOST     | str  | 所要ping的域名地址, 例如"baidu.com"                          |
| SOURCE   | str  | 源地址, 用于绑定, 一般情况下不需要传                         |
| COUNT    | int  | 默认是4次,  发送4次ping包                                    |
| INTERVAL | int  | 间隔时间, 默认是ms单位,  默认1000ms                          |
| SIZE     | int  | 每次读取的包大小默认64, 无需修改                             |
| TIMEOUT  | int  | 超时时间, 单位是ms单位, 默认是5000ms即5s                     |
| quiet    | bool | 默认fasle,打印输出, 设置True后, 调用start的后得到的打印的值会被转换成对象返回, 而不是通过打印显示 |

使用示例

```python
# 方式一
# 打印输出方式
import uping
uping.ping('baidu.com')

# 以下是uping.start()的输出, 无返回值
#72 bytes from 49.49.48.46: icmp_seq=1, ttl=53, time=1169.909000 ms
#72 bytes from 49.49.48.46: icmp_seq=2, ttl=53, time=92.060000 ms
#72 bytes from 49.49.48.46: icmp_seq=3, ttl=53, time=94.818000 ms
#72 bytes from 49.49.48.46: icmp_seq=4, ttl=53, time=114.879000 ms
#4 packets transmitted, 4 packets received, 0 packet loss
#round-trip min/avg/max = 92.06000000000001/367.916/1169.909 ms




# 方式二
# 设置quiet会得到输出结果
import uping
result = uping.ping('baidu.com', quiet=True)
# result可以拿到对应数据
# result(tx=4, rx=4, losses=0, min=76.93899999999999, avg=131.348, max=226.697)

```

