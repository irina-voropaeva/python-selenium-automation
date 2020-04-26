from selenium.webdriver.common.by import By


class LanguageLocators:
    LOCATOR_HIDED_SELECT_LANGUAGE = (By.ID, "dropdownMenu100-2")
    LOCATOR_UA = (By.XPATH, "//a[text()=\"Українська\"]")
    LOCATOR_RU = (By.XPATH, "//a[text()=\"Русский\"]")

class LanguageChooser:
    def __init__(self, driver, base_page):
        self.driver = driver
        self.base_page = base_page
        self.base_page\
            .find_clickable_element(LanguageLocators.LOCATOR_HIDED_SELECT_LANGUAGE)\
            .click()

    def choose_ua(self):
        self.base_page\
            .find_clickable_element(LanguageLocators.LOCATOR_UA)\
            .click()

    def choose_ru(self):
        self.base_page \
            .find_clickable_element(LanguageLocators.LOCATOR_RU) \
            .click()
