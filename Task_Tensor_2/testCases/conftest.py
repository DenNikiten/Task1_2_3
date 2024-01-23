from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()