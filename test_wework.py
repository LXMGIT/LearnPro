from wework_test.mainPage import mainPage
import pytest

class TestRegist():

    def setup(self):
        self.mainPage = mainPage()

    def test_regist(self):
        self.mainPage.goto_regist().regist()