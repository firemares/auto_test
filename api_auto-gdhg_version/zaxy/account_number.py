import function
from  selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
from time import sleep


def report_fun(ser_name):
    a = 1
    re = 1
    i = 0
    b=1
    # 输入账号密码
    h=0
    while h==0:
        h=function.login()
    # 判断是否进入主页面
    while a == 1:
        # 取login（）函数的值，判断验证码是否输入正确
        result =function.check_yzm(ser_name)
        # 输入错误继续循环输入验证码
        if result == 1:
            a=1
        # 跳出循环进入主页面
        elif result==0:
            a=0
            # print('进入主页面成功')
    # 访问资产发现
    function.visit_service()
    # 判断是否存在服务----------------节点一
    # 没有服务就循环
    while b == 1 and i < 20:
        # 取返回值
        b = function.check_service(ser_name)
        i = i + 1
        if b == 1 and i == 20:
            print('寻找服务'+str(i)+'次,没有找到服务存在')
            exit()
        else:
            continue

    # 进行纳管，给服务命名等操作
    function.employ(ser_name)
    sleep(2)
    # 配置账号采集
    number1 = function.account_0()
    function.account_1(ser_name)
    function.account_2(ser_name)
    re1 = 1
    # 检查50次是否存在流量
    while re1==1 and i<50:
        # 访问 账号访问
        function.fresh()
        sleep(1)
        re1=function.check_account(ser_name, number1)

        i=i+1

        sleep(10)
    if re1 ==1:
        print("账号访问存在问题")
        exit()
    else:
        print("*****************")
        print("**账号访问没有问题**")
        print("*****************")


if __name__ == '__main__':

    print("请给纳管服务提前命名")
    ser_name = input()
    # 打开网页
    function.open_url(url='https://192.168.10.161')
    report_fun(ser_name)
