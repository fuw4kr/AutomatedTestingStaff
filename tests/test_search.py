import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSearch:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_search_by_keyword_t105(self):
        home_page = HomePage(self.driver)

        # Кроки тесту
        home_page.open()
        home_page.search_for_item("Худі")

        # Чекаємо, поки в URL з'явиться слово 'search' або запит (до 5 секунд)
        WebDriverWait(self.driver, 5).until(EC.url_contains("search"))

        # Перевірка результату (Assert) - перевіряємо, що ми перейшли на сторінку пошуку
        assert "search" in self.driver.current_url