from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    _locat_usename = (By.ID, "_easyui_textbox_input1")
    _locat_pwd = (By.ID, "_easyui_textbox_input2")
    _locat_orgcode = (By.CSS_SELECTOR,"[style='margin-bottom:20px']:nth-child(3) .textbox-addon.textbox-addon-right")
    _locat_chooseOrgcode = (By.ID, "orgCode_easyui_combobox_i1_7")
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
    _locat_Language = (By.ID, "_easyui_textbox_input4")
    _locat_chooseLanguage = (By.CSS_SELECTOR,'.combobox-item.combobox-item-selected[id="chooseLanguage_easyui_combobox_i3_0"]')
    _locat_login = (By.ID, "btnLogin")
    _locat_iframe = (By.CSS_SELECTOR,"#tabPages > div.tabs-panels.tabs-panels-noborder.panel-noscroll > div:nth-child(3) > div > iframe")
    _locat_purchase_type = (By.CSS_SELECTOR, 'li:nth-child(10) .textbox.combo .textbox-addon.textbox-addon-right')
    _locat_purchase_choose = (By.ID, "purchaseType_easyui_combobox_i6_2")
    """
    下拉框选项
    purchaseType_easyui_combobox_i6_1 : 国废采购
    purchaseType_easyui_combobox_i6_2 : 竹木采购
    purchaseType_easyui_combobox_i6_3 : 煤炭采购
    purchaseType_easyui_combobox_i6_4 : 木粉采购
    purchaseType_easyui_combobox_i6_5 : 木浆采购
    purchaseType_easyui_combobox_i6_6 : 辅料采购
    purchaseType_easyui_combobox_i6_7 : 燃料采购
    purchaseType_easyui_combobox_i6_9 : 木料采购
    purchaseType_easyui_combobox_i6_11 : 五金采购
    """
    _locat_vendor = (By.ID, '_easyui_textbox_input15')
    _locat_delivery_date = (By.CSS_SELECTOR, '#saveForm > ul > li:nth-child(8) > span > span')
    _locat_delivery_date_choose = (
    By.CSS_SELECTOR, 'body > div:nth-child(27) > div > div.datebox-button > table > tbody > tr > td:nth-child(1) > a')
    _locat_reach_date = (By.CSS_SELECTOR, '#saveForm > ul > li:nth-child(9) > span > span > a')
    _locat_reach_date_choose = (By.CSS_SELECTOR, 'body > div:nth-child(28) > div > div.datebox-button > table > tbody > tr > td:nth-child(1) > a')

    def __init__(self,base_driver=None):
        #用作ide类型提示
        base_driver : WebDriver
        if base_driver is None:
            option = webdriver.ChromeOptions()
            # option.debugger_address = "127.0.0.1:9222"
            option.add_experimental_option("detach", True)  # 不自动关闭浏览器
            self.driver = webdriver.Chrome(options=option)
            # self.driver = webdriver.Edge()
            self.driver.maximize_window()
            self.driver.get("http://lmbussit.leemanpaper.com/main/login.html")          #sit环境
            # self.driver.get("http://lmbusuat.leemanpaper.com/main/login.html")          #uat环境
            self.driver.implicitly_wait(5)
            cookies = [{'domain': 'lmbussit.leemanpaper.com', 'httpOnly': False, 'name': 'sso_ticket', 'path': '/main',
                        'sameSite': 'Lax', 'secure': False,
                        'value': 'OTkxbzBucG8KWVozNjU3ODQKWVpHLVBNCjQwNTQzNTQwMDQ5NTYKN28zbjIwc241OG80NDhx'}]
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get("http://lmbussit.leemanpaper.com/main/index.html")
        else:
            self.driver = base_driver

    def find(self,by,value=None):
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by,value=value)

    def finds(self,by,value=None):
        if value is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by=by,value=value)

    def wait_click(self,wait_ele):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(wait_ele))

    def book_common(self):
        iframe = self.find(self._locat_iframe)
        self.driver.switch_to.frame(iframe)
        self.find(self._locat_purchase_type).click()     # 选择采购类型
        self.find(self._locat_purchase_choose).click()
        self.find(self._locat_vendor).send_keys("0055")  # 选择供应商
        sleep(1)
        self.find(self._locat_delivery_date).click()  # 送货日期
        self.find(self._locat_delivery_date_choose).click()
        self.find(self._locat_reach_date).click()  # 到厂日期
        self.find(self._locat_reach_date_choose).click()