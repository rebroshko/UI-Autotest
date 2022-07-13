import pytest
from pages.main_page import MainPage



@pytest.mark.usefixtures('browser', 'base_url')
def test_picture_on_yandex(browser, base_url):
    page = MainPage(browser, base_url)          # initial Page Object
    page.open()                                # open_yandex_page
    # page.check_link_picture_is_present()
    # photo_category_page = PicturePage(browser, link_on_first_cat)                  # new place and text for next step
    # photo_category_page.open()




