import pytest
from selenium import webdriver

@pytest.mark.usefixtures("setup")
class TestBase:
    def test_home_page_title(self):
        assert "My Store" == self.driver.title