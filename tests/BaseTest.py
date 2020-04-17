from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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
        self.log.info("Setup for method done")

    def teardown_method(self, test_method):
        self.driver.close()
        self.log.info("Teardown for method done")

    def set_browser(self):
        if self.browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            self.log.info("Chrome has been chosen")
        elif self.browser == "edge":
            self.driver = webdriver.Edge(executable_path="../drivers/msedgedriver.exe")
            self.log.info("Edge has been chosen")
        else:
            raise ValueError("Invalid browser type")
        self.log.info("Browser " + self.browser + " cannot be chosen")
