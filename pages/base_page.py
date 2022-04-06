from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
        
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.__url_dict = {
        "homepage" : "http://automationpractice.com/index.php",
        "login_page" : "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    }

    def go_to_page(self, url):
        self.driver.get(self.__url_dict[url])