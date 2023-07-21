from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestLogin:

    def setup(self):
        option = webdriver.ChromeOptions()
        # option.debugger_address="127.0.0.1:9222"
        option.add_experimental_option("detach", True)  # 不自动关闭浏览器
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.get("http://lmbusuat.leemanpaper.com/main/login.html")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "_easyui_textbox_input1").send_keys("LM032451")
        self.driver.find_element(By.ID, "_easyui_textbox_input2").send_keys("L123456")
        self.driver.find_element(By.CSS_SELECTOR,
                            "[style='margin-bottom:20px']:nth-child(3) .textbox-addon.textbox-addon-right").click()
        self.driver.find_element(By.ID, "orgCode_easyui_combobox_i1_7").click()
        """
        下拉框选项
        orgCode_easyui_combobox_i1_0 : 理文造纸
        orgCode_easyui_combobox_i1_1 : 重庆理文造纸有限公司
        orgCode_easyui_combobox_i1_2 : 东莞理文造纸厂有限公司
        orgCode_easyui_combobox_i1_3 : 广东理文造纸有限公司
        orgCode_easyui_combobox_i1_4 : 江苏理文造纸有限公司
        orgCode_easyui_combobox_i1_5 : 江西理文造纸有限公司
        orgCode_easyui_combobox_i1_6 : 重庆理文卫生用纸制造有限公司
        orgCode_easyui_combobox_i1_7 : 崇左理文纸浆制品有限公司
        orgCode_easyui_combobox_i1_8 : 重庆理文制浆有限公司
        """
        self.driver.find_element(By.ID, "_easyui_textbox_input4").click()
        self.driver.find_element(By.CSS_SELECTOR,
                            '.combobox-item.combobox-item-selected[id="chooseLanguage_easyui_combobox_i3_0"]').click()
        self.driver.find_element(By.ID, "btnLogin").click()

    def test_songhuo(self):
        # self.driver.get("http://lmbusuat.leemanpaper.com/main/index.html")
        # self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR,'.float_l.nav_cont.nav_text[title="采购管理"]').click()
        self.driver.find_element(By.CSS_SELECTOR,'.system.float_r[title="预约送货"]').click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,'.system_setting.middle_left[title="送货预约"]').click()
        sleep(1)
        iframe = self.driver.find_element(By.CSS_SELECTOR,"#tabPages > div.tabs-panels.tabs-panels-noborder.panel-noscroll > div:nth-child(2) > div > iframe")
        self.driver.switch_to.frame(iframe)
        """
        新增预约单
        """
        self.driver.find_element(By.CSS_SELECTOR,'li:nth-child(10) .textbox.combo .textbox-addon.textbox-addon-right').click()
        self.driver.find_element(By.ID,"purchaseType_easyui_combobox_i6_2").click()
        """
        下拉框选项
        purchaseType_easyui_combobox_i6_1 : 国废采购
        purchaseType_easyui_combobox_i6_2 : 竹木采购
        purchaseType_easyui_combobox_i6_3 : 煤炭采购
        purchaseType_easyui_combobox_i6_4 : 木粉采购
        purchaseType_easyui_combobox_i6_5 : 木浆采购
        purchaseType_easyui_combobox_i6_6 : 辅料采购
        """
        self.driver.find_element(By.ID,'_easyui_textbox_input15').send_keys("A0003")     #选择供应商
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,'#saveForm > ul > li:nth-child(8) > span > span').click()        #送货日期
        self.driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(27) > div > div.datebox-button > table > tbody > tr > td:nth-child(1) > a').click()
        self.driver.find_element(By.CSS_SELECTOR,'#saveForm > ul > li:nth-child(9) > span > span > a').click()      #到厂日期
        self.driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(28) > div > div.datebox-button > table > tbody > tr > td:nth-child(1) > a').click()
        self.driver.find_element(By.CSS_SELECTOR,'.datagrid-toolbar td:nth-child(1)').click()       #新增明细
        self.driver.find_element(By.CSS_SELECTOR,'[field="originCode"] .textbox-addon.textbox-addon-right').click()    #选择产地
        self.driver.find_element(By.ID,"datagrid-row-r13-1-0").click()
        self.driver.find_element(By.ID,'_easyui_textbox_input26').send_keys("ZB0003")      #选择料号
        sleep(1)
        self.driver.find_element(By.ID,"_easyui_textbox_input27").send_keys("1")        #车数
        self.driver.find_element(By.ID,"_easyui_textbox_input28").send_keys("111")      #吨数
        self.driver.find_element(By.CSS_SELECTOR,'[field="deliveryCarType"] .textbox-addon.textbox-addon-right').click()        #选择车型
        self.driver.find_element(By.ID,"_easyui_combobox_i10_2").click()
        self.driver.find_element(By.ID,"addSave").click()       #保存
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#editList > a:nth-child(7)').click()      #提交
        self.driver.find_element(By.CSS_SELECTOR,'body > div.panel.window.messager-window > div.dialog-button.messager-button > a:nth-child(1)').click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#editList > a:nth-child(8) > span').click()       #同意
        self.driver.find_element(By.CSS_SELECTOR, 'body > div.panel.window.messager-window > div.dialog-button.messager-button > a:nth-child(1)').click()


