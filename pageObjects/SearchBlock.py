from selenium.webdriver.common.by import By

from pageObjects.AdvancedSearchFiltersBlock import AdvancedSearchFiltersBlock
from pageObjects.BasePage import BasePage
from pageObjects.SearchResultsPage import SearchResultsPage


class SearchLocators:
    LOCATOR_JOB_FIELD = (By.ID, "search")
    LOCATOR_CITY_FIELD = (By.XPATH, "//input[@placeholder=\"Місто\"]")
    LOCATOR_SEARCH_BUTTON = (By.ID, "sm-but")
    LOCATOR_JOB_CLEAR_BUTTON = (By.CLASS_NAME, "link-close")
    LOCATOR_CITY_CLEAR_BUTTON = (By.XPATH, "//a[contains(@class, \"link-close\") and contains(@class, "
                                           "\"js-region-reset\")]")
    LOCATOR_ADVANCED_SEARCH = (By.ID, "adv-search")
    LOCATOR_CITY_KHERSON = (By.XPATH, "//li[text()=\"Херсон\"]")


class SearchBlock(BasePage):

    def enter_job(self, word):
        search_field = self.find_element(SearchLocators.LOCATOR_JOB_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return self

    def click_city_field(self):
        self.find_element(SearchLocators.LOCATOR_CITY_FIELD) \
            .click()
        return self

    def choose_city_kherson(self):
        self.find_element(SearchLocators.LOCATOR_CITY_KHERSON, time=2) \
            .click()
        return self

    def click_job_field(self):
        self.find_element(SearchLocators.LOCATOR_JOB_FIELD) \
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
        return self.find_element(SearchLocators.LOCATOR_JOB_FIELD, time=2) \
            .text

    def get_city_field_value(self):
        return self.find_element(SearchLocators.LOCATOR_CITY_FIELD, time=2) \
            .text

    def click_advanced_search(self):
        self.find_element(SearchLocators.LOCATOR_ADVANCED_SEARCH, time=2)\
            .click()
        return AdvancedSearchFiltersBlock(self.driver)

    def is_title_for_empty_job_and_city_correct(self):
        russian_title = "вакансий в Украине. Поиск вакансий и работы"
        ukrainian_title = "вакансій в Україні. Пошук вакансій і роботи"

        if self.language == "ua":
            if self.driver.title.__contains__(ukrainian_title):
                return True
        if self.language == "ru":
            if self.driver.title.__contains__(russian_title):
                return True
        return False

    def is_title_for_empty_job_and_default_city_correct(self):
        russian_title = "Работа в "
        ukrainian_title = "Робота у"

        if self.language == "ua":
            if self.driver.title.__contains__(ukrainian_title):
                return True
        if self.language == "ru":
            if self.driver.title.__contains__(russian_title):
                return True
        return False

    def is_title_for_empty_job_and_kherson_city_correct(self):
        russian_title = "Херсон"
        ukrainian_title = "Херсон"

        if self.language == "ua":
            if self.driver.title.__contains__(ukrainian_title):
                return True
        if self.language == "ru":
            if self.driver.title.__contains__(russian_title):
                return True
        return False