from selenium import webdriver

class BasePage:

    def base(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)  # 不自动关闭浏览器
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("http://lmbussit.leemanpaper.com/main/login.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

