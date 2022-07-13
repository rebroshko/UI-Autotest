import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):    # add flag url
    parser.addoption('--url', default='https://www.mvideo.ru', help='Url for open base page')


@pytest.fixture
def base_url(request):
    return request.congig.getoption('--url')


@pytest.fixture
def get_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--log-level=DEBUG')
    return options


@pytest.fixture(scope='function')
def browser(get_chrome_options):
    options = get_chrome_options
    path_driver = Service('/Users/insafsibgatullin/Downloads/chromedriver')  # Driver Chrome path
    browser = webdriver.Chrome(service=path_driver, options=options)
    yield browser
    browser.quit()

