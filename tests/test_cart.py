import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCart:
    def setup_method(self):
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')

        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--accept-lang=uk-UA,uk')

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': '''
                        Object.defineProperty(navigator, 'webdriver', {
                          get: () => undefined
                        })
                    '''
        })

        self.driver.implicitly_wait(15)

    def teardown_method(self):
        self.driver.quit()

    def test_add_item_to_cart_t107(self):
        product_page = ProductPage(self.driver)
        product_page.open()
        print(f"\nДІАГНОСТИКА - Заголовок сторінки: {self.driver.title}")
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

    def test_cart_persistence_after_refresh_114(self):
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)

        product_page.open()
        product_page.add_item_and_go_to_cart()

        WebDriverWait(self.driver, 10).until(EC.url_contains("cart"))

        self.driver.refresh()
        import time
        time.sleep(4)

        assert "cart" in self.driver.current_url, "Після оновлення нас викинуло з кошика!"

        try:
            is_empty = cart_page.empty_cart_message.is_displayed()
        except:
            is_empty = False

        assert not is_empty, "РЕАЛЬНИЙ БАГ! Кошик очистився після оновлення сторінки (F5)!"

    def test_add_max_quantity_t117(self):
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)

        product_page.open()
        product_page.add_item_and_go_to_cart()

        WebDriverWait(self.driver, 10).until(EC.url_contains("cart"))

        clicks_made = cart_page.increase_quantity_to_max()
        print(f"\nВдалося додати товар {clicks_made + 1} разів (1 початковий + {clicks_made} кліків).")

        plus_btn = cart_page.plus_button
        is_disabled = plus_btn.get_attribute("disabled") is not None

        assert is_disabled or clicks_made < 30, f"БАГ! Система дозволяє додавати нескінченну кількість товару! Зроблено {clicks_made} кліків."