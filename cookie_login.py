import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_cookie_login():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)  # 不自动关闭浏览器
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get("http://lmbusuat.leemanpaper.com/main/login.html")
    # driver.implicitly_wait(5)
    # driver.find_element(By.ID, "_easyui_textbox_input1").send_keys("LM032451")
    # driver.find_element(By.ID, "_easyui_textbox_input2").send_keys("L123456")
    # driver.find_element(By.CSS_SELECTOR,
    #                          "[style='margin-bottom:20px']:nth-child(3) .textbox-addon.textbox-addon-right").click()
    # driver.find_element(By.ID, "orgCode_easyui_combobox_i1_7").click()
    # """
    # 下拉框选项
    # orgCode_easyui_combobox_i1_0 : 理文造纸
    # orgCode_easyui_combobox_i1_1 : 重庆理文造纸有限公司
    # orgCode_easyui_combobox_i1_2 : 东莞理文造纸厂有限公司
    # orgCode_easyui_combobox_i1_3 : 广东理文造纸有限公司
    # orgCode_easyui_combobox_i1_4 : 江苏理文造纸有限公司
    # orgCode_easyui_combobox_i1_5 : 江西理文造纸有限公司
    # orgCode_easyui_combobox_i1_6 : 重庆理文卫生用纸制造有限公司
    # orgCode_easyui_combobox_i1_7 : 崇左理文纸浆制品有限公司
    # orgCode_easyui_combobox_i1_8 : 重庆理文制浆有限公司
    # """
    # driver.find_element(By.ID, "_easyui_textbox_input4").click()
    # driver.find_element(By.CSS_SELECTOR,
    #                          '.combobox-item.combobox-item-selected[id="chooseLanguage_easyui_combobox_i3_0"]').click()
    # driver.find_element(By.ID, "btnLogin").click()
    # cookie = driver.get_cookies()
    # print(cookie)
    # #将cookie写进yaml文件
    # with open("./data.yaml","w",encoding="UTF-8") as f:
    #     yaml.dump(cookie,f)

    with open("./data.yaml",encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get("http://lmbussit.leemanpaper.com/main/index.html")