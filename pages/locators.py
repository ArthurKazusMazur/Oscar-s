from selenium.webdriver.common.by import By


class MainPageLocators():
    VIEW_BASKET_BTN = (By.XPATH, '//*[@id="default"]/header/div[1]//div[2]/span/a')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class LoginPageLocators():
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONF_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    CONFIRM_REGISTER_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.CSS_SELECTOR, '[name="login_submit"]')
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, '.alertinner.wicon')


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    VIEW_BASKET_BTN = (By.XPATH, '//p/a[1][@class = "btn btn-info"]')
    CATALOGUE_PRODUCT_NAME = (By.XPATH, '//div/h1')
    CATALOGUE_PRICE = (By.XPATH, '//div/p[@class="price_color"]')


class ConfirmationPageLocators():
    BASKET_TOTAL_PRICE = (By.XPATH, '//div[@class="alertinner "]/p[1]/strong')
    BASKET_PRODUCT_NAME = (By.XPATH, '//div[@class="alertinner " and text()]/strong')


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//div/p')
