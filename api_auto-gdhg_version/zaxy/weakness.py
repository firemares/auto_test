import function
import auto_threads
import time
import datetime
from time import sleep




def short_weakness(ser_name):
    a = 1
    re = 1
    i = 0
    b = 1

    # 输入账号密码
    h = 0
    while h == 0:
        h = function.login()
    # 判断是否进入主页面
    while a == 1:
        # 取login（）函数的值，判断验证码是否输入正确
        result = function.check_yzm(ser_name)
        # 输入错误继续循环输入验证码
        if result == 1:
            a = 1
        # 跳出循环进入主页面
        elif result == 0:
            a = 0
            # print('进入主页面成功')



    # 访问弱点评估
    h = 0
    while h== 0 :
        h = function.visit_weak()

    # 创建弱点评估任务
    h= 0
    while h==0:
        h= function.creat_weak_job(ser_name)
        function.fresh()


    print("请等待十分钟,待评估任务启动,工具将自动运行,当前时间:"+str(datetime.datetime.now()))
    sleep(600)


    # 校验任务执行情况
    h= 0
    i = 0
    while h==0 and i<20:
        h= function.check_weak(ser_name)
        function.fresh()
        i= i + 1
    if i == 20:
        print("弱点评估任务创建存在问题")
    else:
        print("***********************")
        print("弱点评估没有问题")
        print("***********************")

    # 创建弱点循环任务
    function.weakness_1(ser_name)
    function.fresh()
    print("请等待十分钟,待评估任务启动,工具将自动运行,当前时间:" + str(datetime.datetime.now()))
    sleep(600)
    h= 0
    i = 0
    while h==0 and i<20:
        h= function.check_weakness_1(ser_name)
        function.fresh()
        i= i + 1
    if i == 20:
        print("弱点评估任务创建存在问题")
    else:
        print("***********************")
        print("弱点评估没有问题")
        print("***********************")


    # 检查是否出发弱点规则


if __name__ =="__main__":
    function.open_url(url='https://192.168.10.161')
    ser_name = input()
    short_weakness(ser_name)

