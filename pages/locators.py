from selenium.webdriver.common.by import By


class PromoPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    VIEW_BASKET_BTN = (By.XPATH, '//p/a[1][@class = "btn btn-info"]')
    CATALOGUE_PRODUCT_NAME = (By.XPATH, '//div/h1')
    CATALOGUE_PRICE = (By.XPATH, '//div/p[@class="price_color"]')


class BasketPageLocators():
    BASKET_TOTAL_PRICE = (By.XPATH, '//h3[@class="price_color"]')
    BASKET_PRODUCT_NAME = (By.XPATH, '//div//h3/a')
