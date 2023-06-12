from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.debugger_address="127.0.0.1:9222"
        # option.add_experimental_option("detach", True)  # 不自动关闭浏览器
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("http://lmbussit.leemanpaper.com/main/index.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def test_songhuo(self):
        self.driver.find_element(By.CSS_SELECTOR,'.float_l.nav_cont.nav_text[title="采购管理"]').click()
        self.driver.find_element(By.CSS_SELECTOR,'.system.float_r[title="预约送货"]').click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'.system_setting.middle_left[title="送货预约"]').click()
        sleep(3)
        iframe = self.driver.find_element(By.CSS_SELECTOR,"#tabPages > div.tabs-panels.tabs-panels-noborder.panel-noscroll > div:nth-child(2) > div > iframe")
        self.driver.switch_to.frame(iframe)
        """
        新增预约单
        """
        # self.driver.find_element(By.ID,"btnDelete").click()       #新增
        self.driver.find_element(By.CSS_SELECTOR,'li:nth-child(10) .textbox.combo .textbox-addon.textbox-addon-right').click()
        self.driver.find_element(By.ID,"purchaseType_easyui_combobox_i6_5").click()
        """
        下拉框选项
        purchaseType_easyui_combobox_i6_1 : 国废采购
        purchaseType_easyui_combobox_i6_2 : 竹木采购
        purchaseType_easyui_combobox_i6_3 : 煤炭采购
        purchaseType_easyui_combobox_i6_4 : 木粉采购
        purchaseType_easyui_combobox_i6_5 : 木浆采购
        purchaseType_easyui_combobox_i6_6 : 辅料采购
        """
        self.driver.find_element(By.ID,'_easyui_textbox_input15').send_keys("广利贸易")
        self.driver.find_element(By.ID,'_easyui_textbox_input19').send_keys("2023年06月06日")
        self.driver.find_element(By.ID,'_easyui_textbox_input20').send_keys("2023年06月06日")
