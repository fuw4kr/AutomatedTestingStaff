import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc


class TestSearch:
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

    def test_search_by_keyword_t105(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.search_for_item("Худі")
        WebDriverWait(self.driver, 5).until(EC.url_contains("search"))
        assert "search" in self.driver.current_url

    @pytest.mark.xfail (reason="При вводі спецсимволів товар все рівно шукається.")
    def test_search_invalid_item_115(self):
        home_page = HomePage(self.driver)

        home_page.open()

        home_page.search_for_item("1=1")

        assert home_page.empty_search_message.is_displayed(), "Повідомлення про порожній пошук не з'явилося!"