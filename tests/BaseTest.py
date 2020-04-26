import os
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from config.config import Config
from pageObjects.SearchBlock import SearchBlock


class BaseTest:
    base_url = "https://www.work.ua/"
    browser = Config().get_config()["browser"]
    config = Config()

    def setup_method(self):
        self.set_browser()

        self.driver.get(self.base_url)
        self.search_block = SearchBlock(self.driver)
        self.config.log().info("Setup for method done")

    def teardown_method(self, test_method):
        self.driver.quit()

        self.config.log().info("Teardown for method done")
        self.config.log().info("\n")

    def set_browser(self):
        if self.browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            self.config.log().info("Chrome has been chosen")
        elif self.browser == "edge":
            self.driver = webdriver.Edge(executable_path="D:\\ksu-python-selenium\\python-selenium-automation\\drivers\\MicrosoftWebDriver.exe")
            self.config.log().info("Edge has been chosen")
        else:
            self.config.log().info("Browser " + self.browser + " cannot be chosen")
            raise ValueError("Invalid browser type")
