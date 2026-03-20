import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage


class TestFooter:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_social_media_link_t111(self):
        home_page = HomePage(self.driver)

        home_page.open()

        actual_link = home_page.get_instagram_url()

        print(f"Знайдене посилання: {actual_link}")  # Виведемо в консоль для себе
        assert "instagram.com/staff_clothes" in actual_link, f"Посилання некоректне: {actual_link}"