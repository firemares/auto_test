import function
from  selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
from time import sleep



def check_all_alarm(ser_name):
    # name = input()
    # 输入账号密码
    a = 1
    h = 0
    function.open_url(url='https://192.168.10.30')
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
    j = 1
    # 配置sys告警规则
    while b == 0 and j<10:
        sleep(1)
        # 访问系统告警中心
        function.visit_sys_alarm()
        # 编辑系统告警
        b = function.edit_sys_alarm()
        # print(1)
        function.fresh()
        j=j + 1

    # 匹配sys三个告警是否可以正常使用
    b = 0
    j = 1
    while b == 0 and j<30:
        print("寻找告警:"+str(j)+"次")

        function.fresh()
        sleep(1)
        # 访问系统告警中心
        function.visit_sys_alarm()
        # 提取所有触发的系统告警
        all_name = function.check_sys_alarm()
        j = j + 1
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

if __name__ == "__main__":
    check_all_alarm("testtesttesttest1")