import allure

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
    def setup(self, browser, url="https://practice-automation.com/form-fields/"):
        self.main_page = MainPage(browser)
        self.main_page.open(url)
        yield self.main_page
        self.main_page.quit()

    @allure.feature("Positive Test-Case")
    @allure.story("Ввод всех полей")
    @pytest.mark.parametrize("name,password,mail", [
        ("maxim", "9012832", "name@example.com"),
        ("pasha", "kasljdasds", "normalMain@mail.ru"),
        ("egor228443", "()*@)(#*!@*#)", "supercool@gmail.com"),
    ])
    def test_fill_form_full(self, name, password, mail):
        self.main_page.nameInput_send(name)
        self.main_page.passwordInput_send(password)
        self.main_page.checkbox1_click()
        self.main_page.checkbox2_click()
        self.main_page.radio1_click()
        self.main_page.select_click()
        self.main_page.email_send(mail)
        self.main_page.send_longest()
        self.main_page.submit_click()
        with allure.step("Достоверимся, что алерт с сообщением выпал"):
            assert self.main_page.check_state_alert() == 'Message received!'

    @allure.feature("Positive Test-Case")
    @allure.story("Ввод только требующихся полей")
    @pytest.mark.parametrize("name", [
        "klasjdsad",
        "skjdsadasdd",
        "28973123*(@&#*(&!@#&asjkhdaskld"
    ])
    def test_fill_only_required(self, name):
        self.main_page.nameInput_send(name)
        self.main_page.submit_click()
        with allure.step("Достоверимся, что алерт с сообщением выпал"):
            assert self.main_page.check_state_alert() == 'Message received!'

    @allure.feature("Positive Test-Case")
    @allure.story("Неполный ввод полей, в том числе имени")
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
        with allure.step("Достоверимся, что алерт с сообщением выпал"):
            assert self.main_page.check_state_alert() == 'Message received!'