# 工作中的TCP/IP

## ？

- 半连接
- Keep alive 探针
- linger

## 参考

- [酷壳：TCP的那些事（上）](https://coolshell.cn/articles/11564.html)
- [酷壳：TCP的那些事（下）](https://coolshell.cn/articles/11609.html)
- [聊聊TCP中的KeepAlive机制](https://zhuanlan.zhihu.com/p/28894266)
- [tcp的半连接与完全连接队列](https://segmentfault.com/a/1190000008224853)


## 半连接



## Keep alive

内核管理，只能检测这个TCP连接是否还在。

1. KeepAlive默认情况下是关闭的，可以被上层应用开启和关闭
2. tcp_keepalive_time: KeepAlive的空闲时长，或者说每次正常发送心跳的周期，默认值为7200s（2小时）
3. tcp_keepalive_intvl: KeepAlive探测包的发送间隔，默认值为75s
4. tcp_keepalive_probes: 在tcp_keepalive_time之后，没有接收到对方确认，继续发送保活探测包次数，默认值为9（次）


## 可靠性

checksum 序号 自动重发

## 流量控制

可用缓冲区大小

## 拥塞控制

慢启动 快重传 快恢复

## BUGs


## 调试工具

### 命令行工具

#### traceroute

#### route 

#### iptables

mangle chain filter nat 

input output forward postrouting prerouting 

#### ip rule 

#### ifconfig

#### tcpdump

#### nmap

#### netstat

#### nslookup

#### ifup

#### ifdown

### Wireshark

检测发送、接收的所有数据。

#### 过滤器

tcp

### Network Emulator for Windows Toolkit

下载地址：https://blog.mrpol.nl/2010/01/14/network-emulator-toolkit/

模拟各种网络状况：

- Loss：丢包
- Error：错误包
- Latency：延时
- BW&Quene：带宽及队列
- Reorder：重新排列（模拟是否按顺序排列）
- Disconnect：断网 （模拟周期性的断开or链接网络）

教程：http://blog.sina.com.cn/s/blog_13cc013b50102wa0g.html

## 服务器网络问题

### 多网卡 无法访问

#### 问题描述

系统版本：CentOS Linux release 7.3.1611 (Core) 

服务上有多个网卡，每个网卡都连接到内网，每个网卡都可以上网，现在想要通过一张网卡对公网提供Web服务，在配置完网卡后，用浏览器访问发现，**ERR_CONNECTION_TIMED_OUT**。

网卡设备目录：`/etc/sysconfig/device`

网卡配置目录：``


网卡配置：

```
TYPE=Ethernet
BOOTPROTO=static
DEFROUTE=yes
PEERDNS=yes
PEERROUTES=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_PEERDNS=yes
IPV6_PEERROUTES=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=em3
UUID=cf985ac4-a7c3-41cd-ac92-cdf0a03b84c7
DEVICE=em3
ONBOOT=yes
IPADDR="192.168.1.114"
NETMASK="255.255.255.0"
GATEWAY="192.168.1.114"
DNS1="114.114.114.114"
DNS2="8.8.8.8"
```

#### 网络工具检查

