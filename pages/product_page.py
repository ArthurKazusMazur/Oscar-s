from pages.base_page import BasePage
from pages.locators import PromoPageLocators


class PromoPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*PromoPageLocators.ADD_TO_BASKET_BTN) \
            .click()

    def view_basket(self):
        self.browser.find_element(*PromoPageLocators.VIEW_BASKET_BTN).click()

    def get_catalogue_product_price(self):

        catalogue_product_price = self.browser.find_element(*PromoPageLocators.CATALOGUE_PRODUCT_NAME).text
        print(catalogue_product_price.text)

    def get_catalogue_product_name(self):
        pass
