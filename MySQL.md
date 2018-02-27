# MySQL

## 查看帮助

非常重要，遇到不会或者不常用的命令可以查看帮助解决。

`MariaDB [(none)]> ? grant;`


## 优化

## 主从备份、读写分离

#### 1. 创建用户

## SQL语句执行顺序



## 

## 备份&还原



### 备份

备份的对象可以是

- 表的数据
- 表的结构
- 表的数据和结构
- 数据库的数据
- 数据库的结构
- 数据库的数据和结构



#### 备份全部（）

`mysqldump -u root -p database_name > database_name_backup.sql`

### 还原

```bash
mysql -u root -p

create database_name;

use database_name;

source database_name_backup.sql
```

`source`是执行SQL语句的命令。

## 可用字段

通过帮助可以查看支持的所有数据类型。

- int
- char
- varchar
- longtext
- tinytext
- json
- timestamp
- datetime
- 二进制数据


## 字符集

使用UTF-8

数据库连接URL设置字符集为UTF-8

`mysql:root:password@localhost/database?charset=utf-8`

## 用户

### 创建用户

### 授权用户 grant GRANT

`grant all on db1.table1 to 'username'@'host' with max_queries_per_hour 10;`

权限控制：

- `all`
- `select`
- 


## 配置

数据库级的配置，MySQL的配置。

## Python连接数据库

### MySQL官方纯Python实现的connector

`mysql-connector-python`安装简单，跨平台，只需通过`pip`即可安装。
