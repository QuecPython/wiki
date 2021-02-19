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