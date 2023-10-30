import requests
import threading
import time
import re
import datetime
from time import sleep


# response = requests.post(url,json=data,headers=head)
# print(response.text)

def creat_senstives():
    file = open('敏感数据.txt')
    txt_content = str(file.readlines()).replace('：', '： ')
    # print(txt_content)
    sen = txt_content.split(" ")
    # print(sen)
    senstive_name = []
    senstive_content = []

    for i in sen:
        if re.match('\S+：', i, re.S) == None:
            # print(i)
            senstive_content.append(i.replace('\\n', ''))
        else:
            senstive_name.append(i)
            pass
    return senstive_content

def jobs(num,ser_name):
    head = {
        'Content-Type': 'application/json'
    }

# ***每次启动必须修改的地方***
    url = "http://172.16.76.213:30080/collector/v1/data/source/plugin"

    null = ""
    data_web = {"url": "https://"+str(ser_name)+"/audiwwwqqct/vbaaqqqqbbqw/audiqet-log/login?a=15684236954", "method": "POST",
            "protocol": "http/1.1", "statusCode": 200, "requestTimestamp": time.time(), "responseTimestamp": null,
            "clientAddress": "85.25.43.84", "clientPort": "8080", "localIp": "192.168.10.222", "localPort": "553",
            "remoteAddress": "121.8.215.106", "remotePort": 443,
            "requestHeaders": [{"name": "Accept", "value": "application/json, text/plain, */*"},
                               {"name": "Accept-Encoding", "value": "gzip, deflate, br"},
                               {"name": "Accept-Language", "value": "zh-CN,zh;q=0.9"},
                               {"name": "Cache-Control", "value": "no-cache"},
                               {"name": "Connection", "value": "keep-alive"},
                               {"name": "Content-Type", "value": "application/json;charset=UTF-8"},
                               {"name": "Cookie", "value": "JSESSIONID=C81B617FBE6E696F3915B5EBB5CB01C0"},
                               {"name": "Host", "value": "192.168.10.161"}, {"name": "Pragma", "value": "no-cache"},
                               {"name": "Referer", "value": "https://192.168.10.161/"},
                               {"name": "Sec-Fetch-Dest", "value": "empty"},
                               {"name": "Server", "value": "Nginx"},
                               {"name": "Sec-Fetch-Mode", "value": "cors"},
                               {"name": "Sec-Fetch-Site", "value": "same-origin"},
                               {"name": "User-Agent","value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
                               {"name": "token",
                                "value": "eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ"},
                               {"name": "x-request-id", "value": "1949107800.105645"}],
            "responseHeaders": [{"name": "Cache-Control", "value": "no-cache, no-store, max-age=0, must-revalidate"},
                                {"name": "Connection", "value": "keep-alive"},
                                # 下载接口
                                {"name": "Content-Type", "value": "application/json"},
                                {"name": "Date", "value": "Mon, 24 Apr 2023 07:08:24 GMT"},
                                {"name": "Expires", "value": "0"}, {"name": "Pragma", "value": "no-cache"},
                                {"name": "Server", "value": "nginx"}, {"name": "Transfer-Encoding", "value": "chunked"},
                                {"name": "X-Content-Type-Options", "value": "nosniff"},
                                {"name": "X-Frame-Options", "value": "DENY"},
                                {"name": "X-XSS-Protection", "value": "1; mode=block"}],
            "requestPayload": "{\"username\":\"SecAdmin\",\"password\":\"admin12345\",\"captcha\":\"eval[6]\",\"uuid\":\"02617812\"}",
            "responseContent":"{\"sessionTimeoutSecond\":1800,\"code\":200,\"aa\":15768495336,\"msg\":\"操作成功\",\"data\":{\"role\":\"sadsad\",\"roleId\":\"2\",\"sessionTimeout\":30,\"userId\":\"2\",\"pwInvalidTime\":1681494743000,\"token\":\"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjMxMzQ3qwUA3pf3ZScAAAA.rZQwP-_IpYLMBv8VosLkGx6mLMXzumQsqkT_rfEg-mIPGxM0ffcNACOsdHATtcvg80dXYznqmNJsiRcooTHlrw\",\"username\":\"SecAdmin\"},\"successFlag\":true}"}


    data_mobile = {"url": "https://"+str(ser_name)+"/audiwwwqqct/vbaaqqqqbbqw/audiqet-log/login?a=15684236954", "method": "POST",
            "protocol": "http/1.1", "statusCode": 200, "requestTimestamp": time.time(), "responseTimestamp": null,
            "clientAddress": "85.25.43.84", "clientPort": "8080", "localIp": "192.168.10.222", "localPort": "553",
            "remoteAddress": "121.8.215.106", "remotePort": 443,
            "requestHeaders": [{"name": "Accept", "value": "application/json, text/plain, */*"},
                               {"name": "Accept-Encoding", "value": "gzip, deflate, br"},
                               {"name": "Accept-Language", "value": "zh-CN,zh;q=0.9"},
                               {"name": "Cache-Control", "value": "no-cache"},
                               {"name": "Connection", "value": "keep-alive"},
                               {"name": "Content-Type", "value": "application/json;charset=UTF-8"},
                               {"name": "Cookie", "value": "JSESSIONID=C81B617FBE6E696F3915B5EBB5CB01C0"},
                               {"name": "Host", "value": "192.168.10.161"}, {"name": "Pragma", "value": "no-cache"},
                               {"name": "Referer", "value": "https://192.168.10.161/"},
                               {"name": "Sec-Fetch-Dest", "value": "empty"},
                               {"name": "Server", "value": "Nginx"},
                               {"name": "Sec-Fetch-Mode", "value": "cors"},
                               {"name": "Sec-Fetch-Site", "value": "same-origin"},
                               # Android
                               {"name": "User-Agent","value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/83.0.4103.97 Safari/537.36 Android"},
                               {"name": "token",
                                "value": "eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ"},
                               {"name": "x-request-id", "value": "1949107800.105645"}],
            "responseHeaders": [{"name": "Cache-Control", "value": "no-cache, no-store, max-age=0, must-revalidate"},
                                {"name": "Connection", "value": "keep-alive"},
                                # 下载接口
                                {"name": "Content-Type", "value": "application/json"},
                                {"name": "Date", "value": "Mon, 24 Apr 2023 07:08:24 GMT"},
                                {"name": "Expires", "value": "0"}, {"name": "Pragma", "value": "no-cache"},
                                {"name": "Server", "value": "nginx"}, {"name": "Transfer-Encoding", "value": "chunked"},
                                {"name": "X-Content-Type-Options", "value": "nosniff"},
                                {"name": "X-Frame-Options", "value": "DENY"},
                                {"name": "X-XSS-Protection", "value": "1; mode=block"}],
            "requestPayload": "{\"username\":\"SysAdmin\",\"password\":\"admin12345\",\"captcha\":\"eval[6]\",\"uuid\":\"02617812\"}",
            "responseContent":"{\"sessionTimeoutSecond\":1800,\"code\":200,\"aa\":15768495336,\"msg\":\"操作成功\",\"data\":{\"role\":\"sadsad\",\"roleId\":\"2\",\"sessionTimeout\":30,\"userId\":\"2\",\"pwInvalidTime\":1681494743000,\"token\":\"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjMxMzQ3qwUA3pf3ZScAAAA.rZQwP-_IpYLMBv8VosLkGx6mLMXzumQsqkT_rfEg-mIPGxM0ffcNACOsdHATtcvg80dXYznqmNJsiRcooTHlrw\",\"username\":\"SysAdmin\"},\"successFlag\":true}"}

    data_account = {"url": "https://"+str(ser_name)+"/audiwwwqqct/vbaaqqqqbbqw/audiqet-log/login?a=15684236954", "method": "POST",
            "protocol": "http/1.1", "statusCode": 200, "requestTimestamp": time.time(), "responseTimestamp": null,
            "clientAddress": "85.25.43.84", "clientPort": "8080", "localIp": "192.168.10.222", "localPort": "553",
            "remoteAddress": "121.8.215.106", "remotePort": 443,
            "requestHeaders": [{"name": "Accept", "value": "application/json, text/plain, */*"},
                               {"name": "Accept-Encoding", "value": "gzip, deflate, br"},
                               {"name": "Accept-Language", "value": "zh-CN,zh;q=0.9"},
                               {"name": "Cache-Control", "value": "no-cache"},
                               {"name": "Connection", "value": "keep-alive"},
                               {"name": "Content-Type", "value": "application/json;charset=UTF-8"},
                               {"name": "Cookie", "value": "JSESSIONID=C81B617FBE6E696F3915B5EBB5CB01C0"},
                               {"name": "Host", "value": "192.168.10.161"}, {"name": "Pragma", "value": "no-cache"},
                               {"name": "Referer", "value": "https://192.168.10.161/"},
                               {"name": "Sec-Fetch-Dest", "value": "empty"},
                               {"name": "Server", "value": "Nginx"},
                               {"name": "Sec-Fetch-Mode", "value": "cors"},
                               {"name": "Sec-Fetch-Site", "value": "same-origin"},
                               # Android
                               {"name": "User-Agent","value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/83.0.4103.97 Safari/537.36 Android"},
                               {"name": "token",
                                "value": "eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ"},
                               {"name": "x-request-id", "value": "1949107800.105645"}],
            "responseHeaders": [{"name": "Cache-Control", "value": "no-cache, no-store, max-age=0, must-revalidate"},
                                {"name": "Connection", "value": "keep-alive"},
                                # 下载接口
                                {"name": "Content-Type", "value": "application/json"},
                                {"name": "Date", "value": "Mon, 24 Apr 2023 07:08:24 GMT"},
                                {"name": "Expires", "value": "0"}, {"name": "Pragma", "value": "no-cache"},
                                {"name": "Server", "value": "nginx"}, {"name": "Transfer-Encoding", "value": "chunked"},
                                {"name": "X-Content-Type-Options", "value": "nosniff"},
                                {"name": "X-Frame-Options", "value": "DENY"},
                                {"name": "X-XSS-Protection", "value": "1; mode=block"}],
            "requestPayload": "{\"username\":\"SecAdmin\",\"password\":\"admin12345\",\"captcha\":\"eval[6]\",\"uuid\":\"02617812\"}",
            "responseContent":"{\"sessionTimeoutSecond\":1800,\"code\":200,\"aa\":15768495336,\"msg\":\"操作成功\",\"data\":{\"role\":\"sadsad\",\"roleId\":\"2\",\"sessionTimeout\":30,\"userId\":\"2\",\"pwInvalidTime\":1681494743000,\"token\":\"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjMxMzQ3qwUA3pf3ZScAAAA.rZQwP-_IpYLMBv8VosLkGx6mLMXzumQsqkT_rfEg-mIPGxM0ffcNACOsdHATtcvg80dXYznqmNJsiRcooTHlrw\",\"username\":\"SecAdmin\"},\"successFlag\":true}"}


    data1 = {"url": "https://"+str(ser_name)+"/audkksadads2qqt/vada/audasit-log?a=15684236954", "method": "POST",
            "protocol": "http/1.1", "statusCode": 200, "requestTimestamp": time.time(), "responseTimestamp": null,
            "clientAddress": "192.168.10.113", "clientPort":"8080", "localIp": "192.168.101.212", "localPort": "553",
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
                               {"name": "Referer", "value": "https://192.168.110.161/"},
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
                                # "application/json"
                                {"name": "Content-Type", "value": "application/json"},
                                {"name": "Date", "value": "Mon, 24 Apr 2023 07:08:24 GMT"},
                                {"name": "Expires", "value": "0"}, {"name": "Pragma", "value": "no-cache"},
                                {"name": "Server", "value": "nginx"}, {"name": "Transfer-Encoding", "value": "chunked"},
                                {"name": "X-Content-Type-Options", "value": "nosniff"},
                                {"name": "X-Frame-Options", "value": "DENY"},
                                {"name": "X-XSS-Protection", "value": "1; mode=block"},
                                {"name": "Token","value":"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ"}
                                ],

            "requestPayload": "{\"username\":\"SysAdmin\",\"password\":\"admin12345\",\"captcha\":\"1493\",\"uuid\":\"02617812\"}",
            "responseContent":"{\"token\":\"\",\"result\": \"success\",\"data\": {\"aa\": \"511\",\"aaa\": \"404\",\"aaab\": \"11\",\"adasa\": \"11\",\"awsa\": \"11\",\"bb\": \"11\",\"data\": [{\"aa\": \"aa\"},{\"bb\": \"aa\"},{\"assaa1\": \"aav\"},{\"asa1\": \"aav\"},{\"aaw\": \"aa\"},{\"aqa\": \"aa\"},{\"aaba\": \"aba\"}]}}\n"}
            # "responseContent": "{\"exception\":500,\"result\":\"success\",\"data\": {\"aa\": \"11\",\"bb\": \"11\",\"data\": [{\"aa\": \"aa\"}, {\"bb\": \"aa\"}],\"msg\":\"\",\"events\":[{\"type\":\"presence\",\"user_id\":24,\"server_timestamp\":1683855835.4996939,\"presence\":{\"ZulipElectron\":{\"client\":\"ZulipElectron\",\"status\":\"active\",\"exception\":500,\"timestamp\":1683855835,\"pushable\":false}},\"id\":2269}],\"queue_id\":\"1683410438:278\"}\n"}


    data_account1 = {"url": "https://"+str(ser_name)+"/oarrwert9/d1asd/das2d/da3asd/ds4a/cx5z/czc6qwdq/v7vzx/rew8rt/fsore9/archrwerarams=%7B%22txttitle%22%3A%22%22%2C%22txtarchiveno%22%3A%22%22%2C%22zihao%22%3A%22%22%2C%22txtlaiwendept%22%3A%22%22%2C%22flag%22%3A%22%22%2C%22archivefiletypeguid%22%3A%22%22%2C%22inducestate%22%3A%22%22%2C%22jpdjinji%22%3A%22%22%2C%22jpdmiji%22%3A%22%22%2C%22jpdfileguifanshuxing%22%3A%22%22%2C%22startdate%22%3A%22%22%2C%22enddate%22%3A%22%22%2C%22initouname%22%3A%22%22%2C%22searchtype%22%3A%22%22%2C%22operatorfordisplayname%22%3A%22%22%2C%22handleself%22%3A%22%22%2C%22pagesize%22%3A%2210%22%2C%22currentpageindex%22%3A8%7Dparams=%7B%22txttitle%22%3A%22%22%2C%22txtarchiveno%22%3A%22%22%2C%22zihao%22%3A%22%22%2C%22txtlaiwendept%22%3A%22%22%2C%22flag%22%3A%22%22%2C%22archivefiletypeguid%22%3A%22%22%2C%22inducestate%22%3A%22%22%2C%22jpdjinji%22%3A%22%22%2C%22jpdmiji%22%3A%22%22%2C%22jpdfileguifanshuxing%22%3A%22%22%2C%22startdate%22%3A%22%22%2C%22enddate%22%3A%22%22%2C%22initouname%22%3A%22%22%2C%22searchtype%22%3A%22%22%2C%22operatorfordisplayname%22%3A%22%22%2C%22handleself%22%3A%22%22%2C%22pagesize%22%3A%2210%22%2C%22currentpageindex%22%3A9%7Dparams=%7B%22txttitle%22%3A%22%22%2C%22txtarchiveno%22%3A%22%22%2C%22zihao%22%3A%22%22%2C%22txtlaiwendept%22%3A%22%22%2C%22flag%22%3A%22%22%2C%22archivefiletypeguid%22%3A%22%22%2C%22inducestate%22%3A%22%22%2C%22jpdjinji%22%3A%22%22%2C%22jpdmiji%22%3A%22%22%2C%22jpdfileguifanshuxing%22%3A%22%22%2C%22startdate%22%3A%22%22%2C%22enddate%22%3A%22%22%2C%22initouname%22%3A%22%22%2C%22searchtype%22%3A%22%22%2C%22operatorfordisplayname%22%3A%22%22%2C%22handleself%22%3A%22%22%2C%22pagesize%22%3A%2210%22%2C%22currentpageindex%22%3A10%7Dparams=%7B%22txttitle%22%3A%22%22%2C%22txtarchiveno%22%3A%22%22%2C%22zihao%22%3A%22%22%2C%22txtlaiwendept%22%3A%22%22%2C%22flag%22%3A%22%22%2C%22archivefiletypeguid%22%3A%22%22%2C%22inducestate%22%3A%22%22%2C%22jpdjinji%22%3A%22%22%2C%22jpdmiji%22%3A%22%22%2C%22jpdfileguifanshuxing%22%3A%22%22%2C%22startdate%22%3A%22%22%2C%22enddate%22%3A%22%22%2C%22initouname%22%3A%22%22%2C%22searchtype%22%3A%22%22%2C%22operatorfordisplayname%22%3A%22%22%2C%22handleself%22%3A%22%22%2C%22pagesize%22%3A%2210%22%2C%22currentpageindex%22%3A11%7DPOST", "method": "POST",
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
                               {"name": "Referer", "value": "https://192.168.110.161/"},
                               {"name": "Sec-Fetch-Dest", "value": "empty"},
                               {"name": "Sec-Fetch-Mode", "value": "cors"},
                               {"name": "Sec-Fetch-Site", "value": "same-origin"},
                               {"name": "User-Agent","value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
                               {"name": "Token",
                                "value": "eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ"},
                               {"name": "x-request-id", "value": "1949107800.105645"}],
            "responseHeaders": [{"name": "Cache-Control", "value": "no-cache, no-store, max-age=0, must-revalidate"},
                                {"name": "Connection", "value": "keep-alive"},
                                {"name": "Content-Type", "value": "application/json"},
                                {"name": "Date", "value": "Mon, 24 Apr 2023 07:08:24 GMT"},
                                {"name": "Expires", "value": "0"}, {"name": "Pragma", "value": "no-cache"},
                                {"name": "Server", "value": "nginx"}, {"name": "Transfer-Encoding", "value": "chunked"},
                                {"name": "X-Content-Type-Options", "value": "nosniff"},
                                {"name": "X-Frame-Options", "value": "DENY"},
                                {"name": "X-XSS-Protection", "value": "1; mode=block"},
                                {"name": "Token","value":"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ"}
                                ],

            "requestPayload": "{\"username\":\""+ser_name+"\",\"password\":\"admin12345\",\"captcha\":\"1493\",\"uuid\":\"02617812\"}",
            "responseContent":"{\"token\":\"\",\"result\": \"success\",\"data\": {\"aa\": \"11\",\"aaa\": \"404\",\"aaab\": \"11\",\"adasa\": \"11\",\"awsa\": \"11\",\"bb\": \"11\",\"data\": [{\"aa\": \"aa\"},{\"bb\": \"aa\"},{\"assaa1\": \"aav\"},{\"asa1\": \"aav\"},{\"aaw\": \"aa\"},{\"aqa\": \"aa\"},{\"aaba\": \"aba\"}]}}\n"}

    data3 = {
        "url": "https://"+str(ser_name)+"/json/events?dont_block=false&queue_id=1683410438%3A278&last_event_id=2268&client_gravatar=true&slim_presence=true",
        "method": "GET", "protocol": "h2", "statusCode": 200, "requestTimestamp": time.time(),
        "responseTimestamp": null, "clientAddress":null, "clientPort": null, "localIp": "192.168.10.222",
        "localPort": "553", "remoteAddress": "172.16.0.6", "remotePort": 443,
        "requestHeaders": [{"name": ":authority", "value": "chat.csdev.com"}, {"name": ":method", "value": "GET"},
                           {"name": ":path",
                            "value": "/json/events?dont_block=false&queue_id=1683410438%3A278&last_event_id=2268&client_gravatar=true&slim_presence=true"},
                           {"name": ":scheme", "value": "https"},
                           {"name": "accept", "value": "application/json, text/javascript, */*; q=0.01"},
                           {"name": "accept-encoding", "value": "gzip, deflate, br"},
                           {"name": "accept-language", "value": "zh-CN,zh;q=0.9"},
                           {"name": "cache-control", "value": "no-cache"},
                           {"name": "referer", "value": "https://chat.csdev.com/"},
                           {"name": "sec-fetch-dest", "value": "empty"}, {"name": "sec-fetch-mode", "value": "cors"},
                           {"name": "sec-fetch-site", "value": "same-origin"},
                           {"name": "user-agent", "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
                           {"name": "x-csrftoken",
                            "value": "SqGeHphhbqwpg5pF8FC2S0q2avHHpRuWxJ5ikbgToy7FlZUmwCxBhuUnWxyrwSG5"},
                           {"name": "x-requested-with", "value": "XMLHttpRequest"}],
        "responseHeaders": [
            {"name": "cache-control", "value": "max-age=0, no-cache, no-store, must-revalidate, private"},
            {"name": "content-encoding", "value": "gzip"}, {"name": "content-language", "value": "zh-hans"},
            {"name": "content-type", "value": "application/json"},
            {"name": "date", "value": "Fri, 12 May 2023 01:43:55 GMT"},
            {"name": "etag", "value": "W/\"b9db0445037752eb446271d6fc7ca28a347748ac\""},
            {"name": "expires", "value": "Fri, 12 May 2023 01:43:55 GMT"},
            {"name": "server", "value": "nginx"}, {"name": "status", "value": "200"},
            {"name": "strict-transport-security", "value": "max-age=15768000"},
            {"name": "vary", "value": "Accept-Encoding\nAccept-Language, Cookie"},
            {"name": "x-content-type-options", "value": "nosniff"},
            {"name": "x-frame-options", "value": "DENY"},
            {"name": "x-xss-protection", "value": "1; mode=block"}], "requestPayload": null,
        "responseContent": "{\"exception\":500,\"result\":\"success\",\"msg\":\"\",\"events\":[{\"type\":\"presence\",\"user_id\":24,\"server_timestamp\":1683855835.4996939,\"presence\":{\"ZulipElectron\":{\"client\":\"ZulipElectron\",\"status\":\"active\",\"exception\":500,\"timestamp\":1683855835,\"pushable\":false}},\"id\":2269}],\"queue_id\":\"1683410438:278\"}\n"}



    start_time = time.time()
    for i in range(num):
        # pc/mobile接口
        response=requests.post(url, json=data_web, headers=head)
        response1 = requests.post(url, json=data_mobile, headers=head)
        response2 = requests.post(url, json=data_account, headers=head)
        # # url敏感，状态码200,弱点响应字段,下载
        # response = requests.post(url, json=data1, headers=head)
        # 自适应账号名称
        # response2=requests.post(url, json=data_account, headers=head)
        # 错误码500
        # response2=requests.post(url, json=data, headers=head)
        # response3 = requests.post(url, json=data3, headers=head)
        # print('1')
        if response.text=="上传成功！":
            continue
        else:
            print("流量存在问题")

    last_time = time.time()
    num = i/(last_time-start_time)
    # print(num)
    # print("流量状态:"+response.text)
    # print(2)



def thread(num,threads_num,ser_name):
    theards=[]
    # job="test"
    for i in range(1,threads_num):
        # name=job+str(i)
        theards.append(
            threading.Thread(target=jobs,args=(num,ser_name))
        )
    for t in theards:
         t.start()
    for t in theards:
        t.join()

if __name__ == "__main__":
    # 'https://192.168.14.198/audit/vwqeqwe/audit-lqweqwog/isKeepAndAllApi?periodType=15846875339'

    # sleep(500)
    thread(100, 3, 'test1.com')
    # for i in range(50):
    #     thread(2,10,'sda.d'+str(i)+'sd1df.scs')



