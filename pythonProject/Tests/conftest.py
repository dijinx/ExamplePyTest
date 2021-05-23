import time

import pytest
from selenium import webdriver
from Config.config import TestData


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        # сюда можно вложить переменную с путём до драйвера  к эксекьютбл пат
        driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == 'firefox':
        # сюда можно вложить переменную с путём до драйвера
        driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    time.sleep(5)
    driver.quit()
