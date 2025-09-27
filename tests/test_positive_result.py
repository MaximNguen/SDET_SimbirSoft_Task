from pages.main_page import MainPage
import pytest

# Положительный тест кейс на рассмотрении несколько возможных исходов
class TestPositiveResult:
    @pytest.fixture(autouse=True)
    def main_page(self, browser):
        self.main_page = MainPage(browser)
        self.main_page.open()

    def test_fill_form_full(self):
        self.main_page.nameInput_send("Maxim")
        self.main_page.passwordInput_send("12345678")
        self.main_page.checkbox1_click()
        self.main_page.checkbox2_click()
        self.main_page.radio1_click()
        self.main_page.select_click()
        self.main_page.email_send()
        self.main_page.send_longest()
        self.main_page.submit_click()
        assert self.main_page.check_state_alert() == 'Message received!'

    def test_fill_only_required(self):
        self.main_page.nameInput_send("TestName")
        self.main_page.submit_click()
        assert self.main_page.check_state_alert() == 'Message received!'

    def test_fill_not_full(self): # Можно считать он лишним, раз у нас требует только Name, но добавляю, чтобы проверить работает ли скролл для элементов
        self.main_page.send_longest()
        self.main_page.nameInput_send("TestName")
        self.main_page.select_click()
        self.main_page.submit_click()
        assert self.main_page.check_state_alert() == 'Message received!'