import re

from pages.base_page import BasePage
from pages.elements import *

import allure
from selenium.webdriver.support.ui import Select

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self, url):
        with allure.step(f"Открываем браузер по ссылке - {url}"):
            self.browser.get(url)

    def scroll(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def quit(self):
        with allure.step("Закрываем браузер"):
            self.browser.quit()

    def nameInput(self):
        name = self.find(NAMEINPUT[0], NAMEINPUT[1])
        self.scroll(name)
        with allure.step("Поиск поле для ввода имени"):
            return name

    def nameInput_send(self, text):
        with allure.step("Ввод текста в поле имени"):
            return self.nameInput().send_keys(text)

    def passwordInput(self):
        passw = self.find(PASSWORDINPUT[0], PASSWORDINPUT[1])
        self.scroll(passw)
        with allure.step("Поиск поле для пароля"):
            return passw

    def passwordInput_send(self, text):
        with allure.step("Ввод пароля"):
            return self.passwordInput().send_keys(text)

    def checkbox1(self):
        check1 = self.find(CHECKBOX1[0], CHECKBOX1[1])
        self.scroll(check1)
        with allure.step("Ищем первую нужную ячейку"):
            return check1

    def checkbox1_click(self):
        with allure.step("Нажимаем первую нужную ячейку"):
            return self.checkbox1().click()

    def checkbox2(self):
        check2 = self.find(CHECKBOX2[0], CHECKBOX2[1])
        self.scroll(check2)
        with allure.step("Ищем вторую нужную ячейку"):
            return check2

    def checkbox2_click(self):
        with allure.step("Нажимаем на вторую нужную ячейку"):
            return self.checkbox2().click()

    def radio1(self):
        radio1 = self.find(RADIO1[0], RADIO1[1])
        self.scroll(radio1)
        with allure.step("Ищем радиоячейку"):
            return radio1

    def radio1_click(self):
        with allure.step("Нажимаем на радиоячейку"):
            return self.browser.execute_script("arguments[0].click();", self.radio1())

    def select(self):
        select1 = self.find(SELECT[0], SELECT[1])
        self.scroll(select1)
        with allure.step("Ищем поле с выбором"):
            return select1

    def select_click(self):
        with allure.step("Выбираем нужный пункт"):
            return Select(self.select()).select_by_value('yes')

    def email(self):
        email1 = self.find(EMAILINPUT[0], EMAILINPUT[1])
        self.scroll(email1)
        with allure.step("Ищем поле для ввода почты"):
            return email1

    def email_send(self, mail):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, mail):
            with allure.step("Вводим почту, прошедший валидацию"):
                return self.email().send_keys(mail)
        else:
            with allure.step("Почта у нас не прошла валидацию на формат name@example.com"):
                raise ValueError(f'Ваша почта - {mail} не соответствует формату name@example.com')

    def message(self):
        mess = self.find(MESSAGE[0], MESSAGE[1])
        self.scroll(mess)
        with allure.step("Ищем поле для сообщенй"):
            return mess

    def send_longest(self):
        lst = self.find_elements_texts(LIST[0], LIST[1])
        texts = [element.text for element in lst]
        texts = sorted(texts, key=lambda x: len(x))
        with allure.step("Вводим нужный текст в поле сообщений"):
            return self.message().send_keys(texts[-1])

    def submit(self):
        submitButton = self.find(SUBMIT[0], SUBMIT[1])
        self.scroll(submitButton)
        with allure.step("Ищем кнопку подтвердить"):
            return submitButton

    def submit_click(self):
        with allure.step("Подтверждаем"):
            return self.browser.execute_script("arguments[0].click();", self.submit())

    def check_state_alert(self):
        alert = self.browser.switch_to.alert
        with allure.step("Проверяем какой текст выпал из Alert"):
            return alert.text

    def check_alert(self):
        try:
            alert = self.browser.switch_to.alert
            with allure.step("Нам выпал алерт"):
                return True
        except:
            with allure.step("Нам алерт не выпал, тест относится к негативному тест кейсу"):
                return False