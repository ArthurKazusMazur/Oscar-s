from pages.base_page import BasePage
from pages.locators import LoginPageLocators, MainPageLocators

login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


class LoginRegisterPage(BasePage):
    def register_new_user(self, user_email, user_password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(user_email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT).send_keys(user_password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONF_PASSWORD_INPUT).send_keys(user_password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTER_BTN).click()
        self.is_element_present(*LoginPageLocators.CONFIRMATION_MESSAGE)

        assert self.browser.find_element(*LoginPageLocators.CONFIRMATION_MESSAGE).text == "Thanks for registering!", \
            "OOPS, LOOKS LIKE YOU COULD NOT REGISTER!!!"

    def user_login(self, user_email, user_password):
        self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT)
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT).send_keys(user_email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(user_password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()
        assert self.is_element_present(*MainPageLocators.USER_ICON), 'OOPS, LOOKS LIKE YOU are not REGISTERED!!!'
