# QuecPython Exception Handling Manual

## QuecPython Error Codes

Various error code constants defined in QuecPython (Continuously Updated)

| Error Code Constant     | Error Code | Description                                     |
| ----------------------- | ---------- | ----------------------------------------------- |
| QUEC_PY_FAIL            | -1         | Generic failure codes                           |
| QUEC_PY_OK              | 0          | Quec_py value indicating success (no error)     |
| QUEC_PY_EPERM           | 1          | Operation not permitted                         |
| QUEC_PY_ENOENT          | 2          | No such file or directory                       |
| QUEC_PY_ESRCH           | 3          | No such process                                 |
| QUEC_PY_EINTR           | 4          | Interrupted system call                         |
| QUEC_PY_EIO             | 5          | I/O error                                       |
| QUEC_PY_ENXIO           | 6          | No such device or address                       |
| QUEC_PY_E2BIG           | 7          | Argument list too long                          |
| QUEC_PY_ENOEXEC         | 8          | Exec format error                               |
| QUEC_PY_EBADF           | 9          | Bad file number                                 |
| QUEC_PY_ECHILD          | 10         | No child processes                              |
| QUEC_PY_EAGAIN          | 11         | Try again                                       |
| QUEC_PY_ENOMEM          | 12         | Out of memory                                   |
| QUEC_PY_EACCES          | 13         | Permission denied                               |
| QUEC_PY_EFAULT          | 14         | Bad address                                     |
| QUEC_PY_ENOTBLK         | 15         | Block device required                           |
| QUEC_PY_EBUSY           | 16         | Device or resource busy                         |
| QUEC_PY_EEXIST          | 17         | File exists                                     |
| QUEC_PY_EXDEV           | 18         | Cross-device link                               |
| QUEC_PY_ENODEV          | 19         | No such device                                  |
| QUEC_PY_ENOTDIR         | 20         | Not a directory                                 |
| QUEC_PY_EISDIR          | 21         | Is a directory                                  |
| QUEC_PY_EINVAL          | 22         | Invalid argument                                |
| QUEC_PY_ENFILE          | 23         | File table overflow                             |
| QUEC_PY_EMFILE          | 24         | Too many open files                             |
| QUEC_PY_ENOTTY          | 25         | Not a typewriter                                |
| QUEC_PY_ETXTBSY         | 26         | Text file busy                                  |
| QUEC_PY_EFBIG           | 27         | File too large                                  |
| QUEC_PY_ENOSPC          | 28         | No space left on device                         |
| QUEC_PY_ESPIPE          | 29         | Illegal seek                                    |
| QUEC_PY_EROFS           | 30         | Read-only file system                           |
| QUEC_PY_EMLINK          | 31         | Too many links                                  |
| QUEC_PY_EPIPE           | 32         | Broken pipe                                     |
| QUEC_PY_EDOM            | 33         | Math argument out of domain of func             |
| QUEC_PY_ERANGE          | 34         | Math result not representable                   |
| QUEC_PY_EDEADLK         | 35         | Resource deadlock would occur                   |
| QUEC_PY_ENAMETOOLONG    | 36         | File name too long                              |
| QUEC_PY_ENOLCK          | 37         | No record locks available                       |
| QUEC_PY_ENOSYS          | 38         | Function not implemented                        |
| QUEC_PY_ENOTEMPTY       | 39         | Directory not empty                             |
| QUEC_PY_ELOOP           | 40         | Too many symbolic links encountered             |
| QUEC_PY_EWOULDBLOCK     | 41         | Operation would block                           |
| QUEC_PY_ENOMSG          | 42         | No message of desired type                      |
| QUEC_PY_EIDRM           | 43         | Identifier removed                              |
| QUEC_PY_ECHRNG          | 44         | Channel number out of range                     |
| QUEC_PY_EL2NSYNC        | 45         | Level 2 not synchronized                        |
| QUEC_PY_EL3HLT          | 46         | Level 3 halted                                  |
| QUEC_PY_EL3RST          | 47         | Level 3 reset                                   |
| QUEC_PY_ELNRNG          | 48         | Link number out of range                        |
| QUEC_PY_EUNATCH         | 49         | Protocol driver not attached                    |
| QUEC_PY_ENOCSI          | 50         | No CSI structure available                      |
| QUEC_PY_EL2HLT          | 51         | Level 2 halted                                  |
| QUEC_PY_EBADE           | 52         | Invalid exchange                                |
| QUEC_PY_EBADR           | 53         | Invalid request descriptor                      |
| QUEC_PY_EXFULL          | 54         | Exchange full                                   |
| QUEC_PY_ENOANO          | 55         | No anode                                        |
| QUEC_PY_EBADRQC         | 56         | Invalid request code                            |
| QUEC_PY_EBADSLT         | 57         | Invalid slot                                    |
| QUEC_PY_EDEADLOCK       | 58         | Deadlock                                        |
| QUEC_PY_EBFONT          | 59         | Bad font file format                            |
| QUEC_PY_ENOSTR          | 60         | Device not a stream                             |
| QUEC_PY_ENODATA         | 61         | No data available                               |
| QUEC_PY_ETIME           | 62         | Timer expired                                   |
| QUEC_PY_ENOSR           | 63         | Out of streams resources                        |
| QUEC_PY_ENONET          | 64         | Machine is not on the network                   |
| QUEC_PY_ENOPKG          | 65         | Package not installed                           |
| QUEC_PY_EREMOTE         | 66         | Object is remote                                |
| QUEC_PY_ENOLINK         | 67         | Link has been severed                           |
| QUEC_PY_EADV            | 68         | Advertise error                                 |
| QUEC_PY_ESRMNT          | 69         | Srmount error                                   |
| QUEC_PY_ECOMM           | 70         | Communication error on send                     |
| QUEC_PY_EPROTO          | 71         | Protocol error                                  |
| QUEC_PY_EMULTIHOP       | 72         | Multihop attempted                              |
| QUEC_PY_EDOTDOT         | 73         | RFS specific error                              |
| QUEC_PY_EBADMSG         | 74         | Not a data message                              |
| QUEC_PY_EOVERFLOW       | 75         | Value too large for defined data type           |
| QUEC_PY_ENOTUNIQ        | 76         | Name not unique on network                      |
| QUEC_PY_EBADFD          | 77         | File descriptor in bad state                    |
| QUEC_PY_EREMCHG         | 78         | Remote address changed                          |
| QUEC_PY_ELIBACC         | 79         | Can not access a needed shared library          |
| QUEC_PY_ELIBBAD         | 80         | Accessing a corrupted shared library            |
| QUEC_PY_ELIBSCN         | 81         | .lib section in a.out corrupted                 |
| QUEC_PY_ELIBMAX         | 82         | Attempting to link in too many shared libraries |
| QUEC_PY_ELIBEXEC        | 83         | Cannot exec a shared library directly           |
| QUEC_PY_EILSEQ          | 84         | Illegal byte sequence                           |
| QUEC_PY_ERESTART        | 85         | Interrupted system call should be restarted     |
| QUEC_PY_ESTRPIPE        | 86         | Streams pipe error                              |
| QUEC_PY_EUSERS          | 87         | Too many users                                  |
| QUEC_PY_ENOTSOCK        | 88         | Socket operation on non-socket                  |
| QUEC_PY_EDESTADDRREQ    | 89         | Destination address required                    |
| QUEC_PY_EMSGSIZE        | 90         | Message too long                                |
| QUEC_PY_EPROTOTYPE      | 91         | Protocol wrong type for socket                  |
| QUEC_PY_ENOPROTOOPT     | 92         | Protocol not available                          |
| QUEC_PY_EPROTONOSUPPORT | 93         | Protocol not supported                          |
| QUEC_PY_ESOCKTNOSUPPORT | 94         | Socket type not supported                       |
| QUEC_PY_EOPNOTSUPP      | 95         | Operation not supported on transport endpoint   |
| QUEC_PY_EAFNOSUPPORT    | 97         | Address family not supported by protocol        |
| QUEC_PY_EADDRINUSE      | 98         | Address already in use                          |
| QUEC_PY_ECONNABORTED    | 103        | Software caused connection abort                |
| QUEC_PY_ECONNRESET      | 104        | Connection reset by peer                        |
| QUEC_PY_ENOBUFS         | 105        | No buffer space available                       |
| QUEC_PY_EISCONN         | 106        | Transport endpoint is already connected         |
| QUEC_PY_ENOTCONN        | 107        | Transport endpoint is not connected             |
| QUEC_PY_ETIMEDOUT       | 110        | Connection timed out                            |
| QUEC_PY_ECONNREFUSED    | 111        | Connection refused                              |
| QUEC_PY_EHOSTUNREACH    | 113        | No route to host                                |
| QUEC_PY_EALREADY        | 114        | Operation already in progress                   |
| QUEC_PY_EINPROGRESS     | 115        | Operation now in progress                       |

### Error Code to Error Message

```python
import uerrno.errno_to_str()

# Not yet realized
errInfo = uerrno.errno_to_str()
print(errInfo)
```

## QuecPython Exception Checking Process

### Abnormal Reboot Handling

The firmware version is the business mode by default, that is, it will automatically reboot when the underlying abnormal error occurs, so as to prevent the module program from stopping and being unusable. In the debugging period, we need to expose and locate the cause of the problem. At this time, we need to set three AT commands (AT port execution): 

- at+qdumpcfg=0,0
- at+qdumpcfg=1,0
- at+log=19,1

Execute the above three AT commands in turn to enter debug mode. If there is an underlying exception error, it will enter DUMP mode and DUMP port will appear. At this time, you have two choices:

* Method 1 : Provide firmware version, test steps and test code, and go to **QuecPython** official website to submit problem work orders
*  Method 2 : Use Tera term window debugging tool (search for how to use this tool by Google) to crawl Dumpllog, provide firmware version, test steps and test code, and go to **QuecPython** official website to submit problem work orders, saving time for reappearing problems. 

**Note: These commands still take effect after rebooting. If you need to exit debug mode, you can burn the firmware version again.**

## Meaning and Use of QuecPython Power up/down Reason

### Register Meaning

#### power_up_reason

Corresponding register: NINGBO_PWRUP_LOG_REG
Meaning of each bit:

| 0x01: bit0 | onkey hardware to power up  |
| ---------- | :-------------------------- |
| 0x02: bit1 | exton1 hardware to power up |
| 0x04: bit2 | exton2 hardware to power up |
| 0x08: bit3 | bat hardware to power up    |
| 0x10: bit4 | rtc_alarm to power up       |
| 0x20: bit5 | fault to power up           |
| 0x40: bit6 | vbus_detect to power up     |

>
> Currently in use：exton1 hardware to power up (Powerkey hardware is connected to exton1), fault  to power up, vbus_detect to power up.

#### power_down_reason

Corresponding: NINGBO_POWERDOWN_LOG_REG
Meaning of each bit:

| 0x01: bit0 | over temperature to power down                             |
| ---------- | :--------------------------------------------------------- |
| 0x02: bit1 | PMIC VINLDO Voltage below 2.9 V to power down              |
| 0x04: bit2 | SW_PDOWN software calls power_down interface to power down |
| 0x08: bit3 | None                                                       |
| 0x10: bit4 | PMIC watch dog to power down                               |
| 0x20: bit5 | long press of ONKEY to power down                          |
| 0x40: bit6 | VINLDO overtension to power down                           |
| 0x80: bit7 | VRTC LOW to power down                                     |

>
> The long press of ONKEY power down is not currently in use.

#### power_down_reason2

Only the power_down_reason register is focused on currently , which does not need to be used.

### Reasons for Power-up

#### Up/Down Process

**1.  Long press powerkey to power down ** 
A long press action is detected and finally PMIC_SW_PDOWN is called.

**2. Hardware RESET** 
The CPU RESET pin is called, the PMIC is not powered down, and the PWRUP_LOG_REG and POWERDOWN_LOG_REG registers are not updated.

**3. Software RESET** 
A. If PMIC_SW_RESET is called, FAULT_WAKEUP is enabled first, then SW_PDOWN is called, and then FAULT wakes up and reboots. 
B. If abnormal reboot similar hardware RESET, only CPU RESET, PMIC does not power down. 

**4. Press powerkey to power up**
exton1 hardware to power up.

**5. Plug in USB to power up**
vbus_detect to power up.

#### Acquisition of Reasons for Power-up

After reading power_down_reason every time you boot, its flag will be cleared, and power_up_reason will not be cleared. 

**1. powerkey**
Power_up_reason==0x02，power_down_reason!=0.

**2. Hardware, abnormal RESET**
Since the PMIC does not power down, the PWRUP_LOG_REG register will not be updated, and the POWERDOWN_LOG_REG register will be cleared, so power_up_reason==0x02 and power_down_reason==0 are required. Or power_up_reason==0x40, and power_down_reason==0.

**3. Software RESET**
If USB is plugged in, power_up_reason==0x60 and power_down_reason==0x04 are required.

**4. Vbus**
Power_up_reason==0x40，且power_down_reason!=0x00.

**5. Other reasons for power-up are obtained by bit meaning after the foregoing reasons.**

### Reasons for Power-down

It can be obtained according to the meaning of bit as in the code.

### Use of Power-on/down Reason Interface

At present, both boot side and kernel side provide power-on/down reason interface. Because the power-on/down reason flag in POWERDOWN_LOG_REG register needs to be cleared after obtaining power-on/down reason, if this interface is called on boot side, it cannot be called on kernel side, otherwise the obtained value will be abnormal. Now the boot-side interface is not called by default.

