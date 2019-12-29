from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADDTOCART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    TOTAL_PRICE = (By.CSS_SELECTOR, "div.basket-mini")