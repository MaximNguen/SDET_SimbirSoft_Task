from pages.main_page import MainPage
import pytest

# Тесты на проверку наличия элементов для заполнения формы
class TestAllEmelentsExist:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        self.main_page.open()
        yield self.main_page
        self.main_page.quit()

    # Я сделаю 2 набора, 1 тест сразу все кнопки проверяет, другой по отдельности, чтобы не тратить время на ожидание загрузки :/
    def test_nameinput_exist(self):
        assert self.main_page.nameInput().is_displayed()

    def test_passInput_exist(self):
        assert self.main_page.passwordInput().is_displayed()

    def test_check1_exist(self):
        assert self.main_page.checkbox1().is_displayed()

    def test_check2_exist(self):
        assert self.main_page.checkbox2().is_displayed()

    def test_radio1_exist(self):
        assert self.main_page.radio1().is_displayed()

    def test_select_exist(self):
        assert self.main_page.select().is_displayed()

    def test_email_exist(self):
        assert self.main_page.email().is_displayed()

    def test_message_exist(self):
        assert self.main_page.message().is_displayed()

    def test_submit_exist(self):
        assert self.main_page.submit().is_displayed()

    def test_all_elements_exist(self):
        assert self.main_page.nameInput().is_displayed() and self.main_page.passwordInput().is_displayed() and \
               self.main_page.checkbox1().is_displayed() and self.main_page.checkbox2().is_displayed() and \
               self.main_page.radio1().is_displayed() and self.main_page.select().is_displayed() and \
               self.main_page.email().is_displayed() and self.main_page.message().is_displayed() and self.main_page.submit().is_displayed()
