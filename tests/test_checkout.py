import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.checkout_page import CheckoutPage
import time


class TestCheckout:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

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