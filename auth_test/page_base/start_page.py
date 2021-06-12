from const_user import const_user
from page_base.base_page import BasePage


class StartPage(BasePage):

    def open_start_page(self):
        BasePage.open(self, const_user.start_page)

    def check_url(self):
        url = self.driver.current_url
        assert str(url) == 'http://the-internet.herokuapp.com/'
