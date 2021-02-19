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