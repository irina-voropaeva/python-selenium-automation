from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from pageObjects.SearchBlock import SearchBlock
from tests.BaseTest import BaseTest


class TestSimpleSearchUa(BaseTest):

    def test_search_with_entered_job_default_city(self):
        search_text = "qa engineer"

        self.search_block\
            .enter_job(search_text)\
            .click_on_the_search_button()

        assert search_text in self.driver.title

    def test_search_with_empty_job_and_default_city(self):

        self.search_block\
            .click_job_field_clear_button()\
            .click_on_the_search_button()

        assert search_text in self.driver.title

    def test_search_with_empty_both_fields(self):

        self.search_block\
            .click_job_field_clear_button()\
            .click_city_field_clear_button()\
            .click_on_the_search_button()

        assert search_text in self.driver.title



