from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import datetime
from selenium.webdriver.common.action_chains import ActionChains
import ddddocr
from time import sleep
import pythonProject.api_auto.sec.auto_threads as auto_threads




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
            "SysAdmin")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div/div[1]").click()
        # 输入密码
        driver.find_element(By.XPATH,
                            "/html/body/div/div[1]/section/div/div/div[3]/form/div[2]/div/div/input").send_keys(
            "hillstone@2022")
    except NoSuchElementException as e:
        return 0
    # 有验证码输入   赋值为1
    else:
        return 1

    sleep(1)

# 校验验证码
def check_yzm():
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