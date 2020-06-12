import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from wework_test.registPage import registPage


class loginPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.implicitly_wait(2)

    def scan(self):
        pass

    def goto_regist(self):
        # time.sleep(3)
        self._driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return registPage(self._driver)
