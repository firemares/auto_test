import paramiko
import re
from time import sleep





class Ssh:
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ***每次启动必须修改的地方***
    ssh_con.connect('192.168.10.161', 22, 'root', 'DF*c3000')
    def __init__(self):
        # self.ip=0
        # self.cmd=0
        pass



    def connect(self,cmd):
        # ssh_con = paramiko.SSHClient()
        # ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ***每次启动必须修改的地方***
#         ssh_con.connect('192.168.10.212',22,'root', 'DF*c3000')


        # ssh = ssh_con.invoke_shell()


        # print('执行linux命令中~~~~\n')
        # 输入，标准输出，错误输出
        stdin,stdout,stderr=self.ssh_con.exec_command(cmd)
        response_stdout =stdout.read()
        response_stderr = stderr.read()

        if response_stdout!=None:
            return response_stdout
        else:
            return response_stderr


    def check_now_file(self,cmd):
        print('####################')
        print("当前目录是"+str(Ssh().connect(cmd)))
        print('####################\n')

    def check_firewalld(self,cmd):
        result = re.findall('dead', str(Ssh().connect(cmd)), re.S)
        if result == []:
            # print(result)
            print('####################')
            print('防火墙是开启状态')
            print('####################\n')


            result1 = re.findall('3306|30080|8080|6379|15672|5672|8123|7000|443|5005|27017', str(Ssh().connect('firewall-cmd --list-all')), re.S)

            print('检查防火墙必要端口状态~~~\n')
            if len(result1) > 10:
                print('防火墙已开放端口有：'+str(result1))
                return 0
            else:
                print('防火墙已开放端口有：' + str(result1))
                ports = ['3306', '30080', '8080', '6379', '15672', '5672', '8123', '7000', '443','5005','27017']
                for port in ports:
                    i = 0
                    if result1==[]:
                        port_cmd = 'firewall-cmd --add-port=' + port+ '/tcp --permanent'
                        # 开启端口
                        Ssh.ssh_con.exec_command(port_cmd)
                        sleep(1)
                    else:
                        for re_port in result1:
                            if port != re_port and i <len(result1):
                                i = i + 1
                                if i == len(result1):
                                    port_cmd = 'firewall-cmd --add-port=' + port + '/tcp --permanent'
                                    # 开启端口
                                    Ssh.ssh_con.exec_command(port_cmd)
                                    sleep(1)
                                pass
                            elif port == re_port:
                                i = i + 1
                                pass


                # 重启firewall
                Ssh.ssh_con.exec_command('systemctl restart firewalld')
                sleep(10)
                return 1
        else:
            print('####################')
            print('firewall是关闭状态')
            print('####################')
            print("开启firewall中~~~\n")
            Ssh().connect('systemctl start firewalld')
            return 1


    def check_mongodb(self  ,cmd):
        # print(stderr.read().decode())
        # print(response)
        result =re.findall('dead',str(Ssh().connect(cmd)),re.S)
        if result == []:
            print('####################')
            print('配置项1：mongodb是开启状态')
            print('####################\n')
            return 0
        else:
            print('配置项1：mongodb是关闭状态')
            print("开启mongodb中\n")
            Ssh().connect('mongod --config /usr/local/mongodb/bin/mongodb.conf')
            return 1

        # with open('./environment.txt', 'w') as f:
        #     print(response, file=f)
        # print(type(response))
        # ssh_con.close()



    def check_mysql(self,cmd):
        result =re.findall('dead',str(Ssh().connect(cmd)),re.S)
        if result == []:
            print('####################')
            print('配置项2：mysql是开启状态')
            print('####################\n')
            return 0
        else:
            print('配置项2：mysql是关闭状态')
            print("开启mysql中\n")
            Ssh().connect('systemctl start mysqld')
            return 1


    def check_clickhouse(self,cmd):
        result =re.findall('dead',str(Ssh().connect(cmd)),re.S)
        if result == []:
            print('####################')
            print('配置项3：clickhouse是开启状态')
            print('####################\n')
            return 0
        else:
            print('配置项3：clickhouse是关闭状态')
            print("开启clickhouse中\n")
            Ssh().connect('systemctl start clickhouse-server')
            return 1


    def check_rabbitmq(self,cmd):
        result = re.findall('rabbitmq', str(Ssh().connect(cmd)), re.S)
        if len(result)>1:
            print('####################')
            print('配置项4：rabbitmq是开启状态')
            print('####################\n')
            return 0
        else:
            print('配置项4：rabbitmq是关闭状态')
            print("开启rabbitmq中\n")
            Ssh().connect('/usr/sbin/rabbitmqctl -t 10 list_queues')
            return 1


    def check_timon(self,cmd):
        result =re.findall('dead',str(Ssh().connect(cmd)),re.S)
        if result == []:
            print('####################')
            print('配置项5：timon是开启状态')
            print('####################\n')
            return 0
        else:
            print('配置项5：timon是关闭状态')
            print("开启timon中\n")
            Ssh().connect('systemctl start timon')
            return 1



    def check_redis(self,cmd):
        result =re.findall('dead',str(Ssh().connect(cmd)),re.S)
        if result == []:
            print('####################')
            print('配置项6：redis是开启状态')
            print('####################\n')
            return 0
        else:
            print('配置项6：redis是关闭状态')
            print("开启redis中\n")
            Ssh().connect('systemctl start redis')
            return 1



    def check_api_install_package(self, cmd):
         response = str(Ssh().connect(cmd))

         re_result = re.findall('(api|asi).?allinone(.*?)jar',response,re.S)
         # print(re_result)
         if re_result != []:
            print('安装包有：'+str(re_result))
            return str(re_result)
         else:
            # response = Ssh().connect('ls')

            return 0


    def check_java_active(self):
        result_api = re.findall('java(.*)(api|asi).allinone(.*?)jar',str(Ssh().connect('ps -ef |grep api')),re.S)
        result_asi = re.findall('java(.*)(api|asi).allinone(.*?)jar', str(Ssh().connect('ps -ef |grep asi')), re.S)
        if result_api!=[] or result_asi !=[]:
            if result_api!=[]:
                num = 1
            else:
                num = 2
            print('####################')
            print('配置项6：java是运行状态')
            print('####################\n')
            return 0
        else:
            print('配置项6：java是关闭状态')
            print("开启java中\n")
            # 检查java包是否存在
            result_test=ssh.check_api_install_package('cd /home/fortbox/core/asi/base/ && ls')
            re_api = re.findall('api', str(result_test), re.S)
            re_asi = re.findall('asi', str(result_test), re.S)
### 后续需要修改 ###
            if result_test == 0:
                print('当前位置没有java安装包')
                print('请先安装java安装包')
            elif re_api !=[]:
                print('开启api-java安装包中~~~~\n')
                self.ssh_con.exec_command( 'cd /home/fortbox/core/asi/base && nohup java -jar -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005 api-allinone-RELEASE-2.3.1-execute.jar &')

                print('请等待30秒~~~~\n')
                sleep(30)
                return 2

            elif re_asi !=[]:
                print('开启asi-java安装包中~~~~\n')
                self.ssh_con.exec_command(
                    'cd /home/fortbox/core/asi/base && nohup java -jar -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005 asi-allinone-0.0.1-SNAPSHOT.jar &')
                print('请等待30秒~~~~\n')
                sleep(30)
                return 2
            else:
                return 1

            return 1




ssh =Ssh()
# print(ssh.a)

# 检查系统配置环境
def check_environment():

# ssh.check_now_file(cmd='pwd')
    j=1
    k=0
    while j == 1 and k<20:
        print('检查api审计系统启动配置项中~~~~\n')
    # 检查firewall
        r0 = ssh.check_firewalld('systemctl status firewalld')

        # 检查mongod
        r1=ssh.check_mongodb('systemctl status mongod')
        # 检查mysql
        r2=ssh.check_mysql('systemctl status mysqld')
        # 检查clickhouse
        r3=ssh.check_clickhouse('systemctl status clickhouse-server')
        # 检查rabbitmq
        r4=ssh.check_rabbitmq('ps -ef |grep rabbitmq')
        # 检查timon
        r5=ssh.check_timon('systemctl status timon')
        # 检查redis
        r6=ssh.check_redis('systemctl status redis')

        if r0 == 0 and r1 == 0 and r2 == 0 and  r3 == 0 and r4 == 0 and r5==0 and r6==0:
        # 检查java
            i=1
            while i!= 0:
                i = ssh.check_java_active()
                j=0
        else:
            print("存在配置项未启动，正在启动在~，请稍等\n")
            j=1
        k=k+1
    if  j ==1 :
        print("当前脚本无法启动配置项，存在未知问题，请手动修改")
        exit()
    else:
        pass



if __name__ == '__main__':

    check_environment()
# ssh