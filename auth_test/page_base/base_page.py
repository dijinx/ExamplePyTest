from const_user import const_user

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def check_url(self):
        url = self.driver.get_title()
        assert url == const_user.start_page
