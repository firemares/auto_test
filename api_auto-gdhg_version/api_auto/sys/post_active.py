import requests
import time

head = {
    'Content-Type': 'application/json'
}
url = "https://192.168.10.161/collector/v1/data/source/plugin"

null = ""


data = {"url": "https://sadadasd/audit/v1/audit-log/login", "method": "POST",
        "protocol": "http/1.1", "statusCode": 200, "requestTimestamp": time.time(), "responseTimestamp": null,
        "clientAddress": null, "clientPort": null, "localIp": "192.168.10.222", "localPort": "553",
        "remoteAddress": "192.168.10.161", "remotePort": 443,
        "requestHeaders": [{"name": "Accept", "value": "application/json, text/plain, */*"},
                           {"name": "Accept-Encoding", "value": "gzip, deflate, br"},
                           {"name": "Accept-Language", "value": "zh-CN,zh;q=0.9"},
                           {"name": "Cache-Control", "value": "no-cache"},
                           {"name": "Connection", "value": "keep-alive"},
                           {"name": "Content-Type", "value": "application/x-msdownload"},
                           {"name": "Cookie", "value": "JSESSIONID=C81B617FBE6E696F3915B5EBB5CB01C0"},
                           {"name": "Host", "value": "192.168.10.161"}, {"name": "Pragma", "value": "no-cache"},
                           {"name": "Referer", "value": "https://192.168.10.161/"},
                           {"name": "Sec-Fetch-Dest", "value": "empty"},
                           {"name": "Sec-Fetch-Mode", "value": "cors"},
                           {"name": "Sec-Fetch-Site", "value": "same-origin"},
                           {"name": "User-Agent",
                            "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
                           {"name": "token",
                            "value": "eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ"},
                           {"name": "x-request-id", "value": "1949107800.105645"}],
        "responseHeaders": [{"name": "Cache-Control", "value": "no-cache, no-store, max-age=0, must-revalidate"},
                            {"name": "Connection", "value": "keep-alive"},
                            {"name": "Content-Type", "value": "application/json;charset=UTF-8"},
                            {"name": "Date", "value": "Mon, 24 Apr 2023 07:08:24 GMT"},
                            {"name": "Expires", "value": "0"}, {"name": "Pragma", "value": "no-cache"},
                            {"name": "Server", "value": "nigx"}, {"name": "Transfer-Encoding", "value": "chunked"},
                            {"name": "X-Content-Type-Options", "value": "nosniff"},
                            {"name": "X-Frame-Options", "value": "DENY"},
                            {"name": "X-XSS-Protection", "value": "1; mode=block"}],
        "requestPayload": "{\"username\":\"SecAdmin\",\"password\":\"admin12345\",\"captcha\":\"1493\",\"uuid\":\"02617812\"}",
        "responseContent": "{\"sessionTimeoutSecond\":1800,\"code\":200,\"aa\":15768495336,\"msg\":\"操作成功\",\"data\":{\"role\":\"SecAdmin\",\"roleId\":\"2\",\"sessionTimeout\":30,\"userId\":\"2\",\"pwInvalidTime\":1681494743000,\"token\":\"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjMxMzQ3qwUA3pf3ZScAAAA.rZQwP-_IpYLMBv8VosLkGx6mLMXzumQsqkT_rfEg-mIPGxM0ffcNACOsdHATtcvg80dXYznqmNJsiRcooTHlrw\",\"username\":\"SecAdmin\"},\"successFlag\":true}"}

response=requests.post(url, json=data, headers=head,verify=False)

print(response.text)