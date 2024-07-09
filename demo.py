from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By





def test_login():
    option = webdriver.ChromeOptions()
    # option.debugger_address = "127.0.0.1:9222"
    option.add_experimental_option("detach", True)  # 不自动关闭浏览器
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get("https://www.baidu.com/")
    driver.implicitly_wait(5)
    # driver.find_element(By.ID,"s-top-loginbtn").click()
    # driver.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("754605301@qq.com")
    # driver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("41028abcd")
    # driver.find_element(By.ID, "TANGRAM__PSP_11__isAgree").click()
    # driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()
    # sleep(5)
    # cookie = driver.get_cookies()
    # print(cookie)
    cookies = [
        {'domain': '.baidu.com', 'expiry': 1754968561, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'BhS2FnTmVYclB6Y1NkUWVVcUVyMVBQa0ZkUWp5YmF3QXQ3OGJsck43VHk1ckptSVFBQUFBJCQAAAAAAAAAAAEAAADALBY50rnYvJqI6O4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPJZi2byWYtmLT'},
        {'domain': '.baidu.com', 'expiry': 1720493490, 'httpOnly': False, 'name': 'BA_HECTOR', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'a1808k2580al2g80048l8g2h236ajl1j8ml1j1u'},
        {'domain': '.baidu.com', 'expiry': 1754968561, 'httpOnly': True, 'name': 'BDUSS_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'BhS2FnTmVYclB6Y1NkUWVVcUVyMVBQa0ZkUWp5YmF3QXQ3OGJsck43VHk1ckptSVFBQUFBJCQAAAAAAAAAAAEAAADALBY50rnYvJqI6O4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPJZi2byWYtmLT'},
        {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'BD_HOME', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'},
        {'domain': 'www.baidu.com', 'expiry': 1721272556, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '12314753'},
        {'domain': '.baidu.com', 'expiry': 1726622551, 'httpOnly': False, 'name': 'PSTM', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1692062552'},
        {'domain': '.baidu.com', 'expiry': 1720494926, 'httpOnly': False, 'name': 'BDORZ', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'FAE1F8CFA4E8841CC28A015FEAEE495D'},
        {'domain': '.baidu.com', 'expiry': 1726622551, 'httpOnly': False, 'name': 'BIDUPSID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '3A39F79CC00E65ED77F6FE2556D7AAFA'},
        {'domain': '.baidu.com', 'expiry': 1751944555, 'httpOnly': False, 'name': 'H_PS_PSSID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '60272_60378_60443'},
        {'domain': '.baidu.com', 'expiry': 1723598555, 'httpOnly': False, 'name': 'ZFY', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '9GK2aPb7MvFg4XxLvNMp2i2vy:ACRS4YNtAAy:AwkGe4A:C'},
        {'domain': '.baidu.com', 'expiry': 1751944556, 'httpOnly': False, 'name': 'BAIDUID_BFESS', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '3A39F79CC00E65ED77F6FE2556D7AAFA:FG=1'}
    ]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()






