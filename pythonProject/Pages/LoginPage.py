from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """локаторы"""
    LOGIN = (By.ID, 'phoneInput')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'submit')
    CHANGE_PHONE_NUMBER = (By.LINK_TEXT, 'Изменить номер телефона')
    """конструктор данного класса"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """действия на странице"""

    """это используется для получения названия страницы"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """это используется для получения текста со страницы"""
    def is_change_phone_link_exist(self):
        return self.is_visible(self.CHANGE_PHONE_NUMBER)

    """это используется для авторизации"""
    def do_login(self, user, password):
        self.do_send_keys(self.LOGIN, user)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)

