from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Подстрока 'login' отсутствует в текущем url браузера"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Форма логина не обнаружена"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не обнаружена"