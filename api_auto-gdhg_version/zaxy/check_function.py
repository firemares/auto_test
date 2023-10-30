import paramiko
import re
from time import sleep
import datetime


#查询系统哪些进程挂掉

#查询redis，timon配置


# 查询数据库所有表名称

# clickhouse
# clickhouse -client -h 127.0.0.1 -uroot --password DF * c3000asi
# select name from system.tables where database = 'asi';

# mysql
# mysql -uroot -p;
# select table_name from information_schema.tables where table_schema = 'asi';