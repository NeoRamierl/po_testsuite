from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADDTOCART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")

