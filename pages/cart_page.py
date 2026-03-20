from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):

    @property
    def clear_cart_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='ОЧИСТИТИ КОШИК' or text()='Очистити кошик']"))
        )

    @property
    def empty_cart_message(self):

        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//*[contains(translate(text(), 'НЕМАЄ ТОВАРІВ', 'немає товарів'), 'немає товарів')]"))
        )

    def clear_entire_cart(self):
        self.clear_cart_button.click()