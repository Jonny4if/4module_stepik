from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert 'login' in self.browser.current_url, "Haven't login in url" 

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login FORM is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register FORM is not presented"
     
    def register_new_user(self, email, password):
        # регистрируем пользователя
        form_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_INPUT_EMAIL)
        form_email.send_keys(email)
        form_pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_INPUT_PASSWORD1)    
        form_pass1.send_keys(password)
        form_pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_INPUT_PASSWORD2)
        form_pass2.send_keys(password)
        btn_register = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BTN_ENTER)
        btn_register.click()