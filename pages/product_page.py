from .base_page import BasePage
from .locators import PromoPageLocators


class PromoPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*PromoPageLocators.ADD_TO_BASKET_BTN)\
            .click()
        self.browser.solve_quiz_and_get_code()
