from pages.main_page import MainPage
import pytest

# Положительный тест кейс на рассмотрении несколько возможных исходов
class TestPositiveResult:
    @classmethod
    def setup_class(cls):
        print("\n========= Начало выполнения положительного тест-кейса ==========")

    @classmethod
    def teardown_class(cls):
        print("========= Конец выполнения положительного тест-кейса ==========")

    @pytest.fixture(autouse=True)
    def main_page(self, browser):
        self.main_page = MainPage(browser)
        self.main_page.open()
        yield self.main_page
        self.main_page.quit()

    @pytest.mark.parametrize("name,password", [
        ("maxim", "9012832"),
        ("pasha", "kasljdasds"),
        ("egor228443", "()*@)(#*!@*#)"),
    ])
    def test_fill_form_full(self, name, password):
        self.main_page.nameInput_send(name)
        self.main_page.passwordInput_send(password)
        self.main_page.checkbox1_click()
        self.main_page.checkbox2_click()
        self.main_page.radio1_click()
        self.main_page.select_click()
        self.main_page.email_send()
        self.main_page.send_longest()
        self.main_page.submit_click()
        assert self.main_page.check_state_alert() == 'Message received!'

    @pytest.mark.parametrize("name", [
        "klasjdsad",
        "skjdsadasdd",
        "28973123*(@&#*(&!@#&asjkhdaskld"
    ])
    def test_fill_only_required(self, name):
        self.main_page.nameInput_send(name)
        self.main_page.submit_click()
        assert self.main_page.check_state_alert() == 'Message received!'

    @pytest.mark.parametrize("name", [
        "91283990()*@(*!@$",
        "[;];;;];]",
        "28973123*(@&#*(&!@#&asjkhdaskld"
    ])
    def test_fill_not_full(self, name): # Можно считать он лишним, раз у нас требует только Name, но добавляю, чтобы проверить работает ли скролл для элементов
        self.main_page.send_longest()
        self.main_page.nameInput_send(name)
        self.main_page.select_click()
        self.main_page.submit_click()
        assert self.main_page.check_state_alert() == 'Message received!'