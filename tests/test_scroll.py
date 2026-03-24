import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

class TestScroll:
    def setup_method(self):
        options = uc.ChromeOptions()

        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.driver = uc.Chrome(options=options)
        self.driver.implicitly_wait(15)

    def teardown_method(self):
        self.driver.quit()

    def test_scroll_to_top_t112(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.scroll_down()

        assert home_page.get_scroll_position() > 0, "Сторінка не прокрутилася вниз!"

        btn = home_page.scroll_to_top_button
        self.driver.execute_script("arguments[0].click();", btn)

        time.sleep(2)

        final_position = home_page.get_scroll_position()
        print(f"Позиція після кліку: {final_position}")

        assert final_position < 100, f"Сторінка не повернулася вгору! Позиція: {final_position}"