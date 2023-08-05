from time import sleep

from selenium.webdriver.common.by import By
from page.base_page import BasePage


class MaterialsPage(BasePage):
    _locat_iframe = (By.CSS_SELECTOR,"#tabPages > div.tabs-panels.tabs-panels-noborder.panel-noscroll > div:nth-child(3) > div > iframe")
    _locat_commodityCode = (By.ID,'_easyui_textbox_input4')
    _locat_commodityCnName = (By.ID,'_easyui_textbox_input5')
    _locat_commodityEnName = (By.ID,'_easyui_textbox_input6')
    _locat_commoditySpecification = (By.ID,'_easyui_textbox_input7')
    _locat_unit = (By.CSS_SELECTOR,'.tabs li:nth-child(2)')
    _locat_commodityUnit1 = (By.CSS_SELECTOR,'#datagrid-row-r13-2-0 [field="commodityUnit"]')
    _locat_commodityUnit1_right = (By.CSS_SELECTOR,'#datagrid-row-r13-2-0 .textbox-addon.textbox-addon-right')
    _locat_commodityUnit1_choose = (By.ID,"_easyui_combobox_i32_12")
    _locat_conversionRate1 = (By.CSS_SELECTOR,'#datagrid-row-r13-2-0 [field="conversionRate"] .textbox-text.validatebox-text.textbox-prompt')
    _locat_commodityUnit2 = (By.CSS_SELECTOR,'#datagrid-row-r13-2-1 [field="commodityUnit"]')
    _locat_commodityUnit2_right = (By.CSS_SELECTOR, '#datagrid-row-r13-2-1 .textbox-addon.textbox-addon-right')
    _locat_commodityUnit2_choose = (By.ID, "_easyui_combobox_i34_12")
    _locat_conversionRate2 = (By.CSS_SELECTOR, '#datagrid-row-r13-2-1 [field="conversionRate"] .textbox-text.validatebox-text.textbox-prompt')
    _locat_commodityUnit3 = (By.CSS_SELECTOR,'#datagrid-row-r13-2-2 [field="commodityUnit"]')
    _locat_commodityUnit3_right = (By.CSS_SELECTOR, '#datagrid-row-r13-2-2 .textbox-addon.textbox-addon-right')
    _locat_commodityUnit3_choose = (By.ID, "_easyui_combobox_i36_12")
    _locat_conversionRate3 = (By.CSS_SELECTOR,'#datagrid-row-r13-2-2 [field="conversionRate"] .textbox-text.validatebox-text.textbox-prompt')
    _locat_commodityUnit4 = (By.CSS_SELECTOR,'#datagrid-row-r13-2-3 [field="commodityUnit"]')
    _locat_commodityUnit4_right = (By.CSS_SELECTOR, '#datagrid-row-r13-2-3 .textbox-addon.textbox-addon-right')
    _locat_commodityUnit4_choose = (By.ID, "_easyui_combobox_i38_12")
    _locat_conversionRate4 = (By.CSS_SELECTOR,'#datagrid-row-r13-2-3 [field="conversionRate"] .textbox-text.validatebox-text.textbox-prompt')
    _locat_commodityUnit5 = (By.CSS_SELECTOR,'#datagrid-row-r13-2-4 [field="commodityUnit"]')
    _locat_commodityUnit5_right = (By.CSS_SELECTOR, '#datagrid-row-r13-2-4 .textbox-addon.textbox-addon-right')
    _locat_commodityUnit5_choose = (By.ID, "_easyui_combobox_i40_12")
    _locat_conversionRate5 = (By.CSS_SELECTOR,'#datagrid-row-r13-2-4 [field="conversionRate"] .textbox-text.validatebox-text.textbox-prompt')
    _locat_commodityType = (By.CSS_SELECTOR, '.tabs li:nth-child(4)')
    _locat_add = (By.CSS_SELECTOR,'.panel:nth-child(4) .datagrid-toolbar td:nth-child(1)')
    _locat_remove = (By.CSS_SELECTOR, '.panel:nth-child(4) .datagrid-toolbar td:nth-child(2)')
    _locat_classifyAttribution = (By.CSS_SELECTOR,'#datagrid-row-r24-2-0 [field="classifyAttribution"] .textbox-icon.combo-arrow')
    _locat_classifyAttribution_choose = (By.ID,"_easyui_combobox_i27_0")
    _locat_classifyAttribution_choose1 = (By.ID, "_easyui_combobox_i27_1")
    _locat_commodityTypeCode = (By.ID, '_easyui_textbox_input75')
    _locat_oneClassifyCode = (By.ID,'_easyui_textbox_input77')
    _locat_secondeClassifyCode = (By.ID,'_easyui_textbox_input79')
    _locat_thirdClassifyCode = (By.ID,"_easyui_textbox_input81")
    _locat_fourthClassifyCode = (By.ID,"_easyui_textbox_input83")
    _locat_classifyAttribution2 = (By.CSS_SELECTOR,'#datagrid-row-r24-2-1 [field="classifyAttribution"] .textbox-icon.combo-arrow')
    _locat_classifyAttribution2_choose = (By.ID,"_easyui_combobox_i32_0")
    _locat_classifyAttribution2_choose1 = (By.ID, "_easyui_combobox_i32_1")
    _locat_commodityTypeCode2 = (By.ID, '_easyui_textbox_input100')
    _locat_oneClassifyCode2 = (By.ID,'_easyui_textbox_input102')
    _locat_secondeClassifyCode2 = (By.ID,'_easyui_textbox_input104')





    def commodityInfor(self):
        """
        料品信息维护
        :return:
        """
        iframe = self.find(self._locat_iframe)
        self.driver.switch_to.frame(iframe)
        self.find(self._locat_commodityCode).send_keys("Q123")      #料品编码
        self.find(self._locat_commodityCnName).send_keys("12")      #料品名称
        self.find(self._locat_commodityEnName).send_keys("12")      #料品简称
        self.find(self._locat_commoditySpecification).send_keys("1234")     #规格
        """
        计量单位
        """
        # self.find(self._locat_unit).click()
        # self.find(self._locat_commodityUnit1).click()       #批量单位
        # self.find(self._locat_commodityUnit1_right).click()
        # self.find(self._locat_commodityUnit1_choose).click()
        # self.find(self._locat_conversionRate1).send_keys("1")       #转换率
        # self.find(self._locat_commodityUnit2).click()       #计价单位
        # self.find(self._locat_commodityUnit2_right).click()
        # self.find(self._locat_commodityUnit2_choose).click()
        # self.find(self._locat_conversionRate2).send_keys("1")       #转换率
        # self.find(self._locat_commodityUnit3).click()       #库存单位
        # self.find(self._locat_commodityUnit3_right).click()
        # self.find(self._locat_commodityUnit3_choose).click()
        # self.find(self._locat_conversionRate3).send_keys("1")       #转换率
        # self.find(self._locat_commodityUnit4).click()       #库存主单位
        # self.find(self._locat_commodityUnit4_right).click()
        # self.find(self._locat_commodityUnit4_choose).click()
        # self.find(self._locat_conversionRate4).send_keys("1")       #转换率
        # self.find(self._locat_commodityUnit5).click()       #销售单位
        # self.find(self._locat_commodityUnit5_right).click()
        # self.find(self._locat_commodityUnit5_choose).click()
        # self.find(self._locat_conversionRate5).send_keys("1")       #转换率
        """
        料品分类
        """
        self.find(self._locat_commodityType).click()
        self.find(self._locat_classifyAttribution).click()      #分类归属
        self.find(self._locat_classifyAttribution_choose).click()
        self.find(self._locat_commodityTypeCode).send_keys("COMMODITY_KIND")        #主分类
        sleep(1)
        self.find(self._locat_oneClassifyCode).send_keys("B")       #一级分类
        sleep(1)
        self.find(self._locat_secondeClassifyCode).send_keys("B-SW")        #二级分类
        sleep(1)
        # self.find(self._locat_thirdClassifyCode).send_keys("")      #三级分类
        # self.find(self._locat_fourthClassifyCode).send_keys("")     #四级分类
        self.find(self._locat_add).click()
        self.find(self._locat_classifyAttribution2).click()
        self.find(self._locat_classifyAttribution2_choose1).click()
        self.find(self._locat_commodityTypeCode2).send_keys("PURCHASE_TYPE")
        sleep(1)
        self.find(self._locat_oneClassifyCode2).send_keys("B")
        sleep(1)
        self.find(self._locat_secondeClassifyCode2).send_keys("B-SW")
        """
        管理维度
        """






