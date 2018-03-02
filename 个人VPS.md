# 个人的VPS

## 系统

Ubuntu

## 软件

- docker
- Nginx
- MySQL
- supervisor
- zsh
- Oh My Zsh

### 安装脚本

#### zsh

```sh
sudo apt-get install zsh
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

配置pip自动补全

```
sudo pip completion --zsh >> ~/.zprofile
source .zprofile
```


## 系统管理

## 防火墙

## 用户管理

## SSR

使用Docker部署，用Supervisor来保证服务常驻。

## 网站

## 日志管理

