from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADDTOCART_BTN), "\"Add to basket\" button is missing"

    def should_be_enabled_add_to_cart_btn(self):
        assert self.is_element_enabled(*ProductPageLocators.ADDTOCART_BTN), "\"Add to basket\" button is disabled"

    def should_item_name_match(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_item_name = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert item_name == added_item_name, f"Didn't add correct item: {item_name} expected {added_item_name} actual"

    def should_item_price_match(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        added_item_price = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_PRICE).text
        assert item_price == added_item_price, f"Total price of cart ({added_item_price}) doesn't match with item's price ({item_price})"

    def add_item_to_basket(self):
        self.should_be_add_to_cart_btn()
        self.should_be_enabled_add_to_cart_btn()
        button = self.browser.find_element(*ProductPageLocators.ADDTOCART_BTN)
        button.click()
        self.solve_quiz_and_get_code()
        self.should_item_name_match()
        self.should_item_price_match()


