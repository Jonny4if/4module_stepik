from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def should_be_login_link(self):
        # проверка наличия ссылки на страницу авторизации
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    
    def go_to_login_page(self):
        # переход на страницу авторизации
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_link_go_to_cart(self):
        # проверка наличия ссылки перехода в корзину
        assert self.browser.find_element(*BasePageLocators.GO_TO_CART), "Link go to cart is not presented"  

    def should_be_authorized_user(self):
        # проверка наличия иконки зарегистированого user
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                    " probably unauthorised user"

    def is_disappeared(self, how, what, timeout=4):
        # ожидание что элемент исчезнет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        # проверка наличия элемента на странице
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True    
    
    def is_not_element_present(self, how, what, timeout=4):
        # проверка отсутсвия элемента на странице
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)