import allure

from pages.main_page import MainPage
import pytest

# Тесты на проверку наличия элементов для заполнения формы
class TestAllEmelentsExist:

    @classmethod
    def setup_class(cls):
        print("\n========= Начало выполнения тестов по поиску элементов ==========")

    @classmethod
    def teardown_class(cls):
        print("========= Конец выполнения тестов по поиску элементов ==========")

    @pytest.fixture(autouse=True)
    def setup(self, browser, url = "https://practice-automation.com/form-fields/"):
        self.main_page = MainPage(browser)
        self.main_page.open(url)
        yield self.main_page
        self.main_page.quit()

    # Я сделаю 2 набора, 1 тест сразу все кнопки проверяет, другой по отдельности, чтобы не тратить время на ожидание загрузки :/
    @allure.story("Поиск наличия поле ввода имени")
    def test_nameinput_exist(self):
        assert self.main_page.nameInput().is_displayed()

    @allure.story("Поиск наличия поле ввода пароля")
    def test_passInput_exist(self):
        assert self.main_page.passwordInput().is_displayed()

    @allure.story("Поиск наличия ячейки 1")
    def test_check1_exist(self):
        assert self.main_page.checkbox1().is_displayed()

    @allure.story("Поиск наличия ячейки 2")
    def test_check2_exist(self):
        assert self.main_page.checkbox2().is_displayed()

    @allure.story("Поиск наличия радиоячейки")
    def test_radio1_exist(self):
        assert self.main_page.radio1().is_displayed()

    @allure.story("Поиск наличия списка выбора пунктов")
    def test_select_exist(self):
        assert self.main_page.select().is_displayed()

    @allure.story("Поиск наличия поле ввода почты")
    def test_email_exist(self):
        assert self.main_page.email().is_displayed()

    @allure.story("Поиск наличия поле ввода сообщения")
    def test_message_exist(self):
        assert self.main_page.message().is_displayed()

    @allure.story("Поиск наличия кнопки подтверждения")
    def test_submit_exist(self):
        assert self.main_page.submit().is_displayed()

    @allure.feature('Find All Elements')
    @allure.story("Поиск наличия всех нужных элементов")
    def test_all_elements_exist(self):
        assert self.main_page.nameInput().is_displayed() and self.main_page.passwordInput().is_displayed() and \
               self.main_page.checkbox1().is_displayed() and self.main_page.checkbox2().is_displayed() and \
               self.main_page.radio1().is_displayed() and self.main_page.select().is_displayed() and \
               self.main_page.email().is_displayed() and self.main_page.message().is_displayed() and self.main_page.submit().is_displayed()
