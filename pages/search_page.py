import time
from selenium.webdriver import Keys
from .base_page import BasePage
from .product_page import ProductPage
from .locators import *


class SearchPage(ProductPage):

    def check_visible_search_panel(self):
        assert self.check_visible_element(*BasePageLocators.SEARCH_BAR_FIND), 'Search field not found'

    def write_data_and_switch(self):
        input_element = self.found_element(*BasePageLocators.SEARCH_BAR_FIND)
        input_element.send_keys(BaseLocator.SEARCH_DATA)
        input_element.send_keys(Keys.RETURN) # Ильдар молодец

    def found_product_and_switch(self):
        assert self.check_visible_element(*BasePageLocators.PRODUCT_NAME), 'Product not found'
        product = self.found_element(*BasePageLocators.PRODUCT_NAME)
        product.click()





