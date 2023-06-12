from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_get_cookie():
    option = webdriver.ChromeOptions()
    option.debugger_address = "127.0.0.1:9222"
    # option.add_experimental_option("detach", True)  # 不自动关闭浏览器
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(5)
    driver.get("http://lmbussit.leemanpaper.com/main/login.html")
    driver.maximize_window()
    driver.find_element(By.ID, "_easyui_textbox_input1").send_keys("LM032451")
    driver.find_element(By.ID, "_easyui_textbox_input2").send_keys("L123456")
    driver.find_element(By.CSS_SELECTOR,"[style='margin-bottom:20px']:nth-child(3) .textbox-addon.textbox-addon-right").click()
    driver.find_element(By.ID, "orgCode_easyui_combobox_i1_6").click()
    driver.find_element(By.ID, "_easyui_textbox_input4").click()
    driver.find_element(By.CSS_SELECTOR,'.combobox-item.combobox-item-selected[id="chooseLanguage_easyui_combobox_i3_0"]').click()
    driver.find_element(By.ID, "btnLogin").click()

