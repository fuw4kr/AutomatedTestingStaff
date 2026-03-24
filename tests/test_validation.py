import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

class TestValidation:
    def setup_method(self):
        options = uc.ChromeOptions()

        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.driver = uc.Chrome(options=options)
        self.driver.implicitly_wait(15)

    def teardown_method(self):
        self.driver.quit()

    def test_minimum_password_length_t119(self):
        login_page = LoginPage(self.driver)

        login_page.open()

        login_page.fill_registration_with_short_password("123")

        error_displayed = login_page.is_password_error_displayed()

        assert error_displayed, "Помилка! Система пропустила закороткий пароль, повідомлення не з'явилося."

    def test_valid_registration_data_t118(self):
        login_page = LoginPage(self.driver)

        login_page.open()

        login_page.fill_valid_registration()

        has_errors = login_page.is_any_validation_error_displayed()

        assert not has_errors, "Знайдено помилку валідації! Дані не прийняті фронтендом."

    def test_letters_in_phone_field_t110(self):
        login_page = LoginPage(self.driver)

        login_page.open()

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        import time

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header__profile-links"))
        )
        self.driver.execute_script("document.querySelector('.header__profile-links').previousElementSibling.click();")
        time.sleep(2)

        login_page.registration_button.click()
        time.sleep(1.5)

        phone_el = login_page.phone_input
        phone_el.click()
        phone_el.send_keys("АвтоматизаціяQA")
        time.sleep(1)

        actual_value = phone_el.get_attribute("value")
        print(f"Значення в полі після вводу літер: '{actual_value}'")

        assert "АвтоматизаціяQA" not in actual_value, "БАГ! Поле телефону дозволяє вводити літери!"
        assert actual_value in ["", "+38", "+380"], f"В полі з'явився неочікуваний текст: {actual_value}"