import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login_successfully(self):
        self.login_page = LoginPage(self.driver, self.wait)
        self.login_page.go_to_login_page()
        self.login_page.enter_valid_login()
        assert self.wait.until(EC.visibility_of_element_located((By.ID, "my-account")))