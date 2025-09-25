from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from utils import scroll
import time

browser = webdriver.Chrome()
link = "https://practice-automation.com/form-fields/"
browser.get(link)
browser.implicitly_wait(15)


# Дадим странице время полностью загрузиться
wait = WebDriverWait(browser, 3)

def test_try():
    name_field = wait.until(
        EC.presence_of_element_located((By.ID, "name-input"))
    )
    scroll(browser, name_field)
    name_field.clear()
    name_field.send_keys("MAX!!!")

    password_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    scroll(browser, password_input)
    password_input.clear()
    password_input.send_keys("12345678")

    milkPick = wait.until(
        EC.presence_of_element_located((By.ID, "drink2"))
    )
    scroll(browser, milkPick)
    milkPick.click()

    Coffee = wait.until(
        EC.presence_of_element_located((By.ID, "drink3"))
    )
    scroll(browser, Coffee)
    Coffee.click()

    radioYellow = wait.until(
        EC.presence_of_element_located((By.ID, "color3"))
    )
    scroll(browser, radioYellow)
    browser.execute_script("arguments[0].click();", radioYellow)

    selectList = wait.until(
        EC.presence_of_element_located((By.ID, "automation"))
    )
    scroll(browser, selectList)
    selectList = Select(selectList)
    selectList.select_by_value('yes')

    email = wait.until(
        EC.presence_of_element_located((By.ID, "email"))
    )

    email.send_keys("name@example.com")

    a = browser.find_elements(By.TAG_NAME, "li")
    texts = [element.text for element in a]
    texts = sorted(texts, key=lambda x: len(x))

    message_input = wait.until(
        EC.presence_of_element_located((By.ID, "message"))
    )
    scroll(browser, message_input)
    message_input.clear()
    message_input.send_keys(texts[-1])

    button = wait.until(
        EC.presence_of_element_located((By.ID, "submit-btn"))
    )
    scroll(browser, button)
    browser.execute_script("arguments[0].click();", button)

    alert = wait.until(
        EC.alert_is_present(),
    )
    assert alert.text == "Message received!"
