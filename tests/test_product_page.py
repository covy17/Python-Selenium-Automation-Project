import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.homepage import Homepage
from time import sleep
from pages.product_page import ProductPage

@pytest.mark.usefixtures("setup")
class TestProductPage:
    def test_add_item_from_product_page(self):
        expected_message = "Product successfully added to your shopping cart"
        self.homepage = Homepage(self.driver, self.wait)
        self.product_page = ProductPage(self.driver, self.wait)
        self.homepage.go_to_page('homepage')
        self.homepage.expand_item()
        self.product_page.add_item_to_cart_from_product_page()
        self.wait.until(EC.visibility_of_element_located((By.ID, "layer_cart")))
        assert self.driver.find_element(By.XPATH, f"//h2[contains(.,  '{expected_message}')]")
    
    def test_add_multiple_items_from_product_page(self):
        pass
    
    def test_add_different_sized_item_from_product_page(self):
        pass
    
    def test_add_different_colored_item_from_product_page(self):
        pass
    