import time

import pytest
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
import pages.product_page


@pytest.mark.usefixtures('browser', 'base_url')
def test_choice_first_product(browser, base_url):
    page = SearchPage(browser, base_url)          # initial Page Object
    page.open()                                 # open_yandex_page
    page.check_visible_search_panel()
    page.write_data_and_switch()
    page.found_product_and_switch()
    page.save_product_name()
    page.add_cart()                             # не работает добавление в корзину проверить что товар добавлен
    page_new_feature = MainPage(browser, base_url)
    page_new_feature.open()
    page_new_feature.switch_on_next_product()
    page_new_feature.open_product_page()
    #new_prod_url = page_new_feature.choice_product_page()
    #product_page =
    page_new_feature.save_product_name()
    page_new_feature.add_cart()
    print(page.FULL_NAME_PRODUCT, page_new_feature.FULL_NAME_PRODUCT)
    time.sleep(10)

