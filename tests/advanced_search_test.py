from tests.BaseTest import BaseTest

driver = None


class TestAdvancedSearch(BaseTest):

    def setup_method(self):
        super().setup_method()
        global driver
        driver = self.driver

    def test_category_can_be_chosen(self):
        advanced_search = self.search_block\
            .click_advanced_search()\
            .choose_it_category()

        assert advanced_search.is_it_category_chosen() is False

    def test_employment_type_can_be_chosen(self):
        advanced_search = self.search_block \
            .click_advanced_search() \
            .choose_full_time_employment_type()

        assert advanced_search.is_fulltime_chosen() is True

    def test_salary_can_be_filtered_only_from(self):
        advanced_search = self.search_block \
            .click_advanced_search() \
            .choose_3000_from_salary()

        assert advanced_search.is_from_salary_3000() is True

    def test_salary_can_be_filtered_only_to(self):
        advanced_search = self.search_block \
            .click_advanced_search() \
            .choose_50000_to_salary()

        assert advanced_search.is_to_salary_50000() is True

    def salary_both_filters_can_be_used_simultaneously(self):
        advanced_search = self.search_block \
            .click_advanced_search() \
            .choose_3000_from_salary() \
            .choose_50000_to_salary()

        assert advanced_search.is_from_salary_3000() is True
        assert advanced_search.is_to_salary_50000() is True

    def test_other_block_can_be_chosen(self):
        advanced_search = self.search_block \
            .click_advanced_search() \
            .choose_other_for_students()

        assert advanced_search.is_other_for_students_chosen() is True