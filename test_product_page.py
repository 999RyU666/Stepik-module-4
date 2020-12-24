import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import time

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
                                  
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_price = browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    product_price_in_basket = browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
    product_name_in_basket = browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
    assert product_price == product_price_in_basket, "Incorrect product price"
    assert product_name == product_name_in_basket, "Incorrect product name"
