from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class DeliveryBooking(BasePage):

    _locat_add_details = (By.CSS_SELECTOR, '.datagrid-toolbar td:nth-child(1)')
    _locat_origin = (By.CSS_SELECTOR,'[field="originCode"] .textbox-addon.textbox-addon-right')
    _locat_origin_choose = (By.ID, "datagrid-row-r14-1-0")
    _locat_material = (By.ID, '_easyui_textbox_input26')
    _locat_car = (By.ID, "_easyui_textbox_input27")
    _locat_weight = (By.ID, "_easyui_textbox_input28")
    _locat_car_type = (By.CSS_SELECTOR,'[field="deliveryCarType"] .textbox-addon.textbox-addon-right')
    _locat_car_type_choose = (By.ID, "_easyui_combobox_i10_2")
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
        self.wait_click(self._locat_origin)
        self.find(self._locat_origin).click()  # 选择产地
        self.wait_click(self._locat_origin_choose)
        self.find(self._locat_origin_choose).click()
        self.find(self._locat_material).send_keys("ZB0003")  # 选择料号
        sleep(1)
        self.find(self._locat_car).send_keys("1")  # 车数
        self.find(self._locat_weight).send_keys("5")  # 吨数
        self.find(self._locat_car_type).click()  # 选择车型
        self.find(self._locat_car_type_choose).click()
        self.find(self._locat_seve).click()  # 保存
        # self.wait_click(self._locat_submit)
        sleep(5)
        self.find(self._locat_submit).click()  # 提交
        self.find(self._locat_tip_window).click()
        # self.wait_click(self._locat_accept)
        sleep(3)
        self.find(self._locat_accept).click()  # 同意
        self.find(self._locat_tip_window).click()

    def delivery_booking_auxi(self):
        """
        辅料送货预约
        :return:
        """
