from selenium.webdriver.common.by import By
from page.base_page import BasePage


class LoginPage(BasePage):

    def login(self):
        self.driver.find_element(By.ID, "_easyui_textbox_input1").send_keys("LM032451")
        self.driver.find_element(By.ID, "_easyui_textbox_input2").send_keys("L123456")
        self.driver.find_element(By.CSS_SELECTOR,"[style='margin-bottom:20px']:nth-child(3) .textbox-addon.textbox-addon-right").click()
        self.driver.find_element(By.ID, "orgCode_easyui_combobox_i1_6").click()
        self.driver.find_element(By.ID, "_easyui_textbox_input4").click()
        self.driver.find_element(By.CSS_SELECTOR,'.combobox-item.combobox-item-selected[id="chooseLanguage_easyui_combobox_i3_0"]').click()
        self.driver.find_element(By.ID, "btnLogin").click()

