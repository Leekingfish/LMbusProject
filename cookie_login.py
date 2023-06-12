import yaml
from selenium import webdriver


def test_cookie_login():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)  # 不自动关闭浏览器
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(5)
    driver.get("http://lmbussit.leemanpaper.com/main/login.html")
    driver.maximize_window()
    with open("./data.yaml",encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get("http://lmbussit.leemanpaper.com/main/index.html")