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
        self.product_page.wait_for_product_added_modal_to_appear()
        assert self.driver.find_element(By.XPATH, f"//h2[contains(.,  '{expected_message}')]")
    
    def test_add_multiple_items_from_product_page(self):
        expected_message = "Product successfully added to your shopping cart"
        expected_count = "3"
        self.homepage = Homepage(self.driver, self.wait)
        self.product_page = ProductPage(self.driver, self.wait)
        self.homepage.go_to_page('homepage')
        self.homepage.expand_item()
        self.product_page.increase_item_quantity(2)
        self.product_page.add_item_to_cart_from_product_page()
        self.product_page.wait_for_product_added_modal_to_appear()
        assert self.driver.find_element(By.XPATH, f"//h2[contains(.,  '{expected_message}')]")
        assert self.driver.find_element(By.ID, "layer_cart_product_quantity").text == expected_count
    
    def test_add_different_sized_item_from_product_page(self):
        size = "L"
        self.homepage = Homepage(self.driver, self.wait)
        self.product_page = ProductPage(self.driver, self.wait)
        self.homepage.go_to_page('homepage')
        self.homepage.expand_item()
        self.product_page.select_item_size("L")
        self.product_page.add_item_to_cart_from_product_page()
        self.product_page.wait_for_product_added_modal_to_appear()
        assert size in self.product_page.product_attribute_seperator()
    
    def test_add_different_colored_item_from_product_page(self):
        color = "Blue"
        self.homepage = Homepage(self.driver, self.wait)
        self.product_page = ProductPage(self.driver, self.wait)
        self.homepage.go_to_page('homepage')
        self.homepage.expand_item()
        self.product_page.select_item_color(color)
        self.product_page.add_item_to_cart_from_product_page()
        self.product_page.wait_for_product_added_modal_to_appear()
        assert color in self.product_page.product_attribute_seperator()

    
    def test_add_product_to_wish_list_not_logged_in(self):
        pass
    
    def test_add_prodcut_to_wish_list_logged_in(self):
        pass