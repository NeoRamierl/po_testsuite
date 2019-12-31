from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADDTOCART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span a")


class BasketPageLocators():
    ITEM_AREA = (By.CSS_SELECTOR, "#content_inner .basket_summary")
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner p")
