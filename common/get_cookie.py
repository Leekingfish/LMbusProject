from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_get_cookie():
    option = webdriver.ChromeOptions()
    # option.debugger_address = "127.0.0.1:9222"
    option.add_experimental_option("detach", True)  # 不自动关闭浏览器
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get("http://lmbussit.leemanpaper.com/main/login.html")
    driver.implicitly_wait(5)
    # driver.find_element(By.ID, "_easyui_textbox_input1").send_keys("LM032451")
    # driver.find_element(By.ID, "_easyui_textbox_input2").send_keys("Ljy12300")
    # driver.find_element(By.CSS_SELECTOR,"[style='margin-bottom:20px']:nth-child(3) .textbox-addon.textbox-addon-right").click()
    # driver.find_element(By.ID, "orgCode_easyui_combobox_i1_7").click()
    # driver.find_element(By.ID, "btnLogin").click()
    # sleep(2)
    # cookie = driver.get_cookies()
    # print(cookie)
    # with open("./data.yaml","w",encoding="UTF-8") as f:
    #     yaml.dump(cookie,f)

    cookies = [{'domain': 'lmbussit.leemanpaper.com', 'httpOnly': False, 'name': 'sso_ticket', 'path': '/main', 'sameSite': 'Lax', 'secure': False, 'value': 'OTkxbzBucG8KWVozNjU3ODQKWVpHLVBNCjQwNTQzNTQwMDQ5NTYKN28zbjIwc241OG80NDhx'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("http://lmbussit.leemanpaper.com/main/index.html")

    # with open("./data.yaml", encoding="UTF-8") as f:
    #     yaml_data = yaml.safe_load(f)
    #     for cookie in yaml_data:
    #         driver.add_cookie(cookie)
    #         driver.get("http://lmbussit.leemanpaper.com/main/index.html")



