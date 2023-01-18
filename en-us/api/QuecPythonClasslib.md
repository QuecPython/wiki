#### example -Python Script Execution

Function: Provides the method to execute Python script  from command line.

> example.exec(filePath)

This function specifies the Python script to be executed. 

* Parameter

| Parameter | Type   | Description                                            |
| --------- | ------ | ------------------------------------------------------ |
| filePath  | string | The absolute path of the python script to be executed. |

* Return Value

  * NA

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



#### dataCall - Activate PDP Context

Function: Provides functions for activating the PDP Context.

##### Activate PDP Context

> **dataCall.start(profileIdx, ipType, apn, username, password, authType)**

Call this API to activating the PDP Context.

* Parameter

| Parameter  | Type   | Description                                                  |
| ---------- | ------ | ------------------------------------------------------------ |
| profileIdx | int    | PDP context index. Range: 1 - 8 [volte version with the largest default PID is used to register IMS, please do not repeat the operation]. It is generally set to 1, if set as 2 - 8, the private APN and password may be required. |
| ipType     | int    | IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6.                    |
| apn        | string | Optional. APN name. The maximum length is 63 bytes. (The maximum length is 64 bytes in EC200U/EC200A) |
| username   | string | Optional. APN user name.  The maximum length is 15 bytes.(The maximum length is 64 bytes in EC200U/EC200A) |
| password   | string | Optional. APN password. The maximum length is 15 bytes.(The maximum length is 64 bytes in EC200U/EC200A) |
| authType   | int    | Authentication type. 0-No authentication, 1-PAP, 2-CHAP, 3-PAP AND CHAP(just for CAT-M platform).|

* Return Value

  * Returns 0 on success, -1 otherwise.

* Note

  * The BC25PA platform does not support this method.

* Example

```python
>>> import dataCall
>>> dataCall.start(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
0
```



##### Use the APN in dictionary or json file to Activate PDP Context

> **dataCall.startByUserApns(apn_dict=None, filename=None)**

The user can save multiple APN information in a dictionary or JSON file and then call this interface to activating the PDP Context. And specify by parameter where to get APN information for PDP activation. If PDP activation fails using the first APN information obtained, other APN information set by the user will be used to continue activating the PDP Context.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| apn_dict  | dict   | A dict that stores user APN information. Note the format requirements. For details, see an example. |
| filename  | string | Json file name with file path. The file is used to store user APN information. For details, see the example. The path must start with "/usr/", such as "/usr/xxx.json" in the usr directory. |

* Return Value

  Returns a tuple containing two elements of the form:

  `(stagecode, subcode)`

  Returns (3,1) on success and 0 on failure, Other returned values are described as follows:


| Return Value | type | Description                                                  |
| ------------ | ---- | ------------------------------------------------------------ |
| stagecode    | int  | Stage code, indicates the stage of the dialing.<br>1 - In the stage of obtaining SIM card status, the program returns the value when SIM card status is abnormal;<br>2 - The value returned when the program failed to obtain the network state or failed to obtain the network state in the stage of obtaining network state;<br>3 - The value returned by the program during the dialing;<br>Stagecode should normally return 3 when used by the user. The first two values are abnormal. |
| subcode      | int  | Subcode，it is combined with the value of stagecode  to represent the specific state of dialing in different stages.<br/>When stagecode = 1:<br/>subcode indicates the state of the SIM card, range: [0, 21], for the description of each value, refer to the return value in sim.getStatus():[https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=sim-sim-card](https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=sim-sim-card) <br/><br/>Subcode，it is combined with the value of stagecode  to represent the specific state of dialing in different stages.<br/>When stagecode = 1:<br/>subcode indicates the state of the SIM card, range: [0, 21], for the description of each value, refer to the return value in sim.getStatus():[https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=sim-sim-card](https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=sim-sim-card) <br/><br/>When stagecode = 2:<br/>subcode indicates the state of the network registration, range: [0, 11], for the description of each values, refer to the return value in net.getState():[https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=net-network](https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=net-network) <br/>Subcode = -1: indicates that the network status fails to be obtained.<br/>For other value, see the above link.<br/><br>When stagecode = 3 :<br/>subcode = -1: Indicates that all user APN attempts are made to dial up, but all attempts fail.<br>subcode = 0: Indicates that the module successfully dials before using the user APN. In this case, the following three situations may occur:<br>（1）The user does not disable the default automatic dialing function upon startup.<br>（2）The user successfully calls the dialing interface after starting the machine.<br/>（3）After startup, the user has executed the startByUserApns() interface and dialed successfully, and then executed the interface again.<br>subcode = 1: Dialing succeeded. |

* Note

  The user APN can be saved in the dictionary built-in code, or can be saved in json file, the following describes the format of APN information:

  1. A description of the format for saving APN information in the dict

  （1）It must be in dictionary format, even if there is only APN information, it must be in the following format:

  {"key":  {"profileIdx": x, "ipType": x, "apn": "xxx", "username": "xxx", "password": "xxx", "authType": x}}

  （2）profileIdx, ipType, apn, username, password, and authType are required for each APN message, refer to the parameter description of the datacall.start () interface;

  （3）Since the dictionary is an unordered structure, the APN information is not taken out first which APN is written before, which is random.

* Example：

  ```python
  apn_infos = {
      "1": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "111111-apn", 
          "username": "111111-user", 
          "password": "111111-pwd", 
          "authType": 0
      },
      "2": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "222222-apn", 
          "username": "222222-user", 
          "password": "222222-pwd", 
          "authType": 0
      },
      "3": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "333333-apn", 
          "username": "333333-user", 
          "password": "333333-pwd", 
          "authType": 0
      }
  }
  
  ```

  2. A description of the format for saving APN information in a json file 

  （1）It must be in dictionary format, even if there is only APN information, it must be in the following format:

  {"key":  {"profileIdx": x, "ipType": x, "apn": "xxx", "username": "xxx", "password": "xxx", "authType": x}}

  （2）profileIdx, ipType, apn, username, password, and authType are required for each APN message, refer to the parameter description of the datacall.start () interface;

  ```json
  {
      "1": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "111111-apn", 
          "username": "111111-user", 
          "password": "111111-pwd", 
          "authType": 0
      },
      "2": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "222222-apn", 
          "username": "222222-user", 
          "password": "222222-pwd", 
          "authType": 0
      },
      "3": {
          "profileIdx": 1, 
          "ipType": 0, 
          "apn": "333333-apn", 
          "username": "333333-user", 
          "password": "333333-pwd", 
          "authType": 0
      }
  }
  ```

  3. You can select only one of the two saving modes for APN information based on user requirements;

  4. This interface is used to replace the default dial-up function upon startup. If you choose to use this interface, you need to run this interface in the user script first. After this interface returns a success message, the dial-up networking is successful, and then perform other network services.

* Example

```python
import dataCall


PROJECT_NAME = "QuecPython_DataCall_example"
PROJECT_VERSION = "1.0.0"


"""
Method 1: Save APN information in code
"""
apn_infos = {
    "1": {
        "profileIdx": 1,
        "ipType": 0,
        "apn": "111111",
        "username": "111111",
        "password": "111111",
        "authType": 0
    },
    "2": {
        "profileIdx": 1,
        "ipType": 0,
        "apn": "222222",
        "username": "222222",
        "password": "222222",
        "authType": 0
    },
    "3": {
        "profileIdx": 1,
        "ipType": 0,
        "apn": "333333",
        "username": "333333",
        "password": "333333",
        "authType": 0
    }
}

if __name__ == '__main__':
    stagecode, subcode = dataCall.startByUserApns(apn_dict=apn_infos)
    if stagecode == 3:
        if subcode == 1:
            print('Dialing has been successful')
        elif subcode == 0:
            print('Check whether automatic dialing on startup is disabled or the interface is invoked for the first time  ')
        else:
            print('All APNs have been tried and dial-up failed')
    elif stagecode == 1:
        if subcode == 0:
            print('Check whether a SIM card is inserted or whether the card slot is loose')
        else:
            print('The SIM card status is abnormal (status value: {}). Check whether the SIM card is in arrears'.format(subcode))
    else:
        if subcode == -1:
            print('Failed to get the network status')
        else:
            print('The status of network register is abnormal, status :{}'.format(subcode))

# =======================================================================================
"""
Method 2: Save APN information in a JSON file
"""
apn_file_path = '/usr/apns.json'

if __name__ == '__main__':
    stagecode, subcode = dataCall.startByUserApns(filename=apn_file_path)
    if stagecode == 3:
        if subcode == 1:
            print('Dialing has been successful')
        elif subcode == 0:
            print('Check whether automatic dialing on startup is disabled or the interface is invoked for the first time  ')
        else:
            print('All APNs have been tried and dial-up failed')
    elif stagecode == 1:
        if subcode == 0:
            print('Check whether a SIM card is inserted or whether the card slot is loose')
        else:
            print('The SIM card status is abnormal (status value: {}). Check whether the SIM card is in arrears'.format(subcode))
    else:
        if subcode == -1:
            print('Failed to get the network status')
        else:
            print('The status of network register is abnormal, status :{}'.format(subcode))
```



##### Enable the function of automatically activating the PDP context 

> **dataCall.poweronAutoDatacall(enable)**

Enable the function of automatically activating the PDP context upon startup, take effect after restart. It is enabled by default.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| enable    | int  | 0 - disable the function of automatically activating the PDP context<br>1 - enable the function of automatically activating the PDP context |

* Return Value

  * None

* Note

  This interface is only applicable to development and debugging, because it takes effect only after being reset. If the user wants to disable the function of automatically activating the PDP context when the module is in mass production, user can take the following steps:

  step 1: Create a file called system_config.json on your computer.

  step 2: Copy the following content to the  system_config.json file and save it.  

  ```json
  {"replFlag": 0, "datacallFlag": 0}
  ```

* Parameter:

  ​	replFlag - Enable or disable REPL, Please refer to the official Wiki documentation for details——QuecPythonThirdlib.md——system - Set system;

  ​	datacallFlag - Enable or disable automatic dialing, 0-disable, 1-enable;

  step 3: Use QPYCom to merge the system_config.json file into the firmware, which must be in the module's usr directory, just like merging main.py;

  step 4: Download the firmware successfully merged in the previous step into the module. The module will automatically detect the configuration of the system_config.json file upon startup.



##### Set APN

> **dataCall.setApn(profileIdx, ipType, apn, username, password, authType, flag=0)**

After calling this interface, the user_apn.json will be created in the user partition to save the APN information. When the device is restarted, APN is preferentially obtained from this json file for PDP context activation.

* Parameter

| Parameter  | Type   | Description                                                  |
| ---------- | ------ | ------------------------------------------------------------ |
| profileIdx | int    | PDP context index. Range: 1-8. It is generally set to 1, if set as 2-8, the private APN and password may be required. |
| ipType     | int    | IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6.                    |
| apn        | string | Optional. APN name. The maximum length is 63 bytes.(The maximum length is 64 bytes in EC200U/EC200A) |
| username   | string | Optional. APN user name.  The maximum length is 15 bytes.(The maximum length is 64 bytes in EC200U/EC200A) |
| password   | string | Optional. APN password. The maximum length is 15 bytes.(The maximum length is 64 bytes in EC200U/EC200A) |
| authType   | int    | Authentication type. 0-No authentication, 1-PAP, 2-CHAP, 3-PAP AND CHAP(just for CAT-M platform).     |
| flag       | int    | This parameter is optional. The default value is 0, indicating that only a user_apn.json file is created to save user APN information. If the value is 1, the user_apn.json file is created to save user APN information, and the APN information is used for PDP context activation immediately. |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Note

  * The BC25PA platform does not support this method.

* Example

```python
>>> import dataCall
>>> dataCall.setApn(1, 0, "3gnet.mnc001.mcc460.gprs", "", "", 0)
0
```



##### Set DNS

> **dataCall.setDnsserver(profileIdx, sim_id, priDns, secDns)**

Manually modify DNS information, you can check whether the modification is successful through `dataCall.getInfo(profileIdx, ipType)`. The device uses the DNS information delivered by the base station by default. 

* Parameter

| Parameter  | Type   | Description                                                  |
| ---------- | ------ | ------------------------------------------------------------ |
| profileIdx | int    | PPDP context index. Range: 1-8 [volte version with the largest default PID is used to register IMS, please do not repeat the operation]. It is generally set to 1, if set as 2-8, the private APN and password may be required. |
| sim_id     | int    | simid, range：0/1, default 0，only SIM0 is supported now。   |
| priDns     | string | Primary DNS                                                  |
| secDns     | string | Secondary DNS                                                |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Note

  * Currently only EC600S/EC600N/EC800N/EC200U/EC600U platform support this feature.

* Example

```python
>>> import dataCall
>>> dataCall.setDnsserver(1, 0, "8.8.8.8", "114.114.114.114")
0
```



##### Get APN

> **dataCall.getApn(simid, profileIdx)**

Get APN Information of user. If only simID is specified, the default APN is obtained. If profileIdx is specified, the APN corresponding to profileIdx is obtained.

* Parameter

| Parameter  | Type | Description                                                     |
| ---------- | -------- | ------------------------------------------------------------ |
| simid      | int      | simid, range：0/1；only SIM0 is supported now. |
| profileIdx | int      | PDP context index. Range for ASR : 1-8,range for unisoc : 1-7 |

* Return Value

  * Returns APN on success, integer -1 on failure.

* Note

  * The unisoc and ASR platform support this method.

* Example

```python
>>> import dataCall
>>> dataCall.getApn(0)
'cmnet'

>>> dataCall.getApn(0,2)
'hhhnet'
```



##### Register Callback Function

> **dataCall.setCallback(usrFun)**

This function registers the callback function to send the notification when the network state is changed, such as the network disconnection or connection.

* Parameter

| Parameter | Type     | Description                                     |
| --------- | -------- | ----------------------------------------------- |
| usrFun    | function | Callback function. See example for more details |

* Return Value

  * 0  Successful execution.
  * -1  Failed execution.

* Note

  * The BC25PA platform does not support this method.
  
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



##### Get IP and DNS Information

> **dataCall.getInfo(profileIdx, ipType)**

This API is used to get PDP activation status, IP, and DNS information.

* Parameter

| Parameter  | Type | Description                               |
| ---------- | ---- | ----------------------------------------- |
| profileIdx | int  | PDP context index. Range: 1-8             |
| ipType     | int  | IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6. |

* Return Value

  * If it failed to obtain the dial-up information, returns -1. If successfully, the dial-up information is returned  in the format shown as follows.

  * If ipType =0, the format of the return value is as follows.

    `(profileIdx, ipType, [nwState, reconnect, ipv4Addr, priDns, secDns])`<br/>
    `profileIdx`：PDP context index. Range: 1-8<br/>
    `ipType`：IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6.<br/>
    `nwState`： The result of dial-up. 0 indicates the failed dial-up. 1 indicates the successful dial-up.<br/>
    `reconnect`：The reconnection flag.<br/>
    `ipv4Addr`：IPv4 address, string type.<br/>
    `priDns`：Primary DNS, string type.<br/>
    `secDns`：Secondary DNS, string type.

  * If ipType =1, the format of the return value is as follows.

    `(profileIdx, ipType, [nwState, reconnect, ipv6Addr, priDns, secDns])`<br/>
    `profileIdx`：PDP context index. Range: 1-8<br/>
    `ipType`：IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6.<br/>
    `nwState`：The result of dial-up. 0 indicates the failed dial-up. 1 indicates the successful dial-up.<br/>
    `reconnect`：The reconnection flag.<br/>
    `ipv6Addr`：IPv6 address, string type.<br/>
    `priDns`：Primary DNS, string type.<br/>
    `secDns`：Secondary DNS, string type.

  * If ipType =2, the format of the return value is as follows.

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



#### cellLocator - Cell Tower Locator

Function: Provides Cell Tower Locator function to obtain coordinate information.

Note: the current only  EC600S EC600N/EC800N EC200U/EC600U platform support this function.

##### Obtain Coordinate Information

> **cellLocator.getLocation(serverAddr, port, token, timeout, profileIdx)**

This function obtains coordinate information of the base station.

* Parameter

| Parameter  | Type   | Description                                                  |
| ---------- | ------ | ------------------------------------------------------------ |
| serverAddr | string | Server domain name, the length must be less than 255 bytes, currently only supports “www.queclocator.com” |
| port       | int    | Server port, currently only supports port 80                 |
| token      | string | Token, composed of 16 characters                             |
| timeout    | int    | Timeout. Range: 1-300. Default value: 300. Unit: s.          |
| profileIdx | int    | PDP context index. Range for ASR : 1-8, range for unisoc : 1-7 |

* Return Value

  * If obtain the coordinate information successfully, return the information in the format of：`(longtitude, latitude, accuracy)`，`(0.0, 0.0, 0)` indicates it failed to obtain the coordinate information. 

    `longtitude` : longtitude<br/>
    `latitude` : latitude<br/>
    `accuracy` : accuracy, Unit of m

  * The error code returned is explained as follows:

    -1 – Initialization failed<br/>
    -2 – Server address exceeds 255 bytes<br/>
    -3 – Token length error, it must be 16 bytes.<br/>
    -4 – Timeout is out of range.<br/>
    -5 – PDP error.<br/>
    -6 – Obtaining error.

* Example

```python
>>> import cellLocator
>>> cellLocator.getLocation("www.queclocator.com", 80, "xxxxxxxxxxxxxxxx", 8, 1)
(117.1138, 31.82279, 550)
# "xxxxxxxxxxxxxxxx"indicates the token. You need to apply for the token from the Quectel.
```



#### wifilocator - wifi locator

Function: Provides wifi locator function to obtain coordinate information.

Note: the current only  EC600S EC600N/EC800N EC200U/EC600U platform support this function.

##### Set token

> **wifilocator(token)**

Set the token required for WiFi location.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| token     | string | toekn, made up of 16 characters, you need to apply for this token. |

* Return Value

  * Return an object.



##### Obtain Coordinate Information

> **wifilocator.getwifilocator()**

Obtain Coordinate Information.

* Parameter

  * None

* Return Value

  * If obtain the coordinate information successfully, return the information in the format of：`(longtitude, latitude, accuracy)`，`(0.0, 0.0, 0)` indicates it failed to obtain the coordinate information. 

    `longtitude` : longtitude<br/>
    `latitude` : latitude<br/>
    `accuracy` : accuracy, Unit of m

  * The error code returned is explained as follows:

    -1 – Network exception<br/>
    -2 – Token length error, it must be 16 bytes<br/>
    -3 – Obtaining error

* Example

```python
>>> from wifilocator import wifilocator
>>> wifilocator = wifilocator("xxxxxxxxxxxxxxxx")
>>> wifilocator.getwifilocator()
(117.1152877807617, 31.82142066955567, 100)
# The token "XXXXXXXXXXXXXXXX" need to be applied to Quectel.
```



#### atcmd - AT

Function：send AT cmd.

#### send AT cmd

> **atcmd.sendSync(atcmd,resp,include_str,timeout)**

* Parameter

| Parameter | Type   | Description                                       |
|  ----   | -------- | --------------------------------------------- |
| atcmd   |  string  | AT cmd，must contain‘\r\n’              |
| resp    |  string  | output param       |
| include_str | string | include str                                      |
| timeout | int      | Timeout period, senconds                            |

* Return value

Return 0, or return [errorlist] if failed：

typedef enum HELIOS_AT_RESP_STATUS_ENUM{
	HELIOS_AT_RESP_OK = 0,
	HELIOS_AT_RESP_ERROR,
	HELIOS_AT_RESP_CME_ERROR,
	HELIOS_AT_RESP_CMS_ERROR,
	HELIOS_AT_RESP_INVALID_PARAM,
	HELIOS_AT_RESP_TIME_OUT,
	HELIOS_AT_RESP_SYS_ERROR,
}HELIOS_AT_RESP_STATUS_E;

* Example

```python
>>> import atcmd
>>> resp=bytearray(50)
>>> atcmd.sendSync('at+cpin?\r\n',resp,'',20)
0
>>> print(resp)
bytearray(b'\r\n+CPIN: READY\r\n\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

atcmd.sendSync('at+cpin\r\n',resp,'',20)
1
>>> print(resp)
bytearray(b'\r\nERROR\r\n\n
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
```



#### sim - SIM Card

Function: Provides SIM operations related APIs, such as querying SIM card status, ICCID, IMSI.

Note: The prerequisite for successfully obtaining IMSI, ICCID, and phone number is that the status of the SIM card is 1, which can be queried through sim.getStatus(). 

##### Send APDU command to SIM

> **sim.genericAccess(simId, cmd)**

Send APDU command to SIM card.

Note : Currently, only the ASR-1603 platform supports this function.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| simId     | int    | SIM card id, range : 0 or 1;only SIM0 is supported now       |
| cmd       | string | command passed on by the MT to the SIM in the format as described in GSM 51.011 |

* Return Value

  * The APDU of the response is returned on success, integer -1 on failure.

* Example

```python
>>> sim.genericAccess(0,'80F2000016')
(48, '623E8202782183027FF08410A0000000871002FF86FF9000')
>>>
```



##### Obtain IMSI

> **sim.getImsi()**

Call this API to get the IMSI of the SIM card.

* Parameter

  * None

* Return Value

  * Returns IMSI in string type, or returns -1 if failed.

* Example

```python
>>> import sim
>>> sim.getImsi()
'460105466870381'
```



##### Obtain ICCID

> **sim.getIccid()**

Call this API to get the ICCID of SIM card.

* Parameter

  * None

* Return Value

  * Returns ICCID in string type, or returns -1 if failed.

* Example

```python
>>> sim.getIccid()
'89860390845513443049'
```



##### Obtain the Phone Number

> **sim.getPhoneNumber()**

Call this API to get the phone number of SIM card.

* Parameter

  * None

* Return Value

  * Returns the phone number in string type, or returns -1 if failed.

* Note

  * The BC25PA platform does not support this method.

* Example

```python
>>> sim.getPhoneNumber()
'+8618166328752'
```



##### Obtain the Status of SIM Card

> **sim.getStatus()**

Call this API to get the Status of SIM Card.

* Parameter

  * None

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

Call this API to enables PIN authentication, and then you need to enter the correct PIN before the SIM card can be used normally. The SIM card will be locked if the wrong PIN is entered consecutive 3 times and then PUK is required to unlock the SIM card.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| pin       | string | PIN, ‘1234’ is the default, and the maximum length is 15 bytes. |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Note

  * The BC25PA platform pin password supports up to eight digits.

* Example

```python
>>> sim.enablePin("1234")
0
```



##### Disable PIN Authentication

> **sim.disablePin(pin)**

Call this API to disables PIN authentication

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| pin       | string | PIN, ‘1234’ is the default, and the maximum length is 15 bytes. |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Note

  * The BC25PA platform pin password supports up to eight digits.

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

  * Returns 0 on success, -1 otherwise.

* Note

  * The BC25PA platform pin password supports up to eight digits.

* Example

```python
>>> sim.verifyPin("1234")
0
```



##### Unlock SIM Card

> **sim.unblockPin(puk, newPin)**

This function unlocks the SIM card. When PIN/PIN2 code is wrongly input for times, PUK/PUK2 code and new PIN/PIN2 code are required to unlock the SIM card. If all PUK code input in 10 times are incorrect, SIM card will be permanently locked and automatically scrapped.

* Parameter

| Parameter | Type   | Description                                  |
| --------- | ------ | -------------------------------------------- |
| puk       | string | PUK, and the maximum length is 15 bytes.     |
| newPin    | string | New PIN, and the maximum length is 15 bytes. |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Note

  * The BC25PA platform pin password supports up to eight digits.

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

  * Returns 0 on success, -1 otherwise.

* Note

  * The BC25PA platform pin password supports up to eight digits.

* Example

```python
>>> sim.changePin("1234", "4321")
0
```



##### Read Phonebook

> **sim.readPhonebook(storage, start, end, username)**

Call this API to get one or more phone number records in the specified phonebook on the SIM card.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| storage   | int    | The phonebook storage location of the phone number record to be read. The optional parameters are as follows: <br/>0 – DC，1 – EN，2 – FD，3 – LD，4 – MC，5 – ME，6 – MT，7 – ON，<br/>8 – RC，9 – SM，10 – AP，11 – MBDN，12 – MN，13 – SDN，14 – ICI，15 - OCI |
| start     | int    | The start number of phone number record to be read. Starts from 0, indicates that get phone number record without the number. |
| end       | int    | The end number of phone  number record to be read. Must meet: end - start <= 20 |
| username  | string | Only valid when start =0. The username in the phone number, and the maximum length is 30 bytes.<br/> |

* Return Value

  * If it failed to read, return -1. If read successfully, the record will be returned in the format shown as follows.

  `(record_number, [(index, username, phone_number), ... , (index, username, phone_number)])`

* Description:

  * `record_number` – Integer type. The record number read out.
  * `index` – Integer type. The index position in the phonebook.
  * `username` – String type. User name.
  * `phone_number` – String type. Phone number.

* Note

  * The BC25PA platform does not support this method.

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

Call this API to writes a phone number record.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| storage   | int    | The phonebook storage location of the phone number record to be read. The optional parameters are as follows: <br/>0 – DC，1 – EN，2 – FD，3 – LD，4 – MC，5 – ME，6 – MT，7 – ON，<br/>8 – RC，9 – SM，10 – AP，11 – MBDN，12 – MN，13 – SDN，14 – ICI，15 - OCI |
| index     | int    | The index of phone number record to be written. Range: 1-500. |
| username  | string | The username in the phone number, and the maximum length is 30 bytes. |
| number    | string | The phone number, and the maximum length is 20 bytes.        |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Note

  * The BC25PA platform does not support this method.

* Example

```python
>>> sim.writePhonebook(9, 1, 'Tom', '18144786859')
0
```



##### Register Callback Function

> **sim.setCallback(usrFun)**

Call this API to registers the listening callback function.

(Only valid when the SIM card hot-plugging is enabled.)

* Parameter

| Parameter | Type     | Description                                                |
| --------- | -------- | ---------------------------------------------------------- |
| usrFun    | function | Listening callback function. See example for more details. |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Note

  * The BC25PA platform does not support this method.

* Example

```python
import sim

def cb(args):
    simstates = args
    print('sim states:{}'.format(simstates))
    
sim.setCallback(cb)
```



##### Enable or disable the SIM card hot plug function

> **sim.setSimDet(switch, triggerLevel)**

Call this API to enable or disable the SIM card hot swap function.

* Parameter

| Parameter    | Type | Description                                                  |
| ------------ | ---- | ------------------------------------------------------------ |
| switch       | int  | Enable/Disable SIM card hot-plugging. 0: Disable. 1: Enable. |
| triggerLevel | int  | High/low level (0/1).                                        |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Note

  * The BC25PA platform does not support this method.

* Example

```python
>>> sim.setSimDet(1, 0)
0
```



##### Obtain SIMdet

> **sim.getSimDet()**

This function obtains the SIM card hot-plugging related configuration.

* Parameter

  * None

* Return Value

  * If it failed to obtain, return -1. If the configuration is obtained successfully, a tuple will be returned in the format shown as follows.

  `(detenable, insertlevel)`

* Description：

  * `detenable` - Enable/Disable SIM card hot-plugging. 0: Disable. 1: Enable.
  * `insertlevel` – High/low level (0/1).

* Note

  * The BC25PA platform does not support this method.

* Example

```python
>>> sim.getSimDet()
(1, 0)
```



##### get the current simid

> **sim.getCurSimid()**

get the current simid.（just supported on the 1606 platform）

* Parameter

  * None

* Return Value

  * Returns the current simid, or returns -1 if failed.

* Example

```python
>>> sim.getCurSimid() //current simid is sim0
0
```



##### switchcard api

> **sim.switchCard(simid)**

switchcard api.（just supported on the 1606 platform）

* Parameter

  | Parameter    | Type | Description                                                  |
  | ------------ | ---- | ------------------------------------------------------------ |
  | simid        | int  | simid,  0:sim1  1:sim2                                       |

* Return Value

  * rerurn 0 if switchcard action is successful, else return -1;

* Example

```python
>>> sim.getCurSimid() //current simid is sim0
0
>>> sim.switchCard(1) //switchcard from sim0 to sim1
0
>>> sim.getCurSimid() //current simid is sim1
1
```



##### Register Callback Function for switchcard

> **sim.setSwitchcardCallback(usrFun)**

Call this API to registers the listening callback function.(just supported on the 1606 platform)

* Note

Not all switchcard failures are returned via callbacks:
1.  The target card does not exist or is abnormal
2.   The target card is the current card
In the preceding cases, the card switching interface directly returns -1 and does not enter the actual card switching process.   Therefore, the callback is not triggered

If the card switching condition is met, the card switching interface returns 0, and the underlying task is created to perform the card switching process.
If the card switching fails or succeeds, the system returns the result through callback

* Parameter

| Parameter | Type     | Description                                                |
| --------- | -------- | ---------------------------------------------------------- |
| usrFun    | function | Listening callback function. See example for more details. |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Example

```python
HELIOS_SIM_SWITCH_CURRSIM_PSDC_UP（switchcard succeeded：7）
HELIOS_SIM_SWITCH_ERROR（switchcard failed: 8）

typedef enum
{
	HELIOS_SIM_SWITCH_INIT = 0,
	HELIOS_SIM_SWITCH_START,
	HELIOS_SIM_SWITCH_PRESIM_PDP_DOWN,
	HELIOS_SIM_SWITCH_PRESIM_IMS_DOWN,
	HELIOS_SIM_SWITCH_PRESIM_PSDC_DOWN,
	HELIOS_SIM_SWITCH_CURRSIM_PDP_UP,
    HELIOS_SIM_SWITCH_PRESIM_IMS_UP,
	HELIOS_SIM_SWITCH_CURRSIM_PSDC_UP,
	HELIOS_SIM_SWITCH_ERROR
}HELIOS_SIM_SWITCH_STATE;

import sim

def cb(args):
    switchcard_state = args
    print('sim switchcard states:{}'.format(switchcard_state))
    
sim.setSwitchcardCallback(cb)
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

  * Returns 0 on success, -1 otherwise.

* Example

```python
>>> import voiceCall
>>> voiceCall.setAutoAnswer(5)
0
```



##### Call

> **voiceCall.callStart(phonenum)**

This function initiates a call.

* Parameter

| Parameter | Type   | Description       |
| --------- | ------ | ----------------- |
| phonenum  | string | The phone number. |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Example

```python
>>> voiceCall.callStart("13855169092")
0
```



##### Answer

> **voiceCall.callAnswer()**

This function answers a call.

* Parameter

  * None

* Return Value

  * Returns 0 on success, -1 otherwise.

* Example

```python
>>> voiceCall.callAnswer()
0
```



##### Hang up

> **voiceCall.callEnd()**

This function hangs up a call.

* Parameter

  * None

* Return Value

  * Returns 0 on success, -1 otherwise.

* Example

```python
>>> voiceCall.callEnd()
0
```



##### Set the automatic call hangup function

> **voiceCall.setAutoCancel(enable)**

Set the automatic call hangup function(Only supported on 1803s platform)。

* Parameter 

| Parameter | Type   | Description       |
| --------- | ------ | ------------------------------------------------------------ |
| enable    | int    | Enable or disable the automatic call hangup function. 1: on, 0: off            |

* Return Value

  Returns 0 on success, -1 otherwise.

* Example

```python
#Using the cell phone call UE, It does not automatically hang up by default
>>> voiceCall.getAutoCancelStatus()
0

#Set the automatic hang up function, call the UE with the mobile phone, the default automatic hang up
>>> voiceCall.setAutoCancel(1)
0
>>> voiceCall.getAutoCancelStatus()
1
```



##### To obtain the status is enable or not of automatic call hangup

> **voiceCall.getAutoCancelStatus()**

To obtain the status is enable or not of automatic call hangup(Only supported on 1803s platform)。

* Parameter 

none

* Return Value

  0:It does not automatically hang up by default
  1:default automatic hang up

* Example

```python
#Using the cell phone call UE, It does not automatically hang up by default
>>> voiceCall.getAutoCancelStatus()
0

#Set the automatic hang up function, call the UE with the mobile phone, the default automatic hang up
>>> voiceCall.setAutoCancel(1)
0
>>> voiceCall.getAutoCancelStatus()
1
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

  * Returns 0 on success, -1 otherwise.

* Example

```python
>>> voiceCall.startDtmf('A',100)
0
```



##### Enable DTMF identification

> **voiceCall.dtmfDetEnable(enable)**

Enable DTMF identification. It is disabled by default.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| enable    | int    | 1:Enable DTMF identification, 0:Disable DTMF identification  |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Example

See the example of 'voiceCall.dtmfSetCb()'



##### set the callback of DTMF identification

> **voiceCall.dtmfSetCb(cb)**

Set the callback of DTMF identification

* Parameter

| Parameter | Type     | Description                                                  |
| --------- | ------   | ------------------------------------------------------------ |
| cb        | function | callback function                                            |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Example

```
>>> def cb(args):
... print(args)
...
...
...
>>> voiceCall.dtmfSetCb(cb)
0
>>> voiceCall.dtmfDetEnable(1)
0

>>> voiceCall.callStart('13855169092')

0
>>>
1   //Press "1" on the phone, callback function will receive the pressed character "1".

8   //Press "8" on the phone

9   //Press "9" on the phone
```



##### Set FWmode

> **voiceCall.setFw(reason, fwmode, phonenum)**

Call Forwarding Number and Conditions Control.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| reason    | int    | Forwarding conditions/reasion: <br/>0 - Unconditional<br/>1 - Mobile busy<br/>2 - Not reply<br/>3 - Not reachable<br/>4 - All call forwarding (Refer to 3GPP TS 22.030)<br/>5 - All conditional call forwarding (Refer to 3GPP TS 22.030) |
| fwmode    | int    | Controls the call forwarding supplementary service:<br/>0 - Disable<br/>1 - Enable<br/>2 - Query status<br/>3 - Registration<br/>4 - Erasure |
| phonenum  | string | The targeted number for forwarding                           |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Example

  * None



##### Switch the voice output channel

> **voiceCall.setChannel(device)**

Set the voice output channel during a call. The default channel is handset.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| device    | int  | Output channel<br/>0 - handset<br/>1 - earphone<br/>2 - speaker |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Example

```python
>>> voiceCall.startRecord(0,2,'U:/test.amr')
0
```



##### Get Volume

> **voiceCall.getVolume()**

Get the current volume of the voice.

* Parameter

  * None

* Return Value

  * return volume of the voice.



##### Set Volume

> **voiceCall.setVolume(vol)**

Set the volume of the voice.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| vol       | int  | Volume. Range : 0–11. The higher the number, the higher the volume. |

* Return Value

  Returns 0 on success, -1 otherwise.




##### Enable automatic recording

> **voiceCall.setAutoRecord(enable, record_type, record_mode, filename)**

Enable automatic recording, it is disabled by default.

Note：The non-Volte version does not have this interface.

* Parameter

| Parameter   | Type   | Description                                                  |
| ----------- | ------ | ------------------------------------------------------------ |
| enable      | int    | enable switch, range:<br>0 - disable the automatic recording function<br/>1 - enable the automatic recording function |
| record_type | int    | Recording File Type, range:<br/>0 - AMR<br/>1 - WAV          |
| record_mode | int    | mode, range:<br/>0 - RX <br/>1 - TX<br/>2 - MIX              |
| filename    | string | file name.                                                   |

* Return Value

  * 0 : Successful execution.
  * -1 :Failed execution.
  * "NOT SUPPORT" :The interface is not supported.

* Example

```python
>>> voiceCall.setAutoRecord(1,0,2,'U:/test.amr')
0
```



##### Start recording

> **voiceCall.startRecord(record_type, record_mode, filename)**

Call this API to start recording.

Note：The non-Volte version does not have this interface.

* Parameter

| Parameter   | Type   | Description                                         |
| ----------- | ------ | --------------------------------------------------- |
| record_type | int    | Recording File Type, range:<br/>0 - AMR<br/>1 - WAV |
| record_mode | int    | mode, range:<br/>0 - RX<br/>1 - TX<br/>2 - MIX      |
| filename    | string | file name                                           |

* Return Value

  * 0 : Successful execution.
  * -1 : Failed execution.
  * "NOT SUPPORT" : The interface is not supported.






##### End Recording

> **voiceCall.stopRecord()**

End Current Recording.

Note : The non-Volte version does not have this interface.

* Parameter

  * None

* Return Value

  * 0 : Successful execution.
  * -1 : Failed execution.
  * "NOT SUPPORT" : The interface is not supported.

* Example

```python
>>> voiceCall.stopRecord()
0
```



##### Start Bitstream recording

> **voiceCall.startRecordStream(record_type, record_mode, record_cb)**

Start Bitstream recording.

Note : The non-Volte version does not have this interface.

* Parameter

| Parameter   | Type     | Description                                         |
| ----------- | -------- | --------------------------------------------------- |
| record_type | int      | Recording File Type, range:<br/>0 - AMR<br/>1 - WAV |
| record_mode | int      | mode, range:<br/>0 - RX<br/>1 - TX <br/>2 - MIX     |
| record_cb   | function | callback function                                   |

* Return Value

  * 0 : Successful execution.
  * -1 : Failed execution.
  * "NOT SUPPORT" : The interface is not supported.

* Example

The return value of the callback function is defined as follows
```
args[0]:stream data
args[1]:stream data len
args[2]:states

states values：
typedef enum
{
	HELIOS_VC_AUD_REC_ERROR = -1,
	HELIOS_VC_AUD_REC_START = 0,
	HELIOS_VC_AUD_REC_DATA,
	HELIOS_VC_AUD_REC_PAUSE,
	HELIOS_VC_AUD_REC_FINISHED,
	HELIOS_VC_AUD_REC_DISK_FULL,
}HELIOS_VC_AUD_REC_STATE;
```

```python
>>> import voiceCall
>>> import audio

>>> f=open('usr/mia.amr','w')

>>> def cb(para):
...     if(para[2] == 1):
...         read_buf = bytearray(para[1])
...         voiceCall.readRecordStream(read_buf,para[1])
...         f.write(read_buf,para[1])
...         del read_buf
...     elif(para[2] == 3):
...         f.close()
...         
...         
... 
>>> voiceCall.callStart('13855169092')
0
>>> voiceCall.startRecordStream(0,2,cb)
0
// Hang up the phone here (MO/MT hanging up can be done)
>>> uos.listdir('usr')
['system_config.json', 'mia.amr']
>>> aud=audio.Audio(0)
>>> aud.setVolume(11)
0
>>> aud.play(2,1,'U:/mia.amr')
0
```




##### Register Listening Callback Function

> **voiceCall.setCallback(usrFun))**

This function registers the listening callback function. This function will be triggered when answering/hanging up a call. 

* Parameter

| Parameter | Type     | Description                 |
| --------- | -------- | --------------------------- |
| usrFun    | function | Listening callback function |

* Return Value

  * Returns 0 on success, -1 otherwise.

* Event_id

```c
typedef enum
{
	HELIOS_VC_INIT_OK_IND = 1,
	HELIOS_VC_RING_IND,
	HELIOS_VC_CONNECT_IND,
	HELIOS_VC_NOCARRIER_IND,
	HELIOS_VC_ERROR_IND,
	HELIOS_VC_CCWA_IND,
	HELIOS_VC_DIALING_IND,
	HELIOS_VC_MO_FAILED_IND,
	HELIOS_VC_HOLDING_IND,
	
	HELIOS_VC_RING_VOLTE_IND = 10,
	HELIOS_VC_CONNECT_VOLTE_IND,
	HELIOS_VC_NOCARRIER_VOLTE_IND,
	HELIOS_VC_CCWA_VOLTE_IND,
	HELIOS_VC_DIALING_VOLTE_IND,
	HELIOS_VC_ALERTING_VOLTE_IND,
	HELIOS_VC_HOLDING_VOLTE_IND
}HELIOS_VC_EVENT_ID_E;
```

* Description of callback function parameter 

| event                      | Number of Parameter | Parameter Description                                        |
| -------------------------- | ------------------- | ------------------------------------------------------------ |
| 2, 3, 9                    | 3                   | args[0] : event id<br>args[1] : call id ( call identification number as described in 3GPP TS 22.030 subclause 4.5.5.1; this number can be used in +CHLD command operations )<br/>args[2] : phone number |
| 4                          | 3                   | args[0] : event id<br/>args[1] : call id ( call identification number as described in 3GPP TS 22.030 subclause 4.5.5.1; this number can be used in +CHLD command operations )<br/>args[2] : cause |
| 6                          | 5                   | args[0] : event id<br/>args[1] : call id ( call identification number as described in 3GPP TS 22.030 subclause 4.5.5.1; this number can be used in +CHLD command operations )<br/>args[2] : phone number<br/>args[3] : num type ( [129/145],129:Dialing string without international access code “+”,145:Dialing string includes international access code character “+” )<br/>args[4] : CLI status |
| 7                          | 1                   | args[0] : event id                                           |
| 8                          | 4                   | args[0] : event id<br/>args[1] : call id ( call identification number as described in 3GPP TS 22.030 subclause 4.5.5.1; this number can be used in +CHLD command operations )<br/>args[2] : cause<br/>args[3] : Indicates if in-band tones are available from network |
| 10, 11, 12, 13, 14, 15, 16 | 8                   | args[0] : event id<br/>args[1] : call id ( call identification number as described in 3GPP TS 22.030 subclause 4.5.5.1; this number can be used in +CHLD command operations )<br/>args[2] : dir(MO/MT)<br/>args[3] : state of the call<br>args[4] : type ( It's usually 0,  indicates the voice call service)<br/>args[5] : mpty ( Indicates whether the call is multi-party, 0 : call is not one of multiparty (conference) call parties, 1 : call is one of multiparty (conference) call parties )<br/>args[6] : phone number<br/>args[7] : num type ( [129/145], 129 : Dialing string without international access code “+”, 145 : Dialing string includes international access code character “+” ) |

* Example

```python
def voice_callback(args):
     if args[0] == 10:
         print('voicecall incoming call, PhoneNO.: ', args[6])
     elif args[0] == 11:
	     print('voicecall connected, PhoneNO.: ', args[6])
     elif args[0] == 12:
	     print('voicecall disconnect')
	 elif args[0] == 13:
	     print('voicecall is waiting, PhoneNO.: ', args[6])
     elif args[0] == 14:
         print('voicecall dialing, PhoneNO.: ', args[6])
     elif args[0] == 15:
	     print('voicecall alerting, PhoneNO.: ', args[6])
     elif args[0] == 16:
	     print('voicecall holding, PhoneNO.: ', args[6])
     
>>> voiceCall.setCallback(voice_callback)
0
>>> voiceCall.callStart('10086')
0
```



For firmware versions released before 2021-09-09, use the event and callback functions as follows:

* Event_id

```
#define QUEC_VOICE_CALL_INDICATION_BASE                          ((uint_32)(0x1000))
#define QUEC_VOLTE_INCOMING_CALL_IND                             ((uint_32)(0x0007 + QUEC_VOICE_CALL_INDICATION_BASE))
#define QUEC_VOLTE_CONNECT_CALL_IND                              ((uint_32)(0x0008 + QUEC_VOICE_CALL_INDICATION_BASE))
#define QUEC_VOLTE_DISCONNECT_CALL_IND                           ((uint_32)(0x0009 + QUEC_VOICE_CALL_INDICATION_BASE))
#define QUEC_VOLTE_WAITING_CALL_IND                              ((uint_32)(0x000A + QUEC_VOICE_CALL_INDICATION_BASE))
```

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
```



#### sms - SMS

Function: Provides SMS related APIs.
Note: The BC25PA and 600M platform does not support this module function.

##### Send the Message in TEXT Mode

> **sms.sendTextMsg(phoneNumber, msg, codeMode)**

This function sends the messages in TEXT mode(Empty SMS is not supported).

* Parameter

| Parameter   | Type   | Description                                                  |
| ----------- | ------ | ------------------------------------------------------------ |
| phoneNumber | string | The phone number, and the maximum length is 20 bytes.        |
| msg         | string | The message to be sent, and the maximum length is 140 bytes. |
| codeMode    | string | Character Set.<br/>'GSM' - GSM<br/>'UCS2' - UCS2<br/>Note：<br/>（1）GSM is only for sending English messages.<br/>（2）UCS2 can be used both for English and Chinese messages. |

* Return Value

  * 0  Successful execution.
  * -1  Failed execution.

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

This function sends the messages in PDU mode(Empty SMS is not supported).

* Parameter

| Parameter   | Type   | Description                                                  |
| ----------- | ------ | ------------------------------------------------------------ |
| phoneNumber | string | The phone number, and the maximum length is 20 bytes.        |
| msg         | string | The message to be sent, and the maximum length is 140 bytes. |
| codeMode    | string | Character Set.<br/>'GSM' - GSM<br/>'UCS2' - UCS2<br/>Note：<br/>（1）GSM is only for sending English messages.<br/>（2）UCS2 can be used both for English and Chinese messages. |

* Return Value

  * 0  Successful execution.
  * -1  Failed execution.

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
| index     | int  | The index of the short messages to be deleted                |

* Return Value

  * 0  Successful execution.
  * -1  Failed execution.

* Example

```python
>>> import sms
>>> sms.deleteMsg(0)
0
```



##### Preferred Message Storage

> **sms.setSaveLoc(mem1, mem2, mem3)**

This function selects the memory storages.

* Parameter

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| mem1      | string | Messages to be read and deleted from this memory storage：<br/>"SM" - SIM message storage.<br/>"ME" - Mobile equipment message storage.<br/>"MT" - Not supported currently. |
| mem2      | string | Messages will be written and sent to this memory storage：<br/>"SM" - SIM message storage<br/>"ME" - Mobile equipment message storage.<br/>"MT" - Not supported currently. |
| mem3      | string | Received messages will be placed in this memory storage：<br/>"SM" - SIM message storage<br/>"ME" - Mobile equipment message storage.<br/>"MT" - Not supported currently. |

* Return Value

  * 0  Successful execution.
  * -1  Failed execution.

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

  * None

* Return Value

  * If the information is obtained successfully, a tuple is returned in the following format:

    `([loc1, current_nums, max_nums],[loc2, current_nums, max_nums],[loc3, current_nums, max_nums])`

* Description：

  * `loc1` - The memory storage where the messages to be read and deleted stored in;
  * `loc2` - The memory storage where the messages twill be written and sent stored in;
  * `loc3` - The memory storage where the Received messages stored in;
  * `current_nums` - The current number of messages in the storage.
  * `max_nums` - The maximum number of messages can be stored in the storage.
  
  * -1  Failed execution.

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

  * None

* Return Value

  * The number of messages  Successful execution.
  * -1  Failed execution.

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

  * If successfully, returns the message content in string. If failed, returns -1.



##### Read Message in TEXT Mode

> **sms.searchTextMsg(index)**

This function reads messages in TEXT mode.

* Parameter

| Parameter | Type | Description                                       |
| --------- | ---- | ------------------------------------------------- |
| index     | int  | The index of the message to be read. Range:0 ~ MAX-1, MAX indicates the maximum number can be stored. |

* Return Value

  * If successfully, returns the message content in following format. If failed, returns -1.

  * Return format：(phoneNumber, msg, msgLen)

    `phoneNumber` ：Phone number.<br/>
    `msg` ：Message content<br/>
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

  * None

* Return Value

  * Returns the short message center number in string type if successfully, or returns -1 if failed.

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

  * 0  Successful execution.
  * -1  Failed execution.

* Example

  * None



##### Obtain the Length of PDU Messages

> **sms.getPduLength(pduMsg)**

This function obtains the length of the specified PDU messages.

- Parameter


| Parameter | Type   | Description |
| --------- | ------ | ----------- |
| pduMsg    | string | PDU message |

- Return Value

  * Returns the length of PDU message if successfully, or returns -1 if failed.

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

  * Returns the decoded PDU message in the following format if successfully, or returns -1 if failed.

  * Format：(phoneNumber, msg, time, msgLen)

    `phoneNumber` ：The phone number.<br/>
    `msg` ：Message content.<br/>
    `time` ：Time when the message was received.<br/>
    `msgLen` ：The length of the message.

- Example


```python
>>> import sms
>>>sms.decodePdu('0891683110305005F00405A10110F000081270319043442354516C76CA77ED4FE1FF1A00320030003200315E7496328303975E6CD596C68D445BA34F2067086D3B52A863D09192FF1A4E3B52A88FDC79BB975E6CD596C68D44FF0C5171540C5B8862A47F8E597D751F6D3B3002',20)
('10010', '公益短信：2021年防范非法集资宣传月活动提醒：主动远离非法集资，共同守护美好生活。', '2021-07-13 09:34:44', 118)
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

  * 0  Successful execution.
  * -1  Failed execution.

* Example

  The new architecture refers to example 1, and the old architecture refers to example 2

    * Example 1:

```python
import sms

def cb(args):
    index = args[1]
    storage = args[2]
    print('New message! storage:{},index:{}'.format(storage, index))
    
sms.setCallback(cb)
```

    * Example 2:

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

> **net.setApn(\*args)**

This function sets APN. After setting, you need to restart or switch to mode 0 and then mode 1 through the `net.setmodemFun (mode)` interface for the setting to take effect.

* Parameter

  This API is a variable parameter function in Qualcomm/ASR_1803s/ASR_1601/ASR_1606/Unisoc platform, and the number of parameters is 2 or 7. The number of parameters in other platforms is fixed at 7  ：
    The number of parameters is 2：net.setApn(apn, simid)
    The number of parameters is 7：net.setApn(pid, iptype, apn, usrname, password, authtype, simid)
  
| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| pid       | int    | PDP context index.                                           |
| iptype    | int    | IP type. 0-IPV4, 1-IPV6, 2-IPV4 and IPV6.                    |
| apn       | string | apn name, The maximum length is 63 bytes.                    |
| usrname   | string | user name, The maximum length is 63 bytes.                   |
| password  | string | password, The maximum length is 63 bytes.                    |
| authtype  | int    | Authentication type,0-No authentication, 1-PAP, 2-CHAP, 3-PAP AND CHAP(just for CATM Platform) |
| simid     | int    | simid,（only SIM0 is supported now）<br>0 : SIM card 1<br/>1 :  SIM card 2 |

* Return Value

  * 0  Successful execution
  * -1  Failed execution

* Note

  The BC25PA platform does not support this module function.

* Example

```python
>>> net.setApn('3gnet',0)
0
>>> net.setApn(1,1,'3gnet','mia','123',2,0)
0  
```



##### Obtain the Current  APN

> **net.getApn(\*args)**

This function obtains the current APN.

* Parameter

  This API is a variable parameter function in Qualcomm/ASR_1803s/ASR_1601/ASR_1606/Unisoc platform, and the number of parameters is 1 or 2. The number of parameters in other platforms is fixed at 2  ：
    The number of parameters is 2：net.setApn(pid, simid)
    The number of parameters is 1：net.setApn(simid)
  
| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| pid       | int  | PDP context index.                                           |
| simid     | int  | simid, (only SIM0 is supported now)<br>0 : SIM card 1<br/>1 :  SIM card 2 |

* Return Value

  The number of parameters is 2:
    * pdp context: Successful execution
	* -1  Failed execution
    The number of parameters is 1:
    * apn info: Successful execution
    * -1  Failed execution

* Note

  * The BC25PA platform does not support this module function.

* Example

```python
>>> net.getApn(0)
'3gnet'
>>> net.getApn(1,0)
(1, '3gnet', 'mia', '123', 2)
```

  

##### Obtain CSQ

> **net.csqQueryPoll()**

This function obtains CSQ.

* Parameter

  * None

* Return Value

  * If the execution is successful, the CSQ value is returned. If the execution is failed, -1 is returned. And the returned value 99 indicates the exception.

  * The range of CSQ is 0-31, and the larger the value, the better the signal. 

* Example

```python
>>> import net
>>> net.csqQueryPoll()
31
```



##### Obtain Neighbor Cell Information

> **net.getCellInfo(\*args)**

This function obtains the information of Cell information.

Note：This interface is a variable parameter function in BC25 platform, the number of parameters:[0/1]
case with one Parameter:
	parameter:sinr_enable，
	type:int
	range:0/1
		0，disable to get sinr
		1，enable to get sinr

* Parameter

  This API is a variable parameter function in BC25/EIGEN platform, and the number of parameters is 0 or 1. The number of parameters in other platforms is fixed at 0  ：
    The number of parameters is 0：net.getCellInfo()
    The number of parameters is 1：net.getCellInfo(sinr_enable)
  
| Parameter | Type     | Description                                  |
| -----     | -------- | -------------------------------------------- |
| enable    | int      | range:0/1, 0:disable to get sinr 1:enable to get sinr|

* Return Value

  * If the execution is failed, -1 is returned.  If the execution is successful, the list of neighbor cell information including RATs GSM/UMTS/LTE are returned in the following format. And when the neighbor cell information for one RAT is null, the corresponding list returned is null.  

  * `([(flag, cid, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, licd, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, mcc, mnc, pci, tac, earfcn, rssi, sinr),...])`

* The description of the return value for GSM:

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| flag      | 0: present，1: inter，2: intra                               |
| cid       | Return the cell id of GSM network, 0 means null, range : 0 ~ 65535 |
| mcc       | Mobile Country Code, 0 ~ 999<br>Note : For modules of the EC100Y/EC600S/EC600N series, the value is expressed in hexadecimal. For example, the decimal number 1120 in the following example is 0x460, indicating the mobile device country code 460. For modules of other models, the value is directly expressed in decimal, such as mobile device country code 460, that's 460 in decimal notation. |
| mnc       | Mobile Network Code, range : 0 ~ 99                          |
| lac       | Location Area Code, range : 1 ~ 65534                          |
| arfcn     | Absolute Radio Frequency Channel Number, range : 0 ~ 65535     |
| bsic      | Base Station Identity Code, range : 0 ~ 255                  |
| rssi      | On a GSM network, this value represents the received level and describes the received signal strength. 99 indicates unknown or undetected signal. This value is calculated as follows:<br>rssi = RXLEV - 111<br>The unit is dBm, RXLEV range is 0 ~ 63, so the RSSI range is -111 ~ -48 dBm |

* The description of the return value for UMTS:

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| flag      | 0: present，1: inter，2: intra                               |
| cid       | Return the Cell identity of UMTS network,  Cell identity = RNC_ID * 65536 + Cell_ID,  the range of Cell identity is 0x0000000 ~ 0xFFFFFFF (28bits), the range of RNC_ID is 0 ~ 4095，the range of Cell_ID is 0 ~ 65535 |
| lcid      | URA ID, 0 means null, range : 0 ~ 65535                      |
| mcc       | Mobile Country Code, range : 0 ~ 999                         |
| mnc       | Mobile Network Code, range : 0  ~ 99                           |
| lac       | Location Area Code, range : 1 ~ 65534                        |
| uarfcn    | Absolute Radio Frequency Channel Number, range : 0 ~ 65535   |
| psc       | Base Station Identity Code, range : 0 ~ 255                  |
| rssi      | On a UMTS network, the value indicates the CPICH/PCCPCH receiving power,  unit : dBm, ranges is -5 to 99 |

* The description of the return value for LTE:

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| flag      | 0: present，1: inter，2: intra                               |
| cid       | Return the Cell identity of LTE network,  Cell identity = RNC_ID * 65536 + Cell_ID,  the range of Cell identity is 0x0000000 ~ 0xFFFFFFF (28bits), the range of RNC_ID is 0 ~ 4095，the range of Cell_ID is 0 ~ 65535 |
| mcc       | Mobile Country Code, range : 0 ~ 999                         |
| mnc       | Mobile Network Code, range : 0  ~ 99                           |
| pci       | Physical Cell Identifier，range : 0 ~ 503                    |
| tac       | Tracing area code,  range : 0 ~ 65535                        |
| earfcn    | Extended Absolute Radio Frequency Channel Number, range : 0-65535. |
| rssi      | Received Signal Strength Indication. In LTE network, denotes RSRP quality (negative value), which is converted according to RSRP measurement report value, and the conversion relationship is as follows<br>RSRP quality = RSRP measurement report value - 140, unit : dBm, range : -140 ~ -44 dBm |
| sinr      | Signal to Noise Ratio(supported in BC25/EIGEN，range : -30 ~ 30)   |

* Example

```python
>>> net.getCellInfo()
([], [], [(0, 14071232, 1120, 0, 123, 21771, 1300, -69), (3, 0, 0, 0, 65535, 0, 40936, -140), (3, 0, 0, 0, 65535, 0, 3590, -140), (3, 0, 0, 0, 63, 0, 40936, -112)])

//bc25
>>> net.getCellInfo(1)
([], [], [(0, 17104243, 460, 4, 169, 19472, 3688, -56, -108, -3)])
>>> net.getCellInfo(0)
([], [], [(0, 17104243, 460, 4, 169, 19472, 3688, -75, -102)])
>>> net.getCellInfo()
([], [], [(0, 17104243, 460, 4, 121, 19472, 3688, -76, -105)])
```



##### Obtain RAT and Roaming Configuration

>**net.getConfig()**

The function obtains the current RAT and the roaming configuration.

* Parameter

  * None

* Return Value

  * If the execution is failed, -1 is returned. If the execution is successful, a tuple including the current primary RAT and roaming configuration  is returned.

* Note

  * The BC25PA platform does not support this module function.

* RAT

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
| 19    | CATM,             BG95 supported                             |
| 20    | GSM_CATM,         BG95 supported                             |
| 21    | CATNB,            BG95 supported                             |
| 22    | GSM_CATNB,        BG95 supported                             |
| 23    | CATM_CATNB,       BG95 supported                             |
| 24    | GSM_CATM_CATNB,   BG95 supported                             |
| 25   | CATM_GSM,         BG95 supported                             |
| 26   | CATNB_GSM,        BG95 supported                             |
| 27   | CATNB_CATM,       BG95 supported                             |
| 28   | GSM_CATNB_CATM,   BG95 supported                             |
| 29   | CATM_GSM_CATNB,   BG95 supported                             |
| 30   | CATM_CATNB_GSM,   BG95 supported                             |
| 31   | CATNB_GSM_CATM,   BG95 supported                             |
| 32   | CATNB_CATM_GSM,   BG95 supported                             |

* Example

```python
>>>net.getConfig ()
(8, False)
```



##### Set RAT and Roaming Configuration

> **net.setConfig(mode, roaming)**

The function sets the current RAT and the roaming configuration.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| mode      | int  | RAT. Range: 0-18. For more details, see the table above.     |
| roaming   | int  | Turn on/off the roaming. (0: Turn off. 1: Turn on). This parameter is optional, do not set this parameter for unsupported platforms. |

* Return Value

  * 0  Successful execution.
  * -1  Failed execution.

* Note

  The BC25PA platform does not support this module function. The Unisoc does not support roaming parameters.


##### Obtain the Network Mode

> **net.getNetMode()**

This function obtains the network mode.

* Parameter

  * None

* Return Value

  * If the execution is failed, -1 is returned. If  the execution is successful, a tuple is returned in the format：`(selection_mode, mcc, mnc, act)`
  * The description of the return value:<br/>
    `selection_mode` : Selection Mode. 0- Automatic. 1- Manual.<br/>
    `mcc` : Mobile Country Code, sting type<br/>
    `mnc` : Mobile Network Code, sting type<br/>
    `act` : ACT mode for the primary RAT

* ACT Mode

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

* Note：For CATM platforms, see the following table

| Value| ACT Mode           |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | GSM COMPACT        |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E_UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E_UTRAN_CA         |
| 10   | E_UTRAN_NBIOT      |
| 11   | E_UTRAN_EMTC       |
| 12   | NONE               |

* Example

```python
>>> net.getNetMode()
(0, '460', '46', 7)
```



##### Obtain the Signal Strength

> **net.getSignal(\*args)**

This function obtains the signal strength.

Note：This interface is a variable parameter function in 1803s/qualcomm/unisoc platform, the number of parameters:[0/1]
case with one Parameter:
	parameter:sinr_enable，
	type:int
	range:0/1
		0，disable to get sinr
		1，enable to get sinr

* Parameter

  This API is a variable parameter function except BC25 platform, and the number of parameters is 0 or 1. The number of parameters in other platforms is fixed at 0  ：
    The number of parameters is 0：net.getCellInfo()
    The number of parameters is 1：net.getCellInfo(sinr_enable)
  
| Parameter | Type     | Description                                  |
| -----     | -------- | -------------------------------------------- |
| enable    | int      | range:0/1, 0:disable to get sinr 1:enable to get sinr|

* Return Value

  * If the execution is failed, -1 is returned. If the execution is successful, a tuple including 2 list (GW/LTE) is returned in the following format:

    `([rssi, bitErrorRate, rscp, ecno], [rssi, rsrp, rsrq, cqi, sinr])`

  * The description of the return value:

    * GW list：

      `rssi` : On a GSM/WCDMA network, this value represents the received level and describes the received signal strength. 99 indicates unknown or undetected signal. This value is calculated as follows: <br/>
      &emsp;rssi = RXLEV - 111 <br/>
      &emsp;The unit is dBm, RXLEV range is 0 ~ 63, so the range of rssi  is -111 ~ -48 dBm <br/>
      `bitErrorRate` : Error Rate(BER), range : 0  ~ 7, 99 indicates unknown or undetected signal <br/>
      `rscp` : Received Signal Code Power, range : -121 ~ -25 dBm, 255 indicates unknown or undetected signal <br/>
      `ecno` :   Pilot Channel , range : -24 ~ 0, 255 indicates unknown or undetected signal

    * LTE list：

      `rssi` : Received Signal Strength Indicator, range : -140 ~ -44 dBm, 99 indicates unknown or undetected signal <br/>
      `rsrp` : Reference Signal Receiving Power, range : -141 ~ -44 dBm, 99 indicates unknown or undetected signal <br/>
      `rsrq` : Reference Signal Receiving Quality, range : -20 ~ -3 dBm, A larger value indicates better signal reception quality <br/>
      `cqi` : Channel Quality
	  `sinr`: Signal to Noise Ratio(supported except RDA platform，range : -30 ~ 30)
* Example

```python
>>>net.getSignal()
([99, 99, 255, 255], [-51, -76, -5, 255])

>>>net.getSignal(0)
([99, 99, 255, 255], [-51, -76, -5, 255])
>>>net.getSignal(1)
([99, 99, 255, 255], [-51, -76, -5, 255, 18])
```



##### Obtain the Current Time of the Base Station

> **net.nitzTime()**

This function obtains the current time of the base station. This time is the time that the base station sends when the module is successfully turned on and plugged into the network.

* Parameter

  * None

* Return Value

  * If the execution is failed, -1 is returned. If the execution is successful, a tuple is returned in the following format: 

    `(date, abs_time, leap_sec)`

      `date` : String type. The time of the base station. The TIME zone of the EC600N series is different from that of the EC200U/EC600U series. For details, see the example. If you need to set and obtain the time zone, use the 'setTimeZone(offset)' and 'getTimeZone()' interfaces of the utime module. <br/>
      `abs_time` : Integer type. The absolute number of seconds of time. <br/>
      `leap_sec` : Integer type. The leap second.

* Example

```python
>>> net.nitzTime() 
('21/10/26 06:08:03 8 0', 1635228483, 0) # EC600N series, the time zone unit is hour, 8 indicates the east 8 region
('20/11/26 02:13:25 +32 0', 1606356805, 0) # EC200U/EC600U series, the time zone unit is 15 minutes. +32 indicates the east 8 region
```



##### Obtain the Current Operator Information

> **net.operatorName()**

This function obtains the current operator information.

* Parameter

  * None

* Return Value

  * If the execution is failed, -1 is returned. If the execution is successful, a tuple is returned in the following format:

    `(long_eons, short_eons, mcc, mnc)` <br/>
    `long_eons` :  String type. Full name of the operator information. <br/>
    `short_eons` :  String type. Short name of the operator information. <br/>
    `mcc` : String type. Mobile Country Code. <br/>
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

  * None

* Return Value

  * If the execution is failed, -1 is returned. If the execution is successful, a tuple is returned in the following format. The tuple contains voice and network registration information. The tuple starting with 'voice\_' indicates voice registration information, and the tuple starting with 'data\_' indicates network registration information:

    `([voice_state, voice_lac, voice_cid, voice_rat, voice_reject_cause, voice_psc], [data_state, data_lac, data_cid, data_rat, data_reject_cause, data_psc])`

    The description of the return value:

    `state` : Network registration state. <br/>
    `lac` : Location Area Code, range : 1 ~ 65534 <br/>
    `cid` : cell id, range : 0x0000000 ~ 0xFFFFFFF <br/>
    `rat` : access technology <br/>
    `reject_cause` : Reject cause. This parameter is reserved on EC200U/EC600U/BC25PA <br/>
    `psc` ：Primary Scrambling Code. This parameter is reserved on EC200U/EC600U/BC25PA

* Network registration state

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



* access technology

| Value | Description        |
| ----- | ------------------ |
| 0     | GSM                |
| 1     | GSM COMPACT        |
| 2     | UTRAN              |
| 3     | GSM wEGPRS         |
| 4     | UTRAN wHSDPA       |
| 5     | UTRAN wHSUPA       |
| 6     | UTRAN wHSDPA HSUPA |
| 7     | E_UTRAN            |
| 8     | UTRAN HSPAP        |
| 9     | E_UTRAN_CA         |
| 10    | NONE               |

* Note：For CATM platforms, see the following table

| Value| ACT Mode           |
| ---- | ------------------ |
| 0    | GSM                |
| 1    | GSM COMPACT        |
| 2    | UTRAN              |
| 3    | GSM wEGPRS         |
| 4    | UTRAN wHSDPA       |
| 5    | UTRAN wHSUPA       |
| 6    | UTRAN wHSDPA HSUPA |
| 7    | E_UTRAN            |
| 8    | UTRAN HSPAP        |
| 9    | E_UTRAN_CA         |
| 10   | E_UTRAN_NBIOT      |
| 11   | E_UTRAN_EMTC       |
| 12   | NONE               |

* Example

```python
>>> net.getState()
([11, 26909, 232301323, 7, 0, 466], [0, 26909, 232301323, 7, 0, 0])
```



##### Obtain the ID of the Neighbor Cell

> **net.getCi()**

This function obtains the ID of the Neighbor Cell. The result obtained by this interface is the CID set in the result obtained by the `net.getCellInfo()` interface.

* Parameter

  * None

* Return Value

  * If the execution is failed, -1 is returned. If the execution is successful, an array in list type including cell ID is returned, and the format of this array is `[id, ……, id]`。

* Example

```python
>>> net.getCi()
[14071232, 0]
```



##### Obtain the ID of the Serving Cell

> **net.getServingCi()**

Obtain the ID of the Serving Cell.

* Parameter

  * None

* Return Value

  * Serving cell ID : Successful execution.
  * -1: Failed execution.

* Example

```python
>>> net.getServingCi()
94938399
```



##### Obtain the MNC of the Neighbor Cell

> **net.getMnc()**

This function obtains the MNC of the neighbor cell. The result obtained by this interface is the mnc set in the result obtained by the `net.getCellInfo()` interface.

* Parameter

  * None

* Return Value

  * If the execution is failed, -1 is returned. If the execution is successful, an array in list type including cell MNC is returned, and the format of this array is `[mnc, ……, mnc]`.

* Example

```python
>>> net.getMnc()
[0, 0]
```



##### Obtain the MNC of the Serving Cell

> **net.getServingMnc()**

Obtain the MNC of the Serving Cell.

* Parameter

  * None

* Return Value

  * Serving cell MNC : Successful execution.
  * -1: Failed execution.

* Example

```python
>>> net.getServingMnc()
1
```



##### Obtain the MCC of the Neighbor Cell

> **net.getMcc()**

This function obtains the MCC of the neighbor cell. The result obtained by this interface is the mcc set in the result obtained by the `net.getCellInfo()` interface.

* Parameter

  * None

* Return Value

  * If the execution is failed, -1 is returned. If the execution is successful, an array in list type including cell MCC is returned, and the format of this array is `[mcc, ……, mcc]`.

* Note 

  * For modules of the EC100Y/EC600S/EC600N series, the value is expressed in hexadecimal. For example, the decimal number 1120 in the following example is 0x460, indicating the mobile device country code 460. For modules of other models, the value is directly expressed in decimal, such as the mobile device country code 460. That's 460 in decimal notation.

* Example

```python
>>> net.getMcc()
[1120, 0]
```



##### Obtain the MCC of the Serving Cell

> **net.getServingMcc()**

Obtain the MCC of the Serving Cell.

* Parameter

  * None

* Return Value

  * Serving cell MCC : Successful execution.
  * -1: Failed execution.

* Note

  * For modules of the EC100Y/EC600S/EC600N series, the value is expressed in hexadecimal. For example, the decimal number 1120 in the following example is 0x460, indicating the mobile device country code 460. For modules of other models, the value is directly expressed in decimal, such as the mobile device country code 460.That's 460 in decimal notation.

* Example

```python
>>> net.getServingMcc()
1120
```



##### Obtain the LAC of the Neighbor Cell

> **net.getLac()**

This function obtains the LAC of the neighbor cell. The result obtained by this interface is the lac set in the result obtained by the `net.getCellInfo()` interface.

* Parameter

  * None

* Return Value

  * If the execution is failed, -1 is returned. If the execution is successful, an array in list type including cell LAC is returned, and the format of this array is `[lac, ……, lac]`.

* Example

```python
>>> net.getLac()
[21771, 0]
```



##### Obtain the LAC of the Serving Cell

> **net.getServingLac()**

Obtain the LAC of the Serving Cell.

* Parameter

  * None

* Return Value

  * Serving cell LAC : Successful execution.
  * -1: Failed execution.

* Example

```python
>>> net.getServingLac()
56848
```



##### Obtain the Modem Functionality

> **net.getModemFun()**

This function obtains the current modem functionality.

* Parameter

  * None

* Return Value

  * If the execution is failed, -1 is returned. If the execution is successful, the current modem functionality is returned:

    0 : Minimum functionality<br/>
    1 : Full functionality (Default)<br/>
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
| function  | int  | 0 - Minimum functionality. <br/>1 - Full functionality.<br/>4 - Airplane mode.(The RDA platform does not support CFUN4) |
| rst       | int  | Optional. <br>0 - Take effect immediately (Default).<br/>1- Take effect after rebooting. |

* Return Value

  * 0  Successful execution.
  * -1  Failed execution.

* Example

```python
>>> net.setModemFun(4)
0
```



##### band Setting and obtaining

##### band value comparison table

| NET MODE        | BAND VALUE                                                       |
| --------------- | ------------------------------------------------------------ |
| EGPRS(GSM)      | EGSM900 - 0x1<br/>DCS1800 - 0x2<br/>GSM850 - 0x4<br/>PCS1900 - 0x8 |
| LTE/eMTC/NB-IoT | BAND1 - 0x1<br/>BAND2 - 0x2<br/>BAND3 - 0x4<br/>BAND4 - 0x8<br/>BAND5 - 0x10<br/>BAND8 - 0x80<br/>BAND12 - 0x800<br/>BAND13 - 0x1000<br/>BAND18 - 0x20000<br/>BAND19 - 0x40000<br/>BAND20 - 0x80000<br/>BAND25 - 0x1000000<br/>BAND26 - 0x2000000<br/>BAND27 - 0x4000000<br/>BAND28 - 0x8000000<br/>BAND31 - 0x40000000<br/>BAND66 - 0x20000000000000000<br/>BAND71 - 0x400000000000000000<br/>BAND72 - 0x800000000000000000<br/>BAND73 - 0x1000000000000000000<br/>BAND85 - 0x1000000000000000000000<br/> |

##### band of BG95M3

| NET MODE | BAND VALUE                                                  |
| -------- | ------------------------------------------------------------ |
| eMTC     | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B26/B27/B28/B66/B85 |
| NB-IoT   | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B28/B66/B71/B85    |
| EGPRS    | GSM850/EGSM900/DCS1800/PCS1900                               |

##### band of EG912NENAA

| NET MODE | BAND VALUE                           |
| -------- | ------------------------------------ |
| LTE      | B1/B3/B5/B7/B8/B20/B28/B31/B72       |
| EGPRS    | EGSM900/DCS1800                      |



##### band Setting

> **net.setBand(net_rat, gsm_band, band_tuple)**

  Set required bands, that is, lock the bands specified by the user if the module supports them。 (Platforms are currently supported：CATM/EG912NENAA)

* Parameter

| Parameter  | Type  | Description                                                  |
| ---------- | ----- | ------------------------------------------------------------ |
| net_rat    | int   | Specify which net mode band is to be set<br>0 - GSM<br>1 - LTE<br>2 - CATM<br>3 - NB<br>note：The CATM platform does not support LTE<br/>The EG912NENAA platform just support GSM and LTE |
| gsm_band   | int   | gsm band value<br/>0x01 - GSM_EGSM900<br/>0x02 - GSM_DCS1800<br>0x04 - GSM_GSM850<br/>0x08 - GSM_PCS1900 |
| band_tuple | tuple | band value of other network modes，Is a tuple of four elements, each of which cannot exceed 4 bytes. The format is as follows：<br>(band_hh, band_hl, band_lh, band_ll)|

* Return Value

  * 0  Successful execution.
  * -1  Failed execution.

* Example

```python
import net
import utime

'''
You can use the following two interfaces to set and obtain bands
'''
def set_band(net_rat, band_value):
    if net_rat == 0:
        retval = net.setBand(0, band_value, (0, 0, 0, 0))
    else:
        band_hh = (band_value & 0xFFFFFFFF000000000000000000000000) >> 96
        band_hl = (band_value & 0x00000000FFFFFFFF0000000000000000) >> 64
        band_lh = (band_value & 0x0000000000000000FFFFFFFF00000000) >> 32
        band_ll = (band_value & 0x000000000000000000000000FFFFFFFF)
        retval = net.setBand(net_rat, 0, (band_hh, band_hl, band_lh, band_ll))
    return retval


def get_band(net_rat):
    return net.getBand(net_rat)

#======================================================================================================

'''
Set the band of the GSM network to 0xa, that is, DCS1800 + PCS1900
0xa = 0x2(DCS1800) + 0x8(PCS1900)
'''
def set_gsm_band_example():
    print('Set GSM band to 0xa example:')
    gsm_band = get_band(0)
    print('GSM band value before setting:{}'.format(gsm_band))
    ret = set_band(0, 0xa)
    if ret == 0:
        print('Set GSM band successfully.')
    else:
        print('Set GSM band failed.')
    utime.sleep(1) # It takes a certain period of time to set the band. After a delay period, you can obtain the new result
    gsm_band = get_band(0)
    print('GSM band value after setting:{}'.format(gsm_band))
    return ret


'''
Set the eMTC network band to 0x15, that is, set BAND1+BAND3+BAND5
0x15 = 0x1(BAND1) + 0x4(BAND3) + 0x10(BAND5)
'''
def set_camt_band_example():
    print('Set CATM band to 0x15 example:')
    catm_band = get_band(2)
    print('CATM band value before setting:{}'.format(catm_band))
    ret = set_band(2, 0x15)
    if ret == 0:
        print('Set CATM band successfully.')
    else:
        print('Set CATM band failed.')
    utime.sleep(1)
    catm_band = get_band(2)
    print('CATM band value after setting:{}'.format(catm_band))
    return ret


'''
Set the eMTC network band to 0x1000800000000000020011，that is, set BAND1+BAND5+BAND18+BAND71+BAND85
0x1000400000000000020011 = 0x1 + 0x10 + 0x20000 + 0x400000000000000000 + 0x1000000000000000000000
'''
def set_nb_band_example():
    print('Set NB band to 0x1000400000000000020011 example:')
    nb_band = get_band(3)
    print('NB band value before setting:{}'.format(nb_band))
    ret = set_band(3, 0x1000400000000000020011)
    if ret == 0:
        print('Set NB band successfully.')
    else:
        print('Set NB band failed.')
    utime.sleep(1)
    nb_band = get_band(3)
    print('NB band value after setting:{}'.format(nb_band))
    return ret


def main():
    set_gsm_band_example()
    utime.sleep(1)
    set_camt_band_example()
    utime.sleep(1)
    set_nb_band_example()


if __name__ == '__main__':
    main()
    

#===================================================================================================
#result
Set GSM band to 0xa example:
GSM band value before setting:0xf
Set GSM band successfully.
GSM band value after setting:0xa

Set CATM band to 0x15 example:
CATM band value before setting:0x10000200000000090e189f
Set CATM band successfully.
CATM band value after setting:0x15

Set NB band to 0x1000400000000000020011 example:
NB band value before setting:0x10004200000000090e189f
Set NB band successfully.
NB band value after setting:0x1000400000000000020011

```



##### band obtaining

> **net.getBand(net_rat)**

Band obtaining。(Platforms are currently supported：CATM/EG912NENAA)

* Parameter

| Parameter | Type  | Description                                                  |
| -------   | ----  | ------------------------------------------------------------ |
| net_rat   | int   | Specify which net mode band is to be get<br>0 - GSM<br>1 - LTE<br>2 - CATM<br>3 - NB<br>note：The CATM platform does not support LTE<br/>The EG912NENAA platform just support GSM and LTE |

* Return Value

Return the band value as a hexadecimal string.

* example

```python
net.getBand(2)
'0x10000200000000090e189f'
```



##### band Restores the initial value

> **net.bandRst()**

band Restores the initial value。(Platforms are currently supported：EG912NENAA)

* Parameter

 * NA

* Return Value

  * 0  Successful execution.
  * -1  Failed execution.

* Example

```python
#Set it to another band and call the interface to check whether the interface is successfully restored to the initial value
#EG912NENAA platform initial value：gsm_band:0x3(EGSM900/DCS1800 )  lte_band:0x8000000000480800D5(B1/B3/B5/B7/B8/B20/B28/B31/B72 )
net.bandRst()
0
```



#### checkNet - Wait for Network to be Ready

Function: The checkNet module is mainly used for the script programs [auto-startup], and provides APIs to wait for the network to be ready. If it times out or exits abnormally, the program returns an error code. Therefore, if there are network-related operations in the your program, the method in the checkNet module should be called at the beginning of the user program to wait for the network to be ready. Of course, you can also implement the functions of this module by yourselves. 
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

  * NA

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

  PROJECT_NAME     	  : Project Name.<br/>
  PROJECT_VERSION 	 : Project Version.<br/>
  FIRMWARE_VERSION  : Firmware Version .<br/>
  POWERON_REASON   : The reason of the power-on.<br/>
  SIM_CARD_STATUS     : The status of SIM card.

* Parameter

  * None

* Return Value

  * None

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

  * There are two return values in the following format:

    `stagecode, subcode`

  * The description for each return values:

  | Return Value | Type | Description                                                  |
  | ------------ | ---- | ------------------------------------------------------------ |
  | stagecode    | Int  | Stage code, indicates the stage of the checkNet module. <br>1 - Obtaining the state of the  SIM card. This value is returned when the timeout expires or the state of the SIM card is abnormal. <br>2 - Obtaining the state of the network registration. This value is returned when the timeout expires.<br>3 - Obtaining the state of the dial-up.<br>The normal return value is 3 indicates the normal. |
  | subcode      | Int  | Subcode，it is combined with the value of stagecode  to represent the specific state of checknet in different stages.<br/>When  stagecode = 1 ：<br/>subcode indicates the state of the SIM card, range: [0, 21], for the description of each value, refer to the return value in sim.getStatus() [https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=sim-sim-card](https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=sim-sim-card) <br/><br/><br/>When stagecode = 2 ：<br/>subcode indicates the state of the network registration, range: [0, 11], for the description of each values, refer to the return value in net.getState()[https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=net-network](https://python.quectel.com/wiki/#/en-us/api/QuecPythonClasslib?id=net-network)    <br/>When subcode = -1, indicates the dial-up is failed within the timeout.<br/>For other value, see the above link.<br/>If within the timeout, the network registration is successful, enter the stage of stagecode = 3 directly.<br/><br/>When stagecode = 3 : <br/>subcode = 0, indicates the  dial-up is failed within the timeout.<br/>subcode = 1, indicates the network connection is successful within the timeout, that is the network registration and dial-up is successful. |

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

* Note

If the user is using firmware released after November 2021, the user can use the wait_network_connected(timeout) method as follows:

```python
import checkNet

if __name__ == '__main__':
    # Add the following sentence before running the program.
    stagecode, subcode = checkNet.wait_network_connected(30)
    print('stagecode = {}, subcode = {}'.format(stagecode, subcode))
	......
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

Optional parameters to select whether to automatically restart after downloading the upgrade package 

> **import fota**
>
> **fota_obj = fota()**#Automatically restart after downloading
>
> **fota_obj = fota(reset_disable=1)**#Not restart after downloading

##### One-click Upgrade Interface

> **fota_obj.httpDownload(url1=, url2=, callback=)**

Realize the whole process of firmware download and upgrade with one interface

- Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| url1      | str            | The url of the first stage upgrade package to be downloaded  |
| url2      | str            | The url of the second stage upgrade package to be downloaded. Note: this parameter must be input for the minimum system upgrade because the minimum system is divided into two stages, while this parameter is forbidden to be input  for DFOTA and FullFOTA upgrade because there is only one stage for DFOTA and FullFOTA. Only EC600S/EC600N modules support the minimum system upgrade mode. |
| callback  | function       | Callback function which shows downloading progress and status (Optional). Note: This callback is valid on non-minimum system upgrade mode. |

- Return Value

  * Return integer value 0 if the download is successful and return integer value -1 if the download fails.

* Note

  * on EC600S/EC600N module, the return value only represents the success or failure of the command, and the download status needs to be fed back through the callback.

- Example

```python
#args[0] indicates the download status. If the download is successful, it returns an integer value: 0 or 1 or 2. If the download fails, it returns an integer value: values other than 0,1,2. args[1] represents the download progress. Note:on EC600S/EC600N module,when the download status shows success, it represents the percentage. When the download status shows failure, it represents error code
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

  * 0 	Successful execution
  * -1	Failed execution

* Note

  * Currently only EC600S/EC600N/EC800N/EC200U/EC600U platform support this method.


##### Interface to Upgrade Step by Step and Refresh Cached Data to Flash

> **fota_obj.flush()**

Refresh cached data to the flash.

- Parameter

  * None

- Return Value

  * 0 	Successful execution
  * -1	Failed execution

* Note

  * Currently only EC600S/EC600N/EC800N/EC200U/EC600U platform support this method.

##### Interface to Upgrade Step by Step and Verify the Data

> **fota_obj.verify()**

 Verify the data.

* Parameter

  * None

* Return Value

  * 0 	Successful execution
  * -1	Failed execution

* Note

  * Currently only EC600S/EC600N/EC800N/EC200U/EC600U platform support this method.

* Example

```python
>>> fota_obj.verify()
0
```

##### Interface to set up APN for FOTA download 

> fota_obj.apn_set(fota_apn=,ip_type=,fota_user=,fota_password=)

Set the APN information used for FOTA download.

* Parameter

| Parameter     | Parameter Type | Description                                                  |
| ------------- | -------------- | ------------------------------------------------------------ |
| fota_apn      | str            | APN（You can choose not to pass this parameter）             |
| ip_type       | int            | IP type：0-IPV4，1-IPV6（You can choose not to pass this parameter） |
| fota_user     | str            | user name（You can choose not to pass this parameter）       |
| fota_password | str            | password（You can choose not to pass this parameter）        |

* Return Value

  * 0 	Successful execution
  * -1	Failed execution

* Example

```python
>>> fota_obj.apn_set(fota_apn="CMNET",ip_type=0,fota_user="abc",fota_password="123")
0
```

* Note

  - Currently only BG95 platform support this method.

##### Interface to cancel FOTA downloading

> fota_obj.download_cancel()

Cancel the FOTA download in progress.

- Parameter

  - None

* Return Value

  * 0 	Successful execution
  * -1	Failed execution

* Example

```python
import fota
import _thread
import utime

def th_func():
    utime.sleep(40) #Depending on the size of the package, make sure to cancel before the download is complete
    fota_obj.download_cancel()

def result(args):
    print('download status:',args[0],'download process:',args[1])

fota_obj = fota()
_thread.start_new_thread(th_func, ())
fota_obj.httpDownload(url1="http://www.example.com/fota.bin",callback=result)
```

* Note

  - Currently only BG95 platform support this method.

  

##### Example

###### One-click Upgrade Interface

```python
#Automatically restart after downloading

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

```python
#Not automatically restart after the download is complete (not supported on the EC600S、EC600N、EC800N platform)

# EC200A/EC200U/BG95 platform：
import fota
from misc import Power
fota_obj = fota(reset_disable=1)
def result(args):
    print('download status:',args[0],'download process:',args[1])
fota_obj.httpDownload(url1="http://www.example.com/dfota.bin",callback=result) #expected that not restart after execution
Power.powerRestart() #Manually restart
```



###### Interface to Upgrade Step by Step

- Note
  - Currently only EC600S/EC600N/EC800N/EC200U/EC600U platform support this feature.

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

   * 0 	Successful execution
   * -1	Failed execution



##### Download Files in Batches

> **fota.bulk_download(info=[])**

 - Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| info      | list           | Download files in batches. The elements of the list are  dictionaries containing `url` and `file_name` |


 - Return Value

   * Return the list of failed downloading

 - Example

```python
download_list = [{'url': 'http://www.example.com/app.py', 'file_name': '/usr/app.py'}, {'url': 'http://www.example.com/test.txt', 'file_name': '/usr/text.txt'}]
```

In this example, assuming that `http://www.example.com/test.txt`fails to be downloaded, the return value is`[{url: 'http://www.example.com/test.txt', file_name: '/usr/text.txt'}]`



##### Set Upgrade Flag

> **fota.set_update_flag()**

 - Parameter

   * None

 - Return Value

   * None

> After setting the upgrade flag, call the restart interface, and the upgrade can be started after the restart.

> After the upgrade is complete, you will directly enter the application.

> Reference link of the restart interface : http://qpy.quectel.com/wiki/#/en-us/api/?id=power



#### audio - Audio Playback

Module function: audio playback, supports to play files, mp3 and AMR.

Note: The BC25PA platform does not support this module function.



##### Audio

###### Create an object

> **import audio**
>
> **aud = audio.Audio(device)**

* Parameter


| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| device    | int            | Output channel<br/>0 - handset<br/>1 - earphone<br/>2 - speaker |

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

  * 0 	Successful execution
  * -1	Failed execution

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

* Return Value

  * 0 	Successful execution
  * -1	Failed execution
  * 1	 Cannot be played immediately, but join the playback queue
  * -2	Cannot be played immediately, and the priority group queue task of the request has reached the 		upper limit and cannot be added to the play queue

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

  * None

* Return Value

  * 0 	Successful execution
  * -1	Failed execution



###### stop queue playback

> **aud.stopAll()**

Stop the playback of the entire queue, that is, if TTS or audio is currently being played, and there are other content to be played in the queue, after calling this interface, it will not only stop the currently playing content, but also clear the content of the queue, and no longer play any more. content. If it is currently playing and the playback queue is empty, calling this interface has the same effect as the stop() interface.

* Parameter

  * None

* Return Value

  * 0     Successful execution
  * -1    Failed execution



###### Register the Callback Function

> **aud.setCallback(usrFun)**

Register the callback function of the user. It is used to notify the user of the audio file playback status. Note that time-consuming and blocking operations should not be performed in this callback function. It is recommended to only perform simple and short-time operations.

* Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| usrFun    | function       | The callback function of the user. See the format in the following example |

* Return Value

  * 0 Successful execution
  * -1 Failed execution

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

  * None

* Return Value

  * 0 Successful execution
  * -1 Failed execution



###### Get Audio Volume

> **aud.getVolume()**

Get the audio volume, and the default value is 7.

* Parameter

  * None

* Return Value

  * Return the volume in integer.



###### Set Audio Volume

> **aud.setVolume(vol)**

Set audio volume.

* Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| vol       | int            | Volume. Range: 0 –11. The higher the number, the higher the volume. |

* Return Value

  * 0 Successful execution
  * -1 Failed execution

* Example

```python
>>> aud.setVolume(6)
0
>>> aud.getVolume()
6
```



###### Audio streaming

> aud.playStream(format, buf)

Audio stream playback, supporting MP3, AMR and WAV format audio stream playback.

* Parameter

|Parameter | parameter type | parameter description|
| ------ | -------- | ------------------------------------------------------------ |
|Format | int | audio stream format <br/> 1 - PCM (not supported temporarily) <br/> 2 - WAVPCM <br/> 3 - MP3 <br/> 4 - ARMNB |
|Buf | buf | audio stream content|

* Return Value

  * If the playback is successful, the integer 0 will be returned;
  * If playback fails, integer - 1 will be returned;

  

###### Stop audio streaming

> audio_test.stopPlayStream()

Stop audio streaming

* Parameter

  * None

* Return Value

  * Stop successfully, return integer 0;
  * Stop failure returns integer - 1;


- Examples

  ```python
  import audio
  import utime
  
  audio_test = audio.Audio(0)
  
  Size = 10 * 1024 # ensure that the audio data filled at one time is large enough for continuous playback at the bottom layer
  format = 4
  
  def play_from_fs():
      file_ size = uos. Stat ("/usr/test.AMR") [6] # get the total bytes of the file
      print(file_size)
      with open("/usr/test.amr", "rb")as f:   
          while 1:
              b = f.read(size)   # read
              if not b:
                  break
              audio_test.playStream(format, b)
              utime.sleep_ms(20)
  
  
  play_from_fs()
  utime.sleep_ms(5000) # wait for playback to complete
  audio_test.stopPlayStream() # stops this playback so as not to affect the next playback
  ```



###### Tone playback

Support platform EC600U/EC200U/EC600N/EC800N

> aud.aud_tone_play(tone, time)

Play tone tone and stop playing automatically after playing for a period of time（Note: When the EC600N/EC800N platform calls this interface, it is an immediate return. When the EC600U/EC200U platform calls this interface, it is a blocking wait ）

* Parameter

|Parameter | parameter type | parameter description|
| ---- | -------- | ------------------------------------------------------------ |
|Tone | int | tone type <br/> 0 ~ 15 - key tone (0 ~ 9, a, B, C, D, #, *) <br/> 16 - dial tone |
|Time | int | playback duration, unit MS <br/> 0 - Keep playing without stopping, It can only be stopped by calling the aud.aud_tone_play_stop() interface (The EC600N/EC800N duration is unlimited. The EC600U/EC200U duration is about 2 minutes) <br/> greater than 0 - playback duration time MS |

* Return Value

  * If the playback is successful, the integer 0 will be returned;

  * If playback fails, integer - 1 will be returned;

  

###### Stop tone playback

> aud.aud_tone_play_stop()

Actively stop playing tone

* Parameter

  * None

* Return Value

  * Stop successfully, return integer 0;
  * Stop failure returns integer - 1;




- Examples

```python
import audio
import utime

aud = audio.Audio(0)

#EC200U/EC600U platform
def dial_play_ec600u():
    for i in range(0,10):
        aud.aud_tone_play(16, 1000)
        utime.sleep(1)

#EC600N/EC800N platform
def dial_play_ec600n():
    for i in range(0,10):
        aud.aud_tone_play(16, 1000)
        utime.sleep(2)
        
# dial_play_ec600n()
dial_play_ec600u()
```



##### Record

Applicable versions: EC100Y(V0009) and above; EC600S(V0003) and above.

Note: The BC25PA platform does not support this module function.

###### Create an Object

> **import audio**
>
> **record = audio.Record(device)**

Without parameter, the handset is used for playback by default; with parameter, the playback device is set as parameter.

Note: with parameter, the parameter should be the same as that set by audio.audio().

* Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| device    | int            | Output channel<br/>0 - handset<br/>1 - earphone<br/>2 - speaker |

* Return Value

  * 0 Successful execution
  * -1 Failed execution
* Example

```python
import audio 
record_test = audio.Record()#Without parameter, use the handset to play
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

  * 0	Successful execution
  * -1	File overwrite failed
  * -2	File open failed
  * -3	The file is in use
  * -4	Channel setting error 
  * -5	Request for timer resource failed
  * -6	Audio format detection error
  * -7	The file has been created by another object

* Example

```python
record_test.start("test.wav",40)	#Record the file in wav format
record_test.start("test.amr",40)	#Record the file in amr format
record_test.start("test",40)	#Record the file in amr format
```



###### Stop Recording

> **record.stop()**

Stop recording.

* Parameter

  * None

* Return Value

  * 0 Successful execution
  * -1 Failed execution

* Example

```python
record_test.stop()
```



###### Read Storage Path of the Recording File

> **record. getFilePath(file_name)**

Read storage path of the recording file.

* Parameter

| Parameter | Parameter Type | Description                |
| --------- | -------------- | -------------------------- |
| file_name | str            | Name of the recording file |

* Return Value

  * If the file is successfully executed, the path of the recording file is returned, string type. If the target file does not exist, integer -1 is returned. If the file name length is 0, integer -2 is returned.

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

  * Return the data of record if it is executed successfully, bytearray type.

    -1	Error reading data
    -2	File open failed
    -3	Wrong offset setting
    -4	The file is in use
    -5	Setting exceeds file size(offset+size > file_size)
    -6	The read size is greater than 10 K
    -7	 Less than 10 K of memory
    -8	 The file does not belong to the object

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

  * Return the file size if it is executed successfully.

  * In wav format, this value will be 44 bytes larger than the return value of the callback (44 bytes is the size of the file header)

  * In amr format, this value will be 6 bytes larger than the return value of the callback (6 bytes is the size of the file header); Or else

    *-1*	Failed execution <br/>
    *-2*	File open failed <br/>
    *-3*	The file is in use <br/>
    *-4*	The length of file name is 0

* Example

```python
record_test.getSize(“test.amr”)
```



###### Delete Recording File

> **record.Delete(file_name)**

Delete the recording file.

* Parameter

*file\_name*： 

String type. The file name of the recording.

Note: When the parameter is empty, delete all recording files in the object

| Parameter | Parameter Type | Description                |
| --------- | -------------- | -------------------------- |
| file_name | str            | File name of the recording |

* Return Value

  * 0	Successful execution
  * -1	The file does not exist
  * -2	File is in use
  * -3	The file does not belong to the object

* Example

```python
record_test.Delete(“test.amr”)
```



###### Determine Whether the Recording File Exists

> **record.exists(file_name)**

Determine whether the recording file exists.

* Parameter

| Parameter | Parameter Type | Description                |
| --------- | -------------- | -------------------------- |
| ile_name  | str            | File name of the recording |

* Return Value

  * true		The file exists
  * false	   The file does not exist
  * -1		The file does not belong to the object

* Example

```python
record_test.exists(“test.amr”)
```



###### Determine Whether the Recording is in Progress

> **record.isBusy()**

Determine whether the recording is in progress

* Parameter

  * None

* Return Value

  * 0	idle
  * 1	busy

* Example

```python
record_test.isBusy()
```



###### Register the Callback of Recording End

> **record.end_callback(callback)**

Set the callback of recording end

* Parameter

| Parameter | Parameter Type | Description       |
| --------- | -------------- | ----------------- |
| callback  | funciton       | Callback function |

* Return Value

  * 0	Successful execution
  * other	Failed  execution  

* Example

```python
def record_callback(para): 
	print("file_name:",para[0])   # Return the file path 
    print("audio_len:",para[1])   # Return the recording length 
    print("audio_state:",para[2])  
    # Return recording state -1: error, 0: start, 3: success 
record_test.end_callback(record_callback)
```



| para[2] | Description          |
| ------- | -------------------- |
| -1      | error                |
| 0       | Start the recording  |
| 3       | End of the recording |



###### Set Recording Gain

> **record.gain(code_gain,dsp_gain)**

Set recording gain.

* Parameter

| Parameter | Parameter Type | Description                  |
| --------- | -------------- | ---------------------------- |
| code_gain | int            | Uplink codec gain [0,4]      |
| dsp_gain  | int            | Uplink digital gain [-36,12] |

* Return Value

  * 0	Successful execution

* Example

```python
record_test.gain(4,12)
```



###### Switch amr recording DTX function

Currently only 600N/800N platforms support this function.

> **record.amrEncDtx_enable(on_off)**

Switch amr recording DTX function

- Parameter

| Parameter | Parameter Type | Description                                                  |
| --------- | -------------- | ------------------------------------------------------------ |
| on_off    | int            | 1: open DTX <br>0: close DTX   <br>No parameters：Get current configuration |

- Return Value

  * No parameters：Get current configuration

  * with parameters：If the parameter is correct, there is no return, if the parameter is wrong, an exception will be thrown.

- Example

```python
record_test.amrEncDtx_enable(1)
```



###### Recording stream

At present, it is only supported by ec200u/ec600u platforms.

> **record.stream_start(format, samplerate, time)**

Recording audio stream

* Parameter

|Parameter | parameter type | parameter description|
| ---------- | -------- | --------------------------- |
|Format | int | audio format. At present, AMR format is supported|
|SampleRate | int | sampling rate. At present, 8K and 16K are supported|
|Time | int | recording duration, unit s (seconds)|

* Return Value

  * The integer 0 is returned successfully, and the integer - 1 is returned in case of failure.

* Example

```python
record_test.stream_start(record_test.AMRNB, 8000, 5)
```

* Note

  * while recording the audio stream, read the audio stream in time. At present, cyclic buf is adopted, and if it is not read in time, it will lead to data loss



###### Read recording stream

At present, it is only supported by ec200u/ec600u platforms.

> **record.stream_read(read_buf, len)**

Recording audio stream

* Parameter

|Parameter | parameter type | parameter description|
| -------- | -------- | ------------- |
| read_ Buf | buf | recording stream saving buf|
|Len | int | read length|

* Return Value

  * The number of bytes actually read is returned successfully, and integer - 1 is returned in case of failure.

* Examples

```python
read_buf = bytearray(128)
record_test.stream_read(read_buf, 128)
```

###### Recording stream example

```python
import audio
import utime
record_test = audio.Record()
audio_test = audio.Audio(0)

read_time = 5

buf = bytearray(0)

def stream_rec_cb(para):
    global buf
    if(para[0] == 'stream'):
        if(para[2] == 1):
            read_buf = bytearray(para[1])
            record_test.stream_read(read_buf,para[1])
            buf += read_buf
            del read_buf
        elif (para[2] == 3):
            audio_test.stopPlayStream()
            audio_test.playStream(record_test.AMRNB, buf)



record_test.end_callback(stream_rec_cb)
audio_test.stopPlayStream()
record_test.stream_start(record_test.AMRNB, 8000, read_time)
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

  * None

* Return Value

  * None



###### Module Restart

> **Power.powerRestart()**

The module restarts.

* Parameter

  * None

* Return Value

  * None



###### Get the Reason for Module Powering On

> **Power. powerOnReason()**

It gets the reason for module powering on.

* Parameter
  * None

* Return Value

The values returned are explained as follows:

| return value | description                                     |
| ------------ | ----------------------------------------------- |
| 0            | Fail to get reason for booting or unknow reason |
| 1            | Press PWRKEY to boot                            |
| 2            | Press RESET KEY to restart                      |
| 3            | Booting triggered by VBAT                       |
| 4            | Booting triggered by RTC                        |
| 5            | Booting triggered by watchdog or Abnormal boot  |
| 6            | Booting triggered by VBUS                       |
| 7            | Booting triggered by charge in                  |
| 8            | Booting from PSM wakeup                         |
| 9            | Booting by dump                                 |



###### Get the Reason for the Last Powering Down of the Module

> **Power. powerDownReason()**

It gets the reason for the last powering down of the module.

* Parameter
  * None

* Return Value

The values returned are explained as follows:

| return value | description                                                  |
| ------------ | ------------------------------------------------------------ |
| 0            | Fail to get reason for shutdown or unknow reason             |
| 1            | Press PWRKEY to shutdown                                     |
| 2            | Shutdown caused by excessive Vin voltage, exceeding the VSYS_OVER_TH threshold voltage |
| 3            | Shutdown caused by low Vin voltage                           |
| 4            | Shutdown caused by high temperature                          |
| 5            | Shutdown triggered by watchdog                               |
| 6            | VRTC voltage is lower than VRTC_MIN_TH, which triggers shutdown |


* Note

  * The BC25PA and EC200U/EC600U platform does not support this method.



###### Get Voltage of the Battery.

> **Power. getVbatt()**

It gets the voltage of the battery. Unit: mV.

* Parameter

  * None

* Return Value 

  * Integer type. Voltage value.

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

  * None

* Return Value

  * Return an object.




###### Register Callback Function

> pk.powerKeyEventRegister(usrFun)

* Parameter

| Parameter | Type     | Description                                                  |
| --------- | -------- | ------------------------------------------------------------ |
| usrFun    | function | Callback function, which is triggered when the power key button is pressed or released |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.

* Note

  * For EC600S-CN and EC600N-CN modules, when the powerkey button is pressed or released, the callback function registered by the user will be triggered;

  * The EC200U and EC600U series modules will trigger the callback function only when the powerkey button is released, and the time for the button to be pressed needs to be maintained for more than 500 ms.

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

| Constent | Description | Usage Platform                                               |
| -------- | ----------- | ------------------------------------------------------------ |
| PWM.PWM0 | PWM0        | EC600S/EC600N/EC100Y/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N |
| PWM.PWM1 | PWM1        | EC600S/EC600N/EC100Y/EC800N/EC600M/EC800M/EG912N             |
| PWM.PWM2 | PWM2        | EC600S/EC600N/EC100Y/EC800N/EC600M/EC800M/EG912N             |
| PWM.PWM3 | PWM3        | EC600S/EC600N/EC100Y/EC800N/EC600M/EC800M/EG912N             |



###### Create a PWM Object

> **from misc import PWM**
>
> **pwm = PWM(PWM.PWMn,PWM.ABOVE_xx, highTime, cycleTime)**

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| PWMn      | int  | PWM Number<br/>Note: EC100Y-CN module supports PWM0–PWM3, and the corresponding pins are as follows: <br/>PWM0 – Pin No. 19<br/>PWM1 – Pin No. 18<br/>PWM2 – Pin No. 23<br/>PWM3 – Pin No. 22<br/>Note: EC600S-CN/EC600N-CN  modules support PWM0–PWM3, and the corresponding pins are as follows: <br/>PWM0 – Pin No. 52<br/>PWM1 –Pin No. 53<br/>PWM2 – Pin No. 70<br/>PWM3 – Pin No. 69<br />Note：EC800N modules support PWM0-PWM3，and the corresponding pins are as follows：<br/>PWM0 – Pin No. 79<br/>PWM1 – Pin No. 78<br/>PWM2 – Pin No. 16<br/>PWM3 – Pin No. 49<br />Note: EC200U series module supports PWM0, and the corresponding pins are as follows: <br />PWM0 – Pin No. 135<br />Note: EC600U series module supports PWM0, and the corresponding pins are as follows:<br />PWM0 – Pin No. 70<br />Note: EC600M series module supports PWM0-PWM3, and the corresponding pins are as follows：<br/>PWM0 – Pin No. 57<br/>PWM1 – Pin No. 56<br/>PWM2 – Pin No. 70<br/>PWM3 – Pin No. 69<br />Note: EG915U series module supports PWM0, and the corresponding pins are as follows:<br />PWM0 – Pin No. 20<br />Note: EC800M series module supports PWM0-PWM3, and the corresponding pins are as follows：<br/>PWM0 – Pin No. 83<br/>PWM1 – Pin No. 78<br/>PWM2 – Pin No. 16<br/>PWM3 – Pin No. 49<br/>Note: EG912N series module supports PWM0-PWM3, and the corresponding pins are as follows：<br/>PWM0 – Pin No. 21<br/>PWM1 – Pin No. 116<br/>PWM2 – Pin No. 107<br/>PWM3 – Pin No. 92 |
| ABOVE_xx  | int  | EC600SCN/EC600N/EC800N/EC600M/EC800M/EG912N modules:<br />PWM.ABOVE_MS              Range of MS level: (0,1023]<br/>PWM.ABOVE_1US               Range of US level: (0,157]<br/>PWM.ABOVE_10US               Range of US level: (1,1575]<br/>PWM.ABOVE_BELOW_US          Range of NS level: (0,1024]<br/>EC200U/EC600U/EG915U modules:<br />PWM.ABOVE_MS            Range of MS level: (0,10]<br/>PWM.ABOVE_1US             Range of US level: (0,10000]<br/>PWM.ABOVE_10US             Range of US level: (1,10000]<br/>PWM.ABOVE_BELOW_US             Range of NS level: [100,65535] |
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

  * None

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.



###### Close PWM Output

> **pwm.close()**

It closes PWM output.

* Parameter

  * None

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.



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

| Constant | Description   | Usage Platform                                               |
| -------- | ------------- | ------------------------------------------------------------ |
| ADC.ADC0 | ADC Channel 0 | EC600S/EC600N/EC100Y/EC600U/EC200U/BC25PA/BG95M3/EC200A/EC600M/EG915U/EC800M/EG912N |
| ADC.ADC1 | ADC Channel 1 | EC600U/EC200U/EC200A/EC600M/EG915U/EC800M/EG912N             |
| ADC.ADC2 | ADC Channel 2 | EC600U/EC200U                                                |
| ADC.ADC3 | ADC Channel 3 | EC600U                                                       |



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

  * None

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.



###### Read Voltage Value of the Channel

> **adc.read(ADCn)**

It reads the voltage value of the specified channel. Unit: mV.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| ADCn      | int  | ADC Channel<br/>The corresponding pins for EC100Y-CN module are as follows:<br/>ADC0 – Pin No. 39<br/>ADC1 – Pin No. 81<br/>The corresponding pins for EC600S-CN/EC600N_CN modules are as follows<br/>ADC0 – Pin No. 19<br/>The corresponding pins for EC600M modules are as follows<br/>ADC0 – Pin No. 19<br/>ADC1 – Pin No. 20<br/>The corresponding pins for EC800N/BC25PA series module are as follows<br />ADC0 – Pin No. 9<br/>The corresponding pins for EC600U series module are as follows<br />ADC0 – Pin No. 19<br/>ADC1 – Pin No. 20<br />ADC2 – Pin No. 113<br />ADC3 – Pin No. 114<br />The corresponding pins for EC200U series module are as follows<br />ADC0 – Pin No. 45<br/>ADC1 – Pin No. 44<br />ADC2 – Pin No.43<br />The corresponding pins for EC200A series module are as follows<br/>ADC0 – Pin No. 45<br/>ADC1 – Pin No. 44<br/>The corresponding pins for BG95M3 series module are as follows<br />ADC0 – Pin No. 24<br />The corresponding pins for EG915U series module are as follows<br />ADC0 – Pin No. 24<br/>ADC1 – Pin No. 2<br/>The corresponding pins for EC800M series module are as follows<br/>ADC0 – Pin No. 9<br/>ADC1 – Pin No. 96<br/>The corresponding pins for EG912N series module are as follows<br/>ADC0 – Pin No. 24<br/>ADC1 – Pin No. 2 |

* Return Value

  * Return the voltage value of the specified channel if the execution is successful, otherwise return -1.

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

  * None

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.



##### USB

It provides USB plug detection interface.
Note : Currently only EC600S EC600N/EC800N/EC200U/EC600U platform support this function.

###### Create an USB Object

> from misc import USB
>
> usb = USB()

* Parameter

  * None

* Return Value

  * None

  

###### Get Current USB Connection Status

> usb.getStatus()

* Parameter

  * None

* Return Value

  * -1: Get status failed
  * 0: USB is not connected currently
  * 1: USB is connected



###### Register Callback Function

> usb.setCallback(usrFun)

* Parameter

| Parameter | Type     | Description                                                  |
| --------- | -------- | ------------------------------------------------------------ |
| usrFun    | function | Callback function, which will be triggered to notify the user of the current USB status when the USB is inserted or unplugged. Please note that do not perform blocking operations in the callback function. |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.

* Example

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



##### USBNET

It provides the USB network adapter function.

NOTE : Currently only EC600S EC600N/EC800N/EC200U/EC600U platform support this function.

###### Setting the USBNET working type (Take effect after restart)

USBNET.set_worktype(type)

- Parameter

  | Parameter | Type | Description                                                  |
  | --------- | ---- | ------------------------------------------------------------ |
  | type      | int  | USBNET working type<br>Type_ECM – ECM mode <br>Type_RNDIS – RNDIS mode |

- Return Value

  * Return 0 if the setting is successful, otherwise return -1.



###### Obtain the working type of USB network card (restart takes effect)

> **USBNET.get_worktype()**

* Parameter

  * None

* Return Value

  * The current network card mode is returned successfully, and the integer - 1 is returned in case of failure. Return value Description:
  
    * 1 - ECM mode
    * 3 - rndis mode



###### Get the current status of usbnet

> **USBNET.get_status()**

* Parameter

  * None

* Return Value

  * The current state of usbnet is returned successfully, and the integer - 1 is returned in case of failure.

  * Status description:

    0 - not connected <br/>
    1 - connection successful



###### Open USBNET

> **USBNET.open()**

- Parameter

  * None

- Return Value

  * Return 0 if the opening is successful, otherwise return -1.
  
  

###### Close USBNET

> **USBNET.close()**

- Parameter

  * None

- Return Value

  * Return 0 if successful, otherwise return -1.



Example

```python
from misc import USBNET
from misc import Power

#work on ECM mode default
USBNET.open()

USBNET.set_worktype(USBNET.Type_RNDIS)

#reset the module
Power.powerRestart()


#After restart
from misc import USBNET

#work on RNDIS mode
USBNET.open()
```



###### get the status of NAT enablement

> **USBNET.getNat(simid, pid)**

get the status of NAT enablement(Whether IPV6 is supported)(supported only on EC200U/EC600U)

* Parameter

|   Parameter   | Type     | Description                                           |
|   --------    | -------- | ----------------------------------------------------- |
|   simid       | int      | simid，value：0/1 ，(only SIM0 is supported now)      |
|    pid        | int      | PDP context index ,range:1-7                          |

* Return Value

success：return the status of NAT enablement
0：enabled，means:IPV6 is supported
1：disabled，means:IPV6 is not supported

failed： return -1

* Example

```python
from misc import USBNET
USBNET.getNat(0, 1)
0
```



###### set NAT

> **USBNET.setNat(simid, pid, Nat)**

set NAT，Restart takes effect (supported only on EC200U/EC600U)
( Usbnet.set_worktype () API will make the corresponding Nat value set to 1, so that the pid cannot dial up IPV6, so after close USBnet, you can use this interface to disable NAT and make IPV6 function normal)

* Parameter

|   Parameter   | Type     | Description                                           |
|   --------    | -------- | ----------------------------------------------------- |
|   simid       | int      | simid，value：0/1 ，(only SIM0 is supported now)      |
|    pid        | int      | PDP context index ,range:1-7                          |
|    Nat        | int      | Nat，value：0/1；0：IPV6 is supported；1：IPV6 is not supported |

* Return Value

Return 0 if successful, otherwise return -1

* Example

```python
USBNET.setNat(0, 1, 0)
0
```



##### Diversity antenna configuration API

> **misc.antennaSecRXOffCtrl(\*args)**

Diversity antenna configuration and query API(just supported on the 1803s platform)

* parameter

  This API is a variable parameter function ,and the number of parameters is 0 or 1：
    The number of parameters is 0(query)：misc.antennaSecRXOffCtrl()
    The number of parameters is 1(set)：misc.antennaSecRXOffCtrl(SecRXOff_set)
  
  |   Parameter   | Type     | Description                                           |
  |   --------    | -------- | ----------------------------------------------------- |
  | SecRXOff_set  | int      | range:0/1, 0:The diversity antenna is not turned off  1:Turn off the diversity antenna |

* Return Value

  * query: Return 0/1 if successful, otherwise return -1
  
  * set: Return 0 if successful, otherwise return -1

* Example

```python
import misc
misc.antennaSecRXOffCtrl() //get
0
misc.antennaSecRXOffCtrl(1) //set
0
misc.antennaSecRXOffCtrl() //get
1
```



#### modem - Related Device

Function: This module gets device information.

##### Get IMEI of the Device

> **modem.getDevImei()**

It gets IMEI of the device.

* Parameter

  * None

* Return Value
  * Return the IMEI of string type of the device if the execution is successful, otherwise return -1.
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

  * None

* Return Value

  * Return the device model of string type if the execution is successful, otherwise return -1.

* Example

```python
>>> modem.getDevModel()
'EC100Y'
```



##### Get Device Serial Number

> **modem.getDevSN()**

It gets device serial number.

* Parameter

  * None

* Return Value

  * Return the device serial number of string type if the execution is successful, otherwise return -1.

* Example

```python
>>> modem.getDevSN()
'D1Q20GM050038341P'
```



##### Get Firmware Version number

> **modem.getDevFwVersion()**

It gets the firmware version number.

* Parameter

  * None

* Return Value

  * Return the firmware version number of string type if the execution is successful, otherwise return -1.

* Example

```python
>>> modem.getDevFwVersion()
'EC100YCNAAR01A01M16_OCPU_PY'
```



##### Get Device Manufacturer ID

> **modem.getDevProductId()**

It gets device manufacturer ID.

* Parameter

  * None

* Return Value

  * Return the device manufacturer ID if the execution is successful, otherwise return -1.

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

| Constant         | Applicable Platform                                          | Description    |
| ---------------- | ------------------------------------------------------------ | -------------- |
| Pin.GPIO1        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO1          |
| Pin.GPIO2        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO2          |
| Pin.GPIO3        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO3          |
| Pin.GPIO4        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO4          |
| Pin.GPIO5        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO5          |
| Pin.GPIO6        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO6          |
| Pin.GPIO7        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO7          |
| Pin.GPIO8        | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO8          |
| Pin.GPIO9        | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO9          |
| Pin.GPIO10       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO10         |
| Pin.GPIO11       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO11         |
| Pin.GPIO12       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO12         |
| Pin.GPIO13       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO13         |
| Pin.GPIO14       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO14         |
| Pin.GPIO15       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO15         |
| Pin.GPIO16       | EC600S / EC600N / EC100Y/EC600U/EC200U/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO16         |
| Pin.GPIO17       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC800N/BC25PA/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO17         |
| Pin.GPIO18       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/EC800N/BC25PA/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO18         |
| Pin.GPIO19       | EC600S / EC600N / EC100Y/EC600U/EC200U/EC200A/EC800N/BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO19         |
| Pin.GPIO20       | EC600S / EC600N /EC600U/EC200U/EC200A/ EC800N / BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO20         |
| Pin.GPIO21       | EC600S / EC600N /EC600U/EC200U/ EC800N / BG95M3/EC600M/EG915U/EC800M/EG912N | GPIO21         |
| Pin.GPIO22       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO22         |
| Pin.GPIO23       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EG915U/EC800M/EG912N | GPIO23         |
| Pin.GPIO24       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EG915U/EC800M/EG912N | GPIO24         |
| Pin.GPIO25       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EG915U/EC800M/EG912N | GPIO25         |
| Pin.GPIO26       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EG915U/EC800M/EG912N | GPIO26         |
| Pin.GPIO27       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO27         |
| Pin.GPIO28       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO28         |
| Pin.GPIO29       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO29         |
| Pin.GPIO30       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO30         |
| Pin.GPIO31       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO31         |
| Pin.GPIO32       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO32         |
| Pin.GPIO33       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO33         |
| Pin.GPIO34       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO34         |
| Pin.GPIO35       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO35         |
| Pin.GPIO36       | EC600S / EC600N/EC600U/EC200U/EC200A/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO36         |
| Pin.GPIO37       | EC600S / EC600N/EC600U/EC200U/EC800N/EC600M/EG915U/EC800M/EG912N | GPIO37         |
| Pin.GPIO38       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG912N    | GPIO38         |
| Pin.GPIO39       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG912N    | GPIO39         |
| Pin.GPIO40       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M/EG912N    | GPIO40         |
| Pin.GPIO41       | EC600S / EC600N/EC600U/EC200U/EC600M/EG915U/EC800M           | GPIO41         |
| Pin.GPIO42       | EC600U / EC200U/EC600M/EC800M                                | GPIO42         |
| Pin.GPIO43       | EC600U / EC200U/EC200A/EC600M/EC800M                         | GPIO43         |
| Pin.GPIO44       | EC600U / EC200U/EC200A/EC600M/EC800M                         | GPIO44         |
| Pin.GPIO45       | EC600U / EC200U/EC200A/EC600M                                | GPIO45         |
| Pin.GPIO46       | EC600U / EC200U/EC200A                                       | GPIO46         |
| Pin.GPIO47       | EC200U/EC200A                                                | GPIO47         |
| Pin.IN           | --                                                           | Input mode     |
| Pin.OUT          | --                                                           | Output mode    |
| Pin.PULL_DISABLE | --                                                           | Floating mode  |
| Pin.PULL_PU      | --                                                           | Pull-up mode   |
| Pin.PULL_PD      | --                                                           | Pull-down mode |

**Corresponding Pin Number Description of GPIO**

The GPIO pin numbers provided in this document correspond to the external pin numbers of the module. For example, the GPIO1 of the EC600S-CN module corresponds to the pin number 22, which is the external pin number of the module. Uses can refer to the corresponding hardware resource to view the external pin number of the module.

###### Create a GPIO Object

> **gpio = Pin(GPIOn, direction, pullMode, level)**

* Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| GPIOn     | int  | Pin Number<br />The  corresponding pins of EC100Y-CN module are as follows (pin number is external pin number):<br />GPIO1 – Pin No. 22<br />GPIO2 – Pin No. 23<br />GPIO3 – Pin No. 38<br />GPIO4 – Pin No. 53<br />GPIO5 – Pin No. 54<br />GPIO6 – Pin No. 104<br />GPIO7 – Pin No. 105<br />GPIO8 – Pin No. 106<br />GPIO9 – Pin No. 107<br />GPIO10 – Pin No. 178<br />GPIO11 – Pin No. 195<br />GPIO12 – Pin No. 196<br />GPIO13 – Pin No. 197<br />GPIO14 – Pin No. 198<br />GPIO15 – Pin No. 199<br />GPIO16 – Pin No. 203<br />GPIO17 – Pin No. 204<br />GPIO18 – Pin No. 214<br />GPIO19 – Pin No. 215<br />The corresponding pins of EC600S-CN/EC600N-CN modules are as follows (pin number is external pin number): <br />GPIO1 – Pin No. 10<br />GPIO2 – Pin No. 11<br />GPIO3 – Pin No. 12<br />GPIO4 – Pin No. 13<br />GPIO5 – Pin No. 14<br />GPIO6 – Pin No. 15<br />GPIO7 – Pin No. 16<br />GPIO8 – Pin No. 39<br />GPIO9 – Pin No. 40<br />GPIO10 – Pin No. 48<br />GPIO11 – Pin No. 58<br />GPIO12 – Pin No. 59<br />GPIO13 – Pin No. 60<br />GPIO14 – Pin No. 61<br />GPIO15 – Pin No. 62<br/>GPIO16 – Pin No. 63<br/>GPIO17 – Pin No. 69<br/>GPIO18 – Pin No. 70<br/>GPIO19 – Pin No. 1<br/>GPIO20 – Pin No. 3<br/>GPIO21 – Pin No. 49<br/>GPIO22 – Pin No. 50<br/>GPIO23 – Pin No. 51<br/>GPIO24 – Pin No. 52<br/>GPIO25 – Pin No. 53<br/>GPIO26 – Pin No. 54<br/>GPIO27 – Pin No. 55<br/>GPIO28 – Pin No. 56<br/>GPIO29 – Pin No. 57<br />GPIO30 – Pin No. 2<br />GPIO31 – Pin No. 66<br />GPIO32 – Pin No. 65<br />GPIO33 – Pin No. 67<br />GPIO34 – Pin No. 64<br />GPIO35 – Pin No. 4<br />GPIO36 – Pin No. 31<br />GPIO37 – Pin No. 32<br />GPIO38 – Pin No. 33<br />GPIO39 – Pin No. 34<br />GPIO40 – Pin No. 71<br />GPIO41 – Pin No. 72<br />The corresponding pins of EC600M series module are as follows (pin number is external pin number)：<br />GPIO1 – Pin No. 10<br />GPIO2 – Pin No. 11<br />GPIO3 – Pin No. 12<br />GPIO4 – Pin No. 13<br />GPIO5 – Pin No. 14<br />GPIO6 – Pin No. 15<br />GPIO7 – Pin No. 16<br />GPIO8 – Pin No. 39<br />GPIO9 – Pin No. 40<br />GPIO10 – Pin No. 48<br />GPIO11 – Pin No. 58<br />GPIO12 – Pin No. 59<br />GPIO13 – Pin No. 60<br />GPIO14 – Pin No. 61<br />GPIO15 – Pin No. 62<br/>GPIO16 – Pin No. 63<br/>GPIO17 – Pin No. 69<br/>GPIO18 – Pin No. 70<br/>GPIO19 – Pin No. 1<br/>GPIO20 – Pin No. 3<br/>GPIO21 – Pin No. 49<br/>GPIO22 – Pin No. 50<br/>GPIO23 – Pin No. 51<br/>GPIO24 – Pin No. 52<br/>GPIO25 – Pin No. 53<br/>GPIO26 – Pin No. 54<br/>GPIO27 – Pin No. 55<br/>GPIO28 – Pin No. 56<br/>GPIO29 – Pin No. 57<br />GPIO30 – Pin No. 2<br />GPIO31 – Pin No. 66<br />GPIO32 – Pin No. 65<br />GPIO33 – Pin No. 67<br />GPIO34 – Pin No. 64<br />GPIO35 – Pin No. 4<br />GPIO36 – Pin No. 31<br />GPIO37 – Pin No. 32<br />GPIO38 – Pin No. 33<br />GPIO39 – Pin No. 34<br />GPIO40 – Pin No. 71<br />GPIO41 – Pin No. 72<br />GPIO42 – Pin No. 109<br />GPIO43 – Pin No. 110<br />GPIO44 – Pin No. 112<br />GPIO45 – Pin No. 111<br/>The corresponding pins of EC600U series module are as follows (pin number is external pin number): <br />GPIO1 – Pin No. 61(cannot be gpio function at the same time as GPIO31)<br />GPIO2 – Pin No. 58(cannot be gpio function at the same time as GPIO32)<br />GPIO3 – Pin No. 34(cannot be gpio function at the same time as GPIO41)<br />GPIO4 – Pin No. 60(cannot be gpio function at the same time as GPIO34)<br />GPIO5 – Pin No. 69(cannot be gpio function at the same time as GPIO35)<br />GPIO6 – Pin No. 70(cannot be gpio function at the same time as GPIO36)<br />GPIO7 – Pin No. 123(cannot be gpio function at the same time as GPIO43)<br />GPIO8 – Pin No. 118<br />GPIO9 – Pin No. 9<br />GPIO10 – Pin No. 1(cannot be gpio function at the same time as GPIO37)<br />GPIO11 – Pin No. 4(cannot be gpio function at the same time as GPIO38)<br />GPIO12 – Pin No. 3(cannot be gpio function at the same time as GPIO39)<br />GPIO13 – Pin No. 2(cannot be gpio function at the same time as GPIO40)<br />GPIO14 – Pin No. 54<br />GPIO15 – Pin No. 57<br/>GPIO16 – Pin No. 56<br/>GPIO17 – Pin No. 12<br/>GPIO18 – Pin No. 33(cannot be gpio function at the same time as GPIO42)<br/>GPIO19 – Pin No. 124(cannot be gpio function at the same time as GPIO44)<br/>GPIO20 – Pin No. 122(cannot be gpio function at the same time as GPIO45)<br/>GPIO21 – Pin No. 121(cannot be gpio function at the same time as GPIO46)<br/>GPIO22 – Pin No. 48<br/>GPIO23 – Pin No. 39<br/>GPIO24 – Pin No. 40<br/>GPIO25 – Pin No. 49<br/>GPIO26 – Pin No. 50<br/>GPIO27 – Pin No. 53<br/>GPIO28 – Pin No. 52<br/>GPIO29 – Pin No. 51<br/>GPIO30 – Pin No. 59(cannot be gpio function at the same time as GPIO33)<br/>GPIO31 – Pin No. 66(cannot be gpio function at the same time as GPIO1)<br/>GPIO32 – Pin No. 63(cannot be gpio function at the same time as GPIO2)<br/>GPIO33 – Pin No. 67(cannot be gpio function at the same time as GPIO30)<br/>GPIO34 – Pin No. 65(cannot be gpio function at the same time as GPIO4)<br/>GPIO35 – Pin No. 137(cannot be gpio function at the same time as GPIO5)<br/>GPIO36 – Pin No. 62(cannot be gpio function at the same time as GPIO6)<br/>GPIO37 – Pin No. 98(cannot be gpio function at the same time as GPIO10)<br/>GPIO38 – Pin No. 95(cannot be gpio function at the same time as GPIO11)<br/>GPIO39 – Pin No. 119(cannot be gpio function at the same time as GPIO12)<br/>GPIO40 – Pin No. 100(cannot be gpio function at the same time as GPIO13)<br/>GPIO41 – Pin No. 120(cannot be gpio function at the same time as GPIO3)<br/>GPIO42 – Pin No. 16(cannot be gpio function at the same time as GPIO18)<br/>GPIO43 – Pin No. 10(cannot be gpio function at the same time as GPIO7)<br/>GPIO44 – Pin No. 14(cannot be gpio function at the same time as GPIO19)<br/>GPIO45 – Pin No. 15(cannot be gpio function at the same time as GPIO20)<br/>GPIO46 – Pin No. 13(cannot be gpio function at the same time as GPIO21)<br/>The corresponding pins of EC200U series module are as follows (pin number is external pin number): <br />GPIO1 – Pin No. 27(cannot be gpio function at the same time as GPIO31)<br />GPIO2 – Pin No. 26(cannot be gpio function at the same time as GPIO32)<br />GPIO3 – Pin No. 24(cannot be gpio function at the same time as GPIO33)<br />GPIO4 – Pin No. 25(cannot be gpio function at the same time as GPIO34)<br />GPIO5 – Pin No. 13(cannot be gpio function at the same time as GPIO17)<br />GPIO6 – Pin No. 135(cannot be gpio function at the same time as GPIO36)<br />GPIO7 – Pin No. 136(cannot be gpio function at the same time as GPIO44)<br />GPIO8 – Pin No. 133<br />GPIO9 – Pin No. 3(cannot be gpio function at the same time as GPIO37)<br />GPIO10 – Pin No. 40(cannot be gpio function at the same time as GPIO38)<br />GPIO11 – Pin No. 37(cannot be gpio function at the same time as GPIO39)<br />GPIO12 – Pin No. 38(cannot be gpio function at the same time as GPIO40)<br />GPIO13 – Pin No. 39(cannot be gpio function at the same time as GPIO41)<br />GPIO14 – Pin No. 5<br />GPIO15 – Pin No. 141<br/>GPIO16 – Pin No. 142<br/>GPIO17 – Pin No. 121(cannot be gpio function at the same time as GPIO5)<br/>GPIO18 – Pin No. 65(cannot be gpio function at the same time as GPIO42)<br/>GPIO19 – Pin No. 64(cannot be gpio function at the same time as GPIO43)<br/>GPIO20 – Pin No. 139(cannot be gpio function at the same time as GPIO45)<br/>GPIO21 – Pin No. 126(cannot be gpio function at the same time as GPIO46)<br/>GPIO22 – Pin No. 127(cannot be gpio function at the same time as GPIO47)<br/>GPIO23 – Pin No. 33<br/>GPIO24 – Pin No. 31<br/>GPIO25 – Pin No. 30<br/>GPIO26 – Pin No. 29<br/>GPIO27 – Pin No. 28<br/>GPIO28 – Pin No. 1<br/>GPIO29 – Pin No. 2<br/>GPIO30 – Pin No. 4<br/>GPIO31 – Pin No. 125(cannot be gpio function at the same time as GPIO1)<br/>GPIO32 – Pin No. 124(cannot be gpio function at the same time as GPIO2)<br/>GPIO33 – Pin No. 123(cannot be gpio function at the same time as GPIO3)<br/>GPIO34 – Pin No. 122(cannot be gpio function at the same time as GPIO4)<br/>GPIO35 – Pin No. 42<br/>GPIO36 – Pin No. 119(cannot be gpio function at the same time as GPIO6)<br/>GPIO37 – Pin No. 134(cannot be gpio function at the same time as GPIO9)<br/>GPIO38 – Pin No. 132(cannot be gpio function at the same time as GPIO10)<br/>GPIO39 – Pin No. 131(cannot be gpio function at the same time as GPIO11)<br/>GPIO40 – Pin No. 130(cannot be gpio function at the same time as GPIO12)<br/>GPIO41 – Pin No. 129(cannot be gpio function at the same time as GPIO13)<br/>GPIO42 – Pin No. 61(cannot be gpio function at the same time as GPIO18)<br/>GPIO43 – Pin No. 62(cannot be gpio function at the same time as GPIO19)<br/>GPIO44 – Pin No. 63(cannot be gpio function at the same time as GPIO7)<br/>GPIO45 – Pin No. 66(cannot be gpio function at the same time as GPIO20)<br/>GPIO46 – Pin No. 6(cannot be gpio function at the same time as GPIO21)<br/>GPIO47 – Pin No. 23(cannot be gpio function at the same time as GPIO22)<br/>The corresponding pins of EC200A series module are as follows (pin number is external pin number): <br />GPIO1 – Pin No. 27<br />GPIO2 – Pin No. 26<br />GPIO3 – Pin No.24<br />GPIO4 – Pin No.25<br />GPIO5 – Pin No.5<br />GPIO6 – Pin No.135<br />GPIO7 – Pin No.136<br />GPIO9 – Pin No. 3<br />GPIO10 – Pin No. 40<br />GPIO11 – Pin No. 37<br />GPIO12 – Pin No. 38<br />GPIO13 – Pin No. 39<br />GPIO18 – Pin No. 65<br />GPIO19 – Pin No. 64<br />GPIO20 – Pin No. 139<br />GPIO22 – Pin No. 127<br />GPIO28 – Pin No. 1<br />GPIO29 – Pin No. 2<br />GPIO30 – Pin No. 4<br />GPIO35 – Pin No. 42<br />GPIO36 – Pin No. 119<br />GPIO43 – Pin No. 62<br />GPIO44 – Pin No. 63<br />GPIO45 – Pin No. 66<br />GPIO46 – Pin No. 6<br />GPIO47 – Pin No. 23<br/>The corresponding pins of EC800NCN series module are as follows (pin number is external pin number): <br />GPIO1 – Pin No. 30<br />GPIO2 – Pin No. 31<br />GPIO3 – Pin No. 32<br />GPIO4 – Pin No. 33<br />GPIO5 – Pin No. 49<br />GPIO6 – Pin No. 50<br />GPIO7 – Pin No. 51<br />GPIO8 – Pin No. 52<br />GPIO9 – Pin No. 53<br />GPIO10 – Pin No. 54<br />GPIO11 – Pin No. 55<br />GPIO12 – Pin No. 56<br />GPIO13 – Pin No. 57<br />GPIO14 – Pin No. 58<br />GPIO15 – Pin No. 80<br/>GPIO16 – Pin No. 81<br/>GPIO17 – Pin No. 76<br/>GPIO18 – Pin No. 77<br/>GPIO19 – Pin No. 82<br/>GPIO20 – Pin No. 83<br/>GPIO21 – Pin No. 86<br/>GPIO22 – Pin No. 87<br/>GPIO23 – Pin No. 66<br/>GPIO24 – Pin No. 67<br/>GPIO25 – Pin No. 17<br/>GPIO26 – Pin No. 18<br/>GPIO27 – Pin No. 19<br/>GPIO28 – Pin No. 20<br/>GPIO29 – Pin No. 21<br />GPIO30 – Pin No. 22<br />GPIO31 – Pin No. 23<br />GPIO32 – Pin No. 28<br />GPIO33 – Pin No. 29<br />GPIO34 – Pin No. 38<br />GPIO35 – Pin No. 39<br />GPIO36 – Pin No. 16<br />GPIO37 – Pin No. 78<br />The pin correspondence of BC25PA platform is as follows (pin numbers are external pin numbers):<br />GPIO1 – Pin No. 3<br />GPIO2 – Pin No. 4<br />GPIO3 – Pin No. 5<br />GPIO4 – Pin No. 6<br />GPIO5 – Pin No. 16<br />GPIO6 – Pin No. 20<br />GPIO7 – Pin No. 21<br />GPIO8 – Pin No. 22<br />GPIO9 – Pin No. 23<br />GPIO10 – Pin No. 25<br />GPIO11 – Pin No. 28<br />GPIO12 – Pin No. 29<br />GPIO13 – Pin No. 30<br />GPIO14 – Pin No. 31<br />GPIO15 – Pin No. 32<br/>GPIO16 – Pin No. 33<br/>GPIO17 – Pin No. 2<br/>GPIO18 – Pin No. 8<br/>The pin correspondence of BG95M3 platform is as follows (pin numbers are external pin numbers):<br />GPIO1 – Pin No. 4<br />GPIO2 – Pin No. 5<br />GPIO3 – Pin No. 6<br />GPIO4 – Pin No. 7<br />GPIO5 – Pin No. 18<br />GPIO6 – Pin No. 19<br />GPIO7 – Pin No. 22<br />GPIO8 – Pin No. 23<br />GPIO9 – Pin No. 25<br />GPIO10 – Pin No. 26<br />GPIO11 – Pin No. 27<br />GPIO12 – Pin No. 28<br />GPIO13 – Pin No. 40<br />GPIO14 – Pin No. 41<br />GPIO15 – Pin No. 64<br/>GPIO16 – Pin No. 65<br/>GPIO17 – Pin No. 66<br />GPIO18 – Pin No. 85<br />GPIO19 – Pin No. 86<br />GPIO20 – Pin No. 87<br />GPIO21 – Pin No. 88<br />The pin correspondence of EG915U platform is as follows (pin numbers are external pin numbers):<br />GPIO1 – Pin No.4(cannot be gpio function at the same time as GPIO41)<br />GPIO2 – Pin No.5(cannot be gpio function at the same time as GPIO36)<br />GPIO3 – Pin No.6(cannot be gpio function at the same time as GPIO35)<br />GPIO4 – Pin No.7(cannot be gpio function at the same time as GPIO24)<br />GPIO5 – Pin No.18<br />GPIO6 – Pin No.19<br />GPIO7 – Pin No.1(cannot be gpio function at the same time as GPIO37)<br />GPIO8 – Pin No.38<br />GPIO9 – Pin No.25<br />GPIO10 – Pin No.26<br />GPIO11 – Pin No.27(cannot be gpio function at the same time as GPIO32)<br />GPIO12 – Pin No.28(cannot be gpio function at the same time as GPIO31)<br />GPIO13 – Pin No.40<br />GPIO14 – Pin No.41<br />GPIO15 – Pin No.64<br/>GPIO16 – Pin No.20(cannot be gpio function at the same time as GPIO30)<br/>GPIO17 – Pin No.21<br/>GPIO18 – Pin No.85<br/>GPIO19 – Pin No.86<br/>GPIO20 – Pin No.30<br/>GPIO21 – Pin No.88<br/>GPIO22 – Pin No.36(cannot be gpio function at the same time as GPIO40)<br/>GPIO23 – Pin No.37(cannot be gpio function at the same time as GPIO38)<br/>GPIO24 – Pin No.16(cannot be gpio function at the same time as GPIO4)<br/>GPIO25 – Pin No.39<br/>GPIO26 – Pin No.42(cannot be gpio function at the same time as GPIO27)<br/>GPIO27 – Pin No.78(cannot be gpio function at the same time as GPIO26)<br/>GPIO28 – Pin No.83(cannot be gpio function at the same time as GPIO33)<br/>GPIO29 – Pin No.84<br />GPIO30 – Pin No.92(cannot be gpio function at the same time as GPIO16)<br />GPIO31 – Pin No.95(cannot be gpio function at the same time as GPIO12)<br />GPIO32 – Pin No.97(cannot be gpio function at the same time as GPIO11)<br />GPIO33 – Pin No.98(cannot be gpio function at the same time as GPIO28)<br />GPIO34 – Pin No.104<br />GPIO35 – Pin No.105(cannot be gpio function at the same time as GPIO3)<br />GPIO36 – Pin No.106(cannot be gpio function at the same time as GPIO2)<br />GPIO37 – Pin No.108(cannot be gpio function at the same time as GPIO4)<br />GPIO38 – Pin No.111(cannot be gpio function at the same time as GPIO23)<br />GPIO39 – Pin No.114<br />GPIO40 – Pin No.115(cannot be gpio function at the same time as GPIO22)<br />GPIO41 – Pin No.116(cannot be gpio function at the same time as GPIO1)<br />The corresponding pins of EC800M series module are as follows (pin number is external pin number)：<br />GPIO1 – Pin No. 30<br />GPIO2 – Pin No. 31<br />GPIO3 – Pin No. 32<br />GPIO4 – Pin No. 33<br />GPIO5 – Pin No. 49<br />GPIO6 – Pin No. 50<br />GPIO7 – Pin No. 51<br />GPIO8 – Pin No. 52<br />GPIO9 – Pin No. 53<br />GPIO10 – Pin No. 54<br />GPIO11 – Pin No. 55<br />GPIO12 – Pin No. 56<br />GPIO13 – Pin No. 57<br />GPIO14 – Pin No. 58<br />GPIO15 – Pin No. 80<br/>GPIO16 – Pin No. 81<br/>GPIO17 – Pin No. 76<br/>GPIO18 – Pin No. 77<br/>GPIO19 – Pin No. 82<br/>GPIO20 – Pin No. 83<br/>GPIO21 – Pin No. 86<br/>GPIO22 – Pin No. 87<br/>GPIO23 – Pin No. 66<br/>GPIO24 – Pin No. 67<br/>GPIO25 – Pin No. 17<br/>GPIO26 – Pin No. 18<br/>GPIO27 – Pin No. 19<br/>GPIO28 – Pin No. 20<br/>GPIO29 – Pin No. 21<br />GPIO30 – Pin No. 22<br />GPIO31 – Pin No. 23<br />GPIO32 – Pin No. 28<br />GPIO33 – Pin No. 29<br />GPIO34 – Pin No. 38<br />GPIO35 – Pin No. 39<br />GPIO36 – Pin No. 16<br />GPIO37 – Pin No. 78<br />GPIO38 – Pin No. 68<br />GPIO39 – Pin No. 39<br />GPIO40 – Pin No. 74<br />GPIO41 – Pin No. 75<br />GPIO42 – Pin No. 84<br />GPIO43 – Pin No. 85<br />GPIO44 – Pin No. 25<br />The corresponding pins of EG912N series module are as follows (pin number is external pin number)：<br />GPIO1 – Pin No.4<br />GPIO2 – Pin No.5<br />GPIO3 – Pin No.6<br />GPIO4 – Pin No.7<br />GPIO5 – Pin No.18<br />GPIO6 – Pin No.19<br />GPIO7 – Pin No.1<br />GPIO8 – Pin No.16<br />GPIO9 – Pin No.25<br />GPIO10 – Pin No.26<br />GPIO11 – Pin No.27<br />GPIO12 – Pin No.28<br />GPIO13 – Pin No.40<br/>GPIO14 – Pin No.41<br/>GPIO15 – Pin No.64<br/>GPIO16 – Pin No.20<br/>GPIO17 – Pin No.21<br/>GPIO18 – Pin No.30<br/>GPIO19 – Pin No.34<br/>GPIO20 – Pin No.35<br/>GPIO21 – Pin No.36<br/>GPIO22 – Pin No.37<br/>GPIO23 – Pin No.38<br/>GPIO24 – Pin No.39<br/>GPIO25 – Pin No.42<br />GPIO26 – Pin No.78<br />GPIO27 – Pin No.83<br />GPIO28 – Pin No.92<br />GPIO29 – Pin No.95<br />GPIO30 – Pin No.96<br />GPIO31 – Pin No.97<br />GPIO32 – Pin No.98<br />GPIO33 – Pin No.103<br />GPIO34 – Pin No.104<br />GPIO35 – Pin No.105<br />GPIO36 – Pin No.106<br />GPIO37 – Pin No.107<br />GPIO38 – Pin No.114<br />GPIO39 – Pin No.115<br />GPIO40 – Pin No.116 |
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

  * None

* Return Value

  * Pin level. 0 indicates low level; 1 indicates high level.



###### Set Pin Level

> **Pin.write(value)**

It sets the pin level, you need to ensure that the pin is in output mode before setting it to the high or low level.

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| value     | int  | 0 - When the pin is in output mode, set it to output low;  <br />1 - When the pin is in output mode, set it to output high |

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.

* Example

```python
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
>>> gpio1.write(1)
0
>>> gpio1.read()
1
```



###### Set input / output mode

> **Pin.set_dir(value)**

Set the input / output mode of pin pin GPIO.

* Parameter

|Parameter | type | description|
| ----- | ---- | ------------------------------------------------------------ |
|Value | int | 0 - (pin. In) is set as the input mode<br/> 1 - (pin. Out) set to output mode|

* Return Value

  * The integer value 0 will be returned if the setting is successful, and other values will be returned if the setting is failed.

* Examples

```python
>>> from machine import Pin
>>> gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)
>>> gpio1.write(1)
0
>>> gpio1.set_dir(Pin.IN)
0
```

###### Get input / output mode

> **Pin.get_dir()**

Get the input / output mode of pin pin.

* Parameter

  * None

* Return Value

  * Pin mode, 0-input mode, 1-output mode.



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
| UART.UART4 | UART4       |



###### Create an UART Object

> **uart = UART(UART.UARTn, buadrate, databits, parity, stopbits, flowctl)**

* Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| UARTn     | int  | Functions of UARTn are as follows: <br />UART0 - DEBUG PORT<br />UART1 – BT PORT<br />UART2 – MAIN PORT<br />UART3 – USB CDC PORT(BG95M3 platform not supported)<br />UART4 – STDOUT PORT(only supports EC200U/EC600U/EG915U) |
| buadrate  | int  | Baud rate, common baud rates are supported, such as 4800, 9600, 19200, 38400, 57600, 115200, 230400, etc. |
| databits  | int  | Data bit (5–8)                                               |
| parity    | int  | Parity check (0 – NONE，1 – EVEN，2 - ODD)                   |
| stopbits  | int  | Stop bit (1–2)                                               |
| flowctl   | int  | Hardware control flow (0 – FC_NONE， 1 – FC_HW）             |

* Pin Correspondence

| platform      |                                                              |
| ------------- | :----------------------------------------------------------- |
| EC600U        | uart1:<br />TX: Pin number 124<br />RX: Pin number 123<br />uart2:<br />TX:Pin number 32<br />RX:Pin number 31<br />uart4:<br />TX:Pin number 103<br />RX:Pin number 104 |
| EC200U        | uart1:<br />TX: Pin number 138<br />RX: Pin number 137<br />uart2:<br />TX:Pin number 67<br />RX:Pin number 68<br />uart4:<br />TX:Pin number 82<br />RX:Pin number 81 |
| EC200A        | uart1:<br />TX: Pin number 63<br />RX: Pin number 66<br />uart2:<br />TX: Pin number 67<br />RX: Pin number 68 |
| EC600S/EC600N | uart0:<br />TX: Pin number 71<br />RX: Pin number 72<br />uart1:<br />TX: Pin number 3<br />RX: Pin number 2<br />uart2:<br />TX:Pin number 32<br />RX:Pin number 31 |
| EC100Y        | uart0:<br />TX: Pin number 21<br />RX:Pin number 20<br />uart1:<br />TX: Pin number 27<br />RX: Pin number 28<br />uart2:<br />TX:Pin number 50<br />RX:Pin number 49 |
| EC800N        | uart0:<br />TX: Pin number 39<br />RX: Pin number 38<br />uart1:<br />TX: Pin number 50<br />RX: Pin number 51<br />uart2:<br />TX:Pin number 18<br />RX:Pin number 17 |
| BC25PA        | uart1:<br />TX: Pin number 29<br />RX: Pin number 28         |
| BG95M3        | uart0:<br />TX: Pin number 23<br />RX: Pin number 22<br />uart1:<br />TX:Pin number 27<br />RX:Pin number 28<br />uart2:<br />TX: Pin number 64<br />RX: Pin number 65 |
| EC600M        | uart0:<br />TX: Pin number 71<br />RX: Pin number 72<br />uart1(Turn off flow control):<br />TX: Pin number 3<br />RX: Pin number 2<br />uart1(Turn on flow control):<br />TX: Pin number 33<br />RX: Pin number 34<br />uart2:<br />TX:Pin number 32<br />RX:Pin number 31 |
| EG915U        | uart1:<br />TX: Pin number 27<br />RX: Pin number 28<br />uart2:<br />TX:Pin number 35<br />RX:Pin number 34<br />uart4:<br />TX:Pin number 19<br />RX:Pin number 18 |
| EC800M        | uart0:<br />TX: Pin number 39<br />RX: Pin number 38<br />uart1(Turn off flow control):<br />TX: Pin number 50<br />RX: Pin number 51<br />uart1(Turn on flow control):<br />TX: Pin number 22<br />RX: Pin number 23<br />Note: EC800MCN_GA uart1 is not available<br />uart2:<br />TX:Pin number 18<br />RX:Pin number 17 |
| EG912N        | uart0:<br />TX: Pin number 23<br />RX: Pin number 22<br />uart1(Turn off flow control):<br />TX: Pin number 27<br />RX: Pin number 28<br />uart1(Turn on flow control):<br />TX: Pin number 36<br />RX: Pin number 37<br />uart2:<br />TX:Pin number 34<br />RX:Pin number 35 |

* Example

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
```



###### Get the Size of Unread Data in the Received Buffer

> **uart.any()**

It returns the size of unread data in the received buffer.

* Parameter

  * None

* Return Value

  * Return the size of unread data in the received buffer.

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

  * Return the read data.



###### Send Data to UART

> **uart.write(data)**

It sends data to UART.

* Parameter

| Parameter | Type   | Description        |
| --------- | ------ | ------------------ |
| data      | buf/string | Data has been sent |

* Return Value

  * Return the number of bytes has been sent.



###### Close UART

> **uart.close()**

It closes UART.

* Parameter

  * None

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.



###### Control 485 communication direction

> **uart.control_485(UART.GPIOn, direction)**

Before and after the serial port sends data, pull up and down the specified GPIO to indicate the direction of 485 communication.

- Parameter

| Parameter      | Type | Description                                                         |
| --------- | ---- | ------------------------------------------------------------ |
| GPIOn     | int  | For the GPIO pin number to be controlled, refer to the definition of pin module                      |
| direction | int  | 1 - Indicates that the pin level changes as follows: the serial port pulls high from low before sending data, and then pulls low from high after sending data<br />0 - Indicates that the pin level changes as follows: the serial port pulls low from high before sending data, and then pulls high from low after sending data |

- Return Value

  * Return 0 if the execution is successful, otherwise return -1.。

* Note

  * The BC25PA platform does not support this method.
  
- Example

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
>>> uart1.control_485(UART.GPIO24, 1)
```



###### Set serial port data callback

> **uart.set_callback(fun)**

After the serial port receives the data, it will execute the callback.

- Parameter

|Parameter | type | description|
| ---- | -------- | ------------------------------------------------------------ |
|Fun | function | serial port receiving data callback [result, port, Num] <br/> result: receiving interface (0: success, others: failure) <br/> port: receiving port <br/> num: how much data is returned|

- Return Value

  * The integer 0 is returned successfully, and the integer - 1 is returned in case of failure.

- Examples

```python
>>> from machine import UART
>>> uart1 = UART(UART.UART1, 115200, 8, 0, 1, 0)
>>> 
>>>def uart_call(para):
>>>     print(para)
>>> uart1.set_callback(uart_call)
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
PROJECT_VERSION = "1.0.1"

'''
 * Parameter1: Port
        Note: UARTn functions of EC100Y-CN and EC600S-CN modules are as follows:
        UART0 - DEBUG PORT
        UART1 – BT PORT
        UART2 – MAIN PORT
        UART3 – USB CDC PORT
 * Parameter2: Baud rate
 * Parameter3: data bits  （5 ~ 8）
 * Parameter4: Parity (0：NONE  1：EVEN  2：ODD) 
 * Parameter5：stop bits (1–2) 
 * Parameter6：flow control (0: FC_NONE  1：FC_HW) 
'''


# Set the log output level
log.basicConfig(level=log.INFO)
uart_log = log.getLogger("UART")

class Example_uart(object):
    def __init__(self, no=UART.UART2, bate=115200, data_bits=8, parity=0, stop_bits=1, flow_control=0):
        self.uart = UART(no, bate, data_bits, parity, stop_bits, flow_control)
        self.uart.set_callback(self.callback)


    def callback(self, para):
        uart_log.info("call para:{}".format(para))
        if(0 == para[0]):
            self.uartRead(para[2])

    
    def uartWrite(self, msg):
        uart_log.info("write msg:{}".format(msg))
        self.uart.write(msg)

    def uartRead(self, len):
        msg = self.uart.read(len)
        utf8_msg = msg.decode()
        uart_log.info("UartRead msg: {}".format(utf8_msg))
        return utf8_msg

    def uartWrite_test(self):
        for i in range(10):
            write_msg = "Hello count={}".format(i)
            self.uartWrite(write_msg)
            utime.sleep(1)

if __name__ == "__main__":
    uart_test = Example_uart()
    uart_test.uartWrite_test()
    

# 运行结果示例
'''
INFO:UART:write msg:Hello count=0
INFO:UART:write msg:Hello count=1
INFO:UART:write msg:Hello count=2
INFO:UART:write msg:Hello count=3
INFO:UART:write msg:Hello count=4
INFO:UART:write msg:Hello count=5
INFO:UART:write msg:Hello count=6
INFO:UART:write msg:Hello count=7
INFO:UART:write msg:Hello count=8
INFO:UART:write msg:Hello count=9

INFO:UART:call para:[0, 2, 15]
INFO:UART:UartRead msg: my name is XXX


'''

```



##### Timer

Function: Hardware timer

Note when using this timer: Timer 0-3, each can only perform one task at the same time, and multiple objects cannot use the same timer.



###### Constant description

|Constant | description|
| -------------- | -------------------------- |
| Timer. Timer0 | timer 0|
| Timer. Timer1 | timer 1|
| Timer. Timer2 | timer 2|
| Timer. Timer3 | timer 3|
| Timer. ONE_ Shot | single mode, the timer only executes once|
| Timer. Periodic | cycle mode, timer cycle execution|



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

  * Return 0 if the execution is successful, otherwise return -1.

* Example

```python
//Note when using this timer: Timer 0–3, each can only perform one task at the same time, and multiple objects cannot use the same timer.
>>> def fun(args):
        print(“###timer callback function###”)
>>> timer1.start(period=1000, mode=timer1.PERIODIC, callback=fun)
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

  * None

* Return Value

  * Return 0 if the execution is successful, otherwise return -1.



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
# Note: EC100Y-CN module supports Timer0 ~ Timer3
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



###### Create ExtInt Object

> **extint = ExtInt(GPIOn, mode, pull, callback)**

* Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| GPIOn     | int  | The GPIO Pin number to control refer to the Pin module definition( BG95M3 platform besides)<br />The pin correspondence of BG95M3 platform is as follows (pin numbers are external pin numbers):<br />GPIO2 – Pin number 5<br />GPIO3 – Pin number 6<br />GPIO6 – Pin number 19<br />GPIO7 – Pin number 22<br />GPIO8 – Pin number 23<br />GPIO9 – Pin number 25<br />GPIO11 – Pin number 27<br />GPIO12 – Pin number 28<br />GPIO14 – Pin number 41<br />GPIO16 – Pin number 65<br/>GPIO17 – Pin number 66<br />GPIO18 – Pin number 85<br />GPIO19 – Pin number 86<br />GPIO20 – Pin number 87<br />GPIO21 – Pin number 88 |
| mode      | int  | Set the trigger method<br /> IRQ_RISING – Rising edge trigger<br /> IRQ_FALLING – Falling edge trigger<br /> IRQ_RISING_FALLING – Rising and falling edge trigger |
| pull      | int  | PULL_DISABLE – Floating mode<br />PULL_PU – Pull-up mode<br />PULL_PD  – Pull-down mode |
| callback  | int  | Interrupt trigger callback function<br />The return parameter is a tuple of length 2<br />Args[0]: GPIO number<br />Args[1]: trigger edge (0: rising edge 1: falling edge) |

* Example

```python
>>> from machine import ExtInt
>>> def fun(args):
        print('### interrupt  {} ###'.format(args)) #Args[0]: GPIO number args[1]: rising edge or falling edge
>>> extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
```




###### Enable Interrupt

> **extint.enable()**

It enables external interrupt of the extint object, when the interrupt pin receives a rising or falling edge signal, it calls callback function to execute. 

* Parameter

  * None

* Return Value

  * 0	Successful execution.
  * -1 Failed execution.



###### Disable Interrupt

> **extint.disable()**

It disables the interrupt associated with the extint object. 

* Parameter

  * None

* Return Value

  * 0	Successful execution.
  * -1 Failed execution.



###### Read Row Number of the Pin Map

> **extint.line()**

It returns the row number of the pin map. 

* Parameter

  * None

* Return Value

  * Row number of the pin map. 

* Example

```python
>>> extint = ExtInt(ExtInt.GPIO1, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
>>> extint.line()
32
```



###### Number of read interrupts

> **extint.read_count(is_reset)**

Returns the number of times an interrupt was triggered.

* Parameter

|Parameter | type | description|
| -------- | ---- | ---------------------------------------------- |
| is_ Reset | int | reset count after reading <br/> 0: do not reset <br/> 1: reset|

* Return Value

  * List [rising_count, falling_count]
  * ​       rising_count:   Rising trigger times
  * ​       falling_count:  Fall trigger times



###### Clear interrupts

> **extint.count_reset()**

Number of times to clear the trigger interrupt.

* Parameter

  * None

* Return Value

  * 0: successful
  * Other: failed

###### Get Pin Level

> **extint.read_level()**

It gets pin level.

* Parameter

  * None

* Return Value

  * Pin level. 0 indicates low level; 1 indicates high level

##### RTC

Class function: It provides methods to get and set RTC time. For bc25pa platform, it can wake up the module from deep sleep or software shutdown.

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
| month       | int  | Month, range: 1 ~ 12.                                          |
| day         | int  | Day, range:1 ~ 31.                                             |
| week        | int  | Week, when setting the time, this parameter does not work, reserved; when getting the time, this parameter is valid. |
| hour        | int  | volume_up hour, range: 0 ~ 23.                                 |
| minute      | int  | *content_copy* minute, range:0 ~ 59.                           |
| second      | int  | Second, range: 0 ~ 59.                                         |
| microsecond | int  | *share* microsecond, reserved, set to 0 when setting the time. |

* Return Value

  * When getting the time, return a tuple containing the date and time in the following format: 

    `[year, month, day, week, hour, minute, second, microsecond]`

  0	Successful execution.

  -1 Failed execution.

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

###### Set RTC expiration time

Support platform ec600u/ec200u/ec600n/ec800n/bc25

> **rtc.set_alarm(data_e)**

Set the RTC expiration time. When the expiration time is reached, the registered callback function will be called

* Parameter
| Parameter   | Type | Description                                   |
| ----------- | ---- | ------------------------------------------------------------ |
| year        | int  | year                                                           |
| month       | int  | month,Range1 ~ 12                                                 |
| day         | int  | day,Range1 ~ 31                                                 |
| week        | int  | week,Range0 ~ 6,Where 0 means Sunday and 1 ~ 6 means Monday to Saturday respectively. When setting time,this parameter does not work and is reserved. This parameter is valid when getting time |
| hour        | int  | hour,Range0 ~ 23                                                 |
| minute      | int  | minute,Range0 ~ 59                                                 |
| second      | int  | second,Range0 ~ 59                                                 |
| microsecond | int  | microsecond,The parameter is reserved and not used yet. When setting the time, the parameter can be written as 0            |

* Return Value

  0	Successful execution.

  -1	Failed execution.

* Example
```python
>>> data_e=rtc.datetime()
>>> data_l=list(data_e)
>>> data_l[6] +=30				
>>> data_e=tuple(data_l)
>>> rtc.set_alarm(data_e)
0
```


###### Register RTC alarm callback

Support platform ec600u/ec200u/ec600n/ec800n/bc25
Note:When RTC expiration time callback function is set (for BC25PA platform, if it is recovered from deep sleep or software shutdown, calling this function will immediately call usrfun once)

> rtc.register_callback(fun)

Register RTC alarm callback handler

* Parameter

|Parameter | type | description|
| ---- | -------- | --------------------- |
|Fun | function | RTC alarm callback processing function|

* Return Value

  * The integer value 0 is returned after successful registration, and the integer value - 1 is returned after failed registration.



###### Switch RTC alarm function

Support platform ec600u/ec200u/ec600n/ec800n/bc25
Note:The timer can be started only when the callback function is set (bc25pa platform)

> rtc.enable_alarm(on_off)

Turn on/off RTC alarm function

* Parameter

|Parameter | type | description|
| ------ | ---- | ---------------------------------------- |
| on_ Off | int | 1 - turn on RTC alarm function; 0 - turn off RTC alarm function|

* Return Value

  * An integer value of 0 is returned when opening / closing is successful, and an integer value of - 1 is returned when opening / closing is failed.



- Examples

```python
from machine import RTC
rtc = RTC()
def callback(args):
   print('RTC alarm')

rtc.register_callback(callback)
rtc.set_alarm([2021, 7, 9, 5, 12, 30, 0, 0])
rtc.enable_alarm(1)
```

* Note

  * ec600u/ec200u platform supports automatic startup, that is, after setting the alarm function, the module will be shut down. After the alarm time is up, it can be started automatically. This feature is not supported on other platforms.



##### I2C

Class function: A two-wire protocol used for communication between devices. 

###### Constant Description 

| Constant          |                             | Applicable Platform         |
| ----------------- | --------------------------- | --------------------------- |
| I2C.I2C0          | I2C channel index number: 0 | EC100Y/EC600U/EC200U/EC200A/BC25PA/EC800N/BG95M3/EC600M/EG915U/EC800M |
| I2C.I2C1          | I2C channel index number: 1 | EC600S/EC600N/EC600U/EC200U/BC25PA/BG95M3/EC600M/EG915U/EC800M/EG912N |
| I2C.I2C2 | I2C channel index number: 2 | BG95M3/EC600M |
| I2C.STANDARD_MODE | Standard mode               |                             |
| I2C.FAST_MODE     | Fast mode                   |                             |



###### Create I2C Object

> **from machine import I2C**
>
> **i2c_obj = I2C(I2Cn,  MODE)**

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| I2Cn      | int  | I2C channel index number:<br />I2C.I2C0 : 0  <br />I2C.I2C1 : 1 <br />I2C.I2C2 : 2 |
| MODE      | int  | I2C working mode:<br />I2C.STANDARD_MODE : 0 Standard mode<br />I2C.FAST_MODE ： 1 Fast mode |

- Pin Correspondence

| Platform      |                                                              |
| ------------- | ------------------------------------------------------------ |
| EC600U        | I2C0:<br />SCL: Pin number 11<br />SDA: Pin number 12<br />I2C1:<br />SCL: Pin number 57<br />SDA: Pin number 56 |
| EC200U        | I2C0:<br />SCL: Pin number 41<br />SDA: Pin number 42<br />I2C1:<br />SCL:Pin number 141<br />SDA:Pin number 142 |
| EC200A        | I2C0:<br />SCL: Pin number 41<br />SDA: Pin number 42        |
| EC600S/EC600N | I2C1:<br />SCL: Pin number 57<br />SDA: Pin number 56        |
| EC100Y        | I2C0:<br />SCL: Pin number 57<br />SDA: Pin number 56        |
| BC25PA        | I2C0:<br />SCL: Pin number 23<br />SDA: Pin number 22<br />I2C1:<br />SCL: Pin number 20<br />SDA: Pin number 21 |
| EC800N        | I2C0:<br />SCL:Pin number 67<br />SDA:Pin number 66          |
| BG95M3        | I2C0:<br />SCL: Pin number 18<br />SDA: Pin number 19<br />I2C1:<br />SCL:Pin number 40<br />SDA:Pin number 41<br />I2C2:<br />SCL:Pin number 26<br />SDA:Pin number 25 |
| EC600M        | I2C0:<br />SCL: Pin number 9<br />SDA: Pin number 64<br />I2C1:<br />SCL:Pin number 57<br />SDA:Pin number 56<br />I2C2:<br />SCL:Pin number 67<br />SDA:Pin number 65 |
| EG915U        | I2C0:<br />SCL: Pin number 103<br />SDA: Pin number 114<br />I2C1:<br />SCL:Pin number 40<br />SDA:Pin number 41 |
| EC800M        | I2C0:<br />SCL: Pin number 67<br />SDA: Pin number 66<br />I2C1:<br />SCL:Pin number 68<br />SDA:Pin number 69 |
| EG912N        | I2C1:<br />SCL:Pin number 40<br />SDA:Pin number 41          |

- Exmaple

```python
from machine import I2C

i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # Return i2c object
```



###### Read Data

> **I2C.read(slaveaddress, addr,addr_len, r_data, datalen, delay)**

It reads data from the I2C bus. 

* Parameter

| Parameter    | Type      | Description                                        |
| ------------ | --------- | -------------------------------------------------- |
| slaveaddress | int       | I2C device address.                                |
| addr         | bytearray | I2C register address.                              |
| addr_len     | int       | Length of register address.                        |
| r_data       | bytearray | Byte array of received data.                       |
| datalen      | int       | Length of byte array.                              |
| delay        | int       | Delay, buffer time for data conversion (Unit: ms). |

* Return Value

  * 0	Successful execution.
  * -1 Failed execution



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

  * 0	Successful execution.
  * -1 Failed execution



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
    WHO_AM_I = bytearray([0x02, 0])

    data = bytearray([0x12, 0])   # Enter the corresponding command 
    i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # Return i2c object 
    i2c_obj.write(I2C_SLAVE_ADDR, WHO_AM_I, 1, data, 2) # Write data

    r_data = bytearray(2)  # Create a byte array of received data of length 2 
    i2c_obj.read(I2C_SLAVE_ADDR, WHO_AM_I, 1, r_data, 2, 0)   # read
    i2c_log.info(r_data[0])
    i2c_log.info(r_data[1])


```

##### I2C_simulation

Class function: used for GPIO simulation standard I2C protocol.

Except for creating objects, other operations (reading and writing) are consistent with I2C


###### Create I2C_ Simulation object

> **from machine import I2C_simulation**
>
> **i2c_obj = I2C_simulation(GPIO_clk,  GPIO_sda, CLK)**

* Parameter description

|Parameter | type | description|
| -------- | ---- | ----------------------------------------------------- |
| GPIO_ CLK pin of CLK | int | I2C (GPIO pin number to be controlled, refer to the definition of pin module)|
| GPIO_ SDA pin of SDA | int | I2C (GPIO pin number to be controlled, refer to the definition of pin module)|
|Frequency of CLK | int | I2C (01000000hz]|

- Examples

```python
from machine import I2C_simulation

i2c_obj = I2C_simulation(I2C_simulation.GPIO10, I2C_simulation.GPIO11, 300)  #Return I2C object
```



###### Read data

> **I2C_simulation.read(slaveaddress, addr,addr_len, r_data, datalen, delay)**

Read data from I2C bus.

**Parameter description**

|Parameter | type | description|
| ------------ | --------- | -------------------------------- |
|Slaveaddress | int | I2C device address|
|Addr | bytearray | I2C register address|
| addr_ Len | int | register address length|
| r_ Data | bytearray | byte array of received data|
|Datalen | int | length of byte array|
|Delay | int | delay, data conversion buffer time (unit: ms)|

* Return Value

  * The integer value 0 is returned successfully, and the integer value - 1 is returned in failure.



###### Write data

> **I2C_simulation.write(slaveaddress, addr, addr_len, data, datalen)**

Write data from the I2C bus.

* Parameter description

|Parameter | type | description|
| ------------ | --------- | -------------- |
|Slaveaddress | int | I2C device address|
|Addr | bytearray | I2C register address|
| addr_ Len | int | register address length|
|Data | bytearray | written data|
|Datalen | int | length of data written|

* Return Value

  * The integer value 0 is returned successfully, and the integer value - 1 is returned in failure.



###### Use example

This example is to drive aht10 to obtain temperature and humidity.

```python
import log
#from machine import I2C
from machine import I2C_simulation
import utime as time
"""
1. calibration
2. Trigger measurement
3. read data
"""

#API manual http://qpy.quectel.com/wiki/#/en-us/api/?id=i2c
#Aht10 instructions
#  https://server4.eca.ir/eshop/AHT10/Aosong_AHT10_en_draft_0c.pdf


class aht10class():
    i2c_log = None
    i2c_dev = None
    i2c_addre = None

    # Initialization command
    AHT10_CALIBRATION_CMD = 0xE1
    # Trigger measurement
    AHT10_START_MEASURMENT_CMD = 0xAC
    # reset
    AHT10_RESET_CMD = 0xBA

    def write_data(self, data):
        self.i2c_dev.write(self.i2c_addre,
                           bytearray(0x00), 0,
                           bytearray(data), len(data))
        pass

    def read_data(self, length):
        print("read_data start")
        r_data = [0x00 for i in range(length)]
        r_data = bytearray(r_data)
        print("read_data start1")
        ret = self.i2c_dev.read(self.i2c_addre,
                          bytearray(0x00), 0,
                          r_data, length,
                          0)
        print("read_data start2")
        print('ret',ret)
        print('r_data:',r_data)
        return list(r_data)

    def aht10_init(self, addre=0x38, Alise="Ath10"):
        self.i2c_log = log.getLogger(Alise)
        self.i2c_dev = I2C_simulation(I2C_simulation.GPIO10, I2C_simulation.GPIO11, 300)
        self.i2c_addre = addre
        self.sensor_init()
        pass

    def aht10_transformation_temperature(self, data):
        r_data = data
        #Convert the temperature according to the description in the data book
        humidity = (r_data[0] << 12) | (
            r_data[1] << 4) | ((r_data[2] & 0xF0) >> 4)
        humidity = (humidity/(1 << 20)) * 100.0
        print("current humidity is {0}%".format(humidity))
        temperature = ((r_data[2] & 0xf) << 16) | (
            r_data[3] << 8) | r_data[4]
        temperature = (temperature * 200.0 / (1 << 20)) - 50
        print("current temperature is {0}°C".format(temperature))
        

    def sensor_init(self):
        # calibration
        self.write_data([self.AHT10_CALIBRATION_CMD, 0x08, 0x00])
        time.sleep_ms(300)  # at last 300ms
        pass


    def ath10_reset(self):
        self.write_data([self.AHT10_RESET_CMD])
        time.sleep_ms(20)  # at last 20ms

    def Trigger_measurement(self):
        # Trigger data conversion
        self.write_data([self.AHT10_START_MEASURMENT_CMD, 0x33, 0x00])
        time.sleep_ms(200)  # at last delay 75ms
        # check has success
        r_data = self.read_data(6)
        # check bit7
        if (r_data[0] >> 7) != 0x0:
            print("Conversion has error")
        else:
            self.aht10_transformation_temperature(r_data[1:6])

ath_dev = None

def i2c_aht10_test():
    global ath_dev
    ath_dev = aht10class()
    ath_dev.aht10_init()

    #Test ten times
    for i in range(5):
        ath_dev.Trigger_measurement()
        time.sleep(1)


if __name__ == "__main__":
    print('start')
    i2c_aht10_test()


```



##### SPI

Class function: Serial peripheral interface bus protocol. 


###### Create SPI Object

> **spi_obj = SPI(port, mode, clk)**

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| port      | int  | Channel selection[0,1]                                       |
| mode      | int  | SPI working mode (ususally mode 0): <br />Clock polarity CPOL: When SPI is idle, the level of the clock signal SCLK (0: Low level when idle; 1: High level when idle)<br /> 0 : CPOL=0, CPHA=0<br /> 1 : CPOL=0, CPHA=1<br /> 2:  CPOL=1, CPHA=0<br /> 3:  CPOL=1, CPHA=1 |
| clk       | int  | volume_up clock frequency<br />EC600NCN/EC600SCN/EC800NCN/BG95M3/EC600M/EC800M/EG912N:<br /> 0 : 812.5kHz<br /> 1 : 1.625MHz<br /> 2 : 3.25MHz<br /> 3 : 6.5MHz<br /> 4 : 13MHz<br /> 5 :  26MHz<br /> 6：52MHz<br />EC600UCN/EC200UCN/EG915U:<br />0 : 781.25KHz<br />1 : 1.5625MHz<br />2 : 3.125MHz<br />3 : 5MHz<br />4 : 6.25MHz<br />5 : 10MHz<br />6 : 12.5MHz<br />7 : 20MHz<br />8 : 25MHz<br />9 : 33.33MHz<br />BC25PA：<br />0 ： 5MHz<br />X : XMHz  (X in [1,39]) |

- Pin Description

| Platform      | Pin                                                          |
| ------------- | ------------------------------------------------------------ |
| EC600U        | port0:<br />CS:Pin number 4<br />CLK:Pin number 1<br />MOSI:Pin number 3<br />MISO:Pin number 2<br />port1:<br />CS:Pin number 58 <br />CLK:Pin number 61 <br />MOSI:Pin number 59 <br />MISO:Pin number 60 |
| EC200U        | port0:<br />CS:Pin number 134<br />CLK:Pin number 133<br />MOSI:Pin number 132<br />MISO:Pin number 131<br />port1:<br />CS:Pin number 26<br />CLK:Pin number 27<br />MOSI:Pin number 24<br />MISO:Pin number 25 |
| EC600S/EC600N | port0:<br />CS:Pin number 58<br />CLK:Pin number 61<br />MOSI:Pin number 59<br />MISO:Pin number 60<br />port1:<br />CS:Pin number 4<br />CLK:Pin number 1<br />MOSI:Pin number 3<br />MISO:Pin number 2 |
| EC100Y        | port0:<br />CS:Pin number 25<br />CLK:Pin number 26<br />MOSI:Pin number 27<br />MISO:Pin number 28<br />port1:<br />CS:Pin number 105<br />CLK:Pin number 104<br />MOSI:Pin number 107<br />MISO:Pin number 106 |
| EC800N        | port0:<br />CS:Pin number 31<br />CLK:Pin number 30<br />MOSI:Pin number 32<br />MISO:Pin number 33<br />port1:<br />CS:Pin number 52<br />CLK:Pin number 53<br />MOSI:Pin number 50<br />MISO: Pin number 51 |
| BC25PA        | port0:<br />CS:Pin number 6<br />CLK:Pin number 5<br />MOSI:Pin number 4<br />MISO:Pin number 3 |
| BG95M3        | port0:<br />CS:Pin number 25<br />CLK:Pin number 26<br />MOSI:Pin number 27<br />MISO:Pin number 28<br />port1:<br />CS:Pin number 41<br />CLK:Pin number 40<br />MOSI:Pin number 64<br />MISO:Pin number 65 |
| EC600M        | port0:<br />CS:Pin number 58<br />CLK:Pin number 61<br />MOSI:Pin number 59<br />MISO:Pin number 60<br />port1:<br />CS:Pin number 4<br />CLK:Pin number 1<br />MOSI:Pin number 3<br />MISO:Pin number 2 |
| EG915U        | port0:<br />CS:Pin number 25<br />CLK:Pin number 26<br />MOSI:Pin number 64<br />MISO:Pin number 88 |
| EC800M        | port0:<br />CS:Pin number 31<br />CLK:Pin number 30<br />MOSI:Pin number 32<br />MISO:Pin number 33<br />port1:<br />CS:Pin number 52<br />CLK:Pin number 53<br />MOSI:Pin number 50<br />MISO:Pin number 51 |
| EG912N        | port0:<br />CS:Pin number 25<br />CLK:Pin number 26<br />MOSI:Pin number 27<br />MISO:Pin number 28<br />port1:<br />CS:Pin number 5<br />CLK:Pin number 4<br />MOSI:Pin number 6<br />MISO:Pin number 7 |

* Note:

  * BC25PA platform does not support 1 and 2 modes.

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

  * -1	Failed execution



###### Write Data

> **SPI.write(data, datalen)**

It writes data.

* Parameter

| Parameter | Type  | Description             |
| --------- | ----- | ----------------------- |
| data      | bytes | Data written.           |
| datalen   | int   | Length of data written. |

* Return Value

  * -1	Failed execution



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

  * -1	Failed execution



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

  * None

- Example

```python
from machine import LCD 
lcd = LCD()   # Create lcd object
```



###### LCD Initialization （interface 1：LCM interface of the module）

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

  * 0  	 Successful execution.
  * -1  	Initialized.
  * -2  	Parameter error (empty or too large (bigger than 1000 pixels)) .
  * -3  	Failed cache request.
  * -5  	Configuration parameter error.



###### LCD Initialization（interface 2：SPI  interface of the module）

> **lcd.lcd_init(lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness, lcd_interface, spi_port, spi_mode, cs_pin, dc_pin, rst_pin)**

It initializes LCD. 

- Parameter

| Parameter          | Type      | Description                                                  |
| ------------------ | --------- | ------------------------------------------------------------ |
| lcd_init_data      | bytearray | Inputting configuration commands for LCD.                    |
| lcd_width          | int       | The width of LCD screen, not more than 500.                  |
| lcd_hight          | int       | The height of LCD screen, not more than 500.                 |
| lcd_clk            | int       | SPI clock. refer to the parameter description of Create SPI Object in machine SPI. |
| data_line          | int       | Number of data lines, the parameter values are 1 and 2.      |
| line_num           | int       | The number of lines, the parameter values are 3 and 4.       |
| lcd_type           | int       | Screen type. 0: rgb; 1: fstn.                                |
| lcd_invalid        | bytearray | Inputting configuration commands for LCD area settings.      |
| lcd_display_on     | bytearray | Inputting configuration commands for LCD screen light.       |
| lcd_display_off    | bytearray | Inputting configuration commands for LCD screen off.         |
| lcd_set_brightness | bytearray | Inputting the configuration command of LCD screen brightness. Setting to None indicates that the brightness is controlled by LCD_BL_K (some screens are controlled by registers, and some are controlled by LCD_BL_K) |
| lcd_interface      | int       | type of LCD interface. 0：LCM interface；1：SPI interface    |
| spi_port           | int       | Channel selection[0,1]，refer to SPI description in machine. |
| spi_mode           | int       | SPI working mode (ususally mode 0): <br />Clock polarity CPOL: When SPI is idle, the level of the clock signal SCLK (0: Low level when idle; 1: High level when idle)<br /> 0 : CPOL=0, CPHA=0<br /> 1 : CPOL=0, CPHA=1<br /> 2:  CPOL=1, CPHA=0<br /> 3:  CPOL=1, CPHA=1 |
| cs_pin             | int       | CS PIN，refer to Pin Constant Description                    |
| dc_pin             | int       | DC PIN，refer to Pin Constant Description                    |
| rst_pin            | int       | RST PIN，refer to Pin Constant Description                   |

* Return Value

  * 0  	 Successful execution.
  * -1  	Initialized.
  * -2  	Parameter error (empty or too large (bigger than 1000 pixels)) .
  * -3  	Failed cache request.
  * -5  	Configuration parameter error.



###### Clear LCD.


> **lcd.lcd_clear(color)**

It clears LCD.

- Parameter

| Parameter | Type        | Description                                 |
| --------- | ----------- | ------------------------------------------- |
| color     | hexadecimal | The color value that needs to be refreshed. |

* Return Value

  * 0	Successful execution.
  * -1 Failed execution.



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

  * 0   	Successful execution.
  * -1  	The screen is not initialized.
  * -2  	Wrong width and height settings.
  * -3  	Data cache is empty.



###### Set Screen Brightness 

> **lcd.lcd_brightness(level)**

It sets the screen brightness level. 

- Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| level     | int  | Brightness level. The lcd_set_brightness callback in lcd.lcd_init() will be called. If this parameter is None, the brightness adjustment is controlled by the brightness adjustment pin.<br />Range [0,5]. |

* Return Value

  * 0	Successful execution.
  * -1 Failed execution.



###### Turn on LCD Display 

> **lcd.lcd_display_on()**

It turns on the LCD display, call the lcd_display_on callback in lcd.lcd_init() after calling this interface. 

- Parameter

  * None

* Return Value

  * 0	Successful execution.
  * -1	Failed execution.



###### Turn off LCD Display 

> **lcd.lcd_display_off()**

It turns off the LCD display, call the  lcd_display_off callback in lcd.lcd_init() after calling this interface. 

- Parameter

  * None

* Return Value

  * 0	Successful execution.
  * -1	Failed execution.



###### Write Command

> **lcd.lcd_write_cmd(cmd_value, cmd_value_len)**

It writes command.

- Parameter

| Parameter     | Type        | Description              |
| ------------- | ----------- | ------------------------ |
| cmd_value     | hexadecimal | Command value.           |
| cmd_value_len | int         | Length of command value. |

* Return Value

  * 0	Successful execution.
  * Other value	Failed execution.



###### Write Data

> **lcd.lcd_write_data(data_value, data_value_len)**

It writes data.

- Parameter

| Parameter      | Type        | Description           |
| -------------- | ----------- | --------------------- |
| data_value     | hexadecimal | Data value.           |
| data_value_len | int         | Length of data value. |

* Return Value

  * 0	Successful execution.
  * Other value	Failed execution.



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

  * 0	Successful execution.
  * Other value	Failed execution.



###### show jpeg images

> **lcd.lcd_show_jpg( file_name, start_x,start_y)**

Display jpeg pictures by reading files.

- Parameter

| Parameter | Type | Description             |
| --------- | ---- | ----------------------- |
| file_name | str  | Image name to display   |
| start_x   | int  | starting x coordinate   |
| start_y   | int  | starting y coordinate   |

* Return Value

  * 0   Successful execution.
  * Other value Failed execution.



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
| --------- | ---- | ------------------------------------------------ |
| period    | int  | Set software watchdog detection time, unit (s)。 |

* Return Value

  * It returns software watchdog object.



###### Feed Watchdog

> ​	**wdt.feed()**

It feeds watchdog. 

- Parameter

  * None

* Return Value

  * None



###### Stop Watchdog

> ​	**wdt.stop()**

It stops watchdog. 

- Parameter

  * None

* Return Value

  * None



###### Example

```python
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
##### KeyPad

Module function: provide matrix keyboard interface and support platform EC600SCN_LB/EC800N_CN_LA/EC600NCN_LC/EC200U_CN_LB/EC600U_CN_LB/EC600M_CN_LA/EC800M_CN_LA/EC800M_CN_GA/EG912N_ENAA
EC200U supports 4x3 at most and EC600U supports 6x6 at most.

###### Create keypad object

> **keypad=machine.KeyPad()**

- Parameter

| Parameter | Type | Description                                      |
| ------ | -------- | ----------------------------------- |
|Row | int | Greater than 0, not exceeding the maximum supported by the platform|
|Col | int | Greater than 0, not exceeding the maximum supported by the platform|

- Note: 

  if row and col are not set, the default is 4X4.

|Platform | maximum row | maximum column|
| ------------- | ------ | ------ |
| EC800N/EC600N | 4 | 4 |
| EC600S | 5 | 5 |
| EC200U | 4 | 3 |
| EC600U | 6 | 6 |
| EC600M | 5 | 5 |
| EC800M | 5 | 5 |
| EG912N | 3 | 3 |

- Pin Description

Note: When only some pins are used, the wiring should be done in  descending order of row and column numbers. For example, when EC600M  uses a 2x2 matrix keyboard, the hardware uses pins 49, 51 and 48, 50.

| Platform | Pin                                                          |
| -------- | ------------------------------------------------------------ |
| EC600M   | The row number (output) corresponds to the following pins:<br/>Row No.0 – Pin number 49<br/>Row No.1 – Pin number 51<br/>Row No.2 – Pin number 53<br/>Row No.3 – Pin number 55<br/>Row No.4 – Pin number 56<br/>The column number (input) corresponds to the following pins:<br/>Col No.0 – Pin number 48<br/>Col No.1 – Pin number 50<br/>Col No.2 – Pin number 52<br/>Col No.3 – Pin number 54<br />Col No.4 – Pin number 57 |
| EC800M   | The row number (output) corresponds to the following pins:<br/>Row No.0 – Pin number 86<br/>Row No.1 – Pin number 76<br/>Row No.2 – Pin number 85<br/>Row No.3 – Pin number 82<br/>Row No.4 – Pin number 74<br/>The column number (input) corresponds to the following pins:<br/>Col No.0 – Pin number 87<br/>Col No.1 – Pin number 77<br/>Col No.2 – Pin number 84<br/>Col No.3 – Pin number 83<br />Col No.4 – Pin number 75 |
| EG912N   | The row number (output) corresponds to the following pins:<br/>Row No.1 – Pin number 20<br/>Row No.2 – Pin number 16<br/>Row No.3 – Pin number 116<br/>The column number (input) corresponds to the following pins:<br/>Col No.2 – Pin number 105<br/>Col No.3 – Pin number 21<br />Col No.4 – Pin number 1 |

* Example:
>
>```python
>>>>import machine
>>>>keypad=machine.KeyPad(2,3)		# The matrix keyboard is set as a matrix keyboard with 2 rows and 3 columns
>>>>keypad=machine.KeyPad()  	 	# Not set. The default setting is 4 rows and 4 columns matrix keyboard
>>>>keypad=machine.KeyPad(2)  	 	# The row value is set to 2, and the column value defaults to 4
>```
>
>

###### Initialize keypad

> **keypad.init()**

Initialize keypad settings.

* Parameter

  * None

- Return Value

  * 0 is returned for success and - 1 is returned for failure.

###### Set callback function

> **keypad.set_ callback(usrFun)**

After the key is connected to the module, press and release the key to trigger the callback function setting.

- Parameter

| Parameter | Type | Description                                      |
| ------ | -------- | ------------------------------------------ |
| usrFun | function | callback function. This function will be triggered when the external keyboard key is pressed and placed |


* Note: The argument to the usrfun function is the list data type.

* List contains three parameters. It has the following meanings:

  list[0] - 1 means press and 0 means lift<br/>
  list[1] - row<br/>
  list[2] - col


* Return Value

  * 0


###### Uninitialization

> **keypad.deinit()**

Release the initialized resource and callback function settings.

* Parameter

  * None

* Return Value

  * 0 is returned for success and - 1 is returned for failure.

###### example
```python
import machine
import utime
is_loop = 1
keypad=machine.KeyPad()  
keypad.init()
def userfun(l_list):
    global is_loop 
    if  l_list[0] != 1 :
        is_loop = 0
        print('will exit')
    print(l_list)
    
keypad.set_callback(userfun)
loop_num = 0

while is_loop == 1 and loop_num < 10:
    utime.sleep(5)
    loop_num = loop_num +1
    print(" running..... ",is_loop,loop_num)

keypad.deinit()
print('exit!')
```

#### qrcode- QR Code Display 

Module function:  Generate the corresponding QR code according to the input content. 

Note: The BC25PA platform does not support this module function.

​			Before using the preview, you need to initialize LCD.

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

  * 0       Successful execution.
  * -1     Failed to generate QR code.
  * -2     Failed magnification. 
  * -3     Failed display.



#### pm - Low Power

Module function: When there is no business processing, the system enters the sleep state and enters the low power mode.

##### Create wake_lock Lock 

> ​	**lpm_fd = pm.create_wakelock(lock_name, name_size)**

It creates wake_lock lock.

- Parameter

| Parameter | Type   | Description          |
| --------- | ------ | -------------------- |
| lock_name | string | Custom lock name.    |
| name_size | int    | Length of lock name. |

* Return Value

  * wakelock's Identification number   Successful execution.
  * -1   Failed execution.

* Note

  * The BC25PA platform does not support this method.


##### Delete wake_lock Lock 

> ​	**pm.delete_wakelock(lpm_fd)**

It deletes wake_lock lock. 

- Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| lpm_fd    | int  | The corresponding identification ID of the lock to be deleted. |

* Return Value

  * 0      Successful execution.

* Note

  * The BC25PA platform does not support this method.


##### Lock 

> ​	**pm.wakelock_lock(lpm_fd)**

- Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| lpm_fd    | int  | The wakelock identification ID that needs to perform the lock operation. |

* Return Value

  * 0	Successful execution.
  * -1	Failed execution.

* Note

  * The BC25PA platform does not support this method.


##### Release Lock 

> ​	**pm.wakelock_unlock(lpm_fd)**

It releases lock.

- Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| lpm_fd    | int  | The wakelock identification ID that needs to perform the lock release operation. |

* Return Value

  * 0	Successful execution.
  * -1	Failed execution.

* Note

  The BC25PA platform does not support this method.

##### Automatic Sleep Mode Control 

> ​	**pm.autosleep(sleep_flag)**

It controls automatic sleep mode.

- Parameter

| Parameter  | Type | Description                                                  |
| ---------- | ---- | ------------------------------------------------------------ |
| sleep_flag | int  | 0, turn off automatic sleep mode; 1 turn on automatic sleep mode. |

* Return Value

  * 0	Successful execution.



##### Get the number of locks created 

> ​	**pm.get_wakelock_num()**

It gets the number of locks created.

- Parameter

  * None

* Return Value

  * It returns the number of wakelock locks that have been created. 

* Note

  * The BC25PA platform does not support this method.

##### Set the control time for PSM mode

- Only supported on BC25 platform

> **pm.set_psm_time(tau_uint,tau_time,act_uint,act_time)**  # Set up and enable PSM           <**Mode 1**>
>
> **pm.set_psm_time(mode)**														   # Individual settings enable or disable    <**Mode 2**>


* Parameter

| Parameter     | Parameter Type | Parameter Description                       |
| -------- | -------- | ------------------------------ |
| mode | int | Whether to enable PSM:<br/>0 Disable PSM<br/>1 Enable PSM<br/>2 Disable PSM and delete all parameters of PSM, if there is default value, reset the default value. (Note that when this mode is disabled, if you want to enable PSM, you must use **mode 1**, and **mode 2** has no meaning, because the set TAU ​​and ACT times are all cleared). |
| tau_uint | int   | tau(T3412) timer unit |
| tau_time | int   | tau (T3412) timer time period value |
| act_uint | int   | act(T3324) timer unit |
| act_time | int   | act(T3324) timer time period value |

* tau timer description
|TAU timer unit value  | Type | Unit value description                       |
| -------- | -------- | ------------------------------|
| 0 | int   | 10 Minute |
| 1 | int   | 1 Hour |
| 2 | int   | 10 Hour |
| 3 | int   | 2 Second |
| 4 | int   | 30 Second |
| 5 | int   | 1 Minute |
| 6 | int   | 320 Hour |
| 7 | int   | Timer is disabled |

* act timer description
|ACT timer unit value  | type | Unit value description  
| -------- | -------- | ------------------------------|
| 0 | int   | 2 Second |
| 1 | int   | 1 Minute |
| 2 | int   | 6 Minute |
| 7 | int   | Timer is disabled |

* Return Value

    True: 	success
    False:	failed

* Note
   Only supported on BC25 platform

- Example

```python
>>> import pm
>>> pm.set_psm_time(1,2,1,4)  #Set the tau timer period to 1 hour * 2 = 2 hours, and the act timer period value to 1 minute * 4 = 4 minutes.
True
>>>
```



##### Get control time for PSM mode

- Only supported on BC25 platform

> **pm.get_psm_time()**

* Parameter

  None

* Return Value

  Success：The return value is of type list, as follows：
  |Parameter  | Type | Unit value description                       |
| -------- | -------- | ------------------------------|
| list[0] | int   | Mode description: <br/>0-Disable PSM. <br/>1-Enable PSM. <br/>2.Disable PSM and delete all parameters of PSM, if there is default value, reset to default value. |
| list[1] | int   | tau timer unit |
| list[2] | int   | tau timer time period value |
| list[3] | int   | act timer unit |
| list[4] | int   | act timer time period value |
  Failed：Returns None. Returns failure when PSM is disabled.
  
* Note
    Only supported on BC25 platform

- Example


```python
>>> pm.get_psm_time()

[1, 1, 1, 1, 2]


```




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
| --------- | ------ | ------------------- |
| regex     | string | Regular expression. |

* Return Value

  * It returns regex object.



#####  Match

> ​	**ure.match(regex, string)**

It matches the regular expression object with string, usually from the beginning of the string.

- Parameter

| Parameter | Type   | Description                |
| --------- | ------ | -------------------------- |
| regex     | string | Regular expression.        |
| string    | string | String data to be matched. |

* Return Value

  * A matched object   Successful execution.
  * None   Failed execution.



##### Search

> ​	**ure.search(regex, string)**

ure.search scans the entire string and returns the first successful match. 

- Parameter

| Parameter | Type   | Description                |
| --------- | ------ | -------------------------- |
| regex     | string | Regular expression.        |
| string    | string | String data to be matched. |

* Return Value

  * A matched object   Successful execution.
  * None   Failed execution.



**Match Object**

It matches objects returned by the match() and search methods.

##### Match a Single String 

> ​	**match.group(index)**

It  matches the string of the entire expression.

- Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| index     | int  | In the regular expression, group() proposes the string intercepted by the group, index=0 returns the whole, and it is obtained according to the written regular expression. When the group does not exist, an exception is thrown. |

* Return Value

  * It returns the string of the matched entire expression. 


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

Note: wifiscan supports the platforms: 1603/1606(except:600MCN_LC/800MCN_GC/800MCN_LC)/8910/8850.

##### Determine whether wifiScan is supported

> **wifiScan.support()**

* Function：

  Determine whether the module supports wifiScan function.

* Parameter：

  * None

* Return Value：

  * True	 wifiScan is supported
  * False	wifiScan is not supported

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

  * 0	 Successful execution
  * -1	Failed execution

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

  * None

* Return Value：

  * True	 wifiScan function is enabled
  * False	wifiScan function is disabled.

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

  * None

* Return Value：

  * A tuple	Successful execution
  * -1 Failed execution 

  The format of the returned tuple is as follows:

  `(timeout, round, max_bssid_num, scan_timeout, priority)`

  | Return Value  | Type         | Description                                                  |
  | ------------- | ------------ | ------------------------------------------------------------ |
  | timeout       | Integer type | This parameter is the timeout of upper layer application. When the application triggers timeout, it actively reports the scanned hot spot information. The application automatically reports the hot spot information if it scans all the hop spots which have been set previously or the underlying layer scan reaches the frequency sweeping timeout before the timeout of the application. |
  | round         | Integer type | This parameter is the scanning rounds of wifi. When reaching the scanning rounds, the scan stops and the scanning results are obtained. |
  | max_bssid_num | Integer type | This parameter determines the maximum number of hot spots to be scanned. If the number of hot spots scanned by the underlying layer reaches the maximum, the scan stops and the scanning results are obtained. |
  | scan_timeout  | Integer type | This parameter is the wifi hot spot scanning timeout of underlying layer. If the underlying layer scan reaches the hot spot scanning timeout set previously,  the scan stops and the scanning results are obtained. |
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
  | timeout       | Integer type | This parameter is the timeout of upper layer application. When the application triggers timeout, it actively reports the scanned hot spot information. The application automatically reports the hot spot information if it scans all the hop spots which have been set previously or the underlying layer scan reaches the frequency sweeping timeout before the timeout of the application. <br>Range:<br/>1603/1606 platforms: 4–255; unit: s.<br/>8850/8910 platfroms: 120–5000; unit: ms. |
  | round         | Integer type | This parameter is the scanning rounds of wifi. When reaching the scanning rounds, the scan stops and the scanning results are obtained. <br/>Range:<br/>1603/1606 platforms: 1–3; unit: round<br/>8850/8910 platforms: 1–10; unit: round |
  | max_bssid_num | Integer type | This parameter determines the maximum number of hot spots to be scanned. If the number of hot spots scanned by the underlying layer reaches the maximum, the scan stops and the scanning results are obtained. <br/>Range:<br/>1603 platform: 4–30<br/>1606 platform: 4–10<br/>8850/8910 platforms: 1–30 |
  | scan_timeout  | Integer type | This parameter is the wifi hot spot scanning timeout of underlying layer. If the underlying layer scan reaches the hot spot scanning timeout set previously,  the scan stops and the scanning results are obtained. Range: 1–255.  |
  | priority      | Integer type | This parameter is the priority setting of wifi scanning service. 0 indicates that ps is preferred; 1 indicates that wifi is preferred. When ps is preferred, the wifi scan is terminated when a data service is initiated. When wifi is preferred, RRC connection is not connected when a data service is initiated. wifi scan runs normally. The RRC connection is only established after the scan completes. 8850/8910 platforms do not support this parameter. You can set this parameter to 0. |

* Return Value：

  * 0	 Successful execution
  * -1	Failed execution

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

  * 0	 Successful execution
  * -1	Failed execution

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

  * None

* Return Value：

  * 0	 Successful execution
  * -1	Failed execution

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

  * None

* Return Value：

  * Scanning result	Successful execution
  * -1 Failed execution or error
  * The return value of successful execution is as follows:

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

Module function: provide function of BLE GATT Server（slave） and BLE GATT Client（master）,  using BLE 4.2 protocol.  Currently only 200U/600U modules support BLE.

##### Start  BLE GATT Function

> **ble.gattStart()**

* Function

  Start BLE GATT fucntion.

* Parameter

  * None

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### Stop BLE GATT Function

> **ble.gattStop()**

* Function

  Stop BLE GATT function.

* Parameter

  * None

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### Get BLE Status

> **ble.getStatus()**

* Function

  Get  the status of BLE.

* Parameter

  * None

* Return Value

  * 0	BLE has been stopped
  * 1	BLE has been started
  * -1	Get BLE status failed

* Example

  * None



##### Get BLE Public Address

> **ble.getPublicAddr()**

* Function

  Gets the BLE public address.This interface can be called only after BLE has been initialized and started successfully, for example, after receiving an event with event_id 0 in the callback.

* Note

  If there is a default Bluetooth MAC address, the MAC address obtained by the interface is the same as the default Bluetooth MAC address. If it is not set, the address obtained by the interface will be a static address generated randomly after Bluetooth is started, so it will be different each time Bluetooth is powered on again.

* Parameter

  * None

* Return Value

  * The BLE address of type bytearray (6 bytes) is returned on success, and integer -1 is returned on failure.

* Example

  ```python
  >>> addr = ble.getPublicAddr()
  >>> print(addr)
  b'\xdb3\xf5\x1ek\xac'
  >>> mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
  >>> print('mac = [{}]'.format(mac))
  mac = [ac:6b:1e:f5:33:db]
  ```

  

##### BLE Server - Initialize BLE and Register Callback Function

> **ble.serverInit(user_cb)**

* Function

  Initialize BLE Server and register callback function.

* Parameter

| Parameter | Type     | Description       |
| --------- | -------- | ----------------- |
| user_cb   | function | Callback function |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

- Description

（1）Format of callback function

```python
def ble_callback(args):
	event_id = args[0]  # The first parameter is fixed as event_id
	status = args[1] # The second parameter is fixed as status which indicates the execution result of an operation, such as BLE is enabled successfully or unsuccessfully.
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

* Example

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



##### BLE Server - Release BLE Server Resources 

> **ble.serverRelease()**

* Function

  Release BLE Server resources.

* Parameter

  * None

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Server - Set BLE Local Name

> **ble.setLocalName(code, name)**

* Function

  Set BLE local name.

* Note

  For BLE, if you want  to see the name of the broadcast device when scanning, you need to include the Bluetooth name in the broadcast data, or include the device name in the scan reply data.

* Parameter

  | Parameter | Type         | Description                           |
  | --------- | ------------ | ------------------------------------- |
  | code      | Integer Type | Encoding mode<br>0 - UTF8<br/>1 - GBK |
  | name      | String Type  | BLE name, no more than 29 bytes       |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
>>> ble.setLocalName(0, 'QuecPython-BLE')
0
```



##### BLE Server - Set Advertising Parameter

> **ble.setAdvParam(min_adv,max_adv,adv_type,addr_type,channel,filter_policy,discov_mode,no_br_edr,enable_adv)**

* Function

  Set advertising parameter.

* Parameter

  | Parameter     | Type                  | Description                                                  |
  | ------------- | --------------------- | ------------------------------------------------------------ |
  | min_adv       | Unsigned integer type | Minimal advertising interval. Range: 0x0020–0x4000. It is calculated as follows:<br>Time interval = min_adv \* 0.625. Unit: ms |
  | max_adv       | Unsigned integer type | Maximum advertising interval. Range: 0x0020–0x4000. It is calculated as follows:<br/>Time interval = max_adv \* 0.625. Unit: ms |
  | adv_type      | Unsigned integer type | Advertising type. <br>0 - CONNECTABLE UNDIRECTED, default <br>1 - CONNECTABLE HIGH DUTY CYCLE DIRECTED<br>2 - SCANNABLE UNDIRECTED<br>3 - NON CONNECTABLE UNDIRECTED<br>4 - CONNECTABLE LOW DUTY CYCLE DIRECTED |
  | addr_type     | Unsigned integer type | Local address type.  <br>0 - Public address<br>1 - Random address |
  | channel       | Unsigned integer type | Advertising channel. <br>1 - Advertising channel 37<br>2 - Advertising channel 38<br>4 - Advertising channel 39<br>7 - Advertising channel 37 and 38 and 39, default |
  | filter_policy | Unsigned integer type | Advertising filter policy.<br>0 - Process scan and connection requests from all devices<br/>1 - Process connection requests from all devices and scan requests from only white list devices(Not currently supported)<br/>2 - Process scan requests from all devices and connection requests from only white list devices(Not currently supported)<br/>3 - Process connection and scan requests from only white list devices(Not currently supported) |
  | discov_mode   | Unsigned integer type | Discovery mode. Used by GAP protocol and the default is 2 .<br/>1 - Limited Discoverable Mode<br/>2 - General Discoverable Mode |
  | no_br_edr     | Unsigned integer type | No use of BR/EDR. The default is 1. The value is 0 if BR/EDR is used. |
  | enable_adv    | Unsigned integer type | Enable advertising. The default is 1. The value is 0 if advertising is disabled. |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

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



##### BLE Server - Set Advertising Data

> **ble.setAdvData(data)**

* Function

  Set advertising data.

* Parameter

  | Parameter | Type  | Description                                                  |
  | --------- | ----- | ------------------------------------------------------------ |
  | data      | Array | Advertising data which is no more than 31 octets. Pay attention to the type of this parameter. The advertising data is organized in the program and it needs to be converted through bytearray() before it can be passed in to the API. As shown in below example.<br>Format of advertising data:<br>The content of advertising data. The format is the combination of length+type+data. An advertising data can contain multiple combinations in this format. For example, there are 2 combinations in the example below. The first one is "0x02, 0x01, 0x05". 0x02 means that there are 2 data - 0x01 and 0x05. 0x01 is the type; 0x05 is the specific data. The second one consists of  the length obtained by the length of BLE name plus 1 (1 octet needs to be added as it contains the data that represents type), type 0x09 and the data represented by the corresponding specific encoded value of name.<br>For detailed information of type value, please refer to the following link:<br/>[Generic Access Pfofile](https://btprodspecificationrefs.blob.core.windows.net/assigned-numbers/Assigned%20Number%20Types/Generic%20Access%20Profile.pdf) |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

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



##### BLE Server - Set Scan Response Data

> **ble.setAdvRspData(data)**

* Function

  Set scan response data.

* Parameter

  | Parameter | Type  | Description                                                  |
  | --------- | ----- | ------------------------------------------------------------ |
  | data      | Array | Scan response data which is no more than 31 octets. The considerations are consistent with the description of  *ble.setAdvData(data)* above. The setting of scan response data makes sense only when the scanning mode of the client device is active scan. |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

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



##### BLE Server - Add a Service

> **ble.addService(primary, server_id, uuid_type, uuid_s, uuid_l)**

* Function

  Add a service.

* Parameter

  | Parameter | Type                  | Description                                                  |
  | --------- | --------------------- | ------------------------------------------------------------ |
  | primary   | Unsigned integer type | Service type. 1- Primary service; Other value - Secondary service |
  | server_id | Unsigned integer type | Service ID, which determines a service                       |
  | uuid_type | Unsigned integer type | UUID type<br>0 - Long UUID, 128bit<br>1 - Short UUID, 16bit  |
  | uuid_s    | Unsigned integer type | Short UUID, 2 bytes (16bit). When uuid_type is 0, the value of this parameter is 0. |
  | uuid_l    | Array                 | Long UUID, 16 bytes (128bit). When uuid_type is 1, the value of this parameter is bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

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



##### BLE Server - Add a Characteristic 

> **ble.addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l)**

* Function

  Add a characteristic in a service.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | server_id  | Unsigned integer type | Service ID, which determines a service                       |
  | chara_id   | Unsigned integer type | Characteristic ID                                            |
  | chara_prop | Unsigned integer type | Characteristic properties. Hexadecimal number. You can specify several properties at the same time by OR operations.  <br>0x01 -Broadcast<br/>0x02 - Read<br/>0x04 - Write Without Response<br/>0x08 - Write<br/>0x10 - Notify<br/>0x20 - Indicate<br/>0x40 - Signed Write Command<br/>0x80 - Extended Properties |
  | uuid_type  | Unsigned integer type | uuid type<br/>0 - Long UUID, 128bit<br/>1 - Short UUID, 16bit |
  | uuid_s     | Unsigned integer type | Short UUID, 2 bytes (16bit)                                  |
  | uuid_l     | Array                 | Long UUID, 16 bytes (128bit)                                 |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

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



##### BLE Server - Add a Characteristic Value

> **ble.addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)**

* Function

  Add a characteristic value for a characteristic.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | server_id  | Unsigned integer type | Service ID, which determines a service                       |
  | chara_id   | Unsigned integer type | Characteristic ID                                            |
  | permission | Unsigned integer type | Permission of characteristic value. 2 bytes. Hexadecimal number. You can specify several properties at the same time by OR operations.  <br/><br/>0x0001 - Readable<br/>0x0002 - Writable<br/>0x0004 - Read requires authentication<br/>0x0008 - Read requires authorization<br/>0x0010 - Read requires encryption<br/>0x0020 - Read requires authorization and authentication<br/>0x0040 - Write requires authentication<br/>0x0080 - Write requires authorization<br/>0x0100 - Write requires encryption<br/>0x0200 - Write requires authorization and authentication |
  | uuid_type  | Unsigned integer type | uuid type<br/>0 - Long UUID, 128bit<br/>1 - Short UUID, 16bit |
  | uuid_s     | Unsigned integer type | Short UUID, 2 bytes (16bit)                                  |
  | uuid_l     | Array                 | Long UUID, 16 bytes (128bit)                                 |
  | value      | Array                 | Characteristic value                                         |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

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



##### BLE Server - Add a Characteristic Descriptor

> **ble.addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value)**

* Function

  Add a characteristic descriptor for a characteristic. The characteristic descriptor and characteristic value belong to the same characteristic.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | server_id  | Unsigned integer type | Service ID, which determines a service                       |
  | chara_id   | Unsigned integer type | Characteristic ID                                            |
  | permission | Unsigned integer type | Permission of characteristic value. 2 bytes. Hexadecimal number. You can specify several properties at the same time by OR operations.<br/>0x0001 - Readable<br/>0x0002 - Writable<br/>0x0004 - Read requires authentication<br/>0x0008 - Read requires authorization<br/>0x0010 - Read requires encryption<br/>0x0020 - Read requires authorization and authentication<br/>0x0040 - Write requires authentication<br/>0x0080 - Write requires authorization<br/>0x0100 - Write requires encryption<br/>0x0200 - Write requires authorization and authentication |
  | uuid_type  | Unsigned integer type | uuid type<br/>0 - Long UUID, 128bit<br/>1 - Short UUID, 16bit |
  | uuid_s     | Unsigned integer type | Short UUID, 2 bytes (16bit)                                  |
  | uuid_l     | Array                 | Long UUID, 16 bytes (128bit)                                 |
  | value      | Array                 | Characteristic descriptor value                              |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
def ble_gatt_add_characteristic_desc():
    data = [0x00, 0x00]
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



##### BLE Server - Complete Addition of Services or Delete the Services

> **ble.addOrClearService(option, mode)**

* Function

  Complete the addition of services or clear the added services.

* Parameter

  | Parameter | Type                  | Description                                                  |
  | --------- | --------------------- | ------------------------------------------------------------ |
  | option    | Unsigned integer type | Operation type.<br>0 - Clear the services<br/>1 - Complete the addition of services |
  | mode      | Unsigned integer type | Retention mode of system service.<br/>0 - Delete the default system GAP and GATT services<br/>1 - Retain the default system GAP and GATT services |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Server - Send Notification

> **ble.sendNotification(connect_id, attr_handle, value)**

* Function

  Send notification.

* Parameter

  | Parameter   | Type                  | Description                                       |
  | ----------- | --------------------- | ------------------------------------------------- |
  | connect_id  | Unsigned integer type | Connection ID                                     |
  | attr_handle | Unsigned integer type | Attribute handle                                  |
  | value       | Array                 | Data to be sent. Do not send data longer than MTU |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Server - Send Indication

> **ble.sendIndication(connect_id, attr_handle, value)**

* Function

  Send indication.

* Parameter

  | Parameter   | Type                  | Description                                       |
  | ----------- | --------------------- | ------------------------------------------------- |
  | connect_id  | Unsigned integer type | Connection ID                                     |
  | attr_handle | Unsigned integer type | Attribute handle                                  |
  | value       | Array                 | Data to be sent. Do not send data longer than MTU |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Server - Start Advertising

> **ble.advStart()**

* Function

  Start advertising.

* Parameter

  * None

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

  * None

  


##### BLE Server - Stop Advertising

> **ble.advStop()**

* Function

  Stop advertising.

* Parameter

  * None

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

  * None



##### BLE Server - Comprehensive Example

```python
# -*- coding: UTF-8 -*-

import ble
import utime


BLE_GATT_SYS_SERVICE = 0  # 0-Delete the default GAP and GATT services  1-Retain the default GAP and GATT services
BLE_SERVER_HANDLE = 0
_BLE_NAME = "Quectel_ble"


event_dict = {
    'BLE_START_STATUS_IND': 0,  # ble start
    'BLE_STOP_STATUS_IND': 1,   # ble stop
    'BLE_CONNECT_IND': 16,  # ble connect
    'BLE_DISCONNECT_IND': 17,   # ble disconnect
    'BLE_UPDATE_CONN_PARAM_IND': 18,    # ble update connection parameter
    'BLE_SCAN_REPORT_IND': 19,  # ble gatt client scan and report other devices
    'BLE_GATT_MTU': 20, # ble connection mtu
    'BLE_GATT_RECV_WRITE_IND': 21, # when ble client write characteristic value or descriptor,server get the notice
    'BLE_GATT_RECV_READ_IND': 22, # when ble client read characteristic value or descriptor,server get the notice
    'BLE_GATT_RECV_NOTIFICATION_IND': 23,   # client receive notification
    'BLE_GATT_RECV_INDICATION_IND': 24, # client receive indication
    'BLE_GATT_SEND_END': 25, # server send notification,and receive send end notice
}

class EVENT(dict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        raise ValueError("{} is read-only.".format(key))


event = EVENT(event_dict)


def ble_callback(args):
    global BLE_GATT_SYS_SERVICE
    global BLE_SERVER_HANDLE
    event_id = args[0]
    status = args[1]
    print('[ble_callback]: event_id={}, status={}'.format(event_id, status))

    if event_id == event.BLE_START_STATUS_IND:  # ble start
        if status == 0:
            print('[callback] BLE start success.')
            mac = ble.getPublicAddr()
            if mac != -1 and len(mac) == 6:
                addr = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(mac[5], mac[4], mac[3], mac[2], mac[1], mac[0])
                print('BLE public addr : {}'.format(addr))
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
    elif event_id == event.BLE_STOP_STATUS_IND:  # ble stop
        if status == 0:
            print('[callback] ble stop successful.')
            ble_status = ble.getStatus()
            print('ble status is {}'.format(ble_status))
            ble_gatt_server_release()
        else:
            print('[callback] ble stop failed.')
    elif event_id == event.BLE_CONNECT_IND:  # ble connect
        if status == 0:
            print('[callback] ble connect successful.')
            connect_id = args[2]
            addr = args[3]
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))

            ret = ble_gatt_send_notification()
            if ret == 0:
                print('[callback] ble_gatt_send_notification successful.')
            else:
                print('[callback] ble_gatt_send_notification failed.')
                ble_gatt_close()
                return
        else:
            print('[callback] ble connect failed.')
    elif event_id == event.BLE_DISCONNECT_IND:  # ble disconnect
        if status == 0:
            print('[callback] ble disconnect successful.')
            connect_id = args[2]
            addr = args[3]
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            ble_gatt_close()
            print('[callback] connect_id = {}, addr = {}'.format(connect_id, addr_str))
        else:
            print('[callback] ble disconnect failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_UPDATE_CONN_PARAM_IND:  # ble update connection parameter
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
    elif event_id == event.BLE_GATT_MTU:  # ble connection mtu
        if status == 0:
            print('[callback] ble connect mtu successful.')
            handle = args[2]
            ble_mtu = args[3]
            print('[callback] handle = {:#06x}, ble_mtu = {}'.format(handle, ble_mtu))
        else:
            print('[callback] ble connect mtu failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_RECV_WRITE_IND:
        if status == 0:
            print('[callback] ble recv successful.')
            data_len = args[2]
            data = args[3]  # this is bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # this is bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_RECV_READ_IND:
        if status == 0:
            print('[callback] ble recv read successful.')
            data_len = args[2]
            data = args[3]  # this is bytearray
            attr_handle = args[4]
            short_uuid = args[5]
            long_uuid = args[6]  # this is bytearray
            print('len={}, data:{}'.format(data_len, data))
            print('attr_handle = {:#06x}'.format(attr_handle))
            print('short uuid = {:#06x}'.format(short_uuid))
            print('long uuid = {}'.format(long_uuid))
        else:
            print('[callback] ble recv read failed.')
            ble_gatt_close()
            return
    elif event_id == event.BLE_GATT_SEND_END:
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
    adv_type = 0  # Connectable and undirected broadcast, selected by default
    addr_type = 0  # public address
    channel = 0x07
    filter_strategy = 0  # Process scanning and connection requests for all devices
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
    data = [0x00, 0x00]
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
    data = [0x39, 0x39, 0x39, 0x39, 0x39]  # test data
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
    while True:
        utime.sleep(1)
        count += 1
        if count % 5 == 0:
            print('##### BLE running, count = {}......'.format(count))
        if count > 120:
            count = 0
            print('!!!!! stop BLE now !!!!!')
            ble_gatt_close()
            return 0


if __name__ == '__main__':
    main()

```



##### BLE Client - Initialize BLE and Register Callback Function

> **ble.clientInit(user_cb)**

* Function

  Initialize BLE Client and register callback function.

* Parameter

| Parameter | Tpye     | Description       |
| --------- | -------- | ----------------- |
| user_cb   | function | Callback function |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

- Description

（1）Format of callback function

```python
def ble_callback(args):
	event_id = args[0]  # The first parameter is fixed as event_id
	status = args[1] # The second parameter is fixed as status which indicates the execution result of an operation, such as BLE is enabled successfully or unsuccessfully.
	......
```

（2）Description of callback function parameter 

​		args[0] is fixed to represent event_id; args[1] is fixed to represent status. 0 indicates a success; non-0 indicates a failure. The number of callback function parameter is not fixed as 2; instead it is determined by the first parameter args[0]. The number of parameters and descriptions corresponding to the different event IDs are as follows.

| event_id | Number of Parameter | Parameter Description                                        |
| :------: | :-----------------: | ------------------------------------------------------------ |
|    0     |          2          | args[0]: event_id, which indicates BT/BLE starts<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution |
|    1     |          2          | args[0]: event_id, which indicates BT/BLE stops<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution |
|    16    |          4          | args[0]: event_id, which indicates BLE connect<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2]: connect_id<br/>args[3]: addr, BT/BLE address, data type is bytearray |
|    17    |          4          | args[0] ：event_id, which indicates BLE disconnect<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：connect_id<br/>args[3] ：addr，BT/BLE address，data type is bytearray |
|    18    |          7          | args[0]: event_id, which indicates BLE update connection parameter<br/>args[1]: status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2]: connect_id<br/>args[3]: max_interval, maximum interval. Interval: 1.25ms. Range: 6–3200. Time Range: 7.5ms–4s<br/>args[4]: min_interval, maximum interval. Interval: 1.25ms. Range: 6–3200. Time Range: 7.5ms–4s<br/>args[5]: latency, the time during which the slave ignores the connection state events. It needs to meet the formula（1+latecy)\*max_interval\*2\*1.25<timeout\*10<br/>args[6]: timeout,  the disconnection timeout period when there is no interaction, interval:10ms. Range: 10–3200. Time range: 100ms–32s. |
|    19    |          9          | args[0] ：event_id, which indicates BLE scan report<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：event_type<br/>args[3] ：Name of the scanned devices<br/>args[4] ：address type<br/>args[5] ：device's address, bytearray<br/>args[6] ：rssi, Signal strength<br/>args[7] ：data_len, the length of data<br/>args[8] ：data, Raw data scanned |
|    20    |          4          | args[0] ：event_id, which indicates BLE connection mtu<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：handle<br/>args[3] ：mtu value |
|    23    |          4          | args[0] ：event_id, which indicates client recieve notification<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：data_len, the length of data<br/>args[3] ：data, Raw data scanned, The data format and parsing are shown in the final comprehensive sample program |
|    24    |          4          | args[0] ：event_id, which indicates client recieve indication<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：data_len, the length of data<br/>args[3] ：data, Raw data scanned, The data format and parsing are shown in the final comprehensive sample program |
|    26    |          2          | args[0] ：event_id, which indicates start discovering  service<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution |
|    27    |          5          | args[0] ：event_id, which indicates discovered service<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：start_handle, which indicates the start handle of the service<br/>args[3] ：end_handle, which indicates the end handle of the service<br/>args[4] ：UUID, which indicates the UUID of the service (short UUID) |
|    28    |          4          | args[0] ：event_id, which indicates discover characteristic<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：data_len, the length of data<br/>args[3] ：data, Contain handle, attribute, UUID and other data of the raw data, data format and parsing see the last comprehensive example program |
|    29    |          4          | args[0] ：event_id, which indicates discover characteristic descriptor<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：data_len, the length of data<br/>args[3] ：data, Contain handle, UUID and other data of the raw data, data format and parsing see the last comprehensive example program |
|    30    |          2          | args[0] ：event_id, which indicates write characteristic value and require link layer confirmation<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution |
|    31    |          2          | args[0] ：event_id, which indicates write characteristic value without response<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution |
|    32    |          4          | args[0] ：event_id, which indicates read characteristic value by handle<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：data_len, the length of data<br/>args[3] ：data, Raw data |
|    33    |          4          | args[0] ：event_id, which indicates read characteristic value by uuid<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：data_len, the length of data<br/>args[3] ：data, Raw data |
|    34    |          4          | args[0] ：event_id, which indicates read miltiple characteristic value<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：data_len, the length of data<br/>args[3] ：data, Raw data |
|    35    |          2          | args[0] ：event_id, which indicates wirte characteristic descriptor and require link layer confirmation<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution |
|    36    |          4          | args[0] ：event_id, which indicates read characteristic descriptor<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：data_len, the length of data<br/>args[3] ：data, Raw data |
|    37    |          3          | args[0] ：event_id, which indicates attribute error<br/>args[1] ：status, which indicates the operation state. 0 - Successful execution; non-0 - Failed execution<br/>args[2] ：error code |

* Example

```
See comprehensive example
```



##### BLE Client - Release BLE Client Resources 

> **ble.clientRelease()**

* Function

  Release BLE Client resources.

* Parameter

  * None

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Set Scan Parameters

> **ble.setScanParam(scan_mode, interval, scan_window, filter_policy, addr_type)**

* Function

  Set scan parameters.

* Parameter

| Parameter     | Type                  | Description                                                  |
| ------------- | --------------------- | ------------------------------------------------------------ |
| scan_mode     | Unsigned integer type | Scan mode,  Active scan by default:<br>0 - Negative scan<br/>1 -Active scan. In this mode, the scan-reply data set by the broadcast end is meaningful |
| interval      | Unsigned integer type | Scanning interval, range : 0x0004-0x4000, the calculation is as follows:<br/>time interval = interval \* 0.625,  unit : ms |
| scan_window   | Unsigned integer type | The time of one scan, range : 0x0004-0x4000, the calculation is as follows:<br/>scan_time = scan_window\* 0.625，单位ms |
| filter_policy | Unsigned integer type | Scan filtering policy, default 0：<br/>0 - All broadcast packets except for directional broadcasts that are not from the device<br/>1 - Whitelisted broadcast packets of devices except for directed broadcasts that are not of the device<br/>2 - Undirectional broadcast, directional broadcast directed to the device or directional broadcast using Resolvable private address<br/>3 - Whitelist device non-directional broadcast, directional broadcast to the device or directional broadcast using Resolvable private address |
| addr_type     | Unsigned integer type | Local address type, range:<br/>0 - Public address<br/>1 - Random address |

* Notice

  Something to note about the interval and scan_window parameters : Scan time scan_window cannot be longer than the scan interval. If they are equal, it indicates continuous scanning. In this case, the BLE Controller runs continuous scanning, occupying system resources and therefore cannot perform other tasks. It is not recommended to set the time too short, the more frequent the scan, the higher the power consumption.

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Start Scanning

> **ble.scanStart()**

* Function

  Start scanning.

* Parameter

  * None

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Stop Scanning

> **ble.scanStop()**

* Function

  Stop scanning.

* Parameter

  * None

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Scan filter switch

> **ble.setScanFilter(act)**

* Function

  Turn on or off the scan filter switch. If this parameter is enabled, the broadcast data of the same device is reported only once when scanning the broadcast data of the device. If disabled, all broadcast data on the same device will be reported.The filtering function is enabled by default.

* Parameter

  | Parameter | Type                  | Description                                                  |
  | --------- | --------------------- | ------------------------------------------------------------ |
  | act       | Unsigned integer type | 0 - Turn off the scan filter switch<br/>1 - Turn on the scan filter switch |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Establish a connection

> **ble.connect(addr_type, addr)**

* Function

  Connect to the device based on the specified device address.

* Parameter

  | Parameter | Type                  | Description                                                  |
  | --------- | --------------------- | ------------------------------------------------------------ |
  | addr_type | Unsigned integer type | Address type, range:<br/>0 - Public address<br/>1 - Random address |
  | addr      | bytearray type        | device address, 6 bytes                                      |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Cancels the connection being established

> **ble.cancelConnect(addr)**

* Function

  Cancels the connection being established.

* Parameter

  | Parameter | Type           | Description             |
  | --------- | -------------- | ----------------------- |
  | addr      | bytearray type | device address, 6 bytes |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
None
```



##### BLE Client - Disconnect the connection

> **ble.disconnect(connect_id)**

* Function

  Disconnect an established connection.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | connect_id | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Scan all services

> **ble.discoverAllService(connect_id)**

* Function

  Scan all services of the device.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | connect_id | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Scans services by  UUID

> **ble.discoverByUUID(connect_id, uuid_type, uuid_s, uuid_l)**

* Function

  Scans services by  UUID.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | connect_id | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |
  | uuid_type  | Unsigned integer type | uuid type<br>0 - long UUID, 128bit<br>1 - short UUID, 16bit  |
  | uuid_s     | Unsigned integer type | short UUID, 2 bytes(16bit), When uuid_type is 0, this value is 0 |
  | uuid_l     | bytearray type        | long UUID，16 bytes(128bit),When uuid_type is 1, this value is  bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Scans all includes

> **ble.discoverAllIncludes(connect_id, start_handle, end_handle)**

* Function

  Scan all includes. Start_handle and end_handle belong to the same service.

* Parameter

  | Parameter    | Type                  | Description                                                  |
  | ------------ | --------------------- | ------------------------------------------------------------ |
  | connect_id   | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |
  | start_handle | Unsigned integer type | Start handle from which to start looking for includes        |
  | end_handle   | Unsigned integer type | end handle from which to start looking for includes          |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
None
```



##### BLE Client - Scans all characteristics

> **ble.discoverAllChara(connect_id, start_handle, end_handle)**

* Function

  Scans all characteristics. Start_handle and end_handle belong to the same service.

* Parameter

  | Parameter    | Type                  | Description                                                  |
  | ------------ | --------------------- | ------------------------------------------------------------ |
  | connect_id   | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |
  | start_handle | Unsigned integer type | Start handle from which to start looking for characteristics |
  | end_handle   | Unsigned integer type | end handle from which to start looking for characteristics   |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Scan the description of all characteristics

> **ble.discoverAllCharaDesc(connect_id, start_handle, end_handle)**

* Function

  Scan the description of all characteristics. Start_handle and end_handle belong to the same service.

* Parameter

  | Parameter    | Type                  | Description                                                  |
  | ------------ | --------------------- | ------------------------------------------------------------ |
  | connect_id   | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |
  | start_handle | Unsigned integer type | Start handle from which to start looking for characteristic description |
  | end_handle   | Unsigned integer type | end handle from which to start looking for characteristic description |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Reads the characteristic value by the specified UUID

> **ble.readCharaByUUID(connect_id, start_handle, end_handle, uuid_type, uuid_s, uuid_l)**

* Function

  Scan the description of all characteristics. Start_handle and end_handle must contain a characteristic value  handle.

* Parameter

  | Parameter    | Type                  | Description                                                  |
  | ------------ | --------------------- | ------------------------------------------------------------ |
  | connect_id   | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |
  | start_handle | Unsigned integer type | The start handle must belong to the same characteristic handle |
  | end_handle   | Unsigned integer type | The end handle must belong to the same characteristic handle |
  | uuid_type    | Unsigned integer type | uuid type<br/>0 - long UUID, 128bit<br/>1 - short UUID, 16bit |
  | uuid_s       | Unsigned integer type | short UUID, 2 bytes(16bit), When uuid_type is 0, this value is 0 |
  | uuid_l       | bytearray type        | long UUID，16 bytes(128bit),When uuid_type is 1, this value is  bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Reads the characteristic value by the specified handle

> **ble.readCharaByHandle(connect_id, handle, offset, is_long)**

* Function

  Reads the characteristic value by the specified handle.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | connect_id | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |
  | handle     | Unsigned integer type | the handle of characteristic value                           |
  | offset     | Unsigned integer type | offset                                                       |
  | is_long    | Unsigned integer type | Long characteristic value flag<br/>0 - Short characteristic value, It can be read all at once<br/>1 - Long characteristic value, It needs to be read multiple times |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Reads the characteristic description 

> **ble.readCharaDesc(connect_id, handle, is_long)**

* Function

  Reads the characteristic description.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | connect_id | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |
  | handle     | Unsigned integer type | the handle of characteristic description                     |
  | is_long    | Unsigned integer type | Long characteristic descriptionflag<br/>0 - Short characteristic description<br/>1 - Long characteristic description |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client - Writes the characteristic value(require link layer response)

> **ble.writeChara(connect_id, handle, offset, is_long, data)**

* Function

  Writes the characteristic value  and require link layer response.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | connect_id | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |
  | handle     | Unsigned integer type | the handle of characteristic value                           |
  | offset     | Unsigned integer type | offset                                                       |
  | is_long    | Unsigned integer type | Long characteristic value flag<br/>0 - Short characteristic value, It can be read all at once<br/>1 - Long characteristic value, It needs to be read multiple times |
  | data       | bytearray type        | the data of characteristic value                             |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
None
```



##### BLE Client - Writes the characteristic value(Without link layer response)

> **ble.writeCharaNoRsp(connect_id, handle, data)**

* Function

  Writes the characteristic value  without link layer response.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | connect_id | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |
  | handle     | Unsigned integer type | the handle of characteristic value                           |
  | data       | bytearray type        | the data of characteristic value                             |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
None
```



##### BLE Client - Writes the characteristic description 

> **ble.writeCharaDesc(connect_id, handle, data)**

* Function

  Writes the characteristic description.

* Parameter

  | Parameter  | Type                  | Description                                                  |
  | ---------- | --------------------- | ------------------------------------------------------------ |
  | connect_id | Unsigned integer type | Connection ID, the connection ID obtained when establishing the connection |
  | handle     | Unsigned integer type | the handle of characteristic description                     |
  | data       | bytearray type        | the data of characteristic description                       |

* Return Value

  * 0	 Successful execution
  * -1	Failed execution

* Example

```python
See comprehensive example
```



##### BLE Client- Comprehensive Example

```python
# -*- coding: UTF-8 -*-

import ble
import utime
import _thread
import checkNet
from queue import Queue

PROJECT_NAME = "QuecPython_BLE_Client_Example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

event_dict = {
    'BLE_START_STATUS_IND': 0,  # ble start
    'BLE_STOP_STATUS_IND': 1,   # ble stop
    'BLE_CONNECT_IND': 16,  # ble connect
    'BLE_DISCONNECT_IND': 17,   # ble disconnect
    'BLE_UPDATE_CONN_PARAM_IND': 18,    # ble update connection parameter
    'BLE_SCAN_REPORT_IND': 19,  # ble gatt client scan and report other devices
    'BLE_GATT_MTU': 20, # ble connection mtu
    'BLE_GATT_RECV_NOTIFICATION_IND': 23,   # client receive notification
    'BLE_GATT_RECV_INDICATION_IND': 24, # client receive indication
    'BLE_GATT_START_DISCOVER_SERVICE_IND': 26,  # start discover service
    'BLE_GATT_DISCOVER_SERVICE_IND': 27,    # discover service
    'BLE_GATT_DISCOVER_CHARACTERISTIC_DATA_IND': 28,    # discover characteristic
    'BLE_GATT_DISCOVER_CHARA_DESC_IND': 29, # discover characteristic descriptor
    'BLE_GATT_CHARA_WRITE_WITH_RSP_IND': 30,    # write characteristic value with response
    'BLE_GATT_CHARA_WRITE_WITHOUT_RSP_IND': 31, # write characteristic value without response
    'BLE_GATT_CHARA_READ_IND': 32,  # read characteristic value by handle
    'BLE_GATT_CHARA_READ_BY_UUID_IND': 33,  # read characteristic value by uuid
    'BLE_GATT_CHARA_MULTI_READ_IND': 34,    # read multiple characteristic value
    'BLE_GATT_DESC_WRITE_WITH_RSP_IND': 35, # write characteristic descriptor
    'BLE_GATT_DESC_READ_IND': 36,   # read characteristic descriptor
    'BLE_GATT_ATT_ERROR_IND': 37,   # attribute error
}

gatt_status_dict = {
    'BLE_GATT_IDLE' : 0,
    'BLE_GATT_DISCOVER_SERVICE': 1,
    'BLE_GATT_DISCOVER_INCLUDES': 2,
    'BLE_GATT_DISCOVER_CHARACTERISTIC': 3,
    'BLE_GATT_WRITE_CHARA_VALUE': 4,
    'BLE_GATT_WRITE_CHARA_DESC': 5,
    'BLE_GATT_READ_CHARA_VALUE': 6,
    'BLE_GATT_READ_CHARA_DESC': 7,
}

class EVENT(dict):
    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        raise ValueError("{} is read-only.".format(key))


class BleClient(object):
    def __init__(self):
        self.ble_server_name = 'Quectel_ble' # Ble name of the target device
        self.connect_id = 0
        self.connect_addr = 0
        self.gatt_statue = 0
        self.discover_service_mode = 0 # 0-discover all service, 1-discover service by uuid

        self.scan_param = {
            'scan_mode' : 1, # Active scanning
            'interval' : 0x100,
            'scan_window' : 0x50,
            'filter_policy' : 0,
            'local_addr_type' : 0,
        }

        self.scan_report_info = {
            'event_type' : 0,
            'name' : '',
            'addr_type' : 0,
            'addr' : 0,
            'rssi' : 0,
            'data_len' : 0,
            'raw_data' : 0,
        }

        self.target_service = {
            'start_handle' : 0,
            'end_handle' : 0,
            'uuid_type' : 1, # short uuid
            'short_uuid' : 0x180F, # Battery power service
            'long_uuid' : bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        }

        self.characteristic_list = []
        self.descriptor_list = []
        self.characteristic_count = 0   # ql_ble_gatt_chara_count
        self.chara_descriptor_count = 0 # ql_ble_gatt_chara_desc_count
        self.characteristic_index = 0   # ql_ble_gatt_chara_desc_index
        self.current_chara_index = 0    # ql_ble_gatt_cur_chara
        self.current_desc_index = 0     # ql_ble_gatt_chara_cur_desc
        self.ble_short_uuid_pair_len = 7
        self.ble_long_uuid_pair_len = 21

        ret = ble.clientInit(self.ble_client_callback)
        if ret != 0:
            print('ble client initialize failed.')
            raise ValueError("BLE Client Init failed.")
        else:
            print('ble client initialize successful.')
        print('')

    @staticmethod
    def gatt_open():
        ret = ble.gattStart()
        if ret != 0:
            print('ble open failed.')
        else:
            print('ble open successful.')
        print('')
        return ret

    @staticmethod
    def gatt_close():
        ret = ble.gattStop()
        if ret != 0:
            print('ble close failed.')
        else:
            print('ble close successful.')
        print('')
        return ret

    @staticmethod
    def gatt_get_status():
        return ble.getStatus()

    @staticmethod
    def release():
        ret = ble.clientRelease()
        if ret != 0:
            print('ble client release failed.')
        else:
            print('ble client release successful.')
        print('')
        return ret

    def set_scan_param(self):
        scan_mode = self.scan_param['scan_mode']
        interval = self.scan_param['interval']
        scan_time = self.scan_param['scan_window']
        filter_policy = self.scan_param['filter_policy']
        local_addr_type = self.scan_param['local_addr_type']
        ret = ble.setScanParam(scan_mode, interval, scan_time, filter_policy, local_addr_type)
        if ret != 0:
            print('ble client set scan-parameters failed.')
        else:
            print('ble client set scan-parameters successful.')
        print('')
        return ret

    @staticmethod
    def start_scan():
        ret = ble.scanStart()
        if ret != 0:
            print('ble client scan failed.')
        else:
            print('ble client scan successful.')
        print('')
        return ret

    @staticmethod
    def stop_scan():
        ret = ble.scanStop()
        if ret != 0:
            print('ble client failed to stop scanning.')
        else:
            print('ble client scan stopped successfully.')
        print('')
        return ret

    def connect(self):
        print('start to connect.....')
        addr_type = self.scan_report_info['addr_type']
        addr = self.scan_report_info['addr']
        if addr != 0 and len(addr) == 6:
            addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
            print('addr_type : {}, addr : {}'.format(addr_type, addr_str))
            ret = ble.connect(addr_type, addr)
            if ret != 0:
                print('ble client connect failed.')
            else:
                print('ble client connect successful.')
            print('')
            return ret

    def cancel_connect(self):
        ret = ble.cancelConnect(self.scan_report_info['addr'])
        if ret != 0:
            print('ble client cancel connect failed.')
        else:
            print('ble client cancel connect successful.')
        print('')
        return ret

    def disconnect(self):
        ret = ble.disconnect(self.connect_id)
        if ret != 0:
            print('ble client disconnect failed.')
        else:
            print('ble client disconnect successful.')
        print('')
        return ret

    def discover_all_service(self):
        ret = ble.discoverAllService(self.connect_id)
        if ret != 0:
            print('ble client discover all service failed.')
        else:
            print('ble client discover all service successful.')
        print('')
        return ret

    def discover_service_by_uuid(self):
        connect_id = self.connect_id
        uuid_type = self.target_service['uuid_type']
        short_uuid = self.target_service['short_uuid']
        long_uuid = self.target_service['long_uuid']
        ret = ble.discoverByUUID(connect_id, uuid_type, short_uuid, long_uuid)
        if ret != 0:
            print('ble client discover service by uuid failed.')
        else:
            print('ble client discover service by uuid successful.')
        print('')
        return ret

    def discover_all_includes(self):
        connect_id = self.connect_id
        start_handle = self.target_service['start_handle']
        end_handle = self.target_service['end_handle']
        ret = ble.discoverAllIncludes(connect_id, start_handle, end_handle)
        if ret != 0:
            print('ble client discover all includes failed.')
        else:
            print('ble client discover all includes successful.')
        print('')
        return ret

    def discover_all_characteristic(self):
        connect_id = self.connect_id
        start_handle = self.target_service['start_handle']
        end_handle = self.target_service['end_handle']
        ret = ble.discoverAllChara(connect_id, start_handle, end_handle)
        if ret != 0:
            print('ble client discover all characteristic failed.')
        else:
            print('ble client discover all characteristic successful.')
        print('')
        return ret

    def discover_all_characteristic_descriptor(self):
        connect_id = self.connect_id
        index = self.characteristic_index
        start_handle = self.characteristic_list[index]['value_handle'] + 1

        if self.characteristic_index == (self.characteristic_count - 1):
            end_handle = self.target_service['end_handle']
            print('[1]start_handle = {:#06x}, end_handle = {:#06x}'.format(start_handle - 1, end_handle))
            ret = ble.discoverAllCharaDesc(connect_id, start_handle, end_handle)
        else:
            end_handle = self.characteristic_list[index+1]['handle'] - 1
            print('[2]start_handle = {:#06x}, end_handle = {:#06x}'.format(start_handle - 1, end_handle))
            ret = ble.discoverAllCharaDesc(connect_id, start_handle, end_handle)
        self.characteristic_index += 1
        if ret != 0:
            print('ble client discover all characteristic descriptor failed.')
        else:
            print('ble client discover all characteristic descriptor successful.')
        print('')
        return ret

    def read_characteristic_by_uuid(self):
        connect_id = self.connect_id
        index = self.current_chara_index   # Change this value as needed
        start_handle = self.characteristic_list[index]['handle']
        end_handle = self.characteristic_list[index]['value_handle']
        uuid_type = 1
        short_uuid = self.characteristic_list[index]['short_uuid']
        long_uuid = bytearray([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])

        ret = ble.readCharaByUUID(connect_id, start_handle, end_handle, uuid_type, short_uuid, long_uuid)
        if ret != 0:
            print('ble client read characteristic by uuid failed.')
        else:
            print('ble client read characteristic by uuid successful.')
        print('')
        return ret

    def read_characteristic_by_handle(self):
        connect_id = self.connect_id
        index = self.current_chara_index  # Change this value as needed
        handle = self.characteristic_list[index]['value_handle']
        offset = 0
        is_long = 0

        ret = ble.readCharaByHandle(connect_id, handle, offset, is_long)
        if ret != 0:
            print('ble client read characteristic by handle failed.')
        else:
            print('ble client read characteristic by handle successful.')
        print('')
        return ret

    def read_characteristic_descriptor(self):
        connect_id = self.connect_id
        index = self.current_desc_index  # Change this value as needed
        handle = self.descriptor_list[index]['handle']
        print('handle = {:#06x}'.format(handle))
        is_long = 0
        ret = ble.readCharaDesc(connect_id, handle, is_long)
        if ret != 0:
            print('ble client read characteristic descriptor failed.')
        else:
            print('ble client read characteristic descriptor successful.')
        print('')
        return ret

    def write_characteristic(self):
        connect_id = self.connect_id
        index = self.current_chara_index  # Change this value as needed
        handle = self.characteristic_list[index]['value_handle']
        offset = 0
        is_long = 0
        data = bytearray([0x40, 0x00])
        print('value_handle = {:#06x}, uuid = {:#06x}'.format(handle, self.characteristic_list[index]['short_uuid']))
        ret = ble.writeChara(connect_id, handle, offset, is_long, data)
        if ret != 0:
            print('ble client write characteristic failed.')
        else:
            print('ble client read characteristic successful.')
        print('')
        return ret

    def write_characteristic_no_rsp(self):
        connect_id = self.connect_id
        index = self.current_chara_index  # Change this value as needed
        handle = self.characteristic_list[index]['value_handle']
        data = bytearray([0x20, 0x00])
        print('value_handle = {:#06x}, uuid = {:#06x}'.format(handle, self.characteristic_list[index]['short_uuid']))
        ret = ble.writeCharaNoRsp(connect_id, handle, data)
        if ret != 0:
            print('ble client write characteristic no rsp failed.')
        else:
            print('ble client read characteristic no rsp successful.')
        print('')
        return ret

    def write_characteristic_descriptor(self):
        connect_id = self.connect_id
        index = self.current_desc_index  # Change this value as needed
        handle = self.descriptor_list[index]['handle']
        data = bytearray([0x01, 0x02])
        print('handle = {:#06x}'.format(handle))

        ret = ble.writeCharaDesc(connect_id, handle, data)
        if ret != 0:
            print('ble client write characteristic descriptor failed.')
        else:
            print('ble client read characteristic descriptor successful.')
        print('')
        return ret

    @staticmethod
    def ble_client_callback(args):
        global msg_queue
        msg_queue.put(args)


def ble_gatt_client_event_handler():
    global msg_queue
    old_time = 0

    while True:
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])
        if cur_time[5] != old_time and cur_time[5] % 5 == 0:
            old_time = cur_time[5]
            print('[{}]event handler running.....'.format(timestamp))
            print('')
        msg = msg_queue.get()  # It's blocked here when there's no message
        # print('msg : {}'.format(msg))
        event_id = msg[0]
        status = msg[1]

        if event_id == event.BLE_START_STATUS_IND:
            print('')
            print('event_id : BLE_START_STATUS_IND, status = {}'.format(status))
            if status == 0:
                print('BLE start successful.')
                ble_status = ble_client.gatt_get_status()
                if ble_status == 0:
                    print('BLE Status : stopped.')
                    break
                elif ble_status == 1:
                    print('BLE Status : started.')
                else:
                    print('get ble status error.')
                    ble_client.gatt_close()
                    break

                ret = ble_client.set_scan_param()
                if ret != 0:
                    ble_client.gatt_close()
                    break
                ret = ble_client.start_scan()
                if ret != 0:
                    ble_client.gatt_close()
                    break
            else:
                print('BLE start failed.')
                break
        elif event_id == event.BLE_STOP_STATUS_IND:
            print('')
            print('event_id : BLE_STOP_STATUS_IND, status = {}'.format(status))
            if status == 0:
                print('ble stop successful.')
            else:
                print('ble stop failed.')
                break
        elif event_id == event.BLE_CONNECT_IND:
            print('')
            print('event_id : BLE_CONNECT_IND, status = {}'.format(status))
            if status == 0:
                ble_client.connect_id = msg[2]
                ble_client.connect_addr = msg[3]
                addr = ble_client.connect_addr
                addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
                print('connect_id : {:#x}, connect_addr : {}'.format(ble_client.connect_id, addr_str))
            else:
                print('ble connect failed.')
                break
        elif event_id == event.BLE_DISCONNECT_IND:
            print('')
            print('event_id : BLE_DISCONNECT_IND, status = {}'.format(status))
            if status == 0:
                ble_client.connect_id = msg[2]
                ble_client.connect_addr = msg[3]
                addr = ble_client.connect_addr
                addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
                print('connect_id : {:#x}, connect_addr : {}'.format(ble_client.connect_id, addr_str))
            else:
                print('ble disconnect failed.')
            ble_client.gatt_close()
            break
        elif event_id == event.BLE_UPDATE_CONN_PARAM_IND:
            print('')
            print('event_id : BLE_UPDATE_CONN_PARAM_IND, status = {}'.format(status))
            if status == 0:
                connect_id = msg[2]
                max_interval = msg[3]
                min_interval = msg[4]
                latency = msg[5]
                timeout = msg[6]
                print('connect_id={},max_interval={},min_interval={},latency={},timeout={}'.format(connect_id,max_interval,min_interval,latency,timeout))
            else:
                print('ble update parameter failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_SCAN_REPORT_IND:
            if status == 0:
                # print(' ble scan successful.')

                ble_client.scan_report_info['event_type'] = msg[2]
                ble_client.scan_report_info['name'] = msg[3]
                ble_client.scan_report_info['addr_type'] = msg[4]
                ble_client.scan_report_info['addr'] = msg[5]
                ble_client.scan_report_info['rssi'] = msg[6]
                ble_client.scan_report_info['data_len'] = msg[7]
                ble_client.scan_report_info['raw_data'] = msg[8]

                device_name = ble_client.scan_report_info['name']
                addr = ble_client.scan_report_info['addr']
                rssi = ble_client.scan_report_info['rssi']
                addr_type = ble_client.scan_report_info['addr_type']
                addr_str = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
                if device_name != '' and rssi != 0:
                    print('name: {}, addr: {}, rssi: {}, addr_type: {}'.format(device_name, addr_str, rssi, addr_type))
                    print('raw_data: {}'.format(ble_client.scan_report_info['raw_data']))

                if device_name == ble_client.ble_server_name: # Stop scanning when the target device is detected
                    ret = ble_client.stop_scan()
                    if ret != 0:
                        ble_client.gatt_close()
                        break

                    ret = ble_client.connect()
                    if ret != 0:
                        ble_client.gatt_close()
                        break
            else:
                print('ble scan failed.')
                ret = ble_client.stop_scan()
                if ret != 0:
                    ble_client.gatt_close()
                    break
        elif event_id == event.BLE_GATT_MTU:
            print('')
            print('event_id : BLE_GATT_MTU, status = {}'.format(status))
            if status == 0:
                handle = msg[2]
                ble_mtu = msg[3]
                print('handle = {:#06x}, ble_mtu = {}'.format(handle, ble_mtu))
            else:
                print('ble connect mtu failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_RECV_NOTIFICATION_IND:
            print('')
            print('event_id : BLE_GATT_RECV_NOTIFICATION_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('len={}, data:{}'.format(data_len, data))
                handle = (data[1] << 8) | data[0]
                print('handle = {:#06x}'.format(handle))
            else:
                print('ble receive notification failed.')
                break
        elif event_id == event.BLE_GATT_RECV_INDICATION_IND:
            print('')
            print('event_id : BLE_GATT_RECV_INDICATION_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('len={}, data:{}'.format(data_len, data))
            else:
                print('ble receive indication failed.')
                break
        elif event_id == event.BLE_GATT_START_DISCOVER_SERVICE_IND:
            print('')
            print('event_id : BLE_GATT_START_DISCOVER_SERVICE_IND, status = {}'.format(status))
            if status == 0:
                ble_client.characteristic_count = 0
                ble_client.chara_descriptor_count = 0
                ble_client.characteristic_index = 0
                ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_SERVICE

                if ble_client.discover_service_mode == 0:
                    print('execute the function discover_all_service.')
                    ret = ble_client.discover_all_service()
                else:
                    print('execute the function discover_service_by_uuid.')
                    ret = ble_client.discover_service_by_uuid()
                if ret != 0:
                    print('Execution result: Failed.')
                    ble_client.gatt_close()
                    break
            else:
                print('ble start discover service failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_DISCOVER_SERVICE_IND:
            print('')
            print('event_id : BLE_GATT_DISCOVER_SERVICE_IND, status = {}'.format(status))
            if status == 0:
                start_handle = msg[2]
                end_handle = msg[3]
                short_uuid = msg[4]
                print('start_handle = {:#06x}, end_handle = {:#06x}, short_uuid = {:#06x}'.format(start_handle, end_handle, short_uuid))
                if ble_client.discover_service_mode == 0: # discover service all
                    if ble_client.target_service['short_uuid'] == short_uuid: # After all services are found, searches for characteristic values based on the specified UUID
                        ble_client.target_service['start_handle'] = start_handle
                        ble_client.target_service['end_handle'] = end_handle
                        ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC
                        print('execute the function discover_all_characteristic.')
                        ret = ble_client.discover_all_characteristic()
                        if ret != 0:
                            print('Execution result: Failed.')
                            ble_client.gatt_close()
                            break
                else:
                    ble_client.target_service['start_handle'] = start_handle
                    ble_client.target_service['end_handle'] = end_handle
                    ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC
                    print('execute the function discover_all_characteristic.')
                    ret = ble_client.discover_all_characteristic()
                    if ret != 0:
                        print('Execution result: Failed.')
                        ble_client.gatt_close()
                        break
            else:
                print('ble discover service failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_DISCOVER_CHARACTERISTIC_DATA_IND:
            print('')
            print('event_id : BLE_GATT_DISCOVER_CHARACTERISTIC_DATA_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                pair_len = data[0]
                print('pair_len={}, len={}, data:{}'.format(pair_len, data_len, data))
                if data_len > 0:
                    if ble_client.gatt_statue == gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC:
                        i = 0
                        while i < (data_len - 1) / pair_len:
                            chara_dict = {
                                'handle': (data[i * pair_len + 2] << 8) | data[i * pair_len + 1],
                                'properties': data[i * pair_len + 3],
                                'value_handle': (data[i * pair_len + 5] << 8) | data[i * pair_len + 4],
                                'uuid_type': 0,
                                'short_uuid': 0x0000,
                                'long_uuid': bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
                            }
                            print('handle={:#06x}, properties={:#x}, value_handle={:#06x}'.format(chara_dict['handle'], chara_dict['properties'], chara_dict['value_handle']))
                            if pair_len == ble_client.ble_short_uuid_pair_len:
                                chara_dict['uuid_type'] = 1
                                chara_dict['short_uuid'] = (data[i * pair_len + 7] << 8) | data[i * pair_len + 6]
                                print('short_uuid:{:#06x}'.format(chara_dict['short_uuid']))
                            elif pair_len == ble_client.ble_long_uuid_pair_len:
                                start_index = i * pair_len + 6
                                end_index = start_index + 16
                                chara_dict['uuid_type'] = 0
                                chara_dict['long_uuid'] = data[start_index : end_index]
                                print('long_uuid:{}'.format(chara_dict['long_uuid']))
                            i += 1
                            if ble_client.characteristic_count < 5:
                                ble_client.characteristic_list.append(chara_dict)
                                ble_client.characteristic_count = len(ble_client.characteristic_list)
                            print('characteristic_list len = {}'.format(ble_client.characteristic_count))
                    elif ble_client.gatt_statue == gatt_status.BLE_GATT_READ_CHARA_VALUE:
                        print('data_len = {}'.format(data_len))
                        print('pay_load = {:02x},{:02x},{:02x},{:02x}'.format(data[0], data[1], data[2], data[3]))
            else:
                print('ble discover characteristic failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_DISCOVER_CHARA_DESC_IND:
            print('')
            print('event_id : BLE_GATT_DISCOVER_CHARA_DESC_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                fmt = data[0]
                print('fmt={}, len={}, data:{}'.format(fmt, data_len, data))
                if data_len > 0:
                    i = 0
                    if fmt == 1:  # 16 bit uuid
                        while i < (data_len - 1) / 4:
                            descriptor_dict = {
                                'handle': (data[i * 4 + 2] << 8) | data[i * 4 + 1],
                                'short_uuid': (data[i * 4 + 4] << 8) | data[i * 4 + 3],
                            }
                            print('handle={:#06x}, uuid={:#06x}'.format(descriptor_dict['handle'], descriptor_dict['short_uuid']))
                            i += 1
                            if ble_client.chara_descriptor_count < 5:
                                ble_client.descriptor_list.append(descriptor_dict)
                                ble_client.chara_descriptor_count = len(ble_client.descriptor_list)
                            print('descriptor_list len = {}'.format(ble_client.chara_descriptor_count))
                if ble_client.characteristic_index == ble_client.characteristic_count:
                    print('execute the function read_characteristic_by_uuid.')
                    # ble_client.gatt_statue = gatt_status.BLE_GATT_WRITE_CHARA_VALUE
                    # ret = ble_client.write_characteristic()
                    # ret = ble_client.write_characteristic_no_rsp()

                    ble_client.gatt_statue = gatt_status.BLE_GATT_READ_CHARA_VALUE
                    ret = ble_client.read_characteristic_by_uuid()
                    # ret = ble_client.read_characteristic_by_handle()

                    # ble_client.gatt_statue = gatt_status.BLE_GATT_READ_CHARA_DESC
                    # ret = ble_client.read_characteristic_descriptor()

                    # ble_client.gatt_statue = gatt_status.BLE_GATT_WRITE_CHARA_DESC
                    # ret = ble_client.write_characteristic_descriptor()
                else:
                    print('execute the function discover_all_characteristic_descriptor.')
                    ret = ble_client.discover_all_characteristic_descriptor()
                if ret != 0:
                    print('Execution result: Failed.')
                    ble_client.gatt_close()
                    break
            else:
                print('ble discover characteristic descriptor failed.')
                ble_client.gatt_close()
                break
        elif event_id == event.BLE_GATT_CHARA_WRITE_WITH_RSP_IND:
            print('')
            print('event_id : BLE_GATT_CHARA_WRITE_WITH_RSP_IND, status = {}'.format(status))
            if status == 0:
                if ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_VALUE:
                    pass
                elif ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_DESC:
                    pass
            else:
                print('ble write characteristic with response failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_WRITE_WITHOUT_RSP_IND:
            print('')
            print('event_id : BLE_GATT_CHARA_WRITE_WITHOUT_RSP_IND, status = {}'.format(status))
            if status == 0:
                print('write characteristic value without response successful.')
            else:
                print('write characteristic value without response failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_READ_IND:
            print('')
            # read characteristic value by handle
            print('event_id : BLE_GATT_CHARA_READ_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
                if ble_client.gatt_statue == gatt_status.BLE_GATT_READ_CHARA_VALUE:
                    # print('read characteristic value by handle.')
                    pass
            else:
                print('ble read characteristic failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_READ_BY_UUID_IND:
            print('')
            # read characteristic value by uuid
            print('event_id : BLE_GATT_CHARA_READ_BY_UUID_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
                handle = (data[2] << 8) | data[1]
                print('handle = {:#06x}'.format(handle))
            else:
                print('ble read characteristic by uuid failed.')
                break
        elif event_id == event.BLE_GATT_CHARA_MULTI_READ_IND:
            print('')
            # read multiple characteristic value
            print('event_id : BLE_GATT_CHARA_MULTI_READ_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
            else:
                print('ble read multiple characteristic by uuid failed.')
                break
        elif event_id == event.BLE_GATT_DESC_WRITE_WITH_RSP_IND:
            print('')
            print('event_id : BLE_GATT_DESC_WRITE_WITH_RSP_IND, status = {}'.format(status))
            if status == 0:
                if ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_VALUE:
                    pass
                elif ble_client.gatt_statue == gatt_status.BLE_GATT_WRITE_CHARA_DESC:
                    pass
            else:
                print('ble write characteristic descriptor failed.')
                break
        elif event_id == event.BLE_GATT_DESC_READ_IND:
            print('')
            # read characteristic descriptor
            print('event_id : BLE_GATT_DESC_READ_IND, status = {}'.format(status))
            if status == 0:
                data_len = msg[2]
                data = msg[3]
                print('data_len = {}, data : {}'.format(data_len, data))
                if ble_client.gatt_statue == gatt_status.BLE_GATT_READ_CHARA_DESC:
                    # print('read characteristic descriptor.')
                    pass
            else:
                print('ble read characteristic descriptor failed.')
                break
        elif event_id == event.BLE_GATT_ATT_ERROR_IND:
            print('')
            print('event_id : BLE_GATT_ATT_ERROR_IND, status = {}'.format(status))
            if status == 0:
                errcode = msg[2]
                print('errcode = {:#06x}'.format(errcode))
                if ble_client.gatt_statue == gatt_status.BLE_GATT_DISCOVER_INCLUDES:
                    ble_client.gatt_statue = gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC
                    print('execute the function discover_all_characteristic.')
                    ret = ble_client.discover_all_characteristic()
                    if ret != 0:
                        print('Execution result: Failed.')
                        ble_client.gatt_close()
                        break
                elif ble_client.gatt_statue == gatt_status.BLE_GATT_DISCOVER_CHARACTERISTIC:
                    ble_client.gatt_statue = gatt_status.BLE_GATT_IDLE
                    print('execute the function discover_all_characteristic_descriptor.')
                    ret = ble_client.discover_all_characteristic_descriptor()
                    if ret != 0:
                        print('Execution result: Failed.')
                        ble_client.gatt_close()
                        break
            else:
                print('ble attribute error.')
                ble_client.gatt_close()
                break
        else:
            print('unknown event id : {}.'.format(event_id))

    # ble_client.release()


event = EVENT(event_dict)
gatt_status = EVENT(gatt_status_dict)
msg_queue = Queue(50)
ble_client = BleClient()


def main():
    checknet.poweron_print_once()
    print('create client event handler task.')
    _thread.start_new_thread(ble_gatt_client_event_handler, ())
    # ble.setScanFilter(0) # Disable the scan filtering function
    ret = ble_client.gatt_open()
    if ret != 0:
        return -1

    count = 0
    while True:
        utime.sleep(1)
        count += 1
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])
        if count % 5 == 0:
            print('[{}] BLE Client running, count = {}......'.format(timestamp, count))
            print('')
        if count > 130: # Here set the count is to run the program for a while to exit, convenient test, according to the actual needs of the user to deal with
            count = 0
            print('!!!!! stop BLE Client now !!!!!')
            ble_status = ble_client.gatt_get_status()
            if ble_status == 1:
                ble_client.gatt_close()
            ble_client.release()
            break
        else:
            ble_status = ble_client.gatt_get_status()
            if ble_status == 0: # stopped
                print('BLE connection has been disconnected.')
                ble_client.release()
                break

if __name__ == '__main__':
    main()

```



#### BT - Classic Bluetooth

Features: The module provides the related features of classic Bluetooth, and supports HFP, A2DP, AVRCP and SPP.

##### Initialize Bluetooth 

> **bt.init(user_cb)**

* Feature

This function initializes Bluetooth and registers callback function.

* Parameter

| Parameter | Type     | Description       |
| --------- | -------- | ----------------- |
| user_cb   | function | Callback function |

* Return Value

​        0       Successful execution.

​        -1      Failed execution.

Description:

a) The form of the callback function

```python
def bt_callback(args):
	event_id = args[0]  # The first parameter is fixed at event_id
	status = args[1] # The second parameter is fixed at status, indicating whether the execution result of an operation is successful or not.
	......
```

b) The description of callback function parameters 

args[0]  is fixed at event_id, args[1]  is fixed at status, 0 indicates success, other values indicate failure. The number of parameters of the callback function is not fixed at 2, but is determined by the first parameter args[0]. The following table lists the number of parameters and descriptions corresponding to different event IDs.

| event_id | Number of Parameters | Description of Parameters                                    |
| :------: | :------------------: | ------------------------------------------------------------ |
|    0     |          2           | args[0]: event_id, indicating BT/BLE start event.<br>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure. |
|    1     |          2           | args[0]: event_id, indicating BT/BLE stop event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure. |
|    6     |          6           | args[0]: event_id, indicating BT inquiry event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: rssi, indicating the signal strength of the searched device.<br/>args[3]: device_class <br/>args[4]: device_name, string type, indicating the device name.<br/>args[5]: addr, indicating the MAC address of searched Bluetooth device. |
|    7     |          3           | args[0]: event_id, indicating BT inquiry end event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: end_status, 0 indicates ending the search normally, 8 indicates ending the search forcefully. |
|    14    |          4           | args[0]: event_id, indicating BT SPP receiving event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: data_len, indicating the length of received data.<br/>args[3]: data, bytearray type, indicating the received data. |
|    40    |          4           | args[0]: event_id, indicating BT HFP connection event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_connect_status, indicating the connection status of HFP.<br/>               0 - Disconnected<br/>               1 - Connecting<br/>               2 - Connected<br/>               3 - Disconnecting<br/>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    41    |          4           | args[0]: event_id, indicating BT HFP disconnection event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_connect_status, indicating the connection status of HFP.<br/>               0 - Disconnected<br/>               1 - Connecting<br/>               2 - Connected<br/>               3 - Disconnecting<br/>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    42    |          4           | args[0]: event_id, indicating BT HFP call status event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_call_status. Indicates the call status of HFP.<br/>               0 - No calls (held or active)<br/>               1 - Call is present (active or held)<br/> args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    43    |          4           | args[0]: event_id, indicating BT HFP call setup status event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_call_setup_status, indicating the call setup status of HFP.<br/>               0 - No call setup in progress<br/>               1 - Incoming call setup in progress<br/>               2 - Outgoing call setup in dialing state<br/>               3 - Outgoing call setup in alerting state<br/>T args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    44    |          4           | args[0]: event_id, indicating BT HFP network status event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_network_status, indicating the network status of AG.<br/>               0 - Network is unavailable<br/>               1 - Network is normal<br/>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    45    |          4           | args[0]: event_id, indicating BT HFP network signal event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_network_signal, indicating the signal of AG. Range: 0–5.<br/>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    46    |          4           | args[0]: event_id, indicating BT HFP battery level event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_battery_level, indicating the battery level of AG. Range: 0–5.<br/>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    47    |          4           | args[0]: event_id, indicating BT HFP call held status event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_call_held_status, indicating the call held status of HFP.<br/>               0 - No calls held<br/>               1 - Call is placed on hold or active/held calls swapped<br/>               2 - Call on hold, no active call<br/>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    48    |          4           | args[0]: event_id, indicating BT HFP audio status event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_audio_status, indicating the connection status of audio.<br/>                 0 - Audio is disconnected<br/>                 1 - Audio is connecting<br/>                 2 - Audio is connected<br/>                 3 - Audio is disconnecting<br>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    49    |          4           | args[0]: event_id, indicating BT HFP volume type event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_volume_type<br/>               0 - The volume type is speaker<br/>               1 - The volume type is microphone<br/>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    50    |          4           | args[0]: event_id, indicating BT HFP service type event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_service_type, indicating the network service mode of AG.<br/>                 0 - AG is currently in normal network mode<br/>                 1 - AG is currently in roaming mode<br/>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    51    |          4           | args[0]: event_id, indicating the BT HFP ring event, that is, the ring event when there is an incoming call<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: Currently moot, reserved.<br/>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    52    |          4           | args[0]: event_id, indicating the BT HFP codec type event, that is, the codec mode.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: hfp_codec_type, indicating which codec mode is currently used;<br/>                 1 - CVDS with 8 KHz sampling rate<br/>                 2 - mSBC with 16 KHz sampling rate<br/>args[3]: addr, bytearray type, indicating the address of Bluetooth master device. |
|    61    |          4           | args[0]: event_id, indicating BT SPP connection event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: spp_connect_status, indicating the connection status of SPP.<br/>                 0 - Disconnected<br/>                 1 - Connecting<br/>                 2 - Connected<br/>                 3 - Disconnecting<br/> args[3]: addr, bytearray type, indicating the MAC address of the peer device. |
|    62    |          4           | args[0]: event_id, indicating BT SPP disconnection event.<br/>args[1]: status, indicating the status of the operation. 0 indicates success, other values indicate failure.<br/>args[2]: spp_connect_status, indicating the connection status of SPP.<br/>               0 - Disconnected<br/>               1 - Connecting<br/>               2 - Connected<br/>               3 - Disconnecting<br/> args[3]: addr, bytearray type, indicating the MAC address of the peer device. |

* Example

```python 

```



##### Release Bluetooth Resources

> **bt.release()**

* Feature

  This function releases Bluetooth resources.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Enable Bluetooth

> **bt.start()**

* Feature

  This function enables Bluetooth.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.




##### Disable Bluetooth

> **bt.stop()**

* Feature

  This function disables Bluetooth.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.




##### Get Bluetooth Device Status

> **bt.getStatus()**

* Feature

  This function gets Bluetooth device status.

* Parameter

  None

* Return Value

  | Return Value | Type | Description                          |
  | ------------ | ---- | ------------------------------------ |
  | -1           | int  | Fails to get Bluetooth device status |
  | 0            | int  | Bluetooth device is stopped          |
  | 1            | int  | Bluetooth device is working          |

  

##### Get Bluebooth Device Address

> **bt.getLocalAddr()**

* Feature

  This function gets Bluetooth device address. This function can only be called after the Bluetooth is initialized and enabled successfully, for example, after receiving an event whose event_id is 0 in the callback function, that is, after *bt.start()* is successfully executed.

* Parameter

  None

* Return Value

  If the execution is successful, it returns a 6-byte Bluetooth device address of bytearray type. If the execution fails, it returns -1.

* Example

```python
>>> addr = bt.getLocalAddr()
>>> print(addr)
b'\xc7\xa13\xf8\xbf\x1a'
>>> mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
>>> print('mac = [{}]'.format(mac))
mac = [1a:bf:f8:33:a1:c7]
```



##### Set Bluetooth Device Name

> **bt.setLocalName(code, name)**

* Feature

  This function sets Bluetooth device name.

* Parameter

  | Parameter | Type   | Description                                                |
  | --------- | ------ | ---------------------------------------------------------- |
  | code      | int    | Coding mode<br/>0 - UTF8<br/>1 - GBK                       |
  | name      | string | Bluetooth device name, and the maximum length is 22 bytes. |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python
>>> bt.setLocalName(0, 'QuecPython-BT')
0
```



##### Get Bluetooth Device Name

> **bt.getLocalName()**

* Feature

  This function gets Bluetooth device name.

* Parameter

  None

* Return Value

  If the execution is successful, it returns a tuple with the format (code, name) , including the name encoding mode and the Bluetooth device name. If the execution fails, it returns -1.

* Example

```python
>>> bt.getLocalName()
(0, 'QuecPython-BT')
```



##### Set Visibility of Bluetooth Device

> **bt.setVisibleMode(mode)**

* Feature

  This function sets the visibility of Bluetooth device, that is, whether the Bluetooth device is visible and connectable when it is scanned and acts as a slave device.</font>

* Parameter

  | Parameter | Type | Description                                                  |
  | --------- | ---- | ------------------------------------------------------------ |
  | mode      | int  | 0 - Bluetooth device cannot be searched or connected<br>1 - Bluetooth device can be searched but cannot be connected<br>2 - Bluetooth device cannot be searched but can be connected<br>3 - Bluetooth device can be searched and connected |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python
>>> bt.setVisibleMode(3)
0
```



##### Get Visibility of Bluetooth Device

> **bt.getVisibleMode()**

* Feature

  This function sets the visibility of Bluetooth device.

* Parameter

  None

* Return Value

  If the execution is successful, it returns the visibility value of Bluetooth device. If the execution fails, it returns -1.

* Example

```python
>>> bt.getVisibleMode()
3
```



##### Start Searching for Bluebooth Device

> **bt.startInquiry(mode)**

* Feature

  This function starts searching for nearby Bluetooth devices.

* Parameter

  | Parameter | Type | Description                                                  |
  | --------- | ---- | ------------------------------------------------------------ |
  | mode      | int  | Indicates the Bluetooth device type to be queried. Currently it is set to 15 which means searching all Bluetooth devices.<br /> |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python
bt.startInquiry(15)
```



##### Stop Searching for Bluebooth Device

> **bt.cancelInquiry()**

* Feature

  This function stops searching for Bluetooth devices.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Set Audio Output Channel

> **bt.setChannel(channel)**

* Feature

  This function sets audio output channel when answering a call or playing audio through Bluetooth.

* Parameter

  | Parameter | Type | Description                               |
  | --------- | ---- | ----------------------------------------- |
  | channel   | int  | 0 - Handset<br>1 - Headset<br>2 - Speaker |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Initialize HFP 

> **bt.hfpInit()**

* Feature

​        This function initializes HFP.

* Parameter

  None

* Return Value

​        0       Successful execution.

​        -1      Failed execution.

* Example

```python 

```



##### Release HFP Resources

> **bt.hfpRelease()**

* Feature

  This function releases HFP resources.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Establish HFP Connection 

> **bt.hfpConnect(addr)**

* Feature

  This function establishes an HFP connection and connects to AG.

* Parameter

  | Parameter | Type  | Description                            |
  | --------- | ----- | -------------------------------------- |
  | addr      | array | 6-byte Bluetooth device address of AG. |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Disconnect HFP Connection

> **bt.hfpDisonnect(addr)**

* Feature

  This function disconnects the HFP connection.

* Parameter

  | Parameter | Type  | Description                            |
  | --------- | ----- | -------------------------------------- |
  | addr      | array | 6-byte Bluetooth device address of AG. |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### HFP Set In-call Volume

> **bt.hfpSetVolume(addr, vol)**

* Feature

  This function sets in-call volume through Bluetooth.

* Parameter

  | Parameter | Type  | Description                            |
  | --------- | ----- | -------------------------------------- |
  | addr      | array | 6-byte Bluetooth device address of AG. |
  | vol       | Int   | In-call volume. Range: 1–15.           |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### HFP Hang Up the Phone

> **bt.hfpRejectAfterAnswer(addr)**

* Feature

  This function hangs up the connected phone.

* Parameter

  | Parameter | Type  | Description                            |
  | --------- | ----- | -------------------------------------- |
  | addr      | array | 6-byte Bluetooth device address of AG. |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### HFP Reject the Call

> **bt.hfpRejectCall(addr)**

* Feature

  This function rejects the call.

* Parameter

  | Parameter | Type  | Description                            |
  | --------- | ----- | -------------------------------------- |
  | addr      | array | 6-byte Bluetooth device address of AG. |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### HFP Answer the Call

> **bt.hfpAnswerCall(addr)**

* Feature

  This function answers the call.

* Parameter

  | Parameter | Type  | Description                            |
  | --------- | ----- | -------------------------------------- |
  | addr      | array | 6-byte Bluetooth device address of AG. |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### HFP Enable Voice Assistant

> **bt.hfpEnableVR(addr)**

* Feature

  This function enables voice assistant.

* Parameter

  | Parameter | Type  | Description                            |
  | --------- | ----- | -------------------------------------- |
  | addr      | array | 6-byte Bluetooth device address of AG. |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### HFP Disable Voice Assistant

> **bt.hfpDisableVR(addr)**

* Feature

  This function disables voice assistant.

* Parameter

  | Parameter | Type  | Description                            |
  | --------- | ----- | -------------------------------------- |
  | addr      | array | 6-byte Bluetooth device address of AG. |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### HFP Control Three-way Calling

> **bt.hfpDisableVR(addr, cmd)**

* Feature

  This function controls three-way calling.

* Parameter

  | Parameter | Type  | Description                            |
  | --------- | ----- | -------------------------------------- |
  | addr      | array | 6-byte Bluetooth device address of AG. |
  | cmd       | int   | Control command                        |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### HFP Demo

```python
# -*- coding: UTF-8 -*-

"""
Description: This demo describes answering calls automatically through HFP.
Platform: EC600UCN_LB Uranium EVB
After running this demo, search for the Bluetooth device name and connect it on the phone A , then make a call from phone B to phone A. When phone A starts ringing and vibrating, the Bluetooth device automatically answers the call.
"""
import bt
import utime
import _thread
from queue import Queue
from machine import Pin

# If the corresponding playback channel has an external PA, and PA needs to be enabled by the pin, the following steps are required.
# The GPIO to be used depends on the actual pin used.
gpio11 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_DISABLE, 0)
gpio11.write(1)

BT_NAME = 'QuecPython-hfp'

BT_EVENT = {
    'BT_START_STATUS_IND': 0,           # bt/ble start
    'BT_STOP_STATUS_IND': 1,            # bt/ble stop
    'BT_HFP_CONNECT_IND': 40,           # bt hfp connected
    'BT_HFP_DISCONNECT_IND': 41,        # bt hfp disconnected
    'BT_HFP_CALL_IND': 42,              # bt hfp call state
    'BT_HFP_CALL_SETUP_IND': 43,        # bt hfp call setup state
    'BT_HFP_NETWORK_IND': 44,           # bt hfp network state
    'BT_HFP_NETWORK_SIGNAL_IND': 45,    # bt hfp network signal
    'BT_HFP_BATTERY_IND': 46,           # bt hfp battery level
    'BT_HFP_CALLHELD_IND': 47,          # bt hfp callheld state
    'BT_HFP_AUDIO_IND': 48,             # bt hfp audio state
    'BT_HFP_VOLUME_IND': 49,            # bt hfp volume type
    'BT_HFP_NETWORK_TYPE': 50,          # bt hfp network type
    'BT_HFP_RING_IND': 51,              # bt hfp ring indication
    'BT_HFP_CODEC_IND': 52,             # bt hfp codec type
}

HFP_CONN_STATUS = 0
HFP_CONN_STATUS_DICT = {
    'HFP_DISCONNECTED': 0,
    'HFP_CONNECTING': 1,
    'HFP_CONNECTED': 2,
    'HFP_DISCONNECTING': 3,
}
HFP_CALL_STATUS = 0
HFP_CALL_STATUS_DICT = {
    'HFP_NO_CALL_IN_PROGRESS': 0,
    'HFP_CALL_IN_PROGRESS': 1,
}

BT_IS_RUN = 0

msg_queue = Queue(30)


def get_key_by_value(val, d):
    for key, value in d.items():
        if val == value:
            return key
    return None

def bt_callback(args):
    global msg_queue
    msg_queue.put(args)

def bt_event_proc_task():
    global msg_queue
    global BT_IS_RUN
    global BT_EVENT
    global HFP_CONN_STATUS
    global HFP_CONN_STATUS_DICT
    global HFP_CALL_STATUS
    global HFP_CALL_STATUS_DICT

    while True:
        print('wait msg...')
        msg = msg_queue.get()  # Blocks here when there is no message
        event_id = msg[0]
        status = msg[1]

        if event_id == BT_EVENT['BT_START_STATUS_IND']:
            print('event: BT_START_STATUS_IND')
            if status == 0:
                print('BT start successfully.')
                BT_IS_RUN = 1
                bt_status = bt.getStatus()
                if bt_status == 1:
                    print('BT status is 1, normal status.')
                else:
                    print('BT status is {}, abnormal status.'.format(bt_status))
                    bt.stop()
                    break

                retval = bt.getLocalName()
                if retval != -1:
                    print('The current BT name is : {}'.format(retval[1]))
                else:
                    print('Failed to get BT name.')
                    bt.stop()
                    break

                print('Set BT name to {}'.format(BT_NAME))
                retval = bt.setLocalName(0, BT_NAME)
                if retval != -1:
                    print('BT name set successfully.')
                else:
                    print('BT name set failed.')
                    bt.stop()
                    break

                retval = bt.getLocalName()
                if retval != -1:
                    print('The new BT name is : {}'.format(retval[1]))
                else:
                    print('Failed to get new BT name.')
                    bt.stop()
                    break

                # Set the visibility of Bluetooth device to searchable and connectable.
                retval = bt.setVisibleMode(3)
                if retval == 0:
                    mode = bt.getVisibleMode()
                    if mode == 3:
                        print('BT visible mode set successfully.')
                    else:
                        print('BT visible mode set failed.')
                        bt.stop()
                        break
                else:
                    print('BT visible mode set failed.')
                    bt.stop()
                    break
            else:
                print('BT start failed.')
                bt.stop()
                break
        elif event_id == BT_EVENT['BT_STOP_STATUS_IND']:
            print('event: BT_STOP_STATUS_IND')
            if status == 0:
                BT_IS_RUN = 0
                print('BT stop successfully.')
            else:
                print('BT stop failed.')
            break
        elif event_id == BT_EVENT['BT_HFP_CONNECT_IND']:
            HFP_CONN_STATUS = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CONNECT_IND, {}, hfp_conn_status:{}, mac:{}'.format(status, get_key_by_value(msg[2], HFP_CONN_STATUS_DICT), mac))
            if status != 0:
                print('BT HFP connect failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_DISCONNECT_IND']:
            HFP_CONN_STATUS = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_DISCONNECT_IND, {}, hfp_conn_status:{}, mac:{}'.format(status, get_key_by_value(msg[2], HFP_CONN_STATUS_DICT), mac))
            if status != 0:
                print('BT HFP disconnect failed.')
            bt.stop()
        elif event_id == BT_EVENT['BT_HFP_CALL_IND']:
            call_sta = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CALL_IND, {}, hfp_call_status:{}, mac:{}'.format(status, get_key_by_value(msg[2], HFP_CALL_STATUS_DICT), mac))
            if status != 0:
                print('BT HFP call failed.')
                bt.stop()
                continue

            if call_sta == HFP_CALL_STATUS_DICT['HFP_NO_CALL_IN_PROGRESS']:
                if HFP_CALL_STATUS == HFP_CALL_STATUS_DICT['HFP_CALL_IN_PROGRESS']:
                    HFP_CALL_STATUS = call_sta
                    if HFP_CONN_STATUS == HFP_CONN_STATUS_DICT['HFP_CONNECTED']:
                        print('call ended, ready to disconnect hfp.')
                        retval = bt.hfpDisconnect(addr)
                        if retval == 0:
                            HFP_CONN_STATUS = HFP_CONN_STATUS_DICT['HFP_DISCONNECTING']
                        else:
                            print('Failed to disconnect hfp connection.')
                            bt.stop()
                            continue
            else:
                if HFP_CALL_STATUS == HFP_CALL_STATUS_DICT['HFP_NO_CALL_IN_PROGRESS']:
                    HFP_CALL_STATUS = call_sta
                    print('set audio output channel to 2.')
                    bt.setChannel(2)
                    print('set volume to 7.')
                    retval = bt.hfpSetVolume(addr, 7)
                    if retval != 0:
                        print('set volume failed.')
        elif event_id == BT_EVENT['BT_HFP_CALL_SETUP_IND']:
            call_setup_status = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CALL_SETUP_IND, {}, hfp_call_setup_status:{}, mac:{}'.format(status, call_setup_status, mac))
            if status != 0:
                print('BT HFP call setup failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_CALLHELD_IND']:
            callheld_status = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CALLHELD_IND, {}, callheld_status:{}, mac:{}'.format(status, callheld_status, mac))
            if status != 0:
                print('BT HFP callheld failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_NETWORK_IND']:
            network_status = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_NETWORK_IND, {}, network_status:{}, mac:{}'.format(status, network_status, mac))
            if status != 0:
                print('BT HFP network status failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_NETWORK_SIGNAL_IND']:
            network_signal = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_NETWORK_SIGNAL_IND, {}, signal:{}, mac:{}'.format(status, network_signal, mac))
            if status != 0:
                print('BT HFP network signal failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_BATTERY_IND']:
            battery_level = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_BATTERY_IND, {}, battery_level:{}, mac:{}'.format(status, battery_level, mac))
            if status != 0:
                print('BT HFP battery level failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_AUDIO_IND']:
            audio_status = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_AUDIO_IND, {}, audio_status:{}, mac:{}'.format(status, audio_status, mac))
            if status != 0:
                print('BT HFP audio failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_VOLUME_IND']:
            volume_type = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_VOLUME_IND, {}, volume_type:{}, mac:{}'.format(status, volume_type, mac))
            if status != 0:
                print('BT HFP volume failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_NETWORK_TYPE']:
            service_type = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_NETWORK_TYPE, {}, service_type:{}, mac:{}'.format(status, service_type, mac))
            if status != 0:
                print('BT HFP network service type failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_RING_IND']:
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_RING_IND, {}, mac:{}'.format(status, mac))
            if status != 0:
                print('BT HFP ring failed.')
                bt.stop()
                continue
            retval = bt.hfpAnswerCall(addr)
            if retval == 0:
                print('The call was answered successfully.')
            else:
                print('Failed to answer the call.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_HFP_CODEC_IND']:
            codec_type = msg[2]
            addr = msg[3]  # MAC address of Bluetooth master device
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('BT_HFP_CODEC_IND, {}, codec_type:{}, mac:{}'.format(status, codec_type, mac))
            if status != 0:
                print('BT HFP codec failed.')
                bt.stop()
                continue
    print('Ready to release hfp.')
    bt.hfpRelease()
    bt.release()


def main():
    global BT_IS_RUN

    _thread.start_new_thread(bt_event_proc_task, ())

    retval = bt.init(bt_callback)
    if retval == 0:
        print('BT init successful.')
    else:
        print('BT init failed.')
        return -1
    retval = bt.hfpInit()
    if retval == 0:
        print('HFP init successful.')
    else:
        print('HFP init failed.')
        return -1
    retval = bt.start()
    if retval == 0:
        print('BT start successful.')
    else:
        print('BT start failed.')
        retval = bt.hfpRelease()
        if retval == 0:
            print('HFP release successful.')
        else:
            print('HFP release failed.')
        retval = bt.release()
        if retval == 0:
            print('BT release successful.')
        else:
            print('BT release failed.')
        return -1

    count = 0
    while True:
        utime.sleep(1)
        count += 1
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])

        if count % 5 == 0:
            if BT_IS_RUN == 1:
                print('[{}] BT HFP is running, count = {}......'.format(timestamp, count))
                print('')
            else:
                print('BT HFP has stopped running, ready to exit.')
                break


if __name__ == '__main__':
    main()

```



##### Initialize A2DP/AVRCP 

> **bt.a2dpavrcpInit()**

* Feature

  This function initializes A2DP and AVRCP.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Release A2DP/AVRCP Resources

> **bt.a2dpavrcpRelease()**

* Feature

  This function releases A2DP and AVRCP resources.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Disconnect A2DP  Connection

> **bt.a2dpDisconnect(addr)**

* Feature

  This function disconnects A2DP connection.

* Parameter

  | Parameter | Type  | Description                                    |
  | --------- | ----- | ---------------------------------------------- |
  | addr      | array | 6-byte address of A2DP Bluetooth master device |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Get Address of A2DP Bluetooth  Master Device

> **bt.a2dpGetAddr()**

* Feature

  This function gets address of A2DP Bluetooth master device.

* Parameter

  None

* Return Value

  If the execution is successful, it returns a 6-byte address of A2DP Bluetooth master device in bytearray type. If the execution fails, it returns -1.

* Example

```python

```



##### Get A2DP Connection Status

> **bt.a2dpGetConnStatus()**

* Feature

  This function gets A2DP connection status.

* Parameter

  None

* Return Value

  | Return Value | Type | Description                         |
  | ------------ | ---- | ----------------------------------- |
  | -1           | int  | Fails to get A2DP connection status |
  | 0            | int  | Disconnected                        |
  | 1            | int  | Connecting                          |
  | 2            | int  | Connected                           |
  | 3            | int  | Disconnecting                       |

* Example

```python
1
```



##### AVRCP Set Bluetooth Master Device to Start Playing

> **bt.avrcpStart()**

* Feature

  This function sets Bluetooth master device to start playing.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### AVRCP Set Bluetooth Master Device to Stop Playing

> **bt.avrcpPause()**

* Feature

  This function sets Bluetooth master device to stop playing.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### AVRCP Set Bluetooth Master Device to Play the Previous Track

> **bt.avrcpPrev()**

* Feature

  This function sets Bluetooth master device to play the previous track.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### AVRCP Set Bluetooth Master Device to Play the Next Track

> **bt.avrcpNext()**

* Feature

  This function sets Bluetooth master device to play the next track.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### AVRCP Set Volume of Bluetooth Master Device

> **bt.avrcpSetVolume(vol)**

* Feature

  This function sets the volume of Bluetooth master device.

* Parameter

  | Parameter | Type | Description          |
  | --------- | ---- | -------------------- |
  | vol       | int  | Volume. Range: 0–11. |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### AVRCP Get Volume of Bluetooth Master Device

> **bt.avrcpGetVolume()**

* Feature

  This function gets the volume of Bluetooth master device.

* Parameter

  None

* Return Value

  An integer volume value           Successful execution.

  -1                                                   Failed execution.

* Example

```python

```



##### AVRCP Get Play Status of Bluetooth Master Device

> **bt.avrcpGetPlayStatus()**

* Feature

  This  function gets play status of Bluetooth master device.

* Parameter

  None

* Return Value

  | Return Value | Type | Description                     |
  | ------------ | ---- | ------------------------------- |
  | -1           | int  | Fails to get play status        |
  | 0            | int  | Not play                        |
  | 1            | int  | playing                         |
  | 2            | int  | Play paused                     |
  | 3            | int  | Switching to the previous track |
  | 4            | int  | Switching to the next track     |

* Example

```python

```



##### AVRCP Get Connection Status of Bluetooth Master Device

> **bt.avrcpGetConnStatus()**

* Feature

  This function gets connection status of Bluetooth master device through AVRCP protocol.

* Parameter

  None

* Return Value

  | Return Value | Type | Description                    |
  | ------------ | ---- | ------------------------------ |
  | -1           | int  | Fails to get connection status |
  | 0            | int  | Disconnected                   |
  | 1            | int  | Connecting                     |
  | 2            | int  | Connected                      |
  | 3            | int  | Disconnecting                  |

* Example

```python

```



##### A2DP/AVRCP Demo 

```python
# -*- coding: UTF-8 -*-

"""
Description: This demo describes a simple Bluetooth music playback operation through A2DP/AVRCP.
After running this demo, search for Bluetooth device name and connect it on the mobile phone, then open the music player on the mobile phone. Then return to the demo running interface, and call the corresponding functions according to the prompt menu to perform the music playback, pause, previous track, next track and the volume setting. 
"""
import bt
import utime
import _thread
from queue import Queue
from machine import Pin

BT_STATUS_DICT = {
    'BT_NOT_RUNNING': 0,
    'BT_IS_RUNNING': 1
}

A2DP_AVRCP_CONNECT_STATUS = {
    'DISCONNECTED': 0,
    'CONNECTING': 1,
    'CONNECTED': 2,
    'DISCONNECTING': 3
}

host_addr = 0
msg_queue = Queue(10)

# If the corresponding playback channel has an external PA, and PA needs to be enabled by the pin, the following steps are required.
# Which GPIO to be used depends on the actual pin used.
gpio11 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_DISABLE, 0)
gpio11.write(1)


def cmd_proc(cmd):
    cmds = ('1', '2', '3', '4', '5')
    vols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')

    if cmd in cmds:
        if cmd == '5':
            while True:
                tmp = input('Please input volume: ')
                if len(tmp) != 1:
                    vol = tmp.split('Please input volume: ')[1]
                else:
                    vol = tmp
                if vol in vols:
                    return cmd, int(vol)
                else:
                    print('Volume should be in [0,11], try again.')
        else:
            return cmd, 0
    else:
        print('Command {} is not supported!'.format(cmd))
        return -1

def avrcp_play(args):
    return bt.avrcpStart()

def avrcp_pause(args):
    return bt.avrcpPause()

def avrcp_prev(args):
    return bt.avrcpPrev()

def avrcp_next(args):
    return bt.avrcpNext()

def avrcp_set_volume(vol):
    return bt.avrcpSetVolume(vol)

def bt_callback(args):
    pass

def bt_a2dp_avrcp_proc_task():
    global msg_queue

    cmd_handler = {
        '1': avrcp_play,
        '2': avrcp_pause,
        '3': avrcp_prev,
        '4': avrcp_next,
        '5': avrcp_set_volume,
    }
    while True:
        # print('wait msg...')
        msg = msg_queue.get()
        print('recv msg: {}'.format(msg))
        cmd_handler.get(msg[0])(msg[1])


def main():
    global host_addr
    global msg_queue

    _thread.start_new_thread(bt_a2dp_avrcp_proc_task, ())
    bt.init(bt_callback)
    bt.setChannel(2)
    retval = bt.a2dpavrcpInit()
    if retval == 0:
        print('BT A2DP/AVRCP initialization succeeded.')
    else:
        print('BT A2DP/AVRCP initialization failed.')
        return -1

    retval = bt.start()
    if retval != 0:
        print('BT start failed.')
        return -1

    utime.sleep_ms(1500)

    old_name = bt.getLocalName()
    if old_name == -1:
        print('Get BT name error.')
        return -1
    print('The current BT name is {}'.format(old_name[1]))
    new_name = 'QuecPython-a2dp'
    print('Set new BT name to {}'.format(new_name))
    retval = bt.setLocalName(0, new_name)
    if retval == -1:
        print('Set BT name failed.')
        return -1
    cur_name = bt.getLocalName()
    if cur_name == -1:
        print('Get new BT name error.')
        return -1
    else:
        if cur_name[1] == new_name:
            print('BT name changed successfully.')
        else:
            print('BT name changed failed.')

    visible_mode = bt.getVisibleMode()
    if visible_mode != -1:
        print('The current BT visible mode is {}'.format(visible_mode))
    else:
        print('Get BT visible mode error.')
        return -1

    print('Set BT visible mode to 3.')
    retval = bt.setVisibleMode(3)
    if retval == -1:
        print('Set BT visible mode error.')
        return -1
    count = 0
    while True:
        count += 1
        if count % 5 == 0:
            print('waiting to be connected...')
        if count >= 10000:
            count = 0
        a2dp_status = bt.a2dpGetConnStatus()
        avrcp_status = bt.avrcpGetConnStatus()
        if a2dp_status == A2DP_AVRCP_CONNECT_STATUS['CONNECTED'] and avrcp_status == A2DP_AVRCP_CONNECT_STATUS['CONNECTED']:
            print('========== BT connected! =========')
            addr = bt.a2dpGetAddr()
            if addr != -1:
                mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
                print('The BT address on the host side: {}'.format(mac))
                host_addr = addr
            else:
                print('Get BT addr error.')
                return -1
            print('Please open the music player software on your phone first.')
            print('Please enter the following options to select a function:')
            print('========================================================')
            print('1 : play')
            print('2 : pause')
            print('3 : prev')
            print('4 : next')
            print('5 : set volume')
            print('6 : exit')
            print('========================================================')
            while True:
                tmp = input('> ')
                if len(tmp) != 1:
                    cmd = tmp.split('> ')[1]
                else:
                    cmd = tmp
                if cmd == '6':
                    break
                retval = cmd_proc(cmd)
                if retval != -1:
                    msg_queue.put(retval)
            break
        else:
            utime.sleep_ms(1000)
    print('Ready to disconnect a2dp.')
    retval = bt.a2dpDisconnect(host_addr)
    if retval == 0:
        print('a2dp connection disconnected successfully')
    else:
        print('Disconnect a2dp error.')
    print('Ready to stop BT.')
    retval = bt.stop()
    if retval == 0:
        print('BT has stopped.')
    else:
        print('BT stop error.')
    bt.a2dpavrcpRelease()
    bt.release()


if __name__ == '__main__':
    main()
```



##### Initialize SPP 

> **bt.sppInit()**

* Feature

  This function initializes SPP.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Release SPP Resources

> **bt.sppRelease()**

* Feature

  This function releases SPP resources.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Establish SPP Connection

> **bt.sppConnect(addr)**

* Feature

  This function established an SPP connection.

* Parameter

  | Parameter | Type  | Description                     |
  | --------- | ----- | ------------------------------- |
  | addr      | array | 6-byte Bluetooth device address |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### Disconnect SPP  Connection

> **bt.sppDisconnect()**

* Feature

  This function disconnects SPP connection.

* Parameter

  None

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### SPP Send Data

> **bt.sppSend(data)**

* Feature

  This function sends data through SPP.

* Parameter

  | Parameter | Type  | Description     |
  | --------- | ----- | --------------- |
  | data      | array | Data to be sent |

* Return Value

  0       Successful execution.

  -1      Failed execution.

* Example

```python

```



##### SPP Demo

```python
# -*- coding: UTF-8 -*-

"""
Description: This demo describes the data transmission with the mobile phone through SPP.
1) Before running the demo, you need to install a Bluetooth serial port application on the mobile phone (Android), such as BlueSPP, and then open this application;
2) Change the Bluetooth name of the target device in this demo, that is, change the value of DST_DEVICE_INFO['dev_name'] to the Bluetooth name of the mobile phone that the user wants to connect to;
3) When running the demo, first search for nearby Bluetooth devices. If the target device is found, the search will end, and then an SPP connection request will be sent to the target device;
4) The user should check whether the interface of the Bluetooth pairing request pops up on the mobile phone. When it appears, click to pair;
5) After the Bluetooth devices are successfully paired, the user can enter the Bluetooth serial port interface and send data to the device. After receiving the data, the device will reply "I have received the data you sent."
6) Click to disconnect in the application of the mobile phone to end the demo.
"""
import bt
import utime
import _thread
from queue import Queue


BT_NAME = 'QuecPython-SPP'

BT_EVENT = {
    'BT_START_STATUS_IND': 0,          # bt/ble start
    'BT_STOP_STATUS_IND': 1,           # bt/ble stop
    'BT_SPP_INQUIRY_IND': 6,           # bt spp inquiry ind
    'BT_SPP_INQUIRY_END_IND': 7,       # bt spp inquiry end ind
    'BT_SPP_RECV_DATA_IND': 14,        # bt spp recv data ind
    'BT_SPP_CONNECT_IND': 61,          # bt spp connect ind
    'BT_SPP_DISCONNECT_IND': 62,       # bt spp disconnect ind
}

DST_DEVICE_INFO = {
    'dev_name': 'HUAWEI Mate40 Pro', # The name of the Bluetooth device to be connected
    'bt_addr': None
}

BT_IS_RUN = 0
msg_queue = Queue(30)


def bt_callback(args):
    global msg_queue
    msg_queue.put(args)


def bt_event_proc_task():
    global msg_queue
    global BT_IS_RUN
    global DST_DEVICE_INFO

    while True:
        print('wait msg...')
        msg = msg_queue.get()  # Blocks here when there is no message
        event_id = msg[0]
        status = msg[1]

        if event_id == BT_EVENT['BT_START_STATUS_IND']:
            print('event: BT_START_STATUS_IND')
            if status == 0:
                print('BT start successfully.')
                BT_IS_RUN = 1

                print('Set BT name to {}'.format(BT_NAME))
                retval = bt.setLocalName(0, BT_NAME)
                if retval != -1:
                    print('BT name set successfully.')
                else:
                    print('BT name set failed.')
                    bt.stop()
                    continue

                retval = bt.setVisibleMode(3)
                if retval == 0:
                    mode = bt.getVisibleMode()
                    if mode == 3:
                        print('BT visible mode set successfully.')
                    else:
                        print('BT visible mode set failed.')
                        bt.stop()
                        continue
                else:
                    print('BT visible mode set failed.')
                    bt.stop()
                    continue

                retval = bt.startInquiry(15)
                if retval != 0:
                    print('Inquiry error.')
                    bt.stop()
                    continue
            else:
                print('BT start failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_STOP_STATUS_IND']:
            print('event: BT_STOP_STATUS_IND')
            if status == 0:
                BT_IS_RUN = 0
                print('BT stop successfully.')
            else:
                print('BT stop failed.')

            retval = bt.sppRelease()
            if retval == 0:
                print('SPP release successfully.')
            else:
                print('SPP release failed.')
            retval = bt.release()
            if retval == 0:
                print('BT release successfully.')
            else:
                print('BT release failed.')
            break
        elif event_id == BT_EVENT['BT_SPP_INQUIRY_IND']:
            print('event: BT_SPP_INQUIRY_IND')
            if status == 0:
                rssi = msg[2]
                name = msg[4]
                addr = msg[5]
                mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
                print('name: {}, addr: {}, rssi: {}'.format(name, mac, rssi))

                if name == DST_DEVICE_INFO['dev_name']:
                    print('The target device is found, device name {}'.format(name))
                    DST_DEVICE_INFO['bt_addr'] = addr
                    retval = bt.cancelInquiry()
                    if retval != 0:
                        print('cancel inquiry failed.')
                        continue
            else:
                print('BT inquiry failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_INQUIRY_END_IND']:
            print('event: BT_SPP_INQUIRY_END_IND')
            if status == 0:
                print('BT inquiry has ended.')
                inquiry_sta = msg[2]
                if inquiry_sta == 0:
                    if DST_DEVICE_INFO['bt_addr'] is not None:
                        print('Ready to connect to the target device : {}'.format(DST_DEVICE_INFO['dev_name']))
                        retval = bt.sppConnect(DST_DEVICE_INFO['bt_addr'])
                        if retval != 0:
                            print('SPP connect failed.')
                            bt.stop()
                            continue
                    else:
                        print('Not found device [{}], continue to inquiry.'.format(DST_DEVICE_INFO['dev_name']))
                        bt.cancelInquiry()
                        bt.startInquiry(15)
            else:
                print('Inquiry end failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_RECV_DATA_IND']:
            print('event: BT_SPP_RECV_DATA_IND')
            if status == 0:
                datalen = msg[2]
                data = msg[3]
                print('recv {} bytes data: {}'.format(datalen, data))
                send_data = 'I have received the data you sent.'
                print('send data: {}'.format(send_data))
                retval = bt.sppSend(send_data)
                if retval != 0:
                    print('send data faied.')
            else:
                print('Recv data failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_CONNECT_IND']:
            print('event: BT_SPP_CONNECT_IND')
            if status == 0:
                conn_sta = msg[2]
                addr = msg[3]
                mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
                print('SPP connect successful, conn_sta = {}, addr {}'.format(conn_sta, mac))
            else:
                print('Connect failed.')
                bt.stop()
                continue
        elif event_id == BT_EVENT['BT_SPP_DISCONNECT_IND']:
            print('event: BT_SPP_DISCONNECT_IND')
            conn_sta = msg[2]
            addr = msg[3]
            mac = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(addr[5], addr[4], addr[3], addr[2], addr[1], addr[0])
            print('SPP disconnect successful, conn_sta = {}, addr {}'.format(conn_sta, mac))
            bt.stop()
            continue


def main():
    global BT_IS_RUN

    _thread.start_new_thread(bt_event_proc_task, ())
    retval = bt.init(bt_callback)
    if retval == 0:
        print('BT init successful.')
    else:
        print('BT init failed.')
        return -1
    retval = bt.sppInit()
    if retval == 0:
        print('SPP init successful.')
    else:
        print('SPP init failed.')
        return -1
    retval = bt.start()
    if retval == 0:
        print('BT start successful.')
    else:
        print('BT start failed.')
        retval = bt.sppRelease()
        if retval == 0:
            print('SPP release successful.')
        else:
            print('SPP release failed.')
        return -1

    count = 0
    while True:
        utime.sleep(1)
        count += 1
        cur_time = utime.localtime()
        timestamp = "{:02d}:{:02d}:{:02d}".format(cur_time[3], cur_time[4], cur_time[5])

        if count % 5 == 0:
            if BT_IS_RUN == 1:
                print('[{}] BT SPP is running, count = {}......'.format(timestamp, count))
                print('')
            else:
                print('BT SPP has stopped running, ready to exit.')
                break


if __name__ == '__main__':
    main()
```



#### camera - Camera and Code Scan 

Module function: Preview, camera, code scan

Note: At present, the following modules support the camera function: EC200U series,EC600U series,EC600N series,EC600S series,EC800N series.


##### Preview

Before using the preview, you need to initialize LCD.

###### Create Preview Object

> **import camera**
>
> **preview = camera.camPreview(model,cam_w,cam_h,lcd_w,lcd_h,perview_level)**

* Parameter

| Parameter     | Type | Description                                                  |
| ------------- | ---- | ------------------------------------------------------------ |
| model         | int  | camera model:<br />*0: gc032a spi*<br />*1: bf3901 spi*      |
| cam_w         | int  | camera Horizontal resolution                                 |
| cam_h         | int  | camera Vertical resolution                                   |
| lcd_w         | int  | LCD horizontal resolution                                    |
| lcd_h         | int  | LCD vertical resolution                                      |
| perview_level | int  | Preview level[1,2]. Level 2 only for ASR platform. The higher the level, the smoother the image and the greater the consumption of resources. |

* Return Value

  * -1: Initialization failure.
  * If the object is returned, it means the creation is successful.

* Example

```python
>>> import camera
>>> preview = camera.camPreview(0,640,480,176,220,1)
```



###### Turn on Preview

> **camPreview.open()**

* Parameter

  * None.

* Return Value

  * 0: Successful execution.
  * Other values: Failed execution.



###### Turn off Preview

> **camPreview.close()**

Turns off the preview.

* Parameter

  * None.

* Return Value

  * 0: Successful execution.
  * Other values: Failed execution.



##### Code Scan

Before using  code scan , you need to initialize LCD.

###### Create an Object

> **import camera**
>
>**scan= camera.camScandecode(model,decode_level,cam_w,cam_h,perview_level,lcd_w,lcd_h)**

* Parameter

| Parameter     | Type | Description                                                  |
| ------------- | ---- | ------------------------------------------------------------ |
| model         | int  | camera model:<br />*0: gc032a spi*<br />*1: bf3901 spi*      |
| decode_level  | int  | code scan level[1,2]，Level 2 only for ASR platform. The higher the level, the better the recognition result but the greater the resource consumption* |
| cam_w         | int  | camera horizontal resolution                                 |
| cam_h         | int  | camera vertical resolution                                   |
| perview_level | int  | Preview level[1,2]. Level 2 only for ASR platform. The higher the level, the smoother the image and the greater the consumption of resources.<br />when it is equal to 0, there is no LCD preview function. There is no need to initialize the LCD in advance. <br/> when it is equal to 1 or 2, the LCD must be initialized first |
| lcd_w         | int  | LCD horizontal resolution                                    |
| lcd_h         | int  | LCD vertical resolution                                      |

* Return Value

  * -1: Failed execution.
  * If the object is returned, it means the creation is successful.



###### Turn on Camera

> **camScandecode.open()**

* Parameter

  * None.

* Return Value

  * 0: Successful execution.
  * Other values: Failed execution.



###### Turn off Camera

> **camScandecode.close()**

* Parameter

  * None.

* Return Value

  * 0: Successful execution.
  * Other values: Failed execution.



###### Turn on Code Scan

> **camScandecode.start()**

* Parameter

  * None.

* Return Value

  * 0: Successful execution.
  * Other values: Failed execution.



###### Turn off Code Scan

> **camScandecode.stop()**

* Parameter

  * None.

* Return Value

  * 0: Successful execution.
  * Other values: Failed execution.



###### Pause Code Scan

> **camScandecode.pause()**

* Parameter

  * None.

* Return Value

  * 0: Successful execution.
  * Other values: Failed execution.

###### Resume Code Scan

> **camScandecode.resume()**

* Return Value

  * 0: Successful execution.
  * Other values: Failed execution.



###### Set Code Scan Callback

> **camScandecode.callback(callback)**

* Parameter

| Parameter | Type | Description  |
| --------- | ---- | ------------ |
| callback  | api  | Callback API |

* Return Value

  * 0: Successful execution.
  * Other values: Failed execution.

* Example

```python
def callback(para):
    print(para)		#para[0] code scan result 	0: success. Other values: failure.
    				#para[1] code scan content	
Scandecode.callback(callback) 
```



##### Camera

Camera function.

###### Create object

> **import camera**
>
> **cap= camera.camCapture(model,cam_w,cam_h,perview_level,lcd_w,lcd_h)**

* Parameter

|Parameter | parameter type | parameter description|
| ------------- | -------- | ------------------------------------------------------------ |
|Model | int | camera model: <br/> *0: gc032a spi* <br/> *1: bf3901 spi* |
| cam_ W | int | camera horizontal resolution|
| cam_ H | int | camera vertical resolution |
| perview_ Level | int | preview level [0,2]. Level 2 only for ASR platform. The higher the level, the smoother the image and the greater the resource consumption<br/> when it is equal to 0, there is no LCD preview function. There is no need to initialize the LCD in advance.  <br/> when it is equal to 1 or 2, the LCD must be initialized first |
| lcd_ W | int | LCD horizontal resolution|
| lcd_ H | int | LCD vertical resolution |

* Return Value

  * If an object is returned, the creation is successful



###### Turn on the camera

> **camCapture.open()**

* Parameter

  * None

* Return Value

  * 0: successful
  * Others: failed



###### Turn off the camera

> **camCapture.close()**

* Parameter

  * None

* Return Value

  * 0: successful
  * Others: closing failed



###### Take pictures

The photo format is JPEG

> **camCapture.start(width, height, pic_name)**

* Parameter

|Parameter | parameter type | parameter description|
| -------- | -------- | ----------------------------------------- |
|Width | int | saves the horizontal resolution of the picture|
|Height | int | saves the vertical resolution of the picture|
| pic_ Name | str | picture name. Pictures need no suffix JPEG, it will be added automatically|

* Return Value

  * 0: successful (actually, it depends on the camera callback)



###### Set camera callback

> **camCapture.callback(callback)**

* Parameter

|Parameter | parameter type | parameter description|
| -------- | -------- | -------- |
|Callback | API | callback API|

* Return Value

  * 0: successful
  * Others: failed

* Examples

```python
def callback(para):
    print(para)     #Para [0] photographing results      0: success others: failure
                    #Para [1] name of the saved picture
camCapture.callback(callback) 
```



#### GNSS - External GNSS

Module function: Get positioning data from GPS model of L76 module, including whether the module locates successfully, latitude, longitude, UTC time, positioning mode,  number of satellites, number of visible satellites, azimuth angle, speed over the ground, geodetic height and so on. 

Note: Currently, only the ASR and Unisoc EC200U/EC600U series support this function.



##### Create gnss object

> **from gnss import GnssGetData**
>
> **gnss = GnssGetData(uartn,baudrate,databits,parity,stopbits,flowctl)**

- Parameter

| Parameter | Type | Description                                                  |
| :-------- | :--- | ------------------------------------------------------------ |
| uartn     | int  | UARTn, Range: 0-3: <br />0-UART0 - DEBUG PORT<br />1-UART1 – BT PORT<br />2-UART2 – MAIN PORT<br />3-UART3 – USB CDC PORT |
| baudrate  | int  | Baud rate. The common baud rate, such as 4800, 9600, 19200, 38400, 57600, 115200, 230400 and so on, are supported. |
| databits  | int  | Data bit (5 ~ 8)                                               |
| parity    | int  | Parity (0 – NONE，1 – EVEN，2 - ODD)                         |
| stopbits  | int  | Stop bit (1 ~ 2)                                               |
| flowctl   | int  | Hardware flow control (0 – FC_NONE， 1 – FC_HW)              |

* Return Value

  * None

* Example

```python
from gnss import GnssGetData
gnss = GnssGetData(1, 9600, 8, 0, 1, 0)
```



##### Read and Parse GNSS Data

> **gnss.read_gnss_data(max_retry=1, debug=0)**

* Parameter

| Parameter | Type | Description                                                  |
| --------- | ---- | ------------------------------------------------------------ |
| max_retry | int  | This parameter is optional. Indicates the maximum number of automatic re-reading attempts when the read GNSS is invalid. If the length of read data is 0 (that is, no data is read), exit directly. If any GNGGA, GNRMC, or GPGSV statement is not found or found but the data is invalid, then the next packet of data will be read again. Exit until the GNGGA, GNRMC, and GPGSV statements are found and the data is valid or the maximum number of attempts is reached. The default value is 1, indicating that data is read only once. |
| debug     | int  | This parameter is optional. The default value is 0. Indicates whether debugging information is output in the process of reading and parsing GNSS data. 0 indicates that no detailed information is output, and 1 indicates that detailed information is output, so that users can intuitively see the analysis results and compare them. Note that if the debug value is 0, it does not output all debugging information, but only some simple and basic information. For example, if the corresponding data is not found in the original GNSS data or the data is invalid, the message is displayed indicating that the data is invalid or the relevant data is not found. For details, see the example. |

* Return Value

  * Returns the length of GNSS data read from the serial port, in bytes.

* Example

```python
#=========================================================================
gnss.read_gnss_data()	# read only once and no detailed debugging information is displayed
4224	# Read data successfully, and parse GNGGA, GNRMC, and GPGSV statements successfully, return the original length of the read data directly
#=========================================================================
gnss.read_gnss_data()  # read only once and no detailed debugging information is displayed
GNGGA data is invalid. # Data reading succeeds, but the GNGGA location data is invalid
GNRMC data is invalid. # Data reading succeeds, but the GNRMC location data is invalid
648		# Returns the length of the original data read
#=========================================================================
gnss.read_gnss_data(max_retry=3)  # Set the maximum number of automatic reads to 3
Not find GPGSV data or GPGSV data is invalid.  # GPGSV data not found or invalid for the first read
continue read.        # Continue reading the next packet of data
Not find GNGGA data.  # The second read failed to find GNGGA data
Not find GNRMC data.  # The second read failed to find GNRMC data
continue read.        # Continue reading the next packet of data
Not find GNGGA data.  # The third read failed to find GNGGA data
Not find GNRMC data.  # The third read failed to find GNRMC data
continue read.        # If the third attempt fails again, the system determines that the maximum number of attempts has reached and exits
128
#=========================================================================
gnss.read_gnss_data(debug=1)  # Set to read parsing process output details
GGA data : ['GNGGA', '021224.000', '3149.27680', 'N', '11706.93369', 'E', '1', '19', '0.9', '168.2', 'M', '-5.0', 'M', '', '*52']  # Output GNGGA data matched from the original GNSS data and simply processed
RMC data : ['GNRMC', '021224.000', 'A', '3149.27680', 'N', '11706.93369', 'E', '0.00', '153.28', '110122', '', '', 'A', 'V*02']  # Output GNRMC data matched from the original GNSS data and simply processed
total_sen_num = 3, total_sat_num = 12  # Output the total number of complete GPGSV statements and the number of visible satellites
# The following is the specific GPGSV statement information
[0] : ['$GPGSV', '3', '1', '12', '10', '79', '210', '35', '12', '40', '070', '43', '21', '08', '305', '31', '23', '46', '158', '43', '0*6E']
[1] : ['$GPGSV', '3', '2', '12', '24', '', '', '26', '25', '54', '125', '42', '31', '', '', '21', '32', '50', '324', '34', '0*64']
[2] : ['$GPGSV', '3', '3', '12', '193', '61', '104', '44', '194', '58', '117', '42', '195', '05', '162', '35', '199', '', '', '32', '0*54']
4224
```



##### Get the original GNSS data

> **gnss.getOriginalData()**

This interface is used to return the original GNSS data read from the serial port. If users want to get the original GNSS data for their own processing or some data confirmation, they can get it through this interface. 

* Parameter

  * None

* Return Value

  * Returns original GNSS data read from the serial port as a string.

* Example

```python
data = gnss.getOriginalData()
print(data)
# Due to the large amount of data, only partial results are listed
00,A,3149.28094,N,11706.93869,E,0.00,153.28,110122,,,A,V*04
$GNVTG,153.28,T,,M,0.00,N,0.00,K,A*2E
$GNZDA,021555.000,11,01,2022,00,00*4D
$GPTXT,01,01,01,ANTENNA OK*35
$GNGGA,021556.000,3149.28095,N,11706.93869,E,1,24,0.6,166.5,M,-5.0,M,,*5E
$GNGLL,3149.28095,N,11706.93869,E,021556.000,A,A*47
$GNGSA,A,3,10,12,21,23,24,25,32,193,194,195,199,,1.0,0.6,0.8,1*35
$GNGSA,A,3,01,04,07,09,14,21,22,24,38,39,42,45,1.0,0.6,0.8,4*36
... 
$GNGGA,021600.000,3149.28096,N,11706.93877,E,1,25,0.6,166.4,M,-5.0,M,,*52
$GNGLL,3149.28096,N,11706.93877,E,021600.000,A,A*4B
$GNGSA,A,3,10,12,21,23,24,25,31,32,193,194,195,199,1.0,0.6,0.8,1*37
$GNGSA,A,3,01,04,07,09,$GNGGA,021601.000,3149.28096,N,11706.93878,E,1,25,0.6,166.4,M,-5.0,M,,*5C
$GNGLL,3149.2809
```



##### Check the validity of the parsing result

> **gnss.checkDataValidity()**

The interface provided by the GNSS module obtains data from GNGGA, GNRMC and GPGSV statements in the original GNSS packets read from the serial port. This interface is used to check the validity of GNGGA, GNRMC and GPGSV statements in a packet of GNSS data read from the serial port.

* Parameter

  * None

* Return Value

  * Returns a tuple of the form` (gga_valid, rmc_valid, gsv_valid)`

    `gga_valid` - Indicates whether GNGGA data is matched and parsed successfully. 0 indicates that GNGGA data is not matched or invalid. 1 indicates that GNGGA data is valid;<br/>
    `rmc_valid` - Indicates whether GNRMC data is matched and parsed successfully. 0 indicates that GNRMC data is not matched or invalid. 1 indicates that GNRMC data is valid;<br/>
    `gsv_valid` - Indicates whether GPGSV data is matched and parsed successfully. 0 indicates that GPGSV data is not matched or invalid. 1 indicates that GPGSV data is valid.

  * If the user only cares about the location result, that is, whether the GNGGA data is valid, the `gga_valid` parameter is 1 (or whether the location is successful through the gnss.isFix () interface), and all three parameters are not required to be 1. GNRMC data is parsed to obtain the earth speed, and GPGSV data is parsed to obtain the number of visible satellites and their corresponding azimuth angles. Therefore, if you do not care about these parameters, you can ignore `rmc_valid` and `gsv_valid`.

* Example

```python
gnss.checkDataValidity()
(1, 1, 1)  #  GNGGA, GNRMC, and GPGSV data are matched and parsed successfully
```



##### Get Whether the Positioning is Successful

> **gnss.isFix()**

- Parameter

  * None.

- Return Value

  * 1: Successful positioning 
  * 0:  Positioning failure

* Example

```python
gnss.isFix()
1
```



##### Get UTC Time

> **gnss.getUtcTime()**

- Parameter

  * None.

- Return Value

  * Return UTC Time as a string on success, otherwise return -1.

* Example

```python
gnss.getUtcTime()
'06:22:05.000'  # hh:mm:ss.sss
```



##### Get Positioning Mode

> **gnss.getLocationMode()**

- Parameter

  * None.

- Return Value

| value | description                                         |
| ----- | --------------------------------------------------- |
| -1    | get data failed                                     |
| 0     | Unavailable or invalid positioning                  |
| 1     | A valid positioning, positioning mode: GPS or SPS   |
| 2     | A valid positioning, positioning mode: DGPS or DSPS |
| 6     | Estimation (dead reckoning) model                   |

* Example

```python
gnss.getLocationMode()
1
```



##### Get number of satellites used for positioning

> **gnss.getUsedSateCnt()**

- Parameter

  * None.

- Return Value

  * The number of satellites used for GPS module positioning is returned as an integer on success, and integer -1 is returned on failure.

* Example

```python
gnss.getUsedSateCnt()
24
```



##### Get Latitude and Longitude Information

> **gnss.getLocation()**

* Parameter

  * None.

* Return Value

  * The latitude and longitude information of the GPS module is returned on success, and integer -1 is returned on failure. The return value is in the following format on success:

    `(longitude, lon_direction, latitude, lat_direction)` <br/>
    `longitude` - float type <br/>
    `lon_direction` - Longitude direction. The value is a string of characters. E indicates east longitude and W indicates west longitude <br/>
    `latitude` - float type <br/>
    `lat_direction` -  Latitude direction. The value is a string of characters. N indicates north latitude and S indicates south latitude

* Example

```python
gnss.getLocation()
(117.1156448333333, 'E', 31.82134916666667, 'N')
```



##### Get Number of Visible Satellites

> **gnss.getViewedSateCnt()**

- Parameter

  * None.

- Return Value

  * Return the number of visible satellites of GPS module on success, otherwise return -1.

* Example

```python
gnss.getViewedSateCnt()
12
```



##### Get the azimuth of the visible GNSS satellite

> **gnss.getCourse()**

- Parameter

  * None.

- Return Value

  * Returns all visible GNSS satellite azimuth angles on success, Range: 0–359, based on true north, otherwise return -1.The return format is dictionary, where key indicates the satellite number and value indicates the azimuth. Note that the value of value can be either an integer value or ", depending on whether the azimuth in the GPGSV statement in the original GNSS data has a value. The return value is of the following form:
  
    `{key:value, ...,  key:value}`

* Example

```python
gnss.getCourse()
{'10': 204, '195': 162, '12': 68, '193': 105, '32': 326, '199': 162, '25': 122, '31': 247, '24': 52, '194': 116, '21': 304, '23': 159}
```



##### Get the altitude of the GPS module

> **gnss.getGeodeticHeight()**

- Parameter

  * None.

- Return Value

  * The float altitude is returned in meters on success, and integer -1 on failure.

* Example

```python
gnss.getGeodeticHeight()
166.5
```



##### Get  Speed Over the Ground

> **gnss.getSpeed()**

- Parameter

  * None.

- Return Value

  * Return the speed over the ground of GPS module(Unit: KM/h), float type, otherwise return -1 .

- Example

```python
gnss.getSpeed()
0.0
```





#### quecgnss - built-in GNSS

Note: The current only  EC200UCNAA/EC200UCNLA/EC200UEUAA models support this feature.

##### Initialize the GNSS

> **import quecgnss**
>
> **quecgnss.init()**

* Function

  Initialization of GNSS module functions.

* Parameter

  None

* Return Value

  Returns integer 0 on success, integer -1 on failure.



##### Get the GNSS working status

> **quecgnss.get_state()**

* Function

  Get the GNSS module status.

* Parameter

  None

* Return Value

| Value | Type | Description                                                  |
| ----- | ---- | ------------------------------------------------------------ |
| 0     | int  | The GNSS module is closed                                    |
| 1     | int  | The GNSS module is being firmware upgrade                    |
| 2     | int  | The GNSS module is  positioning. In this mode, the GNSS module starts to read GNSS positioning data. The validity of the positioning data needs to be determined by parsing corresponding statements after obtaining the positioning data, for example, whether the STATUS of the GNRMC statement is A or V. A indicates that the positioning is valid, and V indicates that the positioning is invalid. |



##### Enable or disable GNSS

> **quecgnss.gnssEnable(opt)**

* Function

  Enable or disable the GNSS module. If you use the GNSS function for the first time after power-on, you do not need to invoke this interface to enable the GNSS function. Instead, you can invoke the init() interface. The init() interface automatically enables the GNSS function during initialization.

* Parameter

  | Parameter | Type | Description                          |
  | --------- | ---- | ------------------------------------ |
  | opt       | int  | 0 - disable GNSS<br/>1 - enable GNSS |

* Return Value

  Returns integer 0 on success, integer -1 on failure.



##### Get the GNSS data

> **quecgnss.read(size)**

* Function

  Get the GNSS data。

* Parameter

  | Parameter | Type | Description                                                |
  | --------- | ---- | ---------------------------------------------------------- |
  | size      | int  | Specifies the size of the data to read, the unit is bytes. |

* Return Value

  Returns a tuple on success, integer -1 on failure. The tuple form is as follows:

  `(size, data)`

  `size` - The actual size of the data read

  `data` - positioning data

##### Example

```python
import quecgnss


def main():
    ret = quecgnss.init()
    if ret == 0:
    	print('GNSS init ok.')
    else:
        print('GNSS init failed.')
        return -1
    data = quecgnss.read(4096)
    print(data[1].decode())
    
    quecgnss.gnssEnable(0)


if __name__ == '__main__':
    main()
    

#===================================================================================================
# The result
167,169,170,,,,,,,,1.773,1.013,1.455*15
$GPGSV,2,1,8,3,23,303,34,16,32,219,28,22,74,98,26,25,16,43,25*77
$GPGSV,2,2,8,26,70,236,28,31,59,12,38,32,55,127,34,4,5,,21*49
$BDGSV,2,1,8,163,51,192,32,166,70,11,31,167,52,197,32,169,59,334,31*61
$BDGSV,2,2,8,170,40,205,31,161,5,,31,164,5,,27,165,5,,29*59
$GNRMC,022326.000,A,3149.324624,N,11706.921702,E,0.000,261.541,180222,,E,A*38
$GNGGA,022326.000,3149.324624,N,11706.921702,E,1,12,1.013,-8.580,M,0,M,,*47
$GNGLL,3149.324624,N,11706.921702,E,022326.000,A,A*44
$GNGSA,A,3,31,32,3,16,22,25,26,,,,,,1.773,1.013,1.455*1C
$GNGSA,A,3,163,166,167,169,170,,,,,,,,1.773,1.013,1.455*15
$GPGSV,2,1,8,3,23,303,34,16,32,219,27,22,74,98,26,25,16,43,25*78
$GPGSV,2,2,8,26,70,236,28,31,59,12,37,32,55,127,34,4,5,,20*47
$BDGSV,2,1,8,163,51,192,32,166,70,11,31,167,52,197,32,169,59,334,31*61
$BDGSV,2,2,8,170,40,205,31,161,5,,31,164,5,,27,165,5,,29*59
$GNRMC,022327.000,A,3149.324611,N,11706.921713,E,0.000,261.541,180222,,E,A*3F
$GNGGA,022327.000,3149.324611,N,11706.921713,E,1,12,1.013,-8.577,M,0,M,,*48
$GNGLL,3149.324611,N,11706.921713,E,022327.000,A,A*43
...... # There is too much data, so it is omitted
$GNGSA,A,3,31,32,3,16,22,25,26,,,,,,1.837,1.120,1.456*11
$GNGSA,A,3,163,166,167,169,170,,,,,,,,1.837,1.120,1.456*18
$GPGSV,2,1,8,3,23,302,27,16,32,220,26,22,73,101,27,25,16,43,27*45
$GPGSV,2,2,8,26,70,237,28,31,59,13,33,32,54,128,28,4,5,,24*44
$BDGSV,2,1,8,163,51,192,33,166,71,11,35,167,52,198,33,169,59,334,34*6E
$BDGSV,2,2,8,170,40,205,32,161,5,,33,164,5,,28,165,5,,30*5F
$GNRMC,022507.000,A,3149.324768,N,11706.922344,E,0.000,261.541,180222,,E,A*31
$GNGGA,022507.000,3149.324768,N,11706.922344,E,1,12,1.120,-8.794,M,0,M,,*48
$GNGLL,3149.324768,N,11706.922344,E,022507.000,A,A*4D
$GNGSA,A,3,31,32,3,16,22,25,26,,,,,,1.837,1.120,1.455*12
$GNGSA,A,3,163,166,167,169,170,,,,,,,,1.837,1.120,1.455*1B
$GPGSV,2,1,8,3,23,302,26,16,32,220,26,22,73,101,27,25,16,43,26*45
$GPGSV,2,2,8,26,70,237,28,31,59,13,32,32,54,128,28,4,5,,24*45
$BDGSV,2,1,8,163,51,192,24,166,71,11,35,167,52,198,33,169,59,334,34*68
$BDGSV,2,2,8,170,40,205,31,161,5,,33,164,5,,28,165,5,,30*5C
$GNRMC,022508.000,A,3149.324754,N,11706.922338,E,0.002,261.541,180222,,E,A*38
$GNGGA,022508.000,3149.324754,N,11706.922338,E,1,12,1.120,-8.750,M,0,M,,*4B
$GNGLL,3149.324754,N,11706.922338,E,022508.000,A,A*46
$GNGSA,A,3,31,3

```



#### Securedata - secure data area

Module function: the module provides a bare flash area and a special read-write interface for customers to store important information, and the information will not be lost after burning the firmware (burning the firmware without this function cannot be guaranteed not to be lost). Provide a storage and read interface, not a delete interface.

At present, only ec600n series projects are supported

##### Data storage

>**SecureData.Store(index, databuf, len)**

* Parameter

| Parameter | type | description |
| ------ | -------- | ------------------------------------------------------------ |
| Index | int | index range is 1-16: <br/> 1 - 8 maximum storage of 52 bytes of data <br/> 9 - 12 maximum storage of 100 bytes of data <br/> 13 - 14 maximum storage of 500 bytes of data <br/> 15 - 16 maximum storage of 1000 bytes of data |
| Databuf | bytearray | data array to be stored|
| Len | int | length of data to be written|


When storing, it is stored according to the shorter of databuf and Len

* Return Value

  -1: Parameter error
  0: normal execution

##### Data reading

>**SecureData.Read(index,databuf,len)**

* Parameter

| Parameter | type | description |
| ------ | -------- | ----------------------------------------------- |
| Index | int | index range is 1-16: <br/> read the index number corresponding to the stored data|
| Databuf | bytearray | stores the read data|
| Len | int | length of data to be read|

If the stored data is not as large as the incoming len, the actual stored data length is returned

* Return Value

  -2: The stored data does not exist and the backup data does not exist
  -1: Parameter error
  Other: length of data actually read

* Example

```python
import SecureData
#Data to be stored buf
databuf = '\x31\x32\x33\x34\x35\x36\x37\x38'
#Store data with length of 8 in the storage area with index of 1
SecureData.Store(1, databuf, 8)
#Define an array with a length of 20 to read the stored data
buf = bytearray(20)
#Read the data in the storage area with index 1 into buf, and store the length of the read data in the variable length
length = SecureData.Read(1, buf, 20)
#Output read data
print(buf[:length])
```

* implementation results

```python
>>> import SecureData
>>> databuf = '\x31\x32\x33\x34\x35\x36\x37\x38'
>>> SecureData.Store(1, databuf, 8)
0
>>> buf = bytearray(20)
>>> length = SecureData.Read(1, buf, 20)
>>> print(buf[:length])
bytearray(b'12345678')
>>> 
```



#### NB Internet of things cloud platform

Module function: Provide the function of connecting to the IoT cloud platform, and provide the connection to the IoT cloud platform. Through the communication function of the IoT cloud platform and module devices, it currently supports China Telecom lot IoT platform, China Telecom AEP IoT platform and China Mobile onenet IoT platform. The quecthing version does not contain this module.
Module name: nb(lowercase)

Support platform: BC25PA

Introduction: it includes two sub modules OC, AEP. The two sub modules all use lwm2m for data interaction.

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

- Parameter

  * None.

- Return Value

  * Success - 0
  * Failed - not 0

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

  * The received data is a hexadecimal string, so the data length must be even.

- Return Value

  * Success - 0
  * Failed - not 0

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
| data_len  | int    | Expected Send data length (note that this parameter is adjusted according to the actual length of data, and the minimum value is taken according to the comparison between the capacity of data variable and data_len),Non blocking|
| data      | string | Data to be sent,The maximum supported data length is 1024 bytes                                   |
| type      | int    | Indicates that the core network releases the RRC connection with the module: <0-no indication. <br/>1-Indicates that no further uplink or downlink data is expected after the packet uplink data, the core network can release it immediately. <br/>2-Indicates that a single downlink data packet corresponding to the reply is expected after the uplink data of the packet, and the core network releases it immediately after it is sent.|

- Note

  * The sent data is a hexadecimal string, and the data length is even.

- Return Value

  * Success - 0
  * Failed - not 0

- Example

```python
>>> print(data)
bytearray(b'313233')
>>> oc.send(6,data,0)
0
```

###### Close connection

- Parameter

  * None

- Return Value

  * Success -True
  * Failed -False

- Example

```python
>>> oc.close()
True
```

##### AEP

###### Create AEP object

> **AEP(ip,port,model,psk)**

- **Parameter**

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| ip        | string | The server IP address of the Internet of things platform, with a maximum length of 16. |
| port      | string | Server port of Internet of things platform, maximum length 5. |
| model | int | 0 Set the receiving data mode to buffer mode, no URC report when new data is received<br/> 1 Set the receiving data mode to direct spitting mode, when new data is received, it will be reported immediately through URC.<br/> 2 Set the receiving data mode to buffer mode, and only report the indication URC when new data is received. Can be omitted, defaults to 1. |
| psk | string | Hexadecimal string type. The key of the encrypted device, which can be generated by the platform or set independently when the encrypted device is registered on the platform side. The maximum supported length is 256 bytes. It can be omitted |
- Example

```python
>>> from nb import AEP
>>> aep=AEP("221.229.214.202","5683")
```
###### set callback function

> **aep.set_event_callcb(usrfunc)**
- parameters

| Parameters | Type | Description |
| ---- | ------ | ------------------------------------- -------- |
| usrfunc | func(data) | call usrfunc when an event occurs |
- func(data) parameter description:
| Parameters | Type | Description |
| ---- | ------ | ------------------------------------- -------- |
| data | list | data[0]:event_id,event type><br/>data[1]:event_code,event type corresponding return code><br/>data[2]:recv_data,data><br/>data [3]: data_len, data length><br/> |

- Notice
    For the description of event_id, event_code, recv_data, data_len, see [event description] (# event description) in this module. This function, it is recommended to register before connecting to prevent event loss.
-
###### Connect to AEP cloud platform

> **aep.connect(timeout)**

- Parameter

    Type: int, timeout, unit (ms), if no parameter is entered, the default is 30s

    Note: The worst-case blocking duration of timeout failure is: 15s+timeout. Concurrent operations are not supported.

- Return Value

  * Success - 0
  * Failed - -1

- Example

```python
>>> aep.connect(3000)
0
```

###### Query data to be read

> **aep.check()**

- Parameter

  * None

- Return Value

  * Returns the number of pieces of data to be read distributed by the cloud platform

- Example

```python
>>> from nb import AEP
>>> aep=AEP("221.229.214.202","5683")
>>> aep.check()
0
```

###### Receive data

> **aep.recv(data_len,data，timeout))**

- Instructions for use, the effect of the [model](#create AEP object) value on this function is as follows
| model | Description |
| -------- | ---------------------------------------- -------------------- |
|0| is the cache mode, the cloud platform sends the data to the module, the module will not have any active prompt action, but can only read it actively. |
|1| is the direct spit mode, the cloud platform sends data to the module, the module will spit the received data directly to urc, and the callback function set by set_event_callcb(usrfunc) will directly take over the received data and the data length. |
|2| is the cache mode. When there is no cached data, the cloud platform will send data to the module, and the module will report the event through the callback function usrfunc, indicating that there is cached data to be read (the cloud platform sends data to the module, the module The group judges that the cache is empty and reports the event to indicate that there is data arriving, and the cached data is not empty and does not report the event)|

- **Parameter**

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| data_len  | int    | Expected accepted data length (note that this parameter is adjusted according to the actual length of data, and the minimum value is taken according to the comparison between the capacity of data variable and data_len) |
| data      | string | Store received data                                          |
| timeout | int | Timeout time, in ms, default 30s if not entered. |

- Note

  The received data is a hexadecimal string, so the data length must be even.

- Return Value

  * Success - 0
  * Failed - not 0

- Example

```python
>>> aep.recv(6,data)
0
```

###### Send data

> **aep.send(data_len,data,type,timeout)**

- Instructions for use:
    In the timeout failure state, the worst-case blocking duration is: 5s+timeout. Concurrent operations are not supported.

- **Parameter**

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| data_len | int | The length of the data expected to be sent (note that this parameter is adjusted according to the actual length of the data, and the minimum value is taken according to the comparison between the capacity of the data variable and data_len), non-blocking. |
| data | string | Data to be sent, up to 1024 bytes of data. |
| type | int | Indicates that the core network releases the RRC connection with the module:<br/>0-send NON data and set the RAI auxiliary release flag carried by the module to send data to 0<br/>1-send NON data and Set the RAI auxiliary release flag carried by the module to send data to 1<br/> 2- Send NON data and set the RAI auxiliary release flag carried by the module to send data to 2<br/> 100- Send CON data and the module sends The RAI auxiliary release flag carried by the data is set to 0<br/> 101- Send CON data and set the RAI auxiliary release flag carried by the module to send data to 1<br/> 102- Send CON data and send the data to the module. The carried RAI auxiliary release flag is set to 2 |
| timeout | int | Timeout time, in ms, if not input, the default is 30s |

- RAI Auxiliary Release Marker Description
| | Description |
| -------------- | ---------------------------------- -------------------------- |
| RAI | The RAI flag is used to instruct the core network to release the RRC connection to the module. :<br/>When RAI is 0, there is no indication. <br/>When RAI is 1, it indicates that no further upstream or downstream data is expected after the upstream data of the packet, and the core network can release it immediately. <br/>When RAI is 2, it indicates that a single downlink data packet corresponding to the reply is expected after the uplink data of the packet, and the core network releases it immediately after sending it. |

- Note

  The sending data is a hexadecimal string, the data length is an even number, blocking (timeout 3 minutes), and returning success indicates that the sending instruction is executed successfully.

- Return Value

  * Success - 0
  * Failed - not 0

- Example

```python
>>> print(data)
bytearray(b'313233')
>>> aep.send(6,data,0)
0
```
###### Check connection status
> **aep.connect_check()**
- parameters

  None
  
- Return value
   Return value type: string
   The meaning is as follows
  
  | Return value | Description |
  | -------- | ------ |
  | UNINITIALISED |Uninitialized state |
  | REGISTERING |Connecting |
  | REJECTED_BY_SERVER |The connection request was rejected by the server |
  | TIMEOUT |Connection timed out |
  | REGISTERED |Connected Not Subscribed |
  | REGISTERED_AND_OBSERVED |Connected and subscribed |
  | DEREGISTERED | Disconnected |
  | RESUMPTION_FAILED DTLS |Session recovery failed |
  | FALIED |Failed to execute the function |
  
 - Example

````python
>>> aep.connect_check()
'UNINITIALISED\r\n'
````

###### close the connection
> **aep.close()**

- Parameter

  * None

- Return Value

  * Success - true
  * Failed - false

- Example

```python
>>> aep.close()
True
```

###### Event Description

The general description of the events of this module is as follows:

|event_id |event_code |recv_data |data_len |description|
| -------------- | ---------|----------|------------- |---------------------------- |
|0 |0 |NULL |0 |modem enters psm and reports this event. At this time, the module does not accept the network data sent to the module, and can break the psm state on the modem side by actively sending data. |
|0 |1 |NULL |0 |modem exits psm mode and reports this event. |
|23 |6 |NULL |0 |The connection is successfully restored after waking up from deep sleep, and this event is reported. Reported when AEP.set_event_callcb(usrfunc) is called. |
|23 |7 |NULL |0 |Failed to resume connection after wake-up from deep sleep, you can disconnect and reconnect. Reported when AEP.set_event_callcb(usrfunc) is called. |
|24 |8 |NULL |0 |After the cloud platform issues the fota upgrade command, this event is reported when the module starts to download the differential upgrade package. |
|24 |9 |NULL |0 |When the cloud platform issues the fota upgrade command, and the module fota upgrade is completed, this event is reported. |
|25 |10 |NULL |0 |Received the RST packet from the cloud platform and actively reported this event. In this case, you need to disconnect and reconnect to complete the subscription for normal communication. |
|27 |0 |data |data_len |Receive data from the cloud platform, report this event when modem=1 and call set_event_callcb(usrfunc) to set the callback function. |
|28 |0 |NULL |0 |Receive data from the cloud platform and report this event when modem=2 and the module has no cached data (when aep.check() returns 0, it means that there is no cached data). |
|others |0 |NULL |0 |Ignore such events|

###### Use example

Sample model

```json
{
  "productInfo": {
    "productId": 15082482
  },
  "properties": [
    {
      "propertyId": 1,
      "identifier": "ecl",
      "Propertyname": "wireless signal coverage level",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"null\",\"min\":\"-32768\",\"len\":4,\"unitName\":\"\",\"max\":\"32767\""
    },
    {
      "propertyId": 2,
      "identifier": "pci",
      "Propertyname": "physical cell ID",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"null\",\"min\":\"-32768\",\"len\":4,\"unitName\":\"\",\"max\":\"32767\""
    },
    {
      "propertyId": 3,
      "identifier": "IMEI",
      "propertyName": "IMEI",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 4,
      "identifier": "rsrp",
      "Propertyname": "reference signal reception power",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"null\",\"min\":\"-32768\",\"len\":4,\"unitName\":\"\",\"max\":\"32767\""
    },
    {
      "propertyId": 5,
      "identifier": "sinr",
      "Propertyname": "signal to interference plus noise ratio",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"null\",\"min\":\"-32768\",\"len\":4,\"unitName\":\"\",\"max\":\"32767\""
    },
    {
      "propertyId": 6,
      "identifier": "time",
      "Propertyname": "current time",
      "description": null,
      "dataType": "timestamp",
      "dataSchema": "\"len\":8"
    },
    {
      "propertyId": 7,
      "identifier": "ICCID",
      "propertyName": "ICCID",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 8,
      "identifier": "cell_id",
      "Propertyname": "cell location information",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"null\",\"min\":\"-2147483648\",\"len\":4,\"unitName\":\"\",\"max\":\"2147483647\""
    },
    {
      "propertyId": 9,
      "identifier": "velocity",
      "Propertyname": "water velocity",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"m/s\",\"min\":\"0\",\"len\":4,\"unitName\":\"meters per second\",\"max\":\"100\""
    },
    {
      "propertyId": 10,
      "identifier": "act_result",
      "Propertyname": "instruction execution result",
      "description": null,
      "dataType": "enum",
      "dataSchema": "\"len\":1,\"enumDetail\":{\"0\":\"execution succeeded\",\"1\":\"execution failed\"}"
    },
    {
      "propertyId": 11,
      "identifier": "error_code",
      "Propertyname": "failure",
      "description": null,
      "dataType": "enum",
      "dataSchema": "\"len\":1,\"enumDetail\":{\"0\":\"normal\",\"1\":\"sensor failure\"}"
    },
    {
      "propertyId": 12,
      "identifier": "water_flow",
      "Propertyname": "water flow",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"m³/h\",\"min\":\"0\",\"len\":4,\"unitName\":\"cubic meters per hour\",\"max\":\"9999999\""
    },
    {
      "propertyId": 13,
      "identifier": "module_type",
      "Propertyname": "module model",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 14,
      "identifier": "temperature",
      "Propertyname": "water temperature",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"°C\",\"min\":\"0\",\"len\":4,\"unitName\":\"Celsius\",\"max\":\"100\""
    },
    {
      "propertyId": 15,
      "identifier": "valve_onoff",
      "Propertyname": "valve switch",
      "description": null,
      "dataType": "enum",
      "dataSchema": "\"len\":1,\"enumDetail\":{\"0\":\"close\",\"1\":\"turn on\"}"
    },
    {
      "propertyId": 16,
      "identifier": "battery_state",
      "Propertyname": "battery status",
      "description": null,
      "dataType": "enum",
      "dataSchema": "\"len\":1,\"enumDetail\":{\"0\":\"normal\",\"1\":\"low batter\"}"
    },
    {
      "propertyId": 17,
      "identifier": "battery_value",
      "Propertyname": "battery power",
      "description": null,
      "dataType": "integer",
      "dataSchema": "\"unit\":\"%\",\"min\":\"0\",\"len\":4,\"unitName\":\"percentage\",\"max\":\"100\""
    },
    {
      "propertyId": 18,
      "identifier": "terminal_type",
      "Propertyname": "terminal model",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 19,
      "identifier": "back_total_flow",
      "Propertyname": "reverse cumulative traffic",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"m³\",\"min\":\"0\",\"len\":4,\"unitName\":\"cubic meter\",\"max\":\"99999999\""
    },
    {
      "propertyId": 20,
      "identifier": "battery_voltage",
      "Propertyname": "battery voltage",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"V\",\"min\":\"0\",\"len\":4,\"unitName\":\"volt\",\"max\":\"24\""
    },
    {
      "propertyId": 21,
      "identifier": "hydraulic_value",
      "Propertyname": "water pressure value",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"MPa\",\"min\":\"0\",\"len\":4,\"unitName\":\"MPa\",\"max\":\"10\""
    },
    {
      "propertyId": 22,
      "identifier": "hardware_version",
      "Propertyname": "hardware version",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 23,
      "identifier": "software_version",
      "Propertyname": "software version",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 24,
      "identifier": "manufacturer_name",
      "Propertyname": "manufacturer name",
      "description": null,
      "dataType": "vary-string",
      "dataSchema": "\"len\":0,\"unit\":\"null\",\"unitName\":\"\""
    },
    {
      "propertyId": 25,
      "identifier": "water_consumption",
      "Propertyname": "water consumption",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"m³\",\"min\":\"0\",\"len\":4,\"unitName\":\"cubic meter\",\"max\":\"99999999\""
    },
    {
      "propertyId": 26,
      "identifier": "forward_total_flow",
      "Propertyname": "forward cumulative traffic",
      "description": null,
      "dataType": "float",
      "dataSchema": "\"unit\":\"m³\",\"min\":\"0\",\"len\":4,\"unitName\":\"cubic meter\",\"max\":\"99999999\""
    }
  ],
  "services": [
    {
      "serviceId": 1,
      "identifier": "data_report",
      "Servicename": "business data reporting",
      "serviceType": "DataReport",
      "description": null,
      "properties": [
        {
          "propertyId": 12,
          "serial": 1
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 1002,
      "identifier": "battery_voltage_low_alarm",
      "Servicename": "battery low voltage alarm",
      "serviceType": "EventReport",
      "description": null,
      "properties": [
        {
          "propertyId": 16,
          "serial": 1
        },
        {
          "propertyId": 20,
          "serial": 2
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 2,
      "identifier": "signal_report",
      "Servicename": "signal data reporting",
      "serviceType": "DataReport",
      "description": null,
      "properties": [
        {
          "propertyId": 4,
          "serial": 1
        },
        {
          "propertyId": 5,
          "serial": 2
        },
        {
          "propertyId": 2,
          "serial": 3
        },
        {
          "propertyId": 1,
          "serial": 4
        },
        {
          "propertyId": 8,
          "serial": 5
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 9001,
      "identifier": "valve_onoff_resp",
      "Servicename": "valve switch control response",
      "serviceType": "CommandResponse",
      "description": null,
      "properties": [
        {
          "propertyId": 15,
          "serial": 1
        },
        {
          "propertyId": 10,
          "serial": 2
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 8001,
      "identifier": "valve_onoff_cmd",
      "Servicename": "valve switch control",
      "serviceType": "Command",
      "description": null,
      "properties": [
        {
          "propertyId": 15,
          "serial": 1
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 1001,
      "identifier": "error_code_report",
      "Servicename": "fault reporting",
      "serviceType": "EventReport",
      "description": null,
      "properties": [
        {
          "propertyId": 11,
          "serial": 1
        },
        {
          "propertyId": 6,
          "serial": 2
        }
      ],
      "parameters": []
    },
    {
      "serviceId": 3,
      "identifier": "info_report",
      "Servicename": "equipment information reporting",
      "serviceType": "DataReport",
      "description": null,
      "properties": [
        {
          "propertyId": 24,
          "serial": 1
        },
        {
          "propertyId": 18,
          "serial": 2
        },
        {
          "propertyId": 13,
          "serial": 3
        },
        {
          "propertyId": 22,
          "serial": 4
        },
        {
          "propertyId": 23,
          "serial": 5
        },
        {
          "propertyId": 3,
          "serial": 6
        },
        {
          "propertyId": 7,
          "serial": 7
        }
      ],
      "parameters": []
    }
  ]
}
```

Sample code

```python
from nb import AEP
import utime
import ustruct

#The following five functions need to be judged. If the machine is in large format, the data will not be transferred
def aep_htons(source):
    return source & 0xffff
def aep_htoni(source):
    return source & 0xffffffff


def aep_htonl(source):
    return source & 0xffffffffffffffff

def aep_htonf(source):
    return ustruct.unpack('<I', ustruct.pack('<f', source))[0]

def aep_htond(source):
    return ustruct.unpack('Q', ustruct.pack('d', source))[0]

def HexToStr(source, t=None):
    if t:
        if not isinstance(t, int):
            raise Exception("{} is not int type".format(t))
        fmt = "%0" + str(t*2)+"x"
        return fmt%source
    else:
        if not source >> 8:
            return "%02x" % source
        elif not source >> 16:
            return "%04x" % source
        elif not source >> 32:
            return "%08x" % source
        else:
            return "%016x" % source


def StrToHex(source):
    return int(source)

#According to the definition of the reference model, packaging and unpacking are resolved according to the attributes in the corresponding service ID
serid_ Dict = {'valve switch control': 8001,
               'fault reporting': 1001,
               'equipment information reporting': 3,
               'valve switch control response': 9001,
               'Signal data reporting ': 2,
               'battery low voltage alarm': 1002,
               'business data reporting': 1
           }
dict_ CMD = {'data reporting': 0x02,
             'event reporting': 0x07,
             'wireless parameter reporting': 0x03,
             'fixed downlink command': 0x06,
             'command response': 0x86
         }
send_type={'RAI_NONE':0,
            'TYpe_001':1,
            'TYpe_002':2,
            'TYpe_100':100,
            'TYpe_101':101,
            'TYpe_102':102
}
servcei_info={
    'ip':"221.229.214.202",
    'port':"5683"
}
modem_type={
    'cache_no_urc':0,
    'no_cache':1,
    'cache_have_urc':2
}
aep_event={
    'psm_event':0,
    'con_event':21,
    'send_event':22,
    'recover_event':23,
    'rst_event':25,
    'recv_event_data':27,
    'recv_event_flag':28,
}
def aep_pack_cmdtype02(service_id,data_in):
    Data = hextostr (dict_cmd ['data reporting'], 1)
    data+=HexToStr(service_id,2)                #Convert serviceid to string
    if service_id == 1:
        data+=HexToStr(4,2)                     #The sending data is 8.14, and the float type is four bytes long. Here is only one example
        data+=HexToStr(aep_htonf(data_in),4)    #Convert float data to string
    else:
        print('not support')                    #
    return data
 
def aep_pack(cmdtype,service_id,data):
    if cmdtype == dict_cmd['data reporting']:                            #Data reporting - 0x02, here is only one example
        return aep_pack_cmdtype02(service_id,data)
    else:
        print('not support')

def aep_unpack_cmdtype06(data_in):
    print('-------------------unpack recv data before  ------------------')
    print(data_in)
    print(data_in[0:4])
    print(data_in[4:8])
    print(data_in[8:12])
    print(data_in[12:])
    print('-------------------unpack recv data before------------------')
    service_id  = int(str(data_in.decode()[0:4]),16)
    service_id  = aep_htons(service_id)
    task_id     = data_in[4:8]
    payload_len = int(str(data_in.decode()[8:12]),16)
    payload_len = aep_htons(payload_len)
    value = 0
    if service_id == serid_dict['Valve switch control']:                 #The object model issues attribute id = 15, two hexadecimal bytes, enumeration type, 0 or 1
       value = int(str(data_in.decode()[12:14]),16)
       value = aep_htons(value)
    if service_ id == serid_ Dict ['fault reporting']:
        pass
    if service_ id == serid_ Dict ['equipment information reporting']:
        pass
    if service_ id == serid_ Dict ['valve switch control response']:
        pass
    if service_ id == serid_ Dict ['signal data reporting']:
        pass
    print('-------------------unpack recv data after------------------')
    print("service_id ",service_id)
    print("task_id ",task_id)
    print("payload_len ",payload_len)
    print("payload ",value)
    print('-------------------unpack recv data after------------------')
    
def aep_unpack(data_in):
    cmdtype=StrToHex(str(data_in.decode()[:2]))
    data=data_in[2:]
    if cmdtype == dict_ CMD ['fixed downlink instruction']:
        aep_unpack_cmdtype06(data)
    else:
        print('not support')

def recv():
    data=bytearray(20)  
    ret=aep.recv(18,data)
    if ret == -1:
        return
    aep_unpack(data)    
    return ret

def connect():
    ret = aep.connect()
    print('connect ',ret)

def send():
    water_flow_value=8.14
    data=aep_ Pack (dict_cmd ['data reporting'], serid_dict ['business data reporting'], water_flow_value)
    print('send: ',data)
    print('len: ',len(data))
    data_len=len(data)
    ret = aep.send(data_len,data,send_type['RAI_NONE'])
    print('send ',ret)

def close():
    ret = aep.close()
    print('close ',ret)
    
def deal_conn(data):
    if data[1] == 0:
        print('connect CtWing success!')
    if data[1] == 3:
        print('subscription /19/0/0 success!')
        send()
    if data[1] == -1 or data[1] == 1:
        print('connect CtWing failed!')
        aep.connect_check()
def deal_recv(data):
    if data[1] == 0:
        aep_unpack(data[2])
        print('will close')
        close()
    if data[1] == 5:
        print('recv data from ctwing falied')
        
def deal_psm(data):
    if data[1] == 0:
        print('enter modem psm')
    if data[1] == 1:
        print('exit modem psm')
def deal_send(data):
    if data[1] == 4:
        print('send data to ctwing success')
    else:
        print('send data to ctwing falied')
        
def deal_rst(data):
    print('recv rst messge from platform')
    close()
def deal_recover(data):
    print('deal_recover:',data)
    
def event_cb(args):
    print('args:',args)
    if args[0] == aep_event['con_event']:
        deal_conn(args)
    if args[0] == aep_event['send_event']:
        deal_send(args)
    if args[0] == aep_event['recv_event_data'] or args[0] == aep_event['recv_event_flag']:
        deal_recv(args)
    if args[0] == aep_event['rst_event']:
        deal_rst(args)
    if args[0] == aep_event['psm_event']:
        deal_psm(args)
    if args[0] == aep_event['recover_event']:
        deal_recover(args)
    
def init():
    
    aep.set_event_callcb(event_cb)
    connect()
    

loop_num = 0

def do_task():
    init()
aep=AEP(servcei_info['ip'],servcei_info['port'],modem_type['no_cache'])

if __name__ == '__main__':
    do_task()

```



#### uping-(ICMP)ping

Module function: Simulate sending icmp-ping packets



##### ping

- Precautions

There may be exceptions here, because the host address cannot resume the exception of the socket connection

Periodically send Ping packet mechanism through `COUNT` and `INTERVAL` in initialization parameters

> **import uping**
>
> **up = uping.ping(HOST, SOURCE=None, COUNT=4, INTERVAL=1000, SIZE=64, TIMEOUT=5000, quiet=False)**

- parameter

| parameter | type | illustrate                                                   |
| --------- | ---- | ------------------------------------------------------------ |
| HOST      | str  | The domain name address to be pinged, such as "baidu.com"    |
| SOURCE    | str  | Source address, used for binding, generally does not need to be passed |
| COUNT     | int  | The default is 4 times, send 4 ping packets                  |
| INTERVAL  | int  | Interval time, the default is ms, the default is 1000ms      |
| SIZE      | int  | The default packet size of each read is 64, no need to modify |
| TIMEOUT   | int  | Timeout time, the unit is ms, the default is 5000ms or 5s    |
| quiet     | bool | Default fasle, print output, after setting True, the printed value obtained after calling start will be converted into an object and returned, rather than displayed by printing |



example of use

```python
# method one
# printout method
import uping
uping.ping('baidu.com')

# The following is the output of uping.start(), no return value
#72 bytes from 49.49.48.46: icmp_seq=1, ttl=53, time=1169.909000 ms
#72 bytes from 49.49.48.46: icmp_seq=2, ttl=53, time=92.060000 ms
#72 bytes from 49.49.48.46: icmp_seq=3, ttl=53, time=94.818000 ms
#72 bytes from 49.49.48.46: icmp_seq=4, ttl=53, time=114.879000 ms
#4 packets transmitted, 4 packets received, 0 packet loss
#round-trip min/avg/max = 92.06000000000001/367.916/1169.909 ms




# Method 2
# Setting quiet will get the output
import uping
result = uping.ping('baidu.com', quiet=True)
# result can get the corresponding data
# result(tx=4, rx=4, losses=0, min=76.93899999999999, avg=131.348, max=226.697)
```

