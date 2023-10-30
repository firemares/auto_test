import function
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
from time import sleep
import auto_threads

def short_risk_fun(ser_name):
    a = 1
    i = 0
    b = 1

    # 输入账号密码
    h=0
    while h==0:
        h=function.login()
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
        # print('寻找服务'+str(i)+'次')
        if b == 1 and i == 20:
            print('寻找服务'+str(i)+'次,没有找到服务存在')
            exit()
        else:
            continue


    # 进行纳管，给服务命名等操作
    function.empoly_short_risk(ser_name)
    # 访问服务管理页面
    h=0
    while h==0:
        h=function.visit_service_manage(ser_name)
    # driver.close()

    # 检查50次是否存在流量
    re = 1
    while re==1 and i<50:
        # 访问审计中心
        function.visit_audit_center()
        # 检查是否存在流量
        re=function.check_audit_center(ser_name)
        function.fresh()

        i=i+1
        # print(i)
        sleep(20)
    if re == 1:
        print("最短流程存在问题")
        function.close()
        exit()
    # else:
    #     print("***********************")
    #     print("最短流程没有问题")
    #     print("***********************")

    # 访问监测服务配置

    # 访问威胁监测
    h = 0
    while h == 0:
        h = function.visit_risk()



    # 检查50次是否存在流量
    re_risk = 1
    j=0
    while re_risk==1 and j<30:
        sleep(15)
        re_risk=function.check_risk(ser_name)
        j=j+1
        # print(j)
        function.fresh()
    if re_risk == 1:
        print("威胁监测存在问题")
        exit()
    # else:
    #     print("*************************")
    #     print("**最短流程+威胁监测没有问题 **")
    #     print("*************************")

    b = 0
    i = 0
    # 匹配该服务是否触发告警
    while b == 0 and i < 50:
        i = i + 1

        sleep(1)
        # 访问威胁告警中
        function.visit_ser_alarm()
        # 匹配该服务名称是否存在告警
        b = function.check_ser_alarm("【"+ser_name+"】")
        function.fresh()

    b = 0
    # 配置sys告警规则
    while b == 0:
        sleep(1)
        # 访问系统告警中心
        function.visit_sys_alarm()
        # 编辑系统告警
        b = function.edit_sys_alarm()
        # print(1)
        function.fresh()

    # 匹配sys三个告警是否可以正常使用
    b = 0
    j = 1
    while b == 0 and j<51:
        print("寻找告警:"+str(j)+"次")
        j = j + 1

        function.fresh()
        sleep(1)
        # 访问系统告警中心
        function.visit_sys_alarm()
        # 提取所有触发的系统告警
        all_name = function.check_sys_alarm()
        if all_name !=[]:
            if len(all_name) < 3:
                b = 0
            else:
                b = 1
        else:
            b=0

    if b == 0:
        print("系统未触发完所有系统告警,告警系统存在问题")
    else:
        print("成功触发所有系统告警:"+str(all_name))

    print("************************************")
    print("**【最短流程+威胁监测+告警中心】没有问题 **")
    print("************************************")

    # 退出登录
    h=0
    while h==0:
        h=function.come_back()



if __name__ == '__main__':
    print("请给纳管服务提前命名")
    ser_name = input(50, 5, 'testtest1.com')
    # 打开网页
    function.open_url(url='https://192.168.10.160')
    short_risk_fun(ser_name)