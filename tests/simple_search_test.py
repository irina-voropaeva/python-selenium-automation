from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from pageObjects.SearchBlock import SearchBlock
from tests.BaseTest import BaseTest


class TestSimpleSearch(BaseTest):

    def test_search_with_entered_job_default_city(self):
        search_text = "qa engineer"

        self.search_block\
            .enter_job(search_text)\
            .click_on_the_search_button()

        assert search_text in self.driver.title

    def test_search_with_empty_job_and_default_city(self):

        self.search_block\
            .click_on_the_search_button()

        assert self.search_block.is_title_for_empty_job_and_default_city_correct() is True

    def test_search_with_empty_job_and_kherson_city(self):

        self.search_block\
            .click_city_field()\
            .choose_city_kherson()\
            .click_on_the_search_button()

        assert self.search_block.is_title_for_empty_job_and_kherson_city_correct() is True

    def test_search_with_empty_both_fields(self):

        self.search_block\
            .click_city_field()\
            .click_city_field_clear_button()\
            .click_on_the_search_button()

        assert self.search_block.is_title_for_empty_job_and_city_correct() is True



