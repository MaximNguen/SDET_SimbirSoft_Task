# Временно буду хранить всякие методы тут
from selenium.webdriver.support.ui import WebDriverWait

def scroll(browser, element):
    browser.execute_script("arguments[0].scrollIntoView();", element)
