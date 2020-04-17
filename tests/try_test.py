from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from webdriver_manager.chrome import ChromeDriverManager

from tests.BaseTest import BaseTest


class TestMy(BaseTest):

    def test_my(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()
