import time
from .base_page import BasePage
from .product_page import ProductPage
from .locators import *


class MainPage(ProductPage):

    def switch_on_next_product(self):
        assert self.check_visible_element(*NewFeature.RIGHT_SWAP_BTN), 'switch button not found'
        btn_right = self.found_element(*NewFeature.RIGHT_SWAP_BTN)
        btn_right.click()

    def open_product_page(self):
        time.sleep(2)
        assert self.check_visible_element(*NewFeature.PRODUCT_WINDOW), 'window not found'
        self.found_element(*NewFeature.PRODUCT_WINDOW).click()





