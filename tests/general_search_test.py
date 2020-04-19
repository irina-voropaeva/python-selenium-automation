import inspect

from pytest import fixture

from tests.BaseTest import BaseTest


class TestGeneralSearch(BaseTest):
    def test_clear_search_field(self):
        self.config.log().info(inspect.currentframe().f_code.co_name + " test started")
        search_text = "my job"

        search_field_value = self.search_block.enter_job(search_text)\
            .click_job_field_clear_button()\
            .get_search_field_value()

        assert len(search_field_value) is 0

    def test_clear_city_field(self):
        self.config.log().info(inspect.currentframe().f_code.co_name + " test started")

        city_field_value = self.search_block.click_city_field()\
            .click_city_field_clear_button()\
            .get_city_field_value()

        assert len(city_field_value) is 0

    def test_advanced_search_can_be_clicked(self):
        self.config.log().info(inspect.currentframe().f_code.co_name + " test started")

        self.search_block.click_advanced_search()\
            .is_advanced_search_filters_shown()
