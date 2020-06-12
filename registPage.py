import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class registPage:
    def __int__(self, driver: WebDriver):
        self._driver = driver
        self._driver.implicitly_wait(2)

    def regist(self):
        self._driver.find_element(By.ID, 'corp_name').send_keys('lifeng')
        self._driver.find_element(By.ID, 'manager_name').send_keys('DIKEHA')

        self._driver.quit()
        return True
