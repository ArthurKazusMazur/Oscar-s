import pytest
from faker import Faker
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.login_page import LoginRegisterPage

link = "http://selenium1py.pythonanywhere.com/en-gb/"
reg_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
# random emails & passwords generator
gen = Faker()
email = gen.email()
password = gen.name()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_register_page(reg_url)

    def test_guest_register_scenario(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_register_page(reg_url)
        login_register_page = LoginRegisterPage(browser, browser.current_url)
        login_register_page.register_new_user(email, password)


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_empty_basket()
