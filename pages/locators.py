from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_CART = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email.form-control")
    REGISTER_FORM_INPUT_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1.form-control")
    REGISTER_FORM_INPUT_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2.form-control")
    REGISTER_FORM_BTN_ENTER = (By.CSS_SELECTOR, "#register_form.well button.btn.btn-lg.btn-primary")

class ProductPageLocators():
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_CART = (By.CSS_SELECTOR, "#messages .alert-success:first-child .alertinner strong")
    PRODUCT_PRICE_CART = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child .alertinner strong")

class BasketPageLocators():
    BASKET_ANY_ITEM = (By.CSS_SELECTOR, "#basket_formset.basket_summary .basket-items") 
    BASKET_CLEAR_MESSAGE = (By.CSS_SELECTOR, ".content #content_inner p")