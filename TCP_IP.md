# 工作中的TCP/IP


## BUGs


## 调试工具

### 命令行工具

#### traceroute

#### 

### Wireshark

检测发送、接收的所有数据。

### Network Emulator for Windows Toolkit

下载地址：https://blog.mrpol.nl/2010/01/14/network-emulator-toolkit/

模拟各种网络状况：

- Loss：丢包
- Error：错误包
- Latency：延时
- BW&Quene：带宽及队列
- Reorder：重新排列（模拟是否按顺序排列）
- Disconnect：断网 （模拟周期性的断开or链接网络）


## 服务器网络问题

### 多网卡 无法访问

#### 问题描述

系统版本：CentOS Linux release 7.3.1611 (Core) 

服务上有多个网卡，每个网卡都连接到内网，每个网卡都可以上网，现在想要通过一张网卡对公网提供Web服务，在配置完网卡后，用浏览器访问发现，**响应时间过长**。

#### 网络工具

