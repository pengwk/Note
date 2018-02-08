# MySQL


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

## 可用字段

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

## 用户

### 创建用户

### 授权用户


## 配置

数据库级的配置，MySQL的配置。

## Python连接数据库

### MySQL官方纯Python实现的connector

`mysql-connector-python`安装简单，跨平台，只需通过`pip`即可安装。
