from pytest import fixture
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.SearchBlock import SearchBlock


class BaseTest:
    base_url = "https://www.work.ua/"

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.get(self.base_url)
        self.search_block = SearchBlock(self.driver)

    def teardown_method(self, test_method):
        self.driver.close()
