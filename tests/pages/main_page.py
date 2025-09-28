from pages.base_page import BasePage
from pages.elements import *
from selenium.webdriver.support.ui import Select

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://practice-automation.com/form-fields/")

    def scroll(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def quit(self):
        self.browser.quit()

    def nameInput(self):
        name = self.find(NAMEINPUT[0], NAMEINPUT[1])
        self.scroll(name)
        return name

    def nameInput_send(self, text):
        return self.nameInput().send_keys(text)

    def passwordInput(self):
        passw = self.find(PASSWORDINPUT[0], PASSWORDINPUT[1])
        self.scroll(passw)
        return passw

    def passwordInput_send(self, text):
        return self.passwordInput().send_keys(text)

    def checkbox1(self):
        check1 = self.find(CHECKBOX1[0], CHECKBOX1[1])
        self.scroll(check1)
        return check1

    def checkbox1_click(self):
        return self.checkbox1().click()

    def checkbox2(self):
        check2 = self.find(CHECKBOX1[0], CHECKBOX1[1])
        self.scroll(check2)
        return check2

    def checkbox2_click(self):
        return self.checkbox2().click()

    def radio1(self):
        radio1 = self.find(RADIO1[0], RADIO1[1])
        self.scroll(radio1)
        return radio1

    def radio1_click(self):
        return self.browser.execute_script("arguments[0].click();", self.radio1())

    def select(self):
        select1 = self.find(SELECT[0], SELECT[1])
        self.scroll(select1)
        return select1

    def select_click(self):
        return Select(self.select()).select_by_value('yes')

    def email(self):
        email1 = self.find(EMAILINPUT[0], EMAILINPUT[1])
        self.scroll(email1)
        return email1

    def email_send(self):
        return self.email().send_keys(EMAILEXAMPLE)

    def message(self):
        mess = self.find(MESSAGE[0], MESSAGE[1])
        self.scroll(mess)
        return mess

    def send_longest(self):
        lst = self.find_elements_texts(LIST[0], LIST[1])
        texts = [element.text for element in lst]
        texts = sorted(texts, key=lambda x: len(x))
        return self.message().send_keys(texts[-1])

    def submit(self):
        submitButton = self.find(SUBMIT[0], SUBMIT[1])
        self.scroll(submitButton)
        return submitButton

    def submit_click(self):
        return self.browser.execute_script("arguments[0].click();", self.submit())

    def check_state_alert(self):
        alert = self.browser.switch_to.alert
        return alert.text

    def check_alert(self):
        try:
            alert = self.browser.switch_to.alert
            return True
        except:
            return False