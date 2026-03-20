from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):

    def open(self):
        self.driver.get("https://www.staff-clothes.com/parnyam/")

    @property
    def search_button(self):
        return self.driver.find_element(By.XPATH, "(//button[@class='header__icon-button'])[1]")

    @property
    def search_input(self):

        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='search__input']/input"))
        )

    def search_for_item(self, keyword):
        self.search_button.click()

        field = self.search_input
        field.clear()
        field.send_keys(keyword)

        field.send_keys(Keys.ENTER)

    @property
    def empty_search_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//*[contains(translate(text(), 'ВИЯВЛЕНО', 'виявлено'), 'виявлено') ]"))
        )