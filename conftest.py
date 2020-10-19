import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action="store", default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action="store", default='en', help="Choose your language: ru, en, es, fr, etc...")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        print("\n\nStarting GOOGLE Chrome browser for test...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument('headless')  # эта опция позволяет запускать браузер "в безголовом" режиме
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.delete_all_cookies()

    elif browser_name == "firefox":
        print("\n\nStarting Mazila Firefox browser for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.maximize_window()
        browser.delete_all_cookies()
    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")

    yield browser
    print("\n\nQuit browser")
    browser.quit()
