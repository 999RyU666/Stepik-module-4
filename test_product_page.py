import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.locators import BasePageLocators
import time

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
                                  
# def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # page = ProductPage(browser, link)
    # page.open()
    # product_price = browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    # product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    # page.add_to_basket()
    # page.solve_quiz_and_get_code()
    # time.sleep(20000)
    # product_price_in_basket = browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
    # product_name_in_basket = browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
    # assert product_price == product_price_in_basket, "Incorrect product price"
    # assert product_name == product_name_in_basket, "Incorrect product name"
    
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.add_to_basket()
    # page.should_not_be_success_message()
    
# def test_guest_cant_see_success_message(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.should_not_be_success_message()

# @pytest.mark.xfail    
# def test_message_disappeared_after_adding_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.add_to_basket()
    # page.message_disappeared_after_adding_product_to_basket()
    
# def test_guest_should_see_login_link_on_product_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.should_be_login_link()
    
# def test_guest_can_go_to_login_page_from_product_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.go_to_login_page()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    assert page.is_not_element_present(*BasePageLocators.BASKET_ITEMS), "Basket is not empty"
    assert page.is_element_present(*BasePageLocators.MESSAGE_EMPTY_BASKET), "There is no empty basket message"