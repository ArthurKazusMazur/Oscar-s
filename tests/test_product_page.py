from pages.product_page import PromoPage
from pages.locators import PromoPageLocators
from pages.locators import BasketPageLocators

url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = PromoPage(browser, url)
    page.open()

    catalogue_product_name = browser.find_element(*PromoPageLocators.CATALOGUE_PRODUCT_NAME).text
    catalogue_product_price = browser.find_element(*PromoPageLocators.CATALOGUE_PRICE).text

    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.view_basket()

    basket_product_name = browser.find_element(*BasketPageLocators.BASKET_PRODUCT_NAME).text
    basket_product_price = browser.find_element(*BasketPageLocators.BASKET_TOTAL_PRICE).text

    assert catalogue_product_price == basket_product_price, "PRODUCT PRICE DOES NOT MATCH!!!"
    assert catalogue_product_name == basket_product_name, "PRODUCT NAME DOES NOT MATCH!!!"

    print(f"Exp: {catalogue_product_name} = {catalogue_product_price}")
    print(f"Act: {basket_product_name} = {basket_product_price}")

