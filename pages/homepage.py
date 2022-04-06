from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage

class Homepage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(
            driver, wait
            )
    
    def search_for_items(self, search_query):
        self.wait.until(EC.element_to_be_clickable((By.ID, "search_query_top"))).send_keys(search_query)
        self.driver.find_element(By.NAME, "submit_search").click()