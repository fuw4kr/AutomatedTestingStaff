import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCart:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_add_item_to_cart_t107(self):
        product_page = ProductPage(self.driver)
        product_page.open()
        product_page.add_item_and_go_to_cart()

        WebDriverWait(self.driver, 10).until(EC.url_contains("cart"))
        assert "cart" in self.driver.current_url

    def test_clear_cart_t108(self):
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)

        product_page.open()
        product_page.add_item_and_go_to_cart()

        WebDriverWait(self.driver, 10).until(EC.url_contains("cart"))

        cart_page.clear_entire_cart()

        assert cart_page.empty_cart_message.is_displayed()