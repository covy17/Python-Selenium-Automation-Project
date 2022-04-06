import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.homepage import Homepage
from pages.search_results_page import SearchResultsPage

@pytest.mark.usefixtures("setup")
class TestHomepage:
    
    def test_search_feature_valid(self):
        expected_search_results = ["Printed Summer Dress", "Printed Dress", "Printed Chiffon Dress", 
                                   "Printed Summer Dress", "Printed Dress",]
        self.homepage = Homepage(self.driver, self.wait)
        self.search_results_page = SearchResultsPage(self.driver, self.wait)
        self.homepage.go_to_page("homepage")
        self.homepage.search_for_items("Printed")
        actual_search_results = self.search_results_page.get_search_results()
        assert actual_search_results == expected_search_results