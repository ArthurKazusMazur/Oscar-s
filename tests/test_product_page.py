from pages.promo_page import PromoPage

url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = PromoPage(browser, url)
    page.open()
    page.add_to_basket()
