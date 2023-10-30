from  selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
from time import sleep
import shortest
import short_risk
import function
import short_health
import all_mod
import threading
import auto_threads

# def jobs(name,num):
#     if num==1:
#         shortest.short_fun(name)
#     elif num == 2:
#         function.open_web()
#         short_risk.short_risk_fun(name)
#     else:
#         return 0
# def theard():
#     theards=[]
#     job="test"
#     for i in range(1,5):
#         name=job+str(i)
#         theards.append(
#             threading.Thread(target=jobs,args=(name,i))
#         )
#     for t in theards:
#          t.start()
#     for t in theards:
#         t.join()
# theard()
#




print("请给纳管服务提前命名")
ser_name = input()
all_name = []
for i in range(10):
    all_name.append(ser_name + str(i))
function.open_url(url='https://192.168.10.161')
shortest.short_fun(all_name[0])
# function.open_web()
# function.open_url(url='https://192.168.10.161')
short_risk.short_risk_fun(all_name[1])
short_health.short_heal_fun(all_name[2])
all_mod.all_fun(all_name[3])


