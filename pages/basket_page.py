from pages.base_page import BasePage
from pages.locators import MainPageLocators, ConfirmationPageLocators
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def view_basket_after_adding_product(self):
        assert self.browser.find_element(*ConfirmationPageLocators.BASKET_TOTAL_PRICE), \
            'NO PRODUCT PRICE, YOUR BASKET is EMPTY!!!'
        assert self.browser.find_element(*ConfirmationPageLocators.BASKET_PRODUCT_NAME), \
            'NO PRODUCT, YOUR BASKET is EMPTY!!!'

    def view_basket(self):
        self.go_to_basket_page(*MainPageLocators.VIEW_BASKET_BTN)

    def should_be_empty_basket(self):
        self.go_to_basket_page(*MainPageLocators.VIEW_BASKET_BTN)
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text == \
               "Your basket is empty. Continue shopping", "OOPS, LOOKS LIKE SMTH is IN YOUR BASKET!!!"
