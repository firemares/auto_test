import re
import time
import datetime

import requests

apis = [
    ["获取系统授权信息 ", "GET", "/system/v1/license/index"],
    ["获取系统时间", "GET", "/system/v1/time/sys"],
    ["修改系统时间", "PUT", "/system/v1/time/sys"],
    ["下载系统.cpu文件", "GET", "/system/v1/license/cpu/serialize"],
    ["系统激活 ", "POST", "/system/v1/license/active"],
    ["获取syslog通知信息", "GET", "/alarm/v1/receiverConfig/get"],
    ["修改syslog通知信息", "PUT", "/alarm/v1/receiverConfig"],
    ["获取邮件通知信息", "GET", "/alarm/v1/receiverConfig/get"],
    ["修改邮件通知信息", "PUT", "/alarm/v1/receiverConfig"],
    ["获取系统升级记录列表（未分页）", "GET", "/system/v1/upgrade/update/logs"],
    ["获取系统升级记录列表（分页）", "GET", "system/v1/upgrade/update/logsPage"],
    ["系统升级", "GET", "/system/v1/upgrade/update"],
    ["获取系统备份记录列表", "POST", "/system/v1/backup/backup-list"],
    ["存储空间信息", "GET", "/system/v1/backup/storageSpace"],
    ["执行备份", "POST", "/system/v1/backup/backup"],
    ["删除备份", "POST", "/system/v1/backup/delete"],
    ["下载备份", "GET", "/system/v1/backup"],
    ["应用列表（分页）", "GET", "/manager/v1/apps/list"],
    ["应用列表（不分页）", "GET", "/manager/v1/apps"],
    ["应用删除", "DELETE", "/manager/v1/apps"],
    ["删除API", "DELETE", "/manager/v1/api-manager"],
    ["全量同步", "POST", "/manager/v1/device/full/sync"],
    ["导入API", "POST", "/manager/v1/api-manager/importApiList"],
    ["移除API", "PUT", "/manager/v1/api-manager/removeApi"],
    ["手工添加API", "POST", "/manager/v1/api-manager/insert"],
    ["批量收录API", "PUT", "/manager/v1/api-manager/batchApiPathParamRepeat"],
    ["收录API", "PUT", "/manager/v1/api-manager/apiPathParamRepeat"]
]
def check_api_respnose(fun,path):
    addr = 'http://192.168.10.212:30080'

    url =  addr+path
    head = {
        'Content-Type': 'application/json',
        'Token':'token-ddf-test-453743'
    }
    if fun == 'GET':
        response= requests.get(url,headers=head)
    elif fun == 'POST':
        response = requests.post(url, headers=head)
    elif fun == 'DELETE':
        response = requests.delete(url, headers=head)
    elif fun == 'PUT':
        response = requests.put(url, headers=head)


    print(response.text)

    return response.text




check_api_respnose('POST',"/manager/v1/api-manager/importApiList")
# print(type('/system/v1/license/index'))
# for i in apis:
#     path = i[2]
#     # print(i[1])
#     # print(type(i[1]))
#     try:
#         status_code=re.findall('"code":200',check_api_respnose(i[1],path),re.S)
#         # print(status_code)
#         if status_code ==[]:
#             print(i)
#     except Exception as e:
#         print(i)
#         pass
#     else:
#         pass
#





