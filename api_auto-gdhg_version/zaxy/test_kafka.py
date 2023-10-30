import function
import paramiko
from time import sleep
import re
import auto_threads

api_sys_ip = '192.168.10.212'

def api_pc_outtime(cmd):

    # ssh_con = paramiko.SSHClient()
    # ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # # ***每次启动必须修改的地方***
    # ssh_con.connect(api_sys_ip, 22, 'root', 'DF*c3000')
    # ssh = ssh_con.invoke_shell()
    # ssh.send(cmd)
    # # print("请等待60秒")
    # sleep(5)
    # # info = ssh.recv(99999).decode()
    # ssh.close()
    # # return info
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ***每次启动必须修改的地方***
    ssh_con.connect(api_sys_ip, 22, 'root', 'DF*c3000')
    try:
        ssh_con.exec_command(cmd, timeout=10)
    except Exception as e:
        pass

def api_pc(cmd):
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ***每次启动必须修改的地方***
    ssh_con.connect(api_sys_ip, 22, 'root', 'DF*c3000')

    stdin, stdout, stderr = ssh_con.exec_command(cmd)

    response_stdout = stdout.read()
    response_stderr = stderr.read()
    ssh_con.invoke_shell().close()
    if response_stdout != None:
        return response_stdout
    else:
        return response_stderr



# 监听kafka内容
def listen_kafka():
    api_pc_outtime('cd /usr/local/kafka/bin &&./output_error.sh &\n')
    print("请等待10秒")
    sleep(10)
    text=api_pc("cd /usr/local/kafka/bin && grep -o 'WARN' error.txt |wc -l").decode()
    print(text)
    api_pc('cd /usr/local/kafka/bin && "">error.txt')
    if text ==0:
        print('kafka在告警，请检查kafka配置是否存在问题')
    else:

        api_pc_outtime('cd /usr/local/kafka/bin &&./output_1.sh &\n')
        print('kafka监听已开启')

# 输出监听内容
def output_kafka_listening():
    api_num = api_pc("cd /usr/local/kafka/bin && grep -o '{\"apiId' 1.txt |wc -l").decode()
    # 有数据
    if api_num != 0:
        print("通知数量为：")
        print(api_num)
        api_pc('cd /usr/local/kafka/bin && "">1.txt')
        return 1
    else:
        print(api_num)
        print("未检测到数据进入")
        return 0



# 停止kafka监听服务器的进程
def kill_kafka():
    re_search=api_pc("ps -ef |grep kafka |grep audit").decode()
    re_reuslt = re.findall('\s\d\d\d+\s', str(re_search), re.S)
    for i in re_reuslt:
        api_pc("kill -9 "+i)
    sleep(3)
    re_search_again = api_pc("ps -ef |grep kafka |grep audit").decode()
    print(re_search_again)

# 开启sys用户中的kafka通知配置
def sys_kafka():
    a = 1
    # 输入账号密码
    h=0
    while h==0:
        h=function.login_user()
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

    sleep(10)
    # 开启kafka
    h = 0
    while h == 0:
        function.visit_sys_base()
        h=function.start_sys_kafka()

    function.come_back()


# 开启sec用户中的kafka通知,并开启监听，输出监听结果
def sec_kafka(ser_name):
    a = 1
    i =0
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
    sleep(10)
    # 访问资产发现
    function.visit_service()
    # 没有服务就循环
    b=1
    while b == 1 and i < 20:
        # 取返回值
        b = function.check_service(ser_name)
        i = i + 1
        if b == 1 and i == 20:
            print('\n寻找服务'+str(i)+'次,没有找到服务存在\n',)
        else:
            continue
    # 进行纳管，给服务命名等操作
    function.empoly_all(ser_name)

# 开启kafka功能
    # 访问审计中心
    h=0
    while h==0:
        # 访问审计中心
        function.visit_audit_center()
        # 开启sec用户下访问审计中的kafka通知规则
        h=function.start_sec_kafka()
        sleep(3)
        function.fresh()

    # 连接212服务器，开启kafka监听
    listen_kafka()

    # 检查20次是否存在流量
    re = 1
    i = 0
    while re == 1 and i < 20:
        # 访问审计中心
        function.visit_audit_center()
        sleep(3)
        function.fresh()
        re = function.check_audit_center(ser_name)
        i = i + 1
        sleep(5)
    # 输出监听结果
    # sleep(40)
    output_kafka_listening()
    function.come_back()


def stop_kafka_anywhere():
    a = 1
    # 输入账号密码
    h=0
    while h==0:
        h=function.login_user()
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
    sleep(10)
    # 关闭kafka
    h = 0
    while h == 0:
        function.visit_sys_base()
        h = function.stop_sys_kafka()

    # 关闭采集kafka信息的进程
    kill_kafka()


if __name__ == "__main__":
    print("请给纳管服务提前命名")
    ser_name = input()
    function.open_url("https://192.168.10.161")
    sys_kafka()
    sec_kafka(ser_name)
    stop_kafka_anywhere()
    # listen_kafka()
    # sleep(2)
    # auto_threads.thread(10, 5, 'testtest1.com')
    # sleep(60)
    # output_kafka_listening()
    # kill_kafka()
    #
