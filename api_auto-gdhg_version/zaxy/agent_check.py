import time
import paramiko
import re
import function
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from  time import sleep
from selenium import webdriver


api_sys_ip = '192.168.10.161'


def api_pc(cmd):
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ***每次启动必须修改的地方***
    ssh_con.connect(api_sys_ip, 22, 'root', 'DF*c3000')
    stdin, stdout, stderr = ssh_con.exec_command(cmd)
    response_stdout = stdout.read()
    response_stderr = stderr.read()

    if response_stdout != None:
        return response_stdout
    else:
        return response_stderr


def agent_pc(cmd):
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ***每次启动必须修改的地方***
    ssh_con.connect('192.168.10.214', 22, 'root', 'DF*c3000')
    stdin, stdout, stderr = ssh_con.exec_command(cmd)
    response_stdout = stdout.read()
    response_stderr = stderr.read()

    if response_stdout != None:
        return response_stdout
    else:
        return response_stderr


def api_pc_outtime(cmd):
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_con.connect(api_sys_ip, 22, 'root', 'DF*c3000')
    try:
        ssh_con.exec_command(cmd, timeout=60)
    except Exception as e:
        pass


def agent_pc_outtime(cmd):
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ***每次启动必须修改的地方***
    ssh_con.connect('192.168.10.214', 22, 'root', 'DF*c3000')
    try:
        ssh_con.exec_command(cmd)
    except Exception as e:
        pass
    sleep(2)


def keep_con_agent_220():
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ***每次启动必须修改的地方***
    ssh_con.connect('192.168.10.214', 22, 'root', 'DF*c3000')
    ssh = ssh_con.invoke_shell()
    ssh.send('cd /home/agent && ./install.sh\n')
    sleep(1)
    ssh.send('192.168.10.220:9091\n')
    sleep(1)
    ssh.send('https://'+str(api_sys_ip)+':443\n')
    info = ssh.recv(99999).decode()
    print(info)
    sleep(2)
    ssh.close()


def keep_con_agent_214():
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ***每次启动必须修改的地方***
    ssh_con.connect('192.168.10.214', 22, 'root', 'DF*c3000')
    ssh = ssh_con.invoke_shell()
    ssh.send('cd /home/agent && ./install.sh\n')
    sleep(1)
    ssh.send('192.168.10.214:9092\n')
    sleep(1)
    ssh.send('https://'+str(api_sys_ip)+':443\n')
    info = ssh.recv(99999).decode()
    print(info)
    sleep(2)
    ssh.close()


def send_agent(cmd):
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ***每次启动必须修改的地方***
    ssh_con.connect('192.168.10.214', 22, 'root', 'DF*c3000')
    ssh = ssh_con.invoke_shell()
    ssh.send(cmd + '\n')
    sleep(5)
    # info = ssh.recv(99999).decode()
    # print(info)
    ssh.close()
    # return info


def start_agent():
    # 登录模块
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
    sleep(2)
    h = 1
    while h == 1:
        function.fresh()
        h = function.visit_sys_edit()

    # 删除agent
    h = 1
    while h == 1:
        function.fresh()
        h = function.delete_agent()
        sleep(2)

    sleep(10)
    h = 1
    while h == 1:

        function.fresh()
        h = function.check_sys_edit()


def get_agenton():
    api_pc_outtime('cd /home && tcpdump -i any port 30080 -Avs0 |grep "AgentOn" > tcp.txt')
    sleep(5)
    re_text = api_pc('cat /home/tcp.txt').decode()
    re_audit0 = re.search('AgentOn=1(.*)?192.168.10.220', str(re_text), re.S)
    re_audit1 = re.search('AgentOn=1(.*)?192.168.10.214', str(re_text), re.S)
    if re_audit0 == None:
        print('[192.168.10.220]:9091的AgentOn=0')
        return 0
    else:
        print('220开启')

    if re_audit1 == None:
        print('[192.168.10.214 ]:9092的AgentOn=0')
        return 0
    else:
        print('214开启')
        return 1


def creat_pcap(url):
    try:
        function.driver.set_page_load_timeout(3)
        function.driver.get(url)
        function.driver.maximize_window()
    except Exception as e:
        pass
    try:
        # 点击【/cookies/set?name=value】
        function.driver.find_element(By.XPATH, "/html/body/div/ul/li[15]/a/code").click()
        return 0
    except NoSuchElementException as e:
        return 1


#
# function.open_url(url='https://192.168.10.161')
# start_agent()

# 检查是否存在agent采集的服务
def check_server(ser_name1, ser_name2):
    # 登录模块
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
    # 访问资产发现
    function.visit_service()
    # 判断是否存在服务----------------节点一

    # 没有服务就循环
    while b == 1 and i < 20:
        # 取返回值
        b = function.check_service_agent(ser_name1, ser_name2)
        i = i + 1
        if b == 1 and i == 20:
            print('寻找服务' + str(i) + '次,没有找到服务存在')
        else:
            continue
    if b == 1:
        return 1
    else:
        return 0


# 5.给两个端口打流量
def send_tcp():
    h = 0
    while h == 0:
        re_text = re.findall('go-httpbin', str(agent_pc('ps -ef | grep go-httpbin')), re.S)
        if len(re_text) > 3:
            h = 1
        else:
            send_agent('cd /home/httpserver && nohup ./go-httpbin -host 192.168.10.220 -port 9091 &')
            send_agent('cd /home/httpserver && nohup ./go-httpbin -host 192.168.10.214 -port 9092 &')
            h = 0

    for i in range(0, 5):
        creat_pcap('http://192.168.10.220:9091')
        function.fresh()
        creat_pcap('http://192.168.10.214:9092')
        function.fresh()


def check_tcp():
    sleep(2)
    function.driver.get(url='https://'+str(api_sys_ip))
    re_num = check_server('192.168.10.220:9091', '192.168.10.214:9092')
    return re_num



if __name__=="__main__":
    # # 1.配置网卡（单网卡双ip，双网卡双ip）
    # # 2.产生流量的机器安装两次agent
    # h = 0
    # while h ==0:
    #     re_grep = re.findall('agent',str(agent_pc('ps -ef |grep agent')),re.S)
    #     if len(re_grep)>4:
    #         h =1
    #     else:
    #         agent_pc('cd /home/agent && ./doub_inter_uninstall.sh')
    #         keep_con_agent_220()
    #         keep_con_agent_214()
    #         h=0



    agent_pc('cd /home/agent && ./doub_inter_uninstall.sh')
    keep_con_agent_220()
    keep_con_agent_214()
    # 3.api系统开启agent采集
    # #
    function.open_url(url='https://'+str(api_sys_ip))
    start_agent()
    # # # 4.采集机器tcpdump取agenton的值，取dbinfo的值（tcpdump -i any port 30080 -Avs0）--(tcpdump -i any port 30080 -Avs0 |grep "AgentOn" > tcp.txt)
    h = 0
    while h == 0:
        h=get_agenton()

    # 5.给两个端口打流量
    send_tcp()


    # 6.检查页面是否存在对应服务
    re_value=check_tcp()
    while re_value == 1:
        send_tcp()
        re_value=check_tcp()
    function.close()

    # port = 9090
    # for j in range(20):
    #     port1 = str(port + j)
    #
    #     send_agent('cd /home/httpserver && nohup ./go-httpbin -host 192.168.10.214 -port '+port1+' &')
    #     sleep(1)