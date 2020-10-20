import pytest
from faker import Faker
from pages.locators import ProductPageLocators
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import MainPageLocators
from pages.login_page import LoginRegisterPage

main_link = 'http://selenium1py.pythonanywhere.com/en-gb/'
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
reg_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
# for logging user
login_email = 'kazus@gmail.com'
login_password = 'qwer123456789'
# random emails & passwords generator
gen = Faker()
email = gen.email()
password = gen.name()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    conf_page = BasketPage(browser, browser.current_url)
    conf_page.view_basket_after_adding_product()


class TestUserAddToBasketFromProductPage():
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # main page and redirect to login page
        main_page = MainPage(browser, main_link)
        main_page.open()
        main_page.go_to_login_register_page(reg_url)
        # login user &  checking wether user is logged in
        login_page = LoginRegisterPage(browser, browser.current_url)
        login_page.user_login(login_email, login_password)
        login_page.is_user_authorized()
        # adding product to basket
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        # checking wether product is in a basket
        basket = BasketPage(browser, browser.current_url)
        basket.view_basket()

    @pytest.mark.skip
    def test_user_can_see_success_message_after_adding_product_to_basket(self, browser):
        # main page and redirect to login page
        main_page = MainPage(browser, main_link)
        main_page.open()
        main_page.go_to_login_register_page(reg_url)
        # login user &  checking wether user is logged in
        login_page = LoginRegisterPage(browser, browser.current_url)
        login_page.user_login(login_email, login_password)
        login_page.is_user_authorized()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page(*ProductPageLocators.VIEW_BASKET_BTN)
        basket = BasketPage(browser, browser.current_url)
        basket.should_be_empty_basket()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page(*MainPageLocators.LOGIN_LINK, reg_url)


@pytest.mark.absence
class TestMessageAbsence():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_message_disappear()
