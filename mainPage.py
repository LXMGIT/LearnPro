import time

from selenium.webdriver.common.by import By
from wework_test.loginPage import loginPage
from wework_test.registPage import registPage
from selenium import  webdriver


class mainPage:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get("https://work.weixin.qq.com/")
        self._driver.implicitly_wait(3)

    def goto_login(self):
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return loginPage(self._driver)

    def goto_regist(self):
        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return registPage(self._driver)
