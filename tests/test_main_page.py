import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.locators import ConfirmationPageLocators

link = "http://selenium1py.pythonanywhere.com/en-gb/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
         # реализация теста
    pass

    def test_guest_should_see_login_link(self, browser):
         # реализация теста
    pass

def test_guest_cant_see_product_in_basket_opened_from_main_page():

Гость открывает главную страницу
Переходит в корзину по кнопке в шапке сайта
Ожидаем, что в корзине нет товаров
Ожидаем, что есть текст о том что корзина пуста

