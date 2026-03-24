import time
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 2000);")
        time.sleep(2)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def get_scroll_position(self):
        return self.driver.execute_script("return window.pageYOffset;")

    def scroll_to_footer_and_measure_time(self, timeout=15):
        start_time = time.time()

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time > timeout:
                return False, elapsed_time  # Не дійшли до футера

            try:
                footer = self.driver.find_element(By.TAG_NAME, "footer")
                is_in_viewport = self.driver.execute_script(
                    "var rect = arguments[0].getBoundingClientRect();"
                    "return (rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight));",
                    footer
                )

                if is_in_viewport:
                    return True, elapsed_time
            except:
                pass

            self.driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(0.5)