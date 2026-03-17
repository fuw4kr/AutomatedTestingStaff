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
        # Кнопка-лупа, яку ми вже успішно знайшли раніше
        return self.driver.find_element(By.XPATH, "(//button[@class='header__icon-button'])[1]")

    @property
    def search_input(self):
        # Чекаємо до 10 секунд, поки поле не стане доступним.
        # Використовуємо точний XPath, спираючись на ваш скриншот:
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='search__input']/input"))
        )

    def search_for_item(self, keyword):
        # 1. Відкриваємо пошук
        self.search_button.click()

        # 2. Отримуємо поле (з очікуванням) і вводимо текст
        field = self.search_input
        field.clear()
        field.send_keys(keyword)

        # 3. Натискаємо Enter для підтвердження
        field.send_keys(Keys.ENTER)