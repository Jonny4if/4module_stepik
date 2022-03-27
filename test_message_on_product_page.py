from pages.product_page import ProductPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.add_to_cart()                  # выполняем метод добавление товара в корзину
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.add_to_cart()                  # выполняем метод добавление товара в корзину
    time.sleep(1)
    page.wait_close_success_message()