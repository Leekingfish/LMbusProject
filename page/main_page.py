from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.delivery_booking_page import DeliveryBooking


class MainPage(BasePage):
    _locat_purchase = (By.CSS_SELECTOR, '.float_l.nav_cont.nav_text[title="采购管理"]')
    _locat_delivery = (By.CSS_SELECTOR, '.system.float_r[title="预约送货"]')
    _locat_delivery2 = (By.CSS_SELECTOR, '.system_setting.middle_left[title="送货预约"]')
    def goto_purchase_management(self):
        """
        跳转送货预约
        :return:
        """
        self.find(self._locat_purchase).click()
        self.find(self._locat_delivery).click()
        sleep(1)
        self.find(self._locat_delivery2).click()
        sleep(1)
        return  DeliveryBooking(self.driver)

