# MySQL


## 备份&还原



### 备份

`mysqldump -u root -p database_name > database_name_backip.sql`

### 还原

```bash
mysql -u root -p

create database_name;

use database_name;

source database_name_backup.sql
```

## 字符集

使用UTF-8

## 

