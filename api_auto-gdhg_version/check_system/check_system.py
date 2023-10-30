import paramiko
import re
from time import sleep
import datetime




class Ssh:
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ***每次启动必须修改的地方***
    ssh_con.connect('192.168.10.31', 22, 'root', 'DF*c3000')
    def __init__(self):
        # self.ip=0
        # self.cmd=0
        pass



    def connect(self,cmd,time):
        # 输入，标准输出，错误输出
        ssh = self.ssh_con.invoke_shell()
        ssh.send(cmd)
        print('请等待'+str(time)+'秒，待命令执行完成')
        sleep(time)
        info = str(ssh.recv(99999999999).decode())
        # print(info)
        ssh.close()
        return info

    def run_maker(self, cmd):
        stdin, stdout, stderr = self.ssh_con.exec_command(cmd)
        response_stdout = stdout.read()
        response_stderr = stderr.read()

        if response_stdout != None:
            return response_stdout
        else:
            return response_stderr

 # 测试写速度
def get_write_performance():
    # 测试写速度
    write_time=[]
    write_speed=[]
    write_content=[]
    for i in range(3):
        write_result=Ssh().connect('time dd of=test if=/dev/zero  bs=2048 count=500000 oflag=direct\n',180)
        time = str(re.findall('\d*.\d+\sMB/秒', write_result, re.S))
        speed = str(re.findall('\d*.\d+\s?秒', write_result, re.S))
        content = str(re.findall('\(\d*.?\d+\s.B\)', write_result, re.S))
        print(time)
        print(speed)
        print(content)

        write_time.append(time)
        write_speed.append(speed)
        write_content.append(content)
        sleep(20)

    print(write_time)
    print(write_speed)
    print(write_content)


# 测试读速度
def get_read_performance():
    # 测试写速度
    read_time=[]
    read_speed=[]
    read_content=[]
    for i in range(3):
        read_result=Ssh().connect('time dd if=test of=/dev/null  bs=2048 count=500000 iflag=direct\n',100)
        time=str(re.findall('\d*.\d+\sMB/秒',read_result,re.S))

        speed=str(re.findall('\d*.\d+\s?秒',read_result,re.S))
        content=str(re.findall('\(\d*.?\d+\s.B\)',read_result,re.S))

        print(time)
        print(speed)
        print(content)

        read_time.append(time)
        read_speed.append(speed)
        read_content.append(content)
        sleep(20)

    print(read_time)
    print(read_speed)
    print(read_content)




# # 测试吞吐速度
def get_qps_performance():

    qps_time=[]
    qps_speed=[]
    qps_content=[]
    for i in range(3):
        # # 测试吞吐速度
        qps_result=Ssh().connect('dd if=/dev/zero of=test bs=64k count=4k oflag=dsync\n',180)

        time=str(re.findall('\d*.\d+\sMB/秒',qps_result,re.S))
        speed=str(re.findall('\d*.\d+\s?秒',qps_result,re.S))
        content=str(re.findall('\(\d*.?\d+\s.B\)',qps_result,re.S))

        print(time)
        print(speed)
        print(content)

        qps_time.append(time)
        qps_speed.append(speed)
        qps_content.append(content)
        sleep(20)

    print(qps_time)
    print(qps_speed)
    print(qps_content)


def memory_size():
    result=str(Ssh().run_maker('free -m'))
    # print(result)
    num=re.findall('\d+',result,re.S)
    memory_size=int(num[0])-int(num[2])-int(num[4])
    print(num[0])
    print('内存实际使用大小为【'+str(memory_size)+'】MB')




get_write_performance()
get_read_performance()
get_qps_performance()
memory_size()
