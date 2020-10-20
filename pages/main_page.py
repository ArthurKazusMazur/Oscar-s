from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "OOPS, LOOKS LIKE LOGIN LINK is MISSED!!!"

    def go_to_login_register_page(self, reg_url):
        self.go_to_login_page(*MainPageLocators.LOGIN_LINK, reg_url)
        assert self.browser.current_url == reg_url, "REDIRECT TO REGISTRATION PAGE is FAILED!!!"

    def go_to_basket(self):
        self.go_to_basket_page(*MainPageLocators.VIEW_BASKET_BTN)
