from time import sleep

from selenium.webdriver.common.by import By
from page.base_page import BasePage


class SupplierPage(BasePage):
    _locat_iframe = (By.CSS_SELECTOR,"#tabPages > div.tabs-panels.tabs-panels-noborder.panel-noscroll > div:nth-child(3) > div > iframe")
    _locat_supplierCode = (By.ID,"_easyui_textbox_input5")
    _locat_supplierName = (By.ID,"_easyui_textbox_input6")
    _locat_supplierShortName = (By.ID,"_easyui_textbox_input7")
    _locat_supplierType = (By.ID,'_easyui_textbox_input29')
    _locat_supplierType_choose = (By.ID,"datagrid-row-r2-1-0")
    _locat_orderQuantityTolerance = (By.ID,'_easyui_textbox_input37')
    _locat_isAllowedSpotPurchase = (By.CSS_SELECTOR,'#addForm-5 li:nth-child(1) .textbox-icon.combo-arrow')
    _locat_isAllowedSpotPurchase_choose = (By.ID,"isAllowedSpotPurchase_easyui_combobox_i13_2")
    _locat_countryCode = (By.ID,"_easyui_textbox_input32")
    _locat_countryName = (By.ID,"_easyui_textbox_input36")
    _locat_address = (By.ID,"_easyui_textbox_input12")
    _locat_itermTitle = (By.CSS_SELECTOR,'.tabs-wrap li:nth-child(2)')
    _locat_tradeTermCode = (By.CSS_SELECTOR,'[field="tradeTermCode"] .textbox-addon.textbox-addon-right')
    _locat_tradeTermCode_choose = (By.ID,"_easyui_combobox_i17_2")
    _locat_paymentType = (By.CSS_SELECTOR,'[field="paymentType"] .textbox-addon.textbox-addon-right')
    _locat_paymentType_choose = (By.ID,"datagrid-row-r26-1-0")
    _locat_paymentTerm = (By.CSS_SELECTOR,'[field="paymentTerm"] .textbox-addon.textbox-addon-right')
    _locat_paymentTerm_choose = (By.ID,"datagrid-row-r27-1-1")
    _locat_currencyCode = (By.CSS_SELECTOR,'[field="currencyCode"] .textbox-addon.textbox-addon-right')
    _locat_currencyCode_choose = (By.ID,"datagrid-row-r28-1-0")
    _locat_billingUnitCode = (By.CSS_SELECTOR,'[field="billingUnitCode"] .textbox-addon.textbox-addon-right')
    _locat_billingUnitCode_choose = (By.ID,'_easyui_combobox_i63_3')
    _locat_taxScheduleCode = (By.ID,'_easyui_textbox_input47')
    _locat_effectiveDate = (By.ID,"_easyui_textbox_input50")
    _locat_effectiveDate_enter = (By.CSS_SELECTOR,'[field="effectiveDate"] .textbox-addon.textbox-addon-right')
    _locat_expirationDate = (By.ID,"_easyui_textbox_input51")
    _locat_expirationDate_enter = (By.CSS_SELECTOR,'[field="expirationDate"] .textbox-addon.textbox-addon-right')


    def supplierInfor(self):
        """
        供应商信息
        :return:
        """
        iframe = self.find(self._locat_iframe)
        self.driver.switch_to.frame(iframe)
        self.find(self._locat_supplierCode).send_keys("123")     #供应商编码
        self.find(self._locat_supplierName).send_keys("123")     #全称
        self.find(self._locat_supplierShortName).send_keys("123")        #简称
        self.find(self._locat_supplierType).send_keys("竹木供应商")         #供应商类型
        self.find(self._locat_supplierType_choose).click()
        """
        基础信息
        """
        # self.find(self._locat_orderQuantityTolerance).send_keys("1")         #浮动比例
        # self.find(self._locat_isAllowedSpotPurchase).click()        #是否允许现货
        # sleep(1)
        # self.find(self._locat_isAllowedSpotPurchase_choose).click()
        # self.find(self._locat_countryCode).send_keys("CN")          #国家
        # self.find(self._locat_countryName).send_keys("CN")          #原产国
        """
        CN	中华人民共和国
        ID	印度尼西亚共和国
        MY	马来西亚
        NZL	新西兰
        US	美国
        VN	越南民主共和国
        """
        # self.find(self._locat_address).send_keys("403 no found")        #详细地址
        """
        条款信息
        """
        self.find(self._locat_itermTitle).click()       #条款信息
        self.find(self._locat_tradeTermCode).click()        #贸易条件
        self.find(self._locat_tradeTermCode_choose).click()
        self.find(self._locat_paymentType).click()      #结算方式
        self.find(self._locat_paymentType_choose).click()
        self.find(self._locat_paymentTerm).click()          #结算条件
        self.find(self._locat_paymentTerm_choose).click()
        self.find(self._locat_currencyCode).click()         #币种
        self.find(self._locat_currencyCode_choose).click()
        self.find(self._locat_billingUnitCode).click()          #计量单位
        self.find(self._locat_billingUnitCode_choose).click()
        self.find(self._locat_taxScheduleCode).send_keys("VT13")        #税别
        self.find(self._locat_effectiveDate).send_keys("2023年08月17日")          #生效时间
        self.find(self._locat_effectiveDate_enter).click()
        self.find(self._locat_expirationDate).send_keys("2033年08月17日")         #失效时间
        self.find(self._locat_expirationDate_enter).click()

