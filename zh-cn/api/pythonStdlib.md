#### uos - 基本系统服务

uos模块包含文件系统访问和挂载构建，该模块实现了CPython模块相应模块的子集。更多信息请参阅阅CPython文档：[os](https://docs.python.org/3.5/library/os.html#module-os)

##### 删除文件

> **uos.remove(path)** 

删除文件。path表示文件名。

##### 改变当前目录

> **uos.chdir(path)**

改变当前目录。path表示目录名。

##### 获取当前路径

> **uos.getcwd()**

获取当前路径。

##### 列出指定目录文件

> **uos.listdir( [dir] )**

没有参数列出当前目录文件，否则列出给定目录的文件。dir为可选参数，表示目录名，默认为 ‘/’ 目录。

示例：

```
>>> uos.listdir()
[‘file1’, ‘read.txt’, ‘demo.py’]
```

##### 创建新目录

> **uos.mkdir(path)**

创建一个新的目录。path表示准备创建的目录名。

示例：

```
>>> uos.mkdir('testdir')
>>> uos.listdir()
[‘file1’, ‘read.txt’, ‘demo.py’, 'testdir']
```

##### 重命名文件

> **uos.rename(old_path, new_path)**

重命名文件。old_path表示旧文件或目录名，new_path表示新文件或目录名。

示例：

```
>>> uos.rename('testdir', 'testdir1')
```

##### 删除指定目录

> **uos.rmdir(path)**

删除指定目录。path表示目录名。

示例：

```
>>> uos.rmdir('testdir')
>>> uos.listdir()
[‘file1’, ‘read.txt’, ‘demo.py’]
```

##### 列出当前目录参数

> **uos.ilistdir( [dir] )**

该函数返回一个迭代器，该迭代器会生成所列出条目对应的3元组。dir为可选参数，表示目录名，没有参数时，默认列出当前目录，有参数时，则列出dir参数指定的目录。元组的形式为 `(name, type, inode[, size])`:

* name 是条目的名称，字符串类型，如果dir是字节对象，则名称为字节;
* type 是条目的类型，整型数，0x4000表示目录，0x8000表示常规文件；
* 是一个与文件的索引节点相对应的整数，对于没有这种概念的文件系统来说，可能为0；
* 一些平台可能会返回一个4元组，其中包含条目的size。对于文件条目，size表示文件大小的整数，如果未知，则为-1。对于目录项，其含义目前尚未定义。

##### 获取文件或目录的状态

> **uos.stat(path)**

获取文件或目录的状态。path表示文件或目录名。返回值是一个元组，返回值形式为：

`(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)`

* `mode` – inode保护模式
* `ino` – inode节点号
* `dev`  – inode驻留的设备
* `nlink`  – inode的链接数
* `uid ` – 所有者的用户ID
* `gid`  – 所有者的组ID
* `size`  – 文件大小，单位字节
* `atime`  – 上次访问的时间
* `mtime`  – 最后一次修改的时间
* `ctime`  – 操作系统报告的“ctime”，在某些系统上是最新的元数据更改的时间，在其它系统上是创建时间，详细信息参见平台文档

##### 获取文件系统状态信息

> **uos.statvfs(path)**

获取文件系统状态信息。path表示文件或目录名。返回一个包含文件系统信息的元组：

`(f_bsize, f_frsize, f_blocks, f_bfree, f_bavail, f_files, f_ffree, f_favail, f_flag, f_namemax)`

* `f_bsize` – 文件系统块大小，单位字节
* `f_frsize` – 分栈大小，单位字节
* `f_blocks` – 文件系统数据块总数
* `f_bfree` – 可用块数
* `f_bavai` – 非超级用户可获取的块数
* `f_files`  – 文件结点总数
* `f_ffree` – 可用文件结点数
* `f_favail` – 超级用户的可用文件结点数
* `f_flag` – 挂载标记
* `f_namemax` – 最大文件长度，单位字节

示例：

```
>>> import uos
>>> res = uos.statvfs("main.py")
>>> print(res)
(4096, 4096, 256, 249, 249, 0, 0, 0, 0, 255)
```

##### 获取关于底层信息或其操作系统的信息

> **uos.uname()**

获取关于底层信息或其操作系统的信息。该接口与micropython官方接口返回值形式有所区别，返回一个元组，形式为：

`(sysname, nodename, release, version, machine)`

* `sysname` – 底层系统的名称，string类型
* `nodename` – 网络名称(可以与 sysname 相同) ，string类型
* `release` – 底层系统的版本，string类型
* `version` – MicroPython版本和构建日期，string类型
* `machine` – 底层硬件(如主板、CPU)的标识符，string类型
* `qpyver` – QuecPython 短版本号，string类型

示例：

```python
>>> import uos
>>> uos.uname()
('sysname=EC600S-CNLB', 'nodename=EC600S', 'release=1.12.0', 'version=v1.12 on 2020-06-23', 'machine=EC600S with QUECTEL', 'qpyver=V0001')
>>> uos.uname()[0].split('=')[1] # 可通过这种方式来获取sysname的值
'EC600S-CNLB'
```



> **uos.uname2()**

获取关于底层信息或其操作系统的信息。该接口与micropython官方接口返回值形式一致。注意与上面uos.uname()接口返回值的区别，返回值形式为：

`(sysname='xxx', nodename='xxx', release='xxx', version='xxx', machine='xxx', qpyver='xxx')`

* `sysname` – 底层系统的名称，string类型
* `nodename` – 网络名称(可以与 sysname 相同) ，string类型
* `release` – 底层系统的版本，string类型
* `version` – MicroPython版本和构建日期，string类型
* `machine` – 底层硬件(如主板、CPU)的标识符，string类型
* `qpyver` – QuecPython 短版本号，string类型

示例：

```python
>>> import uos
>>> uos.uname2()
(sysname='EC600S-CNLB', nodename='EC600S', release='1.12.0', version='v1.12 on 2020-06-23', machine='EC600S with QUECTEL', qpyver='V0001')
>>> uos.uname2().sysname  # 可通过这种方式直接获取sysname的值
'EC600S-CNLB'
>>> uos.uname2().machine
'EC600S with QUECTEL'
```



##### 返回具有*n个*随机字节的bytes对象

> **uos.urandom(n)**

返回具有*n个*随机字节的bytes对象，只要有可能，它就会由硬件随机数生成器生成。

示例：

```
>>> import uos
>>> uos.urandom(5)
b'\xb3\xc9Y\x1b\xe9'
```



##### 注册存储设备 - SPI - SD卡

目前仅EC600N/EC800N平台支持。

> **uos.VfsFat(spi_port, spimode, spiclk, spics)**

初始化SD卡，和SD卡通信。使用SPI通信方式。

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| spi_port | int      | 通道选择[0,1]                                                |
| spimode  | int      | SPI 的工作模式(模式0最常用):<br/>时钟极性CPOL: 即SPI空闲时，时钟信号SCLK的电平（0:空闲时低电平; 1:空闲时高电平）<br/>0 : CPOL=0, CPHA=0<br/>1 : CPOL=0, CPHA=1<br/>2: CPOL=1, CPHA=0<br/>3: CPOL=1, CPHA=1 |
| spiclk   | int      | 时钟频率 0 : 812.5kHz 1 : 1.625MHz 2 : 3.25MHz 3 : 6.5MHz 4 : 13MHz |
| spics    | int      | 指定CS片选引脚为任意GPIO，硬件CS可以接这里指定的脚，也可以接默认的SPI CS脚<br/>1~n:指定Pin.GPIO1~Pin.GPIOn为CS脚 |

* 返回值

成功则返回VfsFat object，失败则会卡住。

* 示例 

```python
>>> cdev = uos.VfsFat(1, 0, 4, 1)
```



##### 注册存储设备 - SDIO - SD卡

目前仅EC600U/EC200U平台支持。

> **VfsSd(str)**

初始化SD卡，使用SDIO通信方式。

* 参数

| 参数 | 参数类型 | 参数说明                            |
| ---- | -------- | ----------------------------------- |
| str  | str      | 传入"sd_fs" |

* 返回值

成功则返回vfs object，失败则会报错。

- 引脚说明

| 平台   | 引脚                                                         |
| ------ | ------------------------------------------------------------ |
| EC600U | CMD:引脚号48<br />DATA0:引脚号39<br />DATA1:引脚号40<br />DATA2:引脚号49<br />DATA3:引脚号50<br />CLK:引脚号132 |
| EC200U | CMD:引脚号33<br />DATA0:引脚号31<br />DATA1:引脚号30<br />DATA2:引脚号29<br />DATA3:引脚号28<br />CLK:引脚号32 |

* 示例 

```python
>>> from uos import VfsSd
>>> udev = VfsSd("sd_fs")
```

###### 设置检测管脚

> **set_det(vfs_obj.GPIOn,mode)**

指定sd卡插拔卡的检测管脚和模式。

* 参数

| 参数          | 参数类型 | 参数说明                                                     |
| ------------- | -------- | ------------------------------------------------------------ |
| vfs_obj.GPIOn | int      | 用于sd卡插拔卡检测的GPIO引脚号，参照Pin模块的定义            |
| mode          | int      | 0:sd卡插上后，检测口为低电平；sd卡取出后，检测口为高电平<br />1:sd卡插上后，检测口为高电平；sd卡取出后，检测口为低电平 |

* 返回值

成功返回0，失败返回-1。

* 示例

```python
>>> from uos import VfsSd
>>> udev = VfsSd("sd_fs")
>>> uos.mount(udev, '/sd')
>>> udev.set_det(udev.GPIO10,0)#使用GPIO10作为卡检测管脚，sd卡插上，检测口为低电平，sd卡取出，检测口为高电平（实际使用根据硬件）
```

###### 设置插拔卡回调函数

> **set_callback(fun)**

设定发生插拔卡事件时的用户回调函数。

* 参数

| 参数 | 参数类型 | 参数说明                                                     |
| ---- | -------- | ------------------------------------------------------------ |
| fun  | function | 插拔卡回调 [ind_type]<br />ind_type: 事件类型，0：拔卡 1：插卡 |

* 返回值

成功返回0，失败返回-1。


SD卡使用示例（SDIO接口）

目前仅EC600U/EC200U平台支持。

```python
from uos import VfsSd
import ql_fs
udev = VfsSd("sd_fs")
uos.mount(udev, '/sd')
udev.set_det(udev.GPIO10,0)
#文件读写
f = open('/sd/test.txt','w+')
f.write('1234567890abcdefghijkl')
f.close()
uos.listdir('/sd')
f = open('/sd/test.txt','r')
f.read()
f.close()
#插拔卡回调函数
def call_back(para):
    if(para == 1):
        print("insert")
        print(uos.listdir('/usr'))  
        print(ql_fs.file_copy('/usr/1.txt','/sd/test.txt'))#复制sd卡里的test.txt内容到usr下的1.txt中
        print(uos.listdir('/usr'))
    elif(para == 0):
        print("plug out")   
        
udev.set_callback(call_back)
```



##### **注册存储设备 - SPI NOR FLASH**

目前仅EG915U支持

> uos.VfsLfs1(readsize,progsize,lookahead,pname,spi_port,spi_clk)

初始化spi nor flash,和外挂nor flash通信。使用SPI通信方式。

* 参数

| 参数      | 参数类型 | 参数说明                                                     |
| --------- | -------- | ------------------------------------------------------------ |
| readsize  | int      | 预留，暂未使用                                               |
| progsize  | int      | 预留，暂未使用                                               |
| lookahead | int      | 预留，暂未使用                                               |
| pname     | str      | 固定为“ext_fs”。后续扩展                                     |
| spi_port  | int      | 支持的端口参照SPI章节说明                                    |
| spi_clk   | int      | 时钟频率：<br />EG915U：0：6.25M 1:12.5M  2:25M  3:50M  4:3.125M 5:1.5625M  6:781.25K |

* 返回值

  成功则返回VfsLfs1 object,失败则 OSError 19。

* 示例

  ```python
  >>>ldev = uos.VfsLfs1(32, 32, 32, "ext_fs",1,0)
  >>>uos.mount(ldev,'/ext')
  >>>f = open('/ext/test.txt','w+')
  >>>f.write('hello world!!!')
  >>>f.close()
  
  >>>uos.listdir('ext')
  
  >>>f = open('/ext/test.txt','r')
  >>>f.read()
  >>>f.close()
  
  ```

  


##### 挂载文件系统

> **uos.mount(vfs_obj, path)**

挂载底层文件系统到VFS。

* 参数

| 参数    | 参数类型   | 参数说明         |
| ------- | ---------- | ---------------- |
| vfs_obj | vfs object | 文件系统对象     |
| path    | str        | 文件系统的根目录 |

* 返回值

无。

* 示例

```python
>>> cdev = uos.VfsFat(1, 0, 4, 1)
>>> uos.mount(cdev, '/sd')
```

- SD卡（SPI接口）使用示例

  目前仅EC600N/EC800N平台支持。

```python
>>> cdev = uos.VfsFat(1, 0, 4, 1)
>>> uos.mount(cdev, '/sd')
>>> f = open('/sd/test.txt','w+')
>>> f.write('0123456')
>>> f.close()
>>> uos.listdir('/sd')
>>> f = open('/sd/test.txt','r')
>>> f.read()
>>> f.close()
```



#### gc - 内存碎片回收

gc 模块实现内存垃圾回收机制，该模块实现了CPython模块相应模块的子集。更多信息请参阅阅CPython文档：[gc](https://docs.python.org/3.5/library/gc.html#module-gc)

##### 启用自动回收内存碎片机制

> **gc.enable()**

启用自动回收内存碎片机制。

##### 禁用自动回收机制

> **gc.disable()**

禁用自动回收机制。

##### 回收内存碎片

> **gc.collect()**

回收内存碎片。

##### 返回分配的堆RAM的字节数

> **gc.mem_alloc()**

返回分配的堆RAM的字节数。此功能是MicroPython扩展。

##### 返回可用堆RAM的字节数

> **gc.mem_free()**

返回可用堆RAM的字节数，如果此数量未知，则返回-1。此功能是MicroPython扩展。



#### ubinascii - 二进制与ASCII转换

ubinascii 模块实现了二进制数据与各种ASCII编码之间的转换(双向)，该模块实现了CPython模块相应模块的子集。更多信息请参阅阅CPython文档：[binascii](https://docs.python.org/3.5/library/binascii.html#module-binascii)

##### 解码base64编码的数据

> **ubinascii.a2b_base64(data)**

解码base64编码的数据，会自动忽略输入中的无效字符，返回 bytes 对象。

##### 以base64格式编码二进制数据

> **ubinascii.b2a_base64(data)**

以base64格式编码二进制数据，返回编码数据。后面跟换行符，作为 bytes 对象。

##### 将二进制数据转换为十六进制字符串表示

> **ubinascii.hexlify(data, [sep])**

将二进制数据转换为十六进制字符串表示。

示例：

```
>>> import ubinascii
# 没有sep参数
>>> ubinascii.hexlify('\x11\x22123')
b'1122313233'
>>> ubinascii.hexlify('abcdfg')
b'616263646667'
# 指定了第二个参数sep，它将用于分隔两个十六进制数
>>> ubinascii.hexlify('\x11\x22123', ' ')
b'11 22 31 32 33'
>>> ubinascii.hexlify('\x11\x22123', ',')
b'11,22,31,32,33'
```

##### 将十六进制形式的字符串转换成二进制形式的字符串表示

> **ubinascii.unhexlify(data)**

将十六进制形式的字符串转换成二进制形式的字符串表示。

示例：

```
>>> import ubinascii
>>> ubinascii.unhexlify('313222')
b'12"'
```



#### ucollections - 集合和容器类型

ucollections 模块用于创建一个新的容器类型，用于保存各种对象。该模块实现了CPython模块相应模块的子集。更多信息请参阅阅CPython文档：[collections](https://docs.python.org/3.5/library/collections.html#module-collections)

##### 创建一个新namedtuple容器类型

> **mytuple = ucollections.namedtuple(name, fields)**

创建一个具有特定名称和一组字段的新namedtuple容器类型，namedtuple是元组的子类，允许通过索引来访问它的字段。

参数

| 参数   | 参数类型 | 参数说明                       |
| ------ | -------- | ------------------------------ |
| name   | str      | 新创建容器的类型名称           |
| fields | tuple    | 新创建容器类型包含子类型的字段 |

示例：

```
>>> import ucollections
>>> mytuple = ucollections.namedtuple("mytuple", ("id", "name"))
>>> t1 = mytuple(1, "foo")
>>> t2 = mytuple(2, "bar")
>>> print(t1.name)
foo
```

##### 创建deque双向队列

> **dq = ucollections.deque(iterable, maxlen, flag)**

创建deque双向队列

* 参数

| 参数     | 参数类型 | 参数说明                                                     |
| -------- | -------- | ------------------------------------------------------------ |
| iterable | tuple    | iterable必须是空元组                                         |
| maxlen   | int      | 指定maxlen并将双端队列限制为此最大长度                       |
| flag     | int      | 可选参数；0(默认)：不检查队列是否溢出，达到最大长度时继续append会丢弃之前的值  ，1：当队列达到最大设定长度会抛出IndexError: full |

* 返回值

deque对象



##### deque对象方法

> ​	**dq.append(data)**

往队列中插入值。

* 参数

| 参数 | 参数类型     | 参数说明             |
| ---- | ------------ | -------------------- |
| data | 基本数据类型 | 需要添加到队列的数值 |

* 返回值

无

##### 从deque的左侧移除并返回移除的数据

> ​	**dq.popleft()**

从deque的左侧移除并返回移除的数据。如果deque为空，会引起索引错误

* 参数

无

* 返回值

返回pop出的值



**使用示例**

```python
from ucollections import deque

dq = deque((),5)
dq.append(1)
dq.append(["a"])
dq.append("a")

dq.popleft()  # 1
dq.popleft()  # ["a"]
dq.popleft()  # a
```



#### urandom - 生成随机数

urandom 模块提供了生成随机数的工具。

##### 随机生成对象 obj 中的元素

> **urandom.choice(obj)**

随机生成对象 obj 中的元素，obj 类型 string。

示例：

```
>>> import urandom
>>> urandom.choice("QuecPython")
't'
```

##### 随机产生一个在k bits范围内的十进制数

> **urandom.getrandbits(k)**

随机产生一个在k bits范围内的十进制数。

示例：

```
>>> import urandom
>>> urandom.getrandbits(1)  #1位二进制位，范围为0~1（十进制：0~1）
1
>>> urandom.getrandbits(1)
0
>>> urandom.getrandbits(8)  #8位二进制位，范围为0000 0000~1111 11111（十进制：0~255）
224
```

##### 随机生成一个 start 到 end 之间的整数

> **urandom.randint(start, end)**

随机生成一个 start 到 end 之间的整数。

示例：

```
>>> import urandom
>>> urandom.randint(1, 4)
4
>>> urandom.randint(1, 4)
2
```

##### 随机生成一个 0 到 1 之间的浮点数

> **urandom.random()**

随机生成一个 0 到 1 之间的浮点数。

示例：

```
>>> import urandom
>>> urandom.random()
0.8465231
```

##### 随机生成 start 到 end 间并且递增为 step 的正整数

> **urandom.randrange(start, end, step)**

随机生成 start 到 end 间并且递增为 step 的正整数。

示例：

```
>>> import urandom
>>> urandom.randrange(0, 8, 2)
0
>>> urandom.randrange(0, 8, 2)
6
```

##### 指定随机数种子

> **urandom.seed(sed)**

指定随机数种子，通常和其它随机数生成函数搭配使用。

示例：

```
>>> import urandom
>>> urandom.seed(20)  #指定随机数种子
>>> for i in range(0, 15): #生成0~15范围内的随机序列
...     print(urandom.randint(1, 10))
...     
8
10
9
10
2
1
9
3
2
2
6
1
10
9
6
```

##### 随机生成 start 到 end 范围内的浮点数

> **urandom.uniform(start, end)**

随机生成 start 到 end 范围内的浮点数。

示例：

```
>>> import urandom
>>> urandom.uniform(3, 5)
3.219261
>>> urandom.uniform(3, 5)
4.00403
```

**使用示例**

```python
'''
@Author: Baron
@Date: 2020-06-22
@LastEditTime: 2020-06-22 17:16:20
@Description: example for module urandom
@FilePath: example_urandom_file.py
'''
import urandom as random
import log
import utime

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Random_example"
PROJECT_VERSION = "1.0.0"

log.basicConfig(level=log.INFO)
random_log = log.getLogger("random")


if __name__ == '__main__':
    # urandom.randint(start, end)
    # 随机1 ~ 4之间
    num = random.randint(1, 4)
    random_log.info(num)

    # random between 0~1
    num = random.random()
    random_log.info(num)

    # urandom.unifrom(start, end)
    # 在开始和结束之间生成浮点数
    num = random.uniform(2, 4)
    random_log.info(num)

    # urandom.randrange(start, end, step)
    # 2-bit binary,the range is [00~11] (0~3)
    num = random.getrandbits(2)
    random_log.info(num)

    # 8-bit binary,the range is [0000 0000~1111 11111] (0~255)
    num = random.getrandbits(8)
    random_log.info(num)

    # urandom.randrange(start, end, step)
    # 从开始到结束随机生成递增的正整数
    num = random.randrange(2, 8, 2)
    random_log.info(num)

    # urandom.choice(obj)
    # 随机生成对象中元素的数量
    num = random.choice("QuecPython")
    random_log.info(num)

```



#### math - 数学运算

math 模块提供数学运算函数。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[math](https://docs.python.org/3.5/library/math.html#module-math)

##### 返回x的y次方

> **math.pow(x, y)**

返回x的y次方，返回值是浮点数。

示例：

```
>>> import math
>>> math.pow(2, 3)
8.0
```

##### 返回x的反余弦弧度值

> **math.acos(x)**

返回x的反余弦弧度值，返回值为浮点数。x是-1~1之间的数，包括-1和1，如果小于-1或者大于1，会产生错误。

示例：

```
>>> import math
>>> math.acos(0.6)
0.9272952
```

##### 返回x的反正弦弧度值

> **math.asin(x)**

返回x的反正弦弧度值，返回值为浮点数。x是-1~1之间的数，包括-1和1，如果小于-1或者大于1，会产生错误。

示例：

```
>>> import math
>>> math.asin(-1)
-1.570796
```

##### 返回x的反正切弧度值

> **math.atan(x)**

返回x的反正切弧度值，返回值为浮点数。

示例：

```
>>> import math
>>> math.atan(-8)
-1.446441
>>> math.atan(6.4)
1.4158
```

##### 返回给定的 X 及 Y 坐标值的反正切值

> **math.atan2(x, y)**

返回给定的 X 及 Y 坐标值的反正切值，返回值为浮点数。

示例：

```
>>> import math
>>> math.atan2(-0.50,0.48)
-0.8058035
>>> math.atan2(7, 9)
0.6610432
```

##### 返回数字的上入整数

> **math.ceil(x)**

返回数字的上入整数。

示例：

```
>>> import math
>>> math.ceil(4.1)
5
```

##### 把y的正负号加到x前面

> **math.copysign(x, y)**

把y的正负号加到x前面，可以使用0，返回值为浮点数。

示例：

```
>>> import math
>>> math.copysign(5, 0)
5.0
>>> math.copysign(5, -4)
-5.0
>>> math.copysign(5, 9)
5.0
```

##### 返回x的弧度的余弦值

> **math.cos(x)**

返回x的弧度的余弦值，范围再-1~1之间，返回值为浮点数。

示例：

```
>>> import math
>>> math.cos(3)
-0.9899925
```

##### 将弧度转换为角度

> **math.degrees(x)**

将弧度转换为角度，返回值为浮点数。

示例：

```
>>> import math
>>> math.degrees(5)
286.4789
>>> math.degrees(math.pi/2)
90.0
```

##### 数学常量 `e`

> **math.e**

数学常量 `e`，`e`即自然常数。

##### 返回e的x次幂

> **math.exp(x)**

返回e的x次幂，返回值为浮点数。

示例：

```
>>> import math
>>> math.exp(1)
2.718282
>>> print(math.e)
2.718282
```

##### 返回数字的绝对值

> **math.fabs(x)**

返回数字的绝对值，返回值为浮点数。

示例：

```
>>> import math
>>> math.fabs(-3.88)
3.88
```

##### 返回数字的下舍整数

> **math.floor(x)**

返回数字的下舍整数。

示例：

```
>>> import math
>>> math.floor(8.7)
8
>>> math.floor(9)
9
>>> math.floor(-7.6)
-8
```

##### 返回x/y的余数

> **math.fmod(x, y)**

返回x/y的余数，返回值为浮点数。

示例：

```
>>> import math
>>> math.fmod(15, 4)
3.0
>>> math.fmod(15, 3)
0.0
```

##### 返回由x的小数部分和整数部分组成的元组

> **math.modf(x)**

返回由x的小数部分和整数部分组成的元组。

示例：

```
>>> import math
>>> math.modf(17.592)
(0.5919991, 17.0)
```

##### 返回一个元组(m,e)

> **math.frexp(x)**

返回一个元组(m,e),其计算方式为：x分别除0.5和1,得到一个值的范围，2e的值在这个范围内，e取符合要求的最大整数值,然后x/(2e)，得到m的值。如果x等于0，则m和e的值都为0，m的绝对值的范围为(0.5,1)之间，不包括0.5和1。

示例：

```
>>> import math
>>> math.frexp(52)
(0.8125, 6)
```

##### 判断 x 是否为有限数

> **math.isfinite(x)**

判断 x 是否为有限数，是则返回True，否则返回False。

示例：

```
>>> import math
>>> math.isfinite(8)
True
```

##### 判断是否无穷大或负无穷大

> **math.isinf(x)**

如果x是正无穷大或负无穷大，则返回True,否则返回False。

示例：

```
>>> import math
>>> math.isinf(123)
False
```

##### 判断是否数字

> **math.isnan(x)**

如果x不是数字，返回True,否则返回False。

示例：

```
>>> import math
>>> math.isnan(23)
False
```

##### 返回x*(2**i)的值

> **math.ldexp(x, exp)**

返回x*(2**i)的值。

示例：

```
>>> import math
>>> math.ldexp(2, 1)
4.0
```

##### 返回x的自然对数

> **math.log(x)**

返回x的自然对数，x > 0，小于0会报错。

示例：

```
>>> import math
>>> math.log(2)
0.6931472
```

##### 数学常量 pi

> **math.pi**

数学常量 pi（圆周率，一般以π来表示）。

##### 将角度转换为弧度

> **math.radians(x)**

将角度转换为弧度，返回值为浮点数。

示例：

```
>>> import math
>>> math.radians(90)
1.570796
```

##### 返回x弧度的正弦值

> **math.sin(x)**

返回x弧度的正弦值，数值在 -1 到 1 之间。

示例：

```
>>> import math
>>> math.sin(-18)
0.7509873
>>> math.sin(50)
-0.2623749
```

##### 返回数字x的平方根

> **math.sqrt(x)**

返回数字x的平方根，返回值为浮点数。

示例：

```
>>> import math
>>> math.sqrt(4)
2.0
>>> math.sqrt(7)
2.645751
```

##### 返回 x 弧度的正切值

> **math.tan(x)**

返回 x 弧度的正切值，数值在 -1 到 1 之间，为浮点数。

示例：

```
>>> import math
>>> math.tan(9)
-0.4523157
```

##### 返回x的整数部分

> **math.trunc(x)**

返回x的整数部分。

示例：

```
>>> import math
>>> math.trunc(7.123)
7
```

**使用示例**

```python
# 数学运算math函数示例

import math
import log
import utime


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"


if __name__ == '__main__':
    # 设置日志输出级别
    log.basicConfig(level=log.INFO)
    math_log = log.getLogger("Math")

    # x**y运算后的值
    result = math.pow(2,3)
    math_log.info(result)
    # 8.0

    # 取大于等于x的最小的整数值，如果x是一个整数，则返回x
    result = math.ceil(4.12)
    math_log.info(result)
    # 5

    # 把y的正负号加到x前面，可以使用0
    result = math.copysign(2,-3)
    math_log.info(result)
    # -2.0

    # 求x的余弦，x必须是弧度
    result = math.cos(math.pi/4)
    math_log.info(result)
    # 0.7071067811865476

    # 把x从弧度转换成角度
    result = math.degrees(math.pi/4)
    math_log.info(result)
    # 45.0

    # e表示一个常量
    result = math.e
    math_log.info(result)
    # 2.718281828459045

    # exp()返回math.e(其值为2.71828)的x次方
    result = math.exp(2)
    math_log.info(result)
    # 7.38905609893065

    # fabs()返回x的绝对值
    result = math.fabs(-0.03)
    math_log.info(result)
    # 0.03

    # floor()取小于等于x的最大的整数值，如果x是一个整数，则返回自身
    result = math.floor(4.999)
    math_log.info(result)
    # 4

    # fmod()得到x/y的余数，其值是一个浮点数
    result = math.fmod(20,3)
    math_log.info(result)
    # 2.0

    # frexp()返回一个元组(m,e),其计算方式为：x分别除0.5和1,得到一个值的范围，2e的值在这个范围内，e取符合要求的最大整数值,然后x/(2e),得到m的值。如果x等于0,则m和e的值都为0,m的绝对值的范围为(0.5,1)之间，不包括0.5和1
    result = math.frexp(75)
    math_log.info(result)
    # (0.5859375, 7)

    # isfinite()如果x不是无穷大的数字,则返回True,否则返回False
    result = math.isfinite(0.1)
    math_log.info(result)
    # True

    # isinf()如果x是正无穷大或负无穷大，则返回True,否则返回False
    result = math.isinf(234)
    math_log.info(result)
    # False

    # isnan()如果x不是数字True,否则返回False
    result = math.isnan(23)
    math_log.info(result)
    # False

    # ldexp()返回x*(2**i)的值
    result = math.ldexp(5,5)
    math_log.info(result)
    # 160.0

    # modf()返回由x的小数部分和整数部分组成的元组
    result = math.modf(math.pi)
    math_log.info(result)
    # (0.14159265358979312, 3.0)

    # pi:数字常量，圆周率
    result = math.pi
    math_log.info(result)
    # 3.141592653589793

    # sin()求x(x为弧度)的正弦值
    result = math.sin(math.pi/4)
    math_log.info(result)
    # 0.7071067811865476

    # sqrt()求x的平方根
    result = math.sqrt(100)
    math_log.info(result)
    # 10.0

    # tan()返回x(x为弧度)的正切值
    result = math.tan(math.pi/4)
    math_log.info(result)
    # 0.9999999999999999

    # trunc()返回x的整数部分
    result = math.trunc(6.789)
    math_log.info(result)
    # 6

```



#### usocket - socket模块

usocket 模块提供对BSD套接字接口的访问。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[socket](https://docs.python.org/3.5/library/socket.html#module-socket)

##### 创建一个新的套接字

> **usocket.socket(af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP)**

根据给定的地址族、套接字类型以及协议类型参数，创建一个新的套接字。注意，在大多数情况下不需要指定*proto*，也不建议这样做，因为某些MicroPython端口可能会省略 `IPPROTO_*`常量。

**常量说明**

af - 地址族

* usocket.AF_INET ：IPV4

* usocket.AF_INET6 ：IPV6

type - socket类型

* usocket.SOCK_STREAM ：对应TCP的流式套接字

* usocket.SOCK_DGRAM ：对应UDP的数据包套接字

* usocket.SOCK_RAW ：原始套接字

proto - 协议号

* usocket.IPPROTO_TCP

* usocket.IPPROTO_UDP

* usocket.IPPROTO_TCP_SER ：对应TCP socket 服务端套接字

其他

* usocket.SOL_SOCKET - 套接字选项级别，

* usocket.SO_REUSEADDR - 允许绑定地址快速重用

示例：

```
import usocket
# 创建基于TCP的流式套接字
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
# 创建基于UDP的数据报套接字
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
# 创建基于TCP的服务端套接字
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM, usocket.IPPROTO_TCP_SER)
```

##### 将主机域名（host）和端口（port）转换为用于创建套接字的5元组序列

> **usocket.getaddrinfo(host, port)**

将主机域名（host）和端口（port）转换为用于创建套接字的5元组序列，元组结构如下：

`(family, type, proto, canonname, sockaddr)`



**socket类的方法**

##### 服务端绑定指定地址address


> **socket.bind(address)**

服务端绑定指定地址address的服务器。

* `address` ：包含地址和端口号的元组或列表

注意：该方法在服务端套接字使用时，绑定address时会将address设为客户端可连接address。其他客户端是否可连接，需确认运营商网络是否支持。

示例：

```
#绑定拨号IP为服务器地址，端口自定义
socket.bind(("",80))
#绑定自定义address
socket.bind(("192.168.0.1",80))
```

##### 允许服务端接受连接


> **socket.listen(backlog)**

允许服务端接受连接，可指定最大连接数。

* `backlog` ：接受套接字的最大个数，至少为0。

##### 接受连接请求

> **socket.accept()**

接受连接请求，返回元组，包含新的套接字和客户端地址以及客户端端口，形式为：`(conn, address, port)`

* `conn` ：新的套接字对象，可以用来发送和接收数据

* `address` ：连接到服务器的客户端地址

* `port` ：连接到服务器的客户端端口

##### 连接到指定地址address的服务器

> **socket.connect(address)**

连接到指定地址address的服务器。

* `address` ：包含地址和端口号的元组或列表

##### 从套接字中读取size字节数据

> **socket.read( [ size ] )**

从套接字中读取size字节数据，返回一个字节对象。如果没有指定size，则会从套接字读取所有可读数据，直到读取到数据结束，此时作用和 `socket.readall()` 相同。

##### 将字节读取到缓冲区buf中

> **socket.readinto(buf, [ , nbytes ])**

将字节读取到缓冲区buf中。如果指定了nbytes，则最多读取nbytes数量的字节；如果没有指定nbytes，则最多读取len(buf)字节。返回值是实际读取的字节数。

##### 按行读取数据

> **socket.readline()**

按行读取数据，遇到换行符结束，返回读取的数据行。

##### 写入缓冲区的数据

> **socket.write(buf)**

写入缓冲区的数据，buf为待写入的数据，返回实际写入的字节数。

##### 发送数据

> **socket.send(bytes)**

发送数据，返回实际发送的字节数。

* `bytes` ：bytes型数据

##### 将所有数据都发送到套接字

> **socket.sendall(bytes)**

将所有数据都发送到套接字。与`send()`方法不同的是，此方法将尝试通过依次逐块发送数据来发送所有数据。

注意：该方法再非阻塞套接字上的行为是不确定的，建议再MicroPython中，使用 `write()` 方法，该方法具有相同的“禁止短写”策略来阻塞套接字，并且将返回在非阻塞套接字上发送的字节数。

* `bytes` ：bytes型数据

##### 将数据发送到套接字

> **socket.sendto(bytes, address)**

将数据发送到套接字。该套接字不应连接到远程套接字，因为目标套接字是由*address*指定的。

* `bytes` ：bytes型数据

* `address` ：包含地址和端口号的元组或列表

##### 从套接字接收数据

> **socket.recv(bufsize)**

从套接字接收数据。返回值是一个字节对象，表示接收到的数据。一次接收的最大数据量由bufsize指定。

* `bufsize` ：一次接收的最大数据量

##### 将套接字标记为关闭并释放所有资源

> **socket.close()**

将套接字标记为关闭并释放所有资源。

##### 从套接字接收数据

> **socket.recvfrom(bufsize)**

从套接字接收数据。返回一个元组，包含字节对象和地址。

返回值形式为：`(bytes, address)`

* bytes ：接收数据的字节对象

* address ：发送数据的套接字的地址

##### 设置套接字选项的值

> **socket.setsockopt(level, optname, value)**

设置套接字选项的值。

`level ` :套接字选项级别


* usocket.SOL_SOCKET

`optname`:socket选项

* usocket.SO_REUSEADDR //设置端口复用允许。

* usocket.TCP_KEEPALIVE //设置TCP保活包间隔时间。

value ：既可以是一个整数，也可以是一个表示缓冲区的bytes类对象

示例：

```
#设置端口复用允许
socket.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
#设置TCP保活包间隔时间，value 单位为分钟，范围：1-120
socket.setsockopt(usocket.SOL_SOCKET, usocket.TCP_KEEPALIVE, 1)
```

##### 设置套接字为阻塞模式或者非阻塞模式



> **socket.setblocking(flag)**

设置套接字为阻塞模式或者非阻塞模式。如果标志为false，则将套接字设置为非阻塞，否则设置为阻塞模式。

该方法是某些 `settimeout()` 调用的简写：

`socket.setblocking(True)` 相当于 `socket.settimeout(None)`

`socket.setblocking(False)` 相当于 `socket.settimeout(0)`

##### 设置套接字的发送和接收超时时间

> **socket.settimeout(value)**

设置套接字的发送和接收超时时间，单位秒。

* `value` ：可以是表示秒的非负浮点数，也可以是None。如果给出一个非零值，则[`OSError`](http://docs.micropython.org/en/latest/library/builtins.html#OSError)在该操作完成之前已超过超时时间值，则随后的套接字操作将引发异常。如果给定零，则将套接字置于非阻塞模式。如果未指定，则套接字将处于阻塞模式。

**返回与套接字关联的文件对象**

> **socket.makefile(mode='rb')**

返回与套接字关联的文件对象，返回值类型与指定的参数有关。仅支持二进制模式 (rb和wb)。

##### 获取套接字的状态

> **socket.getsocketsta()**

获取TCP套接字的状态，状态值描述如下：

| 状态值 | 状态        | 描述                                                         |
| ------ | ----------- | ------------------------------------------------------------ |
| 0      | CLOSED      | 套接字创建了，但没有使用这个套接字                           |
| 1      | LISTEN      | 套接字正在监听连接                                           |
| 2      | SYN_SENT    | 套接字正在试图主动建立连接，即发送SYN后还没有收到ACK         |
| 3      | SYN_RCVD    | 套接字正在处于连接的初始同步状态，即收到对方的SYN，但还没收到自己发过去的SYN的ACK |
| 4      | ESTABLISHED | 连接已建立                                                   |
| 5      | FIN_WAIT_1  | 套接字已关闭，正在关闭连接，即发送FIN，没有收到ACK也没有收到FIN |
| 6      | FIN_WAIT_2  | 套接字已关闭，正在等待远程套接字关闭，即在FIN_WAIT_1状态下收到发过去FIN对应的ACK |
| 7      | CLOSE_WAIT  | 远程套接字已经关闭，正在等待关闭这个套接字，被动关闭的一方收到FIN |
| 8      | CLOSING     | 套接字已关闭，远程套接字正在关闭，暂时挂起关闭确认，即在FIN_WAIT_1状态下收到被动方的FIN |
| 9      | LAST_ACK    | 远程套接字已关闭，正在等待本地套接字的关闭确认，被动方在CLOSE_WAIT状态下发送FIN |
| 10     | TIME_WAIT   | 套接字已经关闭，正在等待远程套接字的关闭，即FIN、ACK、FIN、ACK都完毕，经过2MSL时间后变为CLOSED状态 |

注意：

BG95平台不支持该API。
如果用户调用了 `socket.close()` 方法之后，再调用 `socket.getsocketsta()` 会返回-1，因为此时创建的对象资源等都已经被释放。


**socket通信示例**：

```python
'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2020-04-26 09:56:08
@Description: example for module usocket
@FilePath: example_socket_file.py
'''
# 导入usocket模块
import usocket
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Socket_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
socket_log = log.getLogger("SOCKET")

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        socket_log.info('Network connection successful!')

    	# 创建一个socket实例
    	sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    	# 解析域名
    	sockaddr=usocket.getaddrinfo('www.tongxinmao.com', 80)[0][-1]
    	# 建立连接
    	sock.connect(sockaddr)
    	# 向服务端发送消息
    	ret=sock.send('GET /News HTTP/1.1\r\nHost: www.tongxinmao.com\r\nAccept-Encoding: deflate\r\nConnection: keep-alive\r\n\r\n')
    	socket_log.info('send %d bytes' % ret)
    	#接收服务端消息
    	data=sock.recv(256)
    	socket_log.info('recv %s bytes:' % len(data))
    	socket_log.info(data.decode())

    	# 关闭连接
    	sock.close()
    else:
        socket_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

```



#### uio - 输入输出流

uio 模块包含其他类型的stream（类文件）对象和辅助函数。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[io](https://docs.python.org/3.5/library/io.html#module-io)

##### 打开文件

> __fd = uio.open(name, mode=’r’, **kwarg)__

打开文件，内置`open()`函数是该函数的别名。

* `name` ：文件名

* `mode` ：打开模式

- r  只读模式打开文件
  - w  写入模式打开文件，每次写入会覆盖上次写入数据
  - a  只写追加模式打开文件，可连续写入文件数据而不是覆盖数据


* `**kwarg`：可变长参数列表

##### 关闭打开的文件

> **fd.close()**

关闭打开的文件。



#### ustruct - 打包和解压原始数据类型

该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[struct](https://docs.python.org/3.5/library/struct.html#module-struct)

**字节顺序，大小和对齐方式**

默认情况下，C类型以机器的本机格式和字节顺序表示，并在必要时通过跳过填充字节来正确对齐（根据C编译器使用的规则）。根据下表，格式字符串的第一个字符可用于指示打包数据的字节顺序，大小和对齐方式：

| Character | Byte order             | Size     | Alignment |
| --------- | ---------------------- | -------- | --------- |
| `@`       | native                 | native   | native    |
| `=`       | native                 | standard | none      |
| `<`       | little-endian          | standard | none      |
| `>`       | big-endian             | standard | none      |
| `!`       | network (= big-endian) | standard | none      |

**格式化字符表**

| Format | C Type               | Python type | Standard size |
| ------ | -------------------- | ----------- | ------------- |
| `b`    | `signed char`        | integer     | 1             |
| `B`    | `unsigned char`      | integer     | 1             |
| `h`    | `short`              | integer     | 2             |
| `H`    | `unsigned short`     | integer     | 2             |
| `i`    | `int`                | integer     | 4             |
| `I`    | `unsigned int`       | integer     | 4             |
| `l`    | `long`               | integer     | 4             |
| `L`    | `unsigned long`      | integer     | 4             |
| `q`    | `long long`          | integer     | 8             |
| `Q`    | `unsigned long long` | integer     | 8             |
| `f`    | `float`              | float       | 4             |
| `d`    | `double`             | float       | 8             |
| `P`    | `void *`             | integer     | 4             |

默认情况下，C类型以机器的本机格式和字节顺序表示，并在必要时通过跳过填充字节来正确对齐（根据C编译器使用的规则）

##### 返回存放 fmt 需要的字节数

> **ustruct.calcsize(fmt)**

返回存放 fmt 需要的字节数。

* `fmt` ：格式字符的类型，详情见上文格化式字符表

示例：

```
>>> import ustruct
>>> ustruct.calcsize('i')
4
>>> ustruct.calcsize('f')
4
>>> ustruct.calcsize('d')
8
```

##### 按照格式字符串 fmt 压缩参数v1、 v2、…

> **ustruct.pack(fmt, v1, v2, ...)**

按照格式字符串 fmt 压缩参数v1、 v2、…返回值是参数编码后的字节对象。

* `fmt` ：格式字符的类型，详情见上文格化式字符表

##### 根据格式化字符串 fmt 对数据进行解压

> **ustruct.unpack(fmt, data)**

根据格式化字符串 fmt 对数据进行解压，返回值为一个元组。

示例：

```
>>> import ustruct
>>> ustruct.pack('ii', 7, 9)  #打包2两个整数
b'\x07\x00\x00\x00\t\x00\x00\x00'
>>> ustruct.unpack('ii', b'\x07\x00\x00\x00\t\x00\x00\x00')  #解压两个整数
(7, 9)
```

##### 根据格式字符串fmt将值v1、v2、 …打包到从`offset`开始的缓冲区中

> **ustruct.pack_into(fmt, buffer, offset, v1, v2, ...)**

根据格式字符串fmt将值v1、v2、 …打包到从`offset`开始的缓冲区中。从缓冲区的末尾算起，`offset`可能为负。

* `fmt` ：格式字符的类型，详情见上文格化式字符表

##### 根据格式化字符串 `fmt` 解析从 `offest` 开始的数据解压

> **ustruct.unpack_from(fmt, data, offset=0)**

根据格式化字符串 `fmt` 解析从 `offest` 开始的数据解压，从缓冲区末尾开始计数的偏移量可能为负值。返回值是解压值的元组。



#### ujson - JSON编码和解码

ujson 模块实现在Python数据对象和JSON数据格式之间进行转换的功能。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[json](https://docs.python.org/3.5/library/json.html#module-json)

##### 将 `obj` 数据对象转化成 JSON字符串

> **ujson.dump(obj, stream)**

将 `obj` 数据对象转化成 JSON字符串，将其写入到给定的 `stream` 中。

##### 将 `dict` 类型的数据转换成str

> **ujson.dumps(dict)**

将 `dict` 类型的数据转换成str。

##### 解析给定的数据 `stream`

> **ujson.load(stream)**

解析给定的数据 `stream`，将其解释为JSON字符串并反序列化成Python对象。

##### 解析JSON字符串并返回`obj`对象

> **ujson.loads(str)**

解析JSON字符串并返回`obj`对象



**使用示例**

```python
'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module ujson
@FilePath: example_json_file.py
'''

# ujson.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。

import ujson
import log
import utime


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Json_example"
PROJECT_VERSION = "1.0.0"


# 设置日志输出级别
log.basicConfig(level=log.INFO)
ujson_log = log.getLogger("UJSON loads")


if __name__ == '__main__':
    inp = {'bar': ('baz', None, 1, 2)}
    ujson_log.info(type(inp))
    # <class 'dict'>

    # 将Dict转换为json
    s = ujson.dumps(inp)
    ujson_log.info(s)
    ujson_log.info(type(s))
    # {"bar": ["baz", null, 1, 2]}, <class 'str'>

    # 将json转换为Dict
    outp = ujson.loads(s)
    ujson_log.info(outp)
    ujson_log.info(type(outp))
    # ujson.dump()和juson.load()主要用来读写json文件

```



#### utime - 与时间相关功能

utime 模块用于获取当前时间和日期、测量时间间隔和延迟。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[time](https://docs.python.org/3.5/library/time.html#module-time)

##### 格式化时间戳

> **utime.localtime([secs])**

该函数用来将一个以秒表示的时间转换为一个元组，元组包含了了年、月、日、时、分、秒、星期、一年中第几天；如果没有给定参数sec，则使用RTC时间。返回值形式如下：

`(year, month, mday, hour, minute, second, weekday, yearday)`

* `year` ：年份，int型

* `month` ：月份，1~12，int型

* `mday` ：日，当月多少号，1~31，int型

* `hour` ：小时，0~23，int型

* `minute` ：分钟，0~59，int型

* `second` ：秒，0~59，int型

* `weekday` ：星期，周一到周日是0~6，int型

* `yearday` ：一年中的第多少天，int型

示例：

```
>>> import utime
>>> utime.localtime()
(2020, 9, 29, 8, 54, 42, 1, 273)
>>> utime.localtime(646898736)
(2020, 7, 1, 6, 5, 36, 2, 183)
```

##### 反向格式化时间戳

> **utime.mktime(date)**

该函数作用与locatime()相反，它将一个存放在元组中的时间转换为以秒计的时间戳。

示例：

```
>>> import utime
>>> date = (2020, 9, 29, 8, 54, 42, 1, 273)
>>> utime.mktime(date)
1601340882
```

##### 休眠给定秒数的时间

> **utime.sleep(seconds)**

休眠给定秒数的时间。

注意：sleep()函数的调用会导致程序休眠阻塞。

##### 休眠给定毫秒数的时间

> **utime.sleep_ms(ms)**

休眠给定毫秒数的时间。

注意：sleep_ms()函数的调用会导致程序休眠阻塞。

##### 休眠给定微秒的时间

> **utime.sleep_us(us)**

休眠给定微秒的时间。

注意：sleep_us()函数的调用会导致程序休眠阻塞。

##### 返回不断递增的毫秒计数器

> **utime.ticks_ms()**	

返回不断递增的毫秒计数器，在某些值后会重新计数(未指定)。计数值本身无特定意义，只适合用在 `ticks_diff()`函数中。

注意：sleep_us()函数的调用会导致程序休眠阻塞。

##### 返回不断递增的微秒计数器

> **utime.ticks_us()**	

和`ticks_ms()`类似，只是返回微秒计数器。

##### 和 ticks_ms/ticks_us 类似，具有更高精度 (使用 CPU 时钟)

> **utime.ticks_cpu()**	

和 ticks_ms/ticks_us 类似，具有更高精度 (使用 CPU 时钟)。

##### 计算两次调用` ticks_ms()`，`ticks_us()`或 `ticks_cpu()`之间的时间

> **utime.ticks_diff(ticks1, ticks2)**

计算两次调用` ticks_ms()`， `ticks_us()`，或 `ticks_cpu()`之间的时间。因为这些函数的计数值可能会回绕，所以不能直接相减，需要使用 ticks_diff() 函数。“旧” 时间需要在 “新” 时间之前，否则结果无法确定。这个函数不要用在计算很长的时间 (因为 ticks_*() 函数会回绕，通常周期不是很长)。通常用法是在带超时的轮询事件中调用。

示例：

```python
import utime
start = utime.ticks_us()
while pin.value() == 0:
    if utime.ticks_diff(utime.ticks_us(), start) > 500:
        raise TimeoutError
```

##### 返回自纪元以来的秒数

> **utime.time()**	

返回自纪元以来的秒数（以整数形式）。如果未设置RTC，则此函数返回自特定于端口的参考时间点以来的秒数（对于不具有电池后备RTC的嵌入式板，通常是由于加电或复位）。如果要开发可移植的MicroPython应用程序，则不应依赖此功能提供高于秒的精度。如果需要更高的精度，请使用 `ticks_ms()`和`ticks_us()`函数，如果需要日历时间，则 `localtime()`不带参数会更好。

##### 获取时区

> **utime.getTimeZone()**

获取当前时区，单位小时，范围[-12, 12]，负值表示西时区，正值表示东时区，0表示零时区。

##### 设置时区

> **utime.setTimeZone(offset)**

设置时区，单位小时，范围[-12, 12]，负值表示西时区，正值表示东时区，0表示零时区。设置时区后，本地时间会随之变化为对应时区的时间。

**使用示例**

```python
'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module utime
@FilePath: example_utime_loacltime_file.py
'''
import utime
import log


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_localtime_example"
PROJECT_VERSION = "1.0.0"


# 设置日志输出级别
log.basicConfig(level=log.INFO)
time_log = log.getLogger("LocalTime")

if __name__ == '__main__':
    # 获取本地时间，返回元组
    tupe_t = utime.localtime()
    time_log.info(tupe_t)
    # 返回当前时间戳，参数为元组
    t = utime.mktime(utime.localtime())
    time_log.info(t)
    # 休眠sleep示例
    for i in [0, 1, 2, 3, 4, 5]:
        utime.sleep(1)   # 休眠(单位 m)
        time_log.info(i)

    for i in [0, 1, 2, 3, 4, 5]:
        utime.sleep_ms(1000)   # 休眠(单位 ms)
        time_log.info(i)
```



#### sys - 系统相关功能

sys 模块中提供了与QuecPython运行环境有关的函数和变量。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[sys](https://docs.python.org/3.5/library/sys.html#module-sys)

说明：新架构代码升级了MPY的版本，sys变更为usys。导入模块时建议使用以下方式进行导入 

```python
try:
    import usys as sys
except ImportError:
    import sys
```

**常数说明**

> **sys.argv**

当前程序启动的可变参数列表。

> **sys.byteorder**

字节顺序 (‘little’  - 小端， ‘big’ - 大端)。

> **sys.implementation**

返回当前microPython版本信息。对于MicroPython，它具有以下属性：

- name - 字符串“ micropython”
- version - 元组（主要，次要，微型），例如（1、7、0）

建议使用此对象来将MicroPython与其他Python实现区分开。

> **sys.maxsize**

本机整数类型可以在当前平台上保留的最大值，如果它小于平台最大值，则为MicroPython整数类型表示的最大值（对于不支持长整型的MicroPython端口就是这种情况）。

> **sys.modules**

已载入模块的字典。

> **sys.platform**

MicroPython运行的平台。

 > **sys.stdin**

 标准输入（默认是USB虚拟串口，可选其他串口）。

 > **sys.stdout**

 标准输出（默认是USB虚拟串口，可选其他串口）。

> **sys.version**

MicroPython 语言版本，字符串格式。

> **sys.version_info**

MicroPython  语言版本，整数元组格式。



**方法**

> **sys.exit(retval=0)**

使用给定的参数退出当前程序。与此同时，该函数会引发`SystemExit`退出。如果给定了参数，则将其值作为参数赋值给`SystemExit`。



> **sys.print_exception(exc, file=sys.stdout)**

打印异常到文件对象，默认是 sys.stdout，即输出异常信息的标准输出。



#### uzlib - zlib解压缩

uzlib 模块解压缩用[DEFLATE算法](https://en.wikipedia.org/wiki/DEFLATE)压缩的二进制数据 （通常在zlib库和gzip存档器中使用），压缩尚未实现。该模块实现相应CPython模块的子集。更多信息请参阅阅CPython文档：[zlib](https://docs.python.org/3.5/library/zlib.html#module-zlib)

注意：解压缩前，应检查模块内可使用的空间，确保有足够空间解压文件。

##### 返回解压后的 bytes 对象

> **uzlib.decompress(data, wbits=0, bufsize=0)**

返回解压后的 bytes 对象。`wbits`是解压时使用的DEFLATE字典窗口大小（8-15，字典大小是`wbits`值的2的幂）。如果该值为正，则假定`data`为zlib流（带有zlib标头），如果为负，则假定为原始的DEFLATE流。`bufsize`参数是为了与CPython兼容，将被忽略。

##### 创建一个`stream`装饰器

> **class uzlib.DecompIO(stream, wbits=0)**

创建一个`stream`装饰器，该装饰器允许在另一个流中透明地压缩数据。这允许处理数据大于可用堆大小的压缩流。wbits的值除了上面所述的值以外，还可以取值24..31（16 + 8..15），这表示输入流具有gzip标头。



#### _thread - 多线程

_thread 模块提供创建新线程的方法，并提供互斥锁。

##### 获取当前线程号

> **_thread.get_ident()**

获取当前线程号。

##### 获取系统剩余内存大小

> **_thread.get_heap_size()**

获取系统剩余内存大小。

##### 设置创建新线程使用的栈大小

> **_thread.stack_size(size)**

设置创建新线程使用的栈大小（以字节为单位），默认为8448字节，最小8192字节。

##### 创建一个新线程

> **_thread.start_new_thread(function, args)**

创建一个新线程，接收执行函数和被执行函数参数，当 function 函数无参时传入空的元组。返回线程的id。

##### 根据线程id删除一个线程

> **_thread.stop_thread(thread_id)**

删除一个线程，thread_id为创建线程时返回的线程id。当 thread_id为0时则删除当前线程。不可删除主线程。

##### 创建一个互斥锁对象

> **_thread.allocate_lock()**

创建一个互斥锁对象。

示例：

```
import _thread
lock = _thread.allocate_lock()
```

##### 获取锁

> **lock.acquire()**

获取锁，成功返回True，否则返回False。

##### 释放锁

> **lock.release()**

释放锁。

##### 返回锁的状态

> **lock.locked()**

返回锁的状态，True表示被某个线程获取，False则表示没有。

##### 删除锁

> **_thread.delete_lock(lock)**

删除已经创建的锁。



**_thread使用示例**

```python
'''
@Author: Baron
@Date: 2020-06-22
@LastEditTime: 2020-06-22 17:16:20
@Description: example for module _thread
@FilePath: example_thread_file.py
'''
import _thread
import log
import utime


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值
'''
PROJECT_NAME = "QuecPython_Thread_example"
PROJECT_VERSION = "1.0.0"


# 设置日志输出级别
log.basicConfig(level=log.INFO)
thread_log = log.getLogger("Thread")

a = 0
state = 1
state1 = 1
# 创建一个lock的实例
lock = _thread.allocate_lock()

def th_func(delay, id):
	global a
	global state,state1
	while True:
		lock.acquire()  # 获取锁
		if a >= 10:
			thread_log.info('thread %d exit' % id)
			lock.release()  # 释放锁
			if id == 1:
				state = 0
			else:
				state1 = 0
			break
		a += 1
		thread_log.info('[thread %d] a is %d' % (id, a))
		lock.release()  # 释放锁
		utime.sleep(delay)

def th_func1():
	while True:
		thread_log.info('thread th_func1 is running')
		utime.sleep(1)

if __name__ == '__main__':
	for i in range(2):
		_thread.start_new_thread(th_func, (i + 1, i))   # 创建一个线程，当函数无参时传入空的元组
        
	thread_id = _thread.start_new_thread(th_func1, ())   # 创建一个线程，当函数无参时传入空的元组
    
	while state or state1:
		pass
    
	_thread.stop_thread(thread_id)   # 删除线程
	_thread.delete_lock(lock)   # 删除锁
	thread_log.info('thread th_func1 is stopped')
```



#### uhashlib - 哈希算法

模块功能: 实现二进制数据散列算法,目前支持sha256，sha1，MD5。

##### 创建一个SHA256哈希对象

> ​	**hash_obj = uhashlib.sha256(bytes)**

创建一个SHA256哈希对象

* 参数 

| 参数  | 参数类型 | 参数说明                                              |
| ----- | -------- | ----------------------------------------------------- |
| bytes | bytes    | 可选参数，可在创建时传入bytes数据，也可通过update方法 |

* 返回值

SHA256哈希对象

##### 创建一个SHA1哈希对象

> ​	**hash_obj  = uhashlib.sha1(bytes)**

创建一个SHA1哈希对象

* 参数 

| 参数  | 参数类型 | 参数说明                                              |
| ----- | -------- | ----------------------------------------------------- |
| bytes | bytes    | 可选参数，可在创建时传入bytes数据，也可通过update方法 |

* 返回值

SHA1哈希对象

##### 创建一个MD5哈希对象

> ​	**hash_obj  = uhashlib.md5(bytes)**

创建一个MD5哈希对象

* 参数 

| 参数  | 参数类型 | 参数说明                                              |
| ----- | -------- | ----------------------------------------------------- |
| bytes | bytes    | 可选参数，可在创建时传入bytes数据，也可通过update方法 |

* 返回值

MD5哈希对象



**哈希对象方法**

##### 将更多的bytes数据加到散列

> ​	**hash_obj .update(bytes)**

将更多的bytes数据加到散列

* 参数 

| 参数  | 参数类型 | 参数说明         |
| ----- | -------- | ---------------- |
| bytes | bytes    | 需要被加密的数据 |

* 返回值

无

##### 返回通过哈希传递的所有数据的散列

> ​	**hash_obj .digest()**

返回通过哈希传递的所有数据的散列，数据为字节类型。调用此方法后，无法再将更多的数据送入散列。

* 参数 

无

* 返回值

返回加密后字节类型的数据



**使用实例**

```python
import uhashlib
import ubinascii

hash_obj  = uhashlib.sha256()  # 创建hash对象
hash_obj.update(b"QuecPython")
res = hash_obj.digest()
# b"\x1e\xc6gq\xb3\xa9\xac>\xa4\xc4O\x00\x9eTW\x97\xd4.\x9e}Bo\xff\x82u\x89Th\xfe'\xc6\xcd"
# 转成十六进制表示
hex_msg = ubinascii.hexlify(res)
# b'1ec66771b3a9ac3ea4c44f009e545797d42e9e7d426fff8275895468fe27c6cd'
```

