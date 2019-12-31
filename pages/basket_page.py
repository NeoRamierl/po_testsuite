from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "/basket/" in self.browser.current_url, "This is not basket URL"

    def should_be_text_basket_empty(self):
        assert "empty" in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MSG).text, "Text for empty basket is not correct"

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_AREA), "Basket is not empty"

    def should_disappear_item_area(self):
        assert self.is_disappeared(*BasketPageLocators.ITEM_AREA), \
            "Item area is presented, but should not be"

