from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):

    def open(self):
        self.driver.get("https://www.staff-clothes.com/m/new-products/")

    @property
    def first_product(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(@class, 'product-card__info--title')])[1]"))
        )

    @property
    def size_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='29' or text()='30' or text()='S' or text()='M']"))
        )

    @property
    def add_to_cart_button(self):
        # СКРИНШОТ 1: Ідеальний стабільний локатор за ID!
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "order-btn"))
        )

    @property
    def go_to_cart_modal_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Перейти до кошика']"))
        )

    def add_item_and_go_to_cart(self):
        self.first_product.click()

        self.size_button.click()

        self.add_to_cart_button.click()

        self.go_to_cart_modal_button.click()