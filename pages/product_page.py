from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADDTOCART_BTN), "\"Add to basket\" button is missing"

    def should_be_enabled_add_to_cart_btn(self):
        assert self.is_element_enabled(*ProductPageLocators.ADDTOCART_BTN), "\"Add to basket\" button is disabled"

    def add_item_to_basket(self):
        self.should_be_add_to_cart_btn()
        self.should_be_enabled_add_to_cart_btn()
        button = self.browser.find_element(*ProductPageLocators.ADDTOCART_BTN)
        button.click()
        self.solve_quiz_and_get_code()
        text = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        print(text)

