from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time


class LoginPage(BasePage):

    def open(self):
        self.driver.get("https://www.staff-clothes.com/")
        time.sleep(3)

    @property
    def registration_button(self):
        visible_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(
                (By.XPATH, "//button[contains(translate(., 'РЕЄСТРАЦІЯ', 'реєстрація'), 'реєстрація')]"))
        )
        return visible_elements[0]

    @property
    def phone_input(self):
        visible_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//input[@type='tel']"))
        )
        return visible_elements[0]

    @property
    def name_input(self):
        visible_elements = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_any_elements_located(
                (By.XPATH, "//input[@type='text'] | //label[contains(., 'ПІБ')]/input"))
        )
        return visible_elements[0]

    @property
    def password_input(self):
        visible_elements = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//input[@type='password']"))
        )
        return visible_elements[0]

    @property
    def confirm_password_input(self):
        visible_elements = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//input[@type='password']"))
        )
        return visible_elements[1]

    @property
    def password_error_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(., '6 символів') or contains(., 'Пароль повинен')]"))
        )

    @property
    def terms_checkbox(self):
        # Локатор для галочки згоди
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'modal')]//label[@for='terms-of-use']"))
        )

    @property
    def submit_button(self):
        visible_elements = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_any_elements_located((By.XPATH,
                                                   "//div[contains(@class, 'modal')]//button[contains(translate(., 'ОТРИМАТИ', 'отримати'), 'отримати')]"))
        )
        return visible_elements[0]

    def fill_registration_with_short_password(self, short_pass="123"):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header__profile-links"))
        )
        self.driver.execute_script("document.querySelector('.header__profile-links').previousElementSibling.click();")
        time.sleep(2)

        self.registration_button.click()
        time.sleep(1.5)

        phone = self.phone_input
        phone.click()
        phone.send_keys("501234567")

        name = self.name_input
        name.click()
        name.send_keys("Тест Автоматизація")

        pwd = self.password_input
        pwd.click()
        pwd.send_keys(short_pass)

        pwd_confirm = self.confirm_password_input
        pwd_confirm.click()
        pwd_confirm.send_keys(short_pass)

        pwd_confirm.send_keys(Keys.TAB)
        time.sleep(1.5)

    def fill_valid_registration(self, phone="501112233", name="Крістіна Тест", valid_pass="StrongPass123!"):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header__profile-links"))
        )
        self.driver.execute_script("document.querySelector('.header__profile-links').previousElementSibling.click();")
        time.sleep(2)

        self.registration_button.click()
        time.sleep(1.5)

        phone_el = self.phone_input
        phone_el.click()
        phone_el.send_keys(phone)

        name_el = self.name_input
        name_el.click()
        name_el.send_keys(name)

        pwd_el = self.password_input
        pwd_el.click()
        pwd_el.send_keys(valid_pass)

        pwd_confirm_el = self.confirm_password_input
        pwd_confirm_el.click()
        pwd_confirm_el.send_keys(valid_pass)

        pwd_confirm_el.send_keys(Keys.TAB)
        time.sleep(1)

        checkbox = self.terms_checkbox
        actions = ActionChains(self.driver)
        actions.move_to_element(checkbox).click().perform()
        time.sleep(1.5)

    def is_password_error_displayed(self):
        try:
            return self.password_error_message.is_displayed()
        except:
            return False

    def is_submit_button_disabled(self):
        try:
            btn = self.submit_button
            return btn.get_attribute("disabled") is not None
        except:
            return True

    def is_any_validation_error_displayed(self):
        errors = self.driver.find_elements(By.XPATH,
                                           "//div[contains(@class, 'modal')]//*[contains(text(), 'Необхідно') or contains(text(), 'повинен') or contains(text(), 'формат')]")
        for err in errors:
            if err.is_displayed():
                return True
        return False