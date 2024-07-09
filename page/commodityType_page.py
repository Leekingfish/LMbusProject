from selenium.webdriver.common.by import By
from page.base_page import BasePage


class CommodityTypePage(BasePage):

    _locat_iframe = (By.CSS_SELECTOR,"#tabPages > div.tabs-panels.tabs-panels-noborder.panel-noscroll > div:nth-child(3) > div > iframe")


    def commodityType_add(self):
        pass

    def commodityType_change(self):
        pass