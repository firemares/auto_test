# coding:utf-8
import threading
from clickhouse_driver import Client
import datetime
from toollib.guid import SnowFlake
import random

con1 = Client(
    host='192.168.10.30',
    port=9000,
    user='root',
    password='DF*c3000asi',
    database='api_info',
    # send_receive_timeout=5
)

i = 0
totle = []
for k in range(5):
    snow = SnowFlake()
    uid = snow.gen_uid()
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
      # id, re_ran, ran_name, id - ran, now_time, now_time, now_time

    totle = totle + [(str(id), '1683077057875-9e76d8a09f', '[]', str(re_ran), ran_name, 'wwwwwwwwwwwwwwww', id - ran, '',
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


    sql_insert = "INSERT INTO api_info.api_audit_log (id, dispatch_id, type_list, sensitive_ids, site_id, site_name, api_id, api_name, url, `path`, query_params, `method`, protocol, duration, `authorization`, response_time, package_length, request_length, response_length, client_address, client_port, client_domain_id, client_domain_name, is_office_wlan, remote_address, remote_domain_id, remote_domain_name, remote_port, status_code, login_name, account_system_id, is_staff_account, account_no, request_content_type, request_payload, response_content_type, response_content, request_header, response_header, request_cookie, response_cookie, user_agent, referer, x_forwarded_for, login_flag, login_id, create_time, is_dangerous, category_ids, category_names, level_id, level_name, app_id, app_name, app_realm, is_sensitive, is_keep_record, audit_center_id, audit_center_name, tenant_id, rule_id, parent_rule_id, rule_name, risk_id, risk_level_name, audit_time, audit_type, is_deleted) VALUES"

con1.execute(sql_insert, totle)

totle_1 = ('%s', '1683181204219-62802bfd94', '', '%s', '8123', '%s', '', 'https://2122/audit/v1/audit-log/login',
           '/audit/v1/audit-log/login', '[]', 'POST', 'https', 9032, '', '%s', 0, 82, 430, '', 0, '', '', 0,
           '192.168.10.161', '', '', 443, 200, '', '', '', '', 'application/x-www-form-urlencoded',
           '\"{\"username\":\"SecAdmin\",\"password\":\"admin12345\",\"captcha\":\"1493\",\"uuid\":\"02617812\"}\"',
           'application/json;charset=UTF-8',
           '\"{\"sessionTimeoutSecond\":1800,\"code\":200,\"aa\":15768495336,\"msg\":\"操作成功\",\"data\":{\"role\":\"SecAdmin\",\"roleId\":\"2\",\"sessionTimeout\":30,\"userId\":\"2\",\"pwInvalidTime\":1681494743000,\"token\":\"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjMxMzQ3qwUA3pf3ZScAAAA.rZQwP-_IpYLMBv8VosLkGx6mLMXzumQsqkT_rfEg-mIPGxM0ffcNACOsdHATtcvg80dXYznqmNJsiRcooTHlrw\",\"username\":\"SecAdmin\"},\"successFlag\":true}\"',
           '[{\"name\":\"Accept\",\"value\":\"application/json, text/plain, */*\"},{\"name\":\"Accept-Encoding\",\"value\":\"gzip, deflate, br\"},{\"name\":\"Accept-Language\",\"value\":\"zh-CN,zh;q=0.9\"},{\"name\":\"Cache-Control\",\"value\":\"no-cache\"},{\"name\":\"Connection\",\"value\":\"keep-alive\"},{\"name\":\"Content-Type\",\"value\":\"application/x-www-form-urlencoded\"},{\"name\":\"Host\",\"value\":\"192.168.10.161\"},{\"name\":\"Pragma\",\"value\":\"no-cache\"},{\"name\":\"Referer\",\"value\":\"https://192.168.10.161/\"},{\"name\":\"Sec-Fetch-Dest\",\"value\":\"empty\"},{\"name\":\"Sec-Fetch-Mode\",\"value\":\"cors\"},{\"name\":\"Sec-Fetch-Site\",\"value\":\"same-origin\"},{\"name\":\"User-Agent\",\"value\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36\"},{\"name\":\"token\",\"value\":\"eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAKtWKi5NUrJSMoy3ig9OTXZMyc3MU9JRSq0oULIyNLMwMjEwMzQzrQUAFf0WQycAAAA.EQ8LhXoAcZ6GduduzQOgfSQEznbv3HrL6z_htEJKKPVmxAKD9eRpjT6tyKMq4rEK-KMBaY4h0D8VHMQrnLkUcQ\"},{\"name\":\"x-request-id\",\"value\":\"1949107800.105645\"}]',
           '[{\"name\":\"Cache-Control\",\"value\":\"no-cache, no-store, max-age=0, must-revalidate\"},{\"name\":\"Connection\",\"value\":\"keep-alive\"},{\"name\":\"Content-Type\",\"value\":\"application/json;charset=UTF-8\"},{\"name\":\"Date\",\"value\":\"Mon, 24 Apr 2023 07:08:24 GMT\"},{\"name\":\"Expires\",\"value\":\"0\"},{\"name\":\"Pragma\",\"value\":\"no-cache\"},{\"name\":\"Server\",\"value\":\"nigx\"},{\"name\":\"Transfer-Encoding\",\"value\":\"chunked\"},{\"name\":\"X-Content-Type-Options\",\"value\":\"nosniff\"},{\"name\":\"X-Frame-Options\",\"value\":\"DENY\"},{\"name\":\"X-XSS-Protection\",\"value\":\"1; mode=block\"}]',
           '[{\"httpOnly\":false,\"name\":\"JSESSIONID\",\"priority\":\"Medium\",\"secure\":false,\"size\":42,\"value\":\"C81B617FBE6E696F3915B5EBB5CB01C0\"}]',
           '[]',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
           'https://192.168.10.161/', '', 0, '', '%s', 0, '', '', 0, '', '', '', '192.168.10.161:443', 0, 0, 0, 0, '',
           '', '', 0, '')


