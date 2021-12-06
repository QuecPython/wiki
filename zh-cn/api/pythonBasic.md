### 内置函数

Python 解释器内置了很多函数和类型，您可以在任何时候使用它们，以下按字母表顺序列出它们。更多信息请参阅CPython文档：[Built-in Functions](https://docs.python.org/3.5/library/functions.html)

|           |               | 内置函数     |                |            |
| --------- | ------------- | ------------ | -------------- | ---------- |
| abs()     | all()         | any()        | bin()          | callable() |
| chr()     | classmethod() | compile()    | delattr()      | dir()      |
| divmod()  | enumerate()   | eval()       | exec()         | filter()   |
| getattr() | globals()     | hasattr()    | hash()         | hex()      |
| id()      | input()       | isinstance() | issubclass()   | iter()     |
| len()     | locals()      | map()        | max()          | min()      |
| next()    | oct()         | open()       | ord()          | pow()      |
| print()   | property()    | range()      | repr()         | reversed() |
| round()   | setattr()     | sorted()     | staticmothed() | sum()      |
| super()   | type()        | zip()        |                |            |



### 内置常量

有少数的常量存在与内置命名空间中，如下表所示。更多信息请参阅阅CPython文档：[Built-in Constants](https://docs.python.org/3.5/library/constants.html)

| 内置常量       |                                                              |
| -------------- | ------------------------------------------------------------ |
| False          | bool 类型的假值                                              |
| True           | bool 类型的真值                                              |
| None           | Nonetype类型的唯一值                                         |
| \_\_debug\_\_  | Python没有以 -O 选项启动，则此常量为真值                     |
| Ellipsis       | 与用户定义的容器数据类型的扩展切片语法结合使用               |
| NotImplemented | 二进制特殊方法应返回的特殊值（例如，__eq()__、__lt()__等）表示操作没有针对其他类型实现 |



### 内置类型

下表列出内置的数据类型，更多详情请参阅阅CPython文档：[Built-in Types](https://docs.python.org/3.5/library/stdtypes.html)

| 内置类型   |                                    |
| ---------- | ---------------------------------- |
| int        | 整数，数值类型                     |
| float      | 浮点数，数值类型                   |
| complex    | 复数，数值类型                     |
| bool       | bool，数值类型                     |
| list       | 列表，序列类型                     |
| tuple      | 元组，序列类型                     |
| range      | range对象，序列类型                |
| str        | 字符串，序列类型                   |
| bytes      | 单个字节构成的不可变序列，序列类型 |
| bytearray  | bytes对象的可变对应物，序列类型    |
| memoryview | 二进制序列                         |
| dict       | 字典，映射类型                     |
| set        | 集合                               |
| frozenset  | 集合，不可修改，具有哈希值         |
| object     | 对象，python3.x后class默认的基类   |