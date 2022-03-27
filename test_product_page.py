from pages.base_page import BasePage
from pages.product_page import ProductPage 
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time
import pytest
import random

# тест с параметризацией реализован в отдельном файле test_product_page_with_fixture.py

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # регистрируем нового user
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + str(random.randint(3, 100))
        page.register_new_user(email, password)
        # запускаем проверку что авторизация прошла
        page_base = BasePage(browser, browser.current_url)
        page_base.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        #отсутствие сообщения о добавлении товара в корзину
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        # проверка соотвествия страницы продукта
        page.should_be_product_page()   

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    page = ProductPage(browser, link)
    page.open()
    # проверка соотвествия страницы продукта
    page.should_be_product_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # проверка наличия ссылки на страницу авторизации
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/the-girl-who-kicked-the-hornets-nest_199/"
    page = ProductPage(browser, link)
    page.open()
    #переходим на страницу корзины
    basket_page = BasketPage(browser, browser.current_url)
    # запускаем метод проверки корзины
    basket_page.basket_opened_and_basket_clear()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # со страницы продукта можно перейти на страницу авторизации
    page.go_to_login_page_from_product_page()

@pytest.mark.message
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # добавление товара в корзину
    page.add_to_cart()
    # отсутствие сообщения о добавлении товара в корзину
    page.should_not_be_success_message()

@pytest.mark.message
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # отсутствие сообщения о добавлении товара в корзину
    page.should_not_be_success_message()

@pytest.mark.message
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # добавление товара в корзину
    page.add_to_cart()
    time.sleep(1)
    # cобщение о добавлении товара в корзину пропадает
    page.wait_close_success_message()