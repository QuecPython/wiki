#### example -Python Script Execution

Function: Provides the method to execute Python script  from command line.

> example.exec(filePath)

This function specifies the Python script to be executed. 

* Parameter

| Parameter | Type   | Description                                            |
| --------- | ------ | ------------------------------------------------------ |
| filePath  | string | The absolute path of the python script to be executed. |

* Return Value

NA

* Example

```python
#Suppose there is a file test.py with the following content:

def myprint():
    count = 10
    while count > 0:
        count -= 1
        print('##### test #####')

myprint()

#Upload the file test.py to the module, and executing the following code from the command line. 
>>> uos.listdir('/usr/')
['apn_cfg.json', 'test.py']
>>> import example
>>> example.exec('/usr/test.py')
# Execution results are as follow.

##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
```



#### dataCall - Data Call

Function: Provides  the data call related interface.

##### Dial-Up

> **dataCall.start(profileIdx, ipType, apn, username, password, authType)**

This function starts the dial-up and activates the data link.

* Parameter

| Parameter  | Type   | Description                                                  |
| ---------- | ------ | ------------------------------------------------------------ |
| profileIdx | int    | PDP context index. Range: 1-8. It is generally set to 1, if set as 2-8, the private APN and password may be required. |
| ipType     | int    | IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6.                    |
| apn        | string | Optional. APN name. The maximum length is 63 bytes.          |
| username   | string | Optional. APN user name.  The maximum length is 15 bytes.    |
| password   | string | Optional. APN password. The maximum length is 15 bytes.      |
| authType   | int    | Authentication type. 0-No authentication, 1-PAP, 2-CHAP.     |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform does not support this method.

* Example

```python
>>> import dataCall
>>> dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
0
```



##### Configure APN Information

> **dataCall.setApn(profileIdx, ipType, apn, username, password, authType)**

After calling this interface, the user_apn.json will be created in the user partition to save the APN configurations.

* Parameter

| Parameter  | Type   | Description                                                  |
| ---------- | ------ | ------------------------------------------------------------ |
| profileIdx | int    | PDP context index. Range: 1-8. It is generally set to 1, if set as 2-8, the private APN and password may be required. |
| ipType     | int    | IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6.                    |
| apn        | string | Optional. APN name. The maximum length is 63 bytes.          |
| username   | string | Optional. APN user name.  The maximum length is 15 bytes.    |
| password   | string | Optional. APN password. The maximum length is 15 bytes.      |
| authType   | int    | Authentication type. 0-No authentication, 1-PAP, 2-CHAP.     |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform does not support this method.
* Example

```python
>>> import dataCall
>>> dataCall.setApn(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
0
```



##### Register Callback Function

> **dataCall.setCallback(usrFun)**

This function registers the callback function to send the notification when the network state is changed, such as the network disconnection or connection.

* Parameter

| Parameter | Type     | Description                                     |
| --------- | -------- | ----------------------------------------------- |
| usrFun    | function | Callback function. See example for more details |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform does not support this method.
  
* Example

```python
>>> import dataCall
>>> import net

>>> def nw_cb(args):
		pdp = args[0]
		nw_sta = args[1]
		if nw_sta == 1:
			print("*** network %d connected! ***" % pdp)
		else:
			print("*** network %d not connected! ***" % pdp)
			
>>> dataCall.setCallback(nw_cb)
0
>>> net.setModemFun(4)  # Turns on the airplane mode.
0
>>> *** network 1 not connected! *** # The callback function is triggered when the network disconnection.
>>> net.setModemFun(1)  # Turns off the airplane mode.
0
>>> *** network 1 connected! *** # Turns off the airplane mode and dials up automatically.  The callback function is triggered when the network connection.
```



##### Obtain the Dial-Up Information

> **dataCall.getInfo(profileIdx, ipType)**

This function obtains the dial-up information, such as the connection state, IP address and DNS.

* Parameter

| Parameter  | Type | Description                               |
| ---------- | ---- | ----------------------------------------- |
| profileIdx | int  | PDP context index. Range: 1-8             |
| ipType     | int  | IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6. |

* Return Value

If it failed to obtain the dial-up information, returns -1. If successfully, the dial-up information is returned  in the format shown as follows.

 If ipType =0, the format of the return value is as follows.

`(profileIdx, ipType, [nwState, reconnect, ipv4Addr, priDns, secDns])`

`profileIdx`：PDP context index. Range: 1-8

`ipType`：IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6.

`nwState`： The result of dial-up. 0 indicates the failed dial-up. 1 indicates the successful dial-up.

`reconnect`：The reconnection flag.

`ipv4Addr`：IPv4 address.

`priDns`：Primary DNS.

`secDns`：Secondary DNS.

 If ipType =1, the format of the return value is as follows.

`(profileIdx, ipType, [nwState, reconnect, ipv6Addr, priDns, secDns])`

`profileIdx`：PDP context index. Range: 1-8

`ipType`：IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6.

`nwState`：The result of dial-up. 0 indicates the failed dial-up. 1 indicates the successful dial-up.

`reconnect`：The reconnection flag.

`ipv6Addr`：IPv6 address.

`priDns`：Primary DNS.

`secDns`：Secondary DNS.

 If ipType =2, the format of the return value is as follows.

`(profileIdx, ipType, [nwState, reconnect, ipv4Addr, priDns, secDns], [nwState, reconnect, ipv6Addr, priDns, secDns])`

* Example

```python
>>> import dataCall
>>> dataCall.getInfo(1, 0)
(1, 0, [1, 0, '10.91.44.177', '58.242.2.2', '218.104.78.2'])
```

Note: `(1, 0, [0, 0, '0.0.0.0', '0.0.0.0', '0.0.0.0'])`indicates no dial-up or the dial-up failure.

##### Example

```python
import dataCall
import net
import utime
import checkNet

'''
The following two global variables are required. You can modify the values of these two global variables accordingly.
'''
PROJECT_NAME = "QuecPython_DataCall_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)


state = 1
'''
dataCall.setCallback()
When the network state is changed, such as the network disconnection or connection, the callback function is triggered.
'''
# Define the callback function.
def nw_cb(args):
    global state
    pdp = args[0]   # PDP context index.
    nw_sta = args[1]  # Network connection state. 0-Disconnection. 1-Connection.
    if nw_sta == 1:
        print("*** network %d connected! ***" % pdp)
    else:
        print("*** network %d not connected! ***" % pdp)
    state -= 1


if __name__ == '__main__':
    stagecode, subcode = checknet.wait_network_connected(30)
    if stagecode == 3 and subcode == 1:
    	checknet.poweron_print_once()
   
        # Registers the callback function.
        dataCall.setCallback(nw_cb)

        # Turns on the airplane mode and the callback function is triggered.
        net.setModemFun(4)
        utime.sleep(2)

        # Turns off the airplane mode and the callback function is triggered.
        net.setModemFun(1)

        while 1:
            if state:
                pass
            else:
                break

```



#### cellLocator - Base Station Positioning

Function: Provides base station positioning interface to obtain coordinate information.

* note

  The BC25PA platform does not support this module function.
  
##### Obtain Coordinate Information

> **cellLocator.getLocation(serverAddr, port, token, timeout, profileID)**

This function obtains coordinate information of the base station.

* Parameter

| Parameter  | Type   | Description                                                  |
| ---------- | ------ | ------------------------------------------------------------ |
| serverAddr | string | Server domain name, the length must be less than 255 bytes, currently only supports “www.queclocator.com” |
| port       | int    | Server port, currently only supports port 80                 |
| token      | string | Token, composed of 16 characters                             |
| timeout    | int    | Timeout. Range: 1-300. Default value: 300. Unit: s.          |
| profileID  | int    | PDP index. Range: 1-8.                                       |

* Return Value

If obtain the coordinate information successfully, return the information in the format of：`(latitude, longtitude, accuracy)`，`(0.0, 0.0, 0)` indicates it failed to obtain the coordinate information. The error code returned is explained as follows:

-1 – Initialization failed 

-2 – Server address exceeds 255 bytes

-3 – Token length error, it must be 16 bytes.

-4 – Timeout is out of range.

-5 – PDP error.

-6 – Obtaining error.

* Example

```python
>>> import cellLocator
>>> cellLocator.getLocation("www.queclocator.com", 80, "1111111122222222", 8, 1)
(117.1138, 31.82279, 550)
# The key provided is only for test.
```



#### sim - SIM Card

Function: Provides SIM operations related APIs, such as querying SIM card status, ICCID, IMSI.

Note: The prerequisite for successfully obtaining IMSI, ICCID, and phone number is that the status of the SIM card is 1, which can be queried through sim.getStatus(). 

##### Obtain IMSI

> **sim.getImsi()**

This function obtains the IMSI of SIM card.

* Parameter

NA

* Return Value

Returns IMSI in string type, or returns -1 if failed.

* Example

```python
>>> import sim
>>> sim.getImsi()
'460105466870381'
```



##### Obtain ICCID

> **sim.getIccid()**

This function obtains the ICCID of SIM card.

* Parameter

NA

* Return Value

Returns ICCID in string type, or returns -1 if failed.

* Example

```python
>>> sim.getIccid()
'89860390845513443049'
```



##### Obtain the Phone Number

> **sim.getPhoneNumber()**

This function obtain the phone number of SIM card.

* Parameter

NA

* Return Value

Returns the phone number in string type, or returns -1 if failed.

* note

  The BC25PA platform does not support this method.
  
* Example

```python
>>> sim.getPhoneNumber()
'+8618166328752'
```



##### Obtain the Status of SIM Card

> **sim.getStatus()**

This function obtain the Status of SIM Card

* Parameter

NA

* Return Value

| Return  Value | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| 0             | SIM was removed.                                             |
| 1             | SIM is ready.                                                |
| 2             | Expecting the universal PIN./SIM is locked, waiting for a CHV1 password. |
| 3             | Expecting code to unblock the universal PIN./SIM is blocked, CHV1 unblocking password is required. |
| 4             | SIM is locked due to a SIM/USIM personalization check failure. |
| 5             | SIM is blocked due to an incorrect PCK; an MEP unblocking password is required. |
| 6             | Expecting key for hidden phone book entries.                 |
| 7             | Expecting code to unblock the hidden key.                    |
| 8             | SIM is locked; waiting for a CHV2 password.                  |
| 9             | SIM is blocked; CHV2 unblocking password is required.        |
| 10            | SIM is locked due to a network personalization check failure. |
| 11            | SIM is blocked due to an incorrect NCK; an MEP unblocking password is required. |
| 12            | SIM is locked due to a network subset personalization check failure. |
| 13            | SIM is blocked due to an incorrect NSCK; an MEP unblocking password is required. |
| 14            | SIM is locked due to a service provider personalization check failure. |
| 15            | SIM is blocked due to an incorrect SPCK; an MEP unblocking password is required. |
| 16            | SIM is locked due to a corporate personalization check failure. |
| 17            | SIM is blocked due to an incorrect CCK; an MEP unblocking password is required. |
| 18            | SIM is being initialized; waiting for completion.            |
| 19            | Use of CHV1/CHV2/universal PIN/code to unblock the CHV1/code to unblock the CHV2/code to unblock the universal PIN/ is blocked. |
| 20            | Invalid SIM card.                                            |
| 21            | Unknow status.                                               |



##### Enable PIN Authentication

> **sim.enablePin(pin)**

This function enables PIN authentication, and then you need to enter the correct PIN before the SIM card can be used normally. The SIM card will be locked if the wrong PIN is entered consecutive 3 times and then PUK is required to unlock the SIM card.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| pin       | string | PIN, ‘1234’ is the default, and the maximum length is 15 bytes. |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform pin password supports up to eight digits.
  
* Example

```python
>>> sim.enablePin("1234")
0
```



##### Disable PIN Authentication

> **sim.disablePin(pin)**

This function disables PIN authentication

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| pin       | string | PIN, ‘1234’ is the default, and the maximum length is 15 bytes. |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform pin password supports up to eight digits.
  
* Example

```python
>>> sim.disablePin("1234")
0
```



##### PIN Authentication

> **sim.verifyPin(pin)**

PIN authentication. Only can be called after sim.enablePin(pin) is executed successfully. And the SIM card only can be used after the verification is successful.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| pin       | string | PIN, ‘1234’ is the default, and the maximum length is 15 bytes. |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform pin password supports up to eight digits.
  
* Example

```python
>>> sim.verifyPin("1234")
0
```



##### Unlock SIM Card

> **sim.unblockPin(puk, newPin)**

This function unlocks the SIM card. When PIN/PIN2 code is wrongly input for times, PUK/PUK2 code and new PIN/PIN2 code are required to unlock the SIM card. If all PUK code input in10 times are incorrect, SIM card will be permanently locked and automatically scrapped.s

* Parameter

| Parameter | Type   | Description                                  |
| --------- | ------ | -------------------------------------------- |
| puk       | string | PUK, and the maximum length is 15 bytes.     |
| newPin    | string | New PIN, and the maximum length is 15 bytes. |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform pin password supports up to eight digits.
  
* Example

```python
>>> sim.unblockPin("12345678", "0000")
0
```



##### Change PIN

> **sim.changePin(oldPin, newPin)**

Changes PIN.

* Parameter

| Parameter | Type   | Description                                  |
| --------- | ------ | -------------------------------------------- |
| oldPin    | string | Old PIN, and the maximum length is 15 bytes. |
| newPin    | string | New PIN, and the maximum length is 15 bytes. |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform pin password supports up to eight digits.
  
* Example

```python
>>> sim.changePin("1234", "4321")
0
```



##### Read Phonebook

> **sim.readPhonebook(storage, start, end, username)**

This function obtains one or more phone number records in the specified phonebook on the SIM card.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| storage   | int    | The phonebook storage location of the phone number record to be read. The optional parameters are as follows: <br/>0 – DC，1 – EN，2 – FD，3 – LD，4 – MC，5 – ME，6 – MT，7 – ON，<br/>8 – RC，9 – SM，10 – AP，11 – MBDN，12 – MN，13 – SDN，14 – ICI，15 - OCI |
| start     | int    | The start number of phone number record to be read. Starts from 0, indicates that get phone number record without the number. |
| end       | int    | The end number of phone  number record to be read. Must meet: end - start <= 20 |
| username  | string | Only valid when start =0. The username in the phone number, and the maximum length is 30 bytes.<br/> |

* Return Value

If it failed to read, return -1. If read successfully, the record will be returned in the format shown as follows.

`(record_number, [(index, username, phone_number), ... , (index, username, phone_number)])`

Description:

`record_number` – Integer type. The record number read out.

`index` – Integer type. The index position in the phonebook.

`username` – String type. User name.

`phone_number` – String type. Phone number.

* note

  The BC25PA platform does not support this method.
  
* Example

```python
>>> sim.readPhonebook(9, 1, 4, "")
(4,[(1,'Tom','15544272539'),(2,'Pony','15544272539'),(3,'Jay','18144786859'),(4,'Pondy','15544282538')])
>>> sim.readPhonebook(9, 0, 0, "Tom")
(1, [(1, 'Tom', '18144786859')])
>>> sim.readPhonebook(9, 0, 0, "Pony")
(1, [(2, 'Pony', '17744444444')])
>>> sim.readPhonebook(9, 0, 0, "Pon") #Note, once ‘pon’ is included, the matching is successful
(2, [(2, 'Pony', '17744444444'),(4,'Pondy','15544282538')])
```



##### Write Phonebook

> **sim. writePhonebook(storage, index, username, number)**

This function writes a phone number record.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| storage   | int    | The phonebook storage location of the phone number record to be read. The optional parameters are as follows: <br/>0 – DC，1 – EN，2 – FD，3 – LD，4 – MC，5 – ME，6 – MT，7 – ON，<br/>8 – RC，9 – SM，10 – AP，11 – MBDN，12 – MN，13 – SDN，14 – ICI，15 - OCI |
| index     | int    | The index of phone number record to be written. Range: 1-500. |
| username  | string | The username in the phone number, and the maximum length is 30 bytes. |
| number    | string | The phone number, and the maximum length is 20 bytes.        |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform does not support this method.
  
* Example

```python
>>> sim.writePhonebook(9, 1, 'Tom', '18144786859')
0
```



##### Register Listening Callback Function

> **sim.setCallback(usrFun)**

This function registers the listening callback function. This function will be triggered when receiving SMS.

(Only valid when the SIM card hot-plugging is enabled.)

* Parameter

| Parameter | Type     | Description                                                |
| --------- | -------- | ---------------------------------------------------------- |
| usrFun    | function | Listening callback function. See example for more details. |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform does not support this method.
  
* Example

```python
import sim

def cb(args):
    simstates = args
    print('sim states:{}'.format(simstates))
    
sim.setCallback(cb)
```



##### Set SIMdet

> **sim.setSimDet(detenable, insertlevel)**

This function sets the SIM card hot-plugging related configurations.

* Parameter

| Parameter   | Type | Description                                                  |
| ----------- | ---- | ------------------------------------------------------------ |
| detenable   | int  | Enable/Disable SIM card hot-plugging. 0: Disable. 1: Enable. |
| insertlevel | int  | High/low level (0/1).                                        |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform does not support this method.
  
* Example

```python
>>> sim.setSimDet(1, 0)
0
```



##### Obtain SIMdet

> **sim.getSimDet()**

This function obtains the SIM card hot-plugging related configuration.

* Parameter

NA

* Return Value

If it failed to obtain, return -1. If the configuration is obtained successfully, a tuple will be returned in the format shown as follows.

`(detenable, insertlevel)`

Description：

`detenable` - Enable/Disable SIM card hot-plugging. 0: Disable. 1: Enable.

`insertlevel` – High/low level (0/1).

* note

  The BC25PA platform does not support this method.
  

Example

```python
>>> sim.getSimDet()
(1, 0)
```



#### voiceCall - Call Related

Function: Provides call related APIs.

Note: For 4G only software version, VoLTE must be enable to perform call related functions.

##### Set the Auto-Answer Time

> **voiceCall.setAutoAnswer(seconds)**

This function sets the Auto-Answer Time.

* Parameter

| Parameter | Type | Description                              |
| --------- | ---- | ---------------------------------------- |
| seconds   | int  | Auto-Answer time. Range: 0-255. Unit: s. |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
>>> import voiceCall
>>> voiceCall.setAutoAnswer(5)
0
```



##### Initiate a Call

> **voiceCall.callStart(phonenum)**

This function initiates a call.

* Parameter

| Parameter | Type   | Description       |
| --------- | ------ | ----------------- |
| phonenum  | string | The phone number. |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
>>> voiceCall.callStart("13855169092")
0
```



##### Answer a Call

> **voiceCall.callAnswer()**

This function answers a call.

* Parameter

NA

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
>>> voiceCall.callAnswer()
0
```



##### Hang up a Call

> **voiceCall.callEnd()**

This function hangs up a call.

* Parameter

NA

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
>>> voiceCall.callEnd()
0
```



##### Set DTMF

> **voiceCall.startDtmf(dtmf, duration)**

This function sets DTMF.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| dtmf      | string | DTMF string. The maximum length of string is 32. Valid characters: 0、1、…、9、A、B、C、D、*、# |
| duration  | int    | The duration of each tone. Range: 100-1000. Unit: ms.        |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
>>> voiceCall.startDtmf('A',100)
0
```


##### Set FWmode

> **voiceCall.setFw(reason, fwmode, phonenum)**

Call Forwarding Number and Conditions Control

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| reason    | int    | Forwarding conditions/reasion: <br/>0 : Unconditional<br/>1 : Mobile busy<br/>2 : Not reply<br/>3 : Not reachable<br/>4 : All call forwarding (Refer to 3GPP TS 22.030)<br/>5 : All conditional call forwarding (Refer to 3GPP TS 22.030) |
| fwmode    | int    | Controls the call forwarding supplementary service:<br/>0 : Disable<br/>1 : Enable<br/>2 : Query status<br/>3 : Registration<br/>4 : Erasure |
| phonenum  | string | The targeted number for forwarding                           |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

NA



##### Register Listening Callback Function

> **voiceCall.setCallback(usrFun))**

This function registers the listening callback function. This function will be triggered when answering/hanging up a call. 

* Parameter

| Parameter | Type     | Description                 |
| --------- | -------- | --------------------------- |
| usrFun    | function | Listening callback function |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
def voice_callback(args):
     if args[0] == 4106:
         print('voicecall is waiting')
     elif args[0] == 4105:
         print('voicecall disconnect')
     elif args[0] == 4104:
         print('voicecall connected, CallNO.: ', args[6])
     elif args[0] == 4103:
         print('voicecall incoming call, PhoneNO.: ', args[6])

>>> voiceCall.setCallback(voice_callback)
0
>>> voiceCall.callStart('10086')
0
```



#### sms - SMS

Function: Provides SMS related APIs.
Note: The BC25PA platform does not support this module function.

##### Send the Message in TEXT Mode

> **sms.sendTextMsg(phoneNumber, msg, codeMode)**

This function sends the messages in TEXT mode.

* Parameter

| Parameter   | Type   | Description                                                  |
| ----------- | ------ | ------------------------------------------------------------ |
| phoneNumber | string | The phone number, and the maximum length is 20 bytes.        |
| msg         | string | The message to be sent, and the maximum length is 140 bytes. |
| codeMode    | string | Character Set.<br/>'GSM' - GSM<br/>'UCS2' - UCS2<br/>Note：<br/>（1）GSM is only for sending English messages.<br/>（2）UCS2 can be used both for English and Chinese messages. |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
# -*- coding: UTF-8 -*-
import sms

sms.sendTextMsg('18158626517', '这是一条中文测试短信！', 'UCS2')
sms.sendTextMsg('18158626517', 'Hello, world.', 'GSM')
sms.sendTextMsg('18158626517', '这是一条夹杂中文与英文的测试短信,hello world!', 'UCS2')
```



##### Send the Message in PDU Mode

> **sms.sendPduMsg(phoneNumber, msg, codeMode)**

This function sends the messages in PDU mode.

* Parameter

| Parameter   | Type   | Description                                                  |
| ----------- | ------ | ------------------------------------------------------------ |
| phoneNumber | string | The phone number, and the maximum length is 20 bytes.        |
| msg         | string | The message to be sent, and the maximum length is 140 bytes. |
| codeMode    | string | Character Set.<br/>'GSM' - GSM<br/>'UCS2' - UCS2<br/>Note：<br/>（1）GSM is only for sending English messages.<br/>（2）UCS2 can be used both for English and Chinese messages. |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
# -*- coding: UTF-8 -*-
import sms

if __name__ == '__main__':
    sms.sendPduMsg('18158626517', 'send pdu msg by GSM mode.', 'GSM')
    sms.sendPduMsg('18158626517', 'send pdu msg by UCS2 mode.', 'UCS2')
    sms.sendPduMsg('18158626517', '这是一条中文测试短信！通过PDU-UCS2模式', 'UCS2')   
```



##### Delete Messages

> **sms.deleteMsg(index)**

This function deletes the specified messages.

- Parameter


| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| index     | int  | The index of the short messages to be deleted.<br/>If short messages are stored in SIM card, range: 0-49.<br/>If short messages are stored in ME, range: 0-179. And only the short messages exist in the corresponding index, can the short messages be deleted successfully. |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
>>> import sms
>>> sms.deleteMsg(0)
0
```



##### Preferred Message Storage

> **sms.setSaveLoc(mem1, mem2, mem3)**

This function selects the memory storages, and the default is SIM message storage.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| mem1      | string | Messages to be read and deleted from this memory storage：<br/>"SM" - SIM message storage.<br/>"ME" - Mobile equipment message storage.<br/>"MT" - Not supported currently. |
| mem2      | string | Messages will be written and sent to this memory storage：<br/>"SM" - SIM message storage<br/>"ME" - Mobile equipment message storage.<br/>"MT" - Not supported currently. |
| mem3      | string | Received messages will be placed in this memory storage：<br/>"SM" - SIM message storage<br/>"ME" - Mobile equipment message storage.<br/>"MT" - Not supported currently. |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
>>> import sms
>>> sms.setSaveLoc('SM', 'SM', 'SM')
0
```



##### Obtain Message Storage

> **sms.getSaveLoc()**

This function obtains the current information in the message storage.

* Parameter

NA

* Return Value

If the information is obtained successfully, a tuple is returned in the following format:

`([loc1, current_nums, max_nums],[loc2, current_nums, max_nums],[loc3, current_nums, max_nums])`

Description：

`loc1` - The memory storage where the messages to be read and deleted stored in;

`loc2` - The memory storage where the messages twill be written and sent stored in;

`loc3` - The memory storage where the Received messages stored in;

`current_nums` - The current number of messages in the storage.

`max_nums` - The maximum number of messages can be stored in the storage.

* Example

```python
>>> sms.getSaveLoc()
(['SM', 2, 50], ['SM', 2, 50], ['SM', 2, 50])
>>> sms.setSaveLoc('SM','ME','MT')
0
>>> sms.getSaveLoc()
(['SM', 2, 50], ['ME', 14, 180], ['MT', 2, 50])
```



##### Obtain the Number of Messages

> **sms.getMsgNums()**

This function obtains the number of messages.

* Parameter


NA

* Return Value

The number of messages  Successful execution.

-1  Failed execution.

* Example

```python
>>> import sms
>>> sms.getMsgNums() # Messages should be sent to module before to get the number.
1
```



##### Read Message in PDU Mode

> **sms.searchPduMsg(index)**

This function reads messages in PDU mode.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| index     | int  | The index of the message to be read. Range: 0 ~ MAX-1, MAX indicates the maximum number can be stored. |

* Return Value

If successfully, returns the message content in string. If failed, returns -1.



##### Read Message in TEXT Mode

> **sms.searchTextMsg(index)**

This function reads messages in TEXT mode.

* Parameter

| Parameter | Type | Description                                       |
| --------- | ---- | ------------------------------------------------- |
| index     | int  | The index of the message to be read. Range: 0~49. |

* Return Value

If successfully, returns the message content in following format. If failed, returns -1.

Return format：(phoneNumber, msg, msgLen)

`phoneNumber` ：Phone number.

`msg` ：Message content

`msgLen` ：Message Length

* Example

```python
>>> import sms
>>> sms.sendPduMsg('+8618226172342', '123456789aa', 'GSM') # Send a message.
>>> sms.searchPduMsg(0) # Obtain messages in TEXT mode.
'0891683110305005F0240BA19169256015F70000022141013044230B31D98C56B3DD70B97018'
>>> sms.searchTextMsg(0) # Obtain messages in TEXT mode.
('+8618226172342', '123456789aa', 22)
```



##### Obtain the Short Message Center Number

> **sms.getCenterAddr()**

This function obtains the short message center number.

* Parameter

NA

* Return Value

Returns the short message center number in string type if successfully, or returns -1 if failed.

* Example

```python
>>> import sms
>>> sms.getCenterAddr()
'+8613800551500'
```



##### Set the Short Message Center Number

> **sms.setCenterAddr(addr)**

This function sets the short message center number. And it is not recommended to modify the short  message center number.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| addr      | string | The short message center number to be set.|

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

NA



##### Obtain the Length of PDU Messages

> **sms.getPduLength(pduMsg)**

This function obtains the length of the specified PDU messages.

- Parameter


| Parameter | Type   | Description |
| --------- | ------ | ----------- |
| pduMsg    | string | PDU message |

- Return Value


Returns the length of PDU message if successfully, or returns -1 if failed.

- Example


```python
>>> import sms
>>> sms.searchPduMsg(0)
'0891683108501505F0040D91688122162743F200000211529003332318C16030180C0683C16030180C0683E170381C0E87'
>>> sms.getPduLength(sms.searchPduMsg(0)) 
40
```



##### Decode PDU

> **sms.decodePdu(pduMsg, pduLen)**

This function decodes PDU.

- Parameter


| Parameter | Type   | Description           |
| --------- | ------ | --------------------- |
| pduMsg    | string | PDU message           |
| pduLen    | int    | Length of PDU message |

- Return Value


Returns the decoded PDU message in the following format if successfully, or returns -1 if failed.

Format：(phoneNumber, msg, time, msgLen)

`phoneNumber` ：The phone number.

`msg` ：Message content.

`time` ：Time when the message was received.

`msgLen` ：The length of the message.

- Example


```python
>>> import sms
>>>sms.decodePdu('0891683110305005F00405A10110F000081270319043442354516C76CA77ED4FE1FF1A00320030003200315E7496328303975E6CD596C68D445BA34F2067086D3B52A863D09192FF1A4E3B52A88FDC79BB975E6CD596C68D44FF0C5171540C5B8862A47F8E597D751F6D3B3002',20)
>>>('10010', '公益短信：2021年防范非法集资宣传月活动提醒：主动远离非法集资，共同守护美好生活。', '2021-07-13 09:34:44', 118)
>>> 
```



##### Registers the Listening Callback Function

> **sms.setCallback(usrFun)**

This function registers the listening callback function. This function will be triggered when receiving the short messages. 

* Parameter

| Parameter | Type     | Description                                                |
| --------- | -------- | ---------------------------------------------------------- |
| usrFun    | function | Listening callback function. See example for more details. |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

The new architecture refers to example 1, and the old architecture refers to example 2

example 1:

```python
import sms

def cb(args):
    index = args[1]
    storage = args[2]
    print('New message! storage:{},index:{}'.format(storage, index))
    
sms.setCallback(cb)
```

example 2:

```python
import sms

def cb(args):
    ind_flag = args[0]
	if ind_flag == 4097:
	    mes_buf = args[1]
		mes_len = args[2]
		print('New message! ind_flag:{},mes_buf:{},mes_len:{}'.format(ind_flag, mes_buf, mes_len))
    elif ind_flag == 4099:
	    mes_type = args[1]
		storage = args[2]
        index = args[3]
        print('New message! ind_flag:{},mes_type:{},storage:{},index:{}'.format(ind_flag, mes_type, storage, index))
	elif ind_flag == 4100:
	    mes_buf = args[1]
        print('New message! ind_flag:{},mes_buf:{}'.format(ind_flag, mes_buf))
	elif ind_flag == 4101:
		storage = args[1]
        index = args[2]
        print('New message! ind_flag:{},storage:{},index:{}'.format(ind_flag, storage, index))
    
sms.setCallback(cb)
```



#### net - Network

Function: Provides APIs to query/set network related performance.

##### Set APN

> **net.setApn(apn, simid)**

This function sets APN.

* Parameter

| Parameter | Type   | Description                        |
| --------- | ------ | ---------------------------------- |
| apn       | string | apn name                           |
| simid     | int    | simid (0:SIM card 1 1: SIM card 2) |

* Return Value

0  Successful execution.

-1  Failed execution

* note

  The BC25PA platform does not support this module function.
  
##### Obtain the Current  APN

> **net.getApn(simid)**

This function obtains the current APN.

* Parameter

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| simid     | int  | simid       |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform does not support this module function.

##### Obtain CSQ

> **net.csqQueryPoll()**

This function obtains CSQ.

* Parameter

NA

* Return Value

If the execution is successful, the CSQ value is returned. If the execution is failed, -1 is returned. And the returned value 99 indicates the exception.

The range of CSQ is 0-31, and the larger the value, the better the signal. 

* Example

```python
>>> import net
>>> net.csqQueryPoll()
31
```



##### Obtain Neighbor Cell Information

> **net.getCellInfo()**

This function obtains the information of Cell information.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned.  If the execution is successful, the list of neighbor cell information including RATs GSM/UMTS/LTE are returned in the following format. And when the neighbor cell information for one RAT is null, the corresponding list returned is null.  

`([(flag, cid, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, licd, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, mcc, mnc, pci, tac, earfcn, rssi),...])`

The description of the return value for GSM:

| Parameter | Description                             |
| --------- | --------------------------------------- |
| flag      | 0: present，1: inter，2: intra          |
| cid       | Return CID, 0 means null.               |
| mcc       | Mobile Country Code                     |
| mnc       | Mobile Network Code                     |
| lac       | Location Area Code                      |
| arfcn     | Absolute Radio Frequency Channel Number |
| bsic      | Base Station Identity Code              |
| rssi      | Received Signal Strength Indication     |

The description of the return value for UMTS:

| Parameter | Description                             |
| --------- | --------------------------------------- |
| flag      | 0: present，1: inter，2: intra          |
| cid       | Return CID, 0 means null.               |
| lcid      | Area identification number              |
| mcc       | Mobile Country Code                     |
| mnc       | Mobile Network Code                     |
| lac       | Location Area Code                      |
| uarfcn    | Absolute Radio Frequency Channel Number |
| psc       | Base Station Identity Code              |
| rssi      | Received Signal Strength Indication     |

The description of the return value for LTE:

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| flag      | 0: present，1: inter，2: intra                               |
| cid       | Return CID, 0 means null.                                    |
| mcc       | Mobile Country Code                                          |
| mnc       | Mobile Network Code                                          |
| pci       | Physical Cell Identifier                                     |
| tac       | Tracing area code                                            |
| earfcn    | Extended Absolute Radio Frequency Channel Number. Range: 0-65535. |
| rssi      | Received Signal Strength Indication                          |

* Example

```python
>>> net.getCellInfo()
([], [], [(0, 14071232, 1120, 0, 123, 21771, 1300, -69), (3, 0, 0, 0, 65535, 0, 40936, -140), (3, 0, 0, 0, 65535, 0, 3590, -140), (3, 0, 0, 0, 63, 0, 40936, -112)])
```



##### Obtain RAT and Roaming Configuration

>**net.getConfig()**

The function obtains the current RAT and the roaming configuration.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If the execution is successful, a tuple including the current primary RAT and roaming configuration  is returned.

* note

  The BC25PA platform does not support this module function.

RAT

| Value | RAT                                                          |
| ----- | ------------------------------------------------------------ |
| 0     | GSM                                                          |
| 1     | UMTS. Not supported in EC100Y                                |
| 2     | GSM_UMTS, auto. not supported in EC100Y and EC200S           |
| 3     | GSM_UMTS, GSM preferred. Not supported in EC100Y and EC200S  |
| 4     | SM_UMTS, UMTS preferred. Not supported in EC100Y and EC200S  |
| 5     | LTE                                                          |
| 6     | GSM_LTE, auto, single link                                   |
| 7     | GSM_LTE, GSM preferred, single link                          |
| 8     | GSM_LTE, LTE preferred, single link                          |
| 9     | UMTS_LTE, auto, single link. Not supported in EC100Y and EC200S |
| 10    | UMTS_LTE, UMTS preferred, single link. Not supported in EC100Y and EC200S |
| 11    | UMTS_LTE, LTE preferred, single link . Not supported in EC100Y and EC200S |
| 12    | GSM_UMTS_LTE, auto, single link. Not supported in EC100Y and EC200S |
| 13    | GSM_UMTS_LTE, GSM preferred, single link. Not supported in EC100Y and EC200S |
| 14    | GSM_UMTS_LTE, UMTS preferred, single link. Not supported in EC100Y and EC200S |
| 15    | GSM_UMTS_LTE, LTE preferred, single link. Not supported in EC100Y and EC200S |
| 16    | GSM_LTE, dual link                                           |
| 17    | UMTS_LTE, dual link. Not supported in EC100Y and EC200S      |
| 18    | GSM_UMTS_LTE, dual link. Not supported in EC100Y and EC200S  |

* Example

```python
>>>net.getConfig ()
(8, False)
```



##### Set RAT and Roaming Configuration

> **net.setConfig(mode, roaming)**

The function sets the current RAT and the roaming configuration.

* Parameter

| Parameter | Type | Description                                              |
| --------- | ---- | -------------------------------------------------------- |
| mode      | int  | RAT. Range: 0-18. For more details, see the table above. |
| roaming   | int  | Turn on/off the roaming. (0: Turn off. 1: Turn on)       |

* Return Value

0  Successful execution.

-1  Failed execution.

* note

  The BC25PA platform does not support this module function.


##### Obtain the Network Mode

> **net.getNetMode()**

This function obtains the network mode.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If  the execution is successful, a tuple is returned in the format：`(selection_mode, mcc, mnc, act)`

The description of the return value:
`selection_mode` : Selection Mode. 0- Automatic. 1- Manual.
`mcc` : Mobile Country Code
`mnc` : Mobile Network Code
`act` : ACT mode for the primary RAT

ACT Mode

| Value | ACT Mode           |
| ----- | ------------------ |
| 0     | GSM                |
| 1     | COMPACT            |
| 2     | UTRAN              |
| 3     | GSM wEGPRS         |
| 4     | UTRAN wHSDPA       |
| 5     | UTRAN wHSUPA       |
| 6     | UTRAN wHSDPA HSUPA |
| 7     | E UTRAN            |
| 8     | UTRAN HSPAP        |
| 9     | E TRAN A           |
| 10    | NONE               |

* Example

```python
>>> net.getNetMode()
(0, '460', '46', 7)
```



##### Obtain the Signal Strength

> **net.getSignal()**

This function obtains the signal strength.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If the execution is successful, a tuple including 2 list (GW/LTE) is returned in the following format:

`([rssi, bitErrorRate, rscp, ecno], [rssi, rsrp, rsrq, cqi])`

The description of the return value:

GW list：

`rssi` : Received Signal Strength Indicator

`bitErrorRate` : Error Rate

`rscp` : Received Signal Code Power

`ecno` :   Pilot Channel  

LTE list：

`rssi` : Received Signal Strength Indicator

`rsrp` : Reference Signal Receiving Power

`rsrq` : Reference Signal Receiving Quality

`cqi` : Channel Quality

* Example

```python
>>>net.getSignal()
([99, 99, 255, 255], [-51, -76, -5, 255])
```



##### Obtain the Current Time of the Base Station

> **net.nitzTime()**

This function obtains the current time of the base station.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If the execution is successful, a tuple is returned in the following format: 

`(date, abs_time, leap_sec)`

`date` : String type. The time of the base station.

`abs_time` : Integer type. The absolute number of seconds of time.

`leap_sec` : Integer type. The leap second.

* Example

```python
>>> net.nitzTime()
('20/11/26 02:13:25+32', 1606356805, 0)
```



##### Obtain the Current Operator Information

> **net.operatorName()**

This function obtains the current operator information.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If the execution is successful, a tuple is returned in the following format:

`(long_eons, short_eons, mcc, mnc)`

`long_eons` :  String type. Full name of the operator information.

`short_eons` :  String type. Short name of the operator information. 

`mcc` : String type. Mobile Country Code.

`mnc` : String type. Mobile Network Code.

* Example

```python
>>> net.operatorName()
('CHN-UNICOM', 'UNICOM', '460', '01')
```



##### Obtain the Registration State

> **net.getState()**

This function obtains the registration state. 

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If the execution is successful, a tuple is returned in the following format:

`([voice_state, voice_lac, voice_cid, voice_rat, voice_reject_cause, voice_psc], [data_state, data _lac, data _cid, data _rat, data _reject_cause, data _psc])`

The description of the return value:

`state` : Network registration state.

`lac` : Location Area Code

`cid` : ID information in integer type

`rat` : RAT

`reject_cause` : Reject cause

`psc` ：Primary Scrambling Code

Network registration state

| Value | Description                                                  |
| ----- | ------------------------------------------------------------ |
| 0     | Not registered, MT is not currently searching an operator to register to. |
| 1     | Registered, home network.                                    |
| 2     | Not registered, but MT is currently trying to attach or searching an operator to register to. |
| 3     | Registration denied.                                         |
| 4     | unknown.                                                     |
| 5     | Registered, roaming.                                         |
| 6     | Registered for “SMS only”, home network (not applicable).    |
| 7     | Registered for “SMS only”, roaming (not applicable).         |
| 8     | Attached for emergency bearer services only.                 |
| 9     | Registered for “CSFB not preferred”, home network (not applicable). |
| 10    | Registered for “CSFB not preferred”, roaming (not applicable). |
| 11    | Emergency bearer services only.                              |

* Example

```python
>>> net.getState()
([11, 26909, 232301323, 7, 0, 466], [0, 26909, 232301323, 7, 0, 0])
```



##### Obtain the ID of the Neighbor Cell

> **net.getCi()**

This function obtains the ID of the Neighbor Cell.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If the execution is successful, an array in list type including cell ID is returned, and the format of this array is `[id, ……, id]`。

* Example

```python
>>> net.getCi()
[14071232, 0]
```



##### Obtain the MNC of the Neighbor Cell

> **net.getMnc()**

This function obtains the MNC of the neighbor cell.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If the execution is successful, an array in list type including cell MNC is returned, and the format of this array is `[mnc, ……, mnc]`.

* Example

```python
>>> net.getMnc()
[0, 0]
```



##### Obtain the MCC of the Neighbor Cell

> **net.getMcc()**

This function obtains the MCC of the neighbor cell.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If the execution is successful, an array in list type including cell MCC is returned, and the format of this array is `[mcc, ……, mcc]`.

* Example

```python
>>> net.getMcc()
[1120, 0]
```



##### Obtain the LAC of the Neighbor Cell

> **net.getLac()**

This function obtains the LAC of the neighbor cell.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If the execution is successful, an array in list type including cell LAC is returned, and the format of this array is `[lac, ……, lac]`.

* Example

```python
>>> net.getLac()
[21771, 0]
```



##### Obtain the Modem Functionality

> **net.getModemFun()**

This function obtains the current modem functionality.

* Parameter

NA

* Return Value

If the execution is failed, -1 is returned. If the execution is successful, the current modem functionality is returned:

0 : Minimum functionality

1 : Full functionality (Default)

4 : Airplane

* Example

```python
>>> net.getModemFun()
1
```



##### Set the Modem Functionality

> **net.setModemFun(function, rst)**

This function sets the current modem functionality.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| function  | int  | 0 - Minimum functionality. 1 - Full functionality. 4 - Airplane mode.(The RDA platform does not support CFUN4) |
| rst       | int  | Optional. 0 - Take effect immediately (Default). 1 - Take effect after rebooting. |

* Return Value

0  Successful execution.

-1  Failed execution.

* Example

```python
>>> net.setModemFun(4)
0
```



#### checkNet - Wait for Network to be Ready

Function: The checkNet module is mainly used for the script programs [auto-startup], and provides APIs to wait for the network to be ready. If it times out or exits abnormally, the program returns an error code. Therefore, if there are network-related operations in the your program, the method in the checkNet module should be called at the beginning of the user program to wait for the network to be ready. Of course, you can also implement the functions of this module by yourselves. 
Note: The BC25PA platform does not support this module function.
##### Create checkNet Object

> **import checkNet**
>
> PROJECT_NAME = "QuecPython_Math_example"
> PROJECT_VERSION = "1.0.0"
> checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

* Function

  Create a checkNet object. PROJECT_NAME and PROJECT_VERSION are two required global variables, users can modify the values of these two variables accordingly.

* Parameter

  | Parameter       | Description                   |
  | --------------- | ----------------------------- |
  | PROJECT_NAME    | String type. Project name.    |
  | PROJECT_VERSION | String type. Project version. |

* Return Value

  NA

- Example


```python
import checkNet

PROJECT_NAME = "XXXXXXXX"
PROJECT_VERSION = "XXXX"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)
```



##### Print Log when Power-On

> **checknet.poweron_print_once()**

* Function

  Prints the following log information when the module is powering on.

  PROJECT_NAME     	  : Project Name.
  PROJECT_VERSION 	 : Project Version.
  FIRMWARE_VERSION  : Firmware Version .
  POWERON_REASON   : The reason of the power-on.
  SIM_CARD_STATUS     : The status of SIM card.

* Parameter

  NA

* Return Value

  NA

* Example

```python 
import checkNet

PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

if __name__ == '__main__':
    # Add the following sentence before running the program.
    checknet.poweron_print_once()
	......
    
# When the progrm is running, the following log information is printed.
==================================================
PROJECT_NAME     : QuecPython_Math_example
PROJECT_VERSION  : 1.0.0
FIRMWARE_VERSION : EC600UCNLBR01A01M16_OCPU_V01
POWERON_REASON   : 2
SIM_CARD_STATUS  : 1
==================================================
```



##### Wait for Network to be Ready

> **checknet.wait_network_connected(timeout)**

* Function

  Waits for the network ready. Within the timeout, once the dial-up success is detected, the network state is returned. Otherwise, the block is not exit until the timeout expires.

* Parameter

| Return Value | Type | Description                                         |
| ------------ | ---- | --------------------------------------------------- |
| timeout      | Int  | Timeout. Range: 1-3600. Default value: 60. Unit: s. |

* Return Value

  There are two return values in the following format:

  `stagecode, subcode`

  The description for each return values:

  | Return Value | Type | Description                                                  |
  | ------------ | ---- | ------------------------------------------------------------ |
  | stagecode    | Int  | Stage code, indicates the stage of the checkNet module. <br>1 - Obtaining the state of the  SIM card. This value is returned when the timeout expires or the state of the SIM card is abnormal. <br>2 - Obtaining the state of the network registration. This value is returned when the timeout expires.<br>3 - Obtaining the state of the dial-up.<br>The normal return value is 3 indicates the normal. |
  | subcode      | Int  | Subcode，it is combined with the value of stagecode  to represent the specific state of checknet in different stages.<br/>When  stagecode = 1 ：<br/>subcode indicates the state of the SIM card, range: [0, 21], for the description of each value, refer to the return value in sim.getStatus() https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=sim-sim%e5%8d%a1](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=sim-sim卡) <br/><br/><br/>When stagecode = 2 ：<br/>subcode indicates the state of the network registration, range: [0, 11], for the description of each values, refer to the return value in net.getState()https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=net-%e7%bd%91%e7%bb%9c%e7%9b%b8%e5%85%b3%e5%8a%9f%e8%83%bd](https://python.quectel.com/wiki/#/zh-cn/api/QuecPythonClasslib?id=net-网络相关功能)    <br/>When subcode = -1, indicates the dial-up is failed within the timeout.<br/>For other value, see the above link.<br/>If within the timeout, the network registration is successful, enter the stage of stagecode = 3 directly.<br/><br/>When stagecode = 3 : <br/>subcode = 0, indicates the  dial-up is failed within the timeout.<br/>subcode = 1, indicates the network connection is successful within the timeout, that is the network registration and dial-up is successful. |

* Example

```python
import checkNet

PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

if __name__ == '__main__':
    #  Add the following sentence before running the program.
    stagecode, subcode = checknet.wait_network_connected(30)
    print('stagecode = {}, subcode = {}'.format(stagecode, subcode))
	......
    
# The network is ready.
stagecode = 3, subcode = 1
# The SIM card is not inserted.
stagecode = 1, subcode = 0
#The SIM card is locked.
stagecode = 1, subcode = 2
```



##### checkNet Exception Handling

You can troubleshoot and solve the exception according to the return value described in `checknet.wait_network_connected(timeout)` ：

```python
import checkNet

PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

if __name__ == '__main__':
    # Add the following sentence before running the program.
    stagecode, subcode = checknet.wait_network_connected(30)
    print('stagecode = {}, subcode = {}'.format(stagecode, subcode))
    
    if stagecode == 1:
        # If subcode = 0, you can check whether the SIM card is inserted or card slot is 		 # loose.
        # If the subcode is not 0, you can check the state if tge SIM card according to  		 # the corresponding description in wiki.
    elif stagecode == 2:
        if subcode == -1:
            # This case indicates that the API execution for obtaining the network 					# registration status has failed all the time within the timeout. On the 				# premise of confirming that the SIM card can be used normally and can be 				# recognized by the module, you can contact our FAE to feed back the problem.
        elif subcode == 0:
            # This case indicates that the network registration has failed all the time 			# within the timeout. You can follow the steps below to troubleshoot the 				# problem.
            # (1)Obtains the state of SIM card by sim.getState(), the abormal return 				#    value is 1.
            # (2)If the SIM card status is normal, you can obtain the current signal 				#	 strength through the net.csqQueryPoll() interface to check whether 				#	 signal strength is weak. If yes,  the reason of network registration 				#	 failure may be current signal strength is weak, and you can increase the 			  #	   timeout or place the module to a better signal position; 
            # (3)If the SIM card status is normal, and the signal stregth is rather 				#	 better, you contact Quectel FAE, and provide the information of SIM 				#	 card, such as the operator, IMSI, and so on, andsend the SIM card to 				#	 Quectel if necessary.
        else:
            # For the reason of the registration failure, see the return value in 					# net.getState() 
    elif stagecode == 3:
        if subcode == 1:
            #  Indicates the network connection is successful, that is the network 					#  registration and dial-up is successful.
        else:
            #  Indicates the dial-up faiure within the timeout, you can retry the network 			  #  connecion according to the following step.
            #  (1) Obtains the state of SIM card by sim.getState(), the abormal return 				#      value is 1.
            #  (2) Obtains the state of the network registration by net.getState(), the 				   abnoram return value is 1. 
            #  (3) Executes the dial-up interface maunally.
            #  (4) If the manual dial-up is successful, but automatic dial-up is failed 			#	   when the module is powered on, the reason may be the current matched 			#	   APN is not in the default APN list.You can obtain the IMSI through 				#      sim.getImsi() of SIM module to confirm whether the number composed of 			 #      the fourth and fifth characters of IMSI is in the range of 01 ~ 13. If 			   #	  not, it indicates that there is no APN information corresponding to 				#      this kind of SIM card in the current default APN list. In this case, 			#      you can execute dataCall.setApn(...) to save the APN inforamtion. 
            #  (5) If it failed to execute the dial-up maunally, please contact Quectel 			#	   FAE, and provide the information of SIM card, such as the operator, 				#      IMSI, and so on, and send the SIM card to Quectel if necessary.
```



#### fota - Firmware Upgrade

Module function: Firmware upgrade.

##### Create a fota Object

> **import fota**
>
> **fota_obj = fota()**

##### One-click Upgrade Interface

> **fota_obj.httpDownload(url1=, url2=, callback=)**

Realize the whole process of firmware download and upgrade with one interface

- Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| url1      | str            | The url of the first stage upgrade package to be downloaded  |
| url2      | str            | The url of the second stage upgrade package to be downloaded. Note: this parameter must be input for the minimum system upgrade because the minimum system is divided into two stages, while this parameter is forbidden to be input  for DFOTA and FullFOTA upgrade because there is only one stage for DFOTA and FullFOTA. |
| callback  | function       | Callback function which shows downloading progress and status (Optional). Note: This callback is valid on EC600S/EC600N modules with non-minimum system upgrade mode. It is invalid on other modules. |

- Return Value

  Return integer value 0 if the download is successful and return integer value -1 if the download fails. Note: on EC600S/EC600N module, the return value only represents the success or failure of the command, and the download status needs to be fed back through the callback.

- Example

```python
#args[0] indicates the download status. If the download is successful, it returns an integer value: 0 or 1 or 2. If the download fails, it returns an integer value: -1. args[1] represents the download progress. When the download status shows success, it represents the percentage. When the download status shows failure, it represents error code
def result(args):
    print('download status:',args[0],'download process:',args[1])
    
#DFOTA upgrade, fullFOTA upgrade    
fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)    
#Minimum system upgrade
fota_obj.httpDownload(url1="http://www.example.com/fota1.bin",url2="http://www.example.com/fota2.bin")
```



##### Interface to Upgrade Step by Step and Write Upgrade Package Data Stream

> **fota_obj.write(bytesData, file_size)**

Write upgrade package data stream

* Parameter

| Parameter | Parameter Type | Description                                        |
| --------- | -------------- | -------------------------------------------------- |
| bytesData | bytes          | Upgrade the package file data                      |
| file_size | int            | Total size of the upgrade package file(Unit: byte) |

* Return Value

  0 	Successful execution

  -1	Failed execution

* note

  The BC25PA platform does not support this method.


##### Interface to Upgrade Step by Step and Refresh Cached Data to Flash

> **fota_obj.flush()**

Refresh cached data to the flash.

- Parameter

None

- Return Value

  0 	Successful execution

  -1	Failed execution

* note

  The BC25PA platform does not support this method.

##### Interface to Upgrade Step by Step and Verify the Data

> **fota_obj.verify()**

 Verify the data.

* Parameter

None

* Return Value

  0 	Successful execution

  -1	Failed execution

* note

  The BC25PA platform does not support this method.

* Example

```python
>>> fota_obj.verify()
0
```



##### Example

###### One-click Upgrade Interface

```python
import fota
import utime
import log

# Set the log output level
log.basicConfig(level=log.INFO)
fota_log = log.getLogger("Fota")

# This example needs upgrade package file (delta package and other .bin files).
def result(args):
    print('download status:',args[0],'download process:',args[1])
    
def run():
    fota_obj = fota()  # Create a Fota object
    fota_log.info("httpDownload...")
    #DFOTA upgrade, fullFOTA upgrade    
    res = fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)    
    #Minimum system upgrade
    #res = fota_obj.httpDownload(url1="http://www.example.com/fota1.bin",url2="http://www.example.com/fota2.bin")
    if res != 0:
        fota_log.error("httpDownload error")
        return
    fota_log.info("wait httpDownload update...")
    utime.sleep(2)

if __name__ == '__main__':
    fota_log.info("run start...")
    run()    
```



###### Interface to Upgrade Step by Step

```python
'''
@Author: Pawn
@Date: 2020-07-28
@LastEditTime: 2020-11-30
@Description: example for module fota
@FilePath: example_fota_file.py
'''


import fota
import utime
import log
from misc import Power
import uos

'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
'''
PROJECT_NAME = "QuecPython_Fota_example"
PROJECT_VERSION = "1.0.0"

# Set the log output level
log.basicConfig(level=log.INFO)
fota_log = log.getLogger("Fota")

# This example needs upgrade package file (delta package and other .bin files) and store the file to the file system.

def run():
    fota_obj = fota()  # Create a Fota object
    file_size = uos.stat("/usr/FotaFile.bin")[6]  # Get the total bytes of the file
    print(file_size)
    with open("/usr/FotaFile.bin", "rb")as f:   # Open.bin file with rb mode(upgrade package file is needed)
        while 1:
            c = f.read(1024)   # read
            if not c:
                break
            fota_obj.write(c, file_size)  # Write .bin file data and its total size
	
    fota_log.info("fota image flush...")
    res = fota_obj.flush()  # Refresh
    if res != 0:
        fota_log.error("flush error")
        return
    fota_log.info("fota image verify...")
    res = fota_obj.verify()  # Verify
    if res != 0:
        fota_log.error("verify error")
        return
    fota_log.info("power_reset...")
    utime.sleep(2)
    Power.powerRestart()   # Restart the module


if __name__ == '__main__':
    fota_log.info("run start...")
    run()

```



#### app_fota - Upgrade User File 

Module function: Upgrade user file 
Note: The BC25PA platform does not support this module function.
##### Create an app_fota Object

1. Import app_fota module
2. Call`new` method to create an app_fota object

```python
import app_fota
fota = app_fota.new()
```



##### Download a Single File

> **fota.download(url, file_name)**

 - Parameter

| Parameter | Parameter Type | Description                                        |
| --------- | -------------- | -------------------------------------------------- |
| url       | str            | The url of the file to be downloaded               |
| file_name | str            | The absolute path of the local file to be upgraded |


 - Return Value

   0 	Successful execution

   -1	Failed execution



##### Download Files in Batches

> **fota.bulk_download(info=[])**

 - Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| info      | list           | Download files in batches. The elements of the list are  dictionaries containing `url` and `file_name` |


 - Return Value
   Return the list of failed downloading

 - Example

```python
download_list = [{'url': 'http://www.example.com/app.py', 'file_name': '/usr/app.py'}, {'url': 'http://www.example.com/test.txt', 'file_name': '/usr/text.txt'}]
```

In this example, assuming that `http://www.example.com/test.txt`fails to be downloaded, the return value is`[{url: 'http://www.example.com/test.txt', file_name: '/usr/text.txt'}]`



##### Set Upgrade Flag

> **fota.set_update_flag()**

 - Parameter
   None

 - Return Value
   None

> After setting the upgrade flag, call the restart interface, and the upgrade can be started after the restart.
> After the upgrade is complete, you will directly enter the application.

> Reference link of the restart interface : http://qpy.quectel.com/wiki/#/zh-cn/api/?id=power



#### audio - Audio Playback

Module function: audio playback, supports to play files in TTS, mp3 and AMR.
Note: The BC25PA platform does not support this module function.
##### TTS 

###### Create the TTS Object

> **import audio**
> **tts = audio.TTS(device)**

* Parameter 

`device` : Device type. 0 - handset, 1 - earphone, 2 - speaker.

* Example

```python
>>> import audio
>>> tts = audio.TTS(1)
```



###### Disable TTS Function

> **tts.close()**

Disable TTS function.

* Parameter

None

* Return Value

  0 	Successful execution

  -1	Failed execution



###### Start to Play TTS

> **tts.play(priority, breakin, mode, str)**

Audio playback supports priority 0–4, the higher the number, the higher the priority. Each priority group can join up to 10 playback tasks at the same time; the playback strategy is described as follows:

1. If task A is currently playing and it is allowed to be interrupted and a higher priority task B comes at this time, the current task A will be interrupted, and task B with higher priority will be played directly.

2. If task A is currently playing and it is not allowed to be interrupted and a higher priority task B comes at this time, task B will be added to a appropriate position in the playback queue, waiting for task A to complete, and then the tasks will be played from the queue in turn with priority from high to low;

3. If task A is currently playing and it is not allowed to be interrupted and task B with the same priority comes at this time, task B will be added to the end of the playback queue of the priority group, waiting for task A to complete, and then the tasks will be played from the queue in turn from high to low in priority;

4. If task A is currently playing and it is allowed to be interrupted and a task B with the same priority comes at this time, the current task A will be interrupted and task B will be played directly;

5. If task A is currently playing and there are already several playback tasks in the priority group playback queue of task A, and the last task N in the priority group playback queue is allowed to be interrupted, and at this time, if task B with the same priority, task B will directly overwrite task N; in other words, only the last element of a certain priority group is allowed to be interrupted, that is, breakin is 1, and other tasks are not allowed to be interrupted;

6. If task A is currently playing, regardless of whether task A is allowed to be interrupted, task B with a lower priority comes at this time, add B to the playback queue of the priority group corresponding to B.

* Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| priority  | int            | Playback priority. Supports Priority 0–4. The higher the number, the higher the priority. |
| breakin   | int            | Interruption mode. 0 means not allowed to be interrupted; 1 means allowed to be interrupted |
| mode      | int            | Encoding mode. 1 - UNICODE16 (Size end conversion), 2 - UTF-8, 3 - UNICODE16 (Don't convert) |
| str       | string         | String to be played                                          |

* Return Value

  0 	Successful execution

  -1	Failed execution

  1	 Cannot be played immediately, but join the playback queue

  -2	Cannot be played immediately, and the priority group queue task of the request has reached the upper limit and cannot 		be added to the play queue

* Example

```python
>>> import audio
>>> tts = audio.TTS(1)
#Task A is currently playing and it is allowed to be interrupted and a higher priority task B comes at this time, task A is interrupted, and task B is played directly.
>>> tts.play(1, 1, 2, '1111111111111111')  #Task A
0
>>> tts.play(2, 0, 2, '2222222222222222')  #Task B
0

#Task A is currently playing and it is not allowed to be interrupted and a higher priority task B comes at this time, task B is added to the playback queue, waiting for task A to complete (Assuming the playback queue is empty before)
>>> tts.play(1, 0, 2, '1111111111111111')  #Task A
0
>>> tts.play(2, 0, 2, '2222222222222222')  #Task B
1

#Task A is currently playing and it is allowed to be interrupted and task B with the same priority comes at this time, the current task A is interrupted and task B is played directly
>>> tts.play(2, 1, 2, '2222222222222222222')  #Task A
0
>>> tts.play(2, 0, 2, '3333333333333333333')  #Task B
0

#Task A is currently playing and it is not allowed to be interrupted and task B with the same priority comes at this time, task B will be added to the playback queue, waiting for task A to complete, and then task B is played (Assuming the playback queue is empty before)
>>> tts.play(2, 0, 2, '2222222222222222222')  #Task A
0
>>> tts.play(2, 0, 2, '3333333333333333333')  #Task B
1

#Task A is currently playing and it is not allowed to be interrupted and task B with the same priority comes at this time,and task B is allowed to be interrupted, task B will join the playback queue. Task C with the same priority as task A and B comes at the same time, then task C will join the playback queue and directly overwrite task B. Therefore, task C is played after task A completes (Assuming the playback queue is empty before)
>>> tts.play(2, 0, 2, '2222222222222222222')  #Task A
0
>>> tts.play(2, 1, 2, '3333333333333333333')  #Task B
1
>>> tts.play(2, 0, 2, '4444444444444444444')  #Task C
1

```

Chinese example of tts playback:

Note that "# -*- coding: UTF-8 -*-" needs to be added at the beginning of the python file. If there are punctuation marks in the Chinese to be played, they should be changed to English punctuation marks.

```python
# -*- coding: UTF-8 -*-
import audio

tts = audio.TTS(1)
str1 = '移联万物,志高行远' #The comma here is in English
tts.play(4, 0, 2, str1)
```



###### Stop Playing TTS

> **tts.stop()**

Stop playing TTS.

* Parameter

None

* Return Value

  0 	Successful execution

  -1	Failed execution



###### Register Callback Function

> **tts.setCallback(usrFun)**

Register the callback function of the user. It is used to notify the user of the TTS playback status. Note that time-consuming and blocking operations should not be performed in this callback function. It is recommended to only perform simple and short-time operations.

* Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| usrFun    | function       | The callback function of the user. See the format in the following example |

* Return Value

  0 	Successful execution

  -1	Failed execution

* Example

```python
import audio

def tts_cb(event):
	if event == 2:
		print('TTS-play start.')
	elif event == 4:
		print('TTS-play finish.')

tts = audio.TTS(1)
tts.setCallback(tts_cb)
tts.play(1, 0, 2, 'QuecPython')
```

Description of several event values of the TTS playback callback function:

| event | Status             |
| ----- | ------------------ |
| 2     | Start to play      |
| 3     | Stop playing       |
| 4     | Playback completed |



###### Get TTS Volume

> **tts.getVolume()**

Ger the volume of the current TTS playback. The volume value is 0–9. 0 means mute. Default value: 4

* Parameter

None

* Return Value

  0 	Successful execution

  -1	Failed execution

* Example

```python
>>> tts.getVolume()
4
```



###### Set TTS Volume

> **tts.setVolume(vol)**

Set TTS playback volume.

* Parameter

| Parameter | Parameter Type | Description                                 |
| --------- | -------------- | ------------------------------------------- |
| vol       | int            | The volume value. Range: 0–9. 0 means mute. |

* Return Value

  0 	Successful execution

  -1	Failed execution

* Example

```python
>>> tts.setVolume(6)
0
```



###### Get Audio Playback Speed

> **tts.getSpeed()**

Get the current playback speed. The speed value is 0–9, and the larger the value, the faster the speed. Default value: 4.

* Parameter

None

* Return Value

  0 	Successful execution

  -1	Failed execution

* Example

```python
>>> tts.getSpeed()
4
```



###### Set Playback Speed

> **tts.setSpeed(speed)**

Set TTS playback speed.

* Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| speed     | int            | Speed value. Range: 0–9, and the larger the value, the faster the speed. |

* Return Value

  0 	Successful execution

  -1	Failed execution

* Example

```python
>>> tts.setSpeed(6)
0
```



###### Get TTS State

> **tts.getState()**

Get TTS state.

* Parameter

None

* Return Value

  0	 Integer value. Indicates that there is currently no TTS playback.

  1	Integer value. Indicates that TTS is playing.

* Example

```python
>>> tts1 = audio.TTS(1)
>>> tts1.getState()
0
>>> tts1.play(1, 0, 2, '8787878787878787') 
0
>>> tts1.getState() #Execute this interface when the above TTS is playing
1
```



###### Example

```python
'''
@Author: Pawn
@Date: 2020-08-19
@Description: example for module TTS
@FilePath: example_tts_file.py
'''
import log
from audio import TTS
import utime


'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects.
'''
PROJECT_NAME = "QuecPython_TTS_example"
PROJECT_VERSION = "1.0.0"

# Set the log output level
log.basicConfig(level=log.INFO)
tts_Log = log.getLogger("TTS")


if __name__ == '__main__':
    # Parameter 1: device(0: handset, 1:earphone, 2:speaker)
    tts = TTS(1)
    # Get the current playback volume
    volume_num = tts.getVolume()
    tts_Log.info("Current TTS volume is %d" %volume_num)

    # Set the volume to 6
    volume_num = 6
    tts.setVolume(volume_num)
    #  (0-4)Parameter 1: Priority (0–4)
    #  Parameter 2: Interruption mode: 0 means not allowed to be interrupted; 1 means allowed to be interrupted
    #  Parameter 3: Encoding mode. (1: UNICODE16 (Size end conversion), 2: UTF-8, 3:UNICODE16 (Don't convert))
    #  Parameter 4: data string (String to be played)
    tts.play(1, 1, 2, 'QuecPython') # Play
    tts.close()   # Disable TTS feature
```



##### Audio

###### Create an object

> **import audio**
>
> **aud = audio.Audio(device)**

* Parameter

`device` : Device type. 0 -handset. 1 - earphone, 2 - speaker.

* Example

```python
>>> import audio
>>> aud = audio.Audio(1)
```



###### Set GPIO for Outputting PA

> **aud.set_pa(gpio)**

Set the GPIO pin for outputting PA and enable the PA function. Currently, it supports switch from class AB switch to class D, that is, the pulses of the two rising edges are respectively 1 us < pulse < 12 us

* Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| gpio      | int            | Set the GPIO pin for output. The GPIO can be get from the pins |

- Return Value

  0 	Successful execution

  -1	Failed execution

- Example

```python
>>> import audio
>>> from machine import Pin
>>> aud = audio.Audio(0)

>>> aud.set_pa(Pin.GPIO15)
1
#Set TTS successfully and play the audio. the pulse switches from class AB to class D
>>> aud.play(2, 1, 'U:/music.mp3')
0
```



###### Play Audio File

> **aud.play(priority, breakin, filename)**

Play audio files. The audio playback supports files in mp3, amr and wav format. Support priority 0–4, the higher the number, the higher the priority. Each priority group can add up to 10 playback tasks at the same time, sharing the same playback queue with TTS playback.

* Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| priority  | int            | Playback priority. Supports priority 0–4, and the higher the number, the higher the priority |
| breakin   | int            | Interruption mode. 0 means not allowed to be interrupted; 1 means allowed to be interrupted |
| filename  | string         | The file name to be played, including the file storage path  |

* Return value

  0 	Successful execution

  -1	Failed execution

  1	 Cannot be played immediately, but join the playback queue

  -2	Cannot be played immediately, and the priority group queue task of the request has reached the 		upper limit and cannot be added to the play queue

* Example

```python
>>> import audio
>>> a = audio.Audio(1)

>>> a.play(2, 1, 'U:/music.mp3')  #Add the path before the file name
0
```

Notes on the file playback path:

The user partition path is fixed at the beginning of 'U:/', which means the root directory of the user partition. If the user creates a new audio directory under the root directory and stores the audio file in this new audio directory under the root directory, the path parameter should be 'U:/audio/music.mp3' in the playback interface.

* Description

Since TTS and audio file share the same playback queue, the playback priority and interruption mode set in TTS are not only compared with other TTS playback tasks, but also compared with the priority and interruption mode of audio file playback tasks. Conversely, the playback priority and interruption mode set in the audio file playback are also effective for the TTS task.



###### Stop Playing Audio File

> **aud.stop()**

Stop playing the audio file.

* Parameter

None

* Return Value

  0 	Successful execution

  -1	Failed execution



###### Register the Callback Function

> **aud.setCallback(usrFun)**

Register the callback function of the user. It is used to notify the user of the audio file playback status. Note that time-consuming and blocking operations should not be performed in this callback function. It is recommended to only perform simple and short-time operations.

* Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| usrFun    | function       | The callback function of the user. See the format in the following example |

* Return Value

  0 	Successful execution

  -1	Failed execution

* Example

```python
import audio

def audio_cb(event):
	if event == 0:
		print('audio-play start.')
	elif event == 7:
		print('audio-play finish.')

aud = audio.Audio(1)
aud.setCallback(audio_cb)
aud.play(1, 0, 'U:/test.mp3')
```

Description of several event values of the audio playback callback function:

| event | Status             |
| ----- | ------------------ |
| 0     | Start to play      |
| 7     | Playback completed |



###### Get Audio Initialization Status

> **aud.getState()**

Get audio initialization status.

* Parameter

None

* Return Value

0 	Successful execution

-1	Failed execution



###### Get Audio Volume

> **aud.getVolume()**

Get the audio volume, and the default value is 7.

* Parameter

None

* Return Value

Return the volume in integer.



###### Set Audio Volume

> **aud.setVolume(vol)**

Set audio volume.

* Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| vol       | int            | Volume. Range: 1–11. The higher the number, the higher the volume. |

* Return Value

  0 	Successful execution

  -1	Failed execution

* Example

```python
>>> aud.setVolume(6)
0
>>> aud.getVolume()
6
```



##### Record

Applicable versions: EC100Y(V0009) and above; EC600S(V0003) and above.
Note: The BC25PA platform does not support this module function.
###### Create an Object

> **import audio**
>
> **record = audio.Record()**

* Parameter

  NA	

* Return Value

  0 	Successful execution

  -1	Failed execution

* Example

```python
import audio 
record_test = audio.Record()
```



###### Start Recording

> **record.start(file_name,seconds)**

Start recording.

* Parameter

| Parameter | Parameter Type | Description                             |
| --------- | -------------- | --------------------------------------- |
| file_name | str            | File name of the recording              |
| seconds   | int            | Time needed for recording. Unit: second |

* Return Value

  0	Successful execution

  -1	File overwrite failed

  -2	File open failed

  -3	The file is in use

  -4	Channel setting error ( Set to 0 or 1 only)

  -5	Request for timer resource failed

  -6	Audio format detection error

  -7	The file has been created by another object

* Example

```python
record_test.start(“test.wav”,40)	#Record the file in wav format
record_test.start(“test.amr”,40)	#Record the file in amr format
record_test.start(“test”,40)	#Record the file in amr format
```



###### Stop Recording

> **record.stop()**

Stop recording.

* Parameter

None

* Return Value

None

* Example

```python
record_test.stop()
```



###### Read Storage Path of the Recording File

> **record. getFilePath(file_name)**

Read storage path of the recording file.

* Parameter

  *file\_name*: 

  String type. Name of the recording file.

* Return Value

  String: Path of the recording file

* Example

```python
record_test.getFilePath(“test.wav”)
```



###### Read Recording Data

> **record.getData(file_name，offset, size)**

Read the recording data.

* Parameter

| Parameter | Parameter Type | Description                |
| --------- | -------------- | -------------------------- |
| file_name | str            | File name of the recording |
| offset    | int            | Offset of the read data    |
| size      | int            | Read size: less than 10 K  |

* Return Value

  -1	Error reading data

  -2	File open failed

  -3	Wrong offset setting

  -4	The file is in use

  -5	Setting exceeds file size(offset+size > file_size)

  -6	The read size is greater than 10 K

  -7	 Less than 10 K of memory

  -8	 The file does not belong to the object

  bytes	Return data

* Example

```python
record_test.getData(“test.amr”,0, 44) 
```



###### Read Recording File Size

> **record.getSize(file_name)**

Read recording file size.

* Parameter

| Parameter | Parameter Type | Description                |
| --------- | -------------- | -------------------------- |
| file_name | str            | File name of the recording |



* Return Value

  Return the file size if it is executed successfully.

  In wav format, this value will be 44 bytes larger than the return value of the callback (44 bytes is the size of the file header)

  In amr format, this value will be 6 bytes larger than the return value of the callback (6 bytes is the size of the file header); Or else

  *-1*	Failed execution 

  *-2*	File open failed 

  *-3*	The file is in use

  -4	The file does not belong to the object

* Example

```python
record_test.getSize(“test.amr”)
```



###### Delete Recording File

> **record.Delete(file_name/empty)**

Delete the recording file.

* Parameter

*file\_name*： 

String type. The file name of the recording.

Note: When the parameter is empty, delete all recording files in the object

* Return Value

  0	Successful execution

  -1	The file does not exist

  -2	File is in use

  -3	The file does not belong to the object

* Example

```python
record_test.Delete(“test.amr”)
record_test.Delete()
```



###### Determine Whether the Recording File Exists

> **record.exists(file_name)**

Determine whether the recording file exists.

* Parameter

| Parameter | Parameter Type | Description                |
| --------- | -------------- | -------------------------- |
| ile_name  | str            | File name of the recording |

* Return Value

  true		The file exists

  false	   The file does not exist

  -1			The file does not belong to the object

* Example

```python
record_test.exists(“test.amr”)
```



###### Determine Whether the Recording is in Progress

> **record.isBusy()**

Determine whether the recording is in progress

* Parameter

None

* Return Value

  0	idle

  1	busy

* Example

```python
record_test.isBusy()
```



###### 注册录音结束回调Register the Callback of Recording End

> **record.end_callback(callback)**

Set the callback of recording end

* Parameter

| Parameter | Parameter Type | Description  |
| --------- | -------------- | ------------ |
| callback  | api            | Callback API |

* Return Value

  0			Successful execution

  other	Failed  execution  

* Example

```python
def record_callback(para): 
	print("file_name:",para[0])   # Return the file path 
    print("audio_len:",para[1])   # Return the recording length 
    print("audio_state:",para[2])  
    # Return recording state -1: error, 0: start, 3: success 
record_test.end_callback(record_callback)
```



###### Set Recording Gain

> **record.gain(code_gain,dsp_gain)**

Set recording gain.

* Parameter

| Parameter | Parameter Type | Description                  |
| --------- | -------------- | ---------------------------- |
| code_gain | int            | Uplink codec gain [0,4]      |
| dsp_gain  | int            | Uplink digital gain [-36,12] |

* Return Value

  0	Successful execution

* Example

```python
record_test.gain(4,12)
```



###### Read the List of Recording Files

> **record.list_file()**

View the list of recording files in the object.

* Parameter

None

* Return Value

*str*  String type. Recording file list.  

* Example

```python
record_test.list_file()
```



###### Example

```python
import utime
import audio
from machine import Pin


flag = 1
'''
The external speaker plays the recording file.Input parameter 0外接喇叭播放录音文件，参数选择0
'''
aud = audio.Audio(0)
tts = audio.TTS(0)

aud.setVolume(11)
'''
(EC600S) The external speaker can play the recording file after enabling the following interface
(EC100Y: enabling the following interface ia not required)
'''
# audio_EN = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PD, 1)


def record_callback(args):
    global flag
    print('file_name:{}'.format(args[0]))
    print('file_size:{}'.format(args[1]))
    print('record_sta:{}'.format(args[2]))

    record_sta = args[2]
    if record_sta == 3:
        print('The recording is over, play it')
        tts.play(1, 0, 2, '录音结束,准备播放录音文件')
        aud.play(1, 0, record.getFilePath())
        flag = 0
    elif record_sta == -1:
        print('The recording failure.')
        tts.play(1, 0, 2, '录音失败')
        flag = 0

record = audio.Record()
record.end_callback(record_callback)
record.start('recordfile.wav', 10)

while 1:
    if flag:
        pass
    else:
        break
```



#### misc - Other

Functions: This module provides powering down, restarting the software, PWM and ADC related functions.

##### Power

It powers down and restarts the software.

###### Module Power Down

> **from misc import Power**
>
> **Power.powerDown()**

The module powers down.

* Parameter

None

* Return Value

None



###### Module Restart

> **Power.powerRestart()**

The module restarts.

* Parameter

None

* Return Value

None



###### Get the Reason for Module Powering On

> **Power. powerOnReason()**

It gets the reason for module powering on.

* Parameter

None

* Return Value

The values returned are explained as follows:

1: Power on normally

2:  Restart

3: VBAT 

4: RTC powers on regularly

5: Fault 

6: VBUS

0: Unknown

* note

  BC25PA platform only does not support restart reason 5.

###### Get the Reason for the Last Powering Down of the Module

> **Power. powerDownReason()**

It gets the reason for the last powering down of the module.

* Parameter

None

* Return Value

1: Power down normally

2: The voltage is too high

3: The voltage is low

4: Over temperature

5: WDT

6: VRTC is low

0: Unknown


* note

  The BC25PA platform does not support this method.

###### Get Voltage of the Battery.

> **Power. getVbatt()**

It gets the voltage of the battery. Unit: mV.

* Parameter

None

* Return Value 

Integer type. Voltage value.

* Example

```python
>>> Power.getVbatt()
3590
```



##### PowerKey

It provides a registration callback function.

###### Create an PowerKey Object

> from misc import PowerKey
>
> pk = PowerKey()

* Parameter

  None

* Return Value

  Return an object.




###### Register Callback Function

> pk.powerKeyEventRegister(usrFun)

* Parameter

| Parameter | Type     | Description                                                  |
| --------- | -------- | ------------------------------------------------------------ |
| usrFun    | function | Callback function, which is triggered when the power key button is pressed or released |

* Return Value

  Return 0 if the execution is successful, otherwise return -1.

* Note

  For EC600S-CN and EC600N-CN modules, when the powerkey button is pressed or released, the callback function registered by the user will be triggered;

  The EC200U and EC600U series modules will trigger the callback function only when the powerkey button is released, and the time for the button to be pressed needs to be maintained for more than 500 ms.

* Example

  EC600S-CN/EC600N-CN modules：

```python
from misc import PowerKey

pk = PowerKey()

def pwk_callback(status):
	if status == 0:
		print('powerkey release.')
	elif status == 1:
		print('powerkey press.')
        
pk.powerKeyEventRegister(pwk_callback)
```

​		EC200U/EC600U series modules：

```python
from misc import PowerKey

pk = PowerKey()

def pwk_callback(status):
	if status == 0: # The callback function is triggered only when the button is released
		print('powerkey release.')

pk.powerKeyEventRegister(pwk_callback)
```



##### PWM
Note: The BC25PA platform does not support this module function.
###### Constant Description

| Constent | Description | Usage Platform                         |
| -------- | ----------- | -------------------------------------- |
| PWM.PWM0 | PWM0        | EC600S / EC600N / EC100Y/EC600U/EC200U |
| PWM.PWM1 | PWM1        | EC600S / EC600N / EC100Y               |
| PWM.PWM2 | PWM2        | EC600S / EC600N / EC100Y               |
| PWM.PWM3 | PWM3        | EC600S / EC600N / EC100Y               |



###### Create a PWM Object

> **from misc import PWM**
>
> **pwm = PWM(PWM.PWMn,PWM.ABOVE_xx, highTime, cycleTime)**

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| PWMn      | int  | PWM Number<br/>Note: EC100Y-CN module supports PWM0–PWM3, and the corresponding pins are as follows: <br/>PWM0 – Pin No. 19<br/>PWM1 – Pin No. 18<br/>PWM2 – Pin No. 23<br/>PWM3 – Pin No. 22<br/>Note: EC600S-CN/EC600N-CN  modules support PWM0–PWM3, and the corresponding pins are as follows: <br/>PWM0 – Pin No. 52<br/>PWM1 –Pin No. 53<br/>PWM2 – Pin No. 70<br/>PWM3 – Pin No. 69<br />Note: EC200U series module supports PWM0, and the corresponding pins are as follows: <br />PWM0 – Pin No. 135<br />Note: EC600U series module supports PWM0, and the corresponding pins are as follows:<br />PWM0 – Pin No. 70<br /> |
| ABOVE_xx  | int  | PWM.ABOVE_MS				Range of MS level: (0,1023]<br/>PWM.ABOVE_1US				Range of US level: (0,157]<br/>PWM.ABOVE_10US				Range of US level: (1,1575]<br/>PWM.ABOVE_BELOW_US			Range of NS level: (0,1024] |
| highTime  | int  | In MS level, the unit is ms<br/>In US level, the unit is us<br/>In NS level: it needs to be calculated by the user<br/>               Frequency = 13Mhz / cycleTime<br/>               Duty cycle = highTime/ cycleTime |
| cycleTime | int  | In MS level, the unit is ms<br/>In US level, the unit is us<br/>In NS level: it needs to be calculated by the user<br/>             Frequency = 13Mhz / cycleTime<br/>             Duty cycle = highTime/ cycleTime |

* Example

```python
>>> from misc import PWM
>>> pwm1 = PWM(PWM.PWM1, PWM.BOVE_MS, 100, 200)
```



###### Open PWM Output

> **pwm.open()**

It opens PWM output.

* Parameter

None

* Return Value

Return 0 if the execution is successful, otherwise return -1.



###### Close PWM Output

> **pwm.close()**

It closes PWM output.

* Parameter

None

* Return Value

Return 0 if the execution is successful, otherwise return -1.



###### Example

```python
# PWM Example

from misc import PWM
import utime


'''
The following two global variables are required. Users can modify the values of the following two global variables according to the actual projects.
'''
PROJECT_NAME = "QuecPython_PWM_example"
PROJECT_VERSION = "1.0.0"

'''
* Parameter 1: PWM number
        Note: EC100Y-CN module supports PWM0–PWM3, and the corresponding pins are as follows: 
        PWM0 – Pin No.19
        PWM1 – Pin No.18
        PWM2 – Pin No.23
        PWM3 – Pin No.22

        Note: EC600S-CN/EC600N-CN  modules support PWM0–PWM3, and the corresponding pins are as follows: 
        PWM0 – Pin No.52
        PWM1 – Pin No.53
        PWM2 – Pin No.70
        PWM3 – Pin No.69
* Parameter 2: high_time
        High level time. Unit: ms
* Parameter 3: cycle_time
        The whole cycle time of PWM. Unit: ms
'''
# It is neccessary to cooperate with peripherals or use DuPont line to short-circuit the corresponding pins for testing

if __name__ == '__main__':
    pwm = PWM(PWM.PWM0, PWM.ABOVE_MS, 100, 200)  # Initialize a PWM object
    pwm.open()  # Open PWM output
    utime.sleep(10)
    pwm.close()  # Close PWM output
```



##### ADC

###### Constant Description

| Constant | Description   | Usage Platform                            |
| -------- | ------------- | ----------------------------------------- |
| ADC.ADC0 | ADC Channel 0 | EC600S/EC600N/EC100Y/EC600U/EC200U/BC25PA |
| ADC.ADC1 | ADC Channel 1 | EC600S/EC600N/EC600U/EC200U        |
| ADC.ADC2 | ADC Channel 2 | EC600U/EC200U                      |
| ADC.ADC3 | ADC Channel 3 | EC600U                             |



###### Create an ADC Object

> **from misc import ADC**
>
> **adc = ADC()**

* Example

```python
>>> from misc import ADC
>>> adc = ADC()
```



###### Initialize ADC Function

> **adc.open()**

It initializes ADC function.

* Parameter

None

* Return Value

Return 0 if the execution is successful, otherwise return -1.



###### Read Voltage Value of the Channel

> **adc.read(ADCn)**

It reads the voltage value of the specified channel. Unit: mV.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| ADCn      | int  | ADC Channel<br/>The corresponding pins for EC100Y-CN module are as follows:<br/>ADC0 – Pin No. 39<br/>ADC1 – Pin No. 81<br/>The corresponding pins for EC600S-CN/EC600N_CN modules are as follows<br/>ADC0 – Pin No. 19<br/>The corresponding pins for EC600U series module are as follows<br />ADC0 – Pin No. 19<br/>ADC1 – Pin No. 20<br />ADC2 – Pin No. 113<br />ADC3 – Pin No. 114<br />The corresponding pins for EC200U series module are as follows<br />ADC0 – Pin No. 45<br/>ADC1 – Pin No. 44<br />ADC2 – Pin No.43<br /> |

* Return Value

Return the voltage value of the specified channel if the execution is successful, otherwise return -1.

* Example

```python
>>>adc.read(ADC.ADC0)  #Read the voltage value of ADC channel 0
613
>>>adc.read(ADC.ADC1)  #Read the voltage value of ADC channel 1
605
```



###### Close ADC

> **adc.close()**

It closes ADC.

* Parameter

None

* Return Value

Return 0 if the execution is successful, otherwise return -1.

##### USB

It provides USB plug detection interface.
Note: The BC25PA platform does not support this module function.
###### Create an USB Object

> from misc import USB
>
> usb = USB()

* Parameter

  None

* Return Value

  None

  

###### Get Current USB Connection Status

> usb.getStatus()

* Parameter

  None

* Return Value

  -1: Get status failed

  0 - USB is not connected currently

  1 - USB is connected



###### Register Callback Function

> usb.setCallback(usrFun)

* Parameter

| Parameter | Type     | Description                                                  |
| --------- | -------- | ------------------------------------------------------------ |
| usrFun    | function | Callback function, which will be triggered to notify the user of the current USB status when the USB is inserted or unplugged. Please note that do not perform blocking operations in the callback function. |

* Return Value

  Return 0 if the execution is successful, otherwise return -1.

Example

```python
from misc import USB

usb = USB()

def usb_callback(conn_status):
	status = conn_status
	if status == 0:
		print('USB is disconnected.')
	elif status == 1:
		print('USB is connected.')
usb.setCallback(usb_callback)
```



#### modem - Related Device

Function: This module gets device information.

##### Get IMEI of the Device

> **modem.getDevImei()**

It gets IMEI of the device.

* Parameter

None

Return Value

Return the IMEI of string type of the device if the execution is successful, otherwise return -1.

* Example

```python
>>> import modem
>>> modem.getDevImei()
'866327040830317'
```



##### Get Device Model

> **modem.getDevModel()**

It gets device model.

* Parameter

None

* Return Value

Return the device model of string type if the execution is successful, otherwise return -1.

* Example

```python
>>> modem.getDevModel()
'EC100Y'
```



##### Get Device Serial Number

> **modem.getDevSN()**

It gets device serial number.

* Parameter

None

* Return Value

Return the device serial number of string type if the execution is successful, otherwise return -1.

* Example

```python
>>> modem.getDevSN()
'D1Q20GM050038341P'
```



##### Get Firmware Version number

> **modem.getDevFwVersion()**

It gets the firmware version number.

* Parameter

None

* Return Value

Return the firmware version number of string type if the execution is successful, otherwise return -1.

* Example

```python
>>> modem.getDevFwVersion()
'EC100YCNAAR01A01M16_OCPU_PY'
```



##### ID Get Device Manufacturer ID

> **modem.getDevProductId()**

It gets device manufacturer ID.

* Parameter

None

* Return Value

Return the device manufacturer ID if the execution is successful, otherwise return -1.

* Example

```python
>>> modem.getDevProductId()
'Quectel'
```



#### machine - Related Hardware Functions

Function: The module contains specific functions related to the hardware on a specific circuit board. Most of the functions in this module allow accessing and controlling the hardware of the system directly and unrestricted.

##### Pin

Function: GPIO read and write operations.

###### Constant Description

| Constant         | Applicable Platform                    | Description    |
| ---------------- | -------------------------------------- | -------------- |
| Pin.GPIO1        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO1          |
| Pin.GPIO2        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO2          |
| Pin.GPIO3        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO3          |
| Pin.GPIO4        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO4          |
| Pin.GPIO5        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO5          |
| Pin.GPIO6        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO6          |
| Pin.GPIO7        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO7          |
| Pin.GPIO8        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO8          |
| Pin.GPIO9        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO9          |
| Pin.GPIO10       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO10         |
| Pin.GPIO11       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO11         |
| Pin.GPIO12       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO12         |
| Pin.GPIO13       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO13         |
| Pin.GPIO14       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO14         |
| Pin.GPIO15       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO15         |
| Pin.GPIO16       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO16         |
| Pin.GPIO17       | EC600S / EC600N / EC100Y               | GPIO17         |
| Pin.GPIO18       | EC600S / EC600N / EC100Y               | GPIO18         |
| Pin.GPIO19       | EC600S / EC600N / EC100Y               | GPIO19         |
| Pin.GPIO20       | EC600S / EC600N                        | GPIO20         |
| Pin.GPIO21       | EC600S / EC600N                        | GPIO21         |
| Pin.GPIO22       | EC600S / EC600N                        | GPIO22         |
| Pin.GPIO23       | EC600S / EC600N                        | GPIO23         |
| Pin.GPIO24       | EC600S / EC600N                        | GPIO24         |
| Pin.GPIO25       | EC600S / EC600N                        | GPIO25         |
| Pin.GPIO26       | EC600S / EC600N                        | GPIO26         |
| Pin.GPIO27       | EC600S / EC600N                        | GPIO27         |
| Pin.GPIO28       | EC600S / EC600N                        | GPIO28         |
| Pin.GPIO29       | EC600S / EC600N                        | GPIO29         |
| Pin.IN           | --                                     | Input mode     |
| Pin.OUT          | --                                     | Output mode    |
| Pin.PULL_DISABLE | --                                     | Floating mode  |
| Pin.PULL_PU      | --                                     | Pull-up mode   |
| Pin.PULL_PD      | --                                     | Pull-down mode |

Constant description for BC25PA platform
| Constant         | Applicable Platform                    | Description    |
| ---------------- | -------------------------------------- | -------------- |
| Pin.GPIO1        | BC25PA                   | GPIO3    |
| Pin.GPIO2        | BC25PA                   | GPIO4    |
| Pin.GPIO3        | BC25PA                   | GPIO5    |
| Pin.GPIO4        | BC25PA                   | GPIO6    |
| Pin.GPIO5        | BC25PA                   | GPIO16   |
| Pin.GPIO6        | BC25PA                   | GPIO20   |
| Pin.GPIO7        | BC25PA                   | GPIO21   |
| Pin.GPIO8        | BC25PA                   | GPIO22   |
| Pin.GPIO9        | BC25PA                   | GPIO23   |
| Pin.GPIO10       | BC25PA                   | GPIO25   |
| Pin.GPIO11       | BC25PA                   | GPIO28   |
| Pin.GPIO12       | BC25PA                   | GPIO29   |
| Pin.GPIO13       | BC25PA                   | GPIO30   |
| Pin.GPIO14       | BC25PA                   | GPIO31   |
| Pin.GPIO15       | BC25PA                   | GPIO32   |
| Pin.GPIO16       | BC25PA                   | GPIO33   |

**Corresponding Pin Number Description of GPIO**

The GPIO pin numbers provided in this document correspond to the external pin numbers of the module. For example, the GPIO1 of the EC600S-CN module corresponds to the pin number 22, which is the external pin number of the module. Uses can refer to the corresponding hardware resource to view the external pin number of the module.

###### Create a GPIO Object

> **gpio = Pin(GPIOn, direction, pullMode, level)**

* Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| GPIOn     | int  | Pin Number<br />The  corresponding pins of EC100Y-CN module are as follows (pin number is external pin number):<br />GPIO1 – Pin No. 22<br />GPIO2 – Pin No. 23<br />GPIO3 – Pin No. 38<br />GPIO4 – Pin No. 53<br />GPIO5 – Pin No. 54<br />GPIO6 – Pin No. 104<br />GPIO7 – Pin No. 105<br />GPIO8 – Pin No. 106<br />GPIO9 – Pin No. 107<br />GPIO10 – Pin No. 178<br />GPIO11 – Pin No. 195<br />GPIO12 – Pin No. 196<br />GPIO13 – Pin No. 197<br />GPIO14 – Pin No. 198<br />GPIO15 – Pin No. 199<br />GPIO16 – Pin No. 203<br />GPIO17 – Pin No. 204<br />GPIO18 – Pin No. 214<br />GPIO19 – Pin No. 215<br />The corresponding pins of EC600S-CN/EC600N-CN modules are as follows (pin number is external pin number): <br />GPIO1 – Pin No. 10<br />GPIO2 – Pin No. 11<br />GPIO3 – Pin No. 12<br />GPIO4 – Pin No. 13<br />GPIO5 – Pin No. 14<br />GPIO6 – Pin No. 15<br />GPIO7 – Pin No. 16<br />GPIO8 – Pin No. 39<br />GPIO9 – Pin No. 40<br />GPIO10 – Pin No. 48<br />GPIO11 – Pin No. 58<br />GPIO12 – Pin No. 59<br />GPIO13 – Pin No. 60<br />GPIO14 – Pin No. 61<br />GPIO15 – Pin No. 62<br/>GPIO16 – Pin No. 63<br/>GPIO17 – Pin No. 69<br/>GPIO18 – Pin No. 70<br/>GPIO19 – Pin No. 1<br/>GPIO20 – Pin No. 3<br/>GPIO21 – Pin No. 49<br/>GPIO22 – Pin No. 50<br/>GPIO23 – Pin No. 51<br/>GPIO24 – Pin No. 52<br/>GPIO25 – Pin No. 53<br/>GPIO26 – Pin No. 54<br/>GPIO27 – Pin No. 55<br/>GPIO28 – Pin No. 56<br/>GPIO29 – Pin No. 57<br />The corresponding pins of EC600U series module are as follows (pin number is external pin number): <br />GPIO1 – Pin No. 61<br />GPIO2 – Pin No. 58<br />GPIO3 – Pin No. 34<br />GPIO4 – Pin No. 60<br />GPIO5 – Pin No. 69<br />GPIO6 – Pin No. 70<br />GPIO7 – Pin No. 123<br />GPIO8 – Pin No. 118<br />GPIO9 – Pin No. 9<br />GPIO10 – Pin No. 1<br />GPIO11 – Pin No. 4<br />GPIO12 – Pin No. 3<br />GPIO13 – Pin No. 2<br />GPIO14 – Pin No. 54<br />GPIO15 – Pin No. 57<br/>GPIO16 – Pin No. 56<br/>The corresponding pins of EC200U series module are as follows (pin number is external pin number): <br />GPIO1 – Pin No. 27<br />GPIO2 – Pin No. 26<br />GPIO3 – Pin No. 24<br />GPIO4 – Pin No. 25<br />GPIO5 – Pin No. 13<br />GPIO6 – Pin No. 135<br />GPIO7 – Pin No. 136<br />GPIO8 – Pin No. 133<br />GPIO9 – Pin No. 3<br />GPIO10 – Pin No. 40<br />GPIO11 – Pin No. 37<br />GPIO12 – Pin No. 38<br />GPIO13 – Pin No. 39<br />GPIO14 – Pin No. 5<br />GPIO15 – Pin No. 141<br/>GPIO16 – Pin No. 142<br/> |
| direction | int  | IN – input mode; OUT – output mode                           |
| pullMode  | int  | PULL_DISABLE – floating mode<br />PULL_PU – pull-up mode<br />PULL_PD – pull-down mode |
| level     | int  | 0 - Set the pin to low level; 1- Set the pin to high level   |

* Example

```python
from machine import Pin
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
```



###### Get Pin Level

> **Pin.read()**

It gets pin level.

* Parameter

None

* Return Value

Pin level. 0 indicates low level; 1 indicates high level.



###### Set Pin Level

> **Pin.write(value)**

It sets the pin level, you need to ensure that the pin is in output mode before setting it to the high or low level.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| value     | int  | 0 - When the pin is in output mode, set it to output low;  <br />1 - When the pin is in output mode, set it to output high |

* Return Value

Return 0 if the execution is successful, otherwise return -1.

* Example

```python
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
>>> gpio1.write(1)
0
>>> gpio1.read()
1
```



###### Usage Example

```python
# Pin usage example

from machine import Pin
import utime


'''
The following two global variables are required. Users can modify the values of the following two global variables according to the actual projects.
'''
PROJECT_NAME = "QuecPython_Pin_example"
PROJECT_VERSION = "1.0.0"

'''
* Parameter 1: Pin Number
        The  corresponding pins of EC100Y-CN module are as follows :
        GPIO1 – Pin No.22
        GPIO2 – Pin No.23
        GPIO3 – Pin No.38
        GPIO4 – Pin No.53
        GPIO5 – Pin No.54
        GPIO6 – Pin No.104
        GPIO7 – Pin No.105
        GPIO8 – Pin No.106
        GPIO9 – Pin No.107
        GPIO10 – Pin No.178
        GPIO11 – Pin No.195
        GPIO12 – Pin No.196
        GPIO13 – Pin No.197
        GPIO14 – Pin No.198
        GPIO15 – Pin No.199
        GPIO16 – Pin No.203
        GPIO17 – Pin No.204
        GPIO18 – Pin No.214
        GPIO19 – Pin No.215

        The  corresponding pins of EC600S-CN/EC600N-CN module are as follows :
        GPIO1 – Pin No.10
        GPIO2 – Pin No.11
        GPIO3 – Pin No.12
        GPIO4 – Pin No.13
        GPIO5 – Pin No.14
        GPIO6 – Pin No.15
        GPIO7 – Pin No.16
        GPIO8 – Pin No.39
        GPIO9 – Pin No.40
        GPIO10 – Pin No.48
        GPIO11 – Pin No.58
        GPIO12 – Pin No.59
        GPIO13 – Pin No.60
        GPIO14 – Pin No.61
        GPIO15 – Pin No.62
        GPIO16 – Pin No.63
        GPIO17 – Pin No.69
        GPIO18 – Pin No.70
        GPIO19 – Pin No.1
        GPIO20 – Pin No.3
        GPIO21 – Pin No.49
        GPIO22 – Pin No.50
        GPIO23 – Pin No.51
        GPIO24 – Pin No.52
        GPIO25 – Pin No.53
        GPIO26 – Pin No.54
        GPIO27 – Pin No.55
        GPIO28 – Pin No.56
        GPIO29 – Pin No.57
* Parameter2: direction
        IN – Input mode
        OUT – Output mode
* Parameter3: pull
        PULL_DISABLE – Floating mode
        PULL_PU – Pull-up mode
        PULL_PD – Pull-down mode
* Parameter4: level
        0: Set the pin to low level
        1: Set the pin to high level
'''
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)

if __name__ == '__main__':
    gpio1.write(1) # Set GPIO1 output high level 
    val = gpio1.read() # Get the current high and low status of GPIO1
    print('val = {}'.format(val))

```



##### UART

Function: UART serial data transmission

* note
  BC25PA platform, only uart1 is supported
  
###### Constant Description

| Constant   | Sedcription |
| ---------- | ----------- |
| UART.UART0 | UART0       |
| UART.UART1 | UART1       |
| UART.UART2 | UART2       |
| UART.UART3 | UART3       |



###### Create an UART Object

> **uart = UART(UART.UARTn, buadrate, databits, parity, stopbits, flowctl)**

* Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| UARTn     | int  | Functions of UARTn are as follows: <br />UART0 - DEBUG PORT<br />UART1 – BT PORT<br />UART2 – MAIN PORT<br />UART3 – USB CDC PORT |
| buadrate  | int  | Baud rate, common baud rates are supported, such as 4800, 9600, 19200, 38400, 57600, 115200, 230400, etc. |
| databits  | int  | Data bit (5–8)                                               |
| parity    | int  | Parity check (0 – NONE，1 – EVEN，2 - ODD)                   |
| stopbits  | int  | Stop bit (1–2)                                               |
| flowctl   | int  | Hardware control flow (0 – FC_NONE， 1 – FC_HW）             |

* Example

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
```



###### Get the Size of Unread Data in the Received Buffer

> **uart.any()**

It returns the size of unread data in the received buffer.

* Parameter

None

* Return Value

Return the size of unread data in the received buffer.

* Example

```python
>>> uart.any()
20 #It indicates that there are 20 bytes of data in the received buffer that have not         been read
```



###### Read Data from UART

> **uart.read(nbytes)**

It reads data from UART.

* Parameter

| Parameter | Type | Description                    |
| --------- | ---- | ------------------------------ |
| nbytes    | int  | The number of bytes to be read |

* Return Value

Return the read data.



###### Send Data to UART

> **uart.write(data)**

It sends data to UART.

* Parameter

| Parameter | Type   | Description        |
| --------- | ------ | ------------------ |
| data      | string | Data has been sent |

* Return Value

Return the number of bytes has been sent.



###### Close UART

> **uart.close()**

It closes UART.

* Parameter

None

* Return Value

Return 0 if the execution is successful, otherwise return -1.



###### Control 485 communication direction

> **uart.control_485(UART.GPIOn, direction)**

Before and after the serial port sends data, pull up and down the specified GPIO to indicate the direction of 485 communication.

- parameter

| Parameter      | Type | Description                                                         |
| --------- | ---- | ------------------------------------------------------------ |
| GPIOn     | int  | For the GPIO pin number to be controlled, refer to the definition of pin module                      |
| direction | int  | 1 - Indicates that the pin level changes as follows: the serial port pulls high from low before sending data, and then pulls low from high after sending data<br />0 - Indicates that the pin level changes as follows: the serial port pulls low from high before sending data, and then pulls high from low after sending data |

- Return Value

Return 0 if the execution is successful, otherwise return -1.。

* note

  The BC25PA platform does not support this method.
  
- Example

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
>>> uart1.control_485(UART.GPIO24, 1)
```



###### Usage Example

```python
"""
To run this example, you need to connect the MAIN port of the development board to the PC through the serial cable, and use the serial tool on the PC to open the MAIN port and send data to this port, then you can see the message sent by the PC.
"""
import _thread
import utime
import log
from machine import UART


'''
The following two global variables are required. Users can modify the values of the following two global variables according to the actual projects.
'''
PROJECT_NAME = "QuecPython_UART_example"
PROJECT_VERSION = "1.0.0"

'''
 * Parameter1: Port
        Note: UARTn functions of EC100Y-CN and EC600S-CN modules are as follows:
        UART0 - DEBUG PORT
        UART1 – BT PORT
        UART2 – MAIN PORT
        UART3 – USB CDC PORT
 * Parameter2: Baud rate
 * Parameter3: data bits  （5~8）
 * Parameter4: Parity (0：NONE  1：EVEN  2：ODD) 
 * Parameter5：stop bits (1–2) 
 * Parameter6：flow control (0: FC_NONE  1：FC_HW) 
'''


# Set the log output level
log.basicConfig(level=log.INFO)
uart_log = log.getLogger("UART")

state = 5


def uartWrite():
    count = 10
    # Configure UART
    uart = UART(UART.UART2, 115200, 8, 0, 1, 0)
    while count:
        write_msg = "Hello count={}".format(count)
        # Send data
        uart.write(write_msg)
        uart_log.info("Write msg :{}".format(write_msg))
        utime.sleep(1)
        count -= 1
    uart_log.info("uartWrite end!")


def UartRead():
    global state
    uart = UART(UART.UART2, 115200, 8, 0, 1, 0)
    while 1:
        # It returns whether the data length is readable
        msgLen = uart.any()
        # Read when there is data
        if msgLen:
            msg = uart.read(msgLen)
            # The initial data is byte type, and encode it
            utf8_msg = msg.decode()
            # str
            uart_log.info("UartRead msg: {}".format(utf8_msg))
            state -= 1
            if state == 0:
                break
        else:
            continue



def run():
    # Create a thread to listen to received UARt messages
    _thread.start_new_thread(UartRead, ())


if __name__ == "__main__":
    uartWrite()
    run()
    while 1:
        if state:
            pass
        else:
            break

# Example of running results
'''
INFO:UART:Write msg :Hello count=8
INFO:UART:Write msg :Hello count=7
INFO:UART:Write msg :Hello count=6
INFO:UART:Write msg :Hello count=5
INFO:UART:Write msg :Hello count=4
INFO:UART:Write msg :Hello count=3
INFO:UART:Write msg :Hello count=2
INFO:UART:Write msg :Hello count=1
INFO:UART:uartWrite end!
INFO:UART:UartRead msg: read msg 1

INFO:UART:UartRead msg: read msg 2

INFO:UART:UartRead msg: read msg 3
'''

```



##### Timer

Function: Hardware timer

Note when using this timer: Timer 0-3, each can only perform one task at the same time, and multiple objects cannot use the same timer.

###### Constant Description

| Constant       | Description                                  |
| -------------- | -------------------------------------------- |
| Timer.Timer0   | Timer 0                                      |
| Timer.Timer1   | Timer 1                                      |
| Timer.Timer2   | Timer 2                                      |
| Timer.Timer3   | Timer 3                                      |
| Timer.ONE_SHOT | Single mode, the timer executes only once    |
| Timer.PERIODIC | Periodic mode, the timer executes cyclically |



###### Create a Timer Object

> **timer = Timer(Timern)**

It creates a timer object.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| Timern    | int  | Timer number<br />It supports Timer0–Timer3 (Note when using this timer: Timer 0–3, each can only perform one task at the same time, and multiple objects cannot use the same timer). |

* Example

```python
>>> from machine import Timer
>>> timer1 = Timer(Timer.Timer1)  # Note when using this timer: Timer 0–3, each can only perform one task at the same time, and multiple objects cannot use the same timer.
```



###### Start Timer

> **timer.start(period, mode, callback)**

It starts timer.

* Parameter

| Parameter | Type     | Description                                                  |
| --------- | -------- | ------------------------------------------------------------ |
| period    | int      | Interrupt period, it greater than or equal to 1. Unit: milliseconds |
| mode      | int      | Running mode<br />Timer.ONE_SHOT - Single mode, the timer executes only once<br />Timer.PERIODIC  -  Periodic mode, the timer executes cyclically |
| callback  | function | Execution function of timer                                  |

* Return Value

Return 0 if the execution is successful, otherwise return -1.

* Example

```python
//Note when using this timer: Timer 0–3, each can only perform one task at the same time, and multiple objects cannot use the same timer.
>>> def fun(args):
        print(“###timer callback function###”)
>>> timer.start(period=1000, mode=timer.PERIODIC, callback=fun)
0
###timer callback function###
###timer callback function###
###timer callback function###
……
```



###### Stop Timer

> **timer.stop()**

It stops timer.

* Parameter

None

* Return Value

Return 0 if the execution is successful, otherwise return -1.



###### Usage Example

```python
'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module timer
@FilePath: example_timer_file.py
'''
import log
import utime
from machine import Timer
import checkNet


'''
The following two global variables are required. Users can modify the values of the following two global variables according to the actual projects.
'''
PROJECT_NAME = "QuecPython_Timer_example"
PROJECT_VERSION = "1.0.0"

# Set the log output level
log.basicConfig(level=log.INFO)
Timer_Log = log.getLogger("Timer")

num = 0
state = 1
# Note: EC100Y-CN module supports Timer0~Timer3
t = Timer(Timer.Timer1)

# Create an execution function and pass in the timer instance
def timer_test(t):
	global num
	global state
	Timer_Log.info('num is %d' % num)
	num += 1
	if num > 10:
		Timer_Log.info('num > 10, timer exit')
		state = 0
		t.stop()   # Stop the timer instance


if __name__ == '__main__':
	t.start(period=1000, mode=t.PERIODIC, callback=timer_test)   # Start the timer
```



##### ExtInt

Function: The module configures I/O pins to interrupt when an external event occurs.

###### Constant Description

| Constant         | Applicable Platform                    | Description    |
| ---------------- | -------------------------------------- | -------------- |
| Pin.GPIO1        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO1          |
| Pin.GPIO2        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO2          |
| Pin.GPIO3        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO3          |
| Pin.GPIO4        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO4          |
| Pin.GPIO5        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO5          |
| Pin.GPIO6        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO6          |
| Pin.GPIO7        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO7          |
| Pin.GPIO8        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO8          |
| Pin.GPIO9        | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO9          |
| Pin.GPIO10       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO10         |
| Pin.GPIO11       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO11         |
| Pin.GPIO12       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO12         |
| Pin.GPIO13       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO13         |
| Pin.GPIO14       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO14         |
| Pin.GPIO15       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO15         |
| Pin.GPIO16       | EC600S / EC600N / EC100Y/EC600U/EC200U | GPIO16         |
| Pin.GPIO17       | EC600S / EC600N / EC100Y               | GPIO17         |
| Pin.GPIO18       | EC600S / EC600N / EC100Y               | GPIO18         |
| Pin.GPIO19       | EC600S / EC600N / EC100Y               | GPIO19         |
| Pin.GPIO20       | EC600S / EC600N                        | GPIO20         |
| Pin.GPIO21       | EC600S / EC600N                        | GPIO21         |
| Pin.GPIO22       | EC600S / EC600N                        | GPIO22         |
| Pin.GPIO23       | EC600S / EC600N                        | GPIO23         |
| Pin.GPIO24       | EC600S / EC600N                        | GPIO24         |
| Pin.GPIO25       | EC600S / EC600N                        | GPIO25         |
| Pin.GPIO26       | EC600S / EC600N                        | GPIO26         |
| Pin.GPIO27       | EC600S / EC600N                        | GPIO27         |
| Pin.GPIO28       | EC600S / EC600N                        | GPIO28         |
| Pin.GPIO29       | EC600S / EC600N                        | GPIO29         |
| Pin.IN           | --                                     | Input mode     |
| Pin.OUT          | --                                     | Output mode    |
| Pin.PULL_DISABLE | --                                     | Floating mode  |
| Pin.PULL_PU      | --                                     | Pull-up mode   |
| Pin.PULL_PD      | --                                     | Pull-down mode |

Constant description for BC25PA platform
| Constant         | Applicable Platform                    | Description    |
| ---------------- | -------------------------------------- | -------------- |
| Pin.GPIO1        | BC25PA                   | GPIO3    |
| Pin.GPIO2        | BC25PA                   | GPIO4    |
| Pin.GPIO3        | BC25PA                   | GPIO5    |
| Pin.GPIO4        | BC25PA                   | GPIO6    |
| Pin.GPIO5        | BC25PA                   | GPIO16   |
| Pin.GPIO6        | BC25PA                   | GPIO20   |
| Pin.GPIO7        | BC25PA                   | GPIO21   |
| Pin.GPIO8        | BC25PA                   | GPIO22   |
| Pin.GPIO9        | BC25PA                   | GPIO23   |
| Pin.GPIO10       | BC25PA                   | GPIO25   |
| Pin.GPIO11       | BC25PA                   | GPIO28   |
| Pin.GPIO12       | BC25PA                   | GPIO29   |
| Pin.GPIO13       | BC25PA                   | GPIO30   |
| Pin.GPIO14       | BC25PA                   | GPIO31   |
| Pin.GPIO15       | BC25PA                   | GPIO32   |
| Pin.GPIO16       | BC25PA                   | GPIO33   |

###### Create ExtInt Object

> **extint = ExtInt(GPIOn, mode, pull, callback)**

* Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| GPIOn     | int  | Pin number<br />The pin correspondence of EC100YCN platform is as follows (pin numbers are external pin numbers):<br />GPIO1 – Pin number 22<br />GPIO2 – Pin number 23<br />GPIO3 – Pin number 38<br />GPIO4 – Pin number 53<br />GPIO5 – Pin number 54<br />GPIO6 – Pin number 104<br />GPIO7 – Pin number 105<br />GPIO8 – Pin number 106<br />GPIO9 – Pin number 107<br />GPIO10 –Pin number 178<br />GPIO11 – Pin number 195<br />GPIO12 – Pin number 196<br />GPIO13 – Pin number 197<br />GPIO14 – Pin number 198<br />GPIO15 – Pin number 199<br />GPIO16 – Pin number 203<br />GPIO17 – Pin number 204<br />GPIO18 – Pin number 214<br />GPIO19 – Pin number 215<br />The pin correspondence of EC600SCN/EC600NCN platform is as follows (pin numbers are external pin numbers):<br />GPIO1 – Pin number 10<br />GPIO2 – Pin number 11<br />GPIO3 – Pin number 12<br />GPIO4 – Pin number 13<br />GPIO5 – Pin number 14<br />GPIO6 – Pin number 15<br />GPIO7 – Pin number 16<br />GPIO8 – Pin number 39<br />GPIO9 – Pin number 40<br />GPIO10 – Pin number 48<br />GPIO11 – Pin number 58<br />GPIO12 – Pin number 59<br />GPIO13 – Pin number60<br />GPIO14 – Pin number 61<br />GPIO15 – Pin number 62<br/>GPIO16 – Pin number 63<br/>GPIO17 – Pin number 69<br/>GPIO18 – Pin number 70<br/>GPIO19 – Pin number 1<br/>GPIO20 – Pin number 3<br/>GPIO21 – Pin number 49<br/>GPIO22 – Pin number 50<br/>GPIO23 – Pin number 51<br/>GPIO24 – Pin number 52<br/>GPIO25 – Pin number 53<br/>GPIO26 – Pin number 54<br/>GPIO27 – Pin number 55<br/>GPIO28 – Pin number 56<br/>GPIO29 – Pin number 57<br />The pin correspondence of EC600UCN platform is as follows (pin numbers are external pin numbers):<br />GPIO1 – Pin number 61<br />GPIO2 – Pin number 58<br />GPIO3 – Pin number 34<br />GPIO4 – Pin number 60<br />GPIO5 – Pin number 69<br />GPIO6 – Pin number 70<br />GPIO7 – Pin number 123<br />GPIO8 – Pin number 118<br />GPIO9 – Pin number 9<br />GPIO10 – Pin number 1<br />GPIO11 – Pin number 4<br />GPIO12 – Pin number 3<br />GPIO13 – Pin number 2<br />GPIO14 – Pin number 54<br />GPIO15 – Pin number 57<br/>GPIO16 – Pin number 56<br/>The pin correspondence of EC200UCN platform is as follows (pin numbers are external pin numbers):<br />GPIO1 – Pin number 27<br />GPIO2 – Pin number 26<br />GPIO3 – Pin number 24<br />GPIO4 – Pin number 25<br />GPIO5 – Pin number 13<br />GPIO6 – Pin number 135<br />GPIO7 – Pin number 136<br />GPIO8 – Pin number 133<br />GPIO9 – Pin number 3<br />GPIO10 – Pin number 40<br />GPIO11 – Pin number 37<br />GPIO12 – Pin number 38<br />GPIO13 – Pin number 39<br />GPIO14 – Pin number 5<br />GPIO15 – Pin number 141<br/>GPIO16 – Pin number 142<br/> |
| mode      | int  | Set the trigger method<br /> IRQ_RISING – Rising edge trigger<br /> IRQ_FALLING – Falling edge trigger<br /> IRQ_RISING_FALLING – Rising and falling edge trigger |
| pull      | int  | PULL_DISABLE – Floating mode<br />PULL_PU – Pull-up mode<br />PULL_PD  – Pull-down mode |
| callback  | int  | Interrupt trigger callback function                          |

* Example

```python
>>> from machine import ExtInt
>>> def fun(args):
        print('### interrupt  {} ###'.format(args))
>>> extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
```




###### Enable Interrupt

> **extint.enable()**

It enables external interrupt of the extint object, when the interrupt pin receives a rising or falling edge signal, it calls callback function to execute. 

* Parameter

NA

* Return Value

0	Successful execution.

-1	Failed execution.



###### Disable Interrupt

> **extint.disable()**

It disables the interrupt associated with the extint object. 

* Parameter

NA

* Return Value

0	Successful execution.

-1	Failed execution.



###### Read Row Number of the Pin Map

> **extint.line()**

It returns the row number of the pin map. 

* Parameter

NA

* Return Value

Row number of the pin map. 

* Example

```python
>>> extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
>>> extint.line()
32
```



##### RTC

Class function: It provides methods to get and set RTC time. 

###### Create RTC Object

> **from machine import RTC**
>
> **rtc = RTC()**



###### Set and Get RTC Time. 

> **rtc.datetime([year, month, day, week, hour, minute, second, microsecond])**

It sets and gets RTC time. When there is no parameter, it gets the time, it sets the time with parameter. When setting the time, the parameter week is not involved, and the parameter microsecond is reserved and not used temporarily, the default is 0. 

* Parameter

| Parameter   | Type | Description                                                  |
| ----------- | ---- | ------------------------------------------------------------ |
| year        | int  | Year                                                         |
| month       | int  | Month, range: 1~12.                                          |
| day         | int  | Day, range:1~31.                                             |
| week        | int  | Week, when setting the time, this parameter does not work, reserved; when getting the time, this parameter is valid. |
| hour        | int  | volume_up hour, range: 0~23.                                 |
| minute      | int  | *content_copy* minute, range:0~59.                           |
| second      | int  | Second, range: 0~59.                                         |
| microsecond | int  | *share* microsecond, reserved, set to 0 when setting the time. |

* Return Value

When getting the time, return a tuple containing the date and time in the following format: 

`[year, month, day, week, hour, minute, second, microsecond]`

0	Successful execution.

-1	Failed execution.

* Example

```python
>>> from machine import RTC
>>> rtc = RTC()
>>> rtc.datetime()
(2020, 9, 11, 5, 15, 43, 23, 0)
>>> rtc.datetime([2020, 3, 12, 1, 12, 12, 12, 0])
0
>>> rtc.datetime()
(2020, 3, 12, 4, 12, 12, 14, 0)
```



##### I2C

Class function: A two-wire protocol used for communication between devices. 

###### Constant Description 

| Constant          |                             | Applicable Platform         |
| ----------------- | --------------------------- | --------------------------- |
| I2C.I2C0          | I2C channel index number: 0 | EC100Y/EC600U/EC200U/BC25PA        |
| I2C.I2C1          | I2C channel index number: 1 | EC600S/EC600N/EC600U/EC200U/BC25PA |
| I2C.STANDARD_MODE | Standard mode               |                             |
| I2C.FAST_MODE     | Fast mode                   |                             |



###### Create I2C Object

> **from machine import I2C**
>
> **i2c_obj = I2C(I2Cn,  MODE)**

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| I2Cn      | int  | I2C channel index number:<br />I2C.I2C0 : 0  <br />I2C.I2C0 : 1 |
| MODE      | int  | I2C working mode:<br />I2C.STANDARD_MODE : 0 Standard mode<br />I2C.FAST_MODE ： 1 Fast mode |

- Pin Correspondence

| Platform      |                                                              |
| ------------- | ------------------------------------------------------------ |
| EC600U        | I2C0:<br />SCL: Pin number 11<br />SDA: Pin number 12<br />I2C1:<br />SCL: Pin number 57<br />SDA: Pin number 56 |
| EC200U        | I2C0:<br />SCL: Pin number 41<br />SDA: Pin number 42<br />I2C1:<br />SCL:Pin number 141<br />SDA:Pin number 142 |
| EC600S/EC600N | I2C1:<br />SCL: Pin number 57<br />SDA: Pin number 56          |
| EC100Y        | I2C0:<br />SCL: Pin number 57<br />SDA: Pin number 56          |
| BC25PA        | I2C0:<br />SCL: Pin number 22<br />SDA: Pin number 23<br />I2C1:<br />SCL: Pin number 20<br />SDA: Pin number 21 |
- Exmaple

```python
from machine import I2C

i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # Return i2c object
```



###### Read Data

> **I2C.read(slaveaddress, addr,addr_len, r_data, datalen, delay)**

It reads data from the I2C bus. 

Parameter

| Parameter    | Type      | Description                                        |
| ------------ | --------- | -------------------------------------------------- |
| slaveaddress | int       | I2C device address.                                |
| addr         | bytearray | I2C register address.                              |
| addr_len     | int       | Length of register address.                        |
| r_data       | bytearray | Byte array of received data.                       |
| datalen      | int       | Length of byte array.                              |
| delay        | int       | Delay, buffer time for data conversion (Unit: ms). |

* Return Value

0	Successful execution.

-1	Failed execution



###### Write Data

> **I2C.write(slaveaddress, addr, addr_len, data, datalen)**

It writes data from the I2C bus. 

* Parameter

| Parameter    | Type      | Description                     |
| ------------ | --------- | ------------------------------- |
| slaveaddress | int       | I2C device address.             |
| addr         | bytearray | I2C register address.           |
| addr_len     | int       | Length of register address.     |
| data         | bytearray | Data written.                   |
| datalen      | int       | The length of the written data. |

* Return Value

0	Successful execution.

-1	Failed execution



###### Example

You need to connect the device when you use it!

```python
import log
from machine import I2C
import utime


'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects. 
'''
PROJECT_NAME = "QuecPython_I2C_example"
PROJECT_VERSION = "1.0.0"

'''
I2C example
'''

# Set the log output level
log.basicConfig(level=log.INFO)
i2c_log = log.getLogger("I2C")


if __name__ == '__main__':
    I2C_SLAVE_ADDR = 0x1B  # i2c device addrress
    # i2c register address, passed in as buff, take the first value and calculate the length of a value. 
	WHO_AM_I = bytearray({0x02, 0})

    data = bytearray({0x12, 0})   # Enter the corresponding command 
    i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # Return i2c object 
    i2c_obj.write(I2C_SLAVE_ADDR, WHO_AM_I, 1, data, 2) # Write data

    r_data = bytearray(2)  # Create a byte array of received data of length 2 
    i2c_obj.read(I2C_SLAVE_ADDR, WHO_AM_I, 1, r_data, 2, 0)   # read
    i2c_log.info(r_data[0])
    i2c_log.info(r_data[1])


```



##### SPI

Class function: Serial peripheral interface bus protocol. 

Adaptation version: EC100Y (V0009) and above; EC600S (V0002) and above. 

###### Create SPI Object

> **spi_obj = SPI(port, mode, clk)**

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| port      | int  | Channel selection[0,1]                                       |
| mode      | int  | SPI working mode (ususally mode 0): <br />Clock polarity CPOL: When SPI is idle, the level of the clock signal SCLK (0: Low level when idle; 1: High level when idle)<br /> 0 : CPOL=0, CPHA=0<br /> 1 : CPOL=0, CPHA=1<br /> 2:  CPOL=1, CPHA=0<br /> 3:  CPOL=1, CPHA=1 |
| clk       | int  | volume_up clock frequency<br /> 0 : 812.5kHz<br /> 1 : 1.625MHz<br /> 2 : 3.25MHz<br /> 3 : 6.5MHz<br /> 4 : 13MHz<br /> 5 :  26MH |

- Pin Description

| Platform      | Pin                                                          |
| ------------- | ------------------------------------------------------------ |
| EC600U        | port0:<br />CS:Pin number 4<br />CLK:Pin number 1<br />MOSI:Pin number 3<br />MISO:Pin number 2<br />port1:<br />CS:Pin number <br />CLK:Pin number <br />MOSI:Pin number <br />MISO:Pin number 60 |
| EC200U        | port0:<br />CS:Pin number 134<br />CLK:Pin number 133<br />MOSI:Pin number 132<br />MISO:Pin number 131<br />port1:<br />CS:Pin number 26<br />CLK:Pin number 27<br />MOSI:Pin number 24<br />MISO:Pin number 25 |
| EC600S/EC600N | port0:<br />CS:Pin number 58<br />CLK:Pin number 61<br />MOSI:Pin number 60<br />MISO:Pin number 59<br />port1:<br />CS:Pin number 4<br />CLK:Pin number 1<br />MOSI:Pin number 3<br />MISO:Pin number 2 |
| EC100Y        | port0:<br />CS:Pin number 25<br />CLK:Pin number 26<br />MOSI:Pin number 27<br />MISO:Pin number 28<br />port1:<br />CS:Pin number 105<br />CLK:Pin number 104<br />MOSI:Pin number 107<br />MISO:Pin number 106 |
| BC25PA        | port0:<br />CS:Pin number 6<br />CLK:Pin number 5<br />MOSI:Pin number 4<br />MISO:Pin number 3|

- Example

```python
from machine import SPI

spi_obj = SPI(1, 0, 1)  # Retuen spi object
```



###### Read Data

> **SPI.read(recv_data, datalen)**

It reads data.

* Parameter

| Paramater | Type      | Description                       |
| --------- | --------- | --------------------------------- |
| recv_data | bytearray | Byte array of received read data. |
| datalen   | int       | The length of the read data.      |

* Return Value

-1	Failed execution



###### Write Data

> **SPI.write(data, datalen)**

It writes data.

* Parameter

| Parameter | Type  | Description             |
| --------- | ----- | ----------------------- |
| data      | bytes | Data written.           |
| datalen   | int   | Length of data written. |

* Return Value

-1	Failed execution



###### Write and Read Data

> **SPI.write_read(r_data，data, datalen)**

It writes and reads data.

* Parameter

| Parameter | Type      | Description                       |
| --------- | --------- | --------------------------------- |
| r_data    | bytearray | Byte array of received read data. |
| data      | bytes     | Data sent.                        |
| datalen   | int       | The length of the read data.      |

* Return Value

-1	Failed execution



###### Example

You need to connect the device when you use it!

```python
import log
from machine import SPI
import utime

'''
SPI example
Adaptation version: EC100Y (V0009) and above; EC600S (V0002) and above 
'''

'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects. 
'''
PROJECT_NAME = "QuecPython_SPI_example"
PROJECT_VERSION = "1.0.0"

spi_obj = SPI(0, 0, 1)

# Set the log output level
log.basicConfig(level=log.INFO)
spi_log = log.getLogger("SPI")


if __name__ == '__main__':
    r_data = bytearray(5)  # Create buff for receiving data 
    data = b"world"  # Write test data 

    ret = spi_obj.write_read(r_data, data, 5)  # Write data and receive 
    spi_log.info(r_data)

```



##### LCD

Class function: This module provides control of the LCD display. 

Adaptation version: EC100Y(V0009) and above; EC600S(V0002) and above. 

Note: The BC25PA platform does not support this module function.

###### Create LCD Object

> **lcd = LCD()**

* Parameter

NA

Example

```python
from machine import LCD 
lcd = LCD()   # Create lcd object
```



###### LCD Initialization 

> **lcd.lcd_init(lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness)**

It initializes LCD. 

- Parameter

| Parameter          | Type      | Description                                                  |
| ------------------ | --------- | ------------------------------------------------------------ |
| lcd_init_data      | bytearray | Inputting configuration commands for LCD.                    |
| lcd_width          | int       | The width of LCD screen, not more than 500.                  |
| lcd_hight          | int       | The height of LCD screen, not more than 500.                 |
| lcd_clk            | int       | LCD SPI clock. SPI clock is 6.5 K/13 K/26 K/52 K.            |
| data_line          | int       | Number of data lines, the parameter values are 1 and 2.      |
| line_num           | int       | The number of lines, the parameter values are 3 and 4.       |
| lcd_type           | int       | Screen type. 0: rgb; 1: fstn.                                |
| lcd_invalid        | bytearray | Inputting configuration commands for LCD area settings.      |
| lcd_display_on     | bytearray | Inputting configuration commands for LCD screen light.       |
| lcd_display_off    | bytearray | Inputting configuration commands for LCD screen off.         |
| lcd_set_brightness | bytearray | Inputting the configuration command of LCD screen brightness. Setting to None indicates that the brightness is controlled by LCD_BL_K (some screens are controlled by registers, and some are controlled by LCD_BL_K) |

* Return Value


  0  	 Successful execution.

  -1  	Initialized.

  -2  	Parameter error (empty or too large (bigger than 1000 pixels)) .

  -3  	Failed cache request.

  -5  	Configuration parameter error.



###### Clear LCD.


> **lcd.lcd_clear(color)**

It clears LCD.

- Parameter

| Parameter | Type        | Description                                 |
| --------- | ----------- | ------------------------------------------- |
| color     | hexadecimal | The color value that needs to be refreshed. |

* Return Value

0	Successful execution.

-1	Failed execution.



###### Regional Writing LCD 

> **lcd.lcd_write(color_buffer,start_x,start_y,end_x,end_y)**

It writes LCD regionally. 

- Parameter

| Parameter    | Type      | Description                       |
| ------------ | --------- | --------------------------------- |
| Color_buffer | bytearray | The color value cache of the LCD. |
| start_x      | int       | Starting x coordinate.            |
| start_y      | int       | Starting y coordinate.            |
| end_x        | int       | End x coordinate.                 |
| end_y        | int       | End y coordinate.                 |

* Return Value

  0   	Successful execution.

  -1  	The screen is not initialized.

  -2  	Wrong width and height settings.

  -3  	Data cache is empty.



###### Set Screen Brightness 

> **lcd.lcd_brightness(level)**

It sets the screen brightness level. 

- Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| level     | int  | Brightness level. The lcd_set_brightness callback in lcd.lcd_init() will be called. If this parameter is None, the brightness adjustment is controlled by the brightness adjustment pin.<br />Range [0,5]. |

* Return Value

0	Successful execution.

-1	Failed execution.



###### Turn on LCD Display 

> **lcd.lcd_display_on()**

It turns on the LCD display, call the lcd_display_on callback in lcd.lcd_init() after calling this interface. 

- Parameter

NA

* Return Value

0	Successful execution.

-1	Failed execution.



###### Turn off LCD Display 

> **lcd.lcd_display_off()**

It turns off the LCD display, call the  lcd_display_off callback in lcd.lcd_init() after calling this interface. 

- Parameter

NA

* Return Value

0	Successful execution.

-1	Failed execution.



###### Write Command

> **lcd.lcd_write_cmd(cmd_value, cmd_value_len)**

It writes command.

- Parameter

| Parameter     | Type        | Description              |
| ------------- | ----------- | ------------------------ |
| cmd_value     | hexadecimal | Command value.           |
| cmd_value_len | int         | Length of command value. |

* Return Value

0	Successful execution.

Other value	Failed execution.



###### Write Data

> **lcd.lcd_write_data(data_value, data_value_len)**

It writes data.

- Parameter

| Parameter      | Type        | Description           |
| -------------- | ----------- | --------------------- |
| data_value     | hexadecimal | Data value.           |
| data_value_len | int         | Length of data value. |

* Return Value

0	Successful execution.

Other value	Failed execution.



###### Display Image 

> **lcd.lcd_show(file_name, start_x,start_y,width,hight)**

It displays images by reading files.

This file is a bin file generated by Image2Lcd tool. If you check the header file including image, you don’t need to fill in the  width and hight.

- Parameter

| Parameter | Type      | Description                                                  |
| --------- | --------- | ------------------------------------------------------------ |
| file_name | file name | Image to be displayed.                                       |
| start_x   | int       | Starting x coordinate.                                       |
| start_y   | int       | Starting y coordinate.                                       |
| width     | int       | Image width (if the image file contains header information, leave it blank) |
| hight     | int       | Image height (if the image file contains header information, leave it blank) |

* Return Value

0	Successful execution.

Other value	Failed execution.



###### Example

It needs to be used with LCD, the following code takes ili9225 as an example! 

```python
from machine import LCD 
#Generally there are two LCD settings: 
#First: Write twice: high eight bits and low eight bits 
XSTART_H = 0xf0
XSTART_L = 0xf1
YSTART_H = 0xf2
YSTART_L = 0xf3
XEND_H = 0xE0
XEND_L = 0xE1
YEND_H = 0xE2
YEND_L = 0xE3
#Second: Write one short per time 
XSTART = 0xD0
XEND = 0xD1
YSTART = 0xD2
YEND = 0xD3


init_data = (0,1,0x02, 1,2,0x01,0x00, 0,1,0x01, 1,2,0x01,0x1C, 0,1,0x03, 1,2,0x10,0x30, 0,1,0x08, 1,2,0x08,0x08, 0,1,0x0B, 1,2,0x11,0x00, 0,1,0x0C, 1,2,0x00,0x00, 0,1,0x0F, 1,2,0x14,0x01, 0,1,0x15, 1,2,0x00,0x00, 0,1,0x20, 1,2,0x00,0x00, 0,1,0x21, 1,2,0x00,0x00, 0,1,0x10, 1,2,0x08,0x00, 0,1,0x11, 1,2,0x1F,0x3F, 0,1,0x12, 1,2,0x01,0x21, 0,1,0x13, 1,2,0x00,0x0F, 0,1,0x14, 1,2,0x43,0x49, 0,1,0x30, 1,2,0x00,0x00, 0,1,0x31, 1,2,0x00,0xDB, 0,1,0x32, 1,2,0x00,0x00, 0,1,0x33, 1,2,0x00,0x00, 0,1,0x34, 1,2,0x00,0xDB, 0,1,0x35, 1,2,0x00,0x00, 0,1,0x36, 1,2,0x00,0xAF, 0,1,0x37, 1,2,0x00,0x00, 0,1,0x38, 1,2,0x00,0xDB, 0,1,0x39, 1,2,0x00,0x00, 0,1,0x50, 1,2,0x00,0x01, 0,1,0x51, 1,2,0x20,0x0B, 0,1,0x52, 1,2,0x00,0x00, 0,1,0x53, 1,2,0x04,0x04, 0,1,0x54, 1,2,0x0C,0x0C, 0,1,0x55, 1,2,0x00,0x0C, 0,1,0x56, 1,2,0x01,0x01, 0,1,0x57, 1,2,0x04,0x00, 0,1,0x58, 1,2,0x11,0x08, 0,1,0x59, 1,2,0x05,0x0C, 0,1,0x07, 1,2,0x10,0x17, 0,1,0x22)

display_on_data = (
0,1,0x07,
1,2,0x10,0x17,
)
display_off_data = (
0,1,0x07,
1,2,0x10,0x04,
)
invalid_data = (
    0,1,0x36,
    1,2,XEND,
    0,1,0x37,
    1,2,XSTART,
    0,1,0x38,
    1,2,YEND,
    0,1,0x39,
    1,2,YSTART,
    0,1,0x20,
    1,2,XSTART,
    0,1,0x21,
    1,2,YSTART,
    0,1,0x22,
)

lcd = LCD()
init_list = bytearray(init_data)
display_on_list = bytearray(display_on_data)
display_off_list = bytearray(display_off_data)
invalid_list = bytearray(invalid_data)

    
lcd.lcd_init(init_list, 176,220,13000,1,4,0,invalid_list,display_on_list,display_off_list,None)

Color_buffer =(0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f, 0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00,0x1f,0x00, 0x1f) 

Color_buffer = bytearray(Color_buffer) 

lcd.lcd_write(Color_buffer,10,10,20,20)
lcd.lcd_clear(0xf800) # Red

lcd.show("lcd_test.bin",0,0)	#The lcd_test.bin contains image header data.
lcd.show("lcd_test1.bin",0,0,126,220) #The lcd_test1.bin does not contain image header data.
```




##### WDT 

Module function: Restart the system when the APP is abnormal and does not execute.

###### Create WDT Object

> ​	**wdt = WDT(period)**

It creates a software watchdog object. 

- Parameter

| Parameter | Type | Description                                      |
| :-------- | :--- | ------------------------------------------------ |
| period    | int  | Set software watchdog detection time, unit (s)。 |

* Return Value

It returns software watchdog object.



###### Feed Watchdog

> ​	**wdt.feed()**

It feeds watchdog. 

- Parameter

NA

* Return Value

NA



###### Stop Watchdog

> ​	**wdt.stop()**

It stops watchdog. 

- Parameter

NA

* Return Value

NA



###### Example

```PYTHON
'''
@Author: Pawn
@Date: 2020-08-12
@LastEditTime: 2020-08-12 17:06:08
@Description: example for module timer
@FilePath: example_wdt.py
'''

from machine import WDT
from machine import Timer
import utime


'''
The following two global variables are required. Users can modify the values of the following two global variables according to their actual projects. 
'''
PROJECT_NAME = "QuecPython_WDT_example"
PROJECT_VERSION = "1.0.0"

timer1 = Timer(Timer.Timer1)

def feed(t):
    wdt.feed()


if __name__ == '__main__':
    wdt = WDT(20)  # Enable watchdog,interval length
    timer1.start(period=15000, mode=timer1.PERIODIC, callback=feed)  # Feed watchdog by using timer.

    # wdt.stop()

```



#### qrcode- QR Code Display 

Module function:  Generate the corresponding QR code according to the input content. 
Note: The BC25PA platform does not support this module function.

> ​	qrcode.show(qrcode_str,magnification,start_x,start_y,Background_color,Foreground_color)

- Parameter

| Parameter        | Type   | Description                                          |
| :--------------- | :----- | ---------------------------------------------------- |
| qrcode_str       | string | QR code cotent.                                      |
| magnification    | int    | Magnification [1,6].                                 |
| start_x          | int    | QR code display starting x coordinate.               |
| start_y          | int    | QR code display starting y coordinate.               |
| Background_color | int    | Foreground color (if not set, the default is 0xffff) |
| Foreground_color | int    | Background color (if not set, the default is 0x0000) |

* Return Value

0       Successful execution.

-1     Failed to generate QR code.

-2     Failed magnification. 

-3     Failed display.



#### pm - Low Power

Module function: When there is no business processing, the system enters the sleep state and enters the low power mode.

##### Create wake_lock Lock 

> ​	**lpm_fd = pm.create_wakelock(lock_name, name_size)**

It creates wake_lock lock.

- Parameter

| Parameter | Type   | Description          |
| :-------- | :----- | -------------------- |
| lock_name | string | Custom lock name.    |
| name_size | int    | Length of lock name. |

* Return Value

wakelock's Identification number   Successful execution.

-1   Failed execution.

* note

  The BC25PA platform does not support this method.


##### Delete wake_lock Lock 

> ​	**pm.delete_wakelock(lpm_fd)**

It deletes wake_lock lock. 

- Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| lpm_fd    | int  | The corresponding identification ID of the lock to be deleted. |

* Return Value

0      Successful execution.

* note

  The BC25PA platform does not support this method.


##### Lock 

> ​	**pm.wakelock_lock(lpm_fd)**

- Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| lpm_fd    | int  | The wakelock identification ID that needs to perform the lock operation. |

* Return Value

0	Successful execution.

-1	Failed execution.

* note

  The BC25PA platform does not support this method.


##### Release Lock 

> ​	**pm.wakelock_unlock(lpm_fd)**

It releases lock.

- Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| lpm_fd    | int  | The wakelock identification ID that needs to perform the lock release operation. |

* Return Value

0	Successful execution.

-1	Failed execution.

* note

  The BC25PA platform does not support this method.

##### Automatic Sleep Mode Control 

> ​	**pm.autosleep(sleep_flag)**

It controls automatic sleep mode.

- Parameter

| Parameter  | Type | Description                                                  |
| :--------- | :--- | ------------------------------------------------------------ |
| sleep_flag | int  | 0, turn off automatic sleep mode; 1 turn on automatic sleep mode. |

* Return Value

0	Successful execution.



##### Get the number of locks created 

> ​	**pm.get_wakelock_num()**

It gets the number of locks created.

- Parameter

NA

* Return Value

It returns the number of wakelock locks that have been created. 

* note

  The BC25PA platform does not support this method.


##### Example

Simulation test, for actual development, please select and use according to service scenarios!  

```python
import pm
import utime

# Create wakelock lock 
lpm_fd = pm.create_wakelock("test_lock", len("test_lock"))
# Set automatic sleep mode 
pm.autosleep(1)

# Simulation test, for actual development, please select and use according to service scenarios.
while 1:
    utime.sleep(20)  # Sleep mode
    res = pm.wakelock_lock(lpm_fd)
    print("ql_lpm_idlelock_lock, g_c1_axi_fd = %d" %lpm_fd)
    print("unlock  sleep")
    utime.sleep(20)
    res = pm.wakelock_unlock(lpm_fd)
    print(res)
    print("ql_lpm_idlelock_unlock, g_c1_axi_fd = %d" % lpm_fd)
    num = pm.get_wakelock_num()  # Get the number of created locks 
    print(num)
```



#### ure - Regular Expression

Module function: Provide matching data through regular expressions. (PS: this re module currently supports fewer operators, and some operators are not currently supported) 

##### Supported Operators 

| **Operator** | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| ‘.’          | Match any character.                                         |
| ‘[]’         | Match character set, currently supports single character and a range, including negative set. |
| ‘^’          | volume_up matches the beginning of the string.               |
| ‘$’          | *content_copy* matches the end of the string.                |
| ‘?’          | Match zero or one of the preceding subpatterns.              |
| ‘*’          | *share* matches zero or more previous subpatterns.           |
| ‘+’          | Match zero or more previous subpatterns.                     |
| ‘??’         | Non-greedy version of ? ,matches 0 or 1.                     |
| ‘*?’         | Non-greedy version of *, matches zero or more.               |
| ‘+?’         | Non-greedy version of +, matches one or more.                |
| ‘\|’         | Match the left sub-pattern or the right sub-pattern of the operator. |
| ‘\d’         | olume_up number matching                                     |
| ‘\D’         | *content_copy* non-number matching                           |
| '\s'         | Match spaces.                                                |
| '\S'         | *share* matches non-space.                                   |
| ‘\w’         | Match "word characters" (ASCII only).                        |
| ‘\W’         | Match non-"word characters" (ASCII only).                    |

**Not Supported：**

- Repeat times  (`{m,n}`)
- Named group  (`(?P<name>...)`)
- Non-capturing group (`(?:...)`)
- Higher-level assertions (`\b`, `\B`)
- Escaping special characters, such as  `\r`, `\n` -Use Python's escaping instead. 



##### Compile and Generate Regular Expression Object 

> ​	**ure.compile(regex)**

The compile function compiles regular expressions and generate a regular expression (Pattern) object for use by match() and search() functions.

- Parameter

| ParamEter | Type   | Description         |
| :-------- | :----- | ------------------- |
| regex     | string | Regular expression. |

* Return Value

It returns regex object.



#####  Match

> ​	**ure.match(regex, string)**

It matches the regular expression object with string, usually from the beginning of the string.

- Parameter

| Parameter | Type   | Description                |
| :-------- | :----- | -------------------------- |
| regex     | string | Regular expression.        |
| string    | string | String data to be matched. |

* Return Value

A matched object   Successful execution.

None   Failed execution.



##### Search

> ​	**ure.search(regex, string)**

ure.search scans the entire string and returns the first successful match. 

- Parameter

| Parameter | Type   | Description                |
| :-------- | :----- | -------------------------- |
| regex     | string | Regular expression.        |
| string    | string | String data to be matched. |

* Return Value

A matched object   Successful execution.

None   Failed execution.



**Match Object**

It matches objects returned by the match() and search methods.

##### Match a Single String 

> ​	**match.group(index)**

It  matches the string of the entire expression.

- Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| index     | int  | In the regular expression, group() proposes the string intercepted by the group, index=0 returns the whole, and it is obtained according to the written regular expression. When the group does not exist, an exception is thrown. |

* Return Value

It returns the string of the matched entire expression. 



##### Match Multiple Strings 

> ​	**match.groups()**

It  matches the string of the entire expression.

- Parameter

NA

* Return Value

It returns a tuple containing all substrings of the matching group. 



##### Get Start Index 

> ​	**match.start(index)**

It returns the index of the starting original string of the matched substring group. 

- Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| index     | int  | Index defaults to the entire group, otherwise a group is selected. |

* Return Value

It returns the index of the starting original string of the matched substring group. 

##### Get End Index 

> ​	**match.end(index)**

It returns the index of the ending original string of the matched substring group. 

- Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| index     | int  | Index defaults to the entire group, otherwise a group is selected. |

* Return Value

It returns the index of the ending original string of the matched substring group. 

##### Example

```python
import ure

res = '''
$GNRMC,133648.00,A,3149.2969,N,11706.9027,E,0.055,,311020,,,A,V*18
$GNGGA,133648.00,3149.2969,N,11706.9027,E,1,24,1.03,88.9,M,,M,,*6C
$GNGLL,3149.2969,N,11706.9027,E,133648.00,A,A*7A
$GNGSA,A,3,31,26,11,194,27,195,08,09,03,193,04,16,1.41,1.03,0.97,1*31
'''

r = ure.search("GNGGA(.+?)M", res)
print(r.group(0))
```

####  wifiScan

Note: The BC25PA platform does not support this module function.

##### Determine whether wifiScan is supported

> **wifiScan.support()**

* Function：

  Determine whether the module supports wifiScan function.

* Parameter：

  None

* Return Value：

  True	 wifiScan is supported

  False	wifiScan is not supported

* Example：

```python 
>>> import wifiScan
>>> wifiScan.support()
True
```



##### Control wifiScan Function

> **wifiScan.control(option)**

* Function:

  Control wifiScan function.

* Parameter:

| Parameter | Type         | Description                                                  |
| --------- | ------------ | ------------------------------------------------------------ |
| option    | Integer type | 0 - Disable wifiscan function<br>1 - Enable wifiscan function |

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example:

```python
>>> wifiScan.control(1) # Enable wifiScan function
0
>>> wifiScan.control(0) # Disable wifiScan function
0
```



##### Get wifiScan State

> **wifiScan.getState()**

* Function：

  Get the wifiScan state. wifiScan is enabled or disabled. 200U/600U modules are disabled by default. wifiScan.control(1) is required to enable wifiScan before using wifiScan function.

* Parameter：

  None

* Return Value：

  True	 wifiScan function is enabled

  False	wifiScan function is disabled.

* Example：

```python
>>> wifiScan.getState()
True
```



##### Get wifiScan Configuration

> **wifiScan.getConfig()**

* Function：

  Get wifiScan configuration.

* Parameter：

  None

* Return Value：

  A tuple	Successful execution

  -1		     Failed execution 

  The format of the returned tuple is as follows:

  `(timeout, round, max_bssid_num, scan_timeout, priority)`

  | Return Value  | Type         | Description                                                  |
  | ------------- | ------------ | ------------------------------------------------------------ |
  | timeout       | Integer type | This parameter is the timeout of upper layer application. When the application triggers timeout, it actively reports the scanned hot spot information. The application automatically reports the hot spot information if it scans all the hop spots which have been set previously or the underlying layer scan reaches the frequency sweeping timeout before the timeout of the application. Range: 4–255. Unit: second. |
  | round         | Integer type | This parameter is the scanning rounds of wifi. When reaching the scanning rounds, the scan stops and the scanning results are obtained. Range: 1–3. Unit: round. |
  | max_bssid_num | Integer type | This parameter determines the maximum number of hot spots to be scanned. If the number of hot spots scanned by the underlying layer reaches the maximum, the scan stops and the scanning results are obtained. Range: 4–30. |
  | scan_timeout  | Integer type | This parameter is the wifi hot spot scanning timeout of underlying layer. If the underlying layer scan reaches the hot spot scanning timeout set previously,  the scan stops and the scanning results are obtained. Range: 1–255. Unit: second. |
  | priority      | Integer type | This parameter is the priority setting of wifi scanning service. 0 indicates that ps is preferred; 1 indicates that wifi is preferred. When ps is preferred,  the wifi scan is terminated when a data service is initiated. When wifi is preferred, RRC connection is not connected when a data service is initiated. wifi scan runs normally. The RRC connection is only established after the scan completes. |

* Example：

```python
>>> wifiScan.getConfig()
(6, 1, 5, 1, 0)
```



##### Configure wifiScan Function

> **wifiScan.setConfig(timeout, round, max_bssid_num, scan_timeout, priority)**

* Function：

  Configure wifiScan function.

* Parameter：

  | Parameter     | Type         | Description                                                  |
  | ------------- | ------------ | ------------------------------------------------------------ |
  | timeout       | Integer type | This parameter is the timeout of upper layer application. When the application triggers timeout, it actively reports the scanned hot spot information. The application automatically reports the hot spot information if it scans all the hop spots which have been set previously or the underlying layer scan reaches the frequency sweeping timeout before the timeout of the application. <br>Range:<br/>600S: 4–255; unit: second.<br/>200U/600U: 120–5000; unit: second. |
  | round         | Integer type | This parameter is the scanning rounds of wifi. When reaching the scanning rounds, the scan stops and the scanning results are obtained. <br/>Range:<br/>600S: 1–3; unit: round<br/>200U/600U: 1–10; unit: round |
  | max_bssid_num | Integer type | This parameter determines the maximum number of hot spots to be scanned. If the number of hot spots scanned by the underlying layer reaches the maximum, the scan stops and the scanning results are obtained. <br/>Range:<br/>600S: 4–30<br/>200U/600U: 1–300 |
  | scan_timeout  | Integer type | This parameter is the wifi hot spot scanning timeout of underlying layer. If the underlying layer scan reaches the hot spot scanning timeout set previously,  the scan stops and the scanning results are obtained. Range: 1–255. Unit: second. |
  | priority      | Integer type | This parameter is the priority setting of wifi scanning service. 0 indicates that ps is preferred; 1 indicates that wifi is preferred. When ps is preferred, the wifi scan is terminated when a data service is initiated. When wifi is preferred, RRC connection is not connected when a data service is initiated. wifi scan runs normally. The RRC connection is only established after the scan completes. |

* Return Value：

  0	 Successful execution

  -1	Failed execution

* Example：

```python
>>> wifiScan.setConfig(5, 2, 6, 3, 0)
0
```



##### Register Callback Function

> **wifiScan.setCallback(usrFun)**

* Function：

  Register user callback function. When scanning hot spot through asynchronous function, users need to register callback function. And the scanning results are returned to users through the callback function.

* Parameter：

  | Parameter | Type     | Description            |
  | --------- | -------- | ---------------------- |
  | usrFun    | function | User callback function |

* Return Value：

  0	 Successful execution

  -1	Failed execution

* Example：

```python
def usr_cb(args):
	print('wifi list:{}'.format(args))
wifiScan.setCallback(usr_cb)
```



##### Start wifiScan Scan-Asynchronous Function

> **wifiScan.asyncStart()**

* Function：

  Start wifiScan scan. The scanning result is returned through the registered callback function.

* Parameter：

  None

* Return Value：

  0	 Successful execution

  -1	Failed execution

* Example：

```python
def usr_cb(args):
	print('wifi list:{}'.format(args))
wifiScan.setCallback(usr_cb)

wifiScan.asyncStart()

'''
Execution result：
wifi list:(2, [('F0:B4:29:86:95:C7': -79),('44:00:4D:D5:26:E0', -92)])
'''
```



##### Start wifiScan Scan-Synchronous API

> **wifiScan.start()**

* Function：

  Start wifiScan function. The scanning result is returned after the scan is complete. As this function is synchronous, the program is blocked in the function when the scan is not complete. And the blocking time is usually 0–2 seconds.

* Parameter：

  None

* Return Value：

  Scanning result	Successful execution

  -1							Failed execution or error

  The return value of successful execution is as follows:

  `（wifi_nums, [(mac, rssi), ... , (mac, rssi)]）`

  | Parameter | Type         | Description                                  |
  | --------- | ------------ | -------------------------------------------- |
  | wifi_nums | Integer type | The number of wifi which has been searched   |
  | mac       | String type  | The MAC address of the wireless access point |
  | rssi      | Integer type | Signal strength                              |

* Example：

```python
>>> wifiScan.start()
(2, [('F0:B4:29:86:95:C7': -79),('44:00:4D:D5:26:E0', -92)])
```



#### ble - Bluetooth Low Energy

Module function: provide function of BLE GATT Server. Currently only 200U/600U modules support BLE.
Note: The BC25PA platform does not support this module function.

##### Initialize BLE and Register Callback Function

> **ble.serverInit(user_cb)**

* Function：

Initialize BLE SERVER and register callback function.

* Parameter：

| Parameter | Type     | Description       |
| --------- | -------- | ----------------- |
| user_cb   | function | Callback function |

* Return Value：

0	 Successful execution

-1	Failed execution

Description：

（1）Format of callback function

```python
def ble_callback(args):
	event_id = args[0]  # The first parameter is fixed as event_id
	status = args[1] # The second parameter is fixed as status which indicates the execution result of an operation, such as BLE 						is enabled successfully or unsuccessfully.
	......
```

（2）Description of callback function parameter 

args[0] is fixed to represent event_id; args[1] is fixed to represent status. 0 indicates a success; non-0 indicates a failure. The number of callback function parameter is not fixed as 2; instead it is determined by the first parameter args[0]. The number of parameters and descriptions corresponding to the different event IDs are as follows.

| event_id | Number of Parameter | Parameter Description                                        |
| :------: | :-----------------: | ------------------------------------------------------------ |
|    0     |          2          | args[0]: event_id, which indicates BT/BLE starts<br>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution |
|    1     |          2          | args[0]: event_id, which indicates BT/BLE stops<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution |
|    16    |          4          | args[0]: event_id, which indicates BLE connects<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2]: connect_id<br/>args[3]: addr, BT/BLE address |
|    17    |          4          | args[0]: event_id, which indicates that BLE disconnects<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2]: connect_id, <br/>args[3]: addr, BT/BLE address |
|    18    |          7          | args[0]: event_id, which indicates BLE update connection parameter<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2]: connect_id<br/>args[3]: max_interval, maximum interval. Interval: 1.25ms. Range: 6–3200. Time Range: 7.5ms–4s<br/>args[4]: min_interval, maximum interval. Interval: 1.25ms. Range: 6–3200. Time Range: 7.5ms–4s<br/>args[5]: latency, the time during which the slave ignores the connection state events. It needs to meet the formula（1+latecy)\*max_interval\*2\*1.25<timeout\*10<br/>args[6]: timeout,  the disconnection timeout period when there is no interaction, interval:10ms. Range: 10–3200. Time range: 100ms–32s. |
|    20    |          4          | args[0]: event_id, which indicates BLE connection mtu<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2]: handle<br/>args[3]: mtu value |
|    21    |          7          | args[0]: event_id, which indicates BLE server: when ble client write characteristic value or descriptor,server get the notice<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2]: data_len, the length of the acquired data<br/>args[3]: data, an array for storing the acquired data<br/>args[4]: attr_handle, attribute handle, integer type<br/>args[5]: short_uuid, integer type<br/>args[6]: long_uuid, a 16-byte array for storing long UUID |
|    22    |          7          | args[0]: event_id, which indicates server: when ble client read characteristic value or descriptor,server get the notice<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2]: data_len, the length of the acquired data<br/>args[3]: data, an array for storing the acquired data<br/>args[4]: attr_handle, attribute handle, integer type<br/>args[5]: short_uuid, integer type<br/>args[6]: long_uuid, a 16-byte array for storing long UUID |
|    25    |          2          | args[0]: event_id, which indicates server send notification,and recieve send end notice<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution |

* Example：

```python 
def ble_callback(args):
    event_id = args[0]
    status = args[1]
    print('[ble_callback]: event_id={}, status={}'.format(event_id, status))

    if event_id == 0:  # ble start
        if status == 0:
            print('[callback] BLE start success.')
        else:
            print('[callback] BLE start failed.')
    elif event_id == 1:  # ble stop
        if status == 0:
            print('[callback] ble stop successful.')
        else:
            print('[callback] ble stop failed.')
    elif event_id == 16:  # ble connect
        if status == 0:
            print('[callback] ble connect successful.')
            connect_id = args[2]
            ble_addr = args[3]
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, ble_addr))
        else:
            print('[callback] ble connect failed.')
    elif event_id == 17:  # ble disconnect
        if status == 0:
            print('[callback] ble disconnect successful.')
            connect_id = args[2]
            ble_addr = args[3]
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, ble_addr))
        else:
            print('[callback] ble disconnect failed.')
            ble.gattStop()
            return
    elif event_id == 18:  # ble update connection parameter
        if status == 0:
            print('[callback] ble update parameter successful.')
            connect_id = args[2]
            max_interval = args[3]
            min_interval = args[4]
            latency = args[5]
            timeout = args[6]
            print('[callback] connect_id={},max_interval={},min_interval={},latency={},timeout={}'.format(connect_id, max_interval, min_interval, latency, timeout))
        else:
            print('[callback] ble update parameter failed.')
            ble.gattStop()
            return
    elif event_id == 20:  # ble connection mtu
        if status == 0:
            print('[callback] ble connect mtu successful.')
            handle = args[2]
            ble_mtu = args[3]
            print('[callback] handle = {}, ble_mtu = {}'.format(handle, ble_mtu))
        else:
            print('[callback] ble connect mtu failed.')
            ble.gattStop()
            return
    elif event_id == 21:  # server:when ble client write characteristic value or descriptor,server get the notice
        if status == 0:
            print('[callback] ble recv successful.')
            data_len = args[2]
            data = args[3]  # this ia a bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # this ia a bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {}'.format(attr_handle))
            print('short uuid = {}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv failed.')
            ble.gattStop()
            return
    elif event_id == 22:  # server:when ble client read characteristic value or descriptor,server get the notice
        if status == 0:
            print('[callback] ble recv read successful.')
            data_len = args[2]
            data = args[3]  # this ia a bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # this ia a bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {}'.format(attr_handle))
            print('short uuid = {}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv read failed.')
            ble.gattStop()
            return
    elif event_id == 25:  # server send notification,and recieve send end notice
        if status == 0:
            print('[callback] ble send data successful.')
        else:
            print('[callback] ble send data failed.')
    else:
        print('unknown event id.')

ble.serverInit(ble_callback)
```



##### Release BLE SERVER Resources 

> **ble.serverRelease()**

* Function:

  Release BLE SERVER resources.

* Parameter:

  None

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example：

```python
See comprehensive example
```



##### Start  BLE GATT Function

> **ble.gattStart()**

* Function:

  Start BLE GATT fucntion.

* Parameter:

  None

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example:

```python
See comprehensive example
```



##### Stop BLE GATT Function

> **ble.gattStop()**

* Function:

  Stop BLE GATT function.

* Parameter:

  None

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example:

```python
See comprehensive example
```



##### Set BLE Local Name

> **ble.setLocalName(code, name)**

* Function:

  Set BLE local name.

* Parameter:

  | Parameter | Type         | Description                           |
  | --------- | ------------ | ------------------------------------- |
  | code      | Integer Type | Encoding mode<br>0 - UTF8<br/>1 - GBK |
  | name      | String Type  | BLE name, no more than 29 bytes       |

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example:

```python
>>> ble.setLocalName(0, 'QuecPython-BLE')
0
```



##### Set Advertising Parameter

> **ble.setAdvParam(min_adv,max_adv,adv_type,addr_type,channel,filter_policy,discov_mode,no_br_edr,enable_adv)**

* Function:

  Set advertising parameter.

* Parameter

  | Parameter     | Type                  | Description                                                  |
  | ------------- | --------------------- | ------------------------------------------------------------ |
  | min_adv       | Unsigned integer type | Minimal advertising interval. Range: 0x0020–0x4000. It is calculated as follows:<br>Time interval = min_adv \* 0.625. Unit: ms |
  | max_adv       | Unsigned integer type | Maximum advertising interval. Range: 0x0020–0x4000. It is calculated as follows:<br/>Time interval = max_adv \* 0.625. Unit: ms |
  | adv_type      | Unsigned integer type | Advertising type. <br>0 - CONNECTABLE UNDIRECTED, default <br>1 - CONNECTABLE HIGH DUTY CYCLE DIRECTED<br>2 - SCANNABLE UNDIRECTED<br>3 - NON CONNECTABLE UNDIRECTED<br>4 - CONNECTABLE LOW DUTY CYCLE DIRECTED |
  | addr_type     | Unsigned integer type | Local address type.  <br>0 - Public address<br>1 - Random address |
  | channel       | Unsigned integer type | Advertising channel. <br>1 - Advertising channel 37<br>2 - Advertising channel 38<br>4 - Advertising channel 39<br>7 - Advertising channel 37 and 38 and 39, default |
  | filter_policy | Unsigned integer type | Advertising filter policy.<br>0 - Process scan and connection requests from all devices<br/>1 - Process connection requests from all devices and scan requests from only white list devices<br/>2 - Process scan requests from all devices and connection requests from only white list devices<br/>3 - Process connection and scan requests from only white list devices |
  | discov_mode   | Unsigned integer type | Discovery mode. Used by GAP protocol and the default is 1 (normal discovery mode) |
  | no_br_edr     | Unsigned integer type | No use of BR/EDR. The default is 1. The value is 0 if BR/EDR is used. |
  | enable_adv    | Unsigned integer type | Enable advertising. The default is 1. The value is 0 if advertising is disabled. |

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example：

```python
def ble_gatt_set_param():
    min_adv = 0x300
    max_adv = 0x320
    adv_type = 0  # CONNECTABLE UNDIRECTED, default
    addr_type = 0  # public address
    channel = 0x07
    filter_strategy = 0  # process scan and connection requests from all devices
    discov_mode = 2
    no_br_edr = 1
    enable_adv = 1
    ret = ble.setAdvParam(min_adv, max_adv, adv_type, addr_type, channel, filter_strategy, discov_mode, no_br_edr, enable_adv)
    if ret != 0:
        print('ble_gatt_set_param failed.')
        return -1
    print('ble_gatt_set_param success.')
    return 0
```



##### Set Advertising Data

> **ble.setAdvData(data)**

* Function:

  Set advertising data.

* Parameter:

  | Parameter | Type  | Description                                                  |
  | --------- | ----- | ------------------------------------------------------------ |
  | data      | Array | Advertising data which is no more than 31 octets. Pay attention to the type of this parameter. The advertising data is organized in the program and it needs to be converted through bytearray() before it can be passed in to the API. As shown in below example.<br>Format of advertising data:<br>The content of advertising data. The format is the combination of length+type+data. An advertising data can contain multiple combinations in this format. For example, there are 2 combinations in the example below. The first one is "0x02, 0x01, 0x05". 0x02 means that there are 2 data - 0x01 and 0x05. 0x01 is the type; 0x05 is the specific data. The second one consists of  the length obtained by the length of BLE name plus 1 (1 octet needs to be added as it contains the data that represents type), type 0x09 and the data represented by the corresponding specific encoded value of name.<br>For detailed information of type value, please refer to the following link:<br/>https://www.bluetooth.com/specifications/assigned-numbers/generic-access-profile/ |

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example：

```python
def ble_gatt_set_data():
    adv_data = [0x02, 0x01, 0x05]
    ble_name = "Quectel_ble"
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvData(data)
    if ret != 0:
        print('ble_gatt_set_data failed.')
        return -1
    print('ble_gatt_set_data success.')
    return 0
```



##### Set Scan Response Data

> **ble.setAdvRspData(data)**

* Function:

  Set scan response data.

* Parameter:

  | Parameter | Type  | Description                                                  |
  | --------- | ----- | ------------------------------------------------------------ |
  | data      | Array | Scan response data which is no more than 31 octets. The considerations are consistent with the description of  *ble.setAdvData(data)* above. The setting of scan response data makes sense only when the scanning mode of the client device is active scan. |

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example:

```python
def ble_gatt_set_rsp_data():
    adv_data = []
    ble_name = "Quectel_ble"
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_rsp_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvRspData(data)
    if ret != 0:
        print('ble_gatt_set_rsp_data failed.')
        return -1
    print('ble_gatt_set_rsp_data success.')
    return 0
```



##### Add a Service

> **ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)**

* Function：

  Add a service.

* Parameter：

  | Parameter | Type                  | Description                                                  |
  | --------- | --------------------- | ------------------------------------------------------------ |
  | primary   | Unsigned integer type | Service type. 1- Primary service; Other value - Secondary service |
  | server_id | Unsigned integer type | Service ID, which determines a service                       |
  | uuid_type | Unsigned integer type | UUID type<br>0 - Long UUID, 128bit<br>1 - Short UUID, 16bit  |
  | uuid_s    | Unsigned integer type | Short UUID, 2 bytes (16bit). When uuid_type is 0, the value of this parameter is 0. |
  | uuid_l    | Array                 | Long UUID, 16 bytes (128bit). When uuid_type is 1, the value of this parameter is bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) |

* Return Value：

  0	 Successful execution

  -1	Failed execution

* Example：

```python
def ble_gatt_add_service():
    primary = 1
    server_id = 0x01
    uuid_type = 1  # short UUID
    uuid_s = 0x180F
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_service failed.')
        return -1
    print('ble_gatt_add_service success.')
    return 0
```



##### Add a Characteristic 

> **ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)**

* Function:

  Add a characteristic in a service.

* Parameter:

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | server_id  | Unsigned integer type | Service ID, which determines a service                       |
  | chara_id   | Unsigned integer type | Characteristic ID                                            |
  | chara_prop | Unsigned integer type | Characteristic properties. Hexadecimal number. You can specify several properties at the same time by OR operations.  <br>0x01 -Broadcast<br/>0x02 - Read<br/>0x04 - Write Without Response<br/>0x08 - Write<br/>0x10 - Notify<br/>0x20 - Indicate<br/>0x40 - Signed Write Command<br/>0x80 - Extended Properties |
  | uuid_type  | Unsigned integer type | uuid type<br/>0 - Long UUID, 128bit<br/>1 - Short UUID, 16bit |
  | uuid_s     | Unsigned integer type | Short UUID, 2 bytes (16bit)                                  |
  | uuid_l     | Array                 | Long UUID, 16 bytes (128bit)                                 |

* Return Value：

  0	 Successful execution

  -1	Failed execution

* Example：

```python
def ble_gatt_add_characteristic():
    server_id = 0x01
    chara_id = 0x01
    chara_prop = 0x02 | 0x10 | 0x20  # 0x02-read 0x10-notify 0x20-indicate
    uuid_type = 1  # short UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_characteristic failed.')
        return -1
    print('ble_gatt_add_characteristic success.')
    return 0
```



##### Add a Characteristic Value

> **ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)**

* Function:

  Add a characteristic value for a characteristic.

* Parameter:

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | server_id  | Unsigned integer type | Service ID, which determines a service                       |
  | chara_id   | Unsigned integer type | Characteristic ID                                            |
  | permission | Unsigned integer type | Permission of characteristic value. 2 bytes. Hexadecimal number. You can specify several properties at the same time by OR operations.  <br/><br/>0x0001 - Readable<br/>0x0002 - Writable<br/>0x0004 - Read requires authentication<br/>0x0008 - Read requires authorization<br/>0x0010 - Read requires encryption<br/>0x0020 - Read requires authorization and authentication<br/>0x0040 - Write requires authentication<br/>0x0080 - Write requires authorization<br/>0x0100 - Write requires encryption<br/>0x0200 - Write requires authorization and authentication |
  | uuid_type  | Unsigned integer type | uuid type<br/>0 - Long UUID, 128bit<br/>1 - Short UUID, 16bit |
  | uuid_s     | Unsigned integer type | Short UUID, 2 bytes (16bit)                                  |
  | uuid_l     | Array                 | Long UUID, 16 bytes (128bit)                                 |
  | value      | Array                 | Characteristic value                                         |

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example:

```python
def ble_gatt_add_characteristic_value():
    data = []
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # short UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    for i in range(0, 244):
        data.append(0x00)
    value = bytearray(data)
    ret = ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_value failed.')
        return -1
    print('ble_gatt_add_characteristic_value success.')
    return 0
```



##### Add a Characteristic Descriptor

> **ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)**

* Function:

  Add a characteristic descriptor for a characteristic. The characteristic descriptor and characteristic value belong to the same characteristic.

* Parameter:

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | server_id  | Unsigned integer type | Service ID, which determines a service                       |
  | chara_id   | Unsigned integer type | Characteristic ID                                            |
  | permission | Unsigned integer type | Permission of characteristic value. 2 bytes. Hexadecimal number. You can specify several properties at the same time by OR operations.<br/>0x0001 - Readable<br/>0x0002 - Writable<br/>0x0004 - Read requires authentication<br/>0x0008 - Read requires authorization<br/>0x0010 - Read requires encryption<br/>0x0020 - Read requires authorization and authentication<br/>0x0040 - Write requires authentication<br/>0x0080 - Write requires authorization<br/>0x0100 - Write requires encryption<br/>0x0200 - Write requires authorization and authentication |
  | uuid_type  | Unsigned integer type | uuid type<br/>0 - Long UUID, 128bit<br/>1 - Short UUID, 16bit |
  | uuid_s     | Unsigned integer type | Short UUID, 2 bytes (16bit)                                  |
  | uuid_l     | Array                 | Long UUID, 16 bytes (128bit)                                 |
  | value      | Array                 | Characteristic descriptor value                              |

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example:

```python
def ble_gatt_add_characteristic_desc():
    data = [0x00, 0x00, 0x00, 0x00]
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # short UUID
    uuid_s = 0x2902
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    value = bytearray(data)
    ret = ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_desc failed.')
        return -1
    print('ble_gatt_add_characteristic_desc success.')
    return 0
```



##### Complete Addition of Services or Clear the Added Services

> **ble.addOrClearService(option, mode)**

* Function:

  Complete the addition of services or clear the added services.

* Parameter:

  | Parameter | Type                  | Description                                                  |
  | --------- | --------------------- | ------------------------------------------------------------ |
  | option    | Unsigned integer type | Operation type.<br>0 - Clear the services<br/>1 - Complete the addition of services |
  | mode      | Unsigned integer type | Retention mode of system service.<br/>0 - Delete the default system GAP and GATT services<br/>1 - Retain the default system GAP and GATT services |

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example:

```python
See comprehensive example
```



##### Send Notification

> **ble.sendNotification(connect_id, attr_handle, value)**

* Function:

  Send notification.

* Parameter:

  | Parameter   | Type                  | Description                                       |
  | ----------- | --------------------- | ------------------------------------------------- |
  | connect_id  | Unsigned integer type | Connection ID                                     |
  | attr_handle | Unsigned integer type | Attribute handle                                  |
  | value       | Array                 | Data to be sent. Do not send data longer than MTU |

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example:

```python
See comprehensive example
```



##### Send Indication

> **ble.sendIndication(connect_id, attr_handle, value)**

* Function:

  Send indication.

* Parameter:

  | Parameter   | Type                  | Description                                       |
  | ----------- | --------------------- | ------------------------------------------------- |
  | connect_id  | Unsigned integer type | Connection ID                                     |
  | attr_handle | Unsigned integer type | Attribute handle                                  |
  | value       | Array                 | Data to be sent. Do not send data longer than MTU |

* Return Value:

  0	 Successful execution

  -1	Failed execution

* Example:

```python
See comprehensive example
```



##### Start Advertising

> **ble.advStart()**

* Function:

  Start advertising.

* Parameter:

  None

* Return Value:

  0	 Successful execution

  -1	Failed execution




##### Stop Advertising

> **ble.advStop()**

Function:

Stop advertising.

Parameter:

None

Return Value:

0	 Successful execution

-1	Failed execution



##### Comprehensive Example:

```python
# -*- coding: UTF-8 -*-

import ble
import utime


BLE_GATT_SYS_SERVICE = 0  # 0-delete the default system GAP and GATT services  1-retain the default system GAP and GATT services
BLE_SERVER_HANDLE = 0
_BLE_NAME = "Quectel_ble_test"
# _BLE_NAME = "bluetooth_ble"


def ble_callback(args):
    global BLE_GATT_SYS_SERVICE
    global BLE_SERVER_HANDLE
    event_id = args[0]
    status = args[1]
    print('[ble_callback]: event_id={}, status={}'.format(event_id, status))

    if event_id == 0:  # ble start
        if status == 0:
            print('[callback] BLE start success.')
            ret = ble_gatt_set_name()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_set_param()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_set_data()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_set_rsp_data()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_service()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_characteristic()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_characteristic_value()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_characteristic_desc()
            if ret != 0:
                ble_gatt_close()
                return
            ret = ble_gatt_add_service_complete()
            if ret != 0:
                ble_gatt_close()
                return
            if BLE_GATT_SYS_SERVICE == 0:
                BLE_SERVER_HANDLE = 1
            else:
                BLE_SERVER_HANDLE = 16
            ret = ble_adv_start()
            if ret != 0:
                ble_gatt_close()
                return
        else:
            print('[callback] BLE start failed.')
    elif event_id == 1:  # ble stop
        if status == 0:
            print('[callback] ble stop successful.')
        else:
            print('[callback] ble stop failed.')
    elif event_id == 16:  # ble connect
        if status == 0:
            print('[callback] ble connect successful.')
            connect_id = args[2]
            ble_addr = args[3]
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, ble_addr))

            # utime.sleep(3)
            ret = ble_gatt_send_notification()
            if ret == 0:
                print('[callback] ble_gatt_send_notification successful.')
            else:
                print('[callback] ble_gatt_send_notification failed.')
                ble_gatt_close()
                return
        else:
            print('[callback] ble connect failed.')
    elif event_id == 17:  # ble disconnect
        if status == 0:
            print('[callback] ble disconnect successful.')
            connect_id = args[2]
            ble_addr = args[3]
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, ble_addr))
        else:
            print('[callback] ble disconnect failed.')
            ble_gatt_close()
            return
    elif event_id == 18:  # ble update connection parameter
        if status == 0:
            print('[callback] ble update parameter successful.')
            connect_id = args[2]
            max_interval = args[3]
            min_interval = args[4]
            latency = args[5]
            timeout = args[6]
            print('[callback] connect_id={},max_interval={},min_interval={},latency={},timeout={}'.format(connect_id, max_interval, min_interval, latency, timeout))
        else:
            print('[callback] ble update parameter failed.')
            ble_gatt_close()
            return
    elif event_id == 20:  # ble connection mtu
        if status == 0:
            print('[callback] ble connect mtu successful.')
            handle = args[2]
            ble_mtu = args[3]
            print('[callback] handle = {}, ble_mtu = {}'.format(handle, ble_mtu))
        else:
            print('[callback] ble connect mtu failed.')
            ble_gatt_close()
            return
    elif event_id == 21:  # server:when ble client write characteristic value or descriptor,server get the notice
        if status == 0:
            print('[callback] ble recv successful.')
            data_len = args[2]
            data = args[3]  # this is a bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # this is a bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {}'.format(attr_handle))
            print('short uuid = {}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv failed.')
            ble_gatt_close()
            return
    elif event_id == 22:  # server:when ble client read characteristic value or descriptor,server get the notice
        if status == 0:
            print('[callback] ble recv read successful.')
            data_len = args[2]
            data = args[3]  # this is a bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # this is a bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {}'.format(attr_handle))
            print('short uuid = {}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv read failed.')
            ble_gatt_close()
            return
    elif event_id == 25:  # server send notification,and recieve send end notice
        if status == 0:
            print('[callback] ble send data successful.')
        else:
            print('[callback] ble send data failed.')
    else:
        print('unknown event id.')


def ble_gatt_server_init(cb):
    ret = ble.serverInit(cb)
    if ret != 0:
        print('ble_gatt_server_init failed.')
        return -1
    print('ble_gatt_server_init success.')
    return 0


def ble_gatt_server_release():
    ret = ble.serverRelease()
    if ret != 0:
        print('ble_gatt_server_release failed.')
        return -1
    print('ble_gatt_server_release success.')
    return 0


def ble_gatt_open():
    ret = ble.gattStart()
    if ret != 0:
        print('ble_gatt_open failed.')
        return -1
    print('ble_gatt_open success.')
    return 0


def ble_gatt_close():
    ret = ble.gattStop()
    if ret != 0:
        print('ble_gatt_close failed.')
        return -1
    print('ble_gatt_close success.')
    return 0


def ble_gatt_set_name():
    code = 0  # utf8
    name = _BLE_NAME
    ret = ble.setLocalName(code, name)
    if ret != 0:
        print('ble_gatt_set_name failed.')
        return -1
    print('ble_gatt_set_name success.')
    return 0


def ble_gatt_set_param():
    min_adv = 0x300
    max_adv = 0x320
    adv_type = 0  # CONNECTABLE UNDIRECTED, default 
    addr_type = 0  # public address
    channel = 0x07
    filter_strategy = 0  # process scan and connection requests from all devices
    discov_mode = 2
    no_br_edr = 1
    enable_adv = 1
    ret = ble.setAdvParam(min_adv, max_adv, adv_type, addr_type, channel, filter_strategy, discov_mode, no_br_edr, enable_adv)
    if ret != 0:
        print('ble_gatt_set_param failed.')
        return -1
    print('ble_gatt_set_param success.')
    return 0


def ble_gatt_set_data():
    adv_data = [0x02, 0x01, 0x05]
    ble_name = _BLE_NAME
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvData(data)
    if ret != 0:
        print('ble_gatt_set_data failed.')
        return -1
    print('ble_gatt_set_data success.')
    return 0


def ble_gatt_set_rsp_data():
    adv_data = []
    ble_name = _BLE_NAME
    length = len(ble_name) + 1
    adv_data.append(length)
    adv_data.append(0x09)
    name_encode = ble_name.encode('UTF-8')
    for i in range(0, len(name_encode)):
        adv_data.append(name_encode[i])
    print('set adv_rsp_data:{}'.format(adv_data))
    data = bytearray(adv_data)
    ret = ble.setAdvRspData(data)
    if ret != 0:
        print('ble_gatt_set_rsp_data failed.')
        return -1
    print('ble_gatt_set_rsp_data success.')
    return 0


def ble_gatt_add_service():
    primary = 1
    server_id = 0x01
    uuid_type = 1  # short UUID
    uuid_s = 0x180F
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_service failed.')
        return -1
    print('ble_gatt_add_service success.')
    return 0


def ble_gatt_add_characteristic():
    server_id = 0x01
    chara_id = 0x01
    chara_prop = 0x02 | 0x10 | 0x20  # 0x02-read 0x10-notify 0x20-indicate
    uuid_type = 1  # short UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    ret = ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)
    if ret != 0:
        print('ble_gatt_add_characteristic failed.')
        return -1
    print('ble_gatt_add_characteristic success.')
    return 0


def ble_gatt_add_characteristic_value():
    data = []
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # short UUID
    uuid_s = 0x2A19
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    for i in range(0, 244):
        data.append(0x00)
    value = bytearray(data)
    ret = ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_value failed.')
        return -1
    print('ble_gatt_add_characteristic_value success.')
    return 0


def ble_gatt_add_characteristic_desc():
    data = [0x00, 0x00, 0x00, 0x00]
    server_id = 0x01
    chara_id = 0x01
    permission = 0x0001 | 0x0002
    uuid_type = 1  # short UUID
    uuid_s = 0x2902
    uuid_l = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    value = bytearray(data)
    ret = ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)
    if ret != 0:
        print('ble_gatt_add_characteristic_desc failed.')
        return -1
    print('ble_gatt_add_characteristic_desc success.')
    return 0


def ble_gatt_send_notification():
    global BLE_SERVER_HANDLE
    data = [0x39, 0x39, 0x39, 0x39, 0x39]  # send any data
    conn_id = 0
    attr_handle = BLE_SERVER_HANDLE + 2
    value = bytearray(data)
    ret = ble.sendNotification(conn_id, attr_handle, value)
    if ret != 0:
        print('ble_gatt_send_notification failed.')
        return -1
    print('ble_gatt_send_notification success.')
    return 0


def ble_gatt_add_service_complete():
    global BLE_GATT_SYS_SERVICE
    ret = ble.addOrClearService(1, BLE_GATT_SYS_SERVICE)
    if ret != 0:
        print('ble_gatt_add_service_complete failed.')
        return -1
    print('ble_gatt_add_service_complete success.')
    return 0


def ble_gatt_clear_service_complete():
    global BLE_GATT_SYS_SERVICE
    ret = ble.addOrClearService(0, BLE_GATT_SYS_SERVICE)
    if ret != 0:
        print('ble_gatt_clear_service_complete failed.')
        return -1
    print('ble_gatt_clear_service_complete success.')
    return 0


def ble_adv_start():
    ret = ble.advStart()
    if ret != 0:
        print('ble_adv_start failed.')
        return -1
    print('ble_adv_start success.')
    return 0


def ble_adv_stop():
    ret = ble.advStop()
    if ret != 0:
        print('ble_adv_stop failed.')
        return -1
    print('ble_adv_stop success.')
    return 0


def main():
    ret = ble_gatt_server_init(ble_callback)
    if ret == 0:
        ret = ble_gatt_open()
        if ret != 0:
            return -1
    else:
        return -1
    count = 0
    while 1:
        utime.sleep(1)
        count += 1
        if count % 5 == 0:
            print('##### BLE running, count = {}......'.format(count))
        if count > 120:
            count = 0
            print('!!!!! stop BLE now !!!!!')
            ble_gatt_close()
            ble_gatt_server_release()
            break


if __name__ == '__main__':
    main()

```



#### camera - Camera and Code Scan 

Module function: Preview, camera, video recorder, code scan (currently only preview and code scan are supported.)
Note: The BC25PA platform does not support this module function.


##### Preview

Before using the preview, you need to initialize LCD.

###### Create Preview Object

> **import camera**
> **preview = camera.camPreview(model,cam_w,cam_h,lcd_w,lcd_h,perview_level)**

* Parameter

| Parameter     | Type | Description                                                  |
| ------------- | ---- | ------------------------------------------------------------ |
| model         | int  | camera model:<br />*0: gc032a spi*<br />*1: bf3901 spi*      |
| cam_w         | int  | *camera Horizontal resolution*                               |
| *cam_h*       | int  | *camera Vertical resolution*                                 |
| *lcd_w*       | int  | *LCD horizontal resolution*                                  |
| *lcd_h*       | int  | *LCD vertical resolution*                                    |
| perview_level | int  | Preview level[1,2]. The higher the level, the smoother the image and the greater the consumption of resources. |

* Return Value

*-1*: Initialization failure.

If the object is returned, it means the creation is successful.

* Example

```python
>>> import camera
>>> preview = camera.camPreview(0,640,480,176,220,1)
```



###### Turn on Preview

**camPreview.open()**

* Parameter

None.

* Return Value

0: Successful execution.

Other values: Failed execution.



Turn off Preview

**camPreview.close()**

Turns off the preview.

* Parameter

None.

* Return Value

0: Successful execution.

Other values: Failed execution.



##### Code Scan

Before using  code scan , you need to initialize LCD.

###### Create an Object

**import camera**
**scan= camera.camScandecode(model,decode_level,cam_w,cam_h,perview_level,lcd_w,lcd_h)**

* Parameter

| Parameter     | Type | Description                                                  |
| ------------- | ---- | ------------------------------------------------------------ |
| model         | int  | camera model:<br />*0: gc032a spi*<br />*1: bf3901 spi*      |
| decode_level  | int  | code scan level，The higher the level, the better the recognition result but the greater the resource consumption* |
| cam_w         | int  | *camera horizontal resolution*                               |
| *cam_h*       | int  | *camera vertical resolution*                                 |
| perview_level | int  | Preview level[1,2]. The higher the level, the smoother the image and the greater the consumption of resources. |
| *lcd_w*       | int  | *LCD horizontal resolution*                                  |
| *lcd_h*       | int  | *LCD vertical resolution*                                    |

* Return Value

*-1*: Failed execution.

If the object is returned, it means the creation is successful.



###### Turn on Camera

**camScandecode.open()**

* Parameter

None.

* Return Value

0: Successful execution.

Other values: Failed execution.



###### Turn off Camera

**camScandecode.close()**

* Parameter

None.

* Return Value

0: Successful execution.

Other values: Failed execution.



###### Turn on Code Scan

**camScandecode.start()**

* Parameter

None.

* Return Value

0: Successful execution.

Other values: Failed execution.



###### Turn off Code Scan

**camScandecode.stop()**

* Parameter

None.

* Return Value

0: Successful execution.

Other values: Failed execution.



###### Pause Code Scan

**camScandecode.pause()**

* Parameter

None.

* Return Value

0: Successful execution.

Other values: Failed execution.



###### Resume Code Scan

* Return Value

0: Successful execution.

Other values: Failed execution.



###### Set Code Scan Callback

**camScandecode.callback(callback)**

* Parameter

| Parameter | Type | Description  |
| --------- | ---- | ------------ |
| callback  | api  | Callback API |

* Return Value

0: Successful execution.

Other values: Failed execution.

* Example

```python
def callback(para):
    print(para)		#para[0] code scan result 	0: success. Other values: failure.
    				#para[1] code scan content	
Scandecode.callback(callback) 
```



#### GNSS - Navigation Positioning and Timing

Module function: Get positioning data from GPS model of L76 module, including whether the module locates successfully, latitude, longitude, UTC time, positioning mode,  number of satellites, number of visible satellites, azimuth angle, speed over the ground, geodetic height and so on. 

Note: The BC25PA platform does not support this module function.

###### Turn on GNSS Port to Read and Parse GNSS Data

**gnss = GnssGetData(uartn,baudrate,databits,parity,stopbits,flowctl)**

**gnss.read_gnss_data()**

- Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| uartn     | int  | UARTn, Range: 0-3: <br />0-UART0 - DEBUG PORT<br />1-UART1 – BT PORT<br />2-UART2 – MAIN PORT<br />3-UART3 – USB CDC PORT |
| baudrate  | int  | Baud rate. The common baud rate, such as 4800, 9600, 19200, 38400, 57600, 115200, 230400 and so on, are supported. |
| databits  | int  | Data bit (5~8)                                               |
| parity    | int  | Parity (0 – NONE，1 – EVEN，2 - ODD)                         |
| stopbits  | int  | Stop bit (1~2)                                               |
| flowctl   | int  | Hardware flow control (0 – FC_NONE， 1 – FC_HW)              |



###### Get Whether the Positioning is Successful

**gnss.isFix()**

- Parameter

None.

- Return Value

1: Successful positioning 

0:  Positioning failure



###### Get UTC Time

**gnss.getUtcTime()**

- **Parameter**

None.

- **Return Value**

UTC Time



###### Get Positioning Mode

**gnss.getLocationMode()**

- **Parameter**

None.

- **Return Value**

| 0    | Unavailable or invalid positioning                  |
| ---- | --------------------------------------------------- |
| 1    | A valid positioning, positioning mode: GPS or SPS   |
| 2    | A valid positioning, positioning mode: DGPS or DSPS |



###### Get Number of Satellites

**gnss.getUsedSateCnt()**

- **Parameter**

None.

- **Return Value**

The number of satellites of GPS module.



###### Get Latitude and Longitude Information

**gnss.getLocation()**

- **Parameter**

None.

- **Return Value**

The latitude and longitude information of GPS module.



###### Get Number of Visible Satellites

**gnss.getViewedSateCnt()**

- **Parameter**

None.

- **Return Value**

The number of visible satellites of GPS module.



###### Get Azimuth Angle 

**gnss.getCourse()**

- **Parameter**

None.

- **Return Value**

Azimuth angle. Range: 0–359, based on true north.



###### Get Geodetic Height

**gnss.getGeodeticHeight()**

- **Parameter**

None.

- **Return Value**

Geodetic height. Unit: m.



###### Get  Speed Over the Ground

**gnss.getSpeed()**

- **Parameter**

None.

- **Return Value**

The speed over the ground of GPS module. Unit: KM/h.



- Example

```python
from machine import UART
from gnss import GnssGetData
import utime

if __name__ == '__main__':
    print("#### enter system main####")
    gnss=GnssGetData(1, 9600, 8, 0, 1, 0)
    while True:
        gnss.read_gnss_data()
        print(gnss.isFix())
        print(gnss.getUtcTime())
        print(gnss.getLocationMode())
        print(gnss.getUsedSateCnt())
        print(gnss.getLocation())
        print(gnss.getViewedSateCnt())
        print(gnss.getCourse())
        print(gnss.getGeodeticHeight())
        print(gnss.getSpeed())
        utime.sleep(3)
    
    
Results:
1
020031.000
1
16
(22.32905, 'N', 113.5597, 'E')
13
034
67.5
0.0
```



#### NB Internet of things cloud platform

Module function: it provides the function of connecting to the Internet of things cloud platform and connecting to the Internet of things cloud platform. Through the communication function of IOT cloud platform and module equipment, it currently supports China Telecom lot IOT platform, China Telecom AEP IOT platform and China Mobile onenet IOT platform.

Module name: nb(lowercase)

Support platform: BC25PA

Introduction: it includes three sub modules OC, AEP. The two sub modules all use lwm2m for data interaction.

##### OC

###### Create OC object

> **oc=OC(ip,port,psk)**

- **Parameter**

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| ip        | string | The server IP address of the Internet of things platform, with a maximum length of 16. |
| port      | string | Server port of Internet of things platform, maximum length 5. |
| psk       | string | PSK code module will be used for communication with dtls protocol (it is OK not to enter it now, but it cannot be empty). The maximum length is 64. |

- Example

```python
>>> from nb import OC
>>> oc=OC("180.101.147.115","5683","763c9692c6639541e1ddcd6769fc9e33")
```

###### Connect to OC cloud platform

> **oc.connect()**

- **Parameter**

None.

- **Return Value**

  Success - 0

  Failed - not 0

- Example

```python
>>> oc.connect()
0
```

###### Receive data

> **oc.recv(data_len,data)**

- **Parameter**

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| data_len  | int    | Expected accepted data length (note that this parameter is adjusted according to the actual length of data, and the minimum value is taken according to the comparison between the capacity of data variable and data_len) |
| data      | string | Store received data                                          |

- Note

The received data is a hexadecimal string, so the data length must be even.

- **Return Value**

Success - 0

Failed - not 0

- Example

```python
>>> oc.recv(6,data)
0
```

###### Send data

> **oc.send(data_len,data,type)**

- **Parameter**

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| data_len  | int    | Expected Send data length (note that this parameter is adjusted according to the actual length of data, and the minimum value is taken according to the comparison between the capacity of data variable and data_len) |
| data      | string | Data to be sent                                              |
| type      | int    | Sending method: 0, 1 and 2 do not need response confirmation, and 100, 101 and 102 need response confirmation. Only 0, 1 and 2 sending methods are supported temporarily. |

- Note

The sent data is a hexadecimal string, and the data length is even.

- **Return Value**

Success - 0

Failed - not 0

- Example

```python
>>> print(data)
bytearray(b'313233')
>>> oc.send(6,data,0)
0
```

###### Close connection

- **Parameter**

None

- **Return Value**

Success -True

Failed -False

- Example

```python
>>> oc.close()
True
```

##### AEP

###### Create AEP object

> **aep=AEP(ip,port)**

- **Parameter**

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| ip        | string | The server IP address of the Internet of things platform, with a maximum length of 16. |
| port      | string | Server port of Internet of things platform, maximum length 5. |

- Example

```python
>>> from nb import AEP
>>> aep=AEP("221.229.214.202","5683")
```

###### Connect to AEP cloud platform

> **aep.connect()**

- **Parameter**

None.

- **Return Value**

  Success - 0

  Failed - not 0

- Example

```python
>>> aep.connect()
0
```

###### Receive data

> **aep.recv(data_len,data)**

- **Parameter**

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| data_len  | int    | Expected accepted data length (note that this parameter is adjusted according to the actual length of data, and the minimum value is taken according to the comparison between the capacity of data variable and data_len) |
| data      | string | Store received data                                          |

- Note

The received data is a hexadecimal string, so the data length must be even.

- **Return Value**

Success - 0

Failed - not 0

- Example

```python
>>> aep.recv(6,data)
0
```

###### Send data

> **aep.send(data_len,data,type)**

- **Parameter**

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| data_len  | int    | Expected Send data length (note that this parameter is adjusted according to the actual length of data, and the minimum value is taken according to the comparison between the capacity of data variable and data_len) |
| data      | string | Data to be sent                                              |
| type      | int    | Sending method: 0, 1 and 2 do not need response confirmation, and 100, 101 and 102 need response confirmation. Only 0, 1 and 2 sending methods are supported temporarily. |

- Note

The sent data is a hexadecimal string, and the data length is even.

- **Return Value**

Success - 0

Failed - not 0

- Example

```python
>>> print(data)
bytearray(b'313233')
>>> aep.send(6,data,0)
0
```

###### Close connection

- **Parameter**

None

- **Return Value**

Success -True

Failed -False

- Example

```python
>>> aep.close()
True
```

##### 

###### 































