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
    # 访问资产发现
    function.visit_service()
    # 判断是否存在服务----------------节点一
    # 没有服务就循环
    while b == 1 and i < 20:
        # 取返回值
        b = function.check_service(ser_name)
        i = i + 1
        if b == 1 and i == 20:
            print('寻找服务' + str(i) + '次,没有找到服务存在')
            exit()
        else:
            continue

    # 进行纳管，给服务命名等操作
    function.employ(ser_name)
    # 访问服务管理页面
    function.visit_service_manage(ser_name)
    # driver.close()
    sleep(2)

    # 检查50次是否存在流量
    while re == 1 and i < 50:
        # 访问审计中心
        function.visit_audit_center()
        function.fresh()
        re = function.check_audit_center(ser_name)

        i = i + 1

        sleep(20)
    if re == 1:
        print("最短流程存在问题")

    else:
        # print("在审计记录中寻找" + str(i) + "次，找到了该服务的流量")
        print("*****************")
        print("**最短流程没有问题**")
        print("*****************")




    # 访问弱点评估
    h = 0
    while h== 0 :
        h = function.visit_weak()
        # function.fresh()

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

    print("***********************")
    print("弱点评估没有问题")
    print("***********************")


    # 检查是否出发弱点规则


if __name__ =="__main__":
    function.open_url(url='https://192.168.10.161')
    short_weakness("wwj41")

