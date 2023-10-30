from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import datetime
from selenium.webdriver.common.action_chains import ActionChains
import ddddocr
from time import sleep
import auto_threads

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=option)


def open_web():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    webdriver.Chrome(chrome_options=option)
# driver.get('https://192.168.10.160/')


def close():
    driver.close()

def fresh():
    driver.refresh()

def open_url(url):
    driver.get(url)
    sleep(1)
    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()
    driver.maximize_window()

def login():
    try:
        # 输入账号
        driver.find_element(By.XPATH,
                            "/html/body/div/div[1]/section/div/div/div[3]/form/div[1]/div/span/span/div/input").send_keys(
            "SecAdmin")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[1]").click()
        # 输入密码
        driver.find_element(By.XPATH,
                            "/html/body/div/div[1]/section/div/div/div[3]/form/div[2]/div/div/input").send_keys(
            "admin12345")
    except NoSuchElementException as e:
        return 0
    # 有验证码输入   赋值为1
    else:
        return 1

    sleep(1)

# 校验验证码
def check_yzm(ser_name):
    try:
        # 输入验证码
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[3]/form/div[3]/div/div[1]/input").clear()
        ele_codepic = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[3]/form/div[3]/div/div[2]/img")

        with open('codepic.png', mode='wb') as f:
            f.write(ele_codepic.screenshot_as_png)
        ocr = ddddocr.DdddOcr()
        code_text = ocr.classification(ele_codepic.screenshot_as_png)
        sleep(1)
        # print(code_text)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/section/div/div/div[3]/form/div[3]/div/div[1]/input").send_keys(code_text)

        # 点击登录
        driver.find_element(By.XPATH,"/html/body/div/div[1]/section/div/div/div[3]/form/div[4]/div/div").click()
        sleep(1)

        try:
            result = driver.find_element(By.XPATH, "/html/body/div[3]")
        #没有验证码输入验证会报错   赋值为2(无实际用途，但是需要使用 except函数)
        except NoSuchElementException as e:
            return 2
        # 有验证码输入   赋值为1
        else:
            return 1
    # 进入主页面会报错，忽略该错误，返回 0
    except NoSuchElementException as e:
        auto_threads.thread(10, 5, ser_name)
        return 0

# 校验验证码0
def check_yzm0():
    try:
        # 输入验证码
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[3]/form/div[3]/div/div[1]/input").clear()
        ele_codepic = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[3]/form/div[3]/div/div[2]/img")

        with open('codepic.png', mode='wb') as f:
            f.write(ele_codepic.screenshot_as_png)
        ocr = ddddocr.DdddOcr()
        code_text = ocr.classification(ele_codepic.screenshot_as_png)
        sleep(1)
        # print(code_text)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/section/div/div/div[3]/form/div[3]/div/div[1]/input").send_keys(code_text)

        # 点击登录
        driver.find_element(By.XPATH,"/html/body/div/div[1]/section/div/div/div[3]/form/div[4]/div/div").click()
        sleep(1)

        try:
            result = driver.find_element(By.XPATH, "/html/body/div[3]")
        #没有验证码输入验证会报错   赋值为2(无实际用途，但是需要使用 except函数)
        except NoSuchElementException as e:
            return 2
        # 有验证码输入   赋值为1
        else:
            return 1
    # 进入主页面会报错，忽略该错误，返回 0
    except NoSuchElementException as e:

        return 0

def visit_sys_edit():
    try:
        # 访问系统配置
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/span[7]").click()
        sleep(3)

        return 0
    # 报错
    except NoSuchElementException as e:
        return 1

# 开启agent状态
def check_sys_edit():
    # port1='9091'
    try:
        # 勾选【方案二：在服务宿主机上部署Agent】
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/label[2]/span[1]/span").click()
        sleep(2)
        name1 = driver.find_element(By.XPATH,
                                    "/html/body/div/div[1]/section/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/span").text
        name2 = driver.find_element(By.XPATH,
                                    "/html/body/div/div[1]/section/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/span").text
        for i in range(1,3):
            # 点击配置按钮
            driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[2]/div/div["+str(i)+"]/div[1]/div/div/button[1]").click()

            # 点击添加端口
            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div[3]/div[1]/div/button").click()

            if str(i) == '1':
                if name1 == '192.168.10.220':
            # 输入端口号
                    driver.find_element(By.XPATH,
                                "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div[3]/div[2]/div/form/div/div/p/div/div/div/div/input").send_keys('9091')
                else:
                    driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div[3]/div[2]/div/form/div/div/p/div/div/div/div/input").send_keys(
                        '9092')
            elif str(i) == '2':
                if name2 == '192.168.10.220':
                    # 输入端口号
                    driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div[3]/div[2]/div/form/div/div/p/div/div/div/div/input").send_keys(
                        '9091')
                else:
                    driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div[3]/div[2]/div/form/div/div/p/div/div/div/div/input").send_keys(
                        '9092')
            else:
                return 0
            sleep(1)
            # 点击更新配置
            driver.find_element(By.XPATH,
                                "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[4]/div/div/div[3]/div/button[1]").click()
            sleep(2)
            # 开启agent状态
            driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[2]/div/div["+str(i)+"]/div[2]/form/div[2]/div/div/span").click()

            sleep(1)
            # 点击确认
            for j in range(1,5):
                try:
                    # '/html/body/div[3]/div/div[3]/button[2]/span'
                    driver.find_element(By.XPATH,"/html/body/div["+str(j)+"]/div/div[3]/button[2]").click()
                    break
                except NoSuchElementException as e:
                    pass
        return 0
    # 报错
    except NoSuchElementException as e:
        return 1

def delete_agent():
    try:
        sleep(2)
        # 勾选【方案二：在服务宿主机上部署Agent】
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/label[2]/span[1]/span").click()
        # 点击删除
        num = 0
        # sleep(1)
        try:
            for i in range(1, 3):
                num = num +1
                # 点击删除
                try:
                    sleep(1)
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[2]/div/div["+str(i)+"]/div[1]/div/div/button[2]").click()

                except NoSuchElementException as e:
                    driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[2]/div/div/div[1]/div/div/button[2]").click()
                sleep(1)
                # 点击确认
                for j in range(1, 5):
                    try:
                        driver.find_element(By.XPATH, "/html/body/div[" + str(j) + "]/div/div[3]/button[2]/span").click()

                        break
                    except NoSuchElementException as e:
                        continue
            return 0
        except NoSuchElementException as e:
            if num>2:
                return 0
            else:
                return 1
    except NoSuchElementException as e:
        return 1

# 访问资产发现
def visit_service():
    try:
        # 访问资产中心
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/span[2]").click()
        sleep(1)
        # 点击开启/关闭 按钮
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div[1]/div/div/button/i").click()
        # 点击开启后的【保存】
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/button[1]").click()
    # 报错
    except NoSuchElementException as e:
        # 点击取消
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button[1]/span").click()
        return 0
    # 正常
    else:
        # driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/button[1]").click()
        return 1

# 判断是否存在服务----------------节点一
def check_service(ser_name):
    driver.refresh()

    try:
        # 打流--50条
        auto_threads.thread(10, 5, ser_name)
        sleep(5)
        # '/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[2]/td[3]/div/a/span'
        name =driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/a/span").text
        # 判断是否存在服务
        if ser_name == name:
            return 0
        else:
            return 1
    # 没有服务
    except NoSuchElementException as e:
        return 1

def check_service_agent(ser_name1,ser_name2):
    driver.refresh()
    try:
        # 打流--50条
        # auto_threads.thread(10, 5, ser_name)
        sleep(5)
        # '/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[2]/td[3]/div/a/span'
        name1 =driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/a/span").text
        name2 = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[2]/td[3]/div/a/span").text
        # 判断是否存在服务
        if ser_name1 == name1 or ser_name1 == name2:
            print("存在"+ser_name1)
            if ser_name2 == name1 or ser_name2 == name2:
                print("存在" + ser_name2)
                print("agent没有问题")
                return 0
            else:
                return 1
        else:
            return 1
    # 没有服务
    except NoSuchElementException as e:
        return 1


# 【最短流程】进行纳管，给服务命名等操作
def employ(ser_name):
    try:
        # 点击纳管
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/button[1]/i").click()
        # 输入服务名称

        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[2]/form/div[1]/div/div/div/input").send_keys(ser_name)
        # 点击【服务名称】###########
        # 循环点击存在的名称，#############每个名称只能保存一次否则就会出错
        for a in range(1,20):
            b=str(a)
            try:

                path = "/html/body/div["+b+"]/div[1]/div[1]/ul/li[1]/span"
                # print(path)
                driver.find_element(By.XPATH,path).click()
            except NoSuchElementException as c:
                continue
            # 纳管没问题
            else:
                # print('纳管成功')

                # 取消勾选威胁
                # sleep(5)
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[2]/form/div[8]/div/label[1]/span[1]/span").click()
                # 取消勾选健康
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[2]/form/div[8]/div/label[2]/span[1]/span").click()
                # 点击保存
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[3]/div/button[1]").click()
                break
    # 纳管有问题
    except NoSuchElementException as e:
        print('纳管有问题')
        return 0
    # 纳管没问题
    else:
        # print('纳管没问题')
        return 1

# 【最短流程+威胁监测】进行纳管，给服务命名等操作
def empoly_short_risk(ser_name):
    try:
        # 点击纳管
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/button[1]/i").click()
        # 输入服务名称

        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[2]/form/div[1]/div/div/div/input").send_keys(ser_name)
        # 点击【服务名称】###########
        # 循环点击存在的名称，#############每个名称只能保存一次否则就会出错
        sleep(2)
        for a in range(1,20):
            b=str(a)
            try:

                path = "/html/body/div["+b+"]/div[1]/div[1]/ul/li[1]/span"
                # print(path)
                driver.find_element(By.XPATH,path).click()
            except NoSuchElementException as c:
                continue
            # 纳管没问题
            else:
                # print('点击成功')
                # 取消勾选健康
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[2]/form/div[8]/div/label[2]/span[1]/span").click()
                # 点击保存
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[3]/div/button[1]").click()
                break
    # 纳管有问题
    except NoSuchElementException as e:
        print('纳管有问题')
        return 0
    # 纳管没问题
    else:
        # print('纳管没问题')
        return 1

# 【最短流程+健康检查】进行纳管，给服务命名等操作
def empoly_short_heal(ser_name):
    try:
        # 点击纳管
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/button[1]/i").click()
        # 输入服务名称

        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[2]/form/div[1]/div/div/div/input").send_keys(ser_name)
        # 点击【服务名称】###########
        # 循环点击存在的名称，#############每个名称只能保存一次否则就会出错
        sleep(2)
        for a in range(1,10):
            b=str(a)
            try:
                path = "/html/body/div["+b+"]/div[1]/div[1]/ul/li[1]/span"
                # print(path)
                driver.find_element(By.XPATH,path).click()
            except NoSuchElementException as c:
                continue
            # 纳管没问题
            else:
                # print('点击成功')
                # 取消勾选威胁
                # sleep(5)
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[2]/form/div[8]/div/label[1]/span[1]/span").click()
                # # 点击保存
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[3]/div/button[1]").click()
                break
    # 纳管有问题
    except NoSuchElementException as e:
        print('纳管有问题')
        return 0
    # 纳管没问题
    else:
        # print('纳管没问题')
        return 1


# 【最短流程+健康检查+威胁监测】进行纳管，给服务命名等操作
def empoly_all(ser_name):
    try:
        # 点击纳管
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/button[1]/i").click()
        # 输入服务名称

        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[2]/form/div[1]/div/div/div/input").send_keys(ser_name)
        # 点击【服务名称】###########
        # 循环点击存在的名称，#############每个名称只能保存一次否则就会出错
        sleep(5)
        for a in range(1,10):
            b=str(a)
            try:
                path = "/html/body/div["+b+"]/div[1]/div[1]/ul/li[1]/span"
                # print(path)
                driver.find_element(By.XPATH,path).click()
            except NoSuchElementException as c:
                continue
            # 纳管没问题
            else:
                # # 点击保存
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[4]/div/div/div[3]/div/button[1]").click()
                break
    # 纳管有问题
    except NoSuchElementException as e:
        print('纳管有问题')
        return 0
    # 纳管没问题
    else:
        # print('纳管没问题')
        return 1



# 【最短流程】的访问服务管理页面的操作
def visit_service_manage(ser_name):
    try:
        # 点击资产台账页面
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/aside/ul/li[2]/div/i").click()
        # 点击服务管理页面(2.3.0和2.3.1xpath不一样)
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/aside/ul/li[2]/ul/li[1]").click()
        # 查询是否存在命名的服务
        # 输入名称
        sleep(1)
        driver.find_element(By.XPATH,
                            "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/input").send_keys(
            ser_name)
        # 点击查询
        driver.find_element(By.XPATH,
                            "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[3]/div[1]/div[3]/button").click()
        name = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[3]/div[2]/div[3]/table/tbody/tr/td[2]/div").text
    except NoSuchElementException as e:
        print("未找到服务")
        return 0
    else:
        # print('服务管理页面中纳管的服务可以被找到')
        return 1




# 点击审计中心
def visit_audit_center():
    # 点击审计中心
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/span[4]").click()
    except NoSuchElementException as e:
        print("未找到服务")
        return 1

# 检查审计中心是否存在流量
def check_audit_center(ser_name):
    try:
        # 打流--50条
        auto_threads.thread(10, 5, ser_name)
        # 检查是否存在流量
        for i in range(1,13):
            get_name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[4]/div[3]/table/tbody/tr["+str(i)+"]/td[4]/div/span").text
            # 找到了
            if ser_name == get_name :
                with open('./text.txt', 'a') as f:
                    print('纳管的服务为:' + get_name, file=f)
                # print('最短流程没有问题')
                re= 0
                break
            # 没找到
            else:
                # 检查是否存在所属服务
                re = 1
                # print("最短流程没有找到一纳管服务的流量，请确认流量是否进入/或系统是否存在问题")
                continue
    # 没找到
    except NoSuchElementException as e:
        print("最短流程没有流量，请确认流量是否进入")
        return 1
    return re

# 访问威胁资产视角
def visit_risk():
    # 点击安全中心
    try:
        sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/span[3]").click()
        sleep(5)
        # 点击威胁资产视角
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/aside/ul/li[1]/ul/li[2]").click()
    except NoSuchElementException as e:
        return 0
    else:
        return 1

# 配置健康检查策略--响应时长>1ms触发
def visit_edit_heal():
    try:
        sleep(2)
        # 点击安全中心
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/span[3]").click()
        sleep(2)
        # 点击健康检查
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/aside/ul/li[3]/div").click()
        sleep(1)
        # 点击检查服务配置
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/aside/ul/li[3]/ul/li[3]").click()
        sleep(2)

        # 点击查询二次
        # driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div[2]/div/div/span").click()

    except NoSuchElementException as e:
        print("没有该服务名称")
        return 0

def edit_heal(ser_name):
    try:
        # 查询该服务
        #   输入名称
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div/input").send_keys(
            ser_name)
        sleep(2)
        # 点击查询
        driver.find_element(By.XPATH,
                            "/html/body/div/div[1]/section/div/div/div[2]/div/div/div[2]/div/div/span").click()
        sleep(5)
        # 点击编辑按钮
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[3]/div[3]/table/tbody/tr/td[5]/div/button/i").click()
        sleep(5)
        # 循环点击[+]号,添加规则

        for a in range(1,10):
            try:
                b=str(a)
                path = "/html/body/div["+b+"]/div/div[2]/form[2]/div/div/div/div[2]/table/thead/tr/th[5]/div/button"
                # print(path)
                driver.find_element(By.XPATH,path).click()
            except NoSuchElementException as e:
                continue
        sleep(1)
        # 点击下拉
        for a in range(1,10):
            try:
                b=str(a)
                path = "/html/body/div["+b+"]/div/div[2]/form[2]/div/div/div/div[3]/table/tbody/tr/td[1]/div/div/div/div/div/span/span/i"
                # print(path)
                driver.find_element(By.XPATH,path).click()
            except NoSuchElementException as e:
                continue

        sleep(1)
        # 选中响应时长
        for a in range(1, 10):
            try:
                b = str(a)
                path = "/html/body/div["+b+"]/div[1]/div[1]/ul/li[1]/span[1]"
                # print(path)
                driver.find_element(By.XPATH, path).click()
            except NoSuchElementException as e:
                continue

        sleep(1)
        # 输入判定值
        for a in range(1, 10):
            try:
                b = str(a)
                path = "/html/body/div["+b+"]/div/div[2]/form[2]/div/div/div/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/div/input"
                # print(path)
                driver.find_element(By.XPATH, path).send_keys(
            "1")
            except NoSuchElementException as e:
                continue


        # 输入策略含义
        for a in range(1, 10):
            try:
                b = str(a)
                path = "/html/body/div["+b+"]/div/div[2]/form[2]/div/div/div/div[3]/table/tbody/tr/td[4]/div/div/div/div/input"
                # print(path)
                driver.find_element(By.XPATH, path).send_keys("自动测试专属规则")
            except NoSuchElementException as e:
                continue
        sleep(1)
        # 点击提交

        for a in range(1, 10):
            try:
                b = str(a)
                path = "/html/body/div["+b+"]/div/div[3]/div/button[1]"
                # print(path)
                driver.find_element(By.XPATH, path).click()
            except NoSuchElementException as e:
                continue

        # print("策略配置中完成")
    except NoSuchElementException as e:
        print("没有该服务名称")
        return 0
    else:
        return 1



# 访问健康检查
def visit_heal():
    try:
    # 点击安全中心
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/span[3]").click()
        sleep(5)
        # 点击健康检查
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/aside/ul/li[3]/div").click()
        sleep(1)
        # 点击健康问题视角
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/aside/ul/li[3]/ul/li[1]").click()
        sleep(3)
    # 没找到
    except NoSuchElementException as e:
        return 0
    else:
        return 1

#查看健康检查是否触发状态码规则
def check_heal1(ser_name):
    try:
        #获取该页面的状态码名称
        name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr/td[2]/div").text
    # 没找到
    except NoSuchElementException as e:
        print("流量没有触发状态码规则，请确认流量是否进入/流量是否存在4xx或5xx状态码")
        auto_threads.thread(10, 5, ser_name)
        return 0
    else:
        with open('./text.txt', 'a') as f:
            print("最近一次触发的健康状态码规则是:" + name, file=f)
        # print("*********************************")
        return 1

#查看健康检查是否触发策略规则
def check_heal2(ser_name):
    try:
        # 点击策略
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[3]/div[1]/div/div/div/div[3]").click()
        sleep(5)
        # 获取该页面触发策略名称
        name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[3]/table/tbody/tr/td[2]/div/span/span").text
    # 没找到
    except NoSuchElementException as e:
        auto_threads.thread(10, 5, ser_name)
        print("流量没有触发健康策略规则，请确认流量是否进入流量/是否配置健康检查策略")
        return 0
    else:
        with open('./text.txt', 'a') as f:
            print("最近一次触发的健康策略规则是:"+name, file=f)
        # print("###########################")
        return 1


#访问威胁资产视角查看纳管服务是否触发威胁
def check_risk(ser_name):
    try:
        #获取该页面的服务名称
        get_name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[5]/div[3]/table/tbody/tr[1]/td[1]/div/span/span/span").text
        # 没找到
        if ser_name == get_name:
            # print('纳管的服务为:' + get_name)
            # print("*********************************")
            # print('威胁没有问题')
            # print("*********************************")
            re = 0
        # 找到了
        else:  # 检查是否存在所属服务
            re = 1
            auto_threads.thread(10, 5, ser_name)
            print("威胁监测没有找到该服务触发规则的记录，请确认流量是否进入")
    # 没找到
    except NoSuchElementException as e:
        print("威胁监测流量，请确认流量是否进入")
        return 1
    return re

# 退出登录
def come_back():
    try:
        # 点击退出
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[3]/div[2]").click()

    # 没找到
    except NoSuchElementException as e:
        return 0
    else:
        # 点击确定
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span").click()
        return 1
# 访问威胁告警中心
def visit_ser_alarm():
    try:
        # 点击告警中心
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/span[5]").click()
    # 没找到
    except NoSuchElementException as e:
        return 0
    else:
        return 1

# 匹配该服务是否触发威胁告警中心的告警
def check_ser_alarm(ser_name):
    for a in range(1,13):
        try:
            #获取告警通知的服务名称
            get_name = driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody/tr["+str(a)+"]/td[5]/div").text
            # "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[5]/div"
            # "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tbody/tr[1]/td[5]/div"
            # print(get_name)
            # 告警通知没找到
            if ser_name == get_name:
                print(get_name+"成功触发告警")
                # print('威胁没有问题')
                break
                return 1
            else:
                continue
                # print("告警通知没有找到该服务触发规则的记录，请确认流量是否进入")
        # 没找到
        except NoSuchElementException as e:
            # print("没有告警通知流量，请确认流量是否进入")
            continue
            return 0

def edit_sys_alarm():
    sleep(2)
    try:
        # 点击【告警规则】
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[5]/button").click()
        sleep(5)
    # 编辑【告警规则】
    #     配置规则
        for a in range(1,4):
            for j in range(1,10):
                # 点击编辑

                try:
                    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div["+str(j)+"]/div/div[2]/div[2]/div[3]/table/tbody/tr["+str(a)+"]/td[5]/div/button[1]").click()
                    break
                except NoSuchElementException as e:
                    continue
            # 清除触发条件
            for i in range(1,11):
                try:
                    driver.find_element(By.XPATH, "/html/body/div["+str(i)+"]/div/div[2]/form/div[3]/div/div[2]/div/div/div/input").clear()
                    break
                except NoSuchElementException as e:
                    continue

            # 输入触发条件
            for j in range(1,11):
                try:
                    driver.find_element(By.XPATH, "/html/body/div["+str(j)+"]/div/div[2]/form/div[3]/div/div[2]/div/div/div/input").send_keys("1")
                    break
                except NoSuchElementException as e:
                    continue

            # 选中通知方式为 SYSlog
            for k in range(1,11):
                try:
                    driver.find_element(By.XPATH, "/html/body/div["+str(k)+"]/div/div[2]/form/div[5]/div/div[1]/label[1]/span[1]/span").click()
                    break
                except NoSuchElementException as e:
                    continue

            # 点击保存
            for l in range(1,11):
                try:
                    driver.find_element(By.XPATH, "/html/body/div["+str(l)+"]/div/div[3]/span/button[1]").click()
                    break
                except NoSuchElementException as e:
                    continue

    # 配置失败
    except NoSuchElementException as e:
        return 0
    else:
        return 1



# 访问系统告警中心
def visit_sys_alarm():
    try:
        # 点击【告警中心】
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/span[5]").click()
        # 点击【系统自身告警】
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]").click()
        # "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]"
    # 访问失败
    except NoSuchElementException as e:
        return 0
    else:
        return 1

# 匹配触发的系统告警有哪些
def check_sys_alarm():
    get_name = []
    x=0
    sleep(10)
    try:
        for a in range(1, 13):
           try:
               # 获取sys通知的服务名称
               name = driver.find_element(By.XPATH,
                                          "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[" + str(
                                              a) + "]/td[2]/div").text
               # "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div"
               # "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[2]/td[2]"
               # print(get_name)
               # 找到告警信息内容
               if get_name != []:
                   # 循环取get_name中的元素和服务名称做比较
                   for e_name in get_name:
                       if name != e_name:
                           x = 1
                           continue
                       else:
                           x = 0
                           break
               else:
                   # 列表为空，直接将元素放入列表中
                   get_name.append(name)
               if x == 1:
                   # 列表不为空，判断列表中所有数据和新取出的数据是否相等
                   get_name.append(name)
               # print("系统已触发系统告警" + str(get_name))
           except NoSuchElementException as e:
               continue
        # 没找到
    except NoSuchElementException as e:
        print("没有告警通知流量，请确认流量是否进入")
        return 0
    else:
        return get_name

# 访问涉敏梳理
def visit_sensitive():
    try:
        sleep(2)
        # 点击【资产中心】
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/span[2]").click()


        # "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]"
    # 访问失败
    except NoSuchElementException as e:
        return 0
    else:
        return 1

# 创建涉敏扫描任务
def creat_sensitive(ser_name):
    try:
        sleep(2)
        # 点击【涉敏梳理】
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/aside/ul/li[3]").click()
        sleep(1)
        # 点击涉敏的【扫描任务】
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]").click()
        # "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]"
        # "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]"
        # 点击【新建扫描任务】
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/button[2]").click()
        sleep(1)

        for i in range(1,11):
            try:
            # 输入任务名称
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div["+str(i)+"]/div/div[2]/form/div[1]/div/div/input").send_keys(ser_name)
                break
            except NoSuchElementException as e:
                continue

            # 循环点击开始时间
        for i in range(1,11):
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div["+str(i)+"]/div/div[2]/form/div[2]/div/div[2]/div/div[1]/div/div/div/input").click()
                break
            except NoSuchElementException as e:
                continue
        # 循环点击【此刻】
        for i in range(1,11):
            try:
                # 点击【此刻】
                driver.find_element(By.XPATH, "/html/body/div["+str(i)+"]/div[2]/button[1]/span").click()
                break
            except NoSuchElementException as e:
                continue
         # 输入结束时间
        for i in range(1,11):
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[" + str(i) + "]/div/div[2]/form/div[2]/div/div[2]/div/div[2]/div/input").send_keys(str(datetime.datetime.now().date()) + " 23:59:00")

                break
            except NoSuchElementException as e:
                continue
        # 点击【敏感特征】
        for i in range(1,11):
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[" + str(i) + "]/div/div[2]/form/div[8]/label").click()
                break
            except NoSuchElementException as e:
                continue

        # 输入扫描对象
        for i in range(1,11):
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div["+str(i)+"]/div/div[2]/form/div[3]/div/div/div[1]/input").send_keys(ser_name)
                break
            except NoSuchElementException as e:
                continue

        # 点击【敏感名称】
        driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul").click()

        # 点击【敏感特征】
        for i in range(1,11):
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div["+str(i)+"]/div/div[2]/form/div[8]/label").click()
                break
            except NoSuchElementException as e:
                continue

        # 输入样本采集数--5
        for i in range(1,11):
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div["+str(i)+"]/div/div[2]/form/div[6]/div/div/div/input").clear()
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div["+str(i)+"]/div/div[2]/form/div[6]/div/div/div/input").send_keys("5")
                break
            except NoSuchElementException as e:
                continue

        # 勾选所有特征
        for i in range(1,11):
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div["+str(i)+"]/div/div[2]/form/div[8]/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span").click()
                break
            except NoSuchElementException as e:
                continue

        # 点击保存
        for i in range(1,11):
            try:

                driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div["+str(i)+"]/div/div[3]/span/button[1]").click()
                # driver.find_element(By.XPATH,
                #                     "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[" + str(
                #                         i) + "]/div/div[3]/span/button[1]").click()
                sleep(5)
                break
            except NoSuchElementException as e:
                continue
        return 1
    # 访问失败
    except NoSuchElementException as e:
        return 0

# 检查任务执行情况
def check_sen(ser_name):
    try:
        sleep(2)
        # 点击涉敏的【扫描任务】
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]").click()
        # 获取任务名称
        get_name = driver.find_element(By.XPATH, '/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr/td[3]/div/span').text
        # 获取任务状态
        result = driver.find_element(By.XPATH,  '/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/span').text
        # 判断任务名称和状态
        if ser_name == get_name and result == "已完成":
            return 1
        else:
            return 0
    # 访问失败
    except NoSuchElementException as e:
        return 0


# 访问弱点评估
def visit_weak():
    try:
        sleep(3)
        # 点击【安全中心】
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/span[3]").click()
        sleep(2)
        # 点击弱点评估
        driver.find_element(By.XPATH, '/html/body/div/div[1]/section/aside/ul/li[2]/div/i').click()
        sleep(2)
        # 点击弱点评估概览
        driver.find_element(By.XPATH, '/html/body/div/div[1]/section/aside/ul/li[2]/ul/li[1]').click()

    # 访问失败
    except NoSuchElementException as e:
        return 0
    else:
        return 1


# 创建弱点评估任务
def creat_weak_job(ser_name):
    try:
        sleep(5)
        try:
        # 点击评估任务
            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]").click()
        except NoSuchElementException as e:
            driver.find_element(By.XPATH, '/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]').click()


        # 点击【新建评估任务】
        driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/button[2]").click()
        try:
            # 输入任务名称
            driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/div[1]/div/div/input").send_keys(ser_name)


            # 点击任务执行方式
            driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/div[2]/div/div/label[1]/span[1]/span").click()
            '/html/body/div[3]/div/div[2]/form/div[2]/div/div/label[1]/span[1]/span'
            '/html/body/div[3]/div/div[2]/form/div[2]/div/div/label[1]/span[1]/span'
            '/html/body/div[3]/div/div[2]/form/div[2]/div/div/label[1]/span[1]/span'

            # 输入任务执行时间
            for i in range(1, 11):
                try:

                    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/div[" + str(i) + "]/div/div/div/input").send_keys('1')
                    break
                except NoSuchElementException as e:
                    continue


            # 点击评估对象
            driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/form/div[5]/div/div/div[1]/input').click()

            # 选择评估对象
            for i in range(1000):
                try:
                    get_name=driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li['+str(i)+']').text
                    if ser_name == get_name:
                        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li['+str(i)+']').click()
                        break
                except NoSuchElementException as e:
                    continue

            # 点击[评估规则]
            driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/div[6]/label").click()

            # 勾选评估规则
            driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/form/div[6]/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span").click()

            # 点击提交
            driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/span/button[1]").click()


        except NoSuchElementException as e:
            return 0
    # 访问失败
    except NoSuchElementException as e:
        return 0
    else:
        return 1

# 校验任务执行情况
def check_weak(ser_name):
    try:
        sleep(1)
        # 点击评估任务
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]").click()
        sleep(3)
        # 查看评估任务执行情况
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/button").click()
        # '/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/button'
        sleep(2)
        try:
            # 获取任务执行结果
            result = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[2]/div[1]/div[3]/table/tbody/tr/td[4]/div").text
            auto_threads.thread(10, 5, ser_name)
            print("触发的弱点评估数是:" + result)
            if result == '0' or result == '':
                return 0
            else:
                return 1
        except NoSuchElementException as e:
            sleep(30)
            return 0


    # 访问失败
    except NoSuchElementException as e:
        return 0

# 访问统计报表
def report_1(ser_name):
    sleep(1)
    # 点击统计报表
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/span[6]").click()
    # 点击报表任务
    driver.find_element(By.XPATH, "/html/body/div/div[1]/section/aside/ul/li[2]").click()
    sleep(5)
    # 点击新建任务
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div["+b+"]/button"
            driver.find_element(By.XPATH, path).click()
        except NoSuchElementException as e:
            continue
    sleep(1)
    # 输入任务名称
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div["+b+"]/div/div[2]/form/div[1]/div/div[1]/input"
            driver.find_element(By.XPATH, path).send_keys(ser_name)
        except NoSuchElementException as e:
            continue

    sleep(1)
    # 点击报表类型
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div["+b+"]/div/div[2]/form/div[2]/div/div[1]/div[2]/input"
            driver.find_element(By.XPATH, path).click()
        except NoSuchElementException as e:
            continue


def choose_report(c):
    # 选择报表类型
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div["+b+"]/div[1]/div[1]/ul/li["+str(c)+"]"
            driver.find_element(By.XPATH, path).click()

        except NoSuchElementException as e:
            continue


def report_2():
    # 点击提交按钮收起下拉框
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div["+b+"]/div/div[3]/span/button[1]"
            driver.find_element(By.XPATH, path).click()
        except NoSuchElementException as e:
            continue

    # 选择执行频率--立即执行
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div["+b+"]/div/div[2]/form/div[3]/div/div[1]/label[1]/span[1]/span"
            driver.find_element(By.XPATH, path).click()
        except NoSuchElementException as e:
            continue

    # 点击开始日期
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div["+b+"]/div/div[2]/form/div[4]/div/div/input[1]"
            driver.find_element(By.XPATH, path).click()
        except NoSuchElementException as e:
            continue

    # 点击开始时间
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div["+b+"]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input"
            driver.find_element(By.XPATH, path).click()
        except NoSuchElementException as e:
            continue

    # 清空
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div["+b+"]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input"
            driver.find_element(By.XPATH, path).clear()
        except NoSuchElementException as e:
            continue

    # 输入时间
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div["+b+"]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input"
            driver.find_element(By.XPATH, path).send_keys("00:00:00")
        except NoSuchElementException as e:
            continue

    # 点击确定
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div["+b+"]/div[2]/button[2]"
            driver.find_element(By.XPATH, path).click()
        except NoSuchElementException as e:
            continue

    # 点击提交
    for a in range(1, 10):
        try:
            b = str(a)
            path = "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div["+b+"]/div/div[3]/span/button[1]"
            driver.find_element(By.XPATH, path).click()
        except NoSuchElementException as e:
            continue
    sleep(2)


def check_report(ser_name):

    try:
        # 点击报表记录
        path = "/html/body/div/div[1]/section/aside/ul/li[3]"
        driver.find_element(By.XPATH, path).click()

        for i in range(1,13):
            # 匹配任务名称
            path = "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[3]/div[3]/table/tbody/tr["+str(i)+"]/td[4]/div/span/a/span"
            # '/html/body/div/div[1]/section/div/div/div[2]/div/div/div[3]/div[3]/table/tbody/tr[2]/td[4]/div/span/a/span'

            # 获取报表名称
            get_name = driver.find_element(By.XPATH, path).text
            print(get_name)
            # 获取报表类型
            get_type = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[3]/div[3]/table/tbody/tr['+str(i)+']/td[3]/div/span').text

            # 任务创建结果
            path1 = "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[3]/div[3]/table/tbody/tr[1]/td[6]/div/span/span"
            jd_loc = driver.find_element(By.XPATH, path1).text
            if ser_name == get_name and jd_loc == "成功":
                with open('./text.txt', 'a') as f:
                    print(get_name+":"+get_type+"--生成成功",file=f)
                return 0
            else:
                continue
        return 1
    except NoSuchElementException as e:
        return 1


# 服务高级配置
def account_1(ser_name):
    # 打流
    auto_threads.thread(10, 5, ser_name)
    sleep(20)
    driver.refresh()
    sleep(3)
    # 点击高级配置
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[3]/div[2]/div[4]/div[2]/table/tbody/tr/td[7]/div/button[3]/i").click()
    sleep(2)
    # 点击编辑
    driver.find_element(By.XPATH, "/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/form/div[5]/div/button").click()
    # '/html/body/div/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/form/div[5]/div/button'
    # 点击url
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/form/div[1]/div/div/div/input").click()
    sleep(3)
    # 选择url
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li").click()
    # 输入账号参数
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/form/div[2]/div/div[1]/input").send_keys("username")
    # 输入密码参数
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/form/div[3]/div/div[1]/input").send_keys("password")
    # 选择身份标记方式
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/form/div[4]/div/div/label[1]/span[1]/span").click()
    # 点击保存
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/form/div[5]/div/button[1]").click()
    sleep(5)

# 访问账号访问中心
def account_2(ser_name):
    # 打流
    auto_threads.thread(10, 5, ser_name)
    sleep(5)
    # 点击审计中心
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/span[4]").click()
    sleep(2)
    # 点击账号访问分析
    driver.find_element(By.XPATH, "/html/body/div/div[1]/section/aside/ul/li[3]").click()


# 检查账号访问中心
def check_account(ser_name):
    # 打流
    auto_threads.thread(10, 5, ser_name)
    try:
        # 点击操作
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr/td[7]/div/span/button/i").click()
        sleep(2)
        # 寻找服务是否存在
        for a in range(1, 13):
            try:
                b = str(a)
                path = "/html/body/div[1]/div[1]/section/div/div/div[2]/div/div/div[3]/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div[3]/table/tbody/tr[" + b + "]/td[3]/div/span"
                get_name = driver.find_element(By.XPATH, path).text
                # print(get_name)
                if get_name == ser_name:
                    re = 0
                    return 0
                else:
                    re = 1
                    continue
            except NoSuchElementException as e:
                continue
    except NoSuchElementException as e:
        return 1
    return re