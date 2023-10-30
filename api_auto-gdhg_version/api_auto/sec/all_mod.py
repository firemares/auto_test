import function
from  selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
from time import sleep
import datetime
# import connect_linux

def all_fun(ser_name):



    # 登录模块
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
        if b == 1 and i == 20:
            with open('./text.txt', 'a') as f:
                f.truncate(0)
                print('寻找服务'+str(i)+'次,没有找到服务存在', file=f)
            exit()
        else:
            with open('./text.txt', 'a') as f:
                f.truncate(0)
            continue

# 纳管模块
    # 进行纳管，给服务命名等操作
    function.empoly_all(ser_name)



# 服务管理模块
    # 访问服务管理页面
    ser = 0
    while ser==0:
        ser=function.visit_service_manage(ser_name)
    # driver.close()
    sleep(3)
    # 配置账号采集
    function.account_1(ser_name)
    # 检查50次是否存在流量
    re = 1
    while re==1 and i<50:
        # 访问审计中心
        function.visit_audit_center()
        function.fresh()
        re=function.check_audit_center(ser_name)
        i=i+1
        # print(i)
        sleep(20)
    if re == 1:
        with open('./text.txt', 'a') as f:
            print("最短流程存在问题", file=f)
        function.close()
        exit()
    else:
        with open('./text.txt', 'a') as f:
            print("**最短流程没有问题**", file=f)

# 账号访问模块
    # 访问账号访问分析页面
    function.account_2(ser_name)
    # 检查20次是否存在流量
    while re == 1 and i < 20:
        # 访问 账号访问
        function.fresh()
        sleep(2)
        re = function.check_account(ser_name)

        i = i + 1

        sleep(10)
    if re == 1:
        with open('./text.txt', 'a') as f:
            print("账号访问存在问题",file=f)
        exit()
    else:
        with open('./text.txt', 'a') as f:
            print("**账号访问没有问题**", file=f)


# 健康检查模块
    h = 0
    while h==0:
        function.fresh()
        h=function.visit_edit_heal()

    # 编辑健康检查规则
    h = 0
    while h==0:
        function.fresh()
        h=function.edit_heal(ser_name)
    h = 0
    # 访问健康检查
    h = 0
    while h==0:
        function.fresh()
        h=function.visit_heal()

    # 检查是否触发状态码规则--检查20次
    re_heal1 = 0
    j=0
    while re_heal1==0 and j<10:
        sleep(5)
        re_heal1=function.check_heal1(ser_name)
        j=j+1
        function.fresh()
    if re_heal1 == 0 and j==10:
        with open('./text.txt', 'a') as f:
            print("寻找状态码规则" + str(j) + "次，没有找到",file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("找到状态码规则" +"花费了"+ str(j) + "次", file=f)

    # 检查是否触发策略规则--检查20次
    re_heal2 = 0
    k=0
    while re_heal2==0 and k<10:
        sleep(5)
        re_heal2=function.check_heal2(ser_name)
        k=k+1
        function.fresh()
    if re_heal1 == 0 and k == 10:
        with open('./text.txt', 'a') as f:
            print("寻找策略规则" + str(k) + "次，没有找到", file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("健康检查没有问题", file=f)


# 威胁监测模块
    # 访问威胁监测
    h = 0
    while h == 0:
        h = function.visit_risk()

    # 检查50次是否存在流量
    re_risk = 1
    j = 0
    while re_risk == 1 and j < 30:
        sleep(15)
        re_risk = function.check_risk(ser_name)
        j = j + 1
        # print(j)
        function.fresh()

    if re_risk == 1:
        with open('./text.txt', 'a') as f:
            print("威胁监测存在问题", file=f)
        exit()
    else:
        with open('./text.txt', 'a') as f:
            print("**威胁监测没有问题**", file=f)



# 告警中心模块
    b = 0
    i = 0
    # 匹配该服务是否触发告警
    while b == 0 and i < 50:
        i = i + 1
        sleep(1)
        # 访问威胁告警中
        function.visit_ser_alarm()
        # 匹配该服务名称是否存在告警
        b = function.check_ser_alarm(ser_name)
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
    while b == 0 and j<50:
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
        with open('./text.txt', 'a') as f:
            print("系统未触发完所有系统告警,告警系统存在问题", file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("成功触发所有系统告警:"+str(all_name), file=f)
            print("**告警中心没有问题**", file=f)


# 涉敏梳理模块
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
        with open('./text.txt', 'a') as f:
            print("涉敏存在问题", file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("涉敏梳理没有问题", file=f)
            # print("最短流程+健康检查+威胁监测+告警中心+涉敏梳理】没有问题", file=f)


# 弱点评估模块
    # 访问弱点评估
    h = 0
    while h == 0:
        h = function.visit_weak()
        # function.fresh()

    # 创建弱点评估任务
    h = 0
    while h == 0:
        h = function.creat_weak_job(ser_name)
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
        sleep(2)
    if i == 20:
        with open('./text.txt', 'a') as f:
            print("弱点评估任务创建存在问题",file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("弱点评估没有问题", file=f)



# 报表模块
    c=1
    while c < 7:
        # 生成报表
        t_name = ser_name +str(c)
        # 访问统计报表
        function.report_1(t_name)
        # 选择报表类型
        function.choose_report(c)
        c = c + 1
        # 生成报表后续
        function.report_2()
        # 检查50次是否存在流量

    for a in range(1, 7):
        re = 1
        i = 0
        c_name = ser_name + str(a)
        while re == 1 and i < 50:
            # 访问 报表任务
            re = function.check_report(c_name)
            function.fresh()
            i = i + 1
            sleep(2)

    # if re == 1:
    #     with open('./text.txt', 'a') as f:
    #         print("生成存在问题", file=f)
    # else:
    #     with open('./text.txt', 'a') as f:
    #         print("**生成报表没有问题**",file=f)

# 退出登录
    h=0
    while h==0:
        h=function.come_back()


if __name__ == '__main__':

    print("请给纳管服务提前命名")
    ser_name = input()
    # 打开网页

# ***每次启动必须修改的地方***
    function.open_url(url='https://192.168.10.212')
    all_fun(ser_name)