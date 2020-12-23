import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser")

@pytest.fixture
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", language)
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print("\nquit browser..")
    browser.quit()
