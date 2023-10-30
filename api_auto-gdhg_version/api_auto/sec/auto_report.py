import function
from  selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
from time import sleep


def report_fun(ser_name):
    a = 1

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
    sleep(2)

    # c=1
    # while c < 7:
    #     # 生成报表
    #     t_name = ser_name +str(c)
    #     function.report_1(t_name)
    #     # 选择报表类型
    #     function.choose_report(c)
    #     c = c + 1
    #     # 生成报表后续
    #     function.report_2()

    # 检查50次是否存在流量

    for a in range(1, 7):
        re = 1
        i = 0
        c_name = ser_name + str(a)
        while re==1 and i<50:
            # 访问 报表任务
            re=function.check_report(c_name)
            function.fresh()
            i=i+1
            sleep(2)

    if re ==1:
        print("生成存在问题")
    else:
        print("*****************")
        print("**生成报表没有问题**")
        print("*****************")


if __name__ == '__main__':

    # print("请给纳管服务提前命名")
    ser_name = "aaa1"
    # 打开网页

    function.open_url(url='https://192.168.10.161')

    report_fun(ser_name)
