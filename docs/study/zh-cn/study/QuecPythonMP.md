# QuecPython 产品开发及量产

##  量产流程

QuecPython 生产固件包含3个部分：                     

- 支持QuecPython 运行环境的固件

固件可以从SDK 中获取，也可以通过QPYCom.exe 下载最新版本，当前固件最新版本是v0008。

- 包含客户脚本/配置文件的镜像

customer_fs.bin由QPYcom.exe生成，下载界面选择要合并的脚本/配置文件点击合并按钮生成customer_fs.bin。

- 包含客户脚本/配置文件备份的镜像

customer_backup_fs.bin，由QPYcom.exe生成，脚本如需备份，需要勾选备份选项，在合成时会在customer_backup_fs 中放置相应文件的备份，customer_fs 中的文件如果发生损坏或者丢失，那么会从备份区还原成工厂版本。

 

  

##  量产工具使用文档

### QPYcom.exe

  QuecPython 调试以及量产包生成工具，主要功能有固件下载、在线调试、量产包生成等，详细使用说明参见[《Quectel QuecPython_QPYcom工具使用说明_V1.0.pdf》](Quectel QuecPython_QPYcom工具使用说明_V1.0.pdf)。

### MultiDownload.exe

  移远提供给客户的多口下载工具，支持一拖多下载，详细使用说明参见[《Quectel_QMulti_DL_用户指导_V1.7.pdf》](Quectel_QMulti_DL_用户指导_V1.7.pdf)。

## 代码保护

### 代码加密



### 关闭控制台

