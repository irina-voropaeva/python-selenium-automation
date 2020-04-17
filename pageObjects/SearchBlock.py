from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.SearchResultsPage import SearchResultsPage


class SearchLocators:
    LOCATOR_SEARCH_FIELD = (By.ID, "search")
    LOCATOR_CITY_FIELD = (By.XPATH, "//input[@placeholder=\"Місто\"]")
    LOCATOR_SEARCH_BUTTON = (By.ID, "sm-but")
    LOCATOR_JOB_CLEAR_BUTTON = (By.CLASS_NAME, "link-close")
    LOCATOR_CITY_CLEAR_BUTTON = (By.XPATH, "//a[contains(@class, \"link-close\") and contains(@class, "
                                           "\"js-region-reset\")]")
    LOCATOR_ADVANCED_SEARCH = (By.ID, "adv-search")


class SearchBlock(BasePage):

    def enter_job(self, word):
        search_field = self.find_element(SearchLocators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return self

    def click_city_field(self):
        self.find_element(SearchLocators.LOCATOR_CITY_FIELD) \
            .click()
        return self

    def click_on_the_search_button(self):
        self.find_element(SearchLocators.LOCATOR_SEARCH_BUTTON, time=2) \
            .click()
        return SearchResultsPage(self.driver)

    def click_job_field_clear_button(self):
        self.find_clickable_element(SearchLocators.LOCATOR_JOB_CLEAR_BUTTON, time=5) \
            .click()
        return self

    def click_city_field_clear_button(self):
        self.find_clickable_element(SearchLocators.LOCATOR_CITY_CLEAR_BUTTON, time=5) \
            .click()
        return self

    def get_search_field_value(self):
        return self.find_element(SearchLocators.LOCATOR_SEARCH_FIELD, time=2) \
            .text

    def get_city_field_value(self):
        return self.find_element(SearchLocators.LOCATOR_CITY_FIELD, time=2) \
            .text

    def click_advanced_search(self):
        return AdvancedSearchFiltersBlock(self.driver)
