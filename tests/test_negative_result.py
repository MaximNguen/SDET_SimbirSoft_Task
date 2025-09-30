from pages.main_page import MainPage
import pytest

# Негативный тест кейс на рассмотрении несколько возможных исходов
class TestNegativeResult:
    @classmethod
    def setup_class(cls):
        print("\n========= Начало выполнения негативного тест-кейса ==========")

    @classmethod
    def teardown_class(cls):
        print("========= Конец выполнения негативного тест-кейса ==========")

    @pytest.fixture(autouse=True)
    def main_page(self, browser):
        self.main_page = MainPage(browser)
        self.main_page.open()
        yield self.main_page
        self.main_page.quit()

    @pytest.mark.parametrize("password,mail", [
        ("92138123", "normalMain@mail.ru"),
        ("jksdhasd", "213213.com"),
        ("hsad127327(@)*(][][;", "@gamil.cim"),
    ])
    def test_fill_form_without_name(self, password, mail):
        self.main_page.passwordInput_send(password)
        self.main_page.checkbox1_click()
        self.main_page.checkbox2_click()
        self.main_page.radio1_click()
        self.main_page.select_click()
        try:
            self.main_page.email_send(mail)
            if not self._is_valid_email(mail):
                pytest.fail(f"Почта {mail} не выдал ошибку при вводе неверного формата")
        except ValueError as a:
            print(f"Ожидаемое исключение для почты {mail}: {a}")
        self.main_page.send_longest()
        self.main_page.submit_click()
        assert self.main_page.check_alert() == False

    def test_fill_form_only_some(self):
        self.main_page.send_longest()
        self.main_page.submit_click()
        assert self.main_page.check_alert() == False

    def _is_valid_email(self, email): # пишем тут метод, потому что он только тут нужен
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is None