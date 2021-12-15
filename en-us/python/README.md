Python Fundamentals

> To learn about Python, you can learn from the official Python tutorial, [https://docs.python.org/3/], or general Python tutorial books, such as:
>
> * *Python Cookbook*, 3rd Edition, by David Beazley and Brian K. Jones (O 'Reilly)
> * *Fluent Python*, by Luciano Ramalho (O’Reilly)
> * *Effective Python*, by Brett Slatkin (Pearson)

## Python Interpreter 

Python is an interpretive language. The Python interpreter can only run one statement of a program at a time. A standard interactive Python interpreter can be opened on the command line by typing the ` python ` command:

```python
$ python
Python 3.6.0 | packaged by conda-forge | (default, Jan 13 2017, 23:17:12)
[GCC 4.8.2 20140120 (Red Hat 4.8.2-15)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 5
>>> print(a)
5
```

`>>>` prompt for code. To exit the Python interpreter and return to the terminal, type ` exit () ` or press Ctrl-D. 

To run a Python program, you simply call Python and use a `. py ` file as its first argument. Suppose you create a ` hello_world. py ` file with the following contents: 

```python
print('Hello world')
```

You can run it with the following command ( ` hello_world. py ` file must be in the terminal's working directory ) :

```python
$ python hello_world.py
Hello world
```

While some Python programmers always execute Python code this way, data analysts and scientific testers use IPython, an enhanced Python interpreter, or Jupyter Notebooks, a web code notebooks originally a subproject of IPython. When you execute the `%run` command, IPython will also execute the code in the specified file, and then interact with the results:

```python
$ ipython
Python 3.6.0 | packaged by conda-forge | (default, Jan 13 2017, 23:17:12)
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: %run hello_world.py
Hello world

In [2]:
```

IPython defaults to the ordinal format ` In [2]: `, unlike the standard ` > > > ` prompt.



## Python Grammar Fundamentals

### Semantics of Language

Python's language design emphasizes readability, conciseness, and clarity. Some people call Python "executable pseudocode".

### Use Indentation Instead of Parentheses

Python uses white space characters (tabs and spaces) to organize code rather than parentheses like other languages such as R C + + Java and Perl. Take the ` for ` loop of a sorting algorithm as an example:

```python
for x in array:
    if x < pivot:
        less.append(x)
    else:
        greater.append(x)
```

The colon marks the beginning of the indented code block, and all code following the colon must be indented by the same amount until the end of the code block. Like it or not, using white space is part of Python programmers' development, which, in my opinion, makes Python code much more readable than other languages. Although it seems strange at first, after a while, you can get used to it.

> Note: I strongly recommend that you use four spaces as the default indentation. You can use tab instead of four spaces. Many text editors are set to use tab stops instead of spaces. Some people use tabs or different numbers of spaces, and it is common to use two spaces. For the most part, four spaces is the most common approach, so I suggest you do the same.

As you should have seen, Python statements don't need to end with semicolons. However, semicolons can be used to segment statements on the same line:

```python
a = 5; b = 6; c = 7
```

Python does not recommend putting multiple statements on one line, which reduces the readability of codes.

### Everything Is an Object

An important feature of the Python language is the consistency of its object model. Every number, string, data structure, function, class, module, and so on is in the Python interpreter's own "box", which is considered a Python object. Each object has a type (for example, a string or function) and internal data. In practice, this can make the language very flexible, because functions can also be used as objects.

### Notes

Any text preceded by a # is ignored by the Python interpreter. This is usually used to add comments. Sometimes, you want to exclude a piece of code, but don't delete it. An easy way is to comment it out:

```python
results = []
for line in file_handle:
    # keep the empty lines for now
    # if len(line) == 0:
    #   continue
    results.append(line.replace('foo', 'bar'))
```

You can also add comments after the executed code. Some people are used to adding comments before the code, but the former method is sometimes useful:

```python
print("Reached this line")  # Simple status report
```

### Function and Object Method Calls

You can call a function in parentheses, pass zero or several arguments, or return a value to a variable:

```python
result = f(x, y, z)
g()
```

Almost every object in Python has additional functions, called methods, that can be used to access the object's contents. You can call it with the following statement:

```python
obj.some_method(x, y, z)
```

Function can use location and keyword arguments:

```python
result = f(a, b, c, d=5, e='foo')
```

More will be introduced later.

### Variable and argument Passing

When you create a variable (or name) in Python, you create a reference to the variable to the right of the equal sign. Consider a list of integers:

```python
In [8]: a = [1, 2, 3]
```

Suppose you assign a to a new variable b:

```python
In [9]: b = a
```

In some methods, this assignment will also copy the data [1, 2, 3\]. In Python, a and b are actually the same object, the original list [1, 2, 3\] (see Figure 2-7). You can add an element to a and then check b:

```python
In [10]: a.append(4)

In [11]: b
Out[11]: [1, 2, 3, 4]
```

![](C:\Users\sonia.liu\AppData\Roaming\Typora\typora-user-images\image-20210728153707264.png)

It is important to understand what Python references mean, when, how, and why data is replicated. Especially when you use Python to deal with large data sets.

> Note: Assignment is also called binding. We bind a name to an object. Variable names may sometimes be called bound variables.

When you pass an object as an argument to a function, the new local variable creates a reference to the original object instead of a copy. If you bind a new object to a variable in a function, the change will not be reflected to the next level. Therefore, the contents of variable arguments can be changed. Suppose you have the following function:

```python
def append_element(some_list, element):
    some_list.append(element)
```

Then:

```python
In [27]: data = [1, 2, 3]

In [28]: append_element(data, 4)

In [29]: data
Out[29]: [1, 2, 3, 4]
```

### Dynamic Reference, Strongly Typed

In contrast to many compiled languages, such as JAVA and C + +, object references in Python contain no attached types. The following code is correct:

```python
In [12]: a = 5

In [13]: type(a)
Out[13]: int

In [14]: a = 'foo'

In [15]: type(a)
Out[15]: str
```

A variable is the name of an object in a special namespace, and the type information is stored in the object itself. Some people may say that Python is not a "typed language". This is incorrect. Look at the following example:

```python
In [16]: '5' + 5
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-f9dbf5f0b234> in <module>()
----> 1 '5' + 5
TypeError: must be str, not int
```

In some languages, such as Visual Basic, the string '5' may be implicitly converted (or projected) to an integer, resulting in a 10. But in other languages, such as JavaScript, the integer 5 is projected as a string, resulting in the join string '55'. In this respect, Python is considered a strongly typed language, meaning that every object has an explicit type (or class), and tacit conversion only occurs in certain situations, such as:

```python
In [17]: a = 4.5

In [18]: b = 2

# String formatting, to be visited later
In [19]: print('a is {0}, b is {1}'.format(type(a), type(b)))
a is <class 'float'>, b is <class 'int'>

In [20]: a / b
Out[20]: 2.25
```

It is important to know the type of object, and it is best to make the function handle multiple types of input. You can use the ` isinstance ` function to check that an object is an instance of a certain type:

```python
In [21]: a = 5

In [22]: isinstance(a, int)
Out[22]: True
```

` isinstance ` can use a type tuple to check that the type of an object is in the tuple:

```python
In [23]: a = 5; b = 4.5

In [24]: isinstance(a, (int, float))
Out[24]: True

In [25]: isinstance(b, (int, float))
Out[25]: True
```

### Attributes and Methods

Python objects usually have attributes (other Python objects stored inside the object) and methods (the object's accessory functions can access the object's internal data). You can access attributes and methods with ` obj.attribute_name `:

```python
In [1]: a = 'foo'

In [2]: a.<Press Tab>
a.capitalize  a.format      a.isupper     a.rindex      a.strip
a.center      a.index       a.join        a.rjust       a.swapcase
a.count       a.isalnum     a.ljust       a.rpartition  a.title
a.decode      a.isalpha     a.lower       a.rsplit      a.translate
a.encode      a.isdigit     a.lstrip      a.rstrip      a.upper
a.endswith    a.islower     a.partition   a.split       a.zfill
a.expandtabs  a.isspace     a.replace     a.splitlines
a.find        a.istitle     a.rfind       a.startswith
```

You can also use `getattr` function to access attributes and methods by names.

```python
In [27]: getattr(a, 'split')
Out[27]: <function str.split>
```

In other languages, the name of the accessed object is usually called "reflection". This book does not make extensive use of the ` getattr ` function and the associated ` hasattr ` and ` setattr ` functions, which allow you to write native, reusable code efficiently.

### Duck Type

Usually, you may not care about the type of object, only whether the object has some method or purpose. This is often called "duck type", which comes from the saying that "it walks like a duck and barks like a duck, then it is a duck". For example, you can determine that an object is iterative by verifying that it follows an iterative protocol. For many objects, this means that it has a ` __iter__ ` magic method, and a better way to judge is to use the ` iterer ` function:

```python
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False
```

This function returns a string and most Python collections are of type ` True `:

```python
In [29]: isiterable('a string')
Out[29]: True

In [30]: isiterable([1, 2, 3])
Out[30]: True

In [31]: isiterable(5)
Out[31]: False
```

I always use this function to write functions that can accept multiple input types. A common example is writing a function that can accept any type of sequence (list, tuple, ndarray) or iterator. You can first check whether the object is a list (or NUmPy array), and if not, turn it into a list:

```python
if not isinstance(x, list) and isiterable(x):
    x = list(x)
```

### Introduce

In Python, a module is a file with the `. py ` extension that contains Python codes. Assume the following modules:

```python
# some_module.py
PI = 3.14159

def f(x):
    return x + 2

def g(a, b):
    return a + b
```

If you want to access the variables and functions defined in ` some_module. py ` from another file in the same directory, you can:

```python
import some_module
result = some_module.f(5)
pi = some_module.PI
```

Or:

```python
from some_module import f, g, PI
result = g(5, PI)
```

Using the ` as ` keyword, you can introduce different variable names:

```python
import some_module as sm
from some_module import PI as pi, g as gf

r1 = sm.f(pi)
r2 = gf(6, pi)
```

### Binary Operators and Comparison Operators

Most binary mathematical operations and comparisons are not difficult to think of:

```python
In [32]: 5 - 7
Out[32]: -2

In [33]: 12 + 21.5
Out[33]: 33.5

In [34]: 5 <= 2
Out[34]: False
```

Table 2-3 lists all binary operators. 

To determine whether two references point to the same object, you can use the ` is ` method. ` is not ` can determine that two objects are different: 

```python
In [35]: a = [1, 2, 3]

In [36]: b = a

In [37]: c = list(a)

In [38]: a is b
Out[38]: True

In [39]: a is not c
Out[39]: True
```

Because `list` always creates a new Python list (that is, a copy), we can conclude that c is different from a. Using the ` is ` comparison differs from the ` == ` operator, as follows:

```python
In [40]: a == c
Out[40]: True
```

` is ` and ` is not ` are commonly used to determine whether a variable is ` none ` because there is only one instance of ` none `:

```python
In [41]: a = None

In [42]: a is None
Out[42]: True
```

![](images\1241.jpg)

| Operation     | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| a + b         | a plus b                                                     |
| a - b         | a minus b                                                    |
| a * b         | multiple a by b                                              |
| a / b         | divide a by b                                                |
| a / / b       | divide a by b, and only take the integer part                |
| a ** b        | a to the power of b                                          |
| a & b         | TRUE if a and b are TRUE; For integers, take bitwise AND     |
| a ︱ b        | TRUE if a or b is TRUE; For integers, take bitwise OR        |
| a ^ b         | For a Boolean, TRUE if either a or B is TRUE and FALSE if both are True;  For integers, take bitwise EXCLUSIVE-OR |
| a == b        | True if a is equal to b                                      |
| a != b        | True if a is not equal to b                                  |
| a < b, a <= b | True if a is less than (or equal to) b                       |
| a > b, a >= b | True if a is more than (or equal to) b                       |
| a is b        | True if a and b reference the same Python object             |
| a is not b    | True if a and b reference different Python object            |

### Mutable and Immutable Objects

Most objects in Python, such as lists, dictionaries, NumPy arrays, and user-defined types (classes), are mutable. Means that these objects or contained values can be modified:

```python
In [43]: a_list = ['foo', 2, [4, 5]]

In [44]: a_list[2] = (3, 4)

In [45]: a_list
Out[45]: ['foo', 2, (3, 4)]
```

Others, such as strings and tuples, are immutable:

```python
In [46]: a_tuple = (3, 5, (4, 5))

In [47]: a_tuple[1] = 'four'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-47-b7966a9ae0f1> in <module>()
----> 1 a_tuple[1] = 'four'
TypeError: 'tuple' object does not support item assignment
```

Remember, you can modify an object doesn't mean you have to modify it. This is called a side effect. For example, when writing a function, any side effects should be stated in the documentation or comments. If possible, I recommend avoiding side effects and adopting immutable methods, even if mutable objects are used.

### Scalar Type

Python's standard library has built-in types for handling numeric data, strings, Boolean values, and datetimes. These single-valued types are called scalar types, which are called scalars in this book. Table 2-4 lists the main scalars. Date and time processing is discussed separately because they are provided by the standard library's ` datetime ` module.

![](images\1242.jpg)

| Type  | Description                                                  |
| ----- | ------------------------------------------------------------ |
| None  | Python's null value (only one instance of the None object exists) |
| str   | A string type that holds Unicode (UFT-8 encoding) strings    |
| bytes | Native ASCII bytes (or Unicode encoded as bytes)             |
| float | Double-precision (64-bit) floating-point number (note that there is no double type) |
| bool  | The value of True or False                                   |
| int   | Arbitrary Precision Integer                                  |

### Numeric Type

The main numeric types in Python are ` int ` and ` float `. ` int ` can store any large number:

```python
In [48]: ival = 17239871

In [49]: ival ** 6
Out[49]: 26254519291092456596965462913230729701102721
```

Floating point numbers use Python's ` float ` type. Each number is a double-precision (64-bit) value. It can also be expressed by scientific notation:

```python
In [50]: fval = 7.243

In [51]: fval2 = 6.78e-5
```

Dividing integers that cannot be obtained results in floating-point numbers:

```python
In [52]: 3 / 2
Out[52]: 1.5
```

To get C-style divisibility (with decimals removed), you can use the bottom division operator//:

```python
In [53]: 3 // 2
Out[53]: 1
```

### String

Many people use Python because of its powerful and flexible string processing. You can use single quotation marks or double quotation marks to write strings:

```python
a = 'one way of writing a string'
b = "another way"
```

For strings with line break, you can use three quotation marks, '''or''"":

```python
c = """
This is a longer string that
spans multiple lines
"""
```

The string ` c ` actually contains four lines of text, a line break after "" "and lines. You can use the ` count ` method to evaluate new rows in ` c `:

```python
In [55]: c.count('\n')
Out[55]: 3
```

Strings in Python are immutable and cannot be modified:

```python
In [56]: a = 'this is a string'

In [57]: a[10] = 'f'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-57-5ca625d1e504> in <module>()
----> 1 a[10] = 'f'
TypeError: 'str' object does not support item assignment

In [58]: b = a.replace('string', 'longer string')

In [59]: b
Out[59]: 'this is a longer string'
```

After the above operation, the variable ` a ` has not been modified:

```python
In [60]: a
Out[60]: 'this is a string'
```

Many Python objects can be converted to strings using the ` str ` function:

```python
In [61]: a = 5.6

In [62]: s = str(a)

In [63]: print(s)
5.6
```

A string is a sequence of Unicode characters, so it can be handled like other sequences, such as lists and tuples (both of which are described in detail in the next chapter):

```python
In [64]: s = 'python'

In [65]: list(s)
Out[65]: ['p', 'y', 't', 'h', 'o', 'n']

In [66]: s[:3]
Out[66]: 'pyt'
```

The syntax ` s [: 3] ` is called slicing and is applicable to many Python sequences. As will be described in more detail later, many slices are used in this book. 

A backslash is an escape character, meaning that it is used alternately to represent special characters, such as newline\ n or Unicode characters. To write a string containing a backslash, you need to escape: 

```python
In [67]: s = '12\\34'

In [68]: print(s)
12\34
```

If the string contains many backslashes but no special characters, it is very troublesome to do so. Fortunately, you can prefix a string with an R to indicate that the character is itself:

```python
In [69]: s = r'this\has\no\special\characters'

In [70]: s
Out[70]: 'this\\has\\no\\special\\characters'
```

r indicates raw.

Merging two strings produces a new string:

```python
In [71]: a = 'this is the first half '

In [72]: b = 'and this is the second half'

In [73]: a + b
Out[73]: 'this is the first half and this is the second half'
```

Templating or formatting strings is another important topic. Python 3 extends this type of approach, only a few of which are covered here. String objects have ` format ` methods that replace formatted arguments with strings to produce a new string:

```python
In [74]: template = '{0:.2f} {1:s} are worth US${2:d}'
```

In this string,

* `{0:.2f}` indicates that the first argument is formatted as a floating-point number with two decimal places.
* `{1:s}` indicates that the second argument is formatted as a string.
* `{2:d}` indicates that the third argument is formatted as an integer.

To replace the arguments with these formatted arguments, we pass a sequence of ` format ` methods:

```python
In [75]: template.format(4.5560, 'Argentine Pesos', 1)
Out[75]: '4.56 Argentine Pesos are worth US$1'
```

String formatting is a deep topic, with a number of methods and options to control how values in a string are formatted. It is recommended to refer to Python official documents. 

String processing is outlined here, and data analysis in Chapter 8 will be described in detail. 

### Bytes and Unicode

In Python 3 and latter versions, Unicode is a first-class string type, which allows for more consistent processing of ASCII and Non-ASCII text. In older Python versions, strings were all bytes and were not encoded in Unicode. If you know the character encoding, you can convert it to Unicode. Look at an example:

```python
In [76]: val = "español"

In [77]: val
Out[77]: 'español'
```

You can encode this Unicode string as UTF-8 with ` encode `:

```python
In [78]: val_utf8 = val.encode('utf-8')

In [79]: val_utf8
Out[79]: b'espa\xc3\xb1ol'

In [80]: type(val_utf8)
Out[80]: bytes
```

If you know the Unicode encoding of a byte object, you can decode it with the ` decode ` method:

```python
In [81]: val_utf8.decode('utf-8')
Out[81]: 'español'
```

Although UTF-8 encoding has become mainstream, for historical reasons, you may still encounter other encoded data:

```python
In [82]: val.encode('latin1')
Out[82]: b'espa\xf1ol'

In [83]: val.encode('utf-16')
Out[83]: b'\xff\xfee\x00s\x00p\x00a\x00\xf1\x00o\x00l\x00'

In [84]: val.encode('utf-16le')
Out[84]: b'e\x00s\x00p\x00a\x00\xf1\x00o\x00l\x00'
```

Many of the files encountered in our work are byte objects, so it is not advisable to blindly encode all the data as Unicode. 

Although it is not used much, you can prefix the byte text with a **b**: 

```python
In [85]: bytes_val = b'this is bytes'

In [86]: bytes_val
Out[86]: b'this is bytes'

In [87]: decoded = bytes_val.decode('utf8')

In [88]: decoded  # this is str (Unicode) now
Out[88]: 'this is bytes'
```

### Boolean Value

There are two Boolean values in Python, True and False. Comparison and other conditional expressions can be judged by True and False. Boolean values can be used in conjunction with **and** and **or**:

```python
In [89]: True and True
Out[89]: True

In [90]: False or True
Out[90]: True
```

### Type Conversion

Str, bool, int, and float are also functions that can be used to convert types:

```python
In [91]: s = '3.14159'

In [92]: fval = float(s)

In [93]: type(fval)
Out[93]: float

In [94]: int(fval)
Out[94]: 3

In [95]: bool(fval)
Out[95]: True

In [96]: bool(0)
Out[96]: False
```

### None

None is Python's null value type. If a function does not have an explicit return value, it will return None by default:

```python
In [97]: a = None

In [98]: a is None
Out[98]: True

In [99]: b = 5

In [100]: b is not None
Out[100]: True
```

None is also often used as the default argument for functions:

```python
def add_and_maybe_multiply(a, b, c=None):
    result = a + b

    if c is not None:
        result = result * c

    return result
```

In addition, None is not only a reserved word, but also a unique instance of NoneType:

```python
In [101]: type(None)
Out[101]: NoneType
```

### Date and Time

Python's built-in ` datetime ` module provides ` datetime `, ` date `, and ` time ` types. The ` datetime ` type combines ` date ` and ` time ` and is most commonly used:

```python
In [102]: from datetime import datetime, date, time

In [103]: dt = datetime(2011, 10, 29, 20, 30, 21)

In [104]: dt.day
Out[104]: 29

In [105]: dt.minute
Out[105]: 30
```

According to the ` datetime ` instance, you can use ` date ` and ` time ` to extract the respective objects:

```python
In [106]: dt.date()
Out[106]: datetime.date(2011, 10, 29)

In [107]: dt.time()
Out[107]: datetime.time(20, 30, 21)
```

The ` strftime ` method can format `datetime` as a string:

```python
In [108]: dt.strftime('%m/%d/%Y %H:%M')
Out[108]: '10/29/2011 20:30'
```

` strptime ` converts a string to a ` datetime ` object:

```python
In [109]: datetime.strptime('20091031', '%Y%m%d')
Out[109]: datetime.datetime(2009, 10, 31, 0, 0)
```

Table 2-5 lists all the formatting commands.

![](images\1243.jpg)

| Type | Description                                                  |
| ---- | ------------------------------------------------------------ |
| %Y   | Four-digit year                                              |
| %y   | Two-digit year                                               |
| %m   | Two-digit month [01, 12]                                     |
| %d   | Two-digit day [01, 31]                                       |
| %H   | Hour (24-hour) [00, 23]                                      |
| %I   | Hour (12-hour) [01, 12]                                      |
| %M   | Two-digit minute [00, 59]                                    |
| %S   | Second [00, 61] (60 and 61 indicate leap second)             |
| %w   | Integer days of the week                                     |
| %U   | Number Week of the Year [00, 53]; Sunday is the beginning of a week, and the days before the first Sunday are "week0". |
| %W   | Number Week of the Year [00, 53]; Monday is the beginning of a week, and the days before the first Monday are "week0". |
| %z   | The UTC time zone offset is +HHMM or -HHMM; If you do not know the time zone, this parameter is null. |
| %F   | Indicate %Y-%m-%d (i.e. 2012-4-18)                           |
| %D   | Indicate %m/%d/%y (i.e. 04/18/12)                            |

Replacing the time field of datetimes is sometimes useful when you cluster or group time series. For example, replace minutes and seconds with 0:

```python
In [110]: dt.replace(minute=0, second=0)
Out[110]: datetime.datetime(2011, 10, 29, 20, 0)
```

Because ` datetime.datetime ` is an immutable type, the above method produces a new object. 

The difference between two datetime objects produces a ` datetime. timedelta ` type: 

```python
In [111]: dt2 = datetime(2011, 11, 15, 22, 30)

In [112]: delta = dt2 - dt

In [113]: delta
Out[113]: datetime.timedelta(17, 7179)

In [114]: type(delta)
Out[114]: datetime.timedelta
```

The result ` timedelta (17,7179) ` indicates how ` timedelta ` will encode 17 days, 7179 seconds. 

Adding ` timedelta ` to ` datetime ` produces a new offset ` datetime `: 

```python
In [115]: dt
Out[115]: datetime.datetime(2011, 10, 29, 20, 30, 21)

In [116]: dt + delta
Out[116]: datetime.datetime(2011, 11, 15, 22, 30)
```

### Control Flow

Python has several built-in keywords for conditional logic, loops, and other control flow operations.

### If, Elif and Else

**If** is the most widely known control flow statement. It checks a condition, and if it is True, it executes the following statement:

```python
if x < 0:
    print('It's negative')
```

` if ` can be followed by one or more ` elif `, and when all conditions are false, you can add an ` else `:

```python
if x < 0:
    print('It's negative')
elif x == 0:
    print('Equal to zero')
elif 0 < x < 5:
    print('Positive but smaller than 5')
else:
    print('Positive and larger than or equal to 5')
```

If a condition is True, the subsequent ` elif ` will not be executed. When **and** and **or** are used, the compound conditional statement is executed from left to right:

```python
In [117]: a = 5; b = 7

In [118]: c = 8; d = 4

In [119]: if a < b or c > d:
   .....:     print('Made it')
Made it
```

In this example, ` c > d ` will not be performed because the first comparison is True: 

You can also string comparisons together: 

```python
In [120]: 4 > 3 > 2 > 1
Out[120]: True
```

### For Loop

A for loop is an iteration within a collection (list or tuple), or just an iterator. The standard syntax for a for loop is:

```python
for value in collection:
    # do something with value
```

You can use continue to advance the for loop and skip the rest. Look at the following example, adding integers in a list and skipping None:

```python
sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value
```

You can jump out of the for loop with ` break `. The following code adds the elements until you encounter 5:

```python
sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
    if value == 5:
        break
    total_until_5 += value
```

Break only breaks the innermost layer of the for loop, and the rest of the for loops still run:

```python
In [121]: for i in range(4):
   .....:     for j in range(4):
   .....:         if j > i:
   .....:             break
   .....:         print((i, j))
   .....:
(0, 0)
(1, 0)
(1, 1)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
(3, 3)
```

If you have a sequence of elements (tuples or lists) in a collection or iterator, you can easily split them into variables using the for loop:

```python
for a, b, c in iterator:
    # do something
```

### While Loop

The while loop specifies a condition and code that exits only when the condition is False or the loop is exited with break:

```python
x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2
```

### Pass

Pass is a non-operational statement in Python. Code blocks can be used when no action is required (as placeholders for unexecuted code); Because Python needs to use white space characters to delimit code blocks, it needs pass:

```python
if x < 0:
    print('negative!')
elif x == 0:
    # TODO: put something smart here
    pass
else:
    print('positive!')
```

### Range

The range function returns an iterator that produces a uniformly distributed sequence of integers:

```python
In [122]: range(10)
Out[122]: range(0, 10)

In [123]: list(range(10))
Out[123]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The three arguments of range are (start, end, step):

```python
In [124]: list(range(0, 20, 2))
Out[124]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

In [125]: list(range(5, 0, -1))
Out[125]: [5, 4, 3, 2, 1]
```

As you can see, the integer generated by range does not include the end point. A common use of range is to iterate through sequences with serial numbers:

```python
seq = [1, 2, 3, 4]
for i in range(len(seq)):
    val = seq[i]
```

You can use a list to store all the integers that range generates in other data structures, and the default iterator form is usually what you want. The following code sums the multiples of 3 or 5 from 0 to 99999:

```python
sum = 0
for i in range(100000):
    # % is the modulo operator
    if i % 3 == 0 or i % 5 == 0:
        sum += i
```

Although range can produce any large number, it consumes very little memory at any time.

### Ternary Expression

Ternary expressions in Python can put if-else statements on one line. The syntax is as follows:

```python
value = true-expr if condition else false-expr
```

` true-expr ` or ` false-expr ` can be any Python code. It has the same effect as the following code:

```python
if condition:
    value = true-expr
else:
    value = false-expr
```

Here's a more specific example:

```python
In [126]: x = 5

In [127]: 'Non-negative' if x >= 0 else 'Negative'
Out[127]: 'Non-negative'
```

As with if-else, only one expression is executed. Therefore, if and else in a ternary expression can contain a large number of evaluations, but only the branch of True will be executed. Therefore, if and else in a ternary expression can contain a large number of evaluations, but only the branch of True will be executed.

Although using ternary expressions can compress the code, it will reduce the readability of the code.



This chapter discusses the built-in features of Python, which will be used in many places in this book. While extension libraries, such as pandas and Numpy, make it easy to work with large data sets, they are used with Python's built-in data processing tools. 

We'll start with Python's most basic data structures: tuples, lists, dictionaries, and collections. Then we will discuss creating your own reusable Python functions. Finally, you will learn about Python's file objects and how to interact with the local hard disk. 

## Data Structure and Sequence
Python's data structure is simple and powerful. Knowing them makes you a skilled Python programmer.

### Tuple
A tuple is a fixed-length, immutable Python sequence object. The easiest way to create tuples is to separate a list of values with commas:

```python
In [1]: tup = 4, 5, 6

In [2]: tup
Out[2]: (4, 5, 6)
```

When defining tuples with complex expressions, it is best to put the values in parentheses, as follows:

```python
In [3]: nested_tup = (4, 5, 6), (7, 8)

In [4]: nested_tup
Out[4]: ((4, 5, 6), (7, 8))
```

You can use ` tuple`  to convert any sequence or iterator into a tuple:

```python
In [5]: tuple([4, 0, 2])
Out[5]: (4, 0, 2)

In [6]: tup = tuple('string')

In [7]: tup
Out[7]: ('s', 't', 'r', 'i', 'n', 'g')
```

You can access elements in tuples with square brackets. Like C, C + +, JAVA and other languages, sequences start from 0:

```python
In [8]: tup[0]
Out[8]: 's'
```

Objects stored in tuples may be mutable objects. Once a tuple is created, the objects in the tuple cannot be modified:

```python
In [9]: tup = tuple(['foo', [1, 2], True])

In [10]: tup[2] = False
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-10-c7308343b841> in <module>()
----> 1 tup[2] = False
TypeError: 'tuple' object does not support item assignment
```

If an object in a tuple is mutable, such as a list, you can modify it in place:

```python
In [11]: tup[1].append(3)

In [12]: tup
Out[12]: ('foo', [1, 2, 3], True)
```

You can concatenate tuples with the plus operator:

```python
In [13]: (4, None, 'foo') + (6, 0) + ('bar',)
Out[13]: (4, None, 'foo', 6, 0, 'bar')
```

Multiplying a tuple by an integer, like a list, concatenates copies of several tuples:

```python
In [14]: ('foo', 'bar') * 4
Out[14]: ('foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar')
```

The object itself is not copied, just referenced.

### Split Tuple
If you want to assign a tuple to a tuple-like variable, Python will try to split the value to the right of the equal sign:

```python
In [15]: tup = (4, 5, 6)

In [16]: a, b, c = tup

In [17]: b
Out[17]: 5
```

Even tuples that contain tuples are split:

```python
In [18]: tup = 4, 5, (6, 7)

In [19]: a, b, (c, d) = tup

In [20]: d
Out[20]: 7
```

With this function, you can easily replace the names of variables, which may be the case in other languages:

```python
tmp = a
a = b
b = tmp
```

But in Python, you can substitute like this:

```python
In [21]: a, b = 1, 2

In [22]: a
Out[22]: 1

In [23]: b
Out[23]: 2

In [24]: b, a = a, b

In [25]: a
Out[25]: 2

In [26]: b
Out[26]: 1
```

Variable splitting is often used to iterate over tuples or list sequences:

```python
In [27]: seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

In [28]: for a, b, c in seq:
   ....:     print('a={0}, b={1}, c={2}'.format(a, b, c))
a=1, b=2, c=3
a=4, b=5, c=6
a=7, b=8, c=9
```

Another common use is to return multiple values from a function. It will be explained in detail later. 

Python recently added more advanced tuple splitting capabilities that allow several elements to be "picked" from the beginning of a tuple. It uses the special syntax ` *rest` , which is also used in function signatures to grab positional arguments for arbitrary-length lists: 

```python
In [29]: values = 1, 2, 3, 4, 5

In [30]: a, b, *rest = values

In [31]: a, b
Out[31]: (1, 2)

In [32]: rest
Out[32]: [3, 4, 5]
```

The part of ` ` rest ` ` is the part you want to discard, and the name of rest is not important. As an idiom, many Python programmers underline unwanted variables:

```python
In [33]: a, b, *_ = values
```

### Tuple Methods
Because the size and content of tuples cannot be modified, its instance methods are lightweight. One of the most useful ones is ` count`  (which also applies to lists), which can count the frequency of a value:

```python
In [34]: a = (1, 2, 2, 2, 3, 4, 2)

In [35]: a.count(2)
Out[35]: 4
```

### List
Compared with tuples, the length of the list is variable and the contents can be modified. You can define it in square brackets, or use the ` list `  function:

```python
In [36]: a_list = [2, 3, 7, None]

In [37]: tup = ('foo', 'bar', 'baz')

In [38]: b_list = list(tup)

In [39]: b_list
Out[39]: ['foo', 'bar', 'baz']

In [40]: b_list[1] = 'peekaboo'

In [41]: b_list
Out[41]: ['foo', 'peekaboo', 'baz']
```

Lists and tuples have similar semantics and can be used interchangeably in many functions. 

The ` list`  function is often used to materialize an iterator or generator in data processing: 

```python
In [42]: gen = range(10)

In [43]: gen
Out[43]: range(0, 10)

In [44]: list(gen)
Out[44]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Appending and Removing Elements
You can use ` append`  to add elements at the end of the list:

```python
In [45]: b_list.append('dwarf')

In [46]: b_list
Out[46]: ['foo', 'peekaboo', 'baz', 'dwarf']
```

` insert ` allows you to insert elements at specific locations:

```python
In [47]: b_list.insert(1, 'red')

In [48]: b_list
Out[48]: ['foo', 'red', 'peekaboo', 'baz', 'dwarf']
```

The sequence number inserted must be between 0 and the list length.

>Warning: ` insert ` is computationally intensive compared to ` append ` because references to subsequent elements must be migrated internally to provide space for new elements. If you want to insert elements at the head and tail of a sequence, you might want to use ` collections.deque `, a double-tail queue.

The inverse of insert is pop, which removes and returns the element at the specified position:

```python
In [49]: b_list.pop(2)
Out[49]: 'peekaboo'

In [50]: b_list
Out[50]: ['foo', 'red', 'baz', 'dwarf']
```

You can remove a value with ` remove `, which looks for the first value and removes:

```python
In [51]: b_list.append('foo')

In [52]: b_list
Out[52]: ['foo', 'red', 'baz', 'dwarf', 'foo']

In [53]: b_list.remove('foo')

In [54]: b_list
Out[54]: ['red', 'baz', 'dwarf', 'foo']
```

Using ` append ` and ` remove ` regardless of performance, you can think of a Python list as a perfect "multiset" data structure. 

Use ` in ` to check whether the list contains a value: 

```python
In [55]: 'dwarf' in b_list
Out[55]: True
```

Negative ` in ` can be added with a not:

```python
In [56]: 'dwarf' not in b_list
Out[56]: False
```

Checking for a value in a list is much slower than dictionaries and collections, because Python searches for values in a list linearly, but in dictionaries and collections, other items can be checked at the same time (based on hash tables).

### Concatenated and Combined Lists
Similar to tuples, you can concatenate two lists with a plus sign:

```python
In [57]: [4, None, 'foo'] + [7, 8, (2, 3)]
Out[57]: [4, None, 'foo', 7, 8, (2, 3)]
```

If you have already defined a list, you can append multiple elements with the ` extend ` method:

```python
In [58]: x = [4, None, 'foo']

In [59]: x.extend([7, 8, (2, 3)])

In [60]: x
Out[60]: [4, None, 'foo', 7, 8, (2, 3)]
```

Concatenating lists by addition is computationally intensive because a new list is created and objects are copied. It is preferable to append elements with ` extend `, especially to a large list. Therefore:

```python
everything = []
for chunk in list_of_lists:
    everything.extend(chunk)
```

Faster than the concatenation method:

```python
everything = []
for chunk in list_of_lists:
    everything = everything + chunk
```

### Sort
You can use the ` sort ` function to sort a list in place (without creating new objects):

```python
In [61]: a = [7, 2, 5, 1, 3]

In [62]: a.sort()

In [63]: a
Out[63]: [1, 2, 3, 5, 7]
```

` sort `  has a number of options that sometimes work well. One of them is the second-level sort key, which can be used for sorting. For example, we can sort strings by length:

```python
In [64]: b = ['saw', 'small', 'He', 'foxes', 'six']

In [65]: b.sort(key=len)

In [66]: b
Out[66]: ['He', 'saw', 'six', 'small', 'foxes']
```

Later, we'll learn about the ` sort `  function, which produces an ordered copy of the sequence.

### Binary Search and Maintenance of Sorted Lists
The ` bisect ` module supports binary lookups and inserts values into sorted lists. ` bisect.bisect ` can find the position where sorting is guaranteed after inserting the value, and ` bisect.insert ` is to insert the value into this position:

```python
In [67]: import bisect

In [68]: c = [1, 2, 2, 2, 3, 4, 7]

In [69]: bisect.bisect(c, 2)
Out[69]: 4

In [70]: bisect.bisect(c, 5)
Out[70]: 6

In [71]: bisect.insort(c, 6)

In [72]: c
Out[72]: [1, 2, 2, 2, 3, 4, 6, 7]
```

>Note: The ` bisect ` module does not check whether the list is in order, which is computationally intensive. Therefore, using ` bisect ` for an unsorted list does not produce an error, but the result may not be correct.

### Slice
You can select a part of most sequence types with slices, the basic form of which is to use `  start: stop `  in square brackets:

```python
In [73]: seq = [7, 2, 3, 7, 5, 6, 0, 1]

In [74]: seq[1:5]
Out[74]: [2, 3, 7, 5]
```

Slices can also be assigned to sequences:
```python
In [75]: seq[3:4] = [6, 3]

In [76]: seq
Out[76]: [7, 2, 3, 6, 3, 5, 6, 0, 1]
```

The starting element of the slice is included, and the ending element is not included. Therefore, the number of elements contained in the result is ` stop-start `. 

Either ` start ` or ` stop ` can be omitted, after which the beginning and end of the sequence are defaulted, respectively: 

```python
In [77]: seq[:5]
Out[77]: [7, 2, 3, 6, 3]

In [78]: seq[3:]
Out[78]: [6, 3, 5, 6, 0, 1]
```

Negative numbers indicate slicing from back to front:

```python
In [79]: seq[-4:]
Out[79]: [5, 6, 0, 1]

In [80]: seq[-6:-2]
Out[80]: [6, 3, 5, 6]
```

It takes a while to get familiar with using slices, especially if you've learned R or MATLAB before. Figure 3-1 shows a slice of positive and negative integers. In the diagram, exponents are marked at the edges to indicate where the slice begins and ends.

![](images\1244.jpg)

![image-20210728171647093](C:\Users\sonia.liu\AppData\Roaming\Typora\typora-user-images\image-20210728171647093.png)

You can take one element at a time by using ` step ` after the second colon:

```python
In [81]: seq[::2]
Out[81]: [7, 3, 3, 6, 1]
```

A clever way is to use `-1 `, which can turn the list or tuple upside down:

```python
In [82]: seq[::-1]
Out[82]: [1, 0, 6, 5, 3, 6, 3, 2, 7]
```

### Enumerate Function
When iterating over a sequence, you may want to track the ordinal number of the current item. The manual method may be as follows: 

```python
i = 0
for value in collection:
   # do something with value
   i += 1
```

Because this is so common, Python has a built-in ` enumerate ` function that returns a sequence of ` (i, value) ` tuples:

```python
for i, value in enumerate(collection):
   # do something with value
```

When you index data, a good way to use ` enumerate ` is to calculate the value of the sequence (unique) ` dict ` mapped to the position:

```python
In [83]: some_list = ['foo', 'bar', 'baz']

In [84]: mapping = {}

In [85]: for i, v in enumerate(some_list):
   ....:     mapping[v] = i

In [86]: mapping
Out[86]: {'bar': 1, 'baz': 2, 'foo': 0}
```

### Sorted Function
The `sorted` function returns a new ordered list from any sequence of elements:

```python
In [87]: sorted([7, 1, 2, 6, 0, 3, 2])
Out[87]: [0, 1, 2, 2, 3, 6, 7]

In [88]: sorted('horse race')
Out[88]: [' ', 'a', 'c', 'e', 'e', 'h', 'o', 'r', 'r', 's']
```

The `sorted` function can take the same arguments as `sorted`.

### Zip Function
` zip `  can combine multiple lists, tuples, or other sequences in pairs into a tuple list:

```python
In [89]: seq1 = ['foo', 'bar', 'baz']

In [90]: seq2 = ['one', 'two', 'three']

In [91]: zipped = zip(seq1, seq2)

In [92]: list(zipped)
Out[92]: [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
```

` zip ` can handle as many sequences as possible, depending on the number of elements in the shortest sequence:

```python
In [93]: seq3 = [False, True]

In [94]: list(zip(seq1, seq2, seq3))
Out[94]: [('foo', 'one', False), ('bar', 'two', True)]
```

One of the common uses of ` zip ` is to iterate over multiple sequences at the same time, possibly in conjunction with ` enumerate `:

```python
In [95]: for i, (a, b) in enumerate(zip(seq1, seq2)):
   ....:     print('{0}: {1}, {2}'.format(i, a, b))
   ....:
0: foo, one
1: bar, two
2: baz, three
```

Given a "compressed" sequence, ` zip ` can be used to decompress the sequence. It can also be used as converting a list of rows into a list of columns. This method seems a bit magical:

```python
In [96]: pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'),
   ....:             ('Schilling', 'Curt')]

In [97]: first_names, last_names = zip(*pitchers)

In [98]: first_names
Out[98]: ('Nolan', 'Roger', 'Schilling')

In [99]: last_names
Out[99]: ('Ryan', 'Clemens', 'Curt')
```

### Reversed Function
` Reversed ` can iterate a sequence from back to front:

```python
In [100]: list(reversed(range(10)))
Out[100]: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

Keep in mind that ` reversed ` is a generator (more on it later), and you can only create flipped sequences after materialization (that is, a list or for loop).

### Dictionary
Dictionaries are probably Python's most important data structure. Its more common name is hash mapping or associative array. It is a variable-size collection of key-value pairs, and both keys and values are Python objects. One way to create a dictionary is to use angle brackets and use colons to separate keys and values:

```python
In [101]: empty_dict = {}

In [102]: d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}

In [103]: d1
Out[103]: {'a': 'some value', 'b': [1, 2, 3, 4]}
```

You can access, insert, or set an element in a dictionary just as you would an element in a list or tuple:

```python
In [104]: d1[7] = 'an integer'

In [105]: d1
Out[105]: {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}

In [106]: d1['b']
Out[106]: [1, 2, 3, 4]
```

You can check whether the dictionary contains a key by checking whether the list and tuple contain a certain value:

```python
In [107]: 'b' in d1
Out[107]: True
```

You can delete a value using the ` del ` keyword or the ` pop ` method (which returns the value while deleting the key):

```python
In [108]: d1[5] = 'some value'

In [109]: d1
Out[109]: 
{'a': 'some value',
 'b': [1, 2, 3, 4],
 7: 'an integer',
 5: 'some value'}

In [110]: d1['dummy'] = 'another value'

In [111]: d1
Out[111]: 
{'a': 'some value',
 'b': [1, 2, 3, 4],
 7: 'an integer',
 5: 'some value',
 'dummy': 'another value'}

In [112]: del d1[5]

In [113]: d1
Out[113]: 
{'a': 'some value',
 'b': [1, 2, 3, 4],
 7: 'an integer',
 'dummy': 'another value'}

In [114]: ret = d1.pop('dummy')

In [115]: ret
Out[115]: 'another value'

In [116]: d1
Out[116]: {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}
```

`keys`and `values` are iterator methods for the dictionary's keys and values. Although there is no order for key-value pairs, these two methods can output keys and values in the same order:

```python
In [117]: list(d1.keys())
Out[117]: ['a', 'b', 7]

In [118]: list(d1.values())
Out[118]: ['some value', [1, 2, 3, 4], 'an integer']
```

Use the ` update ` method to merge one dictionary with another:
```python
In [119]: d1.update({'b' : 'foo', 'c' : 12})

In [120]: d1
Out[120]: {'a': 'some value', 'b': 'foo', 7: 'an integer', 'c': 12}
```

The ` update ` method changes the dictionary in place, so the old value of any key passed to ` update ` is discarded.

### Creating Dictionaries with Sequences
Usually, you may want to pair two sequences into a dictionary. Here's one way to write it:

```python
mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value
```

Because a dictionary is essentially a collection of 2-tuples, a dict can accept a list of 2-tuples:
```python
In [121]: mapping = dict(zip(range(5), reversed(range(5))))

In [122]: mapping
Out[122]: {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}
```

`dict comprehensions`, another elegant way to build dictionaries, will be discussed later.

### Default Value
The following logic is common:

```python
if key in some_dict:
    value = some_dict[key]
else:
    value = default_value
```

Therefore, the methods **get** and **pop** of dict can be returned with default values, and the above if-else statement can be shortened as follows:
```python
value = some_dict.get(key, default_value)
```

**Get** returns **None** by default, and **pop** throws an exception if no key exists. With regard to set values, it is common for values in dictionaries to belong to other collections, such as lists. For example, you can classify words in a list by initials:

```python
In [123]: words = ['apple', 'bat', 'bar', 'atom', 'book']

In [124]: by_letter = {}

In [125]: for word in words:
   .....:     letter = word[0]
   .....:     if letter not in by_letter:
   .....:         by_letter[letter] = [word]
   .....:     else:
   .....:         by_letter[letter].append(word)
   .....:

In [126]: by_letter
Out[126]: {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
```

That's what the ` setdefault ` method does. The previous for loop can be rewritten as:

```python
for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
```

The `collections` module has a useful class, `defaultdict`, which simplifies the above further. Pass a type or function to generate a default value for each location:

```python
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
```

### Valid Key Types
The value of a dictionary can be any Python object, and the key is usually an immutable scalar type (integer, floating point, string) or a tuple (the object in the tuple must be immutable). This is called "hashable". You can use the ` hash ` function to detect whether an object is hashable (which can be used as a dictionary key):

```python
In [127]: hash('string')
Out[127]: 5023931463650008331

In [128]: hash((1, 2, (2, 3)))
Out[128]: 1097636502276347782

In [129]: hash((1, 2, [2, 3])) # fails because lists are mutable
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-129-800cd14ba8be> in <module>()
----> 1 hash((1, 2, [2, 3])) # fails because lists are mutable
TypeError: unhashable type: 'list'
```

One way to use a list as a key is to convert the list into a tuple, and as long as the internal element can be hashed, it can also be hashed:
```python
In [130]: d = {}

In [131]: d[tuple([1, 2, 3])] = 5

In [132]: d
Out[132]: {(1, 2, 3): 5}
```

### Set
A set is an unordered set of non-repeatable elements. You can think of it as a dictionary, but only with keys and no values. You can create collections in two ways: through the set function or using the Angle bracket set statement:

```python
In [133]: set([2, 2, 2, 1, 3, 3])
Out[133]: {1, 2, 3}

In [134]: {2, 2, 2, 1, 3, 3}
Out[134]: {1, 2, 3}
```

Set supports mathematical set operations such as merge, intersection, difference and symmetric difference. Consider two example collections:

```python
In [135]: a = {1, 2, 3, 4, 5}

In [136]: b = {3, 4, 5, 6, 7, 8}
```

Merge is to take elements that do not duplicate in two sets. You can use the ` union `  or the `|` operator:

```python
In [137]: a.union(b)
Out[137]: {1, 2, 3, 4, 5, 6, 7, 8}

In [138]: a | b
Out[138]: {1, 2, 3, 4, 5, 6, 7, 8}
```

The intersection elements are contained in two sets. You can use the ` intersection ` or the ` & ` operator:

```python
In [139]: a.intersection(b)
Out[139]: {3, 4, 5}

In [140]: a & b
Out[140]: {3, 4, 5}
```

Table 3-1 lists common set methods.

![Table 3-1 Set Methods of Python](images\1245.jpg)

| Function                         | Alternative Syntax | Description                                                  |
| -------------------------------- | ------------------ | ------------------------------------------------------------ |
| a.add(x)                         | N/A                | Add element x to set a                                       |
| a.clear()                        | N/A                | Empty the set                                                |
| a.remove(x)                      | N/A                | Remove element x from set a                                  |
| a.pop()                          | N/A                | Removes any element from set a, and raises a KeyError if the set is empty |
| a.union(b)                       | a｜b               | All the non-repeating elements in the sets a and b           |
| a.update(b)                      | a｜= b             | Set the elements of set a to be the combination of a and b   |
| a.intersection(b)                | a & b              | The intersecting elements of a and b                         |
| a.intersection_update(b)         | a &= b             | Set the elements of set a to be the intersection of a and b  |
| a.difference(b)                  | a - b              | Elements that exist in a but not in b                        |
| a.difference_update(b)           | a -= b             | Set the elements of set a to be the difference between a and b |
| a.symmetric_difference(b)        | a ^ b              | Elements that exist in either a or b                         |
| a.symmetric_difference_update(b) | a ^= b             | The elements of set a are only in a or only in b             |
| a.issubset(b)                    | N/A                | True if all elements of a  belongs to b                      |
| a.issuperset(b)                  | N/A                | True if all elements of b  belongs to a                      |
| a.isdisjoint(b)                  | N/A                | True if no common element in a or b                          |

All logical set operations have alternative in-place implementations that directly replace the contents of the set with results. For large sets, this is more efficient:

```python
In [141]: c = a.copy()

In [142]: c |= b

In [143]: c
Out[143]: {1, 2, 3, 4, 5, 6, 7, 8}

In [144]: d = a.copy()

In [145]: d &= b

In [146]: d
Out[146]: {3, 4, 5}
```

Similar to dictionaries, set elements are usually immutable. To get a list-like element, you must convert it to a tuple:

```python
In [147]: my_data = [1, 2, 3, 4]

In [148]: my_set = {tuple(my_data)}

In [149]: my_set
Out[149]: {(1, 2, 3, 4)}
```

You can also detect whether one set is a subset or parent of another:

```python
In [150]: a_set = {1, 2, 3, 4, 5}

In [151]: {1, 2, 3}.issubset(a_set)
Out[151]: True

In [152]: a_set.issuperset({1, 2, 3})
Out[152]: True
```

Sets are equal when the contents of sets are the same:

```python
In [153]: {1, 2, 3} == {3, 2, 1}
Out[153]: True
```

### Lists, Sets, and Dictionary Derivations
List derivation is one of Python's most beloved features. It allows users to easily filter elements from a set, form lists, and modify elements while passing arguments. The form is as follows:

```python
[expr for val in collection if condition]
```

It is equivalent to the following **for** loop;

```python
result = []
for val in collection:
    if condition:
        result.append(expr)
```

The filter condition can be ignored, leaving only the expression. For example, given a list of strings, we can filter out strings of length 2 or less and convert them to uppercase:

```python
In [154]: strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

In [155]: [x.upper() for x in strings if len(x) > 2]
Out[155]: ['BAT', 'CAR', 'DOVE', 'PYTHON']
```

In a similar way, sets and dictionaries can also be derived. The derivation of the dictionary is as follows:

```python
dict_comp = {key-expr : value-expr for value in collection if condition}
```

The derivation of a set is similar to that of a list, except in angle brackets:

```python
set_comp = {expr for value in collection if condition}
```

Similar to list derivation, set and dictionary derivation is also very convenient, and it makes it easy to read and write code. Look at the previous list of strings. If we only want the length of the string, it is very convenient to use the set derivation method:

```python
In [156]: unique_lengths = {len(x) for x in strings}

In [157]: unique_lengths
Out[157]: {1, 2, 3, 4, 6}
```

The ` map ` function can be further simplified:
```python
In [158]: set(map(len, strings))
Out[158]: {1, 2, 3, 4, 6}
```

As an example of a dictionary derivation, we can create a lookup map of a string to determine its position in the list:

```python
In [159]: loc_mapping = {val : index for index, val in enumerate(strings)}

In [160]: loc_mapping
Out[160]: {'a': 0, 'as': 1, 'bat': 2, 'car': 3, 'dove': 4, 'python': 5}
```

### Nested List Derivation
Suppose we have a list containing lists, including some English names and Spanish names:

```python
In [161]: all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
   .....:             ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
```

You may get these names from some files and then want to classify them by language. Now suppose we want to have a list of all the names that contain two or more e's. You can do this with a for loop:

```python
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.extend(enough_es)
```

You can write these together in a nested list derivation, as follows:

```python
In [162]: result = [name for names in all_data for name in names
   .....:           if name.count('e') >= 2]

In [163]: result
Out[163]: ['Steven']
```

The nested list derivation looks a little complicated. The for part of the list derivation is based on the order of nesting, and the filter condition is left at the end. Here's another example where we flatten a list of integer tuples to a list of integers:

```python
In [164]: some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

In [165]: flattened = [x for tup in some_tuples for x in tup]

In [166]: flattened
Out[166]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Remember that the order of the for expression is the same as the order of the nested for loop (not the order of the list derivation) :

```python
flattened = []

for tup in some_tuples:
    for x in tup:
        flattened.append(x)
```

You can have any number of levels of nesting, but if you have more than two or three nests, you should consider code readability. It is also important to distinguish the syntax in the list derivation of the list derivation:

```python
In [167]: [[x for x in tup] for tup in some_tuples]
Out[167]: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

This code produces a list of lists, instead of a flat list containing only elements.

### Function
Function is the leading and most important means of code organization and reuse in Python. As the most important principle, if you want to reuse the same or very similar code, you need to write a function. By giving the function a name, you can also improve the readability of the code.

The function is declared with the ` def ` keyword and returns the value with the ` return ` keyword:

```python
def my_function(x, y, z=1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)
```

It is also possible to have multiple **return** statements at the same time. **None** is returned if no **return** statement is encountered when the end of the function is reached. 

Functions can have some positional arguments and some keyword arguments. Keyword arguments are usually used to specify default values or optional arguments. In the above function, x and y are positional arguments, while z is a keyword arguments. That is, the function can be called in the following two ways: 

```python
my_function(5, 6, z=0.7)
my_function(3.14, 7, 3.5)
my_function(10, 20)
```

The main limitation of function arguments is that the keyword argument must follow the positional argument, if any. You can specify keyword arguments in any order. In other words, you don't have to memorize the order of function arguments, just remember their names.

>Note: You can also pass location arguments with keywords. The previous example can also be written as:
>```python
>my_function(x=5, y=6, z=7)
>my_function(y=6, x=5, z=7)
>```
>This writing can improve readability.

### Namespaces, Scopes, and Local Functions
Function can access variables in two different scopes: global and local. Python has a more scientific name for describing the scope of variables, namely namespace. Any variable assigned in a function is assigned to a local namespace by default. The local namespace is created when the function is called, and the function arguments are immediately filled in the namespace. After the function is executed, the local namespace is destroyed (with some exceptions, see the section on closures later). Look at the following function:

```python
def func():
    a = []
    for i in range(5):
        a.append(i)
```

When func () is called, first an empty list a is created, then five elements are added, and finally a is destroyed when the function exits. Suppose we define a as follows:

```python
a = []
def func():
    for i in range(5):
        a.append(i)
```

We can assign to global variables in a function, but those variables must be declared global using the global keyword:

```python
In [168]: a = None

In [169]: def bind_a_variable():
   .....:     global a
   .....:     a = []
   .....: bind_a_variable()
   .....:

In [170]: print(a)
[]
```

>Note: I often advise people not to use the global keyword frequently. Because global variables are generally used to store some states of the system. If you find yourself using a lot, it might be time for more object-oriented programming (that is, using classes).  

### Returns Multiple Values
When I first programmed in Python (used to Java and C + +), one of my favorite functions was the ability to return multiple values. Here's a simple example:

```python
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c

a, b, c = f()
```

In data analysis and other scientific computing applications, you will find that you often do this. This function actually returns only one object, that is, a tuple, which is finally unpacked into each result variable. In the above example, we can also write:

```python
return_value = f()
```

Here return_value will be a ternary tuple with three return values. In addition, there is a very attractive way to return multivalued values—returning dictionaries:

```python
def f():
    a = 5
    b = 6
    c = 7
    return {'a' : a, 'b' : b, 'c' : c}
```

The second method may be useful depending on the content of the work.

### Functions are Also Objects
Because Python functions are all objects, some design ideas that are difficult to be expressed in other languages are much simpler in Python. Suppose we have an array of strings that we want to do some data cleansing and perform a bunch of transformations on:

```python
In [171]: states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
   .....:           'south   carolina##', 'West virginia?']
```

Whoever has processed the survey data submitted by users can understand what this messy data is all about. In order to get a set of uniformly formed strings that can be used for parsing, many things need to be done: remove white spaces, delete all kinds of punctuation marks, correct uppercase format, and so on. One way to do this is to use the built-in string method and regular expression ` re ` module:

```python
import re

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result
```

The results are as follows:

```python
In [173]: clean_strings(states)
Out[173]: 
['Alabama',
 'Georgia',
 'Georgia',
 'Georgia',
 'Florida',
 'South   Carolina',
 'West Virginia']
```

There's another good way to do this: make a list of all the operations that need to be performed on a given set of strings:

```python
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
```

Then

```python
In [175]: clean_strings(states, clean_ops)
Out[175]: 
['Alabama',
 'Georgia',
 'Georgia',
 'Georgia',
 'Florida',
 'South   Carolina',
 'West Virginia']
```

This multi-function mode enables you to easily modify the conversion mode of strings at a high level. At this time, clean_strings is also more reusable! 

You can also use functions as arguments to other functions, such as the built-in map function, which is used to apply a function to a set of data: 

```python
In [176]: for x in map(remove_punctuation, states):
   .....:     print(x)
Alabama 
Georgia
Georgia
georgia
FlOrIda
south   carolina
West virginia
```

### Lambda
Python supports a function called lambda. It consists of only a single statement, and the result of this statement is the return value. It is defined by the lambda keyword, which has no other meaning than "what we are declaring is a lambda".

```python
def short_function(x):
    return x * 2

equiv_anon = lambda x: x * 2
```

In the rest of this book, it is generally called lambda. They are very convenient in data analysis, because you will find that many data conversion functions take functions as arguments. Passing in a lambda directly is much less (and clearer) than writing a complete function declaration, and even much less than assigning a lambda to a variable. Take a look at this silly simple example:

```python
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)
```

Although you can write [x * 2for x in ints] directly, here we can very easily pass a custom operation to the **apply_to_list**

Let's do another example. Suppose you have a set of strings and you want to sort them by the number of different letters in each string:  

```python
In [177]: strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
```

Here, we can pass a lambda function to the list's sort method:

```python
In [178]: strings.sort(key=lambda x: len(set(list(x))))

In [179]: strings
Out[179]: ['aaaa', 'foo', 'abab', 'bar', 'card']
```

>Note: One of the reasons lambda are called anonymous function, unlike def declared functions, is that the function object itself does not provide the __name__ attribute.

### Currying: Partial Argument Application
Currying is an interesting computer science term that refers to the technique of deriving a new function from an existing function through "partial argument application." For example, suppose we have a simple function that performs the addition of two numbers:

```python
def add_numbers(x, y):
    return x + y
```

From this function, we can derive a new function with only one argument — add_five, which is used to add 5 to its argument:

```python
add_five = lambda y: add_numbers(5, y)
```

The second argument of add_numbers is called "curried". There's nothing particularly fancy here, because we're just defining a new function that can call an existing one. The built-in functools module simplifies this process with the partial function:
```python
from functools import partial
add_five = partial(add_numbers, 5)
```

### Generator
The ability to iterate through sequences (such as objects in a list or lines in a file) in a consistent manner is an important feature of Python. It is realized through iterator protocol, a native way of making objects iterable. For example, iterating over a dictionary can get all its keys:

```python
In [180]: some_dict = {'a': 1, 'b': 2, 'c': 3}

In [181]: for key in some_dict:
   .....:     print(key)
a
b
c
```

When you write **for key in some_dict**, the Python interpreter first tries to create an iterator from **some_dict**:

```python
In [182]: dict_iterator = iter(some_dict)

In [183]: dict_iterator
Out[183]: <dict_keyiterator at 0x7fbbd5a9f908>
```

An iterator is a special object that feeds objects to a Python interpreter in a context such as a for loop. Most methods that can accept objects such as lists can also accept any iterable object. For example, built-in methods such as min, max and sum, and type constructors such as list and tuple:

```python
In [184]: list(dict_iterator)
Out[184]: ['a', 'b', 'c']
```

Generator is a simple way to construct new iterative objects. While a normal function returns only a single value after execution, the generator returns a sequence of values in a delayed manner, that is, pauses after each value is returned until the next value is requested. To create a generator, simply replace **return** with **yeild** in the function:

```python
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2
```

When the generator is called, no code is executed immediately:

```python
In [186]: gen = squares()

In [187]: gen
Out[187]: <generator object squares at 0x7fbbd5ab4570>
```

It doesn't start executing its code until you request an element from the generator:
```python
In [188]: for x in gen:
   .....:     print(x, end=' ')
Generating squares from 1 to 100
1 4 9 16 25 36 49 64 81 100
```

### Generator Expression
A more concise way to construct a generator is to use a generator expression. This is a generator similar to list, dictionary and set derivation. It is created by changing the **[ ]square brackets** at both ends of the list derivation into **( )parentheses**:

```python
In [189]: gen = (x ** 2 for x in range(100))

In [190]: gen
Out[190]: <generator object <genexpr> at 0x7fbbd5ab29e8>
```

It is completely equivalent to the following much more verbose generator:

```python
def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()
```

The generator expression can also replace the list derivation as a function parameter:
```python
In [191]: sum(x ** 2 for x in range(100))
Out[191]: 328350

In [192]: dict((i, i **2) for i in range(5))
Out[192]: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Itertools Module
The standard library itertools module has a set of generators for many common data algorithms. For example, groupby can accept any sequence and a function. It groups successive elements in a sequence according to the return value of a function. Here's an example:

```python
In [193]: import itertools

In [194]: first_letter = lambda x: x[0]

In [195]: names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']

In [196]: for letter, names in itertools.groupby(names, first_letter):
   .....:     print(letter, list(names)) # names is a generator
A ['Alan', 'Adam']
W ['Wes', 'Will']
A ['Albert']
S ['Steven']
```

Table 3-2 lists some itertools functions that I often use. It is recommended to refer to Python official documents for further study.

![Table 3-2 Some Useful Itertools Function](images\1246.jpg)

### Error and Exception Handling
Handling Python errors and exceptions gracefully is an important part of building robust programs. In data analysis, many functions are only used for partial input. For example, Python's float function converts a string to a floating-point number, but there is a ` ValueError ` error when the input is incorrect:

```python
In [197]: float('1.2345')
Out[197]: 1.2345

In [198]: float('something')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-198-439904410854> in <module>()
----> 1 float('something')
ValueError: could not convert string to float: 'something'
```

If you want to handle float errors gracefully let it return the input value. We can write a function that calls **float** in **try/except**:

```python
def attempt_float(x):
    try:
        return float(x)
    except:
        return x
```

Only when **float (x)** throws an exception will the except part be executed:

```python
In [200]: attempt_float('1.2345')
Out[200]: 1.2345

In [201]: attempt_float('something')
Out[201]: 'something'
```

You may notice that float throws an exception that is not just a ValueError:

```python
In [202]: float((1, 2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-202-842079ebb635> in <module>()
----> 1 float((1, 2))
TypeError: float() argument must be a string or a number, not 'tuple'
```

You may only want to deal with ValueErrors. TypeError errors (input is not a string or numeric value) may be reasonable bugs. You can write an exception type:

```python
def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x
```

Then:

```python
In [204]: attempt_float((1, 2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-204-9bdfd730cead> in <module>()
----> 1 attempt_float((1, 2))
<ipython-input-203-3e06b8379b6b> in attempt_float(x)
      1 def attempt_float(x):
      2     try:
----> 3         return float(x)
      4     except ValueError:
      5         return x
TypeError: float() argument must be a string or a number, not 'tuple'
```

You can contain multiple exceptions with tuples:

```python
def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x
```

In some cases, you may not want to suppress exceptions, and you want to execute a piece of code regardless of whether the **try** part of the code succeeds or not. You can use **finally**:

```python
f = open(path, 'w')

try:
    write_to_file(f)
finally:
    f.close()
```

Here, file processing f is always turned off. Similarly, you can use **else** to execute code only if **try** is partially successful:

```python
f = open(path, 'w')

try:
    write_to_file(f)
except:
    print('Failed')
else:
    print('Succeeded')
finally:
    f.close()
```

### Exceptions for IPython
If an exception is thrown while running a script or a statement, IPython will print the full traceback by default, with several lines of context at each point in the traceback:

```python
In [10]: %run examples/ipython_bug.py
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
/home/wesm/code/pydata-book/examples/ipython_bug.py in <module>()
     13     throws_an_exception()
     14
---> 15 calling_things()

/home/wesm/code/pydata-book/examples/ipython_bug.py in calling_things()
     11 def calling_things():
     12     works_fine()
---> 13     throws_an_exception()
     14
     15 calling_things()

/home/wesm/code/pydata-book/examples/ipython_bug.py in throws_an_exception()
      7     a = 5
      8     b = 6
----> 9     assert(a + b == 10)
     10
     11 def calling_things():

AssertionError:
```

Having text on its own is a great advantage over Python standard interpreters. You can use the magic command  `% xmode `  to control the amount of text displayed from Plain (the same as the Python standard interpreter) to Verbose (argument with function). As you'll see later, after an error occurs, you can go into the stack (with% debug or %pdb magics) for post-debugging.

### Files and Operating Systems
Most of the code examples in this book use advanced tools such as pandas.read_csv to read data files on disk into Python data structures. However, we still need to know some basic knowledge about Python file processing. Fortunately, it is inherently simple, which is one of the reasons Python is so popular in text and file processing.

To open a file for reading and writing, use the built-in open function and a relative or absolute file path:

```python
In [207]: path = 'examples/segismundo.txt'

In [208]: f = open(path)
```

By default, files are opened in read-only mode ('r '). Then, we can treat the file handle f like a list, such as iterating over lines:

```python
for line in f:
    pass
```

Lines fetched from a file have the full line terminator (EOL), so you often see code like this (getting a set of lines without EOL):

```python
In [209]: lines = [x.rstrip() for x in open(path)]

In [210]: lines
Out[210]: 
['Sueña el rico en su riqueza,',
 'que más cuidados le ofrece;',
 '',
 'sueña el pobre que padece',
 'su miseria y su pobreza;',
 '',
 'sueña el que a medrar empieza,',
 'sueña el que afana y pretende,',
 'sueña el que agravia y ofende,',
 '',
 'y en el mundo, en conclusión,',
 'todos sueñan lo que son,',
 'aunque ninguno lo entiende.',
 '']
```

If you use **open** to create a file object, be sure to close it with **close**. Close the file to return operating system resources:

```python
In [211]: f.close()
```

The **with** statement makes it easier to clean up open files:
```python
In [212]: with open(path) as f:
   .....:     lines = [x.rstrip() for x in f]
```

This can automatically close the file when exiting the code block.

If you type **F = open (path, 'W')**, a new file will be created in *examples/segismundo.txt*, overwriting any original data at that location. There is also an x file schema that can create writable files, but cannot if the file path exists. Table 3-3 lists all the read/write modes.

![Table 3-3 File Modes of Python](images\1247.jpg)

For readable files, some common methods are **read**, **seek** and **tell**. **Read** returns characters from the file. The content of the character is determined by the encoding of the file (such as UTF-8). If it is opened in binary mode, it is the original byte:

```python
In [213]: f = open(path)

In [214]: f.read(10)
Out[214]: 'Sueña el r'

In [215]: f2 = open(path, 'rb')  # Binary mode

In [216]: f2.read(10)
Out[216]: b'Sue\xc3\xb1a el '
```

The read mode advances the position of the file handle by the number of bytes read. Tell can give the current location:

```python
In [217]: f.tell()
Out[217]: 11

In [218]: f2.tell()
Out[218]: 10
```

Although we read 10 characters from the file, the position is 11, because it took so many bytes to decode the 10 characters with the default encoding. You can use the sys module to check the default encoding:

```python
In [219]: import sys

In [220]: sys.getdefaultencoding()
Out[220]: 'utf-8'
```

Seek changes the file location to the specified byte in the file:

```python
In [221]: f.seek(3)
Out[221]: 3

In [222]: f.read(1)
Out[222]: 'ñ'
```

Finally, close the file:

```python
In [223]: f.close()

In [224]: f2.close()
```

To write to a file, you can use the write or writines method of the file. For example, we could create a blank-line version of prof_mod. py:

```python
In [225]: with open('tmp.txt', 'w') as handle:
   .....:     handle.writelines(x for x in open(path) if len(x) > 1)

In [226]: with open('tmp.txt') as f:
   .....:     lines = f.readlines()

In [227]: lines
Out[227]: 
['Sueña el rico en su riqueza,\n',
 'que más cuidados le ofrece;\n',
 'sueña el pobre que padece\n',
 'su miseria y su pobreza;\n',
 'sueña el que a medrar empieza,\n',
 'sueña el que afana y pretende,\n',
 'sueña el que agravia y ofende,\n',
 'y en el mundo, en conclusión,\n',
 'todos sueñan lo que son,\n',
 'aunque ninguno lo entiende.\n']
```

Table 3-4 lists some of the most commonly used file methods.

![Table 3-4 Important File Methods or Attributes of Python](images\1248.jpg)

### Bytes and Unicode of the file
The default operation for Python files is "text mode," which means you need to process Python strings (i.e. Unicode). It is opposite to "binary mode", and file mode is added with a b. Let's look at the file in the previous section (UTF-8 encoded with non-ASCII characters):

```python
In [230]: with open(path) as f:
   .....:     chars = f.read(10)

In [231]: chars
Out[231]: 'Sueña el r'
```

UTF-8 is a variable-length Unicode encoding, so when I request a certain number of characters from a file, Python reads enough bytes (maybe as little as 10 bytes or as much as 40 bytes) from the file to decode. If the file is opened in "rb" mode, the exact number of requested bytes is read:

```python
In [232]: with open(path, 'rb') as f:
   .....:     data = f.read(10)

In [233]: data
Out[233]: b'Sue\xc3\xb1a el '
```

You can decode bytes into str objects depending on the encoding of the text, but only if each encoded Unicode character is fully shaped: 

```python
In [234]: data.decode('utf8')
Out[234]: 'Sueña el '

In [235]: data[:4].decode('utf8')
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-235-300e0af10bb7> in <module>()
----> 1 data[:4].decode('utf8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc3 in position 3: unexpecte
d end of data
```

Text mode combines the encoding options of open to provide a more convenient way to convert Unicode to another encoding:

```python
In [236]: sink_path = 'sink.txt'

In [237]: with open(path) as source:
   .....:     with open(sink_path, 'xt', encoding='iso-8859-1') as sink:
   .....:         sink.write(source.read())

In [238]: with open(sink_path, encoding='iso-8859-1') as f:
   .....:     print(f.read(10))
Sueña el r
```

Note: Not to use seek in binary mode. If the file location is in the middle of the bytes that define Unicode characters, an error will be generated after reading:

```python
In [240]: f = open(path)

In [241]: f.read(5)
Out[241]: 'Sueña'

In [242]: f.seek(4)
Out[242]: 4

In [243]: f.read(1)
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-243-7841103e33f5> in <module>()
----> 1 f.read(1)
/miniconda/envs/book-env/lib/python3.6/codecs.py in decode(self, input, final)
    319         # decode input (taking the buffer into account)
    320         data = self.buffer + input
--> 321         (result, consumed) = self._buffer_decode(data, self.errors, final
)
    322         # keep undecoded input until the next call
    323         self.buffer = data[consumed:]
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 0: invalid s
tart byte

In [244]: f.close()
```

If you often have to do data analysis on non-ASCII character text, it is important to be familiar with Python's Unicode capabilities. For more information, see Python's official documentation.





