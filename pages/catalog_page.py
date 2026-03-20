from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class CatalogPage(BasePage):

    def open(self):
        self.driver.get("https://www.staff-clothes.com/parnyam/odyag/verhniy-odyag/")

    @property
    def sort_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//button[text()='Сортування'] | //div[contains(@class, 'catalog__filter-section-switcher')]//button"))
        )

    @property
    def cheap_to_expensive_option(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//button[contains(@class, 'catalog__filter-option') and contains(text(), 'Від дешевих до дорогих')]"))
        )

    def sort_from_cheap_to_expensive(self):
        btn = self.sort_button
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        time.sleep(1)

        try:
            btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", btn)

        time.sleep(1.5)

        option = self.cheap_to_expensive_option
        try:
            option.click()
        except:
            self.driver.execute_script("arguments[0].click();", option)

        time.sleep(2)