from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_BAR_FIND = (By.XPATH, '//input[@class="input__field"] ')              # Search element Xpath.
    PRODUCT_NAME = (By.XPATH, '//a[contains(text(), "Apple iPhone")]')
    SAVE_FULL_PRODUCT_NAME = (By.XPATH, '//h1[contains(text(), "Apple iPhone")]')
    CART_BUTTON = (By.XPATH, '//button[contains(@class, "mv-main-button--large")]')


class BaseLocator:
    SEARCH_DATA = 'iPhone'


class NewFeature:
    RIGHT_SWAP_BTN = (By.XPATH, '//button[contains(@class, "forward mv-icon-button--primary mv-icon-button--medium")]')
    PRODUCT_WINDOW = (By.XPATH, '/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/ng-component/div/mvid-promo-and-day-products-collection/mvid-day-products-block/div/div/div[1]/mvid-day-product[2]/a')

