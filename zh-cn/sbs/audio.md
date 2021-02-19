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