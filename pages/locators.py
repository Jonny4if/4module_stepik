from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_CART = (By.CSS_SELECTOR, "#messages .alert-success:first-child .alertinner strong")
    PRODUCT_PRICE_CART = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child .alertinner strong")
