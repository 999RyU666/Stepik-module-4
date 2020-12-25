from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def open_register_page(self):
        register_button = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        register_button.click()
        
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL)
        email_field.send_keys(email)
        password1 = self.browser.find_element(*RegisterPageLocators.PASSWORD)
        password1.send_keys(password)
        password2 = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD)
        password2.send_keys(password)
        submit = self.browser.find_element(*RegisterPageLocators.SUBMIT)
        submit.click()
        