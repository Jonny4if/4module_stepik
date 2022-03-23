from pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
class TestAddProcuctToCart:
    @pytest.fixture()
    def browser_product_in_cart(self, browser, link):
        print("\nstart browser for test..")
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                         # открываем страницу
        page.add_to_cart()                  # выполняем метод добавление товара в корзину
        page.solve_quiz_and_get_code()      # выполняем метод ввода проверочного кода
        time.sleep(5)
        return page                         # возвращаем значение страницы в состоянии добавленого товара + введеного кода

    def test_guest_can_add_product_to_basket(self, browser_product_in_cart):
        browser_product_in_cart.product_name() 

    def test_guest_can_add_product_to_basket2(self, browser_product_in_cart):
        browser_product_in_cart.product_price()
                