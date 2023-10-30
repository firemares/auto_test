# coding:utf-8
import threading
from clickhouse_driver import Client
import datetime
from toollib.guid import SnowFlake
import random

import time
from time import sleep

#
def get_id():
    t=int(time.time())


    # for i in range(1000000000):
    t1 = str(t)
    r = str(random.randrange(1000000000, 9999999999))
    re =int(t1 +r)
    # print(re)
    #
    # print(type(re))
    return re


snow = SnowFlake()
# uid = snow.gen_uid()
# uid0=uid - 999999


def in_api_log():
    con1 = Client(
        host='192.168.10.30',
        port=9000,
        user='root',
        password='DF*c3000asi',
        database='api_info',
        send_receive_timeout=5
    )
    num = 7000
    i = 0

    while i == 0:
        i = 0
        totle = []
        for k in range(num):
            # snow = SnowFlake()
            uid = get_id()
            id = uid
            now_time = datetime.datetime.now().replace(microsecond=0)
            ran_all = []
            for j in range(5):
                ran_all.append(
                    random.randrange(1, 9999)
                )

            re_ran = ""
            for x in ran_all:
                if re_ran == "":
                    re_ran = re_ran + str(x)
                else:
                    re_ran = re_ran + "," + str(x)

            ran = random.randrange(1, 9999)
            ran_name = random.randrange(1, 5000)

            sql1 = "select id from api_info.api_audit_log where id = '%s'" % (id)
            sql_insert = "INSERT INTO api_info.api_audit_log (id, dispatch_id, type_list, sensitive_ids, site_id, site_name, api_id, api_name, url, `path`, query_params, `method`, protocol, duration, `authorization`, response_time, package_length, request_length, response_length, client_address, client_port, client_domain_id, client_domain_name, is_office_wlan, remote_address, remote_domain_id, remote_domain_name, remote_port, status_code, login_name, account_system_id, is_staff_account, account_no, request_content_type, request_payload, response_content_type, response_content, request_header, response_header, request_cookie, response_cookie, user_agent, referer, x_forwarded_for, login_flag, login_id, create_time, is_dangerous, category_ids, category_names, level_id, level_name, app_id, app_name, app_realm, is_sensitive, is_keep_record, audit_center_id, audit_center_name, tenant_id, rule_id, parent_rule_id, rule_name, risk_id, risk_level_name, audit_time, audit_type, is_deleted) VALUES"
            # id, re_ran, ran_name, id - ran, now_time, now_time, now_time

            totle = totle + [
                (id, '1683077057875-9e76d8a09f', '[]', str(re_ran), ran_name, 'wwwwwwwwwwwwwwww', id - ran, '',
                 'https://wwwwwwwwwwwwwwww/audit/v1/audit-log/isKeepAndAllApi',
                 '/audit/v1/audit-log/isKeepAndAllApi', '[{\"name\":\"periodType\",\"value\":\"15846875339\"}]',
                 'GET', 'https', 756906157, '', now_time, 0, 0, 118, '', 0, '', '', 0, '192.168.10.161', '', '',
                 443, 200, '', '', '', '', 'application/x-www-form-urlencoded', '',
                 'application/json;charset=UTF-8',
                 '\"{\"sessionTimeoutSecond\":1800,\"code\":200,\"ms\":\"操作成功\",\"data\":[{\"allApiCount\":1,\"isKeepApiCount\":1}],\"successFlag\":true}\"',
                 '[{\"name\":\"Accept\",\"value\":\"application/json, text/plain, */*\"},{\"name\":\"Accept-Encoding\",\"value\":\"gzip, deflate, br\"},{\"name\":\"Accept-Language\",\"value\":\"zh-CN,zh;q=0.9\"},{\"name\":\"Cache-Control\",\"value\":\"no-cache\"},{\"name\":\"Connection\",\"value\":\"keep-alive\"},{\"name\":\"Content-Type\",\"value\":\"application/x-www-form-urlencoded\"},{\"name\":\"Host\",\"value\":\"192.168.10.161\"},{\"name\":\"Pragma\",\"value\":\"no-cache\"},{\"name\":\"Referer\",\"value\":\"https://192.168.10.161/\"},{\"name\":\"Sec-Fetch-Dest\",\"value\":\"empty\"},{\"name\":\"Sec-Fetch-Mode\",\"value\":\"cors\"},{\"name\":\"Sec-Fetch-Site\",\"value\":\"same-origin\"},{\"name\":\"User-Agent\",\"value\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36\"},{\"name\":\"token\",\"value\":\"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ\"},{\"name\":\"x-request-id\",\"value\":\"1949107800.105645\"}]',
                 '[{\"name\":\"Cache-Control\",\"value\":\"no-cache, no-store, max-age=0, must-revalidate\"},{\"name\":\"Connection\",\"value\":\"keep-alive\"},{\"name\":\"Content-Type\",\"value\":\"application/json;charset=UTF-8\"},{\"name\":\"Date\",\"value\":\"Mon, 24 Apr 2023 07:08:24 GMT\"},{\"name\":\"Expires\",\"value\":\"0\"},{\"name\":\"Pragma\",\"value\":\"no-cache\"},{\"name\":\"Server\",\"value\":\"nigx\"},{\"name\":\"Transfer-Encoding\",\"value\":\"chunked\"},{\"name\":\"X-Content-Type-Options\",\"value\":\"nosniff\"},{\"name\":\"X-Frame-Options\",\"value\":\"DENY\"},{\"name\":\"X-XSS-Protection\",\"value\":\"1; mode=block\"}]',
                 '[{\"httpOnly\":false,\"name\":\"JSESSIONID\",\"priority\":\"Medium\",\"secure\":false,\"size\":42,\"value\":\"C81B617FBE6E696F3915B5EBB5CB01C0\"}]',
                 '[]',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                 'https://192.168.10.161/', '', 0, '', now_time, 0, '', '', 0, '', '', '', '192.168.10.161:443', 0,
                 1, '', '', '', 0, '0', '全流量审计', 0, '', now_time, '', 0)]

        con1.execute(sql_insert, totle)
        print("api插入："+str(num)+"成功")
        # re = con.execute(sql1)
        # print(str(re)+"插入成功")
#
def in_risk_log():
    con = Client(
        host='192.168.10.30',
        port=9000,
        user='root',
        password='DF*c3000asi',
        database='api_info',
        # send_receive_timeout=5
    )
    num = 5000
    i = 0

    while i==0:
        # sleep(2)
        all_uid=""
        a = 0
        totle_1 = []
        totle_2 = []

        for l in range(num):

            # snow = SnowFlake()
            uid =snow.gen_uid()
            now_time=datetime.datetime.now().replace(microsecond=0)
            ran = random.randrange(1, 9999)
            ran1 = random.randrange(1, 9999)
            ran_name = random.randrange(1, 5000)
            a = a + 1
            if a % 20 != 0:
                all_uid = all_uid + str(uid) + ","
            else:
                all_uid = all_uid + str(uid)


            sql_in_sample = "INSERT INTO api_info.risk_sample_record(id, dispatch_id, type_list, site_id, site_name, api_id, api_name, url, `path`, query_params, `method`, protocol, duration, `authorization`, response_time, package_length, request_length, response_length, client_address, client_port, client_domain_id, client_domain_name, is_office_wlan, remote_address, remote_domain_id, remote_domain_name, remote_port, status_code, login_name, account_system_id, is_staff_account, account_no, request_content_type, request_payload, response_content_type, response_content, request_header, response_header, request_cookie, response_cookie, user_agent, referer, x_forwarded_for, login_flag, login_id, create_time, is_dangerous, category_ids, category_names, level_id, level_name, app_id, app_name, app_realm, is_keep_record, is_offline, is_file, is_sensitive, audit_center_id, audit_center_name, tenant_id, is_deleted, sensitive_ids)VALUES"
            # (uid,ran_name,uid-ran1,now_time,now_time)
            totle_1 =totle_1+ [(
                uid, '1683181204219-62802bfd94', '', ran_name, '8123', uid-ran1, '', 'https://2122/audit/v1/audit-log/login',
                '/audit/v1/audit-log/login', '[]', 'POST', 'https', 9032, '', now_time, 0, 82, 430, '', 0, '', '', 0,
                '192.168.10.161', '', '', 443, 200, '', '', '', '', 'application/x-www-form-urlencoded',
                '\"{\"username\":\"SecAdmin\",\"password\":\"admin12345\",\"captcha\":\"1493\",\"uuid\":\"02617812\"}\"',
                'application/json;charset=UTF-8',
                '\"{\"sessionTimeoutSecond\":1800,\"code\":200,\"aa\":15768495336,\"msg\":\"操作成功\",\"data\":{\"role\":\"SecAdmin\",\"roleId\":\"2\",\"sessionTimeout\":30,\"userId\":\"2\",\"pwInvalidTime\":1681494743000,\"token\":\"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjMxMzQ3qwUA3pf3ZScAAAA.rZQwP-_IpYLMBv8VosLkGx6mLMXzumQsqkT_rfEg-mIPGxM0ffcNACOsdHATtcvg80dXYznqmNJsiRcooTHlrw\",\"username\":\"SecAdmin\"},\"successFlag\":true}\"',
                '[{\"name\":\"Accept\",\"value\":\"application/json, text/plain, */*\"},{\"name\":\"Accept-Encoding\",\"value\":\"gzip, deflate, br\"},{\"name\":\"Accept-Language\",\"value\":\"zh-CN,zh;q=0.9\"},{\"name\":\"Cache-Control\",\"value\":\"no-cache\"},{\"name\":\"Connection\",\"value\":\"keep-alive\"},{\"name\":\"Content-Type\",\"value\":\"application/x-www-form-urlencoded\"},{\"name\":\"Host\",\"value\":\"192.168.10.161\"},{\"name\":\"Pragma\",\"value\":\"no-cache\"},{\"name\":\"Referer\",\"value\":\"https://192.168.10.161/\"},{\"name\":\"Sec-Fetch-Dest\",\"value\":\"empty\"},{\"name\":\"Sec-Fetch-Mode\",\"value\":\"cors\"},{\"name\":\"Sec-Fetch-Site\",\"value\":\"same-origin\"},{\"name\":\"User-Agent\",\"value\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36\"},{\"name\":\"token\",\"value\":\"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ\"},{\"name\":\"x-request-id\",\"value\":\"1949107800.105645\"}]',
                '[{\"name\":\"Cache-Control\",\"value\":\"no-cache, no-store, max-age=0, must-revalidate\"},{\"name\":\"Connection\",\"value\":\"keep-alive\"},{\"name\":\"Content-Type\",\"value\":\"application/json;charset=UTF-8\"},{\"name\":\"Date\",\"value\":\"Mon, 24 Apr 2023 07:08:24 GMT\"},{\"name\":\"Expires\",\"value\":\"0\"},{\"name\":\"Pragma\",\"value\":\"no-cache\"},{\"name\":\"Server\",\"value\":\"nigx\"},{\"name\":\"Transfer-Encoding\",\"value\":\"chunked\"},{\"name\":\"X-Content-Type-Options\",\"value\":\"nosniff\"},{\"name\":\"X-Frame-Options\",\"value\":\"DENY\"},{\"name\":\"X-XSS-Protection\",\"value\":\"1; mode=block\"}]',
                '[{\"httpOnly\":false,\"name\":\"JSESSIONID\",\"priority\":\"Medium\",\"secure\":false,\"size\":42,\"value\":\"C81B617FBE6E696F3915B5EBB5CB01C0\"}]',
                '[]',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'https://192.168.10.161/', '', 0, '', now_time, 0, '', '', 0, '', '', '', '192.168.10.161:443', 0, 0, 0, 0, '',
                '', '', 0, '')]




            sql_in_check = "INSERT INTO api_info.risk_check_log(id, site_id, site_name, audit_rule_id, audit_rule_name, rule_problem_causes, audit_type, risk_type, check_target, risk_id, risk_level_name, reduced_value, records, is_deleted, create_time, owasp, owasp_name, cwe_no, cwe_no_name, capec_no, capec_no_name, repair_solution, risk_type_name, check_target_name, app_realms, parent_audit_rule_id)VALUES"

            if a % 20 == 0 and a!=0:
            # (uid+ran,ran_name,all_uid,now_time)
                totle_2 = totle_2 + [(uid, ran_name, str(ran_name), 501, '疑似存在机器人访问', '该服务无法正确控制有限资源的分配和维护，从而使参与者能够影响所消耗的资源量，最终导致可用资源耗尽。',
                                      8, 3, 3, 1, '低风险', '40/20', str(all_uid), 0, now_time, 'API4:2019', '资源缺失 & 速率限制', 'CWE-400',
                                      '未加控制的资源消耗（资源穷尽）', 'CAPEC-125', '洪水攻击', '建议对IP单位时间访问次数进行限制（访问频率限制）', '非法访问', '访问账号',
                                      '192.168.10.161:443', 8)]
                all_uid = ""




        con.execute(sql_in_sample,totle_1)
        # sleep(3)
        if num <20:
            pass
        else:
            con.execute(sql_in_check, totle_2)
            # print(1)
        print("risk完成插入："+str(num)+"条")

        #
        # re = con.execute(sql1)
        # print(str(re)+"插入成功")



def thread(threads_num):
    theards=[]
    for i in range(1,threads_num):
        # name="con"+str(i)
        theards.append(
            threading.Thread(target=in_api_log,)
        )
        theards.append(
            threading.Thread(target=in_risk_log,)
        )
    for t in theards:
         t.start()

    for t in theards:
        t.join()

# def thread(threads_num,num):
#     theards=[]
#     for i in range(1,threads_num):
#         # name="con"+str(i)
#         theards.append(
#             threading.Thread(target=in_api_log,args=num)
#         )
#         theards.append(
#             threading.Thread(target=in_risk_log,args=num)
#         )
#     for t in theards:
#          t.start()
#
#     # for t in theards:
#     #     t.join()

#
# def thread():
#
#
#     t1 = threading.Thread(target=in_api_log,)
#     t2 = threading.Thread(target=in_risk_log,)
#     # t3 = threading.Thread(target=in_api_log,)
#     # t4 = threading.Thread(target=in_risk_log,)
#     # t5 = threading.Thread(target=in_api_log, )
#     # t6 = threading.Thread(target=in_risk_log, )
#     # t7 = threading.Thread(target=in_api_log, )
#     # t8 = threading.Thread(target=in_risk_log, )
#
#     t1.start()
#     t2.start()
#     # t3.start()
#     # t4.start()
#     # t5.start()
#     # t6.start()
#     # t7.start()
#     # t8.start()
#     t1.join()
#     t2.join()
#




if __name__ =='__main__':
    # sql1="select id from api_info.api_audit_log where id = '%s'" % (184165110766370816)
    # re =con.execute(sql1)
    # print(re)
    # in_api_log()
    # in_risk_log()
    thread(2)
    # thread()





