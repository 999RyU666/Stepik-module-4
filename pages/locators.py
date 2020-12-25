from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages .alertinner strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1)")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".basket-mini >span > a")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    
    