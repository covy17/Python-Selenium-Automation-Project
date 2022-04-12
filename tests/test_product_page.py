import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.homepage import Homepage
from pages.search_results_page import SearchResultsPage

@pytest.mark.usefixtures("setup")
class TestProductPage:
    def test_add_item_from_product_page(self):
        pass
    
    def test_add_multiple_items_from_product_page(self):
        pass
    
    def test_add_different_sized_item_from_product_page(self):
        pass
    
    def test_add_different_colored_item_from_product_page(self):
        pass
    