import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.catalog_page import CatalogPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc



class TestCatalog:
    def setup_method(self):
        options = uc.ChromeOptions()

        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        try:
            self.driver = uc.Chrome(options=options, version_main=145)
        except:

            self.driver = uc.Chrome(options=options)

        self.driver.implicitly_wait(15)

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