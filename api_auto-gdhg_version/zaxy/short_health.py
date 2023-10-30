import function
from  selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
from time import sleep

def short_heal_fun(ser_name):
    a = 1
    i = 0


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
            print('进入主页面成功')
    # 访问资产发现
    function.visit_service()
    # 判断是否存在服务----------------节点一
    # 没有服务就循环
    b = 1
    while b == 1 and i < 20:
        # 取返回值
        b = function.check_service(ser_name)
        i = i + 1
        print('寻找服务'+str(i)+'次')
        if b == 1 and i == 20:
            print('没有找到服务存在')
            exit()
        else:
            continue


    # 进行纳管，给服务命名等操作
    function.empoly_short_heal(ser_name)
    # 访问服务管理页面
    ser = 0
    while ser==0:
        ser=function.visit_service_manage(ser_name)
    # driver.close()

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
        print("最短流程存在问题")
        function.close()
        exit()
    # else:
    #     print("最短流程没有问题")

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
        print("寻找状态码规则" + str(j) + "次，没有找到")
    else:
        print("找到状态码规则" +"花费了"+ str(j) + "次")

    # 检查是否触发策略规则--检查20次
    re_heal2 = 0
    k=0
    while re_heal2==0 and k<10:
        sleep(5)
        re_heal2=function.check_heal2(ser_name)
        k=k+1
        function.fresh()
    if re_heal1 == 0 and k == 10:
        print("寻找策略规则" + str(k) + "次，没有找到")
    else:
        # print("找到策略规则" + "花费了" + str(k) + "次")
        print("*************************")
        print("**最短流程+健康检查没有问题**")
        print("*************************")

    # 退出登录
    h=0
    while h==0:
        h=function.come_back()





if __name__ == '__main__':

    print("请给纳管服务提前命名")
    ser_name = input()
    # 打开网页
    function.open_url(url='https://192.168.10.161')
    short_heal_fun(ser_name)