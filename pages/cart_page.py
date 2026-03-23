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

    @property
    def plus_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[contains(text(), '+') or contains(@class, 'plus') or .//svg])[last()]"))
        )

    def increase_quantity_to_max(self):
        plus_btn = self.plus_button
        max_clicks = 30
        clicks = 0

        while clicks < max_clicks:
            if plus_btn.get_attribute("disabled") is not None:
                break

            try:
                self.driver.execute_script("arguments[0].click();", plus_btn)
                time.sleep(0.5)
                clicks += 1
            except:
                break

        return clicks

    def clear_entire_cart(self):
        self.clear_cart_button.click()