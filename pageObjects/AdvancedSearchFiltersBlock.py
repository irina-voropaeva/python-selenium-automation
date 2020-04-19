from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class AdvancedSearchLocators:
    LOCATOR_CATEGORY_SELECTION = (By.ID, "category_selection")
    LOCATOR_EMPLOYMENT_TYPE_SELECTION = (By.ID, "employment_selection")
    LOCATOR_OTHER_SELECTION = (By.XPATH, "//div[@class=\"form-group\"][3]")

    # IT, комп'ютери, інтернет
    LOCATOR_CATEGORY_IT_CHECKBOX_UA = (By.XPATH, "//div/label/a[text()=\"IT, комп\'ютери, інтернет\"]/ancestor::div/label/input")
    LOCATOR_CATEGORY_IT_CHECKBOX_RU = (By.XPATH, "//div/label/a[text()=\"IT, компьютеры, интернет\"]/ancestor::div/label/input")

    LOCATOR_EMPLOYMENT_TYPE_FULL_TIME_CHECKBOX_UA = (By.XPATH, "//div/label/span[text()=\"Повна зайнятість\"]/ancestor::div/label/input")
    LOCATOR_EMPLOYMENT_TYPE_FULL_TIME_CHECKBOX_RU = (By.XPATH, "//div/label/span[text()=\"Полная занятость\"]/ancestor::div/label/input")
    LOCATOR_OTHER_FOR_STUDENTS_CHECKBOX_RU_UA = (By.XPATH, "//div/label/span[text()=\"Студентам\"]/ancestor::div/label/input")

    LOCATOR_SALARY_FROM_SELECTION = (By.ID, "salaryfrom_selection")
    LOCATOR_SALARY_TO_SELECTION = (By.ID, "salaryto_selection")

    LOCATOR_SALARY_FROM_3000_OPTION = (By.XPATH, "//select[@id=\"salaryfrom_selection\"]/option[contains(text(), \"3 000\")]")
    LOCATOR_SALARY_TO_50000_OPTION = (By.XPATH, "//select[@id=\"salaryto_selection\"]/option[contains(text(), \"50 000\")]")


class AdvancedSearchFiltersBlock(BasePage):
    def choose_it_category(self):
        if self.language == "ua":
            self.find_clickable_element(AdvancedSearchLocators.LOCATOR_CATEGORY_IT_CHECKBOX_UA) \
                .click()
        elif self.language == "ru":
            self.find_clickable_element(AdvancedSearchLocators.LOCATOR_CATEGORY_IT_CHECKBOX_RU) \
                .click()
        else:
            return None
        return self

    def choose_full_time_employment_type(self):
        if self.language == "ua":
            self.find_clickable_element(AdvancedSearchLocators.LOCATOR_EMPLOYMENT_TYPE_FULL_TIME_CHECKBOX_UA) \
                .click()
        elif self.language == "ru":
            self.find_clickable_element(AdvancedSearchLocators.LOCATOR_EMPLOYMENT_TYPE_FULL_TIME_CHECKBOX_RU) \
                .click()
        else:
            return None
        return self

    def choose_other_for_students(self):
        self.find_clickable_element(AdvancedSearchLocators.LOCATOR_OTHER_FOR_STUDENTS_CHECKBOX_RU_UA) \
            .click()
        return self

    def choose_3000_from_salary(self):
        self.find_clickable_element(AdvancedSearchLocators.LOCATOR_SALARY_FROM_SELECTION) \
            .click()
        self.find_clickable_element(AdvancedSearchLocators.LOCATOR_SALARY_FROM_3000_OPTION)\
            .click()
        return self

    def choose_50000_to_salary(self):
        self.find_clickable_element(AdvancedSearchLocators.LOCATOR_SALARY_TO_SELECTION) \
            .click()
        self.find_clickable_element(AdvancedSearchLocators.LOCATOR_SALARY_TO_50000_OPTION)\
            .click()
        return self

    def is_it_category_chosen(self):
        if self.language == "ua":
            return self.find_clickable_element(AdvancedSearchLocators.LOCATOR_CATEGORY_IT_CHECKBOX_UA)\
                .is_selected()
        elif self.language == "ru":
            return self.find_clickable_element(AdvancedSearchLocators.LOCATOR_CATEGORY_IT_CHECKBOX_RU) \
                .is_selected()
        else:
            return None

    def is_fulltime_chosen(self):
        if self.language == "ua":
            return self.find_clickable_element(AdvancedSearchLocators.LOCATOR_EMPLOYMENT_TYPE_FULL_TIME_CHECKBOX_UA) \
                .is_selected()
        elif self.language == "ru":
            return self.find_clickable_element(AdvancedSearchLocators.LOCATOR_EMPLOYMENT_TYPE_FULL_TIME_CHECKBOX_RU) \
                .is_selected()
        else:
            return None

    def is_other_for_students_chosen(self):
        return self.find_clickable_element(AdvancedSearchLocators.LOCATOR_OTHER_FOR_STUDENTS_CHECKBOX_RU_UA) \
                .is_selected()

    def is_from_salary_3000(self):
        return self.find_clickable_element(AdvancedSearchLocators.LOCATOR_SALARY_FROM_SELECTION).text.__contains__("3 000")

    def is_to_salary_50000(self):
        return self.find_clickable_element(AdvancedSearchLocators.LOCATOR_SALARY_TO_SELECTION).text.__contains__("50 000")
