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
    _locat_tradeTermCode_choose = (By.ID,"_easyui_combobox_i16_2")
    _locat_paymentType = (By.CSS_SELECTOR,'[field="paymentType"] .textbox-addon.textbox-addon-right')
    _locat_paymentType_choose = (By.ID,"datagrid-row-r26-1-0")
    _locat_paymentTerm = (By.CSS_SELECTOR,'[field="paymentTerm"] .textbox-addon.textbox-addon-right')
    _locat_paymentTerm_choose = (By.ID,"datagrid-row-r27-1-1")
    _locat_currencyCode = (By.CSS_SELECTOR,'[field="currencyCode"] .textbox-addon.textbox-addon-right')
    _locat_currencyCode_choose = (By.ID,"datagrid-row-r28-1-0")
    _locat_billingUnitCode = (By.CSS_SELECTOR,'[field="billingUnitCode"] .textbox-addon.textbox-addon-right')
    _locat_billingUnitCode_choose = (By.ID,'_easyui_combobox_i17_3')
    _locat_taxScheduleCode = (By.ID,'_easyui_textbox_input47')
    _locat_iterm_effectiveDate = (By.ID,"_easyui_textbox_input50")
    _locat_iterm_effectiveDate_enter = (By.CSS_SELECTOR,'#datagrid-row-r20-2-0 [field="effectiveDate"] .textbox-addon.textbox-addon-right')
    _locat_iterm_expirationDate = (By.ID,"_easyui_textbox_input51")
    _locat_iterm_expirationDate_enter = (By.CSS_SELECTOR,'#datagrid-row-r20-2-0 [field="expirationDate"] .textbox-addon.textbox-addon-right')
    _locat_contactTitle = (By.CSS_SELECTOR,'.tabs-wrap li:nth-child(3)')
    _locat_contactName = (By.ID,"_easyui_textbox_input52")
    _locat_positionDesc = (By.ID,"_easyui_textbox_input53")
    _locat_mobilNo = (By.ID,"_easyui_textbox_input54")
    _locat_telNo = (By.ID,"_easyui_textbox_input55")
    _locat_faxNo = (By.ID,"_easyui_textbox_input56")
    _locat_email = (By.CSS_SELECTOR,'[field="email"] .datagrid-editable-input.validatebox-text')
    _locat_contact_effectiveDate = (By.ID,"_easyui_textbox_input57")
    _locat_contact_effectiveDate_enter = (By.CSS_SELECTOR, '#datagrid-row-r21-2-0 [field="effectiveDate"] .textbox-icon.combo-arrow')
    _locat_contact_expirationDate = (By.ID,"_easyui_textbox_input58")
    _locat_contact_expirationDate_enter = (By.CSS_SELECTOR, '#datagrid-row-r21-2-0 [field="expirationDate"] .textbox-addon.textbox-addon-right')
    _locat_siteTitle = (By.CSS_SELECTOR, '.tabs-wrap li:nth-child(6)')
    _locat_siteCode = (By.CSS_SELECTOR,'[field="siteCode"] .textbox-icon.combo-arrow')
    _locat_siteCode_choose = (By.ID,"datagrid-row-r37-1-0")
    _locat_siteType = (By.CSS_SELECTOR,'[field="siteType"] .textbox-icon.combo-arrow')
    _locat_siteType_choose = (By.ID,"_easyui_combobox_i27_1")
    _locat_teamCode = (By.CSS_SELECTOR,'[field="teamCode"] .textbox-icon.combo-arrow')
    _locat_teamCode_choose = (By.ID,"_easyui_combobox_i29_1")
    _locat_buyer = (By.CSS_SELECTOR,'[field="buyer"] .textbox-icon.combo-arrow')
    _locat_buyer_choose = (By.ID,"_easyui_combobox_i31_1")
    _locat_site_effectiveDate = (By.ID,"_easyui_textbox_input101")
    _locat_site_effectiveDate_enter = (By.CSS_SELECTOR, '#datagrid-row-r36-2-0 [field="effectiveDate"] .textbox-icon.combo-arrow')
    _locat_site_expirationDate = (By.ID,"_easyui_textbox_input102")
    _locat_site_expirationDate_enter = (By.CSS_SELECTOR, '#datagrid-row-r36-2-0 [field="expirationDate"] .textbox-addon.textbox-addon-right')
    _locat_bankTitle = (By.CSS_SELECTOR, '.tabs-wrap li:nth-child(4)')
    _locat_bankTitle_choose = (By.ID,"datagrid-row-r22-1-0")
    _locat_bankTitleRemove = (By.CSS_SELECTOR,'.panel:nth-child(4) .datagrid-toolbar td:nth-child(2)')
    _locat_brandTitle = (By.CSS_SELECTOR, '.tabs-wrap li:nth-child(5)')
    _locat_brandTitle_choose = (By.ID,"datagrid-row-r23-1-0")
    _locat_brandTitleRemove = (By.CSS_SELECTOR,'.panel:nth-child(5) .datagrid-toolbar td:nth-child(2)')
    _locat_buyTitle = (By.CSS_SELECTOR, '.tabs-wrap li:nth-child(7)')
    _locat_buyTitle_choose = (By.ID,"datagrid-row-r24-1-0")
    _locat_buyTitleRemove = (By.CSS_SELECTOR,'.panel:nth-child(7) .datagrid-toolbar td:nth-child(2)')
    _locat_save = (By.ID,"addSave")
    _locat_submit = (By.CSS_SELECTOR,'#editList > a:nth-child(12)')
    _locat_tip_window = (By.CSS_SELECTOR, 'body > div.panel.window.messager-window > div.dialog-button.messager-button > a:nth-child(1) > span > span')
    _locat_accept = (By.CSS_SELECTOR,'#editList > a:nth-child(13)')

    def supplierInfor(self):
        """
        供应商信息
        :return:
        """
        iframe = self.find(self._locat_iframe)
        self.driver.switch_to.frame(iframe)
        self.find(self._locat_supplierCode).send_keys("601")     #供应商编码
        self.find(self._locat_supplierName).send_keys("测试")     #全称
        self.find(self._locat_supplierShortName).send_keys("123")        #简称
        self.find(self._locat_supplierType).send_keys("竹木供应商")         #供应商类型
        self.find(self._locat_supplierType_choose).click()
        """
        基础信息
        """
        self.find(self._locat_orderQuantityTolerance).send_keys("1")         #浮动比例
        self.find(self._locat_isAllowedSpotPurchase).click()        #是否允许现货
        sleep(1)
        self.find(self._locat_isAllowedSpotPurchase_choose).click()
        self.find(self._locat_countryCode).send_keys("CN")          #国家
        sleep(1)
        self.find(self._locat_countryName).send_keys("CN")          #原产国
        sleep(1)
        """
        CN	中华人民共和国
        ID	印度尼西亚共和国
        MY	马来西亚
        NZL	新西兰
        US	美国
        VN	越南民主共和国
        """
        self.find(self._locat_address).send_keys("403 no found")        #详细地址
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
        self.find(self._locat_iterm_effectiveDate).send_keys("2023年08月17日")          #生效时间
        self.find(self._locat_iterm_effectiveDate_enter).click()
        self.find(self._locat_iterm_expirationDate).send_keys("2033年08月17日")         #失效时间
        self.find(self._locat_iterm_expirationDate_enter).click()
        """
        联系人信息
        """
        self.find(self._locat_contactTitle).click()         #联系人信息
        self.find(self._locat_contactName).send_keys("1")        #姓名
        # self.find(self._locat_positionDesc).send_keys("1")       #职位
        # self.find(self._locat_mobilNo).send_keys("1")            #手机
        # self.find(self._locat_telNo).send_keys("1")          #联系电话
        # self.find(self._locat_faxNo).send_keys("1")          #传真号码
        # self.find(self._locat_email).send_keys("1")          #邮箱
        self.find(self._locat_contact_effectiveDate).send_keys("2023年08月17日")          #生效时间
        self.find(self._locat_contact_effectiveDate_enter).click()
        self.find(self._locat_contact_expirationDate).send_keys("2029年08月17日")         #失效时间
        self.find(self._locat_contact_expirationDate_enter).click()
        """
        打包场信息
        """
        self.find(self._locat_siteTitle).click()        #打包场信息
        self.find(self._locat_siteCode).click()         #打包场名称
        self.find(self._locat_siteCode_choose).click()
        # self.find(self._locat_siteType).click()         #打包场类型
        # self.find(self._locat_siteType_choose).click()
        self.find(self._locat_teamCode).click()         #团队名称
        self.find(self._locat_teamCode_choose).click()
        self.find(self._locat_buyer).click()            #采购员
        self.find(self._locat_buyer_choose).click()
        self.find(self._locat_site_effectiveDate).send_keys("2023年08月17日")          #生效时间
        self.find(self._locat_site_effectiveDate_enter).click()
        self.find(self._locat_site_expirationDate).send_keys("2029年10月17日")         #失效时间
        self.find(self._locat_site_expirationDate_enter).click()
        """
        银行信息
        """
        self.find(self._locat_bankTitle).click()            #银行信息
        # self.find(self._locat_bankTitle_choose).click()         #选择明细
        self.find(self._locat_bankTitleRemove).click()          #删除
        """
        品牌信息
        """
        self.find(self._locat_brandTitle).click()           #品牌信息
        # self.find(self._locat_brandTitle_choose).click()            #选择明细
        self.find(self._locat_brandTitleRemove).click()         #删除
        """
        回购信息
        """
        self.find(self._locat_buyTitle).click()         #回购信息
        # self.find(self._locat_buyTitle_choose).click()          #选择明细
        self.find(self._locat_buyTitleRemove).click()           #删除

        self.find(self._locat_save).click()         #保存
        sleep(3)
        self.find(self._locat_submit).click()       #提交
        self.find(self._locat_tip_window).click()
        sleep(3)
        self.find(self._locat_accept).click()       #同意
        self.find(self._locat_tip_window).click()