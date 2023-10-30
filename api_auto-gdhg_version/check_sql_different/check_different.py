import codecs
import re

def read_flie(file):
    f = codecs.open(filename=file,mode='r',encoding='utf-8')
    line = str(f.readlines())
    a=line.replace('[','')
    b=a.replace(']','')
    c=b.replace('\\n','')
    d=c.replace("`","'")
    # print(d)
    return d


def get_table_name(table_file):
    table_name=re.findall("'CREATE TABLE\s\w?\S+'",str(table_file),re.S)

    return table_name


def get_action(table_file):
    table_content=re.findall(".*?;",table_file,re.S)
    return table_content


def find_different_table_name(file1,file2):
    sql1=get_table_name(read_flie(file1))
    sql2=get_table_name(read_flie(file2))
    tables=[]
    for table2 in sql2:
        for table1 in sql1:
            if table2==table1:
                re=1
                break
            else:
                re=0
                continue
        if re==0:
            tables.append(table2)
            print("V2.4中不存在"+table2+"这张表")
    num = len(tables)
    if num ==0:
        print("######两个版本表数量和名称未变更######")
        with open('clickhouse_different.txt','w') as f:
            f.write("")
        with open('clickhouse_different.txt','a') as f:
            f.write("该文件对应：\n")
            f.write("########################################################\n")
            f.write("#@"+file1+"@与@"+file2+"@版本#\n")
            f.write("########################################################\n")
            f.write("\n######两个版本表数量和名称未变更######\n\n")


def find_different_actions(file1,file2):
# 文件一的操作列表
    actions1=get_action(read_flie(file1))
    actions2=get_action(read_flie(file2))

    for action2 in actions2:
        for action1 in actions1:
            if action1==action2:
                re=1
                break
            else:
                re=0
                continue
        if re==0:
            print('V2.4.0中#####：' + action2 + '#####的操作在V2.3.0中找不到')
            with open('clickhouse_different.txt','a') as f:
                f.write('V2.4.0中:\n'+action2+'\n########的操作在V2.3.0中找不到\n\n')


def main(file1,file2):
    find_different_table_name(file1,file2)
    find_different_actions(file1,file2)


main('V2.3.0-clickhouse.txt','V2.4-clickhouse-init.txt')