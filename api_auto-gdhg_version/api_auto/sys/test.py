import paramiko



#
# class connent_shell:
#     #
#     # def __init__(self):


def remote_connent():
    ip = '192.168.10.161'
    port = 22
    user = 'root'
    password = 'DF*c3000'

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(ip, port, user, password, timeout=10)

    pwd = 'pwd'
    stdin, stdout, stderr = ssh.exec_command(pwd)
    result = stdout.read()
    print(result)
    ssh.close

remote_connent()