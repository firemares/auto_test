import paramiko
import re
from time import sleep
import datetime


#��ѯϵͳ��Щ���̹ҵ�

#��ѯredis��timon����


# ��ѯ���ݿ����б�����

# clickhouse
# clickhouse -client -h 127.0.0.1 -uroot --password DF * c3000asi
# select name from system.tables where database = 'asi';

# mysql
# mysql -uroot -p;
# select table_name from information_schema.tables where table_schema = 'asi';