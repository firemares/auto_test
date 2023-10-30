import function


function.open_url('https://192.168.10.161')
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
    result = function.check_yzm0()
    # 输入错误继续循环输入验证码
    if result == 1:
        a = 1
    # 跳出循环进入主页面
    elif result == 0:
        a = 0
        # print('进入主页面成功')
function.visit_creat_risk_rule()
function.creat_risk_rule()