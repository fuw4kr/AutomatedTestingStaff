import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.catalog_page import CatalogPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCatalog:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_sorting_cheap_to_expensive_t109(self):
        catalog_page = CatalogPage(self.driver)

        catalog_page.open()

        url_before = self.driver.current_url

        catalog_page.sort_from_cheap_to_expensive()

        url_after = self.driver.current_url

        assert url_before != url_after, "URL не змінився після сортування. Сортування не спрацювало."

    def test_filter_by_size_m_106(self):
        catalog_page = CatalogPage(self.driver)

        catalog_page.open()

        url_before = self.driver.current_url

        catalog_page.filter_by_size_m()

        url_after = self.driver.current_url

        assert url_before != url_after, "URL не змінився після кліку на розмір 'M'. Фільтр не працює!"