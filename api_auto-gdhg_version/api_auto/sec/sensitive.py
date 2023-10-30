import function
from  selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def only_sensitive(ser_name):
    a = 1
    h = 0
    function.open_url(url='https://192.168.10.212')
    while h == 0:
        h = function.login()
    # 判断是否进入主页面
    while a == 1:
        # 取login（）函数的值，判断验证码是否输入正确
        result = function.check_yzm(ser_name)
        if result == 1:
            # 输入错误继续循环输入验证码
            a = 1
        # 跳出循环进入主页面
        elif result == 0:
            a = 0
            print('进入主页面成功')



    # 访问涉敏梳理
    h=0
    while h==0:
       h = function.visit_sensitive()

    # 创建涉敏扫描任务
    h=0
    while h==0:
        h=function.creat_sensitive(ser_name)
        function.fresh()

    # print("save ok")

    # 检查任务执行情况
    h=0
    i=0
    while h==0 and i<20:
        i=i+1
        h=function.check_sen(ser_name)
        sleep(2)
        function.fresh()
    if h==0 and i==20:
        print("涉敏存在问题")



    # print("The porject is ok")

# function.creat_sensitive("sen1")

if __name__ == '__main__':
    only_sensitive("testtest1")