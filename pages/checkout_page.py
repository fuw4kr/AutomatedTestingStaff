from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time


class CheckoutPage(BasePage):

    @property
    def quick_order_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "quick-order-btn"))
        )

    @property
    def name_input(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'custom-input')]//input[@type='text']"))
        )

    @property
    def phone_input(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='tel']"))
        )

    @property
    def size_dropdown(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'quickOrder-size-select')]"))
        )

    @property
    def first_size_option(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(@class, 'quickOrder-option')])[1]"))
        )

    @property
    def submit_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'modal__button--black')]"))
        )

    @property
    def phone_error_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[contains(@class, 'warning')] | //*[contains(., 'формат') and contains(., 'телефон')]"))
        )

    def process_quick_order_with_bad_phone(self, name="Тест Автоматизація", bad_phone="38045454"):
        btn = self.quick_order_button
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)

        try:
            dropdown = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'quickOrder-size-select')]"))
            )
            self.driver.execute_script("arguments[0].click();", dropdown)
            time.sleep(1)

            option = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "(//button[contains(@class, 'quickOrder-option')])[1]"))
            )
            self.driver.execute_script("arguments[0].click();", option)
            time.sleep(1)
            print("Розмір успішно обрано.")
        except:
            print("Цей товар не потребує вибору розміру. Йдемо далі.")
            pass

        n_input = self.name_input
        self.driver.execute_script("arguments[0].click();", n_input)
        n_input.send_keys(name)

        p_input = self.phone_input
        self.driver.execute_script("arguments[0].click();", p_input)
        p_input.send_keys(Keys.CONTROL + "a")
        p_input.send_keys(Keys.DELETE)
        p_input.send_keys(bad_phone)

        submit = self.submit_button
        self.driver.execute_script("arguments[0].click();", submit)
        time.sleep(2)

    def is_phone_error_displayed(self):
        try:
            return self.phone_error_message.is_displayed()
        except:
            return False