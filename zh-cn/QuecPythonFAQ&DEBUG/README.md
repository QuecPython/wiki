# QuecPythonFAQ&DEBUG

## QuecPython FAQ

[**QuecPython_FAQ&Debug 手册**](https://python.quectel.com/wiki/zh-cn/QuecPythonFAQ&DEBUG/FAQ&Debug.pdf)

### QuecPython异常处理

#### 错误码

QuecPython中定义的各种错误代码常量

| 错误码常量              | 错误码 | 释义                                            |
| ----------------------- | ------ | ----------------------------------------------- |
| QUEC_PY_FAIL            | -1     | Generic failure codes                           |
| QUEC_PY_OK              | 0      | Quec_py value indicating success (no error)     |
| QUEC_PY_EPERM           | 1      | Operation not permitted                         |
| QUEC_PY_ENOENT          | 2      | No such file or directory                       |
| QUEC_PY_ESRCH           | 3      | No such process                                 |
| QUEC_PY_EINTR           | 4      | Interrupted system call                         |
| QUEC_PY_EIO             | 5      | I/O error                                       |
| QUEC_PY_ENXIO           | 6      | No such device or address                       |
| QUEC_PY_E2BIG           | 7      | Argument list too long                          |
| QUEC_PY_ENOEXEC         | 8      | Exec format error                               |
| QUEC_PY_EBADF           | 9      | Bad file number                                 |
| QUEC_PY_ECHILD          | 10     | No child processes                              |
| QUEC_PY_EAGAIN          | 11     | Try again                                       |
| QUEC_PY_ENOMEM          | 12     | Out of memory                                   |
| QUEC_PY_EACCES          | 13     | Permission denied                               |
| QUEC_PY_EFAULT          | 14     | Bad address                                     |
| QUEC_PY_ENOTBLK         | 15     | Block device required                           |
| QUEC_PY_EBUSY           | 16     | Device or resource busy                         |
| QUEC_PY_EEXIST          | 17     | File exists                                     |
| QUEC_PY_EXDEV           | 18     | Cross-device link                               |
| QUEC_PY_ENODEV          | 19     | No such device                                  |
| QUEC_PY_ENOTDIR         | 20     | Not a directory                                 |
| QUEC_PY_EISDIR          | 21     | Is a directory                                  |
| QUEC_PY_EINVAL          | 22     | Invalid argument                                |
| QUEC_PY_ENFILE          | 23     | File table overflow                             |
| QUEC_PY_EMFILE          | 24     | Too many open files                             |
| QUEC_PY_ENOTTY          | 25     | Not a typewriter                                |
| QUEC_PY_ETXTBSY         | 26     | Text file busy                                  |
| QUEC_PY_EFBIG           | 27     | File too large                                  |
| QUEC_PY_ENOSPC          | 28     | No space left on device                         |
| QUEC_PY_ESPIPE          | 29     | Illegal seek                                    |
| QUEC_PY_EROFS           | 30     | Read-only file system                           |
| QUEC_PY_EMLINK          | 31     | Too many links                                  |
| QUEC_PY_EPIPE           | 32     | Broken pipe                                     |
| QUEC_PY_EDOM            | 33     | Math argument out of domain of func             |
| QUEC_PY_ERANGE          | 34     | Math result not representable                   |
| QUEC_PY_EDEADLK         | 35     | Resource deadlock would occur                   |
| QUEC_PY_ENAMETOOLONG    | 36     | File name too long                              |
| QUEC_PY_ENOLCK          | 37     | No record locks available                       |
| QUEC_PY_ENOSYS          | 38     | Function not implemented                        |
| QUEC_PY_ENOTEMPTY       | 39     | Directory not empty                             |
| QUEC_PY_ELOOP           | 40     | Too many symbolic links encountered             |
| QUEC_PY_EWOULDBLOCK     | 41     | Operation would block                           |
| QUEC_PY_ENOMSG          | 42     | No message of desired type                      |
| QUEC_PY_EIDRM           | 43     | Identifier removed                              |
| QUEC_PY_ECHRNG          | 44     | Channel number out of range                     |
| QUEC_PY_EL2NSYNC        | 45     | Level 2 not synchronized                        |
| QUEC_PY_EL3HLT          | 46     | Level 3 halted                                  |
| QUEC_PY_EL3RST          | 47     | Level 3 reset                                   |
| QUEC_PY_ELNRNG          | 48     | Link number out of range                        |
| QUEC_PY_EUNATCH         | 49     | Protocol driver not attached                    |
| QUEC_PY_ENOCSI          | 50     | No CSI structure available                      |
| QUEC_PY_EL2HLT          | 51     | Level 2 halted                                  |
| QUEC_PY_EBADE           | 52     | Invalid exchange                                |
| QUEC_PY_EBADR           | 53     | Invalid request descriptor                      |
| QUEC_PY_EXFULL          | 54     | Exchange full                                   |
| QUEC_PY_ENOANO          | 55     | No anode                                        |
| QUEC_PY_EBADRQC         | 56     | Invalid request code                            |
| QUEC_PY_EBADSLT         | 57     | Invalid slot                                    |
| QUEC_PY_EDEADLOCK       | 58     | Deadlock                                        |
| QUEC_PY_EBFONT          | 59     | Bad font file format                            |
| QUEC_PY_ENOSTR          | 60     | Device not a stream                             |
| QUEC_PY_ENODATA         | 61     | No data available                               |
| QUEC_PY_ETIME           | 62     | Timer expired                                   |
| QUEC_PY_ENOSR           | 63     | Out of streams resources                        |
| QUEC_PY_ENONET          | 64     | Machine is not on the network                   |
| QUEC_PY_ENOPKG          | 65     | Package not installed                           |
| QUEC_PY_EREMOTE         | 66     | Object is remote                                |
| QUEC_PY_ENOLINK         | 67     | Link has been severed                           |
| QUEC_PY_EADV            | 68     | Advertise error                                 |
| QUEC_PY_ESRMNT          | 69     | Srmount error                                   |
| QUEC_PY_ECOMM           | 70     | Communication error on send                     |
| QUEC_PY_EPROTO          | 71     | Protocol error                                  |
| QUEC_PY_EMULTIHOP       | 72     | Multihop attempted                              |
| QUEC_PY_EDOTDOT         | 73     | RFS specific error                              |
| QUEC_PY_EBADMSG         | 74     | Not a data message                              |
| QUEC_PY_EOVERFLOW       | 75     | Value too large for defined data type           |
| QUEC_PY_ENOTUNIQ        | 76     | Name not unique on network                      |
| QUEC_PY_EBADFD          | 77     | File descriptor in bad state                    |
| QUEC_PY_EREMCHG         | 78     | Remote address changed                          |
| QUEC_PY_ELIBACC         | 79     | Can not access a needed shared library          |
| QUEC_PY_ELIBBAD         | 80     | Accessing a corrupted shared library            |
| QUEC_PY_ELIBSCN         | 81     | .lib section in a.out corrupted                 |
| QUEC_PY_ELIBMAX         | 82     | Attempting to link in too many shared libraries |
| QUEC_PY_ELIBEXEC        | 83     | Cannot exec a shared library directly           |
| QUEC_PY_EILSEQ          | 84     | Illegal byte sequence                           |
| QUEC_PY_ERESTART        | 85     | Interrupted system call should be restarted     |
| QUEC_PY_ESTRPIPE        | 86     | Streams pipe error                              |
| QUEC_PY_EUSERS          | 87     | Too many users                                  |
| QUEC_PY_ENOTSOCK        | 88     | Socket operation on non-socket                  |
| QUEC_PY_EDESTADDRREQ    | 89     | Destination address required                    |
| QUEC_PY_EMSGSIZE        | 90     | Message too long                                |
| QUEC_PY_EPROTOTYPE      | 91     | Protocol wrong type for socket                  |
| QUEC_PY_ENOPROTOOPT     | 92     | Protocol not available                          |
| QUEC_PY_EPROTONOSUPPORT | 93     | Protocol not supported                          |
| QUEC_PY_ESOCKTNOSUPPORT | 94     | Socket type not supported                       |
| QUEC_PY_EOPNOTSUPP      | 95     | Operation not supported on transport endpoint   |
| QUEC_PY_EAFNOSUPPORT    | 97     | Address family not supported by protocol        |
| QUEC_PY_EADDRINUSE      | 98     | Address already in use                          |
| QUEC_PY_ECONNABORTED    | 103    | Software caused connection abort                |
| QUEC_PY_ECONNRESET      | 104    | Connection reset by peer                        |
| QUEC_PY_ENOBUFS         | 105    | No buffer space available                       |
| QUEC_PY_EISCONN         | 106    | Transport endpoint is already connected         |
| QUEC_PY_ENOTCONN        | 107    | Transport endpoint is not connected             |
| QUEC_PY_ETIMEDOUT       | 110    | Connection timed out                            |
| QUEC_PY_ECONNREFUSED    | 111    | Connection refused                              |
| QUEC_PY_EHOSTUNREACH    | 113    | No route to host                                |
| QUEC_PY_EALREADY        | 114    | Operation already in progress                   |
| QUEC_PY_EINPROGRESS     | 115    | Operation now in progress                       |

#### 错误码到错误消息

```python
import uerrno.errno_to_str()

# 暂未实现
errInfo = uerrno.errno_to_str()
print(errInfo)
```

### QuecPython异常检查流程

#### 异常重启处理

固件版本默认是业务模式，即出现底层异常错误时会自动重启，防止模块程序停止导致无法使用。当我们处于调试期时需要暴露并定位问题原因，此时需要设置三条AT指令（AT口执行）：

- at+qdumpcfg=0,0
- at+qdumpcfg=1,0
- at+log=19,1

依次执行上述三条AT指令即可进入调试模式，此时若出现底层异常错误则会进入DUMP模式，出现DUMP端口，此时您可以有两种选择：

**方法一**：提供固件版本、测试步骤及测试代码，前往QuecPython官网提交问题工单
**方法二**：使用Tera term窗口调试工具（使用方法：百度即可）抓取Dumplog，同时提供固件版本、测试步骤及测试代码，前往QuecPython官网提交问题工单，节省复现问题时间。

**需要注意此指令重启后仍然生效，如需退出调试模式，重新烧录固件版本即可。**

