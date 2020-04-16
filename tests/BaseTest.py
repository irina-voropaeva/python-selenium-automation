from pytest import fixture
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdrivermanager import EdgeDriverManager

from config.config import Config
from pageObjects.SearchBlock import SearchBlock


class BaseTest:
    base_url = "https://www.work.ua/"
    browser = Config().get_config()["browser"]
    log = Config().logger

    def setup_method(self):
        self.set_browser()

        self.driver.get(self.base_url)
        self.search_block = SearchBlock(self.driver)

    def teardown_method(self, test_method):
        self.driver.close()

    def set_browser(self):
        if self.browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif self.browser == "edge":
            self.driver = webdriver.Edge(executable_path="../drivers/msedgedriver.exe")
        else:
            raise ValueError("Invalid browser type")
