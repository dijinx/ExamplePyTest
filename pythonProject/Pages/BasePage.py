from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# этот класс родитель для всех остальных классов сраниц
# он содержит все методы и утилиты для всех страниц

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.click()

    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)).send_keys(text)
        element.send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        element = WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return element


