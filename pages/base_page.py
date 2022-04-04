from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
        
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
