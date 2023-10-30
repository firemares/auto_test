import datetime
import time
import requests
from socket import *
import random
# port = 9090
# for j in range(20):
#     port1 = str(port+j)
#     for i in range(3):
#         r1 = requests.get('http://192.168.10.214:'+port1+'/?a=13972589863')
#         r2 = requests.get('http://192.168.10.214:'+port1+'/status/404')
#         r3 = requests.get('http://192.168.10.214:'+port1+'/status/403')
#         r4 = requests.get('http://192.168.10.214:'+port1+'/cache')
#         print(r4.text)
# print('over')
print(time.time())
# # print(datetime.datetime.now().date())
a=''
print(random.randint(0,999))
head = {
    'Content-Type': 'application/json',
    'Token': 'token-ddf-test-453743'
}

data={"username":"SecAdmin","password":"das","captcha":"asda","uuid":"09051299"}
url = 'http://192.168.10.161:30080/acl/v1/login'
response = requests.get(url,head)
print(response.headers)