import pytest
from selenium import webdriver

def test_base():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert "Google" == driver.title