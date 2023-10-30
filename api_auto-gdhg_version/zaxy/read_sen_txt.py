import requests
import threading
import time
import re
import datetime
from time import sleep
import random


def creat_senstives():
    file=open('敏感数据.txt')
    txt_content=str(file.readlines()).replace('：','： ')
    print(txt_content)
    sen = txt_content.split(" ")
    # print(sen)
    senstive_name=[]
    senstive_content=[]

    for i in sen:
        if re.match('\S+：',i,re.S)==None:
            # print(i)
            senstive_content.append(i.replace('\\n',''))
        else:
            senstive_name.append(i)
            pass
    return senstive_content


def request_content(ser_name,sen_value):

# ***每次启动必须修改的地方***
#     url = "http://192.168.10.161:30080/collector/v1/data/source/plugin"

    null = ""

    data_sen = {"url": "https://"+str(ser_name)+"/senstive/vasdada/audasit?a="+sen_value, "method": "POST",
            "protocol": "http/1.1", "statusCode": 200, "requestTimestamp": time.time(), "responseTimestamp": null,
            "clientAddress": "192.168.10.113", "clientPort": null, "localIp": "192.168.101.212", "localPort": "553",
            "remoteAddress": "192.168.10.61", "remotePort": 443,
            "requestHeaders": [{"name": "Accept", "value": "application/json, text/plain, */*"},
                               {"name": "Accept-Encoding", "value": "gzip, deflate, br"},
                               {"name": "Accept-Language", "value": "zh-CN,zh;q=0.9"},
                               {"name": "Cache-Control", "value": "no-cache"},
                               {"name": "Connection", "value": "keep-alive"},
                               {"name": "Server", "value": "Nginx"},
                               {"name": "Content-Type", "value": "application/json;charset=UTF-8"},
                               {"name": "Cookie", "value": "JSESSIONID=C81B617FBE6E696F3915B5EBB5CB01C0"},
                               {"name": "Host", "value": "192.168.110.161"}, {"name": "Pragma", "value": "no-cache"},
                               {"name": "Referer", "value": "https://192.168.110.1/"},
                               {"name": "Sec-Fetch-Dest", "value": "empty"},
                               {"name": "Sec-Fetch-Mode", "value": "cors"},
                               {"name": "Sec-Fetch-Site", "value": "same-origin"},
                               {"name": "User-Agent","value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
                               {"name": "Token",
                                "value": "eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ"},
                               {"name": "x-request-id", "value": "1949107800.105645"}],
            "responseHeaders": [{"name": "Cache-Control", "value": "no-cache, no-store, max-age=0, must-revalidate"},
                                {"name": "Connection", "value": "keep-alive"},
                                # 下载接口
                                # "application/x-msdownload"
                                {"name": "Content-Type", "value": "application/json"},
                                {"name": "Date", "value": "Mon, 24 Apr 2023 07:08:24 GMT"},
                                {"name": "Expires", "value": "0"}, {"name": "Pragma", "value": "no-cache"},
                                {"name": "Server", "value": "nginx"}, {"name": "Transfer-Encoding", "value": "chunked"},
                                {"name": "X-Content-Type-Options", "value": "nosniff"},
                                {"name": "X-Frame-Options", "value": "DENY"},
                                {"name": "X-XSS-Protection", "value": "1; mode=block"},
                                {"name": "Token","value":"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ"}
                                ],

            "requestPayload": "{\"useasdae\":\"SecAdmin\",\"asdord\":\"asada345\",\"captcha\":\"1493\",\"uuid\":\""+sen_value+"\"}",
            "responseContent":"{\"token\":\"\",\"result\": \"success\",\"data\": {\"aa\": \"11\",\"aaa\": \"404\",\"aaab\": \"11\",\"adasa\": \"11\",\"awsa\": \"11\",\"bb\": \"11\",\"data\": [{\"aa\": \"aa\"},{\"bb\": \"aa\"},{\"assaa1\": \"aav\"},{\"asa1\": \"aav\"},{\"aaw\": \"aa\"},{\"aqa\": \"aa\"},{\"aaba\": \"aba\"}]}}\n"}
            # "responseContent": "{\"exception\":500,\"result\":\"success\",\"data\": {\"aa\": \"11\",\"bb\": \"11\",\"data\": [{\"aa\": \"aa\"}, {\"bb\": \"aa\"}],\"msg\":\"\",\"events\":[{\"type\":\"presence\",\"user_id\":24,\"server_timestamp\":1683855835.4996939,\"presence\":{\"ZulipElectron\":{\"client\":\"ZulipElectron\",\"status\":\"active\",\"exception\":500,\"timestamp\":1683855835,\"pushable\":false}},\"id\":2269}],\"queue_id\":\"1683410438:278\"}\n"}

    return data_sen




def sent_request(ser_name):
    url = "http://172.16.76.213:30080/collector/v1/data/source/plugin"

    head = {
        'Content-Type': 'application/json'
    }

    x= 0
    # api个数

    for i in creat_senstives():
        # api个数
            x=x+1
            # a = random.randint(1, 1999)
            # json=request_content(ser_name+"/saas"+str(a)+"/sada",str(i.replace("',","")))
            # a = random.randint(1, 1999)
            json = request_content(ser_name + "/saas" + str(x) + "/sada", str(i.replace("',", "")))
            response_sen = requests.post(url, json=json, headers=head)
            print(json)

if __name__ == "__main__":
    # print('请输入服务名称')
    # ser_name=input()

    name='test'
    for i in range(5):
        sent_request('test1.com')

    # for i in range(20):
    #     b = random.randint(1, 199)
    #     sent_request(name+str(b)+'.com')
        # sent_request('test194.com')
    # sent_request('seaaasdasddfame.com')
