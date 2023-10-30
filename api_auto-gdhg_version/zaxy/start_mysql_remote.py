import paramiko
import datetime
from time import sleep


# 配置MYsql中用户root,允许远程访问
def edit_mysql_environment(ip):
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ***每次启动必须修改的地方***
    ssh_con.connect(ip, 22, 'root', 'DF*c3000')
    ssh = ssh_con.invoke_shell()
    # 连接mysql
    ssh.send('mysql -u root -p \n')
    sleep(3)
    ssh.send('DF*c3000asi\n')
    sleep(2)
    # 切换数据库
    ssh.send('use mysql;\n')
    sleep(2)
    # 运行远程访问
    ssh.send("update user set host='%' where user='root';\n")
    sleep(2)
    # 查看结果
    ssh.send('select user,host from user;\n')
    sleep(1)
    ssh.send('quit;\n')
    info = ssh.recv(99999).decode()
    print(info)
    sleep(2)
    ssh.close()


# 保存之前的配置文件
def mv_file(ip):
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ***每次启动必须修改的地方***
    ssh_con.connect(ip, 22, 'root', 'DF*c3000')
    stdin, stdout, stderr = ssh_con.exec_command('mv /etc/my.cnf /etc/my_old.cnf')
    response_stdout = stdout.read()
    response_stderr = stderr.read()

    if response_stdout != None:
        print(response_stdout)
        return response_stdout
    else:
        print(response_stderr)
        return response_stderr

# 上传配置好的文件
def upload_file(ip,inpath,outpath):
    trans = paramiko.Transport(ip,22)
    # ***每次启动必须修改的地方***
    trans.connect(username='root', password='DF*c3000')
    sftp = paramiko.SFTPClient.from_transport(trans)
    sftp.put(inpath,outpath)
    sftp.close()

# 重启mysql使配置生效
def restart_mysql(ip):
    ssh_con = paramiko.SSHClient()
    ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_con.connect(ip, 22, 'root', 'DF*c3000')
    stdin, stdout, stderr = ssh_con.exec_command('cat /etc/my.cnf |grep 127.0.0.1')
    response_stdout = stdout.read()
    response_stderr = stderr.read()
    ssh_con.exec_command('systemctl restart mysqld')
    sleep(20)
    if response_stdout != None:
        print(response_stdout)
        return response_stdout
    else:
        print(response_stderr)
        return response_stderr

# 总流程
def set_remote(ip):
    edit_mysql_environment(ip)
    mv_file(ip)
    upload_file(ip,'my.cnf','/etc/my.cnf')
    restart_mysql(ip)


if __name__ == '__main__':

    print('请输入需要mysql需要修改为远程访问的目标机器的ip')
    ip = input()
    set_remote(ip)