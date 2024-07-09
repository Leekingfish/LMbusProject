from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class TransportArrangementPage(BasePage):
    _locat_businessSourceCode = (By.ID,'#addForm-1 li:nth-child(2) .textbox-addon.textbox-addon-right')
    _locat_businessSourceCode_chosse = (By.ID,'businessSourceCode_easyui_combobox_i8_1')
    _locat_businessTaskCode = (By.ID,'#addForm-1 li:nth-child(3) .textbox-addon.textbox-addon-right')
    _locat_businessTaskCode_chosse = (By.ID,'businessTaskCode_easyui_combobox_i17_1')
    """
    businessTaskCode_easyui_combobox_i17_0  销售出货
    businessTaskCode_easyui_combobox_i17_1  客户自提
    businessTaskCode_easyui_combobox_i17_2  固废出厂
    """
    _locat_businessDate = (By.ID,'#addForm-1 li:nth-child(4) .textbox-addon.textbox-addon-right')
    _locat_businessDate_chosse = (By.CSS_SELECTOR,'.combo-panel.panel-body.panel-body-noheader .datebox-button td:nth-child(1)')


    def business(self):
        self.find(self._locat_businessSourceCode).click()       #业务来源
        self.find(self._locat_businessSourceCode_chosse).click()
        self.find(self._locat_businessTaskCode).click()         #任务类型
        self.find(self._locat_businessTaskCode_chosse).click()
        self.find(self._locat_businessDate).click()     #付运通知日期
        self.find(self._locat_businessDate_chosse).click()

