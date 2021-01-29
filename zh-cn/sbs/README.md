# 手把手教学

## 入门

### QuecPython 基础操作说明

本文主要介绍 QuecPython 基础操作，包括文件系统以及指令执行。在 QuecPython中，使用主串口作为指令和数据接收通道，所有操作都通过主串口完成。

适用模块：

-   EC100Y-CN（本文以该模块为例进行介绍）

-   EC600S-CN

#### 系统启动

QuecPython 启动后，将在主串口启动交互式解释器，类似于 Linux Shell。通过该交互式解释器，用户可实时地执行命令，并查看返回的结果。

![](media/0f627ce2f6c2f679cd92c7685c3cf148.jpg)

交互式解释器 

其中：

-   执行 **help(obj)**指令，查看帮助；

-   执行 **dir(obj)**指令，查看模块提供的详细方法；

-   执行**help('modules')**指令，查看当前支持的类库。系统启动时，除了进行硬件资源初始化外，还会进行分区挂载，执行初始化脚本操作。启动脚本主要包括两个：

-   *boot.py*：资源初始化等，如启动时挂载分区，该脚本被冻结在出厂固件中；

-   *main.py*：用户初始化脚本，系统初始化完成后执行。

#### 文件系统

在 QuecPython 中，划分了 5 MB
的空间作为用户分区，用户可以将一些配置、脚本等文件存储在该分区中。在系统启动时，会自动挂载该分区，该分区挂载在‘/’目录。

>   在 QuecPython 中，提供了对文件系统访问的类库*uos*，可用于操作和访问文件系统。
>   以下代码示例为如何在当前目录下创建文件、写入内容及读取内容。

```
import uos    # create a file
f=open('test.txt','w')  
f.write('hello quecpython!\n')  
f.write('123456789abcdefg!\n')  
f.close() # read a file 
f=open('test.txt', 'r') 
print(f.readline()) 
print(f.readline()) 
f.close() 
```



>   为方便操作，可使用 *QPYcom.exe* 工具进行常规的文件系统操作。

脚本下载

步骤 **1**：解压 SDK 压缩包内 *tools* 目录下的 *QPYcom.zip*，获取*QPYcom.exe*，并双击运行；

步骤**2**：进入“下载”Tab，点击“创建”按钮，根据需求创建用户项目；

步骤**3**：点击“**+**”按钮，选择需要下载到模块的脚本；

步骤 **4**：点击界面右下方倒三角按钮，切换到“下载脚本”模式；

步骤**5**：点击“**Download FW**”按钮，下载脚本；

步骤 **6**：进度条显示为“**100%**”时，表示下载完成，可进入“文件”Tab查看模块内文件详情。

![](media/5515ac10e5070dd1b9bfd61c7a7022cf.jpg)

>  **2**：脚本下载界面

查看文件

运行 *QPYcom.exe* 工具，点击“查看”-->“文件浏览”，可实现本地与模块进行 Python
文件的上传、查看、添加、删除操作，操作界面及按钮如下图所示。

![](media/277228479c7256251a776b75160dfcec.jpg)

本地与模块进行 **Python** 文件的上传、查看、添加、删除操作 

命令交互

运行 *QPYcom.exe*工具，点击“查看”-->“交互命令行”，进入交互主界面。在交互界面可以通过交互窗口与模块进行手动输入交互，交互主界面说明如图所示。

![](media/c240cbfd8fcee183b8644a9a41320d34.jpg)

交互界面说明 

>  **4** 执行脚本

>   步骤 **1**：解压 SDK 压缩包内 *tools* 目录下的 *QPYcom.zip*，获取*QPYcom.exe*，并双击运行；
>   步骤 **2**：进入“文件”Tab；
>   步骤 **3**：点击下图红框所示按钮，执行脚本文件。

![](media/8431414d399d975a4c26434403a514bd.jpg)

执行脚本界面 

#### 字节码编译

为了提高代码执行速度以及客户代码安全，移远通信提供了 mpy-cross 工具将用户 Python脚本编译为字节码。字节码可固化在固件中，也可以存放在文件系统中供脚本使用。详情请参考

>  《Quectel_QuecPython_mpy-cross 用户指导》

>   Python 脚本编译为字节码的命令为：

>   mpy-cross.exe -o test.mpy -s test.py -march=armv7m test.py

#### 附录 **A** 术语缩写

表 **1**：术语缩写

| 缩写 | 英文全称                                    | 中文全称           |
| ---- | ------------------------------------------- | ------------------ |
| UART | Universal Asynchronous Receiver/Transmitter | 通用异步收发传输器 |







### QuecPython 技术与资源综述

<!-- [QuecPython 技术与资源综述PDF](res.pdf) -->
 <a href="zh-cn/sbs/res/res.pdf" target="_blank">QuecPython 技术与资源综述PDF</a>







## 云平台

### 接入阿里云应用 开发指导

阿里云物联网平台介绍

阿里云物联网平台为设备提供安全可靠的连接通信能力，向下连接海量设备，支撑设备数据采集上云；向上提供云端API，服务端通过调用云端 API将命令下发至设备端，实现远程控制。物联网平台也提供了其他连接管理能力，如设备管理、规则引擎、安全能力等，为各类IoT 场景和行业开发者赋能。

阿里云物联网平台文档：<https://help.aliyun.com/product/30520.html>[。](https://help.aliyun.com/product/30520.html)开发者可以登录该网址进一步了解该物联网平台及设备接入相关知识。

#### 阿里云物联网平台关键的名词解释

如下表格中简单介绍了阿里云物联网平台中关键的名词解释，详细信息可参考阿里云官方文档（URL：
<https://help.aliyun.com/document_detail/30524.html>[）](https://help.aliyun.com/document_detail/30524.html)。

>   表 **1**：关键名词解释

| 关键名词      | 名词解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 产品          | 设备的集合，通常指一组具有相同功能的设备。物联网平台为每个产品颁发全局唯一的 ProductKey。                                                                                                                                                                                                                                                                                                                                                                                                  |
| 设备          | 归属于某个产品下的具体设备。物联网平台为设备颁发产品内唯一的证书 DeviceName。设备可以直接连接物联网平台，也可以作为子设备通过网关连接物联网平台。                                                                                                                                                                                                                                                                                                                                          |
| 子设备        | 本质上也是设备。子设备不能直接连接物联网平台，只能通过网关连接。                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 网关          | 能够直接连接物联网平台的设备，且具有子设备管理功能，能够代理子设备连接云端。                                                                                                                                                                                                                                                                                                                                                                                                               |
| 设备证书      | 设备证书指 ProductKey、DeviceName、DeviceSecret 的组合，用于设备认证以及建立连接。 ProductKey：物联网平台为产品颁发的全局唯一标识。该参数很重要，在设备认证以及通信中都会用到，因此需要您保管好。 DeviceName：在注册设备时，自定义的或系统生成的设备名称，具备产品维度内的唯一性。该参数很重要，在设备认证以及通信中都会用到，因此需要您保管好。  DeviceSecret：物联网平台为设备颁发的设备密钥，和 DeviceName 成对出现。 该参数很重要，在设备认证时会用到，因此需要您保管好并且不能泄露。 |
| ProductSecret | 由物联网平台颁发的产品密钥，通常与 ProductKey 成对出现，用于一型一密的认证方案。该参数很重要，需要您保管好，不能泄露。                                                                                                                                                                                                                                                                                                                                                                     |
| 一机一密      | 每个设备烧录其唯一的设备证书（ProductKey、DeviceName 和 DeviceSecret）。当设备与物联网平台建立连接时，物联网平台对其携带的设备证书信息进行认证。                                                                                                                                                                                                                                                                                                                                           |
| 一型一密      | 同一产品下所有设备可以烧录相同的 ProductKey 和 ProductSecret。设备发送激活 请求时，物联网平台对其携带的 ProductKey 和 ProductSecret 进行认证，认证通过，下发该设备接入所需信息。设备再携带这些信息与物联网平台建立连接。                                                                                                                                                                                                                                                                   |
| 设备 ID²认证  | ID²（Internet Device ID）是一种物联网设备的可信身份标识，具备不可篡改、不可伪造、全球唯一等安全属性。物联网平台支持设备使用 ID²进行身份认证。                                                                                                                                                                                                                                                                                                                                              |
| Topic         | Topic 是 UTF-8 字符串，是设备发布（Pub）、订阅（Sub）消息的传输中介。 发布：设备可以往该 Topic 发布消息。 订阅：设备可以订阅该 Topic 获取消息。                                                                                                                                                                                                                                                                                                                                            |
| 规则引擎      | 通过创建、配置规则，以实现服务端订阅、数据流转和场景联动。                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 物模型        | 是对设备在云端的功能描述，包括设备的属性、服务和事件。物联网平台通过定义一种物的描述语言来描述物模型，称之为 TSL（即 Thing Specification Language），采用 JSON 格式，开发者可以根据 TSL 组装上报设备的数据。                                                                                                                                                                                                                                                                               |

#### 阿里云接口详解

**aLiYun**

>   该方法用于配置阿里云物联网套件的产品信息和设备信息。

-   函数原型

aLiYun(productKey, productSecret, DeviceName, DeviceSecret)

-   参数

    *productKey*：

    产品标识

    *productSecret*：产品密钥。可选参数，默认为 None。

    一机一密认证方案时，此参数传入
    None（不可以为空字符串）；一型一密认证方案时，此参数传入真实的产品密钥。

    *deviceName*：

    设备名称

    *deviceSecret*：设备密钥。可选参数，默认为
    None。一型一密认证方案时此参数传入 None。

     返回值

    返回阿里云连接对象。

**aLiYun.setMqtt**

>   该方法用于设置 MQTT 数据通道的参数。

>   aLiYun.setMqtt(clientID, clean_session, keepAlive)

-   参数

    *clientID*：

    自定义阿里云连接 ID

    *clean_session*：可选参数，一个决定客户端类型的布尔值。默认为 False。如果为
    True，那么代理将在其断开连接时删除有关此客户端的所有信息。如果为
    False，则客户端是持久客户端，当客户端断开连接时，订阅信息和排队消息将被保留。

    *keepAlive*：通信之间允许的最长时间段。范围：60~1200；单位：秒；默认：300。

-   返回值

    无

**aLiYun.setCallback**

>   该方法用于注册回调函数。

-   函数原型

    aLiYun.setCallback(sub_cb)

-   参数

    *sub_cb*：

    回调函数

-   返回值

    无

**aLiYun.subscribe**

>   该方法用于订阅 MQTT 主题。

>   aLiYun.subscribe(topic,qos)

-   参数

    *topic*：

    订阅的 Topic

    *qos*：

    MQTT 消息服务质量。默认值：0。可选择 0 或 1。

-   返回值

    无

**aLiYun.publish**

>   该方法用于发布消息。

-   函数原型

    aLiYun.publish(topic,msg)

-   参数

    *topic*：

    发布的 Topic

    *msg*：

    需要发送的数据

-   返回值

    无

**aLiYun.start**

>   该方法用于开始运行连接。 aLiYun.start()

-   参数

    无

-   返回值

    无

#### 使用 QuecPython 连接阿里云

创建产品与设备

>   使用阿里云物联网平台时，首先需要在云端创建产品和对应设备，获取设备证书（ProductKey、DeviceName 和DeviceSecret）。产品相当于一类设备的集合，同一产品下的设备具有相同的功能。将物联网平台颁发的设备证书烧录到设备上，用于设备连接物联网平台的身份验证。

步骤**1**：
登录阿里云物联网平台控制台[：](https://iot.console.aliyun.com/product)<https://iot.console.aliyun.com/product>[。](https://iot.console.aliyun.com/product)登陆后，依次点击“设备管理”、导航栏的“产品”开始创建产品并进行产品的参数配置。如下图所示：

![](media/0da5c0e906c2dfef5e1066e03eddb533.jpg)

>   图 **1**：创建产品

步骤**2**：
建议参考下图所示的参数进行配置。如需详细了解参数配置，可访问阿里云物联网平台官方地址：https://help.aliyun.com/document_detail/73728.html[。](https://help.aliyun.com/document_detail/73728.html)

创建完成后，点击“确认”保存配置。

![](media/f20ca6b0c04fd992473f2f7474af106c.jpg)

>   图 **2**：创建产品参数配置参考

步骤**3**：
产品指某一类设备，创建产品后，需要为设备创建身份。用户可以创建单个设备，也可以批量创建设备。如下以创建单个设备为例进行详细介绍。依次点击“设备”、“添加设备”开始添加设备，如下图所示：

![](media/42dbaa1445eaa8539bde9e66a7a78d59.jpg)

>   图 **3**：创建设备

步骤**4**：
设备创建成功后，将自动弹出“设备证书”窗口，可以查看、复制设备证书信息，如下图所示。设备证书由设备的ProductKey、DeviceName 和 DeviceSecret
组成，是设备与物联网平台进行通信的重要身份认证，请妥善保管。

![](media/d8152295b16a9524bb60da43dc35f674.jpg)

>   图 **4**：设备证书信息

接入阿里云物联网平台

>   在接入阿里云物联网平台之前，请确认已在阿里云物联网平台控制台创建产品和设备，并获取设备证书信息（ProductKey、DeviceName
>   和 DeviceSecret）。

通过 MQTT.fx 接入阿里云物联网平台并进行测试

接入阿里云物联网平台

>   步骤**1**： 下载并安装 MQTT.fx 软件。

>   步骤**2**： 打开 MQTT.fx
>   软件，单击设置图标![](media/f926080e54c4ffe9aef2234c64143cdd.jpg)。

![](media/9aab3c579e9b1c974e24cb5ca8fa9cc8.jpg)

>   图 **5**：点击设置按钮

>   步骤**3**：
>   设置连接参数。物联网平台目前支持两种连接模式，不同模式设置参数不同。有关参数设置，
>   详见下表。

>   表 **2**：连接参数设置

| 参数名称     | 输入信息         |
|--------------|------------------|
| Profile Name | 输入自定义名称。 |
| Profile Type | MQTT Broker      |

>   表示接入域名，应输入购买的实例的接入域名。请进入阿里云物联网平台控制台实例管理页面查看实例详情中的接入域名信息。

公共实例的接入域名为*${YourProductKey}.iot-as-mqtt.${YourRegionId}.aliyuncs.com*。

>   Broker Address

-   *${YourProductKey}*应替换为设备所属产品的ProductKey（可从物联网平台控制台设备详情页获取 ProductKey）。
    
-   参见地域和可用区，将*${YourRegionId}*替换为自定义的 Region ID。

| Broker Port | 1883                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Client ID   | 填写 mqttClientId，用于 MQTT 的底层协议报文。格式固定：${clientId}|securemode=3,signmethod=hmacsha1|。完整示例：*12345|securemode=3,signmethod=hmacsha1|*。其中：  *${clientId}*为设备的 ID 信息。可取任意值，长度在 64 字符以内。建议使用设备的                                                                                                                                                                                                                                                                                                                                                    |
|             | MAC 地址或 SN 码。 *securemode* 为安全模式，TCP 直连模式设置为 *securemode=3*，TLS 直连为 *securemode=2*。 *signmethod* 为算法类型，支持 hmacmd5 和 hmacsha1。                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| General     | General 栏目下的设置项可保持系统默认，也可以根据具体需求设置。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| User Name   | 由设备名 DeviceName、符号（&）和产品 ProductKey 组成。固定格式：${YourDeviceName}&${YourProductKey}。完整示例如：device&alxxxxxxxxx。                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Password    | 下载 Password 生成小工具。 进入 <https://files.alicdn.com/tpsservice/88413c66e471bec826257781969d1bc7.zip> [解](https://files.alicdn.com/tpsservice/88413c66e471bec826257781969d1bc7.zip)压缩下载包后，双击 *sign* 文件，即可使用。使用 Password 生成小工具的输入参数：  productKey：设备所属产品 Key。可在控制台设备详情页查看。 deviceName：设备名称。可在控制台设备详情页查看。 deviceSecret：设备密钥。可在控制台设备详情页查看。 timestamp：（可选）时间戳。 clientId：设备的 ID 信息，与 Client ID 中*${clientId}*一致。 method：选择签名算法类型，与 Client ID 中 *signmethod* 确定的加密方法一致 |

>   备注

1.  输入 Client ID 信息后，请勿单击“**Generate**”。

2.  TCP 直连时，Client ID 中 securemode=3，无需设置 SSL/TLS 信息。

3.  TLS 直连时，Client ID 中 securemode=2，需要设置 SSL/TLS 信息。

4.  设置参数时，请确保参数值中或参数值的前后均没有空格。

    连接参数信息设置示例如下图所示：

![](media/e2085274508cac96952fdfe232d0c4b4.jpg)

>   图 **6**：配置参数

>   步骤**4**：
>   连接参数设置完成后，点击“**OK**”确认应用。然后点击“**Connect**”按钮连接阿里云物联网
>   平台。

![](media/9a1039ed5ae22e349c21f6c8fcbe1dc9.jpg)

>   图 **7**：设备详情页面

进行数据测试

下行数据测试

>   下行数据测试是指从阿里云物联网平台发送消息，在 MQTT.fx 上接收消息，测试
>   MQTT.fx 与物联网平台连接是否成功。

>   步骤**1**： 在 MQTT.fx 上，单击导航栏中的“**Subscribe**”。

>   步骤**2**： 输入一个设备具有订阅权限的自定义
>   Topic，单击“**Subscribe**”，订阅该 Topic，如下图所示。

![](media/20ba8885738df4172d61acebdcf0aa43.jpg)

>   图 **8**：订阅自定义 **Topic**

![](media/d516adcc620700e25a229ebfc3dc33fe.jpg)

图 **9**：自定义 **Topic**

>   步骤**3**： 订阅成功后，该 Topic 将显示在列表中，如下图所示：

![](media/6d3f940f6bbc0f8bffc344aace5b8de9.jpg)

>   图 **10**：订阅成功

>   步骤**4**： 在物联网平台控制台中的该设备的设备详情的 Topic列表页下，单击已订阅的 Topic 对应的 发布消息。输入消息内容，单击“确认”。

![](media/9a0a7aa791766b583716d7c2cff312d5.jpg)

>   图 **11**：物联网平台发布消息

>   步骤**5**： 登录 MQTT.fx
>   软件，查看是否接收到上一步骤输入的消息，如下图所示：

![](media/90a8a0a1f6234753ecd29e7e2132f4ce.jpg)

>   图 **12**：客户端接收到物联网平台消息

上行数据测试

上行数据测试是指在 MQTT.fx 上发送消息，通过物联网平台查看设备日志，测试MQTT.fx 与物联网平台连接是否成功。

>   步骤**1**： 在 MQTT.fx 上，单击导航栏的“**Publish**”。

>   步骤**2**： 输入一个设备具有发布权限的 Topic和需要发送的消息内容，单击“**Publish**”，向这个 Topic推送一条消息。如下图所示。

![](media/6a9b5bd82fc31d7fbb8a885cc24c3543.jpg)

>   图 **13**：向物联网平台发布数据

>   步骤**3**：
>   在物联网平台控制台，依次点击“监控运维”、“日志服务”、“云端运行日志”，查看该设备的云消息。

![](media/6b0cd9b99e274453b1fcdf0961b5217b.jpg)

>   图 **14**：查看消息内容

使用 QuecPython 接入阿里云物联网平台

>   在 EC100Y-CN上运行以下代码，运行方法详见《Quectel_QuecPython_基础操作说明》。

```
 from aLiYun import aLiYun 
 import utime 
 productKey = "a1b2gBFGcLF" # 产品标识 
 productSecret = None # 产品密钥（一机一密认证此参数传入 None） 
 DeviceName = "smartLight" # 设备名称 
 DeviceSecret = "78a3407e7d43b445cd2dd895cec50ffa" # 设备密钥（一型一密认证此参数传入 None） 
 # 创建 aliyun 连接对象 
 ali = aLiYun(productKey, productSecret, DeviceName, DeviceSecret) # 设置 mqtt 连接属性 
 clientID = "12345" # 自定义字符（不超过 64） 
 ali.setMqtt(clientID, clean_session=False, keepAlive=300) # 回调函数 
 def sub_cb(topic, msg): 
 	print("subscribe recv:") 
 	print(topic, msg) 
 # 设置回调函数 
 ali.setCallback(sub_cb) 
 topic = "/a1b2gBFGcLF/smartLight/user/get" # 主题 
 # 订阅主题 
 ali.subscribe(topic) 
 topicP="/a1b2gBFGcLF/smartLight/user/update" # 发布消息 
 ali.publish(topic, "hell world") # 运行 
 ali.start() 
 utime.sleep(2) 
```

>   代码运行结果如下：

设备上行从阿里云物联网平台端查看日志，如下图所示：

![](media/c542639b55ad51c52e8a0036d1ca25eb.jpg)

图 **15**：查看消息内容

云端发布消息，设备在 *sub_cb* 回调函数中接收，如下图所示：

![](media/e4c3f24d1835777199a0d86d71bc4dd6.jpg)

图 **16**：发送消息

![](media/70658f75cc3656d9613fb7be881895ab.jpg)

#### 附录 A 参考文档及术语缩写

>   参考文档

Quectel_QuecPython_基础操作说明 QuecPython 上传下载文件说明

>   表 **4**：术语缩写

| 术语 | 英文全称 中文全称                                                     |                          |
|------|-----------------------------------------------------------------------|--------------------------|
| API  | Application Programming Interface 应用程序编程接口                    |                          |
| ID   | Mostly refers to Identifier in terms of 软件中多数指“标识符” software |                          |
| ID²  | Internet Device ID                                                    | 物联网设备的可信身份标识 |
| IoT  | Internet of Things                                                    | 物联网                   |
| MAC  | Medium Access Control                                                 | 媒体访问控制             |
| MQTT | Message Queuing Telemetry Transport                                   | 消息队列遥测传输         |
| SN   | Serial Number                                                         | 序列号                   |
| TCP  | Transmission Control Protocol                                         | 传输控制协议             |
| TLS  | Transport Layer Security                                              | 传输层安全（协议）       |
| TSL  | Thing Specification Language                                          | 物模型                   |



### 接入腾讯云应用 开发指导

物联网平台为设备提供安全可靠的连接通信能力，向下连接海量设备，支撑设备数据采集上云；向上提供云端 API，服务端通过调用云端 API 将指令下发至设备端，实现远程控制。物联网平台也提供了其他 连接 管理能力，如设备管理、规则引擎 、安全能力等，为各类IoT场景和行业开发者赋能。

- 腾讯云物联网平台文档： [https://cloud.tencent.com/document/product/634 ](https://cloud.tencent.com/document/product/634)
- 腾讯云物联网平台管理： [https://console.cloud.tencent.com/iothub ](https://console.cloud.tencent.com/iothub/product/U2D3JII78Y/log)

开发者可以登录如上网址进一步了解该物联网平台及设备接入相关知识。



#### 创建产品与设备

步骤 **1**： 登录腾讯云物联网平台（ [https://console.cloud.tencent.com/iothub），](https://console.cloud.tencent.com/iothub)显示界面如下：

![Quectel_QuecPython_腾讯云IoT平台_014.png](media/Quectel_QuecPython_腾讯云IoT平台_014.png)

​															  图 **1** ： 腾讯云登录界面

步骤 **2**： 点击“ 创建新产品 ，” 新建一个产品名称并选择“ 密匙认证 ”及“ 自定义 ”数据格式，如下图

所示： 

![Quectel_QuecPython_腾讯云IoT平台_015.png](media/Quectel_QuecPython_腾讯云IoT平台_015.png)

​																	图**2** ： 新建产品

步骤 **3**： 点击“ 确定 ，将” 出现下图产品列表界面：

![Quectel_QuecPython_腾讯云IoT平台_016.png](media/Quectel_QuecPython_腾讯云IoT平台_016.png)

​																	图 **3** ： 产品列表

步骤 **4**： 进入产品管理，出现如 下图所示的 设备列表界面：

![Quectel_QuecPython_腾讯云IoT平台_017.png](media/Quectel_QuecPython_腾讯云IoT平台_017.png)

​																图 **4**： 设备列表界面

步骤 **5**： 依次点击“ 设备列表 、”“ 添加新设备 ，”开始新建设备名称及密钥，设置后点击“ 保存 ，”如下

图所示： 

![Quectel_QuecPython_腾讯云IoT平台接入_018.png](media/Quectel_QuecPython_腾讯云IoT平台接入_018.png)

​																	图 **5**： 创建新设备 

步骤 **6**： 创建新设备后，将出现创建成功界面提示，详情如下：

![Quectel_QuecPython_腾讯云IoT平台接入_019.png](media/Quectel_QuecPython_腾讯云IoT平台接入_019.png)

​																	图 **6**： 设备创建成功提示

步骤 **7**： 点击上图中的“ 开始管理设备 ，” 进入设备详细信息界面，如下图所示：

![Quectel_QuecPython_腾讯云IoT平台接入_020.png](media/Quectel_QuecPython_腾讯云IoT平台接入_020.png)

​																		图 **7**： 设备详情页面

步骤 **8**： 复制并保存设备密钥和 client id 等信息，如下图所示

![Quectel_QuecPython_腾讯云IoT平台接入_021.png](media/Quectel_QuecPython_腾讯云IoT平台接入_021.png)

​																			图 **8**： 设备密钥

步骤 **9**： 进入“ 权限列表'' ，可以查阅 相关发布订阅的 Topic，如下图所示： 

![Quectel_QuecPython_腾讯云IoT平台接入_022.png](media/Quectel_QuecPython_腾讯云IoT平台接入_022.png)

​																			图 **9**： topic列表

#### 编写腾讯云测试程序

步骤 **1**： 将开发板接入电脑 。接入后的操作方法详见《 Quectel_QuecPython_基础操作说明》。

![Quectel_QuecPython_腾讯云IoT平台接入_023.png](media/Quectel_QuecPython_腾讯云IoT平台接入_023.png)

​																		图 **10**：开发板接入电脑

步骤 **2**： 创建 *test.py* 文件，编写以下代码，并将 第 ***3.1*** 章 保存的相关参数填充至代码中，如下所示：

```python
from TenCentYun import TXyun 

productID = "U2D3JII78Y"  #  产品标识 
devicename = "dev1"  #  设备名称 
devicePsk = "p2h/OlKGnOPMdugNTGAFrg=="  #  设备密钥（一型一密认证此参数传入 None） ProductSecret = None  #  产品密钥（一机一密认证此参数传入 None） 

tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)  #  创建连接对象

def sub_cb(topic, msg):  #  云端消息响应回调函数
	print("subscribe recv:") 
    print(topic, msg) 

tenxun.setMqtt() 
tenxun.setCallback(sub_cb) 
topic_sub = "U2D3JII78Y/dev1/control"  #  输入订阅 Topic 
topic_pub = "U2D3JII78Y/dev1/event"  #  输入发布 Topic 
tenxun.subscribe(topic_sub) 
tenxun.publish(topic_pub, "hello world") 
tenxun.start() 
```

步骤 **3**： 将 test.py 文件上传到开发板，上传方法详见《 Quectel_QuecPython_基础操作说明 》。 

步骤 **4**： 在 EC100Y-CN 开发板运行 *test.py* 文件，如下图所示：

![Quectel_QuecPython_腾讯云IoT平台接入_025.png](media/Quectel_QuecPython_腾讯云IoT平台接入_025.png)

​															图 **11**：运行 **test.py** 文件 

#### 订阅腾讯云服务器消息

步骤 **1**： 打开腾讯云设备的“在线调试”页面，选择如图所示 Topic，在“消息内容”框中输入任意内

容后点击“ 发送消息 ，如” 下图所示：

![Quectel_QuecPython_腾讯云IoT平台接入_026.png](media/Quectel_QuecPython_腾讯云IoT平台接入_026.png)

​															图 **12**：编写消息内容 

步骤 **2**： 设备端将接收到腾讯云发送的订阅消息，如下图所示：

![Quectel_QuecPython_腾讯云IoT平台接入_027.png](media/Quectel_QuecPython_腾讯云IoT平台接入_027.png)

​															图 **13**：设备订阅消息接收界面

#### 设备向腾讯云发布消息

打开腾讯云的“ 产品列表 ”依次点击“设备管理” --> “云日志” -->“行为日志” ，可以查看设备侧向腾讯云平台发布的消息，如下图所示： 

![Quectel_QuecPython_腾讯云IoT平台接入_028.png](media/Quectel_QuecPython_腾讯云IoT平台接入_028.png)

​															图 **14**：腾讯云接收到设备发布消息

#### 附录A参考文档及术语缩写

表 **1**：参考文档

| 序号 | 文档名称                          | 备注                        |
| ---- | --------------------------------- | --------------------------- |
| [1]  | Quectel_QuecPython_基础操作说明 | QuecPython 上传下载文件说明 |

表 **2**：术语缩写

| 术语 | 英文全称                          | 中文全称         |
| ---- | --------------------------------- | ---------------- |
| API  | Application Programming Interface | 应用程序编程接口 |
| IoT  | Internet of Things                | 物联网           |


## 通信

### MQTT应用 开发指导

#### MQTT概述

**MQTT简介**

MQTT是基于代理的发布/订阅模式通讯协议，具有开放、简单、轻量和易于实现等特点。MQTT最大优点在于，可以以极少的代码和有限的网络带宽，为远程设备连接提供实时可靠的消息服务。由于规范简单，适合对低功耗要求严格和网络带宽有限的物联网场景，例如：遥感数据、汽车、智能家居、智慧城市和医疗医护等。

**MQTT设计原则**

MQTT协议遵循以下设计原则：

1.  功能精简。

2. 采用发布/订阅（Pub/Sub）模式，方便消息传递。
3. 允许用户动态创建主题，降低运营成本。
4. 降低传输量至最低，提高传输效率。
5. 关注低带宽、高延迟、不稳定的网络等因素。
6. 支持连续会话控制。
7. 对客户端计算能力包容性强。
8. 提供服务质量管理。
9. 对传输数据的类型与格式无强制要求，保持灵活性。

**MQTT业务场景**

运用MQTT协议，设备可以方便地连接到物联网云服务，管理设备并处理数据，最后应用到各种业务场景，如下图所示：

![](media/图1_MQTT业务场景.jpg)

图 1 ：MQTT业务场景

**MQTT发布/订阅模式**

发布/订阅模式提供传统客户端-服务器体系结构的替代方法。在客户端服务器模型中，客户端直接与端点进行通信。发布/订阅模型解耦了发送消息的客户端（发布者）与接收消息的客户端（订阅者）之间的关系，二者并不直接建立联系。发布者与订阅者之间由第三个组件（代理）进行连接，代理过滤所有传入的消息，并将其正确分发给订阅者。

发布/订阅模式优点如下：

​		1. 发布者与订阅者无需互相知悉，只需使用同一个代理即可。

​		2. 发布者和订阅者无需交互，发布者不必因等待订阅者确认而导致锁定。

​		3. 发布者和订阅者无需同时在线，可自由选择时间发布/接收消息。

**MQTT协议原理**

![](media/图2_MQTT协议原理图示.jpg)

​															图 2 ：MQTT协议原理图示

1. 实现MQTT协议需要：客户端和服务器端。

2. MQTT协议中有三种身份：发布者（Publisher）、代理（Broker）、订阅者（Subscriber）。其

中，消息的发布者和订阅者都是客户端，消息代理是服务器，消息发布者可以同时是订阅者。

3. MQTT传输的消息分为：主题（Topic）和负载（Payload）两部分：
   	Topic，可以理解为消息的类型，订阅者订阅后，就会收到该主题的消息内容；
       		Payload，可以理解为消息的内容，是指订阅者具体要使用的内容。

**MQTT中的相关方法**

​		MQTT中定义了一些方法（或动作），来于表示对确定资源所进行操作。这个资源可以代表预先存在的数据或动态生成数据，这取决于服务器的实现。通常来说，资源是指服务器上的文件或输出：

 Connect，等待与服务器建立连接；
 Disconnect，等待MQTT客户端完成所做的工作，并与服务器断开TCP/IP会话；
 Subscribe，等待完成订阅；
 UnSubscribe，等待服务器取消客户端的一个或多个topics订阅；
 Publish，MQTT客户端发送消息请求，发送完成后返回应用程序线程。

**MQTT主题**

​		MQTT通过主题对消息进行分类。主题一般是一个UTF- 8 的字符串，可通过符号“/”表示层级关系。主题可直接使用，无需再次创建。主题还可以通过通配符进行过滤，其中，“+”用于过滤一个层级，“#”一般位于主题后表示过滤任意级别的层级。示例如下：

1. building-b/floor- 5 ：代表B楼 5 层的设备。
2. +/floor- 5 ：代表任何一个楼的 5 层的设备。
3. building-b/#：代表B楼所有的设备。

备注

MQTT允许使用通配符订阅主题，但并不允许使用通配符广播。



**MQTT服务质量**

MQTT支持三种不同级别的服务质量，为不同场景保证消息传输的可靠性。

​		级别 0 ：最多一次。

​				消息发送者仅发送一次，不会重复发送。一般用于传输不重要数据的场景。

​	 	级别 1 ：至少一次。

​				消息发送者发送消息以后，若未收到消息接收者的确认信息，则会再次发送，直到接收到消息接受者的确认信息。这种情况可能导致重复消息。一般用于日志处理的场景。

 		级别 2 ：只发送一次。

​				消息发送者发送消息以后等待消息接收者的确认消息，接收到确认消息后消息发送者删除消息并通知消息接收者。如此会减少并发或者增加延时，但是若数据丢失或者重复消息不可接受时，可

设置为级别 2 。




#### MQTT API

**MQTTClient**

该函数用于构建MQTT连接对象。

函数原型

```
MQTTClient(client_id, server, port=0, user=None, password=None, keepalive=0, ssl=False,ssl_params={})
```



参数

client_id：

字符串类型。客户端ID，具有唯一性，也可能是经过加密处理后的client_id，例如阿里云。

server：
字符串类型。服务端地址，可以是IP或者域名。

port：
（可选）整型。服务器端口，默认为 1883 ，通过SSL/TLS的MQTT的默认端口是 8883 。

user：
（可选）字符串类型。在服务器上注册的用户名，也可能是经过加密处理的用户名，例如阿里云。

password：
（可选）字符串类型。在服务器上注册的密码，也可能是经过加密处理的密 码，例如阿里云。

keepalive：
（可选）整型。客户端的keepalive超时值。默认为 60 秒，范围为60~120秒。

ssl：
（可选）布尔型。是否使能支持SSL/TLS。

ssl_params：
（可选）字符串类型。SSL/TLS参数。



返回值

MQTT对象。



**MQTTClient.set_callback**

该函数用于设置回调函数。

函数原型

```
MQTTClient.set_callback(callback)
```

参数

```
callback：
消息回调函数。
```

返回值

无。



**MQTTClient.connect**

该函数用于与服务器建立连接。

函数原型

```
MQTTClient.connect(clean_session=True)
```

参数

clean_session：
布尔型。可选参数，一个决定客户端类型的布尔值。如果为True，那么代理将在其断开连接时删除有
关此客户端的所有信息。如果为False，则客户端是持久客户端，当客户端断开连接时，订阅信息和排
队消息将被保留。默认为False。

返回值

无。

**MQTTClient.disconnect**

该函数用于与服务器断开连接。

函数原型

```
MQTTClient.disconnect()
```

参数

无。

返回值

无。



**MQTTClient.ping**

该函数用于向服务器发送ping包，检测保持连通性。

函数原型

```
MQTTClient.ping()
```

参数

无。

返回值

无。



**MQTTClient.publish**

该函数用于发布消息。

函数原型

```
MQTTClient.publish(topic,msg)
```

参数

topic：
字符串类型。消息主题。

msg：
字符串类型。需要发送的数据。

返回值

无。



**MQTTClient.subscribe**

该函数用于订阅MQTT主题。

函数原型

```
MQTTClient.subscribe(topic,qos)
```

参数

topic：
字符串类型。MQTT主题。

msg：
字符串类型。MQTT消息服务质量，默认为 0 ，可选择 0 或 1 。

返回值

无。

**MQTTClient.check_msg**

该函数用于检查服务器是否有待处理消息。

函数原型

```
MQTTClient.check_msg()
```

参数

无。

返回值

无。



**MQTTClient.wait_msg**

该函数用于等待服务器消息响应。

函数原型

```
MQTTClient.wait_msg()
```

参数

无。

返回值

无。



**MQTTClient.set_last_will**

​		该函数用于设置要发送给服务器的遗嘱，客户端没有调用disconnect()异常断开，则发送通知到客户端。

函数原型

```
MQTTClient.set_last_will(topic,msg,retain=False,qos=0)
```

参数

topic：
字符串类型。遗嘱主题。

msg：
字符串类型。遗嘱内容。

retain：
布尔型。retain=True boker会一直保留消息，默认为False。

qos：
整型。消息服务质量，范围为0~2。

返回值

无。



#### MQTT开发说明

**MQTT服务器搭建和测试**

​	上位机安装MQTT服务器，即消息代理。本文档以mosquitto开源消息代理软件为例。

**搭建MQTT服务器**

1. Linux系统通过以下命令进行安装。
2. Windows系统访问https://mosquitto.org/download/下载适配版本的.exe安装包。

以Windows 系统为例，安装完成后进入 mosquitto 安装目录，启动命令行执行如下命令，查看
mosquitto的用法：

```
mosquitto -h
```

![](media/图3_mosquitto帮助信息.jpg)

​															图 3 ：mosquitto帮助信息

​		上图中的两个关键参数-c和-p，-c用于指定MQTT服务的配置，-p用于指定服务端口。

**启动MQTT服务器**

​		启动MQTT 服务器前，要确保服务器所在网络能够被设备访问。在命令行中键入以下命令，启动

MQTT服务：

```
mosquitto -c mosquitto.conf -p 10080 –v
```

​		测试阶段，配置文件直接使用安装目录下的默认配置即可；本测试本地端口使用 10080 。

![](media/图4_MQTT服务器启动成功.jpg)

​														图 4 ：MQTT服务器启动成功

**验证MQTT服务器有效性**

**安装MQTT客户端**

本文档以MQTT.fx的客户端为例。访问http://mqttfx.bceapp.com，下载并安装客户端软件。

安装完成后，打开MQTT.fx，默认进入发布界面，如下图所示：

![](media/图5_MQTT.fx启动界面.jpg)

​																		图 5 ：MQTT.fx启动界面

**配置MQTT客户端**

​		点击上图中配置按钮 ，添加MQTT连接配置。

​		配置界面默认添加了m2m.eclipse.org和mosquitto服务的配置。可修改任意配置，主要修改“Broker
Address”（代理地址）和“Broker Port”（代理端口）两项。亦可点击配置界面左下角的加号，添加自定义服务连接配置。

​			配置选项“General”、“User Credentials”、“SSL/TLS”、“Proxy”和“LWT”，可根据服务
器的要求进行配置，包括连接超时时间、保活时间间隔、MQTT协议版本、用户名/密码及SSL相关配置。

本文中采用默认配置。

![](media/图6_MQTT连接配置.jpg)

​																			图 6 ：MQTT连接配置

**MQTT交互测试**

1. 建立MQTT连接

​      在 MQTT.fx 启动后进入的默认界面点击“Connect”按钮，建立 MQTT 连接。连接成功后mosquitto服务器打印的日志请参考MQTT服务器与客户端交互。连接成功后即可发布消息、订阅主题，默认已填充待订阅和发布的消息主题。

![](media/图7_MQTT服务器与客户端交互.jpg)

​														图 7 ：MQTT服务器与客户端交互

![](media/图8_发布消息.jpg)

​														图 8 ：发布消息

![](media/图9_订阅主题.jpg)

​														图 9 ：订阅主题

​		MQTT允许用户动态创建主题，也可动态修改主题。将待订阅和发布的消息主题配置一致，如此可实现回显功能。客户端向服务器发布的消息可立即分发至到客户端。


#### 使用MQTT进行数据发布订阅

本测试采用echo功能作为测试示例。

步骤 1 ： 开发板接入电脑，接入后详细操作方法，请参考《Quectel_QuecPython_基础操作说明》。

![](media/图10_接入开发板.jpg)

​															图 10 ：接入开发板

步骤 2 ： 建立test.py文件，导入umqtt模块，我们以连接mq.tongxinmao.com网址为例创建以下代
码：

```
from umqtt import MQTTClient
state = 0
def sub_cb(topic, msg):
	global state
	print("subscribe recv:")
	print(topic, msg)
	state = 1

#创建一个mqtt实例
c = MQTTClient("umqtt_client", "mq.tongxinmao.com", '18830')
#设置消息回调
c.set_callback(sub_cb)
#建立连接

c.connect()
#订阅主题
c.subscribe(b"/public/TEST/quecpython")
print("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic" )
#发布消息
c.publish(b"/public/TEST/quecpython", b"my name is Kingka!")
print("Publish topic: /public/TEST/quecpython, msg: my name is Quecpython")

while True:
	c.wait_msg() #阻塞函数，监听消息
	if state == 1:
		break

#关闭连接
c.disconnect()
```



备注

也 可 以 通过访 问 通 信 猫 在 线 客 户 端 服 务 器 进 行 MQTT 验 证 ：

http://www.tongxinmao.com/txm/webmqtt.php。

![](media/图11_通信猫在线客户端服务器.jpg)

​														图 11 ：通信猫在线客户端服务器



步骤 3 ： 将 test.py 文件上传至 EC1 00 Y-CN QuecPython 开发板内，详细上传方法请参考
《Quectel_QuecPython_基础操作说明》。



步骤 4 ： 在开发板中运行test.py文件，即可以看到模块执行结果，如下图所示：

![](media/图11_通信猫在线客户端服务器.jpg)


#### 附录

表 1 ：术语缩写

```
缩写 			英文全称 									中文全称

API 		Application Programming Interface 			应用程序编程接口

IP 			Internet Protocol 							网际互连协议

MQTT 		Message Queuing Telemetry Transport 		消息队列遥测传输

SSL 		Secure Sockets Layer 						安全套接层

TLS 		Transport Layer Security 					传输层安全（协议）
```




### HTTP应用 开发指导

#### **HTTP协议基础**

**HTTP协议**

HTTP协议是用于从万维网服务器传输超文本到本地浏览器的传送协议。基于TCP的应用层协议，它不关心数据传输的细节，HTTP（超文本传输协议）是一个基于请求与响应模式的、无状态的、应用层的协议，只有遵循统一的HTTP请求格式，服务器才能正确解析不同客户端发的请求，同样地，服务器遵循统一的响应格式，客户端才得以正确解析不同网站发过来的响应。

![Client与Server通信](media/de988b13c542b7f454d13cc183693d82.png)

#### HTTP请求

HTTP请求由请求行、请求头、空行、请求体组成。

![HTTP请求构成](media/30dd898d830b27416fd3b691ae64e3dd.png)

**请求行**

请求行由请求方式 + URL+ 协议版本组成。

-   常见的请求方法有GET、POST、PUT、DELETE、HEAD；

-   URL：客户端要获取的资源路径；

-   协议版本：客户端使用的HTTP协议版本号（目前使用的是http1.1）。

**请求头**

请求头是客户端向服务器发送请求的补充说明。

-   host：请求地址；

-   User-Agent：客户端使用的操作系统和浏览器的名称和版本；

-   Content-Length：发送给HTTP服务器数据的长度；

-   Content-Type：参数的数据类型；

-   Cookie：将cookie的值发送给HTTP 服务器；

-   Accept-Charset：浏览器可接受的字符集；

-   Accept-Language：浏览器可接受的语言；

-   Accept：浏览器可接受的媒体类型。

**请求体**

请求体携带请求参数。

-   application/json：{"name":"value","name1":"value2”}；

-   application/x-www-form-urlencoded： name1=value1&name2=value2；

-   multipart/from-data：表格形式；

-   text/xml；

-   content-type：octets/stream。

#### HTTP响应

HTTP响应由状态行、响应头、空行、响应体组成。

![HTTP响应构成](media/800f014c0ddfdeeef025fd803aa23697.png)

**状态行**

状态行由HTTP 版本号 + 响应状态码 + 状态说明组成。

响应状态码有1XX、2XX、3XX、4XX、5XX。

-   1XX：提示信息 - 表示请求已被成功接收，继续处理；

-   2XX：成功 - 表示请求已被成功接收，理解，接受；

-   3XX：重定向 - 要完成请求必须进行更进一步的处理；

-   4XX：客户端错误 - 请求有语法错误或请求无法实现；

-   5XX：服务器端错误 - 服务器未能实现合法的请求响应头。

**响应头**

响应头与请求头对应，是服务器对该响应的一些附加说明。

**响应体**

为真正的响应数据，即为网页的HTML源代码。

#### URL

URL是WWW的统一资源定位标志，就是指网络地址。

URL格式：https://host:port/path?xxx=aaa&ooo=bbb

其中：

-   http/https：这个是协议类型

-   host：服务器的IP地址或者域名

-   port：HTTP服务器的端口，默认端口是80

-   path：访问资源的路径

-   url里面的？这个符号是个分割线，用来区分问号前面的是path，问号后面的是参数

-   url-params：问号后面的是请求参数，格式：xxx=aaa。多个参数用&符号连接

#### HTTP协议请求方法

HTTP1.0定义了三种请求方法：GET、POST和HEAD方法。HTTP1.1新增了五种请求方法：OPTIONS、PUT、DELETE、TRACE和CONNECT方法。

-   GET：请求指定的页面信息，并返回实体主体。

-   POST：向指定资源提交数据进行处理请求，数据被包含在请求体中。

-   HEAD：返回的响应中没有具体的内容，用于获取报头。

-   OPTIONS：返回服务器针对特定资源所支持的HTTP请求方法，也可以利用向web服务器发送‘*’
    的请求来测试服务器的功能性

-   PUT：向指定资源位置上传其最新内容

-   DELETE：请求服务器删除Request-URL所标识的资源

-   TRACE：回显服务器收到的请求，主要用于测试或诊断

-   CONNECT：*HTTP1.1*协议中预留给能够将连接改为管道方式的代理服务器。

#### HTTP接口

**request.get**

该函数用于发送GET请求。

-   **函数原型**

request.get(url, data, json, headers) 

-   **参数**

*url*：网址，字符串类型。

*data*：（可选参数）附加到请求的正文，json字典类型，默认为None。

*json*：（可选参数）json格式用于附加到请求的主体，默认为None。

*headers*：（可选参数）请求头，默认为None。

-   **返回值**

返回请求对象

**request.post**

该函数用于发送POST请求。

-   **函数原型**

request.post(url, data, json, headers)

-   **参数**

*url*：网址，字符串类型。

*data*：（可选参数）附加到请求的正文，json字典类型，默认为None。

*json*：（可选参数）json格式用于附加到请求的主体，默认为None。

*headers*：（可选参数）请求头，默认为None。

-   **返回值**

返回请求对象

**request.put**

该函数用于发送PUT请求。

-   **函数原型**

request.put(url, data, json, headers)

-   **参数**

*url*：网址，字符串类型。

*data*：（可选参数）附加到请求的正文，json字典类型，默认为None。

*json*：（可选参数）json格式用于附加到请求的主体，默认为None。

*headers*：（可选参数）请求头，默认为None。

-   **返回值**

返回请求对象

**request.head**

该函数用于发送HEAD请求。

-   **函数原型**

request.head(url, data, json, headers)

-   **参数**

*url*：网址，字符串类型。

*data*：（可选参数）附加到请求的正文，json字典类型，默认为None。

*json*：（可选参数）json格式用于附加到请求的主体，默认为None。

*headers*：（可选参数）请求头，默认为None。

-   **返回值**

返回请求对象

**request.patch**

该函数用于发送PATCH请求。

-   **函数原型**

request.patch(url, data, json, headers)

-   **参数**	

*url*：网址，字符串类型。

*data*：（可选参数）附加到请求的正文，json字典类型，默认为None。

*json*：（可选参数）json格式用于附加到请求的主体，默认为None。

*headers*：（可选参数）请求头，默认为None。

-   **返回值**

返回请求对象

**request.delete**

该函数用于发送DELETE请求。

-   **函数原型**

request.delete(url, data, json, headers) 

-   **参数**

*url*：网址，字符串类型。

*data*：（可选参数）附加到请求的正文，json字典类型，默认为None。

*json*：（可选参数）json格式用于附加到请求的主体，默认为None。

*headers*：（可选参数）请求头，默认为None。

-   **返回值**

返回请求对象

**reponse类方法说明**

response =request.get(url)

| **方法**         | **说明**                                |
| ---------------- | --------------------------------------- |
| response.content | 返回响应的内容，以字节为单位            |
| response.text    | 以文本方式返回响应的内容，编码为unicode |
| response.json()  | 返回响应的json编码内容并转为dict类型    |
| response.close() | 关闭socket                              |

#### 示例

将QuecPython开发板连接至电脑，接入后的操作方法详见《Quectel_QuecPython_基础操作说明》。

开发板连接至电脑后，创建*test.py*文件，导入QuecPython的*request*模块，分别创建HTTP GET/PUT/POST/DELETE等请求代码，编写完成后，将文件上传到开发板内并运行*test.py*文件，方法详见《Quectel_QuecPython_基础操作说明》。示例代码及运行结果详见如下章节。

![开发板与电脑连接](media/6bb2bca69cee76f3586799191dd2cc87.jpeg)

**请求POST**

-   **示例代码**

import request 

import ujson  

url = "http://httpbin.org/post" 

data = {"key1": "value1", "key2": "value2", "key3": "value3"}  

**POST请求** 

response = request.post(url, data=ujson.dumps(data)) 

print(response.text) 


-   **代码运行结果**

![](media/ca55e37f24bee44fa77138e1083be1d1.png)

**请求GET**

-   **示例代码**

import request  

url = "http://httpbin.org/get"  

**GET请求**

response = request.get(url) 

print(response.text)


-   **代码运行结果**

![](media/ac0ebee2450a2170f52aeeb36f06ef03.png)

**请求PUT**

-   **示例代码**

import request 

url = "http://httpbin.org/put"  

**PUT请求** 

response = request.put(url) 

print(response.text)


![](media/2f3227680733adae0aa17b3b6518adb9.png)

**请求**PATCH

-   **示例代码**

import request  

url = "http://httpbin.org/patch"  

**PATCH请求** 

response = request.patch(url) 

print(response.text)

-   **代码运行结果**

![](media/480312d532ba119833ca7a16b897e409.png)

**请求DELETE**

-   **示例代码**

import request 

url = "http://httpbin.org/delete"  

**DELETE请求** 

response = request.delete(url) 

print(response.text)


-   **代码运行结果**

![](media/e3245758512d024f27619fd8e359d53c.png)

**请求HTTP连接**

-   **示例代码**

import request 

url = "https://myssl.com" 

**HTTPS请求** 

response = request.get(url) 

print(response.text)


-   **代码运行结果**

![](media/fbea842752b5a5006c5a5cdac1632304.png)

#### 附录A术语缩写

表1：术语缩写

| **缩写** | **英文全称**                      | **中文全称**     |
| -------- | --------------------------------- | ---------------- |
| API      | Application Programming Interface | 应用程序编程接口 |
| HTTP     | Hyper Text Transfer Protocol      | 超文本传输协议   |
| SDK      | Software Development Kit          | 软件开发工具包   |
| TCP      | Transmission Control Protocol     | 传输控制协议     |
| URL      | Uniform Resource Locator,         | 统一资源定位符   |
| WWW      | World Wide Web                    | 万维网           |

### Socket应用 开发指导

#### Socket概述

#### Socket简介

​		所谓Socket（套接字），就是对网络中不同主机上的应用进程之间进行双向通信的端点的抽象。一个Socket就是网络上进程通信的一端，提供了应用层进程利用网络协议交换数据的机制。从所处的地位来讲，Socket上联应用进程，下联网络协议栈，是应用程序通过网络协议进行通信的接口，是应用程序与网络协议根进行交互的接口。

​		Socket可以看成是两个网络应用程序进行通信时，各自通信连接中的端点，这是一个逻辑上的概念。它是网络环境中进程间通信的API（应用程序编程接口），也是可以被命名和寻址的通信端点，使用中的每一个Socket都有其类型和一个与之相连进程。通信时其中一个网络应用程序将要传输的一段信息写入它所在主机的Socket中，该Socket通过与网络接口卡（NIC）相连的传输介质将这段信息送到另外一台主机的Socket中，使对方能够接收到这段信息。Socket是由IP地址和端口结合的，提供向应用层进程传送数据包的机制。

**Socket的应用**

​		Socket可以使一个应用从网络中读取和写入数据，不同计算机上的两个应用可以通过连接发送和接受字节流，注意，当发送消息时，需要知道对方的IP和端口。在日常生活中有很多应用场景，当你浏览网页时，浏览器进程怎么与web服务器进程通信；当你用QQ聊天时，QQ进程怎么与服务器或好友所在的QQ进程通信，这些都是通过socket来实现的。

#### QuecPython Socket API详解

​		Socket起源于Unix，而Unix/Linux基本哲学之一就是“一切皆文件”，都可以用“打开（open）→
读写（write/read）→关闭（close）”模式来操作。在实现过程中服务端可以看作是web服务器，客户端可以看作是要访问web服务器的浏览器，访问过程就可以和打开→读写→关闭一一对应。

​		QuecPython类库中通过usocket实现Socket功能，usocket 模块提供对BSD套接字接口的访问。该模块实现相应CPython模块的子集，更多信息请参阅CPython文档：socket。其中usocket对Socket功能的具体流程及实现的相关API介绍如下。

**usocket.socket**

​		该函数用于服务端或客户端创建一个Socket对象。

函数原型

```
sock=usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
```

参数

usocket.AF_INET：
网络协议，IPv

usocket.SOCK_STREAM：
对应TCP的流式Socket。更多常量定义详见Quectel QuecPython 类库API说明。

返回值

无。

**usock.getaddrinfo**

​		该函数用于将主机域名（host）和端口（port）转换为用于创建套接字的 5 元组序列，元组结构如下：
(family, type, proto, canonname, sockaddr)

函数原型

```
usocket.getaddrinfo(host, port)
```

参数

host：
主机域名。

port：
端口。

返回值

无。



**sock.bind**

​		该函数用于将Socket对象和服务端IP：端口绑定。由于TCP口是动态的，客户端无需进行绑定。使用该函数之前，Socket必须未进行绑定。

函数原型

```
sock.bind(address)
```

参数

address：
由地址端口号组成的列表或者元组。

返回值

无。



**sock.listen**

​		该函数允许服务端接受Socket连接，可指定最大连接数。

函数原型

```
sock.listen(backlog)
```

参数

backlog：
接受的最大Socket连接数，至少为 0 。

返回值

无。



**sock.accept**

​		该函数用于服务端接受客户端连接请求。

函数原型

```
(conn, addres) = sock.accept()
```

参数

无。

返回值

返回元组，包含新的Socket和客户端地址，形式为：(conn, address)。

conn：
新的Socket对象，用来发送和接收数据。

address：
连接到服务器的客户端地址。



**sock.connect**

​		客户端使用该函数连接到指定地址的服务器。

函数原型

```
sock.connect(address)
```

参数

address：
连接到客户端的服务端地址。

返回值

无。



**2.3.7. sock.recv**

​		该函数用于接受客户端或服务端发送的数据。

函数原型

```
recv_data = sock.recv(bufsize)
```

参数

bufsize：
一次接收的最大数据量。

返回值

返回值是一个字节对象，表示接收到的数据。



**sock.send**

​		该函数用于发送数据到服务端或客户端。

函数原型

```
sock.send(send_data.encode("utf8"))
```

参数

send_data：
表示要发送的数据。

返回值

返回实际发送的字节数。

备注

​		TCP协议的Socket是基于字节流的，通过Socket发送数据之前，需先使用encode("utf8")对数据进行编码，其中"utf8"为编码方式。



**sock.close**

​		该函数用于关闭Socket通信。

函数原型

```
sock.close()
```

参数

无。

返回值

无。



**sock.read**

​		该函数用于从Socket中读取size字节数据，如果没有指定size，则会从套接字读取所有可读数据，直到读取到数据结束。

函数原型

```
socket.read([ size ])
```

参数

[ size ]：
要读取的字节数。

返回值

字节对象。



**sock.readinto**

​		该函数用于将字节读取到缓冲区中。

函数原型

```
sock.readinto(buf [ , nbytes ])
```

参数

buf：
存放读取字节的缓冲区。

nbytes：
读取的字节数。

返回值

实际读取的字节数。



**sock.readline**

​		该函数用于按行读取数据，遇到换行符结束。

函数原型

```
sock.readline()
```

参数

无。

返回值

返回读取的数据行。



**sock.write**

​		该函数用于向缓存区写入数据。

函数原型

```
sock.write(buf)
```

参数

buf：
写入缓冲区的数据。

返回值

返回实际写入的字节数。



**sock.sendall**

​		该函数用于将所有数据都发送到Socket。

函数原型

```
sock.sendall(bytes)
```

参数

bytes：
缓存buffer，存放bytes型数据。

返回值

无。



**sock.sendto**

​		该函数用于将数据发送到Socket。该Socket不应连接到远程Socket，因为目标Socket是由address指定的。

函数原型

```
sock.sendto(bytes, address)
```

参数

bytes：
缓存buffer，存放bytes型数据。

address：

包含地址和端口号的元组或列表。

返回值

无。



**sock.recvfrom**

​		该函数用于从Socket接收数据。返回一个元组，包含字节对象和地址。

函数原型

```
socket.recvfrom(bufsize)
```

参数

bufsize：
接收的缓存数据。

返回值

返回一个元组，包含字节对象和地址，形式为：(bytes, address)。

bytes：
接收数据的字节对象。

address：

发送数据的Socket的地址。



**sock.setsockopt**

​		该函数用于设置socket选项的值。

函数原型

```
socket.setsockopt(level, optname, value)
```

参数

level：
socket选项级别。

optname：
socket选项。

value：
既可以是一个整数，也可以是一个表示缓冲区的bytes类对象。

返回值

无。



**sock.setblocking**

​		该函数用于设置Socket为阻塞模式或者非阻塞模式。如果flag为false，则将Socket设置为非阻塞模式，否则设置为阻塞模式。

函数原型

```
socket.setblocking(flag)
```

参数

flag：
Ture 阻塞模式
False 非阻塞模式

返回值

无。



**sock.settimeout**

​		该函数用于设置Socket的超时时间，单位：秒。

函数原型

```
socket.settimeout(value)
```

参数

value：
		可以是秒的非负浮点数，也可以是None。如果将其设置为一个非零值，OSError在该操作完成之前已超过超时时间值，则随后的Socket操作将引发异常；如果将其设置为零，则将Socket置于非阻塞模式。如果未指定该值，则Socket将处于阻塞模式。

返回值

无。



**Socket.makefile**

​		该函数用于生成一个文件与socket对象关联，之后即可像读取普通文件一样使用socket。（普通文件的操作有open和write等。）

函数原型

```
socket.makefile(mode='rb')、
```

参数

mode：
二进制模式（rb和wb）。

返回值

返回与套接字关联的文件对象。



#### Socket功能实现

​		为了使用户更清楚的了解Socket功能，本章节提供了一个在QuecPython上创建Socket的实例，即模拟浏览器访问web服务器获取网页内容。首先在Xshell中，连接模块主串口，进入交互界面，然后按如下步骤实现Socket功能：

1. 导入usocket模块，创建一个Socket实例：

   ```
   import usocket
   sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
   ```

   ![](media/图1.jpg)

2. 解析域名

   ```
   sockaddr=usocket.getaddrinfo('www.tongxinmao.com',80)[0][-1]
   ```

   ​	将主机域名（host）和端口（port）转换为用于创建Socket的 5 元组序列，元组结构如下：

(family, type, proto, canonname, sockaddr)

![](media/图2.jpg)

3. 建立与服务端的连接：

   ```
   sock.connect(sockaddr)
   ```

![](media/图3.jpg)

4. 向服务端发送消息：

   ```
   ret=sock.send('GET  /News  HTTP/1.1\r\nHost:  www.tongxinmao.com\r\nAccept-Encoding:deflate\r\nConnection: keep-alive\r\n\r\n')
   print('send %d bytes' % ret)
   ```

   ![](media/图4.jpg)

5. 接收服务端的消息：

   ```
   data=sock.recv(1024)
   print('recv %s bytes:' % len(data))
   print(data.decode())
   ```

   ![](media/图5.jpg)

   ​		服务端消息接收完成后，可在浏览器上发起请求，验证返回消息是否与Socket接收的消息一致，如下所示：

   ![](media/图6.jpg)

6. 关闭连接：

   ```
   sock.close()
   ```

   ![](media/图7.jpg)

   ​		以上部分代码可见于移远通信提供的SDK工具包中，路径为moudles/socket/example_socket.py，也可通过example模块来执行该脚本文件。

   

   usocket服务端功能实现代码如下图：

```
#导入usocket模块
import usocket

#创建一个socket实例
sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
#设置端口复用
sock.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)

sock.bind(('127.0.0.1', 6000))

sock.listen(50)

sock.close()

while True:
	newSock, addr = sock.accept()
	newSock.send('hello world')
	recv_data = newSock.recv(256)
	print(recv_data.decode())
	newSock.close()
	break
```



​	usocket-API说明文档，详见qpy.quectel.com/wiki/#/zh-cn/api/。



#### 附录

表 1 ：术语缩写

```
术语 				英文全称 						中文全称

API 	Application Programming Interface 	应用程序编程接口

BSD 	Berkeley Socket Berkeley			套接字

HTTP 	Hypertext Transfer Protocol 		超文本传输协议

IPv4 	Internet Protocol version 4 		第 4 版互联网协议

NIC 	Network Interface Controller 		网络接口控制器

SDK 	Software Development Kit 			软件开发工具包

TCP 	Transmission Control Protocol 		传输控制协议^
```




## 系统

### 文件读写 使用说明

#### 文件基本概念 

文件将数据保存并存储在某种长期存储设备上,存储设备主要包括硬盘 、U 盘 、移动硬盘、光盘等。 

**文件存储方式**

文件主要以二进制及文本的方式进行储存。

1. 文本文件 , 例如 Python 的 源程序 :

- 可以使用文本编辑软件查看 ； 

- 本质上还是二进制文件 。 

2. 二进制文件 ，例如图片文件、音频文件、视频文件：

- 保存的内容无法直接阅读 ，而是提供给其他软件使用的 ； 
- 二进制文件不能使用文本编辑软件查看 。 

**文件的基本操作**

文件操作类型

- 打开文件 
- 读、写文件 
  - 读 ： 将文件内容读入内存 
  - 写 ： 将内存内容写入文件
- 关闭文件 

文件访问方式

表 **1**： 文件访问方式

| 访问方式 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| r        | 以只读方式打开文件。文件的指针将会放在文件的开头，为默认模式。如果文件不存在，抛出异常 。 |
| w        | 以只写方式打开文件。如果文件存在会被覆盖；如果文件不存在，创建新文件。 |
| a        | 以读写方式打开文件。如果该文件已存在，文件指针将会放在文件的结尾。如果文件不存在，创建新文件进行写入。 |

**备注** :若频繁移动文件指针，会影响文件的读写效率。通常，在开发过程中会以只读、只写的方式来操作文件。

**文件操作函数**

表 **2**： 文件操作函数

| 函数  | 说明                           | 方法                           |
| ----- | ------------------------------ | ------------------------------ |
| Open  | 打开文件，并且返回文件操作对象 | 负责打开文件，并且返回文件对象 |
| Read  | 将文件内容读取到内存           | 需要通过文件对象来调用         |
| Write | 将指定内容写入文件             | 需要通过文件对象来调用         |
| Close | 关闭文件                       | 需要通过文件对象来调用         |



#### 操作文件及目录 

将 EC100Y-CN QuecPython 开发板 连接至电脑，接入后的操作方法详见《 Quectel_QuecPython_基础 操作说明 》。 

![Quectel_QuecPython_文件读写_029.png](media/Quectel_QuecPython_文件读写_029.png)

​												图 **1**： **EC100Y-CN QuecPython** 开发板与电脑连接

**以只读方式打开文件**

步骤一 ： 创建 *test.py*、*test.txt* 文件， 并 在 *test.py* 文件中导入 QuecPython 中的 *uio* 模块，在 *test.txt* 文件输入 "hello python"。 

- 在 t*est.py* 文件中导入 QuecPython 中的 *uio* 模块 ： 

```python
import uio

# 以只读方式打开 test.txt 文件 
fd = uio.open("test.txt", mode='r') 

# 读取文件内容
text = fd.read() 
print(text)

# 关闭文件
fd.close() 
```

- 在 *test.txt* 文件输入 "hello python"： 

![Quectel_QuecPython_文件读写_032.png](media/Quectel_QuecPython_文件读写_032.png)

​													图 **2**： 在 **test.txt** 文件输入 **"hello python"** 

步骤 二 ： 将 *test.py* 文件和 *test.txt* 文件分别上传到 EC100Y-CN QuecPython 开发板内，上传方法详见《Quectel_QuecPython_基础操作说明》 。 

步骤 三 ： 读取文件 运行结果 

![Quectel_QuecPython_文件读写_033.png](media/Quectel_QuecPython_文件读写_033.png)

​													 		图 **3**： 读取 文件运行结果

**以只写方式打开文件**

步骤一 ： 创建 *test.py* 文件及 内容 为空白的 *test.txt* 文件，在 *test.py* 文件中导入 QuecPython 中的 uio 模

块， 并 编写如下代码 ： 

```python
import uio 

# 以只写方式打开 test.txt 文件 
fd = uio.open("test.txt", mode=‘w') 
              
# 向文件写内容
fd.write("HELLO PYTHON")
              
# 关闭文件 
fd.close() 
```

步骤 二 ： 将 *test.py* 文件和 *test.txt* 文件分别上传到 EC100Y-CN QuecPython 开发板内，上传方法详见《Quectel_QuecPython_基础操作说明》。

步骤 三 ： 写入文件运行结果 

![Quectel_QuecPython_文件读写_035.png](media/Quectel_QuecPython_文件读写_035.png)

​															图 **4**： 写入 文件运行结果

**使用 uos 模块**

1. 列出当前文件列表 

![Quectel_QuecPython_文件读写_036.png](media/Quectel_QuecPython_文件读写_036.png)

​															图 **5**： 列出 当前文件列表

2. 新建目录 

![Quectel_QuecPython_文件读写_037.png](media/Quectel_QuecPython_文件读写_037.png)

​																		图 **6**： 新建目录

3. 删除目录 

![Quectel_QuecPython_文件读写_038.png](media/Quectel_QuecPython_文件读写_038.png)

​																		图 **7**： 删除目录 

**备注**: apn_cfg.json 为默认脚本文件。 



#### 附录术语缩写 

表 **3**： 术语缩写

| 缩写 | 英文全称                          | 中文全称         |
| ---- | --------------------------------- | ---------------- |
| SDK  | Software Development Kit          | 软件开发工具包   |
| API  | Application Programming Interface | 应用程序编程接口 |




### 多线程 应用开发指导

#### 多线程/进程的基本概念 

Python 运行在 Python 虚拟机中，用户创建的多线程只是在 Python
虚拟机中的虚拟线程，而非在操作系统中的真正的线程。也就是说，Python
中的多线程是由 Python 虚拟机来进行轮询调度，而不是操作系统。

多线程可以使同一程序同时执行多个任务。线程在执行过程中与进程存在区别，在每个独立的线程中，都分别存在程序运行的入口、顺序执行序列以及程序的出口。并且线程必须依附在某个程序中，由程序来控制多个线程的运行。

**线程的基本操作** 

>   线程具有 5 种状态，状态转换的过程如下：

![5b584fb5c2b36cb7e057ae95d87b295e](media/5b584fb5c2b36cb7e057ae95d87b295e.png)

>   图 **1**：线程的 **5** 种状态

**线程和进程的主要区别** 

线程和进程都是操作系统控制程序运行的基本单位，系统可以利用这两个特性对程序实现高并发。而线程和进程的主要区别如下：

1.  一个程序至少有一个进程；一个进程中至少包含一个线程。

2.  进程在内存中拥有独立的存储空间，而多个线程则共享它所依赖的进程的存储空间。

3.  进程和线程对操作系统的资源管理的方式不同。

#### 多线程 **API** 详解 

**_thread.allocate_lock** 

>   该函数用于创建一个互斥锁对象。

- 函数原型

  _thread.allocate_lock()

- 参数

  无

  返回值

  返回互斥锁对象。互斥锁对象的函数详见第**3.1.1**章。

**互斥锁对象函数** 

**lock.acquire** 

>   该方法用于获取锁。

- 函数原型

  lock.acquire()

- 参数

  无

- 返回值

True 成功

>   False 失败

**lock.release** 

>   该方法用于释放锁。

- 函数原型

  lock.release()

- 参数

  无

- 返回值

  无

**lock.locked** 

>   该方法用于返回锁的状态。

- 函数原型

  lock.locked()

- 参数

  无

- 返回值

True 表示被某个线程获取

>   False 表示没有被线程获取

**_thread.get_ident** 

>   该方法用于获取当前线程号。

- 函数原型

  _thread.get_ident()

- 参数

  无

- 返回值

  返回当前线程号。

**_thread.stack_size** 

>   该方法用于设置创建新线程使用的堆栈大小。单位：字节。

- 函数原型

  _thread.stack_size(size)

- 参数

  *size*：堆栈大小。默认值：8192。

- 返回值

  返回当前堆栈大小。

**_thread.start_new_thread** 

>   该方法用于创建一个新线程。

- 函数原型

  _thread.start_new_thread(function, args)

- 参数

  *function*：

  接收执行函数

  *args*：

  被执行函数参数

- 返回值

  无

#### 多线程使用示例 

>   步骤**1**：
>   将开发板接入电脑。接入后的操作方法详见《Quectel_QuecPython_基础操作说明》。

>   ![](media/782cd2c870c62e6f022cca4e47c7c806.jpg)

>   图 **2**：开发板接入电脑

>   步骤**2**： 创建 *test.py* 文件，在文件内导入 QuecPython 中的_thread
>   模块，编写多线程代码。

```
import _thread

def th_func(thread_id):

	Print("thread id is:%d" % thread_id)

for i in range(5):

	_thread.start_new_thread(th_func,(i+1,))
```



>   步骤**3**： 将 test.py
>   文件上传到开发板，上传方法详见《Quectel_QuecPython_基础操作说明》。

>   步骤**4**： 程序运行结果，如图所示：

![](media/e2d4afc1ebb0f7d9ad420489f74da40d.jpg)

#### 附录参考文档 

>   表 **1**：参考文档

| 序号 | 文档名称                         | 备注                        |
| ---- | -------------------------------- | --------------------------- |
| [1]  | Quectel_QuecPython_基础操作说明 | QuecPython 上传下载文件说明 |




### 总线 使用指导

#### ADC 数模 转换 

​		数字信号和模拟信号转换器 ADC，称为数模转换器， CPU 本身是数字的，但是外 部的一些变量是模拟 的，所以需要利用数字技术处理外部模拟的物理量。 模拟信号，是一个连续的信号，现实生活中的时间，电 压，高度等就是模拟信号，反应在数学里就是无限细分的值。

​		数模转换就是把模拟信号按照一定精度进行采样，变成有限多个数字量，这个过程就是数模转换，数字 化之后就可以在计算机中用数字来描述模拟量，是计算机技术的基础，计算机所有参与运算的都是数字量， 如果参与计算的有模拟量，就需要使用数模转换器将模拟量转换为数字量来参与运算，同样，也 可以通过使 用有积分和微分效果的器件来将数字信号转换为模拟信号。

QuecPython 开发板中ADC输入引脚如下图所示 。 

![Quectel_QuecPython_总线用户指导_015.png](media/Quectel_QuecPython_总线用户指导_015.png)

​																		图 **1**： **ADC** 输入 引脚

将 GPIO1 串口和 ADC 串口连接 ， 在 QuecPython 中通过 *misc* 模块 ADC 类读取通道电压值 ，通过 *machine* 模块 *Pin* 类中 *Pin.write(value)*方法设置 PIN 脚电平，详细使用方法和 API 接口说明见 《Quectel_QuecPython_类库 API 说明 》。 

```python
from machine import Pin 
from misc import ADC 
adc = ADC 
adc.open() 

gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0) 
gpio1.read()# 获取 gpio 的当前高低状态
gpio1.write(1) # 设置 gpio1 输出高 
adc.read(ADC.ADC0) 
gpio1.write(0) # 设置 gpio1 输出 低 
adc.read(ADC.ADC0) 
```

命令行运行结果可见 ADC通道电压变为 1.8 V，如 图所示： 

![Quectel_QuecPython_总线用户指导_019.png](media/Quectel_QuecPython_总线用户指导_019.png)

​																图 **2**： **ADC** 通道 电压变化 

#### UART

​		UART 是一种串行异步收发协议，应用十分广泛。 UART 工作原理是将数据的二进制位一位一位的进行

传输。在 UART 通讯协议中信号线上的状态位高电平代表 *1*，低电平代表 *0*。当然两个设备使用 UART 串 口通讯时，必须先约定好传输速率和一些数据位。

硬件连接比较简单，仅需要 3 条线，注意连接时若两个设备UART电平范围不一致请做电平转换后再 连接 。 

- TX：发送数据端，要接对面设备的 RX； 
- RX：接收数据端，要接对面设备的 TX； 
- GND：保证两设备共地，有统一的参考平面 。 

![Quectel_QuecPython_总线用户指导_.020.png](media/Quectel_QuecPython_总线用户指导_.020.png)

​																	图 **3**： **UART** 硬件连接 

在 EC100Y-CN 模块 上使用 UART 串口传输 数据时，需将发送数据端 TX 与 对面的 RX 相连 ，将接受数 据端 RX 与 对面的 TX 相连 ，在 QuecPython 中 通过 machine 模块 UART 类 可以实现串口数据传输功能 ， 详细使用方法和 API 接口说明见 《Quectel_QuecPython_类库 API 说明 》。 

![Quectel_QuecPython_总线用户指导_021.png](media/Quectel_QuecPython_总线用户指导_021.png)

​																	图 **4**： **UART API** 示例代码 

#### SPI通信 

SPI 协议是串行外围设备接口，是一种高速全双工的通信总线 。SPI 总线包含 4 条总线，分别为 SS、 SCK、MOSI、MISO。

（1）SS：片选信号线，当有多个 SPI 设备与 MCU 相连时，每个设备的这个片选信号线是与 MCU 单 独的引脚相连的，而其他的 SCK、MOSI、MISO 线则为多个设备并联到相同的 SPI 总线上，低电平有效。

（2）SCK：时钟信号线，由主通信设备产生。 不同的设备支持的时钟频率不一样，如 STM32 的 SPI 时钟频率最大为 f PCLK / 2。 

（3）MOSI：主设备输出 /  从设备输入引脚。主机的数据从这条信号线输出，从机由这条信号线读入 数据，即这条线上数据的方向为主机到从机。

（4）MISO：主设备输入 /  从设备输出引脚。主机从这条信号线读入数据，从机的数据则由这条信号 线输出，即在这条线上数据的方向为从机到主机。

![Quectel_QuecPython_总线用户指导_.022.png](media/Quectel_QuecPython_总线用户指导_.022.png)



​																图 **5**： **SPI** 硬件连接

#### I2C通信 

I2C 接口只有两根线， SCL 和 SDA： 

- SCL： 传输时钟信号，由主设备向从设备传输时钟信号。

- SDA： 传输数据信号，主从设备之间相互传递数据的通道 。 

I2C 属于串行通信，数据以 bit 为单位在 SDA 线上串行依次传输，同步工作状态，主从设备工作在同一 个时钟频率下，通过 SCL 线同步时钟， I2C 传输电平信号，不需要很高的速度，通信双方距离很近，所以 不需要差分信号来抗干扰， I2C 通常用在同一块板子上的两个 IC 之间的通信，数据量不大且速度较低。

![Quectel_QuecPython_总线用户指导_025.png](media/Quectel_QuecPython_总线用户指导_025.png)

​																		图 **6**： **I2C** 硬件连接

以下数据以 I2C 连接 光照传感器为例 。 

![Quectel_QuecPython_总线用户指导_026.png](media/Quectel_QuecPython_总线用户指导_026.png)

![Quectel_QuecPython_总线用户指导_027.png](media/Quectel_QuecPython_总线用户指导_027.png)

​																图 **7**： **I2C** 连接 光照传感器

#### 附录 术语缩写 

表 **1**： 术语缩写 

| ADC  | Analog-to-Digital Converter                 | 模数转换器             |
| ---- | ------------------------------------------- | ---------------------- |
| API  | Application Programming Interface           | 应用程序编程接口       |
| CPU  | Central Processing Unit                     | 中央处理器             |
| UART | Universal Asynchronous Receiver/Transmitter | 通用异步收发传输器     |
| GND  | Ground                                      | 地                     |
| IC   | Integrated Circuit                          | 集成电路               |
| I2C  | Inter-Integrated Circuit                    | 双向二线制同步串行总线 |
| LCD  | Liquid Crystal Display                      | 液晶显示屏             |
| MCU  | Microprogrammed Control Unit                | 微程序控制器           |
| MISO | Master In Slave Out                         | 主机输入从机输出       |
| MOSI | Master Out Slave In                         | 主机输出从机输入       |
| RX   | Receive                                     | 接收                   |
| TX   | Transmit                                    | 发送                   |
| SCK  | Serial Clock                                | 时钟信号线             |
| SCL  | Serial Clock Line                           | 串行 时钟线            |
| SDA  | Serial Data Line                            | 串行 数据线            |
| SPI  | Serial Peripheral Interface                 | 串行外设接口           |
| SS   | Slave Select                                | 片选信号线             |


### LED 使用指导

#### 基本概述

在使用LED功能之前，需要先了解开发板的GPIO串口，GPIO即通用I/O端口。GPIO即开发板的引脚输出输入功能。输出功能，即控制引脚变高和变低；输入功能，即检测引脚上的电平是高电平还是低电平。当需要控制引脚为高电平或低电平时，即使用GPIO的输出功能使用。例如，控制LED灯的亮灭时，需要通过控制输出的高低电平来实现LED灯的亮灭。

以EC100Y-CN模块为例，如图所示为GPIO串口：

![](media/LED图0_gpio.jpg)

​																				图 1 ：GPIO串口


#### LED功能实现

​     	在开发板中实现LED功能需要用到QuecPython中的Pin类功能，以EC100Y-CN模块为例，将模块
的LED控制线与开发板的GPIO1串口相连，再将模块V3.3串口与开发板的V3.3串口相连，为模块供电。连接完成后给开发板上电。

步骤 1 ： 首先导入machine模块，创建GPIO对象。代码示例如下：

```
from machine import Pin
gpio1 = Pin(GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
```



GPIOn 				整型。引脚号。
							引脚对应关系如下：
							GPIO 1 – 引脚号 22
							GPIO2–引脚号 23
							GPIO3–引脚号 178
							GPIO4–引脚号 199
							GPIO5–引脚号 204

direction 			整型。
							IN 输入模式
							OUT 输出模式

pullMode 			整型。
								PULL_DISABLE 浮空模式
								PULL_PU 上拉模式
								PULL_PD 下拉模式

level 整型。		引脚电平。
								0 设置引脚为低电平
								1 设置引脚为高电平

步骤 2 ： 获取引脚电压，执行代码如下：

```
gpio1.read()
```

步骤 3 ： 设置引脚电平。执行代码如下：

```
gpio1.write(1)
```



步骤 4 ： 通过给引脚设置一串变化的电压来实现LED灯的闪烁效果。执行代码如下：

```
import utime
i = 1

while i<100：
	gpio1.write(0)
	utime.sleep(1)
	gpio1.write(1)
	utime.sleep(1)
	i += 1
```

![](media/LED图1.jpg)

![](media/LED图2.jpg)

​	运行以上代码后即可观察到EC100Y-CN模块的LED灯每隔 1 秒闪烁，并且可通过修改代码和连接多

组外设实现更多功能。

![](media/LED图3.jpg)

​																			图 2 ：LED灯闪烁

备注

```
以上部分代码可见于移远通信提供的SDK工具包中，路径为modules/gpio/example_pin.py。
```

#### 附录

表 1 ：术语缩写

```
缩写 		英文全称 							中文全称

GPIO 	General-Purpose Input/Output 		通用型输入/输出

LED 	Light Emitting Diode 				发光二极管

SDK 	Software Development Kit 			软件开发工具包
```



### 定时器 使用指导

#### 定时器功能 

**定时器基本功能** 

定时器可用于多种任务。目前，仅实现了最简单的情况，即定时调用函数，当前移远通信提供的定时器可实现单次和周期性调用函数两种模式。当到达定时器周期时，会触发事件。通过使用回调函数，定时器事件可调用一个Python 函数。

**定时器功能示例** 

将开发板接入电脑，之后，参考《Quectel_QuecPython_基础操作说明》文档进行操作，下面以
EC100Y-CN 模块为例进行说明。

![](media/782cd2c870c62e6f022cca4e47c7c806.jpg)

>   图 **1**：模块接入电脑

>   创建 test.py 文件，在文件内导入 QuecPython 中的 Timer 类，Timer 类在 Machine
>   模块中。编写定时器代码，如下所示：

```
from machine import Timer

def func(args):

	print('###timer callback function###')

	timer = Timer(Timer.Timer1)

	timer.start(period=1000, mode=timer.PERIODIC, callback=func)
```



>   将 test.py
>   文件上传到开发板内，上传方法详见《Quectel_QuecPython_基础操作说明》。

>   程序运行结果，如下所示：

```
>>> import example

>>> example.exec('test.py')

>>> ###timer callback function###

	###timer callback function###

	###timer callback function###

	###timer callback function###

	###timer callback function###

	###timer callback function###

	###timer callback function### 
	
	###timer callback function###
	
timer.stop() 0

>>>
```



#### **QuecPython** 中的定时器 

**Timer 类中的常量** 

| 常量           | 说明                       |
| -------------- | -------------------------- |
| Timer.Timer0   | 定时器 0                   |
| Timer.Timer1   | 定时器 1                   |
| Timer.Timer2   | 定时器 2                   |
| Timer.Timer3   | 定时器 3                   |
| Timer.ONE_SHOT | 单次模式，定时器只执行一次 |
| Timer.PERIODIC | 周期模式，定时器循环执行   |

#### Timer 类中的方法 

**timer = Timer** 

>   该函数用于创建一个 timer 对象。使用定时器相关函数 *timer.start* 和
>   *timer.stop* 之前，需先使用该函数

>   实例化对象，即创建 Timer 对象。

- 函数原型

  timer = Timer(Timern)

- 参数

  *Timern*：常量。定时器号。EC100Y-CN 和 EC600S-CN
  模块支持的定时器为：Timer0~Timer3。 ⚫ 返回值

  返回 timer 对象。

**timer.start** 

>   该函数用于启动定时器。

- 函数原型

  timer.start(period, mode, callback)

- 参数

  *period*：整型。中断周期，单位：毫秒。

  *mode*：

  常量。定时器运行模式，如下：

  Timer.ONE_SHOT 单次模式，定时器只执行一次

  Timer.PERIODIC 周期模式，循环执行

  *callback*： 回调函数，定时执行的函数。

- 返回值

  0 定时器启动成功。 -1 定时器启动失败。

**timer.stop** 

>   该函数用于关闭定时器。

- 函数原型

  timer.stop()

- 参数

  无。

- 返回值

  0 定时器关闭成功。 -1 定时器关闭失败。


#### 附录 

>   表 **1**：术语缩写

| 术语 | 英文全称                          | 中文全称         |
| ---- | --------------------------------- | ---------------- |
| API  | Application Programming Interface | 应用程序编程接口 |




## 应用

### GPS 使用指导

#### GPS概述

利用GPS定位卫星，在全球范围内实时进行[定位](https://baike.baidu.com/item/%E5%AE%9A%E4%BD%8D)、[导航](https://baike.baidu.com/item/%E5%AF%BC%E8%88%AA)的系统，称为全球卫星定位系统，简称GPS。NEMA-0183，是[GPS接收机](https://baike.baidu.com/item/GPS%E6%8E%A5%E6%94%B6%E6%9C%BA/3475821)应当遵守的标准协议，也是目前[GPS](https://baike.baidu.com/item/GPS/214654)接收机上使用最广泛的协议，大多数常见的GPS接收机、GPS数据处理软件、[导航软件](https://baike.baidu.com/item/%E5%AF%BC%E8%88%AA%E8%BD%AF%E4%BB%B6/1401586)都遵守或者至少兼容这个协议。GPS现已被广泛应用于[交通](https://baike.baidu.com/item/%E4%BA%A4%E9%80%9A/30183)、[测绘](https://baike.baidu.com/item/%E6%B5%8B%E7%BB%98/2271120)等许多行业。GPS的所有应用领域，都是基于定位、或从定位延伸出去的，主要包括：运动导航，轨迹记录、大地测量、周边信息查询等。

#### GPS模块使用流程

**准备工作**

**步骤1：**首先准备EC100Y-CN开发板和L80-R GPS模块，将L80-R GPS模块与开发板相连。注意使用时应处于室外环境以便于接收GPS信号。如下图所示：


![](media/1.png)

L80-R GPS模块功能如下图所示：


![](media/2.png)

**步骤2：**通过xshell工具连接开发板，进入交互页面，由上文模块功能图可知*GPS_EN*引脚对应的开发板上的串口为GPIO5，故通过GPIO5启动GPS功能。

​              执行代码如下：

![](media/3.png)

**步骤3：**执行完以上代码后，即可看到模块的GPS指示灯常亮，同理也可以通过设置GPIO1的电压来点亮LED灯。

#### 数据处理

**步骤1：**启用模块的GPS功能后，GPS数据会通过模块的GPS_TXD串口发送到开发板中，接下来通过EC100Y-CN QuecPython的machine模块UART串口的数据传输           功能将数据输出，代码如下图所示：

![](media/4.png)

machine模块的详细API接口说明请参考文档《Quectel QuecPython类库API说明》。



**步骤2：**然后，对接收的NMEA-0183协议定义的数据格式进行处理，这里需要处理的语句是$GNGGA。

​              例如： $GNGGA,092204.999,4250.5589,S,14718.5084,E,1,04,24.4,19.7,M,,,,0000*1F

字段0：$GPGGA，语句ID，表明该语句为Global Positioning System Fix Data（GPS定位信息）

字段1：UTC时间，hhmmss.sss，时分秒格式

字段2：纬度，ddmm.mmmm，度分格式（前导位数不足则补0）

字段3：纬度N（北纬）或S（南纬）

字段4：经度，dddmm.mmmm，度分格式（前导位数不足则补0）

字段5：经度E（东经）或W（西经）

字段6：GPS状态，0=未定位，1=非差分定位，2=差分定位，3=无效PPS，6=正在估算

字段7：正在使用的卫星数量（00~12）（前导位数不足则补0）

字段8：HDOP水平精度因子（0.5~99.9）

字段9：海拔高度（-9999.9~99999.9）

字段10：地球椭球面相对大地水准面的高度

字段11：差分时间（从最近一次接收到差分信号开始的秒数，如果不是差分定位将为空）

字段12：差分站ID号（0000~1023）（前导位数不足则补0，如果不是差分定位将为空）

字段13：校验值



**步骤3：**最后，运行以下代码获取GPS信息中的时间和经纬度，通过不断获取时间和经纬度可以实时追踪位置。

​              详细运行方法请参考文档《Quectel_QuecPython_基础操作说明》。



```
from machine import UART  
import utime  
import modem  
import _thread  
uart = UART(2,115200,8,0,1,0)  
def gngga():  
while True:  
#获取当前RTC时间  
time = utime.localtime( )  
#获取设备IMET  
imei = modem.getDevImei( )  
if uart.any() > 0:  
buf = uart.read(uart.any())  
buf = str(buf,"utf8" )  
try :  
gngga1 = buf.split("$GNGGA,")[1].split("\r\n" )[0].split(",")  
# UTC时间，hhmmss.sss,时分秒格式  
time_gps = gngga1[0]  
#纬度ddmm.mmmm,度分格式前导位数不足则补0  
_latitude = float(gngga1[1])  
#经度dddmm.mmmm,度分格式前导位数不足则补0  
_longitude = float(gngga1[3])  
# UTC时间转化  
_Clock = int(time[0:2])  
_Minute = time[2:4]  
_Second = time[4:6]  
_Clock =_Clock + 8  
#防止超过24小时  
if (_Clock >= 24):  
_Clock = _Clock % 24  
#最终获得时间  
Effect_time = str(_clock) + ':' +_Minute + ':' +_Second  
#最终获得纬度  
Effect_latitude = int(_latitude / 100)+ ((_latitude % 100) / 60)  
#最终获得经度  
Effect_longitude = int(_longitude / 100) +((_longitude % 100)/ 60)  
print( '当前时间:',time)  
print( 'GPS时间:',Effect_time)  
print('设备IMET',imei)  
print(gngga1[2],'',str(Effect_latitude ))  
print(gngga1[4],'',str(Effect_longitude ))  

utime.sleep(2)  
except:  
print('数据格式有误或数据受损')  
continue  
def run():  
_thread.start_new_thread(gngga, ())  

run()
```



#### 附录

表1：术语缩写

| **缩写** | **英文全称**                       | **中文全称**         |
| -------- | ---------------------------------- | -------------------- |
| API      | Application Programming Interface  | 应用程序编程接口     |
| GPS      | Global Positioning System          | 全球定位系统         |
| GPIO     | General-Purpose Input/Output       | 通用型输入/输出      |
| GGA      | Global Positioning System Fix Data | 全球定位系统定位数据 |
| HDOP     | Horizontal Dilution of Precision   | 水平精度因子         |
| LED      | Light Emitting Diode               | 发光二极管           |

### NTP 使用指导

####  概述

​		NTP又称网络时间协议，用于同步计算机时间的一种协议。该协议可以使计算机对其服务器或时钟源（如石英钟，GPS等等）进行同步，同时提供高精准度的时间校正（LAN上与标准时间差小于 1 毫秒，WAN上与标准时间差大约有几十毫秒），且可介由加密确认的方式来防止恶毒的协议攻击。NTP的目的是在无序的互联网环境中提供精确和健壮的时间服务。

​		NTP提供准确时间，首先要有准确的时间来源，即国际标准时间UTC。NTP获得UTC的时间来源可

以是原子钟、天文台、卫星，也可以从互联网上获取。时间按NTP服务器的等级传播，按照离外部UTC时间源的远近将所有服务器归入不同的Stratum（层）中。Stratum- 1 在顶层，有外部UTC接入；Stratum- 2从Stratum- 1 获取时间；Stratum- 3 从Stratum- 2 获取时间，......，以此类推，但Stratum的总数限制在 15以内。所有这些服务器在逻辑上形成阶梯式的架构相互连接，而Stratum- 1 的时间服务器是整个系统的基础。计算机主机一般同多个时间服务器连接，利用统计学的算法过滤来自不同服务器的时间，以选择最佳的路径和来源来校正主机时间，即使主机在长时间无法与某一时间服务器相联系的情况下，NTP服务依然有效运转。

​		为防止对时间服务器的恶意破坏，NTP使用了识别(Authentication)机制，检查来对时的信息是否是真正来自所宣称的服务器并检查资料的返回路径，以提供对抗干扰的保护机制。NTP时间同步报文中包含的时间是格林威治时间，是从 1900 年开始计算的秒数。

#### 功能实现

NTP对时需要从NTP服务器上获取时间，故在实现NTP对时功能之前需连接网络。本文档以通过SIM

卡进行联网为例。

1. 准备一张可用的Nano SIM卡，滑动打开开发板上SIM卡槽，放入SIM卡后合上卡槽盖子并通电，
   等待自动拨号。以EC100Y-CN为例，SIM卡槽位置如图所示：

   ![](media/图1.插入sim卡.jpg)

   ​															图 1 ：插入SIM卡

   自动拨号后，可通过如下方法验证是否拨号成功：

![](media/图2.自动拨号成功验证.jpg)

​															图 2 ：自动拨号成功验证

2. 拨号成功后，导入ntptime模块

   ```
   import ntptime
   ntptime.host
   ```

   

   返回当前的NTP服务器，默认为"ntp.aliyun.com"。

   ![](media/图3.当前ntp服务器.jpg)

   ​														图 3 ：当前NTP服务器

3. 设置NTP服务器。设置成功返回 0 ，设置失败返回- 1 。

   ```
   ntptime.sethost(host)
   ```

   ![](media/图4.设置ntp服务器.jpg)

   ​														图 4 ：设置NTP服务器

4. 同步NTP时间。同步成功返回 0 ，同步失败返回- 1 。

   ```
   ntptime.settime()
   ```

   ​		对时结果可使用utime.localtime()验证。执行utime.localtime()后返回当前时间，返回值为一个元组：(year, month, mday, hour, minute, second, weekday, yearday)。详细说明请参考《QuectelQuecPython类库API说明》。

   ​		ntptime.settime()对时后返回时间为UTC时间，北京时间领先UTC八个小时，所以对时后，对比当前时间可发现时间后退八小时。

   ![](media/图5.对时成功.jpg)

   ​																		图 5 ：对时成功



#### 附录术语缩写

表 1 ：术语缩写

```
术语 			英文描述 							中文描述

GPS 		Global Positioning System 			全球定位系统

LAN 		Local Area Network 					局域网

NTP 		Network Time Protocol				 网络时间协议

RTC 		Real_Time Clock 					实时时钟

SIM 		Subscriber Identity Module 			用户身份识别模块

UTC 		Coordinated Universal Time 			协调世界时

WAN 		Wide Area Network 					广域网
```



### Audio 使用指导 

#### 播放音频文件 

目前用户分区大小默认为 5 M，所以放入音频文件的大小不应该超过 5 M，同时还应预留足够的空间存 放用户的应用程序及其他文件。 本 章节主要介绍如何 上传 并播放 存放在用户 分区 根目录， 及存放在根目录 下某个 目录 中的 音频 文件。 

**将音频文件上传至用户分区的根目录**

步骤 **1**： 解压 SDK 压缩 包内 *tools* 目录 下的 *QPYcom.zip*， 获取 *QPYcom.exe*。

步骤 **2**： 使用 QPYcom.exe 将音频文件上传至模块中，具体上传方式详见《 Quectel_QuecPython_基

础操作说明 》。 

步骤 **3**：上传 音频文件至用户分区的根目录。 假设 音频文件名称为 *music.mp3*，在 音频文件所在目录下

打开 cmd， 执行如下命令： 

```python
QuecPyComTools.exe -d COM20 -b 115200 -f cp music.mp3 :/ 
```

- **说明** 

-d 后面 的参数 COM20 应为 实际 CDC 口。 

- **示例** 

![Quectel_QuecPython_音频文件播放_016.png](media/Quectel_QuecPython_音频文件播放_016.png)

步骤 **4**： 查看用户根目录下是否有 *music.mp3* 文件。 通过 Xshell 连接 模块的 CDC 口 ，进入命令交互

界面，执 行 如下 命令 ： 

```shell
>>> uos.listdir() 
```

- **说明** 

```shell
“ >>>” 表示这是在模块的命令交互行
```

- **示例** 

![Quectel_QuecPython_音频文件播放_018.png](media/Quectel_QuecPython_音频文件播放_018.png)

步骤 **5**：播放音频文件 。通过命令交互界面依次执行如下命令，即可播放。

```shell
>>> import audio           #导入音频播放库

>>> a = audio.Audio(1)      #创建一个音频对象， 此处 选择耳机通道，所以参数为 1 
>>> a.play(1, 0, 'U:/music.mp3')  # 设定优先级为 1，不可被打断，播放该音频文件
```



- **说明** 

创建一个音频对象， 此处 选择耳机通道，所以参数为 1，其他参数请参 《Quectel_QuecPython_ 类库 API 说明》 相关模块说明部分 。 

- **示例** 

![Quectel_QuecPython_音频文件播放_020.png](media/Quectel_QuecPython_音频文件播放_020.png)

**备注** : 用户分区盘符目前固定为 U，播放时必须为绝对路径，比如 U:/path/filename，如果直接放到根目录下， 则为 U:/filename。 

**将 音频文件上传至用户分区根目录 下 的audio目录**

步骤 **1**：在 用户分区根目录下创建 *audio* 目录。 通过命令交互界面执行如下命令。

```shell
>>> uos.mkdir('audio') 
```

- **示例** 

![Quectel_QuecPython_音频文件播放_023.png](media/Quectel_QuecPython_音频文件播放_023.png)

步骤 **2**： 断开 Xshell 与模块 CDC 口的连接 ， 否则 CDC 被 占用， 将 导致 *QPYcom.exe* 工具执 行失败 （若 使用的 是其它工具，请断开其它工具与 CDC 口的连接）

步骤 **3**：上传 音频文件至用户分区根目录 下 的 *audio* 目录 。假设 音频文件名称为 *music.mp3*，在 音频文

件所在目录下打开 cmd， 执行如下 命令： 

```shell
QuecPyComTools.exe -d COM20 -b 115200 -f cp music.mp3 :/audio/ 
```

- **说明** 

最后一个‘ **/**’不能缺失 。 

- **示例** 

![Quectel_QuecPython_音频文件播放_025.png](media/Quectel_QuecPython_音频文件播放_025.png)

步骤 **4**： 查看用户根目录 的 *audio* 目录 下是否有 *music.mp3* 文件。通过 Xshell 重新连接 模块的 CDC 

口 ，进入命令交互界面 ， 执行如下命令： 

```shell
>>> uos.listdir() 
>>> uos.listdir('audio') 
```

- **示例** 

![Quectel_QuecPython_音频文件播放_027.png](media/Quectel_QuecPython_音频文件播放_027.png)

步骤 **5**：播放音频文件 。 通过命令交互界面依次执行如下命令，即可播放。

```shell
>>> import audio           #导入音频播放库
>>> a = audio.Audio(1)      #创建一个音频对象， 此处 选择耳机通道，所以参数为 1 
>>> a.play(1, 0, ‘U:/audio/music.mp3’)  #设定优先级为 1，不可被打断，播放该音频文件
```

- **说明** 

创建一个音频对象，此处 选择耳机通道，所以参数为 1，其他参数请参 《Quectel_QuecPython_ 类库 API 说明》相关模块说明部分 。 

![Quectel_QuecPython_音频文件播放_029.png](media/Quectel_QuecPython_音频文件播放_029.png)

#### 删除音频文件 

本章节主要介绍如何删除 存放在用户分区根目录 ，及存放在根目录下某个目录中的音频文件。 

**删除用户分区的根目录 下 的音频文件**

步骤 **1**：通过 Xshell 或 其他同类工具连接到模块 CDC 口 。 

步骤 **2**：删除 音频文件。 进入 命令交互界面后，执行如下命令 ： 

```shell
>>> uos.remove('music.mp3')    #删除音频文件
>>> uos.listdir()           #查看删除结果，确认文件是否删除成功
```

- **示例** 

![Quectel_QuecPython_音频文件播放_031.png](media/Quectel_QuecPython_音频文件播放_031.png)

​				此时用户分区根目录下的音频 文件 已被删除。

**删除用户分区根目录 下的某个 目录下的音频文件**

步骤 **1**：通过 Xshell 或 其他同类工具连接到模块 CDC 口 。 

步骤 **2**：删除 音频文件。 进入 命令交互界面后，执行如下命令 ： 

```shell
>>> uos.remove('audio/music.mp3')  #删除音频文件
>>> uos.listdir('audio')        #查看删除结果，确认文件是否删除成功
```



#### 批量打包音频文件至用户分区 

实际应用 中，用户可能 提前将音频文件打包到用户分区中，然后利用工具将其打包到固件 并 对设备进行 升级 。本章节介绍如何利用打包工具将音频文件打包至 用户分区中 。 

步骤 **1**： 从 QuecPython 官网 http://qpy.quectel.com/down.html 下载 SDK 包 。 

![Quectel_QuecPython_音频文件播放_033.png](media/Quectel_QuecPython_音频文件播放_033.png)

​																	图 **1**： 下载 **SDK** 包 

步骤 **2**： 解压 SDK 包 ， 并进入 *tools* 目录 下 ， 解压 *littlefs_tools.zip*。 

![Quectel_QuecPython_音频文件播放_034.png](media/Quectel_QuecPython_音频文件播放_034.png)

​															图 **2**： ***littlefs_tools*** 目录下的 文件

步骤 **3**： 将 需要打包的音频文件存放至 *littlefs_tools/mount* 目录下 ， 此处 以 *music.mp3* 为例 。 

![Quectel_QuecPython_音频文件播放_035.png](media/Quectel_QuecPython_音频文件播放_035.png)

图 **3**： 上传 **music.mp3** 音频文件 至 **littlefs_tools/mount** 

**备注** : 

1. 请勿删除 mount 目录下默认的 apn 配置文件。 

2. 目前用户分区大小默认为 5 M，所以放入音频文件的大小不应该超过 5 M，同时还应预留足够的空间 存放用户的应用程序及其他文件。 

步骤 **4**： 返回 至 *littlefs_tools* 目录 ， 即 *mklfs.exe* 所在的目录 。 在该目录 下打开 cmd， 然后输入如下命

令 。 

```shell
mklfs.exe -c mount -b 4096 -r 4096 -p 4096 -s 1048576 -i customer_fs.bin 
```

- **说明** 

1. 上述命令参数中 -s 参数后面的数字表示生成文件系统镜像的大小，单位字节，此处 生成 1M 大小的镜像，即 1024 x 1024Byte = 1048579 Bytes；如果用户分区大小有变化，不 为 1 M， 则需要根据实际情况修改该参数，以生成大小匹配的文件镜像。
1. 默认生成的文件镜像名称就是 customer_fs.bin，暂不支持用户修改该 名称。 

- **示例** 

![Quectel_QuecPython_音频文件播放_038.png](media/Quectel_QuecPython_音频文件播放_038.png)

步骤 **5**：步骤 4 执行 成功后 ，将在 *littlefs_tools* 目录下 生成文件系统镜像文件 *customer_fs.bin*，将其打

`    `包至固件包。

![Quectel_QuecPython_音频文件播放_039.png](media/Quectel_QuecPython_音频文件播放_039.png)

​											图 **4**： 打包 镜像文件 **customer_fs.bin** 至版本包

#### 附录术语缩写 

表 **1**： 术语缩写 

| 缩写 | 英文全称                          | 中文全称         |
| ---- | --------------------------------- | ---------------- |
| SDK  | Software Development Kit          | 软件开发工具包   |
| API  | Application Programming Interface | 应用程序编程接口 |


### TTS 使用指导 

#### 概述 

TTS 是 Text To Speech的缩写，即“从文本到语音”，是人机对话的一部分，让机器能够说话。它是同时运用语言学和心理学的杰出之作，在内置芯片的支持之下，通过神经网络的设计，把文字智能地转化为自然语音流。TTS技术对文本文件进行实时转换，转换时间之短可以秒计算。在其特有智能语音控制器作用下，文本输出的语音音律流畅，使得听者在听取信息时感觉自然，毫无机器语音输出的冷漠与生涩感。在使用开发板的TTS 模块功能之前我们需要先了解模块的 Audio 接口，如下图（以 EC100Y-CN模块为例）：

![](media/35b9112bf62d5cc4a417eb4190b0a979.jpg)

>   图 **1**：**EC100Y-CN** 模块 **Audio** 接口

>   连接 3.5mm 音频接口后按照《Quectel-QuecPython-Cat1开发板使用说明》进行驱动下载和固件安装。

#### TTS API 详解 

>   本章节介绍 TTS 相关 API。

**tts = audio.TTS** 

>   该函数用于导入音频（audio）库并创建 TTS 对象。

- 函数原型

  import audio 

  tts = audio.TTS(device)

- 参数

  *device*：

  表示设备类型，取值如下：

1.  话筒

2.  耳机

3.  喇叭

>   ⚫ 返回值

>   无。

**tts.play** 

>   该函数用于播放语音。

- 函数原型

  tts.play(priority, breakin, mode, str)

- 参数

  *priority*：整型。播放优先级，支持优先级 0~4，数值越大优先级越高。

  *breakin*：整型。打断模式，0 表示不允许被打断，1 表示允许被打断。

  *mode*：

  整型。编码模式：

1. UNICODE16 (Size end conversion)

2. UTF-8

3. UNICODE16 (Don't convert)

   *str*：字符串。待播放字符串。

   ⚫ 返回值

0 播放成功

>   -1 播放失败

>   1 无法立即播放，加入播放队列

-2 无法立即播放，且该请求的优先级组队列任务已达上限，无法加入播放队列备注

>   支持优先级 0~4，数字越大优先级越高，每个优先级组可同时最多加入 10
>   个播放任务，播放队列策略见

>   《Quectel QuecPython 类库 API 说明》。

**tts.setSpeed** 

>   该函数用于设置播放速度。

- 函数原型

  tts.setSpeed(speed)

- 参数

  *speed*：整型。播放速度，范围：0~9。值越大，速度越快。

- 返回值

  设置成功返回当前播放速度，失败返回整型-1。

**tts.setVolume** 

>   该函数用于设置播放音量。

- 函数原型

  tts.setVolume(vol)

- 参数

  *vol*：整型。播放音量。范围：0~9，0 表示静音。

- 返回值

  设置成功返回当前音量，失败返回整型-1。

**tts.getSpeed** 

>   该函数用于获取当前播放速度。

- 函数原型

  tts.getSpeed()

- 参数

  无。

- 返回值

  成功返回当前播放速度，失败返回整型-1。

**tts.getVolume** 

>   该函数用于获取播放音量。

- 函数原型

  tts.getVolume()

- 参数

  无。

- 返回值

  成功返回当前播放音量，失败返回整型-1。

**tts.getState** 

>   该函数用于获取当前播放状态。

- 函数原型

  tts.getState()

- 参数

  无。

- 返回值

1.  当前无 TTS 播放

2.  当前有 TTS 正在播放

**tts.stop** 

>   该函数用于暂停播放。

- 函数原型

  tts.stop()

- 参数

>   无。

-   返回值

0 暂停播放成功

>   -1 暂停播放失败

**tts.close** 

>   该函数用于关闭 TTS 功能。

- 函数原型

  tts.close()

- 参数

  无。

- 返回值

0 关闭 TTS 成功

>   -1 关闭 TTS 失败

#### TTS 功能实现 

**命令行执行** 

1. 通过 Xshell
   连接开发板主串口后按以下步骤执行，通过以下函数导入音频（audio）库并创建 TTS
   对象：

   import audio tts = audio.TTS(device)

![](media/cd4fe22a5b5b1c9a1ecad743187c1d14.jpg)

1. 使用以下函数播放语音：

   tts.play(priority, breakin, mode, str)

![](media/9c3b369e3dc8b4f7b157861383dbbfac.jpg)

![](media/ca8b43ce1e9c9364ba50d7a744f72b71.jpg)

1.  此时可在耳机中听到播放文本内容的语音，可通过 *tts.setSpeed(speed)*和
    *tts.setVolume(vol)*来设置播放速度和播放音量。

![](media/d2cef6ba0685ea8f9fe2095c6e1ef9f9.jpg)

1.  通过 *tts.getSpeed()*和
    *tts.getVolume()*来获取当前播放速度和音量。另外，可通过
    *tts.getState()*来获取当前播放状态。

![](media/dbb0d91af354b1481829d37270a36e0b.jpg)

1.  播放过程中可通过 *tts.stop()*来暂停播放。播放完成后可通过 *tts.close()*关闭
    TTS 功能。

![](media/7a5e31394f4d29cc26626c279cc933fe.jpg)

**执行 py 文件** 

1.  首先在提供的 SDK 工具包中进入 demo 目录，找到 TTS 文件夹，通过 QPYcom 工具将
    TTS 目录下的 example_tts.py
    脚本文件发送到模块中，脚本文件发送和执行具体步骤，参见《QPYcom
    工具使用说明》。

![](media/139025156eadcb1ec370ba48b610e43e.jpg)

1.  在 Xshell 中，连接模块主串口，进入交互界面，通过
    *uos.listdir()*方法确认上一步骤发送的脚本文件是否在当前目录下，然后执行如下步骤：

![](media/85a947dbbd4ec41cb30a42b2a0e60a70.jpg)

通过 import example 导入 example 模块，该模块提供了 *exec()*方法用来执行 python
脚本程序，通过 *example.exec(‘example.tts.py’)*来执行 example.tts.py
脚本，执行完成后即可在耳机中听到播放脚本中文本内容的语音。

#### 附录 

>   表 **1**：术语缩写

| 术语    | 英文全称                                               | 中文全称                        |
| ------- | ------------------------------------------------------ | ------------------------------- |
| API     | Application Programming Interface                      | 应用程序编程接口                |
| LTE     | Long Term Evolution                                    | 长期演进                        |
| SDK     | Software Development Kit                               | 软件开发工具包                  |
| TTS     | Text To Speech                                         | 从文本到语音                    |
| UNICODE | Unicode                                                | 统一码                          |
| UTF     | Universal Character Set/Unicode  Transformation Format | 针对 Unicode 的可变长度字符编码 |

### LCD 使用指导

#### LCD相关接口

**创建LCD对象**

首先，导入machine模块下的LCD，然后创建LCD对象。有关示例代码，请参考以下代码清单：

```
from machine import LCD
lcd = LCD()
```

**lcd.lcd_init**

该方法用于初始化LCD。

**函数原型**

```
lcd.lcd_init(lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid,lcd_display_on, lcd_display_off, lcd_set_brightness)
```

**参数**

lcd_init_data：
传入LCD的配置命令

lcd_width：
LCD屏幕的宽度。宽度不超过 500 。

lcd_hight：
LCD屏幕的高度。高度不超过 500 。

lcd_clk：
LCD SPI时钟。SPI时钟为6.5K/13K/26K/52K。

data_line：
数据线数。参数值为 1 和 2 。
line_num：
线的数量。参数值为 3 和 4 。

lcd_type：
屏幕类型。 0 ：fstn； 1 ：rgb

lcd_invalid：
LCD写屏时xy的设置

lcd_display_on：
LCD屏亮

lcd_display_off：
LCD屏灭

lcd_set_brightness：
LCD设置亮度值。设置为none表示由LCD_BL_K控制亮度（有些屏幕是由寄存器控制屏幕亮度，有些是通过LCD_BL_K控制屏幕亮度）

**返回值**

0 成功

-1 已经初始化

-2 屏初始化参数错误（为空或过大（大于 1000 像素点））

-3 初始化参数解析错误

-4 屏幕缓存申请失败

-5 配置参数错误

**lcd.lcd_clear**

该方法用于清除屏幕。

函数原型

```
lcd.lcd_clear(color)
```

**参数**

color：
需要刷屏的颜色值

**返回值**

0 成功

-1 屏幕未初始化



**lcd.lcd_write**

该方法用于区域写屏。

**函数原型**

lcd.lcd_write(color_buffer,start_x,start_y,end_x,end_y)

**参数**

Color_buffer：
屏幕的颜色值缓存。

start_x：
起始x坐标

start_y：
起始y坐标

end_x：
结束x坐标

end_y：
结束y坐标

**返回值**

0 成功

-1 屏幕未初始化

-2 宽度和高度设置错误

-3 数据缓存为空

**lcd.lcd_brightness**

该方法用于设置屏幕亮度。

**函数原型**

```
lcd.lcd_brightness(level)
```

**参数**

level：
亮度等级。此处会调用lcd.lcd_init()中的lcd_set_brightness参数。若该参数为None，亮度调节则由
背光亮度调节引脚来控制。

**返回值**

0 成功

-1 屏幕未初始化



**lcd.lcd_display_on**

该方法用于设置亮屏。调用此接口后调用lcd.lcd_init()中的lcd_display_on回调。

**函数原型**

```
lcd.lcd_display_on ()
```

**参数**

无

**返回值**

0 成功

-1 屏幕未初始化

**lcd.lcd_display_off**

该方法用于灭屏设置。调用此接口后调用lcd.lcd_init()中的lcd_display_off回调。

**函数原型**

```
lcd.lcd_display_off ()
```

**参数**

无

**返回值**

0 成功

- 1 屏幕未初始化

**lcd.lcd_write_cmd**

该方法用于写入命令。

**函数原型**

```
lcd.lcd_write_cmd (cmd_value, cmd_value_len)
```

**参数**

cmd_value：
命令值

cmd_value_len：
命令值长度

**返回值**

0 				成功
其他值 	   失败

lcd.lcd_write_data

该方法用于写入数据。

**函数原型**

```
lcd.lcd_write_data (data_value, data_value_len)
```

**参数**

data_value：

数据值

data_value_len：
数据值长度

**返回值**

0 				成功
其他值 	   失败


#### LCD配置流程

**LCD硬件接线**

如下表所示，LCD引脚对应模块使用的LCD模块引脚，如下表所示：

表 1 ：引脚对应表

```
LCD引脚  				   LCD模块引脚
LCD_SPI_CLK  			gpio[20]
LCD_SPI_DOUT 			gpio[24]
LCD_SPI_CS  			gpio[22]
LCD_SPI_RS  			gpio[21]
LCD_SPI_RST  			gpio[26]
LCD_BL_K 				/
```

**编写屏幕初始化参数**

在交互式命令行窗口中键入以下内容，准备LCD屏幕初始化参数，参数格式为：类型+长度+参数值：

类型： 0 表示命令； 1 表示数据； 2 表示延时

长度：若类型为 0 ，则长度表示命令后的数据数量；若类型为 1 ，则长度表示数据的长度

参数值：对应值

以下以ili9225为例：

```
Ili9225_init = (
0,1,0x02, 			#命令，后接一个data, cmd值为0x
1,2,0x01,0x00, 		#数据，数据长度为 2 ， data值为0x
0,1,0x01,

1,2,0x01,0x1C,
0,1,0x03,
1,2,0x10,0x30,
0,1,0x08,
1,2,0x08,0x08,
0,1,0x0B,
1,2,0x11,0x00,
0,1,0x0C,
1,2,0x00,0x00,
0,1,0x0F,
1,2,0x14,0x01,
0,1,0x15,
1,2,0x00,0x00,
0,1,0x20,
1,2,0x00,0x00,
0,1,0x21,
1,2,0x00,0x00,
0,1,0x10,
1,2,0x08,0x00,
0,1,0x11,
1,2,0x1F,0x3F,
0,1,0x12,
1,2,0x01,0x21,
0,1,0x13,
1,2,0x00,0x0F,
0,1,0x14,
1,2,0x43,0x49,
0,1,0x30,
1,2,0x00,0x00,
0,1,0x31,
1,2,0x00,0xDB,
0,1,0x32,
1,2,0x00,0x00,
0,1,0x33,
1,2,0x00,0x00,
0,1,0x34,
1,2,0x00,0xDB,
0,1,0x35,
1,2,0x00,0x00,
0,1,0x36,
1,2,0x00,0xAF,
0,1,0x37,
1,2,0x00,0x00,
0,1,0x38,

1,2,0x00,0xDB,
0,1,0x39,
1,2,0x00,0x00,
0,1,0x50,
1,2,0x00,0x01,
0,1,0x51,
1,2,0x20,0x0B,
0,1,0x52,
1,2,0x00,0x00,
0,1,0x53,
1,2,0x04,0x04,
0,1,0x54,
1,2,0x0C,0x0C,
0,1,0x55,
1,2,0x00,0x0C,
0,1,0x56,
1,2,0x01,0x01,
0,1,0x57,
1,2,0x04,0x00,
0,1,0x58,
1,2,0x11,0x08,
0,1,0x59,
1,2,0x05,0x0C,
0,1,0x07,
1,2,0x10,0x17,
0,1,0x22,
)
Ili9225_init_data = bytearray(Ili9225_init)
```



**执行初始化接口**

本节以ili 9225 为例，演示如何驱动屏幕。

创建LCD对象

在交互式命令行窗口中键入以下命令，创建LCD对象。

```
from machine import LCD
lcd = LCD()
```

打开屏显

在交互式命令行窗口中键入以下命令，打开屏显：

```
def display_on(para):
	print("display on")
	lcd.lcd_write_cmd(0x07, 1)
	lcd.lcd_write_data(0x1017, 2)
```

关闭屏显

在交互式命令行窗口中键入以下命令，关闭屏显：

```
def display_off(para):
	print("display off")
	lcd.lcd_write_cmd(0x07, 1)
	lcd.lcd_write_data(0x1004, 2)
```

编写写屏时区域值

不同的LCD屏有不同的设置区域方式，故放置python层实现。在底层实现lcd_write时，会调用该函
数在交互式命令行窗口中键入以下命令，实现lcd_invalid：

```
def lcd_invalid(para):
    print("invalid:",para[0], para[1], para[2], para[3])
    lcd.lcd_write_cmd(0x36, 1)
    lcd.lcd_write_data(para[2], 2)
    lcd.lcd_write_cmd(0x37, 1)
    lcd.lcd_write_data(para[0], 2)
    lcd.lcd_write_cmd(0x38, 1)
    lcd.lcd_write_data(para[3], 2)
    lcd.lcd_write_cmd(0x39, 1)
    lcd.lcd_write_data(para[1], 2)
    lcd.lcd_write_cmd(0x20, 1)
    lcd.lcd_write_data(para[0], 2)
    lcd.lcd_write_cmd(0x21, 1)
    lcd.lcd_write_data(para[1], 2)
    lcd.lcd_write_cmd(0x22, 1)
    lcd.lcd_write_cmd(0xff, 1) #此0xff尤为重要，此值时配置区域完成的标志
```

初始化配置

在交互式命令行窗口中键入以下命令，实现LCD配置：


```
lcd.lcd_init(Ili9225_init_data,176,220,13000,1,4,0,lcd_invalid,display_on,display_off,None))
Ili9225_init_data：	2.1配置的初始化参数
176 ： 				lcd宽度
220 ： 				lcd高度
13000 ： 			spi clk
1 ： 				1 根数据线
4 ： 				4 根线
0 ： 				type， 0 表示rgb
lcd_invalid： 		区域写屏，设置范围
display_on： 		亮屏
display_off: 		 息屏
None: 				 表示LCD亮度由IO口控制
```

清屏

在交互式命令行窗口中键入以下命令，实现清屏：

```
lcd.lcd_clear(0x001f)
```

区域写屏

在交互式命令行窗口中键入以下命令，实现区域写屏：

```
test_buf = (
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
```

```
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
)
test_buf1 = bytearray(test_buf)
lcd.lcd_write(test_buf1,10,10,20,20)
```

备注

因设计原因，该示例目标显示为0x001f（蓝色），当前为0x1f00。

#### LCD执行示例

本章节以ili9225为例，汇总LCD流程脚本命令以及执行结果。

LCD流程脚本命令

```
test=(
0,1,0x02,
1,2,0x01,0x00,
0,1,0x01,
1,2,0x01,0x1C,
0,1,0x03,
1,2,0x10,0x30,
0,1,0x08,
1,2,0x08,0x08,
0,1,0x0B,
1,2,0x11,0x00,
0,1,0x0C,
1,2,0x00,0x00,
0,1,0x0F,
1,2,0x14,0x01,
0,1,0x15,
1,2,0x00,0x00,
0,1,0x20,
1,2,0x00,0x00,
0,1,0x21,
1,2,0x00,0x00,
0,1,0x10,
1,2,0x08,0x00,
0,1,0x11,
1,2,0x1F,0x3F,
0,1,0x12,
1,2,0x01,0x21,
0,1,0x13,
1,2,0x00,0x0F,
0,1,0x14,
1,2,0x43,0x49,

0,1,0x30,
1,2,0x00,0x00,
0,1,0x31,
1,2,0x00,0xDB,
0,1,0x32,
1,2,0x00,0x00,
0,1,0x33,
1,2,0x00,0x00,
0,1,0x34,
1,2,0x00,0xDB,
0,1,0x35,
1,2,0x00,0x00,
0,1,0x36,
1,2,0x00,0xAF,
0,1,0x37,
1,2,0x00,0x00,
0,1,0x38,
1,2,0x00,0xDB,
0,1,0x39,
1,2,0x00,0x00,
0,1,0x50,
1,2,0x00,0x01,
0,1,0x51,
1,2,0x20,0x0B,
0,1,0x52,
1,2,0x00,0x00,
0,1,0x53,
1,2,0x04,0x04,
0,1,0x54,
1,2,0x0C,0x0C,
0,1,0x55,
1,2,0x00,0x0C,
0,1,0x56,
1,2,0x01,0x01,
0,1,0x57,
1,2,0x04,0x00,
0,1,0x58,
1,2,0x11,0x08,
0,1,0x59,
1,2,0x05,0x0C,
0,1,0x07,
1,2,0x10,0x17,
0,1,0x22,
)


from machine import LCD
lcd = LCD()
test1 = bytearray(test)

def display_on(para):
print("display on")
lcd.lcd_write_cmd(0x07, 1)
lcd.lcd_write_data(0x1017, 2)

def display_off(para):
print("display off")
lcd.lcd_write_cmd(0x07, 1)
lcd.lcd_write_data(0x1004, 2)

def display_light(para):
print("display_light")
lcd.lcd_write_cmd(0x13, 1)
lcd.lcd_write_data(para, 2)

def lcd_invalid(para):
print("invalid:",para[0], para[1], para[2], para[3])
lcd.lcd_write_cmd(0x36, 1)
lcd.lcd_write_data(para[2], 2)
lcd.lcd_write_cmd(0x37, 1)
lcd.lcd_write_data(para[0], 2)
lcd.lcd_write_cmd(0x38, 1)
lcd.lcd_write_data(para[3], 2)
lcd.lcd_write_cmd(0x39, 1)
lcd.lcd_write_data(para[1], 2)
lcd.lcd_write_cmd(0x20, 1)
lcd.lcd_write_data(para[0], 2)
lcd.lcd_write_cmd(0x21, 1)
lcd.lcd_write_data(para[1], 2)
lcd.lcd_write_cmd(0x22, 1)
lcd.lcd_write_cmd(0xff, 1)

lcd.lcd_init(test1, 176,220,13000,1,4,0,lcd_invalid,display_on,display_off,display_light)

test_buf = (
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,

0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,
0x1f,
)
test_buf1 = bytearray(test_buf)

lcd.lcd_write(test_buf1,10,10,20,20)

lcd.lcd_clear(0xf800) //红色
```



LCD流程脚本执行结果

LCD流程脚本执行结果分别如图所示：

![](media/脚本执行图1.jpg)




![](media/显示图片1.jpg)



![](media/脚本执行图2.jpg)



![](media/显示图片2.jpg)



![](media/脚本执行图3.jpg)



![](media/显示图片3.jpg)




#### 附录术语缩写

表 2 ：术语缩写

```
缩写 		英文全称 						中文全称

LCD 	Liquid Crystal Display 			液晶显示器

SPI 	Serial Peripheral Interface 	串行外设接口
```



### Record拾音 使用指导

#### 录音接口函数 

**创建record对象**

```python
import audio

record = audio.Record(file_name,callback) 
```

- **参数**

*file_name*： 

字符串 ,录音文件名 。 

*callback*： 

录音结束的回调函数 。 

- **返回值**

返回 *-1* 表示创建失败 ; 若返回对象 ,则表示创建成功 。 

- **示例**

```python
import audio 
def record_callback(para): 
	print("file_name:",para[0])   # 返回文件路径 
    print("audio_len:",para[1])   # 返回录音长度 
    print("audio_state:",para[2])  # 返回录音状态 -1: error 3:  成功 

record_test = audio.Record("record_test.wav",record_callback) 
```



**record.start**

开始录音 。 

- **函数原型**

```python
record.start(seconds) 
```

- **参数** 

*seconds*： 

整型 。 需要录制时长。 单位：秒 。 

- **返回值**

*0*  成功 ； 

*-1*  文件覆盖失败 ； 

*-2*  文件打开失败 ； 

*-3*  文件正在使用 ； 

*-4*  通道设置错误（只能设置 0 或 1）； 

*-5*  定时器资源申请失败 。 

- **示例**

```python
record.start(40) 
```



**record.stop**

停止录音 。

- **函数原型**

```python
record.stop() 
```

- **参数**

  无 

- **返回值**

  无

- **示例**

```python
record_test.stop()
```



**record.getFilePath**

读取录音文件的路径 。 

- **函数原型**

```python
record.getFilePath()
```

- **参数**

  无 

- **返回值**

录音文件的路径 ，字符串 。 

- **示例**

```python
record_test.getFilePath()
```

**record.getData** 

读取录音数据 。 

- **函数原型**

```python
record.getData(offset, size) 
```

- **参数**

*offset*： 

整型 。 读取数据的偏移量 。 

*size*： 

整型 。读取大小 ，需小于10K。

- **返回值**

*1*  读取数据错误 ； 

-*2*  文件打开失败 ； 

*-3*  偏移量设置错误 ； 

*-4*  文件正在使用 ； 

*-5*  设置超出文件大小 （offset+size > file_size）； *-6*  读 size 大于 10K； 

*-7*  内存不足 10K bytes： 返回数据 。 

- **示例**

```python
record_test.getData(0, 44)  # 读取文件头
```



**record.getSize**

读取录音文件大小 。 

- **函数原型**

```python
record.getSize()
```

- **参数**

  无 

- **返回值**

若获取成功,返回文件大小 ，此值会比返回 callback 返回值大 44 bytes（44 bytes 为文件头): 否则 ： 

*-1*  获取文件 大小 失败 ； 

*-2*  文件打开失败 ； 

*-3*  文件正在使用 ； 

- **示例**

```python
record_test.getSize()
```



**record.Delete**

删除录音文件 。 

- **函数原型**

```python
record.Delete()
```

- **参数**

  无 

- **返回值**

*0*  成功 

*-1*  文件不存在 

*-2*  文件正在使用

- **示例** 

```python
record_test.Delete()
```



**record.exists**

判断录音文件是否存在 。 

- **函数原型** 

```python
record.exists()
```

- **参数** 

  无 

- **返回值** 

*TRUE*  文件存在

 *FALSE*  文件不存在



**record.isBusy**

- **函数原型** 

```python
record.isBusy()
```

- **参数**

  无 

- **返回值** 

*0*  IDEL 

*1*  BUSY 

- **返回值**  

```python
record_test.isBusy()
```



#### 示例 

**Record流程脚本命令**

*record* 流程的脚本命令汇总如下 ： 

```python
import audio 

def  record_callback(para):  
    print("file_name:",para[0])  
    print("audio_len:",para[1]) 
    print("audio_state:",para[2]) 

record_test = audio.Record("record_test.wav",record_callback) record_test.isBusy() 
record_test.start(40) 
record_test.isBusy()  
record_test.stop() 
record_test.getFilePath()  
record_test.getData(0, 44)  
record_test.getSize()  
record_test.Delete()  
record_test.exists()  
record_test.isBusy() 
```



**脚本执行结果**

脚本执行结果分别下图所示：

![Quectel_QuecPython_录音API_029.png](media/Quectel_QuecPython_录音API_029.png)



### PWM 使用指导

#### PWM相关接口

**创建PWM对象**

首先，导入misc模块下的PWM，然后创建PWM对象。有关示例代码，请参考以下代码清单：

```
from misc import PWM
pwm0 = PWM(PWM.PWMn,PWM.ABOVE_xx,highTime,cycleTime)
```

**参数**

```
参数 				参数类型				 参数说明
				PWM.PWM0 					PWM0
PWM.PWMn		PWM.PWM1 					PWM1
				PWM.PWM2 					PWM2
				PWM.PWM3 					PWM3	


				PWM.ABOVE_MS				ms级取值范围：(0,1023]
PWM.ABOVE_xx	PWM.ABOVE_1US				us级取值范围：(0,157]
				PWM.ABOVE_10US				us级取值范围：(1,1575]
				PWM.ABOVE_BELOW_US			ns级 取值(0,1024]
					

highTime 		int							ms级时，单位为ms
											us级时，单位为us
											ns级别：需要使用者计算
             										频率 = 13Mhz / cycleTime
         											占空比 = highTime/ cycleTime


cycleTime 		int							ms级时，单位为ms
											us级时，单位为us
											ns级别：需要使用者计算
         											频率 = 13Mhz / cycleTime
         											占空比 = highTime/ cycleTime

```



**pwm.open**

该方法用于开始输出PWM。

**函数原型**

```
pwm.open()
```

**参数**

无

**返回值**

0 成功

-1 失败



**pwm.close**

该方法用于关闭输出PWM。

**函数原型**

```
pwm.open()
```

**参数**

无

**返回值**

0 成功

-1 失败



#### LCD执行示例

PWM流程的脚本命令汇总如下：

```
from misc import PWM
pwm1 = PWM(PWM.PWM0,PWM.ABOVE_MS, 1, 2)
pwm1 = PWM(PWM.PWM0,PWM.ABOVE_1US, 100, 200)
pwm1 = PWM(PWM.PWM0,PWM.ABOVE_10US, 100, 200)
```

#### 附录术语缩写

表 1 ：术语缩写

```
缩写 			英文全称 				中文全称

PWM 	Pulse Width Modulation	 	脉冲宽度调制
```






## 其他

### mpy-cross工具 使用指导

#### **工具介绍**

在Python中，可将.py文件编译为.pyc文件。编译后的.pyc文件是二进制格式，可加快加载速度，更重要的是可以保护原始代码。micropython使用mpy-cross工具完成.py文件编译并加密，编译后的文件为.mpy。

**文件说明**

**.py文件**
Python源代码文件

**.pyc文件**
二进制文件，Python源代码文件经过编译后生成的字节码文件。.pyc文件加载速度有所提高，且pyc是一种跨平台的字节码，由Python虚拟机来执行。

**.mpy文件**
Micropython提供mpy-cross工具，用于将Python源代码文件编译成.mpy文件。该文件和.pyc文件均为二进制字节码文件。

**参数说明**

![](media/图1_mpy-cross参数使用说明.jpg)

​														图 1 ：mpy-cross参数使用说明 图片索引

**备注**

可访问如下链接获取更多有关工具mpy-cross的说明：
https://pypi.org/project/mpy-cross/1.9.3/
https://makeblock-micropython-api.readthedocs.io/zh/latest/novapi/tutorial/precompiled_to_mpy.html

#### 工具使用

1. 连接EC100Y-CN开发板至电脑，如下图所示。接入后操作方法详见《Quectel_QuecPython_基础操作说明》。

   ![](media/图2_开发板接入电脑.jpg)

   ​															图 2 ：开发板接入电脑

2. 使用mpy-cross-amd64.exe工具。在工具同目录下编写usertest.py文件，文件内编写测试函数，
   如下所示：

   ```
   def test_mpy():
   	print(“hello this is mpy file”)
   ```

   

3. 打开Windows下cmd命令行，进入mpy-cross-amd64.exe工具所在目录，如下图所示。

   ![](media/图3_命令行进入工具目录.jpg)

   ​														图 3 ：命令行进入工具目录



4. 随后执行如下命令及参数生成.mpy文件：

   ```
   mpy-cross-amd64.exe -mno-unicode usertest.py
   ```

   生成的.mpy如下图所示

   ![](media/图4_mpy文件.jpg)

   ​																	图 4 ：mpy文件

5. 在test.py文件中使用import导入usertest模块，直接调用usertest文件中的方法，如下所示：

   ```
   import usertest
   usertest.test_mpy()
   ```

   

6. 把test.py文件和usertest.mpy文件分别上传到移远通信EC100Y-CN开发板内，上传方法详见
   《Quectel_QuecPython_基础操作说明》。

   

7. 在开发板中运行test.py文件，可看到经过mpy-cross工具加密过的usertest模块执行结果，如下
   图所示。

   ![](media/图5_test.py运行结果.jpg)

   ​																图 5 ：test.py运行结果





