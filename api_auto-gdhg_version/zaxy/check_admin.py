import function
from time import sleep
import datetime




def check_user(ser_name):
    # 登录Sec
    a = 1
    i = 0
    b = 1
    # 输入账号密码
    h = 0
    while h == 0:
        h = function.login()
    # 判断是否进入主页面
    while a == 1:
        # 取login（）函数的值，判断验证码是否输入正确
        result = function.check_yzm0()
        # 输入错误继续循环输入验证码
        if result == 1:
            a = 1
        # 跳出循环进入主页面
        elif result == 0:
            a = 0
            # print('进入主页面成功')

    # 访问系统配置
    h = 1
    while h == 1:
        function.fresh()
        h = function.visit_sys_edit()



    # 访问用户管理
    h = 0
    while h == 0:
        function.fresh()
        h = function.visit_user_manger()


    # 点击用户管理
    h = 0
    while h == 0:
        h = function.edit_user_manger(ser_name)
        function.fresh()

    # 校验用户是否添加成功
    h = 0
    while h == 0:
        h = function.check_user(ser_name)
        function.fresh()

    # 访问角色管理页面
    h = 0
    while h == 0:
        h = function.visit_role_manger()
        function.fresh()

    # 开启安全操作员可以访问的页面
    h = 0
    while h == 0:
        function.fresh()
        h = function.role_manger_action()

    # 点击退出
    h = 0
    while h == 0:
        # function.fresh()
        h = function.come_back()



    # 登录sys
    a = 1
    i = 0
    b = 1
    # 输入账号密码
    h = 0
    while h == 0:
        h = function.login_user(ser_name)
    # 判断是否进入主页面
    while a == 1:
        # 取login（）函数的值，判断验证码是否输入正确
        result = function.check_yzm0()
        # 输入错误继续循环输入验证码
        if result == 1:
            a = 1
        # 跳出循环进入主页面
        elif result == 0:
            a = 0
            # print('进入主页面成功')

    # 访问主菜单页面
    h = 0
    while h == 0:
        sleep(2)
        h = function.iterate_through()
    if h == 1:
        print('模拟新建账号并授权访问没有问题')


if __name__ == '__main__':
    function.open_url('https://192.168.10.161')
    check_user('admin11')