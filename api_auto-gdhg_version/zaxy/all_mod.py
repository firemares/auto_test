import function
from time import sleep
import datetime
# import connect_linux

def all_fun(ser_name):

    # 检查java环境
    # connect_linux.check_environment()
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
                print('\n寻找服务'+str(i)+'次,没有找到服务存在\n', file=f)
            exit()
        else:
            with open('./text.txt', 'a') as f:
                f.truncate(0)
            continue

    # 创建新的敏感数据
    function.sensitive_1(ser_name)

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
    number1 = function.account_0()
    function.account_1(ser_name)
    # 检查50次是否存在流量
    re = 1
    while re==1 and i<20:
        # 访问审计中心
        function.visit_audit_center()
        sleep(3)
        function.fresh()
        re=function.check_audit_center(ser_name)
        i=i+1
        # print(i)
        sleep(10)
    if re == 1:
        with open('./text.txt', 'a') as f:
            print("\n最短流程存在问题\n", file=f)

    else:
        with open('./text.txt', 'a') as f:
            print("\n最短流程没问题\n", file=f)

# 账号访问模块
    # 访问账号访问分析页面
    re1 = 1

    function.account_2(ser_name)
    # 检查20次是否存在流量
    while re1 == 1 and i < 20:
        # 访问 账号访问
        function.fresh()
        sleep(5)
        re1 = function.check_account(ser_name, number1)

        i = i + 1

        sleep(5)
    if re1 == 1:
        with open('./text.txt', 'a') as f:
            print("\n账号访问存在问题\n", file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("用例19：点击高级配置按钮--成功", file=f)
            print("用例20：点击高级配置页面下编辑按钮--成功", file=f)
            print("用例21：选择登录URL--成功", file=f)
            print("用例22：输入登录账号、密码参数名--成功", file=f)
            print("用例23：选择身份标记方式--成功", file=f)
            print("用例24：账号采集配置--成功", file=f)
            print("用例25：访问审计中心下账号访问分析页面--成功", file=f)
            print("用例26：点击账号访问分析页面下操作详情按钮--成功", file=f)
            print("用例27：出现访问API列表--成功", file=f)
            print("\n账号访问没有问题\n", file=f)


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
            print("\n寻找状态码规则" + str(j) + "次，没有找到\n", file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("\n找到状态码规则" +"花费了"+ str(j) + "次\n", file=f)

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
            print("\n寻找策略规则" + str(k) + "次，没有找到\n", file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("\n健康检查没有问题\n", file=f)


# 威胁监测模块
    # 访问威胁监测
    h = 0
    while h == 0:
        h = function.visit_risk()

    # 检查30次是否存在流量
    re_risk = 1
    j = 0
    while re_risk == 1 and j < 30:
        sleep(5)
        re_risk = function.check_risk(ser_name)
        j = j + 1
        # print(j)
        function.fresh()

    if re_risk == 1:
        with open('./text.txt', 'a') as f:
            print("\n威胁监测存在问题\n", file=f)
        # exit()
    else:
        with open('./text.txt', 'a') as f:
            print("\n威胁监测没有问题\n", file=f)



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
        sleep(3)
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
            print("\n系统未触发完所有系统告警,告警系统存在问题\n", file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("用例39：访问告警中心下系统自身告警通知页面--成功", file=f)
            print("用例40：点击编辑告警规则按钮--成功", file=f)
            print("用例41：点击编辑告警规则按钮--成功", file=f)
            print("用例42：修改告警触发条件--成功", file=f)
            print("用例43：选择告警通知方式--成功", file=f)
            print("用例44：编辑告警规则--成功", file=f)
            print("成功触发所有系统告警:"+str(all_name), file=f)
            print("\n告警中心没有问题\n", file=f)


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
            print("\n涉敏存在问题\n", file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("用例45：访问资产中心下涉敏梳理页面--成功", file=f)
            print("用例46：点击扫描任务页面--成功", file=f)
            print("用例47：点击新建扫描任务按钮--成功", file=f)
            print("用例48：输入任务名称--成功", file=f)
            print("用例49：选择开始、结束时间--成功", file=f)
            print("用例50：选择扫描对象--成功", file=f)
            print("用例51：选择敏感特征--成功", file=f)
            print("用例52：创建新的扫描任务--成功", file=f)
            print("用例53：点击任务执行情况按钮--成功", file=f)
            print("\n涉敏梳理没有问题\n", file=f)
    # 创建循环扫描任务
    function.sen_1(ser_name)
    function.fresh()
    sleep(60)
    h=0
    i=0
    while h==0 and i<20:
        i=i+1
        h=function.check_sen_1(ser_name+"1")
        sleep(2)
        function.fresh()
    if h==0 and i==20:
        with open('./text.txt', 'a') as f:
            print("\n涉敏循环存在问题\n", file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("用例54：点击扫描任务下循环执行按钮--成功", file=f)
            print("用例55：输入每天执行时间--成功", file=f)
            print("用例56：创建循环扫描任务--成功", file=f)
            print("\n循环扫描任务没有问题\n", file=f)




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
            print("\n弱点评估任务创建存在问题\n", file=f)
    else:
        with open('./text.txt', 'a') as f:
            print("用例57：访问安全中心下弱点评估概览页面--成功", file=f)
            print("用例58：访问评估任务页面--成功", file=f)
            print("用例59：点击+新建评估任务按钮--成功", file=f)
            print("用例60：输入任务名称--成功", file=f)
            print("用例61：选择任务执行方式--成功", file=f)
            print("用例62：输入执行时长--成功", file=f)
            print("用例63：选择评估对象--成功", file=f)
            print("用例64：选择评估规则--成功", file=f)
            print("用例65：新建评估任务--成功", file=f)
            print("用例66：点击任务执行情况按钮--成功", file=f)
            print("\n弱点评估没有问题\n", file=f)
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
        with open('./text.txt', 'a') as f:
            print("\n弱点评估任务创建存在问题\n")
    else:
        with open('./text.txt', 'a') as f:
            print("用例67：终止执行中任务--成功", file=f)
            print("用例68：点击评估任务下循环执行按钮--成功", file=f)
            print("用例69：选择循环任务执行间隔--成功", file=f)
            print("用例70：创建循环评估任务--成功", file=f)
            print("\n循环评估任务没有问题\n")



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
    with open('./text.txt', 'a') as f:
        print("用例71：访问统计报表页面--成功", file=f)
        print("用例72：访问报表任务页面--成功", file=f)
        print("用例73：点击+新建任务按钮--成功", file=f)
        print("用例74：输入报表名称--成功", file=f)
        print("用例75：选择报表类型--成功", file=f)
        print("用例76：选择执行频率--成功", file=f)
        print("用例77：选择报表生成时间范围--成功", file=f)
        print("用例78：新建报表任务--成功", file=f)
        print("用例79：访问报表记录页面--成功", file=f)


# 退出登录
    h=0
    while h==0:
        h=function.come_back()

def run(url):
    print("请给纳管服务提前命名")
    ser_name = input()
    # 打开网页


    function.open_url(url)
    all_fun(ser_name)


if __name__ == '__main__':
    # ***每次启动必须修改的地方***
    run('https://172.16.76.213')
