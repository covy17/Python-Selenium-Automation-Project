from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage

class ProductPage(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(
            driver, wait
            )

    def add_item_to_cart_from_product_page(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add to cart']"))).click()
