import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.homepage import Homepage
from time import sleep
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.contact_us_page import ContactUsPage
from helper.file_helper import FileHelper

@pytest.mark.usefixtures("setup")
class TestContactUsPage:
    def test_send_valid_message(self):
        self.contactUsPage = ContactUsPage(self.driver, self.wait)
        self.fileHelper = FileHelper()
        file_path = self.fileHelper.get_relative_file_path("resources/homepage.png")
        self.contactUsPage.go_to_page("contact_us_page")
        self.contactUsPage.fill_in_contact_us_form_and_send("Customer service", "covytest@test.com", "123456789", 
                                                   file_path, "This is a test message")
        assert self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text() = 'Your message has been successfully sent to our team.']")))