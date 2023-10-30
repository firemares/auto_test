import function
from  selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def only_sensitive(ser_name):
    a = 1
    h = 0
    function.open_url(url='https://192.168.10.161')
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

    function.sensitive_1(ser_name)


if __name__ == '__main__':
    ser_name = input()
    only_sensitive(ser_name)
