from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_SUBMIT = (By.XPATH, "//button[contains(text(), \"Register\")]")


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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    ITEM_AREA = (By.CSS_SELECTOR, "#content_inner .basket_summary")
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner p")
