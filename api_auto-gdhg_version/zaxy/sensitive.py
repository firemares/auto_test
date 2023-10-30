import function
from  selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def only_sensitive(ser_name):
    a = 1
    h = 0
    b=1
    i=0
    '172.16.76.135'
    function.open_url(url='https://172.16.76.135')
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

    # 访问资产发现
    function.visit_service()
    # 判断是否存在服务----------------节点一
    # 没有服务就循环
    while b == 1 and i < 20:
        # 取返回值
        b = function.check_service(ser_name)
        i = i + 1
        if b == 1 and i == 20:
            with open('./text.txt', 'a') as f:
                f.truncate(0)
                print('\n寻找服务'+str(i)+'次,没有找到服务存在\n', file=f)
            exit()
        else:
            with open('./text.txt', 'a') as f:
                f.truncate(0)
            continue

    # 纳管模块
    # 进行纳管，给服务命名等操作
    function.empoly_all(ser_name)

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
    else:
        print("111")
    function.sen_1(ser_name)
    function.fresh()
    sleep(90)
    h=0
    i=0
    while h==0 and i<20:
        i=i+1
        h=function.check_sen_1(ser_name+'1')
        sleep(2)
        function.fresh()
    if h==0 and i==20:
        print("涉敏存在问题")

if __name__ == '__main__':
    ser_name = input()
    only_sensitive(ser_name)