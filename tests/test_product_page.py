import pytest
import time

from pages.product_page import PromoPage
from pages.locators import PromoPageLocators
from pages.locators import ConfirmationPageLocators


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()
    page = PromoPage(browser, link)
    page.open()

    catalogue_product_name = browser.find_element(*PromoPageLocators.CATALOGUE_PRODUCT_NAME).text
    catalogue_product_price = browser.find_element(*PromoPageLocators.CATALOGUE_PRICE).text

    page.add_to_basket()
    page.solve_quiz_and_get_code()

    basket_product_name = browser.find_element(*ConfirmationPageLocators.BASKET_PRODUCT_NAME).text
    basket_product_price = browser.find_element(*ConfirmationPageLocators.BASKET_TOTAL_PRICE).text

    assert catalogue_product_price == basket_product_price, "PRODUCT PRICE DOES NOT MATCH!!!"
    assert catalogue_product_name == basket_product_name, "PRODUCT NAME DOES NOT MATCH!!!"

    print(f"Exp: {catalogue_product_name} = {catalogue_product_price}")
    print(f"Act: {basket_product_name} = {basket_product_price}")

