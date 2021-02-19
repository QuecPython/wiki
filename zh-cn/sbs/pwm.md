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



#### PWM执行示例

PWM流程的脚本命令汇总如下：

```python
from misc import PWM
pwm1 = PWM(PWM.PWM0,PWM.ABOVE_MS, 1, 2)
pwm1 = PWM(PWM.PWM0,PWM.ABOVE_1US, 100, 200)
pwm1 = PWM(PWM.PWM0,PWM.ABOVE_10US, 100, 200)
```

#### 附录术语缩写

表 1 ：术语缩写

| 缩写 | 英文全称               | 中文全称     |
| ---- | ---------------------- | ------------ |
| PWM  | Pulse Width Modulation | 脉冲宽度调制 |

