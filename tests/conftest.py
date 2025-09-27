from selenium import webdriver
import pytest

# Сделал для хрома, надо будет добавить еще доп браузеры
@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser