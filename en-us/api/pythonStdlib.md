#### uos - Basic Operating System Services

This module contains functions for file system access and mount. This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [os](https://docs.python.org/3.5/library/os.html#module-os)

##### Remove a file

> **uos.remove(path)** 

Remove a file. Path indicates the file name.

##### Change current directory

> **uos.chdir(path)**

Change current directory. Path indicates the directory name.

##### Get the current directory

> **uos.getcwd()**

Get the current directory.

##### List the given directory

> **uos.listdir( [dir] )**

With no argument, list the current directory. Otherwise list the given directory. dir is an optional Argument that indicates the directory name and defaults to the "/" directory.

* Example:

```
>>> uos.listdir()
[‘file1’, ‘read.txt’, ‘demo.py’]
```

##### Create a new directory

> **uos.mkdir(path)**

Create a new directory. path indicates the directory name to be created.

* Example:

```
>>> uos.mkdir('testdir')
>>> uos.listdir()
[‘file1’, ‘read.txt’, ‘demo.py’, 'testdir']
```

##### Rename a file

> **uos.rename(old_path, new_path)**

Rename a file. old_path indicates old file or old directory, and new_path indicates new file or new directory.

* Example:

```
>>> uos.rename('testdir', 'testdir1')
```

##### Remove the given directory

> **uos.rmdir(path)**

Remove the given directory. path indicates the directory name. 

* Example: 

```
>>> uos.rmdir('testdir')
>>> uos.listdir()
[‘file1’, ‘read.txt’, ‘demo.py’]
```

**List the current directory Arguments**

> **uos.ilistdir( [dir] )**

This function returns an iterator which then yields three tuples corresponding to the entries in the directory that it is listing. dir is an optional Argument and indicates the directory name. With no argument it lists the current directory, otherwise it lists the directory given by *dir*. The tuples have the form`(name, type, inode[, size])`:

* name is a string (or bytes if *dir* is a bytes object) and is the name of the entry;
* type is an integer that specifies the type of the entry, with 0x4000 for directories and 0x8000 for regular files;
* inode is an integer corresponding to the inode of the file, and may be 0 for filesystems that don't have such a notion.
* Some platforms may return a 4-tuple that includes the entry’s *size*. For file entries, *size* is an integer representing the size of the file or -1 if unknown. Its meaning is currently undefined for directory entries.

##### Get the status of a file or directory

> **uos.stat(path)**

Get the status of a file or directory. path indicates the name of a file or directory. The return value is a tuple, and the return value is of the form:

`(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)`

* `mode` – protection bits
* `ino` – number (not implemented, returns 0)
* `dev`  – device (not implemented, returns 0)
* `nlink`  – number of hard links (not implemented, returns 0)
* `uid ` – user ID of owner (not implemented, returns 0)
* `gid`  – group ID of owner (not implemented, returns 0)
* `size`  – size of file in bytes
* `atime`  – time of most recent access
* `mtime`  – time of most recent content modification
* `ctime`  – time of most recent metadata change; the time of creation on others. See the platform documentation for details

##### Get the status of a fileystem

> **uos.statvfs(path)**

Get the status of a fileystem. path indicates the name of a file or directory. Returns a tuple with the filesystem information in the following order:

`(f_bsize, f_frsize, f_blocks, f_bfree, f_bavail, f_files, f_ffree, f_favail, f_flag, f_namemax)`

* `f_bsize` – file system block size, Unit: byte.
* `f_frsize` – fragment size, Unit: byte.
* `f_blocks` – size of fs in f_frsize units
* `f_bfree` – number of free blocks
* `f_bavai` – number of free blocks for unprivileged users
* `f_files`  – number of inodes
* `f_ffree` – number of free inodes
* `f_favail` – number of free inodes for unprivileged users
* `f_flag` – mount flags
* `f_namemax` – maximum filename length


* Example:

```
>>> import uos
>>> res = uos.statvfs("main.py")
>>> print(res)
(4096, 4096, 256, 249, 249, 0, 0, 0, 0, 255)
```

##### Return information about the underlying machine or its operating system

> **uos.uname()**

Return a tuple (possibly a named tuple) containing information about the underlying machine or its operating system.  This interface is different from the official Micropython interface. It returns a tuple of the form:

`(sysname, nodename, release, version, machine)`

* `sysname` – the name of the underlying system, string type
* `nodename` – the network name (can be the same as `sysname`), string type
* `release` – the version of the underlying system, string type
* `version` – the MicroPython version and build date, string type
* `machine` – an identifier for the underlying hardware (eg board, CPU), string type
* `qpyver` – QuecPython short version number, string type


* Example:

```python
>>> import uos
>>> uos.uname()
('sysname=EC600S-CNLB', 'nodename=EC600S', 'release=1.12.0', 'version=v1.12 on 2020-06-23', 'machine=EC600S with QUECTEL', 'qpyver=V0001')
>>> uos.uname()[0].split('=')[1] # access the value of sysname in this way
'EC600S-CNLB'
```



> **uos.uname2()**

Return a tuple (possibly a named tuple) containing information about the underlying machine or its operating system. This interface has the same return form as the official MicroPython interface. Note the difference from the uos.uname() interface. The return value is:

`(sysname='xxx', nodename='xxx', release='xxx', version='xxx', machine='xxx', qpyver='xxx')`

* `sysname` – the name of the underlying system, string type
* `nodename` – the network name (can be the same as `sysname`), string type
* `release` – the version of the underlying system, string type
* `version` – the MicroPython version and build date, string type
* `machine` – an identifier for the underlying hardware (eg board, CPU), string type
* `qpyver` – QuecPython short version number, string type


* Example:

```python
>>> import uos
>>> uos.uname2()
(sysname='EC600S-CNLB', nodename='EC600S', release='1.12.0', version='v1.12 on 2020-06-23', machine='EC600S with QUECTEL', qpyver='V0001')
>>> uos.uname2().sysname  # access the value of sysname in this way
'EC600S-CNLB'
>>> uos.uname2().machine
'EC600S with QUECTEL'
```



##### Return a bytes object with *n* random bytes. 

> **uos.urandom(n)**

Return a bytes object with *n* random bytes. Whenever possible, it is generated by the hardware random number generator.

* Example:

```
>>> import uos
>>> uos.urandom(5)
b'\xb3\xc9Y\x1b\xe9'
```



##### Register storage device - SPI - SD card

At present, it is only supported by ec600n / ec800n platforms.

> **uos.VfsFat(spi_port, spimode, spiclk, spics)**

Initialize SD card and communicate with SD card. Use SPI communication mode.

* Parameters

|Parameter | parameter type | parameter description|
| -------- | -------- | ------------------------------------------------------------ |
| spi_ Port | int | channel selection [0,1]|
|Spimode | int | SPI working mode (mode 0 is the most commonly used): < br / > clock polarity cpol: that is, when SPI is idle, the level of clock signal SCLK (0: idle low level; 1: idle high level) < br / > 0: cpol = 0, CPHA = 0 < br / > 1: cpol = 0, CPHA = 1 < br / > 2: cpol = 1, CPHA = 0 < br / > 3: cpol = 1, CPHA = 1|
|Spiclk | int | clock frequency 0: 812.5khz 1: 1.625mhz 2: 3.25mhz 3: 6.5mhz 4: 13mhz|
|SPICs | int | specifies that the CS chip selection pin is any GPIO. The hardware CS can be connected to the pin specified here or the default SPI CS pin < br / > 1 ~ n: specify pin GPIO1~Pin. Gpion is CS pin|

* Return value

  * Vfsfat object will be returned if successful, and will be stuck if failed.

* Example

```python
>>> cdev = uos.VfsFat(1, 0, 4, 1)
```



##### Register storage device - SDIO - SD card 

At present,it is only supported by EC600U/EC200U platforms.

> **VfsSd(str)**

Initialize SD card Use SDIO interface.

* Parameter

| Parameter | Type | Description                            |
| ---- | -------- | ----------------------------------- |
| str  | str      | pass "sd_fs" |

* Return Value
Return vfs object if the execution is successful, otherwise report error.

- Pin Correspondence

| platform   |                                                          |
| ------ | ------------------------------------------------------------ |
| EC600U | CMD:Pin number 48<br />DATA0:Pin number 39<br />DATA1:Pin number 40<br />DATA2:Pin number 49<br />DATA3:Pin number 号50<br />CLK:Pin number 132 |
| EC200U | CMD:Pin number 33<br />DATA0:Pin number 31<br />DATA1:Pin number 30<br />DATA2:Pin number 29<br />DATA3:Pin number 28<br />CLK:Pin number 32 |

* Exmaple 

```python
>>> from uos import VfsSd
>>> udev = VfsSd("sd_fs")
```

###### Set detection pin

> **set_det(vfs_obj.GPIOn,mode)**

Set the detection pin and mode of SD card insert and plug out detection.

* Parameter

| Parameter          | Type | Description                                                     |
| ------------- | -------- | ------------------------------------------------------------ |
| vfs_obj.GPIOn | int      | GPIO pin number for SD card insert and plug out detection, refer to the definition of Pin module |
| mode          | int      | 0: when inserte the SD card, the detection port is at low level; when plug out the SD card, the detection port is at high level<br />1:when inserte the SD card, the detection port is at high level；when plug out the SD card, the detection port is at low level |

* Return Value

Return 0 if the execution is successful, otherwise return -1.

* Exmaple 

```python
>>> from uos import VfsSd
>>> udev = VfsSd("sd_fs")
>>> uos.mount(udev, '/sd')
>>> udev.set_det(udev.GPIO10,0)#Use gpio10 as the card detection pin, insert the SD card, the detection port is low level, plug out the SD card, the detection port is high level(the actual use depends on the hardware).
```

###### Setting the card insertion and removal callback function

> **set_callback(fun)**

Set the user callback function in case of card insert and plug out event.

* Parameter

| Parameter | Type | Description                                                     |
| ---- | -------- | ------------------------------------------------------------ |
| fun  | function | insertion and removal callback function [ind_type]<br />ind_type: event type，0：plug out 1：insert |

* Return Value

Return 0 if the execution is successful, otherwise return -1.


SD card usage example(SDIO mode)

At present,it is only supported by EC600U/EC200U platforms.

```python
from uos import VfsSd
import ql_fs
udev = VfsSd("sd_fs")
uos.mount(udev, '/sd')
udev.set_det(udev.GPIO10,0)
#file read / write
f = open('/sd/test.txt','w+')
f.write('1234567890abcdefghijkl')
f.close()
uos.listdir('/sd')
f = open('/sd/test.txt','r')
f.read()
f.close()
#card insertion and removal callback function
def call_back(para):
    if(para == 1):
        print("insert")
        print(uos.listdir('/usr'))  
        print(ql_fs.file_copy('/usr/1.txt','/sd/test.txt'))#copy the test.Txt under SD card to 1.txt under usr partition
        print(uos.listdir('/usr'))
    elif(para == 0):
        print("plug out")   
        
udev.set_callback(call_back)
```



##### **Register storage device - SPI NOR FLASH**

At present,it is only supported by EG915U platforms.

> uos.VfsLfs1(readsize,progsize,lookahead,pname,spi_port,spi_clk)

Initialize spi nor flash and Plug-in nor flash communication. Use SPI communication mode.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| readsize  | int  | Reserved, not used yet                                       |
| progsize  | int  | Reserved, not used yet                                       |
| lookahead | int  | Reserved, not used yet                                       |
| pname     | str  | Fixed to "ext_fs". Subsequent expansion                      |
| spi_port  | int  | Supported ports refer to the SPI chapter description         |
| spi_clk   | int  | clock frequency：<br />EG915U：0：6.25M 1:12.5M  2:25M  3:50M  4:3.125M 5:1.5625M  6:781.25K |

* Return value

  VfsLfs1 object will be returned if successful, and OSError 19 will be returned if failed.

* Example

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

  


##### Mount file system

> **uos.mount(vfs_obj, path)**

Mount the underlying file system to VFS.

* Parameters

| Parameter | parameter type | parameter description         |
| --------- | -------------- | ----------------------------- |
| vfs_ Obj  | VFS object     | file system object            |
| Path      | str            | root directory of file system |

* Return Value

  * None

* Example

```python
>>> cdev = uos.VfsFat(1, 0, 4, 1)
>>> uos.mount(cdev, '/sd')
```

-SD card usage example(SPI mode)

  At present, it is only supported by ec600n / ec800n platforms.

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



#### gc - Control the Garbage Collector

This module provides an interface to the optional garbage collector. This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [gc](https://docs.python.org/3.5/library/gc.html#module-gc)

##### Enable automatic garbage collection

> **gc.enable()**

Enable automatic garbage collection.

##### Disable automatic garbage collection

> **gc.disable()**

Disable automatic garbage collection.

##### Run a garbage collection

> **gc.collect()**

Run a garbage collection.

##### Return the number of bytes of heap RAM that are allocated

> **gc.mem_alloc()**

Return the number of bytes of heap RAM that are allocated. This function is MicroPython extension.

##### Return the number of bytes of available heap RAM

> **gc.mem_free()**

Return the number of bytes of available heap RAM, or -1 if this amount is not known. This function is MicroPython extension.



#### ubinascii - Binary/ASCII Conversions

This module implements conversions between binary data and various encodings of it in ASCII form (in both directions). This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [binascii](https://docs.python.org/3.5/library/binascii.html#module-binascii)

##### Decode base64-encoded data

> **ubinascii.a2b_base64(data)**

Decode base64-encoded data, ignoring invalid characters in the input. Returns a bytes object.

##### Encode binary data in base64 format

> **ubinascii.b2a_base64(data)**

Encode binary data in base64 format. Returns the encoded data followed by a newline character, as a bytes object.

##### Convert binary data to hexadecimal representation

> **ubinascii.hexlify(data, [sep])**

Convert binary data to hexadecimal representation. Returns bytes string.

* Example:

```
>>> import ubinascii
# If there is no sep argument
>>> ubinascii.hexlify('\x11\x22123')
b'1122313233'
>>> ubinascii.hexlify('abcdfg')
b'616263646667'
# If the additional argument sep is supplied it is used as a separator between hexadecimal values.
>>> ubinascii.hexlify('\x11\x22123', ' ')
b'11 22 31 32 33'
>>> ubinascii.hexlify('\x11\x22123', ',')
b'11,22,31,32,33'
```

##### Convert hexadecimal data to binary representation

> **ubinascii.unhexlify(data)**

Convert hexadecimal data to binary representation. Returns bytes string.

* Example:

```
>>> import ubinascii
>>> ubinascii.unhexlify('313222')
b'12"'
```



#### ucollections - Collection and Container Types

This module implements advanced collection and container types to hold/accumulate various objects. This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [collections](https://docs.python.org/3.5/library/collections.html#module-collections)

##### Create a new namedtuple container types

> **mytuple = ucollections.namedtuple(name, fields)**

This is factory function to create a new namedtuple type with a specific name and set of fields. A namedtuple is a subclass of tuple which allows to access its fields by numeric index.

* Argument

| Argument | Type  | Description                                                  |
| -------- | ----- | ------------------------------------------------------------ |
| name     | str   | Type name of newly created container                         |
| fields   | tuple | The newly created container type contains fields of subtypes |

* Example：

```
>>> import ucollections
>>> mytuple = ucollections.namedtuple("mytuple", ("id", "name"))
>>> t1 = mytuple(1, "foo")
>>> t2 = mytuple(2, "bar")
>>> print(t1.name)
foo
```

##### Create a deque bidirectional queue

> **dq = ucollections.deque(iterable, maxlen, flag)**

Create a deque bidirectional queue.

* Argument

| Argument | Type  | Description                                                  |
| -------- | ----- | ------------------------------------------------------------ |
| iterable | tuple | iterable must be the empty tuple                             |
| maxlen   | int   | maxlen must be specified and the deque will be bounded to this maximum length. |
| flag     | int   | Optional；0 (default): Do not check whether the queue overflows, and when the maximum length is reached append will discard the previous value;          1：IndexError: full raises when the queue reaches the maximum set length. |

* Returned value

deque objects



##### deque object method

> ​	**dq.append(data)**

Add *x* to the right side of the deque.

* Argument

| Argument | Type       | Description                            |
| -------- | ---------- | -------------------------------------- |
| data     | Basic data | numeric value to be added to the queue |

* Return value

  * None

##### Remove and return an item from the left side of the deque

> ​	**dq.popleft()**

Remove and return an item from the left side of the deque. Raises IndexError if no items are present.

* Argument

  * None

* Return Value

  * Returns the value of pop



* Example:

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



#### urandom - Generate Random Numbers

This module provides random numbers generators.

##### Randomly generate elements in obj

> **urandom.choice(obj)**

Randomly generate elements in obj. The type of obj is string.

* Example:

```
>>> import urandom
>>> urandom.choice("QuecPython")
't'
```

##### Randomly generate a decimal number in the range of k bits

> **urandom.getrandbits(k)**

Randomly generate a decimal number in the range of k bits

```
>>> import urandom
>>> urandom.getrandbits(1)  #1-bit binary bits in the range of 0 ~ 1 (decimal: 0 ~ 1)
1
>>> urandom.getrandbits(1)
0
>>> urandom.getrandbits(8)  #8-bit binary bits ranging from 0000 0000 to 1111 11111 (decimal: 0 ~ 255)
224
```

##### Randomly generate an integer between start and end

> **urandom.randint(start, end)**

Randomly generate an integer between start and end

* Example:

```
>>> import urandom
>>> urandom.randint(1, 4)
4
>>> urandom.randint(1, 4)
2
```

##### Randomly generate a floating point number between 0 and 1

> **urandom.random()**

Randomly generate a floating point number between 0 and 1

* Example:

```
>>> import urandom
>>> urandom.random()
0.8465231
```

##### Randomly generate a positive integer between start and end and increment to step

> **urandom.randrange(start, end, step)**

Randomly generate a positive integer between start and end and increment to step

* Example:

```
>>> import urandom
>>> urandom.randrange(0, 8, 2)
0
>>> urandom.randrange(0, 8, 2)
6
```

##### Specify a random number seed

> **urandom.seed(sed)**

Specifies a random number seed, usually used in conjunction with other random number generation functions.

* Example:

```
>>> import urandom
>>> urandom.seed(20)  #Specify a random number seed
>>> for i in range(0, 15): #Generate a random sequence in the range 0 to 15
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

##### Randomly generates floating point numbers in the range start to end

> **urandom.uniform(start, end)**

Randomly generates floating point numbers in the range start to end.

* Example:

```
>>> import urandom
>>> urandom.uniform(3, 5)
3.219261
>>> urandom.uniform(3, 5)
4.00403
```

**Usage Example**

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
The following two global variables are required, and users can modify the values of the following two global variables according to their actual projects
'''
PROJECT_NAME = "QuecPython_Random_example"
PROJECT_VERSION = "1.0.0"

log.basicConfig(level=log.INFO)
random_log = log.getLogger("random")


if __name__ == '__main__':
    # urandom.randint(start, end)
    # Random between 1 and 4
    num = random.randint(1, 4)
    random_log.info(num)

    # random between 0~1
    num = random.random()
    random_log.info(num)

    # urandom.unifrom(start, end)
    # Generate floating point numbers between start and end
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
    # Randomly generate incremental positive integers from start to end
    num = random.randrange(2, 8, 2)
    random_log.info(num)

    # urandom.choice(obj)
    # Randomly generate the number of elements in an object
    num = random.choice("QuecPython")
    random_log.info(num)

```



#### math - Mathematical Functions

This module provides access to the mathematical functions. This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [math](https://docs.python.org/3.5/library/math.html#module-math)

##### Return x raised to the power y

> **math.pow(x, y)**

Return x raised to the power y. Returned value: floating-point number.

* Example:

```
>>> import math
>>> math.pow(2, 3)
8.0
```

##### Return the inverse cosine of x.

> **math.acos(x)**

Return the inverse cosine of x. Returned value: floating-point number. X is a number between -1 and 1, including -1 and 1. If it is less than -1 or greater than 1, an error will be reported.

* Example:

```
>>> import math
>>> math.acos(0.6)
0.9272952
```

##### Return the inverse sine of x

> **math.asin(x)**

Return the inverse sine of x. Returned value: floating-point number. X is a number between -1 and 1, including -1 and 1. If it is less than -1 or greater than 1, an error will be reported.

* Example:

```
>>> import math
>>> math.asin(-1)
-1.570796
```

##### **Return the inverse tangent of** x

> **math.atan(x)**

Return the inverse tangent of x. Returned value: floating-point number.

* Example:

```
>>> import math
>>> math.atan(-8)
-1.446441
>>> math.atan(6.4)
1.4158
```

##### Return the principal value of the inverse tangent of x and y

> **math.atan2(x, y)**

Return the principal value of the inverse tangent of x and y. Returned value: floating-point number.

* Example:

```
>>> import math
>>> math.atan2(-0.50,0.48)
-0.8058035
>>> math.atan2(7, 9)
0.6610432
```

##### Return an integer, being x rounded towards positive infinity

> **math.ceil(x)**

Return an integer, being x rounded towards positive infinity.

* Example:

```
>>> import math
>>> math.ceil(4.1)
5
```

##### Return x with the sign of y

> **math.copysign(x, y)**

Return x with the sign of y. 0 is valid. Returned value: floating-point number.

* Example:

```
>>> import math
>>> math.copysign(5, 0)
5.0
>>> math.copysign(5, -4)
-5.0
>>> math.copysign(5, 9)
5.0
```

##### Return the cosine of x

> **math.cos(x)**

Return the cosine of x. Returned value: floating-point number, between -1 and 1.

* Example:

```
>>> import math
>>> math.cos(3)
-0.9899925
```

##### Return radians x converted to degrees

> **math.degrees(x)**

Return radians x converted to degrees. Returned value: floating-point number.

* Example:

```
>>> import math
>>> math.degrees(5)
286.4789
>>> math.degrees(math.pi/2)
90.0
```

##### mathematical constant  e

> **math.e**

The mathematical constant e, e is a natural constant.

##### Return the exponential of x

> **math.exp(x)**

Return the exponential of x. Returned value: floating-point number.

* Example:

```
>>> import math
>>> math.exp(1)
2.718282
>>> print(math.e)
2.718282
```

##### Return the absolute value of x

> **math.fabs(x)**

Return the absolute value of x. Returned value: floating-point number.

* Example:

```
>>> import math
>>> math.fabs(-3.88)
3.88
```

##### Return an integer, being x rounded towards negative infinity.

> **math.floor(x)**

Return an integer, being x rounded towards negative infinity.

* Example:

```
>>> import math
>>> math.floor(8.7)
8
>>> math.floor(9)
9
>>> math.floor(-7.6)
-8
```

##### Return the remainder of x/y

> **math.fmod(x, y)**

Return the remainder of x/y. Returned value: floating-point number.

* Example:

```
>>> import math
>>> math.fmod(15, 4)
3.0
>>> math.fmod(15, 3)
0.0
```

##### Return a tuple of the fractional and integer parts of x

> **math.modf(x)**

Return a tuple of the fractional and integer parts of x.

* Example:

```
>>> import math
>>> math.modf(17.592)
(0.5919991, 17.0)
```

##### Returns a tuple (m, e)

> **math.frexp(x)**

Returns a tuple (m, e) calculated by dividing x by 0.5 and 1, respectively, to get a range of values, where the value of 2e is in this range, e takes the maximum integer value that meets the requirements, and then x/(2e) to get the value of m. If X = 0, then both m and e are 0, and the absolute value of m ranges between (0.5, 1), excluding 0.5 and 1.

* Example:

```
>>> import math
>>> math.frexp(52)
(0.8125, 6)
```

##### Return true if x is finite

> **math.isfinite(x)**

Return true if x is finite, false otherwise.

* Example:

```
>>> import math
>>> math.isfinite(8)
True
```

##### Return true if x is infinite

> **math.isinf(x)**

Return true if x is infinite, false otherwise.

* Example:

```
>>> import math
>>> math.isinf(123)
False
```

##### Return true if x is not-a-number

> **math.isnan(x)**

Return true if x is not-a-number, false otherwise.

* Example:

```
>>> import math
>>> math.isnan(23)
False
```

##### Return x*(2**i)

> **math.ldexp(x, exp)**

Return x*(2**i).

* Example:

```
>>> import math
>>> math.ldexp(2, 1)
4.0
```

##### Return the natural logarithm of x

> **math.log(x)**

Return the natural logarithm of x, x > 0, otherwise an error will be reported.

* Example:

```
>>> import math
>>> math.log(2)
0.6931472
```

##### Mathematical constant Pi

> **math.pi**

The mathematical constant Pi (Pi, usually expressed as π).

##### Return degrees x converted to radians

> **math.radians(x)**

Return degrees x converted to radians. Returned value: floating-point number.

* Example:

```
>>> import math
>>> math.radians(90)
1.570796
```

##### Return the sine of x

> **math.sin(x)**

Return the sine of x. The returned value is between -1 and 1.

* Example:

```
>>> import math
>>> math.sin(-18)
0.7509873
>>> math.sin(50)
-0.2623749
```

##### Return the square root of x

> **math.sqrt(x)**

Return the square root of x. Returned value: floating-point number.

* Example:

```
>>> import math
>>> math.sqrt(4)
2.0
>>> math.sqrt(7)
2.645751
```

##### Return the tangent of x

> **math.tan(x)**

Return the tangent of x. Returned value: floating-point number, between -1 and 1.

* Example:

```
>>> import math
>>> math.tan(9)
-0.4523157
```

##### Return an integer, being x rounded towards 0

> **math.trunc(x)**

Return an integer, being x rounded towards 0.

* Example:

```
>>> import math
>>> math.trunc(7.123)
7
```

**Usage Example**

```python
# Example of mathematical operation math function

import math
import log
import utime


'''
The following two global variables are required, and users can modify the values of the following two global variables according to their actual projects
'''
PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"


if __name__ == '__main__':
    # set the log output level
    log.basicConfig(level=log.INFO)
    math_log = log.getLogger("Math")

    # Value after x**y 
    result = math.pow(2,3)
    math_log.info(result)
    # 8.0

    # Take the smallest integer value greater than or equal to x, and return x if x is an integer
    result = math.ceil(4.12)
    math_log.info(result)
    # 5

    # Add the sign of y in front of x, and you can input 0
    result = math.copysign(2,-3)
    math_log.info(result)
    # -2.0

    # Get the cosine of x, x must be radian
    result = math.cos(math.pi/4)
    math_log.info(result)
    # 0.7071067811865476

    # Convert x from radian to angle
    result = math.degrees(math.pi/4)
    math_log.info(result)
    # 45.0

    # e indicates a constant
    result = math.e
    math_log.info(result)
    # 2.718281828459045

    # exp () returns the x power of math.e (whose value is 2.71828)
    result = math.exp(2)
    math_log.info(result)
    # 7.38905609893065

    # fabs () returns the absolute value of x
    result = math.fabs(-0.03)
    math_log.info(result)
    # 0.03

    # floor () takes the largest integer value less than or equal to x, and returns itself if x is an integer
    result = math.floor(4.999)
    math_log.info(result)
    # 4

    # fmod () returns the remainder of x/y, whose value is a floating-point number
    result = math.fmod(20,3)
    math_log.info(result)
    # 2.0

    # frexp () returns a tuple (m, e) calculated by dividing x by 0.5 and 1, respectively, to get a range of values, where the value of 2e is in this range, and e takes the maximum integer value that meets the requirements, and then x/(2e) to get the value of m. If x equals 0, then both m and e are 0, and the absolute value of m ranges between (0.5, 1), excluding 0.5 and 1
    result = math.frexp(75)
    math_log.info(result)
    # (0.5859375, 7)

    # isfinite () returns true if x is not an infinite number, false otherwise
    result = math.isfinite(0.1)
    math_log.info(result)
    # True

    # isinf () returns true if x is positive or negative infinity, false otherwise
    result = math.isinf(234)
    math_log.info(result)
    # False

    # isnan () returns true if x is not a number, false otherwise
    result = math.isnan(23)
    math_log.info(result)
    # False

    # ldexp () returns the value of x* (2**i)
    result = math.ldexp(5,5)
    math_log.info(result)
    # 160.0

    # modf () returns a tuple consisting of the fractional part and the integer part of x
    result = math.modf(math.pi)
    math_log.info(result)
    # (0.14159265358979312, 3.0)

    # Pi: numeric constant, π
    result = math.pi
    math_log.info(result)
    # 3.141592653589793

    # Sin () returns the sine of x (x is the radian)
    result = math.sin(math.pi/4)
    math_log.info(result)
    # 0.7071067811865476

    # sqrt() returns the square root of x
    result = math.sqrt(100)
    math_log.info(result)
    # 10.0

    # tan () returns the tangent of x (x is the radian)
    result = math.tan(math.pi/4)
    math_log.info(result)
    # 0.9999999999999999

    # trunc() returns the integer part of x
    result = math.trunc(6.789)
    math_log.info(result)
    # 6

```



#### usocket - Socket Module

This module provides access to the BSD socket interface. This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [socket](https://docs.python.org/3.5/library/socket.html#module-socket)

##### Create a new socket

> **usocket.socket(af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP)**

Create a new socket using the given address family, socket type and protocol number. Note that specifying *proto* in most cases is not required (and not recommended, as some MicroPython ports may omit `IPPROTO_*` constants). 

**Constant Description**

af - address family

* usocket.AF_INET ：IPV4

* usocket.AF_INET6 ：IPV6

type - socket type

* usocket.SOCK_STREAM ：Streaming socket for TCP

* usocket.SOCK_DGRAM ：Packet socket corresponding to UDP

* usocket.SOCK_RAW ：Raw socket

proto - protocol number

* usocket.IPPROTO_TCP
* usocket.IPPROTO_UDP
* usocket.IPPROTO_TCP_SER : socket for TCP Server

Others

* usocket.SOL_SOCKET - Socket option level

* usocket.SO_REUSEADDR - Allow fast reuse of binding addresses

Example:

```
import usocket
# Creating TCP-based streaming sockets
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
# Creating UDP-based Datagram Sockets
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
# Creating TCP-based server sockets
socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM, usocket.IPPROTO_TCP_SER)
```

##### Translate the host/port argument into a sequence of 5-tuples

> **usocket.getaddrinfo(host, port)**

Translate the host/port argument into a sequence of 5-tuples. The resulting list of 5-tuples has the following structure:

`(family, type, proto, canonname, sockaddr)`



#### Class Socket Methods

##### Bind specified address

> **socket.bind(address)**

Bind the socket to address. The socket must not already be bound. (The format of address depends on the address family)

* `address` : A tuple or list containing addresses and port numbers

Example:

```
# Bind the datacall IP to the server address
socket.bind(("",80))
# Bind a custom IP to the server address
socket.bind(("192.168.0.1",80))
```

#####

##### Enable a server to accept connections


> **socket.listen(backlog)**

Enable a server to accept connections. The maximum number of connections can be specified.

* `backlog` : If backlog is specified, it must be at least 0.

##### Accept a connection

> **socket.accept()**

Accept a connection and return a tuple. The socket must be bound to an address&port and listening for connections. The return value is a pair `(conn, address, port)`

* `conn` : new socket object usable to send and receive data on the connection

* `address` : address bound to the socket on the other end of the connection

##### Connect to a remote socket at *address*

> **socket.connect(address)**

Connect to a remote socket at *address*.

* `address`: A tuple or list containing addresses and port numbers

##### Read up to size bytes from the socket

> **socket.read( [ size ] )**

Read up to size bytes from the socket. Return a bytes object. If *size* is not given, it reads all data available from the socket until EOF. The effect at this time is the same as ` socket.readall () `.

##### Read bytes into the *buf*

> **socket.readinto(buf, [ , nbytes ])**

Read bytes into the *buf*. If *nbytes* is specified then read at most that many bytes. Otherwise, read at most *len(buf)* bytes. Return value: number of bytes read and stored into *buf*.

##### Read a line

> **socket.readline()**

Read a line, ending in a newline character. Return value: the line read.

##### Write the buffer of bytes to the socket

> **socket.write(buf)**

Write the buffer of bytes to the socket. Buf is the data to be written. Return value: number of bytes written.

##### Send data to the socket

> **socket.send(bytes)**

Send data to the socket. Returns number of bytes sent.

* `bytes` : bytes data type

##### Send all data to the socket

> **socket.sendall(bytes)**

Send all data to the socket. Unlike [`send()`](https://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.send), this method will try to send all of data, by sending data chunk by chunk consecutively.

Note: The behaviour of this method on non-blocking sockets is undefined. Due to this, on MicroPython, it's recommended to use [`write()`](https://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.write) method instead, which has the same "no short writes" policy for blocking sockets, and will return number of bytes sent on non-blocking sockets.

* `bytes` ：bytes data type

##### Send data to the socket

> **socket.sendto(bytes, address)**

Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by *address*.

* `bytes` : bytes data type

* `address` ：Tuples or lists containing addresses and port numbers

##### Receive data from the socket

> **socket.recv(bufsize)**

Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by bufsize.

* `bufsize` : The maximum amount of data to be received at once

##### Mark the socket closed and release all resources

> **socket.close()**

Mark the socket closed and release all resources.

##### Receive data from the socket

> **socket.recvfrom(bufsize)**

Receive data from the socket. Returns a tuple containing bytes and addresses.

Returned value: `(bytes, address)`

* bytes: a bytes object representing the data received
* address: the address of the socket sending the data

##### Set the value of the given socket option

> **socket.setsockopt(level, optname, value)**

Set the value of the given socket option.

* `level`: socket option level
* `optname`: socket option
* `value`: either an integer or a bytes class object representing a buffer


* Example:

```
socket.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
```

##### Set blocking or non-blocking mode of the socket

> **socket.setblocking(flag)**

Set blocking or non-blocking mode of the socket: if flag is false, the socket is set to non-blocking, else to blocking mode.

This method is a shorthand for certain [`settimeout()`](https://docs.micropython.org/en/latest/library/usocket.html#usocket.socket.settimeout) calls:

`socket.setblocking(True)` is equivalent to  `socket.settimeout(None)`

`socket.setblocking(False)` is equivalent to  `socket.settimeout(0)`

##### Set a timeout on blocking socket operations

> **socket.settimeout(value)**

Set a timeout on blocking socket operations. Unit: second.

* `value` : a nonnegative floating point number expressing seconds, or None. If a non-zero value is given, subsequent socket operations will raise an [`OSError`](https://docs.micropython.org/en/latest/library/builtins.html#OSError) exception if the timeout period value has elapsed before the operation has completed. If zero is given, the socket is put in non-blocking mode. If None is given, the socket is put in blocking mode.

**Return a file object associated with the socket**

> **socket.makefile(mode='rb')**

Return a file object associated with the socket. The exact returned type depends on the arguments given to makefile(). The support is limited to binary modes only (‘rb’ and ‘wb’).

##### Get socket status

> **socket.getsocketsta()**

Get socket status. The status values are described as follows:

| Status Value | Status      | Description                                                  |
| ------------ | ----------- | ------------------------------------------------------------ |
| 0            | CLOSED      | A socket is created but not used.                            |
| 1            | LISTEN      | The socket is listening for a connection.                    |
| 2            | SYN_SENT    | The socket is trying to actively establish a connection, that is, it has not received an ACK after sending SYN. |
| 3            | SYN_RCVD    | The socket is in the initial synchronization state of the connection, that is, it has received the SYN from the other party, but has not yet received the ACK of the SYN sent by itself. |
| 4            | ESTABLISHED | Connection established.                                      |
| 5            | FIN_WAIT_1  | Socket closed, closing connection, sending FIN, neither ACK nor FIN received. |
| 6            | FIN_WAIT_2  | The socket is closed, waiting for the remote socket to close, that is, the ACK corresponding to the sent FIN is received in the FIN_WAIT_1 state. |
| 7            | CLOSE_WAIT  | The remote socket has been closed, waiting to close this socket, and the passively closed party receives FIN. |
| 8            | CLOSING     | The socket is closed, the remote socket is closing, the closing acknowledgement is temporarily pending, that is, the FIN of the passive party is received in the FIN_WAIT_1 state. |
| 9            | LAST_ACK    | The remote socket is closed, waiting for the closing confirmation of the local socket, and the passive party sends FIN in the CLOSE_WAIT state. |
| 10           | TIME_WAIT   | The socket has been closed, waiting for the remote socket to close, that is, FIN, ACK, FIN, ACK are all finished, and become CLOSED state after 2MSL time. |

Note:

The BG95 platform does not support this API.

If the user calls the ` socket.getsocketsta () ` after calling the ` socket.close () ` method, it returns-1 because the object resources and so on created at this point have been freed.

**Socket Communication Example**：

```python
'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2020-04-26 09:56:08
@Description: example for module usocket
@FilePath: example_socket_file.py
'''
# import usocket module
import usocket
import log
import utime
import checkNet


'''
The following two global variables are required, and users can modify the values of the following two global variables according to their actual projects
'''
PROJECT_NAME = "QuecPython_Socket_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# Set the log output level
log.basicConfig(level=log.INFO)
socket_log = log.getLogger("SOCKET")

if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
        socket_log.info('Network connection successful!')

    	# Create a Socket instance
    	sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    	# Resolve domain name
    	sockaddr=usocket.getaddrinfo('www.tongxinmao.com', 80)[0][-1]
    	# Establish a connection
    	sock.connect(sockaddr)
    	# Send a message to the server
    	ret=sock.send('GET /News HTTP/1.1\r\nHost: www.tongxinmao.com\r\nAccept-Encoding: deflate\r\nConnection: keep-alive\r\n\r\n')
    	socket_log.info('send %d bytes' % ret)
    	#Receive server-side messages
    	data=sock.recv(256)
    	socket_log.info('recv %s bytes:' % len(data))
    	socket_log.info(data.decode())

    	# Close the connection
    	sock.close()
    else:
        socket_log.info('Network connection failed! stagecode = {}, subcode = {}'.format(stagecode, subcode))

```



#### uio - input/output streams

This module contains additional types of [`stream`](https://docs.micropython.org/en/latest/reference/glossary.html#term-stream) (file-like) objects and helper functions. This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [io](https://docs.python.org/3.5/library/io.html#module-io)

##### Open a file

> __fd = uio.open(name, mode=’r’, **kwarg)__

Open a file. Builtin `open()` function is aliased to this function. 

* `name`: file name

* `mode`: open mode

- r  Open the file in read-only mode
  - w  Write mode opens the file, and each write overwrites the last write data
  - a  Write-only append mode opens a file, which can continuously write file data instead of overwriting data


* `**kwarg`: Variable length argument list

##### Close an open file

> **fd.close()**

Close an open file.



#### ustruct - pack and unpack primitive data types

This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [struct](https://docs.python.org/3.5/library/struct.html#module-struct)

**Byte order, size, and alignment**

By default, C types are represented in the machine's native format and byte order, and are correctly aligned by skipping padding bytes if necessary (according to the rules used by the C compiler). According to the following table, the first character of the format string can be used to indicate the byte order, size, and alignment of the packaged data:

| Character | Byte order             | Size     | Alignment |
| --------- | ---------------------- | -------- | --------- |
| `@`       | native                 | native   | native    |
| `=`       | native                 | standard | none      |
| `<`       | little-endian          | standard | none      |
| `>`       | big-endian             | standard | none      |
| `!`       | network (= big-endian) | standard | none      |

**** Formatted Character Table****

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

By default, C types are represented in the machine's native format and byte order, and are correctly aligned by skipping padding bytes if necessary (according to the rules used by the C compiler)

##### Return the number of bytes needed to store the given *fmt*

> **ustruct.calcsize(fmt)**

Return the number of bytes needed to store the given *fmt*.

* `fmt`: For the types of format characters, see the Formatted Character Table above for details

* Example:

```
>>> import ustruct
>>> ustruct.calcsize('i')
4
>>> ustruct.calcsize('f')
4
>>> ustruct.calcsize('d')
8
```

##### Pack the values *v1*, *v2*, … according to the format string *fmt*

> **ustruct.pack(fmt, v1, v2, ...)**

Pack the values *v1*, *v2*, … according to the format string *fmt*. The return value is a bytes object encoding the values.

* `fmt`: For the types of format characters, see the Formatted Character Table above for details

> **ustruct.unpack(fmt, data)**

Unpack from the *data* according to the format string *fmt*. The return value is a tuple of the unpacked values.

* Example:

```
>>> import ustruct
>>> ustruct.pack('ii', 7, 9)  #pack two integers
b'\x07\x00\x00\x00\t\x00\x00\x00'
>>> ustruct.unpack('ii', b'\x07\x00\x00\x00\t\x00\x00\x00')  #unpack two integers
(7, 9)
```

##### Pack the values *v1*, *v2*, … according to the format string *fmt* into a *buffer* starting at *offset*

> **ustruct.pack_into(fmt, buffer, offset, v1, v2, ...)**

Pack the values *v1*, *v2*, … according to the format string *fmt* into a *buffer* starting at *offset*. *offset* may be negative to count from the end of *buffer*.

* `fmt`: For the types of format characters, see the Formatted Character Table above for details

##### Unpack from the *data* starting at *offset* according to the format string *fmt*

> **ustruct.unpack_from(fmt, data, offset=0)**

Unpack from the *data* starting at *offset* according to the format string *fmt*. *offset* may be negative to count from the end of *buffer*. The return value is a tuple of the unpacked values.



#### ujson - JSON encoding and decoding

This modules allows to convert between Python objects and the JSON data format. This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [json](https://docs.python.org/3.5/library/json.html#module-json)

##### Serialise *obj* to a JSON string

> **ujson.dump(obj, stream)**

Serialise *obj* to a JSON string, writing it to the given *stream*.

##### Convert data of type ` dict ` to str

> **ujson.dumps(dict)**

Convert data of type ` dict ` to str.

##### Parse the given *stream*

> **ujson.load(stream)**

Parse the given *stream*, interpreting it as a JSON string and deserialising the data to a Python object.

##### Parse the JSON *str* and return an object

> **ujson.loads(str)**

Parse the JSON *str* and return an object.



**Usage Example**

```python
'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module ujson
@FilePath: example_json_file.py
'''

# ujson.loads is used to decode JSON data. This function returns the data type of the Python field.

import ujson
import log
import utime


'''
The following two global variables are required, and users can modify the values of the following two global variables according to their actual projects
'''
PROJECT_NAME = "QuecPython_Json_example"
PROJECT_VERSION = "1.0.0"


# Set the log output level
log.basicConfig(level=log.INFO)
ujson_log = log.getLogger("UJSON loads")


if __name__ == '__main__':
    inp = {'bar': ('baz', None, 1, 2)}
    ujson_log.info(type(inp))
    # <class 'dict'>

    # Convert Dict to json
    s = ujson.dumps(inp)
    ujson_log.info(s)
    ujson_log.info(type(s))
    # {"bar": ["baz", null, 1, 2]}, <class 'str'>

    # Convert json to Dict
    outp = ujson.loads(s)
    ujson_log.info(outp)
    ujson_log.info(type(outp))
    # ujson.dump () and juson.load () are mainly used to read and write json files

```



#### utime - time related functions

This module provides functions for getting the current time and date, measuring time intervals, and for delays. This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation:  [time](https://docs.python.org/3.5/library/time.html#module-time)

##### Format timestamp

> **utime.localtime([secs])**

Convert the time *secs* expressed in seconds since the Epoch (see above) into an 8-tuple which contains: `(year, month, mday, hour, minute, second, weekday, yearday)` If *secs* is not provided or None, then the current time from the RTC is used. The format of the entries in the 8-tuple are:

`(year, month, mday, hour, minute, second, weekday, yearday)`

* `year`  includes the century, integer type
* `month` is 1-12, integer type
* `mday`  is 1-31, integer type
* `hour`  is 0-23, integer type
* `minute`  is 0-59, integer type
* `second` is 0-59, integer type
* `weekday`  is 0-6 for Mon-Sun, integer type
* `yearday`  is 1-366, integer type


* Example:

```
>>> import utime
>>> utime.localtime()
(2020, 9, 29, 8, 54, 42, 1, 273)
>>> utime.localtime(646898736)
(2020, 7, 1, 6, 5, 36, 2, 183)
```

##### Reverse format timestamp

> **utime.mktime(date)**

This is inverse function of localtime. It’s argument is a full 8-tuple which expresses a time as per localtime.

* Example:

```
>>> import utime
>>> date = (2020, 9, 29, 8, 54, 42, 1, 273)
>>> utime.mktime(date)
1601340882
```

##### Sleep for the given number of seconds

> **utime.sleep(seconds)**

Sleep for the given number of seconds.

Note: The call of sleep () function will cause the program to sleep and block.

##### Delay for given number of milliseconds

> **utime.sleep_ms(ms)**

Delay for given number of milliseconds.

Note: The call of sleep () function will cause the program to sleep and block.

##### Delay for given number of microseconds

> **utime.sleep_us(us)**

Delay for given number of microseconds.

Note: The call of sleep () function will cause the program to sleep and block.

##### Returns an increasing millisecond counter

> **utime.ticks_ms()**	

Returns an increasing millisecond counter. Recount after certain values (unspecified). The count value itself has no specific meaning and is only suitable for use in the ` ticks_diff () ` function.

Note: The call of sleep () function will cause the program to sleep and block.

##### Returns an increasing microsecond counter

> **utime.ticks_us()**	

Just like [`ticks_ms()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_ms) above, but in microseconds.

##### Similar to [`ticks_ms()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_ms) and [`ticks_us()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_us), but with the highest possible resolution in the system (CPU clocks)

> **utime.ticks_cpu()**	

Similar to [`ticks_ms()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_ms) and [`ticks_us()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_us), but with the highest possible resolution in the system (CPU clocks).

##### Measure ticks difference between values returned from [`ticks_ms()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_ms), [`ticks_us()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_us), or [`ticks_cpu()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_cpu) functions

> **utime.ticks_diff(ticks1, ticks2)**

Measure ticks difference between values returned from [`ticks_ms()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_ms), [`ticks_us()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_us), or [`ticks_cpu()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_cpu) functions. However, values returned by [`ticks_ms()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_ms), etc. functions may wrap around, so directly using subtraction on them will produce incorrect result. That is why [`ticks_diff()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_diff) is needed. The "old" time needs to precede the "new" time, otherwise the result cannot be determined. Don't use this function for a long time (because the ticks_* () function will wrap around, and usually the period is not very long). Usually, it is called in a polling event with a timeout.

* Example:

```python
import utime
start = utime.ticks_us()
while pin.value() == 0:
    if utime.ticks_diff(utime.ticks_us(), start) > 500:
        raise TimeoutError
```

##### Returns the number of seconds since the Epoch

> **utime.time()**	

Returns the number of seconds, as an integer, since the Epoch。If an RTC is not set, this function returns number of seconds since a port-specific reference point in time (for embedded boards without a battery-backed RTC, usually since power up or reset). If you want to develop portable MicroPython application, you should not rely on this function to provide higher than second precision. If you need higher precision, use the [`ticks_ms()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_ms) and [`ticks_us()`](https://docs.micropython.org/en/latest/library/utime.html#utime.ticks_us) functions. If you need calendar time, [`localtime()`](https://docs.micropython.org/en/latest/library/utime.html#utime.localtime) without an argument is a better choice. 

**Usage Example**

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
The following two global variables are required, and users can modify the values of the following two global variables according to their actual projects
'''
PROJECT_NAME = "QuecPython_localtime_example"
PROJECT_VERSION = "1.0.0"


# Set the log output level
log.basicConfig(level=log.INFO)
time_log = log.getLogger("LocalTime")

if __name__ == '__main__':
    # Get the local time and return the tuple
    tupe_t = utime.localtime()
    time_log.info(tupe_t)
    # Return the current timestamp with tuple as the argument
    t = utime.mktime(utime.localtime())
    time_log.info(t)
    # sleep examplee
    for i in [0, 1, 2, 3, 4, 5]:
        utime.sleep(1)   # sleep (Unit: m)
        time_log.info(i)

    for i in [0, 1, 2, 3, 4, 5]:
        utime.sleep_ms(1000)   # sleep (Unit: ms)
        time_log.info(i)
```



#### sys - **sys**tem specific functions

This module provide functions and variables related to the QuecPython runtime environment. This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [sys](https://docs.python.org/3.5/library/sys.html#module-sys)

Note: The new architecture code upgrades the version of MPY from sys to usys. You are advised to use the following methods to import modules

```python
try:
    import usys as sys
except ImportError:
    import sys
```

**Constants**

> **sys.argv**

A mutable list of arguments the current program was started with.

> **sys.byteorder**

The byte order of the **sys**tem (`"little"` or `"big"`).

> **sys.implementation**

Object with information about the current Python implementation. For MicroPython, it has following attributes:

- name - string  “ micropython”
- version - tuple (major, minor, micro), e.g. (1, 7, 0)

This object is the recommended way to distinguish MicroPython from other Python implementations.

> **sys.maxsize**

Maximum value which a native integer type can hold on the current platform, or maximum value representable by MicroPython integer type, if it’s smaller than platform max value (that is the case for MicroPython ports without long int support).

> **sys.modules**

Dictionary of loaded modules.

> **sys.platform**

The platform that MicroPython is running on.

> **sys.stdin**

Standard input (The default is USB virtual serial port, and other serial ports can be selected).

> **sys.stdout**

Standard output (The default is USB virtual serial port, and other serial ports can be selected).

MicroPython language version, as a string.

> **sys.version_info**

MicroPython  language version, as a tuple of ints.



**Functions**

> **sys.exit(retval=0)**

Terminate current program with a given exit code. Underlyingly, this function raise as [`SystemExit`](https://docs.micropython.org/en/latest/library/builtins.html#SystemExit) exception. If an argument is given, its value given as an argument to [`SystemExit`](https://docs.micropython.org/en/latest/library/builtins.html#SystemExit).



> **sys.print_exception(exc, file=sys.stdout)**

Print exception with a traceback to a file-like object *file* (or [`usys.stdout`](https://docs.micropython.org/en/latest/library/usys.html?highlight=sys#usys.stdout) by default).

#### uzlib - zlib decompression

This module allows to decompress binary data compressed with [DEFLATE algorithm](https://en.wikipedia.org/wiki/DEFLATE) (commonly used in zlib library and gzip archiver). Compression is not yet implemented. This module implements a subset of the corresponding [CPython](https://docs.micropython.org/en/latest/reference/glossary.html#term-CPython) module, as described below. For more information, refer to the original CPython documentation: [zlib](https://docs.python.org/3.5/library/zlib.html#module-zlib)

Note: Before decompression, check the available space in the module to make sure there is enough space to decompress the file.

##### Return decompressed *data* as bytes. 

> **uzlib.decompress(data, wbits=0, bufsize=0)**

Return decompressed *data* as bytes. *wbits* is DEFLATE dictionary window size used during compression (8-15, the dictionary size is power of 2 of that value). Additionally, if value is positive, *data* is assumed to be zlib stream (with zlib header). Otherwise, if it’s negative, it’s assumed to be raw DEFLATE stream. *bufsize* Argument is for compatibility with CPython and is ignored.

##### Create a [`stream`](https://docs.micropython.org/en/latest/reference/glossary.html#term-stream) wrapper

> **class uzlib.DecompIO(stream, wbits=0)**

Create a [`stream`](https://docs.micropython.org/en/latest/reference/glossary.html#term-stream) wrapper which allows transparent decompression of compressed data in another *stream*. This allows to process compressed streams with data larger than available heap size. In addition to values described in [`decompress()`](https://docs.micropython.org/en/latest/library/uzlib.html#uzlib.decompress), *wbits* may take values 24..31 (16 + 8..15), meaning that input stream has gzip header.



#### _thread - multithreading support

This module provides a way to create a new thread and provides a mutex.

##### Return the ‘thread identifier’ of the current thread

> **_thread.get_ident()**

Return the ‘thread identifier’ of the current thread.

##### Get the remaining memory size of the system

> **_thread.get_heap_size()**

Get the remaining memory size of the system.

##### Return the thread stack size used when creating new threads

> **_thread.stack_size(size)**

Return the thread stack size used when creating new threads. (In bytes), the default is 8K.

##### Start a new thread

> **_thread.start_new_thread(function, args)**

Creates a new thread, receives the Arguments of the executing function and the executed function, and passes in an empty tuple when the function has no arguments. Returns the id of the thread.

##### Stop a thread according to the thread id

> **_thread.stop_thread(thread_id)**

Stop a thread, thread_id is the thread id returned when the thread was created. When thread_id is 0, the current thread is deleted. You cannot delete the main thread.

##### Create a mutex object

> **_thread.allocate_lock()**

Create a mutex object.

* Example:

```
import _thread
lock = _thread.allocate_lock()
```

##### Acquire the lock

> **lock.acquire()**

Acquire the lock. The return value is True if the lock is acquired successfully, False if not.

##### Releases the lock

> **lock.release()**

Releases the lock.

##### Return the status of the lock

> **lock.locked()**

Return the status of the lock: True if it has been acquired by some thread, False if not.



**Usage Example**

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
The following two global variables are required, and users can modify the values of the following two global variables according to their actual projects
'''
PROJECT_NAME = "QuecPython_Thread_example"
PROJECT_VERSION = "1.0.0"


# Set the log output level
log.basicConfig(level=log.INFO)
thread_log = log.getLogger("Thread")

a = 0
state = 1
# Create an instance of lock
lock = _thread.allocate_lock()

def th_func(delay, id):
	global a
	global state
	while True:
		lock.acquire()  # acquire the lock
		if a >= 10:
			thread_log.info('thread %d exit' % id)
			lock.release()  # release the lock
			state = 0
			break
		a += 1
		thread_log.info('[thread %d] a is %d' % (id, a))
		lock.release()  # release the lock
		utime.sleep(delay)

def th_func1():
	while True:
		thread_log.info('thread th_func1 is running')
		utime.sleep(1)

if __name__ == '__main__':
	for i in range(2):
		_thread.start_new_thread(th_func, (i + 1, i))   # Creates a thread that passes in an empty tuple when the function has no arguments
        
	thread_id = _thread.start_new_thread(th_func1, ())   # Creates a thread that passes in an empty tuple when the function has no arguments
    
	while state:
		pass
    
	_thread.stop_thread(thread_id)
	thread_log.info('thread th_func1 is stopped')
```



#### uhashlib -hashing algorithms

This module implements binary data hashing algorithms. SHA256, SHA1 and MD5 are supported currently.目前支持sha256，sha1，MD5。

##### Create an SHA256 hasher object

> ​	**hash_obj = uhashlib.sha256(bytes)**

Create an SHA256 hasher object

* Argument

| Argument | Type  | Description                                                  |
| -------- | ----- | ------------------------------------------------------------ |
| bytes    | bytes | Optional. Bytes data can be imported at creation time, or through the **update**. |

* Return Value

  * SHA256 hasher object

##### Create an SHA1 hasher object

> ​	**hash_obj  = uhashlib.sha1(bytes)**

Create an SHA1 hasher object.

* Argument

| Argument | Type  | Description                                                  |
| -------- | ----- | ------------------------------------------------------------ |
| bytes    | bytes | Optional. Bytes data can be imported at creation time, or through the **update**. |

* Return Value

  * SHA1 hasher object

##### Create an MD5 hasher object

> ​	**hash_obj  = uhashlib.md5(bytes)**

Create an MD5 hasher object

* Argument

| Argument | Type  | Description                                                  |
| -------- | ----- | ------------------------------------------------------------ |
| bytes    | bytes | Optional. Bytes data can be imported at creation time, or through the **update**. |

* Return Value

  * MD5 hasher object



**Methods**

##### Feed more bytes data into hash

> ​	**hash_obj .update(bytes)**

Feed more bytes data into hash

* Argument

| Argument | Type  | Description          |
| -------- | ----- | -------------------- |
| bytes    | bytes | Data to be encrypted |

* Return Value

  * None

##### Return hash for all data passed through hash

> ​	**hash_obj .digest()**

Return hash for all data passed through hash, as a bytes object. After this method is called, more data cannot be fed into the hash any longer.

* Argument

  * None

* Return Value

  * Returns encrypted data of byte type



**Usage Example**

```python
import uhashlib
import ubinascii

hash_obj  = uhashlib.sha256()  # Create hash object
hash_obj.update(b"QuecPython")
res = hash_obj.digest()
# b"\x1e\xc6gq\xb3\xa9\xac>\xa4\xc4O\x00\x9eTW\x97\xd4.\x9e}Bo\xff\x82u\x89Th\xfe'\xc6\xcd"
# Convert to hexadecimal
hex_msg = ubinascii.hexlify(res)
# b'1ec66771b3a9ac3ea4c44f009e545797d42e9e7d426fff8275895468fe27c6cd'
```

