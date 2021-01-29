# **QuecPython低功耗使用说明**

文档主要基于EC600S介绍如何使用QuecPython\_低功耗模式pm，通常便携式、移动式产品都是电池设计方案，需要整体上节省功耗，加强续航能力。通过本文你将了解到pm模块的所有设置参数及使用方法。

##  硬件描述

模块内置低功耗模式，只要软件控制，无需额外的电路。

##  软件设计

1.  函数原型create_wakelock(lock_name,
    name_size)，成功返回wakelock的标识id，否则返回-1。

### 创建锁

>   lpm_fd = pm.create_wakelock(lock_name, name_size)

| 参数      | 参数类型 | 参数说明        |
|-----------|----------|-----------------|
| lock_name | string   | 自定义lock名    |
| name_size | int      | lock_name的长度 |

1.  函数原型delete_wakelock(lpm_fd)，成功返回0。

### 删除锁

>   pm.delete_wakelock(lpm_fd)

| 参数   | 类型 | 说明                   |
|--------|------|------------------------|
| lpm_fd | int  | 需要删除的锁对应标识id |

1.  函数原型wakelock_lock(lpm_fd)，成功返回0，否则返回-1。

### 加锁

>   pm.wakelock_lock(lpm_fd)

| 参数   | 类型 | 说明                             |
|--------|------|----------------------------------|
| lpm_fd | int  | 需要执行加锁操作的wakelock标识id |

1.  函数原型wakelock_unlock(lpm_fd)，成功返回0，否则返回-1。

### 释放锁

>   pm.wakelock_unlock(lpm_fd)

| 参数   | 类型 | 说明                               |
|--------|------|------------------------------------|
| lpm_fd | int  | 需要执行释放锁操作的wakelock标识id |

1.  函数原型autosleep(sleep_flag)，成功返回0。

### 自动休眠

>   pm.autosleep(sleep_flag)

| 参数       | 类型 | 说明                           |
|------------|------|--------------------------------|
| sleep_flag | int  | 0，关闭自动休眠；1开启自动休眠 |

1.  函数原型get_wakelock_num()，返回锁的数量。

### 获取已创建的锁数量

>   pm.get_wakelock_num()

## 交互操作

使用QPYcom工具和模组进行交互，示例如下：

<span><div style="text-align: center;">
![](media/079186e2c37f4af6a3c3d52c58a77644.png)

</div></span>

注意：

1.  import pm即为让pm模块在当前空间可见。

2.  只有import pm模块，才能使用pm内的函数和变量。

## 下载验证

下载.py文件到模组运行，代码如下：

```python
import pm
import utime

lpm_fd = pm.create_wakelock("test_lock", len("test_lock"))
pm.autosleep(1)

while 1:
    print("sleep")
    utime.sleep(5)
    res = pm.wakelock_lock(lpm_fd)
    print(res)
    print("ql_lpm_idlelock_lock, g_c1_axi_fd = %d" %lpm_fd)
    print("not sleep")
    utime.sleep(5)
    res = pm.wakelock_unlock(lpm_fd)
    print(res)
    print("ql_lpm_idlelock_unlock, g_c1_axi_fd = %d" % lpm_fd)
    num = pm.get_wakelock_num()
    print(num)

```

## 配套代码


<!-- * [下载代码](code/pm.py) -->
 <a href="zh-cn/QuecPythonSub/code/pm.py" target="_blank">下载代码</a>

## 专业名词解释

>   **加锁**：不允许模组进入低功耗模式

>   **释放锁**：和加锁相对，允许模组进入低功耗模式
