from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.materials_page import MaterialsPage
from page.delivery_booking_page import DeliveryBooking
from page.supplier_page import SupplierPage


class MainPage(BasePage):
    _locat_purchase = (By.CSS_SELECTOR, '.float_l.nav_cont.nav_text[title="采购管理"]')
    _locat_delivery = (By.CSS_SELECTOR, '.system.float_r[title="预约送货"]')
    _locat_delivery2 = (By.CSS_SELECTOR, '.system_setting.middle_left[title="送货预约"]')
    _locat_systemSetting = (By.CSS_SELECTOR,'.float_l.nav_cont.nav_text[title="系统基础设置"]')
    _locat_commodityManagement = (By.CSS_SELECTOR, '.system.float_r[title="料品管理"]')
    _locat_materialsPage = (By.CSS_SELECTOR, '.system_setting.middle_left[title="料品信息维护"]')
    _locat_supplier = (By.CSS_SELECTOR,'.system.float_r[title="供应商"]')
    _locat_supplierInfor = (By.CSS_SELECTOR,'.system_setting.middle_left[title="供应商信息"]')


    def goto_purchase_management(self):
        """
        跳转送货预约
        :return:
        """
        self.find(self._locat_purchase).click()         #采购管理
        self.find(self._locat_delivery).click()         #预约送货
        sleep(1)
        self.find(self._locat_delivery2).click()        #送货预约
        sleep(1)
        return  DeliveryBooking(self.driver)

    def goto_materialsPage(self):
        """
        跳转料品信息维护
        :return:
        """
        self.find(self._locat_systemSetting).click()        #系统基础设置
        self.find(self._locat_commodityManagement).click()          #料品管理
        sleep(1)
        self.find(self._locat_materialsPage).click()            #料品信息维护
        sleep(1)
        return MaterialsPage(self.driver)

    def goto_supplierPage(self):
        """
        跳转供应商信息
        :return:
        """
        self.find(self._locat_systemSetting).click()        #系统基础设置
        self.find(self._locat_supplier).click()         #供应商
        sleep(1)
        self.find(self._locat_supplierInfor).click()         #供应商信息
        sleep(1)
        return SupplierPage(self.driver)



















