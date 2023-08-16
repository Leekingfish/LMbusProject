from selenium.webdriver.common.by import By
from page.base_page import BasePage


class SupplierPage(BasePage):

    _locat_supplierCode = (By.ID,"_easyui_textbox_input5")
    _locat_supplierName = (By.ID,"_easyui_textbox_input6")
    _locat_supplierShortName = (By.ID,"_easyui_textbox_input7")
    _locat_supplierType = (By.CSS_SELECTOR,'#addForm-1 li:nth-child(4) .textbox-icon.combo-arrow')
    _locat_supplierType_choose = (By.ID,"datagrid-row-r2-1-0")

    def supplierInfor(self):
        """
        供应商信息
        :return:
        """
        self.find(self._locat_supplierCode).send_keys()     #供应商编码
        self.find(self._locat_supplierName).send_keys()     #全称
        self.find(self._locat_supplierShortName).send_keys()        #简称
        self.find(self._locat_supplierType).click()         #供应商类型
        self.find(self._locat_supplierType_choose).click()