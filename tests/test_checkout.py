import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.checkout_page import CheckoutPage
from selenium.webdriver.chrome.options import Options
import time


class TestCheckout:
    def setup_method(self):
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--window-size=1920,1080')

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        options.add_argument('--accept-lang=uk-UA,uk')

        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
        options.add_argument('--disable-blink-features=AutomationControlled')

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.implicitly_wait(15)

    def teardown_method(self):
        self.driver.quit()

    def test_invalid_phone_quick_order_113(self):
        checkout_page = CheckoutPage(self.driver)

        self.driver.get(
            "https://www.staff-clothes.com/product/tah0739/")
        time.sleep(3)

        print("\nПробуємо замовити з номером +38045454...")
        checkout_page.process_quick_order_with_bad_phone(bad_phone="38045454")

        has_error = checkout_page.is_phone_error_displayed()

        assert has_error, "БАГ! Система прийняла некоректний номер телефону в Швидкому Замовленні!"