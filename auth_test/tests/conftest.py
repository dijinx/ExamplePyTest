import time
import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
        driver.implicitly_wait(5)
        yield driver
        time.sleep(1)
        driver.quit()
    if request.param == 'firefox':
        driver = webdriver.Firefox(executable_path='C:\\geckodriver.exe')
        driver.implicitly_wait(5)
        yield driver
        time.sleep(1)
        driver.quit()
