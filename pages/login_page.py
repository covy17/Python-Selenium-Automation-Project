from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(
            driver, wait
            )
        
    def go_to_login_page(self):
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        
    def enter_valid_login(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("covytest@test.com")
        self.driver.find_element(By.ID, "passwd").send_keys("Test1")
        self.driver.find_element(By.ID, "SubmitLogin").click()