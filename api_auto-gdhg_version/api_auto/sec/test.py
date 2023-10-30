import re
import datetime
# import function

a='AgentOn=1&IfList=ens192,ens224,lo&IsReply=1&DbtInfo=[192.168.10.220]:9091&CpuThreshold=80&AuditInfo=192.168.10.161:7000..........~d._..AgentOn=1&IfList=ens192,ens224,lo&IsReply=1&DbtInfo=[192.168.10.214]:9092&CpuThreshold=80&AuditInfo=192.168.10.161:7000..........~d.DU.'


# function.open_url(url='https://192.168.10.161')
# function.driver.get('http://192.168.10.220:9091')
re = re.findall('AgentOn=1(.*)?192.168.10.220',a,re.S)
print(re)