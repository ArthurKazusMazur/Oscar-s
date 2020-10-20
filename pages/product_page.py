from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.locators import ConfirmationPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN) \
            .click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ConfirmationPageLocators.BASKET_PRODUCT_NAME), \
            "CONFIRMATION MESSAGE is PRESENT"

    def should_message_disappear(self):
        assert self.is_disappeared(*ConfirmationPageLocators.BASKET_PRODUCT_NAME), \
            "CONFIRMATION MESSAGE did not DISAPPEAR!!!"

    def get_catalogue_product_name(self):
        pass
