import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc


class TestFooter:
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

    def test_social_media_link_t111(self):
        home_page = HomePage(self.driver)

        home_page.open()

        actual_link = home_page.get_instagram_url()

        print(f"\nЗнайдене посилання: {actual_link}")
        assert "instagram.com/staff_clothes" in actual_link, f"Посилання некоректне: {actual_link}"

    @pytest.mark.xfail(reason="Довга прокрутка до футера.")
    def test_footer_accessibility_time_116(self):
        home_page = HomePage(self.driver)

        print("\nПочинаємо скролити до футера (ліміт 15 секунд)...")

        is_reached, time_taken = home_page.scroll_to_footer_and_measure_time(timeout=15)

        if is_reached:
            print(f"Футер знайдено! Витрачено часу: {time_taken:.2f} секунд.")
        else:
            print(f"Футер недосяжний! Скролили {time_taken:.2f} секунд, але товари продовжують підвантажуватись.")

        assert is_reached, f"БАГ! До футера неможливо дістатися за 15 секунд (витрачено {time_taken:.2f} с)."