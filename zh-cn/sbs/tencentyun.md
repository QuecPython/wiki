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

| 序号 | 文档名称                        | 备注                        |
| ---- | ------------------------------- | --------------------------- |
| [1]  | Quectel_QuecPython_基础操作说明 | QuecPython 上传下载文件说明 |

表 **2**：术语缩写

| 术语 | 英文全称                          | 中文全称         |
| ---- | --------------------------------- | ---------------- |
| API  | Application Programming Interface | 应用程序编程接口 |
| IoT  | Internet of Things                | 物联网           |