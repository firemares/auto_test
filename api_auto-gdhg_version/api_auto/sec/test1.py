import time
import datetime

import requests

head = {
    # 'sn':'tp50h0h0k0l0FTz8k',
    'Content-Type': 'application/json',
    'Token':'token-ddf-test-453743'
}
data1='sn=tp50h0h0k0l0FTz8k'


response= requests.get('http://192.168.10.212:30080/alarm/v1/receiverConfig/get/2',headers=head,json=data1)
# 'sn=tp50h0h0k0l0FTz8k'
print(response.text)
# {
# GETLICENSE("获取系统授权信息 ","GET","/system/v1/license/index"),
# GETSYSTIME("获取系统时间","GET","/system/v1/time/sys"),
# UPDATASYSTIME("修改系统时间","PUT","/system/v1/time/sys"),
# DOWNCPU("下载系统.cpu文件","GET","/system/v1/license/cpu/serialize"),
# ACTIVELICENSE("系统激活 ","POST","/system/v1/license/active"),
# GETSYSLOG("获取syslog通知信息","GET","/alarm/v1/receiverConfig/get"),
# UPDATESYSLOG("修改syslog通知信息","PUT","/alarm/v1/receiverConfig"),
# GETEMAIL("获取邮件通知信息","GET","/alarm/v1/receiverConfig/get"),
# UPDATEEMAIL("修改邮件通知信息","PUT","/alarm/v1/receiverConfig"),
# GETUPGRADE("获取系统升级记录列表（未分页）","GET","/system/v1/upgrade/update/logs"),
# GETUPGRADEPAGE("获取系统升级记录列表（分页）","GET","system/v1/upgrade/update/logsPage"),
# SYSUPGRADE("系统升级","GET","/system/v1/upgrade/update"),
# GETBACKUP("获取系统备份记录列表","POST","/system/v1/backup/backup-list"),
# GETSTORAGESPACE("存储空间信息","GET","/system/v1/backup/storageSpace"),
# EXECBACKUP("执行备份","POST","/system/v1/backup/backup"),
# DELBACKUP("删除备份","POST","/system/v1/backup/delete"),
# DOWNBACKUP("下载备份","GET","/system/v1/backup"),
# APPLISTPAGE("应用列表（分页）","GET","/manager/v1/apps/list"),
# APPLIST("应用列表（不分页）","GET","/manager/v1/apps"),
#
# APPDELETE("应用删除","DELETE","/manager/v1/apps"),
# APIMANAGER("删除API","DELETE","/manager/v1/api-manager"),
# FULL_SYNC("全量同步","POST","/manager/v1/device/full/sync"),
# IMPOYTAPILIST("导入API","POST","/manager/v1/api-manager/importApiList"),
# REMOVE_API("移除API","PUT","/manager/v1/api-manager/removeApi"),
# INSERT_API("手工添加API","POST","/manager/v1/api-manager/insert"),
# BATCH_MANAGER_API("批量收录API","PUT","/manager/v1/api-manager/batchApiPathParamRepeat"),
# MANAGER_API("收录API","PUT","/manager/v1/api-manager/apiPathParamRepeat");}

# class call_counter(object):
#     calls = 0
#     def __init__(self):
#         pass
#     def f(self):
#         call_counter.calls += 1
#         # print(1)
#
#
# # def p():
# #     print(1)
# #
# # def f():
# #     print(1)
#
# for i in range(10):
#     call_counter().f()
#
# print(call_counter.calls)

# print("aaa"+datetime.datetime.now())