import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait

    yield driver, wait
    driver.close()