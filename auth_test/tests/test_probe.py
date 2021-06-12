from page_base.start_page import StartPage
import pytest
import allure


@pytest.mark.smoke(order=1)
def test_probe(driver):
    start_page = StartPage(driver)

    start_page.open_start_page()


@allure.title('Тест проверяет заход на страницу')
@pytest.mark.user
@pytest.mark.smoke(order=2)
def test_probe1(driver):
    start_page = StartPage(driver)

    start_page.open_start_page()
    start_page.check_url()
