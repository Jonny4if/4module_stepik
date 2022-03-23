from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
class ProductPage(BasePage):
    
    def should_be_product_page(self):
        self.add_to_cart()
        self.solve_quiz_and_get_code()
        self.product_name()
        self.product_price()

    def add_to_cart(self):
        # добавляем товар в корзину
        link_add_to_cart = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_CART)
        link_add_to_cart.click()
        
        # получаем проверочный код
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def product_name(self):
        # проверка, что имя товара на странице и корзине совпадают
        name_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PAGE).text
        name_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CART).text
        assert  name_page == name_cart, "Different name!"   

    def product_price(self):
        # проверка, что цена товара на странице и корзине совпадают
        price_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_PAGE).text
        price_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CART).text
        assert price_page == price_cart, "Different price!"
