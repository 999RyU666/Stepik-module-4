from .base_page import BasePage
from .locators import ProductPageLocators

class BasketPage(BasePage):
    def open_basket(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET)
        button.click()
        
    def basket_is_empty(self):
        assert page.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"
        
    def should_be_message_basket_is_empty(self):
        assert page.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "There is no empty basket message"
        