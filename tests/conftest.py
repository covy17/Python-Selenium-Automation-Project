import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture()
def setup(request):
    print("initiating chrome driver")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait

    yield driver, wait
    driver.close()