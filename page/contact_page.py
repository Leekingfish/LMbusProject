from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ContactPage(BasePage):
    _locat_btnQuery = (By.ID,'btnQuery')

    def get_docNo(self):
        self.find(self._locat_btnQuery).click()