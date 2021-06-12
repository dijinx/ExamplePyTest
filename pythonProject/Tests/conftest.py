import time

import pytest
from selenium import webdriver
from Config.config import TestData


@pytest.fixture(params=['chrome'], scope='class')
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield
    time.sleep(5)
    driver.quit()
