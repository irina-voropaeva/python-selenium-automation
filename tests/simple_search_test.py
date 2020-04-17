import inspect

from config.config import Config
from tests.BaseTest import BaseTest


class TestSimpleSearch(BaseTest):

    def test_search_with_entered_job_default_city(self):
        self.log.info(inspect.currentframe().f_code.co_name + " test started")

        search_text = "qa engineer"
        self.log.info("hello from test")
        self.search_block\
            .enter_job(search_text)\
            .click_on_the_search_button()

        assert search_text in self.driver.title

    def test_search_with_empty_job_and_default_city(self):
        self.log.info(inspect.currentframe().f_code.co_name + " test started")

        self.search_block\
            .click_on_the_search_button()

        assert self.search_block.is_title_for_empty_job_and_default_city_correct() is True

    def test_search_with_empty_job_and_choosed_kherson_city(self):
        self.log.info(inspect.currentframe().f_code.co_name + " test started")

        self.search_block\
            .click_city_field()\
            .choose_city_kherson()\
            .click_on_the_search_button()

        assert self.search_block.is_title_for_empty_job_and_kherson_city_correct() is True

    def test_search_with_empty_both_fields(self):
        self.log.info(inspect.currentframe().f_code.co_name + " test started")

        self.search_block\
            .click_city_field()\
            .click_city_field_clear_button()\
            .click_on_the_search_button()

        assert self.search_block.is_title_for_empty_job_and_city_correct() is True

    def test_search_with_empty_job_and_entered_kherson_city(self):
        self.log.info(inspect.currentframe().f_code.co_name + " test started")

        city = "Херсон"

        self.search_block\
            .click_city_field()\
            .click_city_field_clear_button()\
            .enter_city(city)\
            .click_on_the_search_button()

        assert self.search_block.is_title_for_empty_job_and_kherson_city_correct() is True



