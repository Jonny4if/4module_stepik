from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import time
import pytest

# тест с параметризацией реализован в отдельном файле test_product_page_with_fixture.py 
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

#def test_guest_can_add_product_to_basket(browser,link):

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # открываем страницу
    # time.sleep(5)                     # ставим на паузу
    page.should_be_product_page()       # выполняем метод страницы

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page_from_product_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/the-girl-who-kicked-the-hornets-nest_199/"
    page = BasketPage(browser, link)
    page.open()
    page.basket_opened_and_basket_clear()