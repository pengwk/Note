## Mac 系统

### brew

#### 获取相关信息

- brew info mongo
- brew search mongo

#### 安装卸载

- brew install mongodb@3.4
- brew uninstall mongodb@3.4
- brew list 列出所有 brew 安装的软件包

#### 服务管理

- brew services list 列出当前用户所有服务
- brew services run 一次性运行
- brew services start redis 加入开机启动或者登录启动
- brew services stop redis 停止服务并从开机启动或登录启动中移除
- brew services restart 重启服务并从开机启动或登录启动中移除
- brew services cleanup 清理无用的服务

开机启动要求使用 sudo，默认是 登录启动

### iTerm2

- command + t 新建标签页（ TAB ）
- command + w 关闭当前标签页（ TAB ）
- command + n 新建窗口
- command + d 垂直切分标签页
- command + shift + d 水平切分标签页
- ⌘ + ]或者 ⌘ + [ 分屏标签页间切换
- command + ; 自动补全
- command + 2 切换到第二个标签页

#### 其他技巧

1. open ~ 使用 Finder 打开home目录

## 其他小问题

### Git 在 Terminal 下中文显示有问题

`git config –global core.quotepath false`
