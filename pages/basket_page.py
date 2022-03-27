from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_opened_and_basket_clear(self):
        # переход корзину, корзина ПУСТА
        self.go_to_cart()
        self.cart_clear()
        self.message_cart_clear()

    def go_to_cart(self):
        # переход корзину
        link = self.browser.find_element(*BasePageLocators.GO_TO_CART)
        assert self.browser.find_element(*BasePageLocators.GO_TO_CART), "Link go to cart is not presented"  
        link.click()
        
    def cart_clear(self):
        # в корзине нет товаров
        assert not self.is_element_present(*BasketPageLocators.BASKET_ANY_ITEM), "Should NOT BE product in cart"
        
    def message_cart_clear(self):
        # есть сообщение корзина пуста 
        assert self.browser.find_element(*BasketPageLocators.BASKET_CLEAR_MESSAGE), "Doesn't message CART CLEAR"