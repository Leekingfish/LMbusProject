from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class DeliveryBooking(BasePage):

    _locat_add_details = (By.CSS_SELECTOR, '.datagrid-toolbar td:nth-child(1)')
    _locat_purchaseOrder = (By.CSS_SELECTOR,'[field="purchaseOrder"] .textbox-addon.textbox-addon-right')
    _locat_purchaseOrder_chosse = (By.ID, "datagrid-row-r14-1-4")
    _locat_purchaseId = (By.CSS_SELECTOR,'[field="purchaseId"] .textbox-addon.textbox-addon-right')
    _locat_purchaseId_chosse = (By.ID, 'datagrid-row-r15-1-0')
    _locat_originCode = (By.CSS_SELECTOR,'[field="originCode"] .textbox-addon.textbox-addon-right')
    _locat_originCode_choose = (By.ID, "datagrid-row-r14-1-0")
    _locat_commodityCode = (By.ID, '_easyui_textbox_input26')
    _locat_specificationCode = (By.CSS_SELECTOR,'[field="specificationCode"] .textbox-addon.textbox-addon-right')
    _locat_specificationCode_chosse = (By.ID,'datagrid-row-r16-1-0')
    _locat_carNumber = (By.CSS_SELECTOR, '[field="carNumber"] .textbox-text.validatebox-text.validatebox-invalid.eaf-validate-required.textbox-prompt')
    _locat_packQuantity = (By.CSS_SELECTOR,'[field="packQuantity"] .textbox-text.validatebox-text.eaf-validate-required')
    _locat_quantity = (By.CSS_SELECTOR, '[field="quantity"] .textbox-text.validatebox-text.eaf-validate-required')
    _locat_deliveryCarType = (By.CSS_SELECTOR,'[field="deliveryCarType"] .textbox-addon.textbox-addon-right')
    _locat_deliveryCarType_choose = (By.ID, "_easyui_combobox_i10_2")
    _locat_seve = (By.ID, "addSave")
    _locat_submit = (By.CSS_SELECTOR,'#editList > a:nth-child(7)')
    _locat_tip_window = (By.CSS_SELECTOR,'body > div.panel.window.messager-window > div.dialog-button.messager-button > a:nth-child(1)')
    _locat_accept = (By.CSS_SELECTOR,'#editList > a:nth-child(8) > span')

    def delivery_booking_banb(self):
        """
        竹木送货预约
        :return:
        """
        self.book_common()
        self.find(self._locat_add_details).click()  # 新增明细
        self.find(self._locat_originCode).click()  # 选择产地
        self.find(self._locat_originCode_choose).click()
        self.find(self._locat_commodityCode).send_keys("ZD0005")  # 选择料号
        sleep(1)
        self.find(self._locat_carNumber).send_keys("1")  # 车数
        self.find(self._locat_quantity).send_keys("5")  # 吨数
        self.find(self._locat_deliveryCarType).click()  # 选择车型
        self.find(self._locat_deliveryCarType_choose).click()
        self.find(self._locat_seve).click()  # 保存
        sleep(5)
        self.find(self._locat_submit).click()  # 提交
        self.find(self._locat_tip_window).click()
        sleep(3)
        self.find(self._locat_accept).click()  # 同意
        self.find(self._locat_tip_window).click()

    def delivery_booking_auxi(self):
        """
        辅料送货预约
        :return:
        """
        self.book_common()
        self.find(self._locat_add_details).click()  # 新增明细
        self.find(self._locat_purchaseOrder).click()  # 选择PO
        self.find(self._locat_purchaseOrder_chosse).click()
        self.find(self._locat_purchaseId).click()  # 选择采购员
        self.find(self._locat_purchaseId_chosse).click()
        self.find(self._locat_specificationCode).click()   #选择包装规格
        self.find(self._locat_specificationCode_chosse).click()
        self.find(self._locat_carNumber).send_keys("1")  # 车数
        self.find(self._locat_packQuantity).send_keys("2")  # 包数
        self.find(self._locat_quantity).send_keys("1000")  # 吨数
        self.find(self._locat_deliveryCarType).click()  # 选择车型
        self.find(self._locat_deliveryCarType_choose).click()
        self.find(self._locat_seve).click()  # 保存
        sleep(5)
        self.find(self._locat_submit).click()  # 提交
        self.find(self._locat_tip_window).click()
        sleep(3)
        self.find(self._locat_accept).click()  # 同意
        self.find(self._locat_tip_window).click()

    def delivery_booking_fuel(self):
        """
        燃料送货预约
        :return:
        """
        self.book_common()
        self.find(self._locat_add_details).click()  # 新增明细
        self.find(self._locat_purchaseOrder).click()  # 选择PO
        self.find(self._locat_purchaseOrder_chosse).click()
        self.find(self._locat_purchaseId).click()  # 选择采购员
        self.find(self._locat_purchaseId_chosse).click()
        self.find(self._locat_carNumber).send_keys("2")  # 车数
        self.find(self._locat_quantity).send_keys("5")  # 吨数
        self.find(self._locat_deliveryCarType).click()  # 选择车型
        self.find(self._locat_deliveryCarType_choose).click()
        self.find(self._locat_seve).click()  # 保存
        sleep(5)
        self.find(self._locat_submit).click()  # 提交
        self.find(self._locat_tip_window).click()
        sleep(3)
        self.find(self._locat_accept).click()  # 同意
        self.find(self._locat_tip_window).click()