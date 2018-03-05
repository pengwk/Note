# 工作中的Docker

### 后台运行

`docker-compose up -d`


### 启动容器

`docker run -it -p 80:80 container_name`


## 常用docker

使用官方提供的镜像Image，将

### MySQL

- 镜像选择 官方
- 版本选择 5.7 mysql:5.7
- root账户设置 `-e MYSQL_ROOT_PASSWORD=my-secret-pw`
- 数据文件 `-v /my/own/datadir:/var/lib/mysql`
- 配置文件 

将配置文件`mysql.cnf`放到`/my/custom/`目录下，`-v /my/custom/:/etc/mysql/conf.d`

- 日志文件
- 外网访问
- 官方文档 <https://hub.docker.com/_/mysql/>

注意事项：

```
docker pull mysql
```

### Redis


### Nginx
