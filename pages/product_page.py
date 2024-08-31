import time
from .base_page import BasePage
from .locators import BasePageLocators


class ProductPage(BasePage):
    FULL_NAME_PRODUCT = []

    def save_product_name(self):
        product_name = self.found_element(*BasePageLocators.SAVE_FULL_PRODUCT_NAME)
        self.FULL_NAME_PRODUCT = product_name.text

    def add_cart(self):
        self.browser.delete_all_cookies()
        time.sleep(2)
        assert self.check_visible_element(*BasePageLocators.CART_BUTTON), 'Cart button not found'
        self.found_element(*BasePageLocators.CART_BUTTON).click()
