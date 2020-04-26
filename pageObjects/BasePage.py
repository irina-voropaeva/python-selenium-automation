from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from config.config import Config
from pageObjects.LanguageChooser import LanguageChooser


class BasePage:
    language = Config().get_config()["language"]
    config = Config()

    def __init__(self, driver):
        self.driver = driver
        language_choose = LanguageChooser(driver, self)
        if self.language == "ua":
            language_choose.choose_ua()
        elif self.language == "ru":
            language_choose.choose_ru()
        else:
            raise ValueError("Invalid language in config")


    def find_element(self, locator, time=10):
        self.config.log().info("Finding element by locator")
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_clickable_element(self, locator, time=10):
        self.config.log().info("Finding element by clickable locator")
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        self.config.log().info("Finding elements")
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, url):
        self.config.log().info("Go to site " + url)
        return self.driver.get(url)
