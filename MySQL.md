# MySQL

## 查看帮助

非常重要，遇到不会或者不常用的命令可以查看帮助解决。

`MariaDB [(none)]> ? grant;`

## 底层实现

#### 索引

B+ Tree


1. 聚集索引
2. 非聚集索引


1.聚集索引

-----

2.非聚集索引

----


##### 列索引（单、多）

#### 临时表


#### 日志

预写日志，方便回滚。

#### 笛卡尔乘积

## SQL语句执行顺序

1. from
2. join
3. on
3. where
4. group by
5. avg, sum
6. having
7. select
8. distinct
9. order by

-----
首先找到相应的数据集，再筛选数据，数据确定后进行排序。

## 优化


#### 查看执行计划

**explain**在原来的select语句前加`explain`即可。

```sql
MariaDB [iot]> explain select * from device;
+------+-------------+--------+------+---------------+------+---------+------+------+-------+
| id   | select_type | table  | type | possible_keys | key  | key_len | ref  | rows | Extra |
+------+-------------+--------+------+---------------+------+---------+------+------+-------+
|    1 | SIMPLE      | device | ALL  | NULL          | NULL | NULL    | NULL |    2 |       |
+------+-------------+--------+------+---------------+------+---------+------+------+-------+
```

#### show profiles


#### 慢查询日志

#### 原则们

1. 小结果集驱动大结果集
2. 尽一切可能避免全表扫描
3. 仅查询返回自己需要的列

#### 全表扫描

什么情况下会导致全表扫描？

#### 读写分离

在主（master）上写，同步到从（slave）上，并且配置应用程序只在从机上读数据。

## 主从备份、读写分离

#### 1. 创建用户





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
