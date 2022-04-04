import pytest
from selenium import webdriver

@pytest.mark.usefixtures("setup")
class TestStart:
    def test_title(self):
        assert "My Store" == self.driver.title