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

    @pytest.mark.parametrize("password", [
        "92138123",
        "jksdhasd",
        "hsad127327(@)*(][][;"
    ])
    def test_fill_form_without_name(self, password):
        self.main_page.passwordInput_send(password)
        self.main_page.checkbox1_click()
        self.main_page.checkbox2_click()
        self.main_page.radio1_click()
        self.main_page.select_click()
        self.main_page.email_send()
        self.main_page.send_longest()
        self.main_page.submit_click()
        assert self.main_page.check_alert() == False

    def test_fill_form_only_some(self):
        self.main_page.send_longest()
        self.main_page.submit_click()
        assert self.main_page.check_alert() == False