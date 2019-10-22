import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language: en, ru, es, ar, ca, cs, da, de, el, fi, fr, it, ko, nl, pl, pt, pt-br, ro, sk, uk, zh-cn")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    options = Options()
    if lang is not None:
        print("\nstart using language for test")
    else:
        raise pytest.UsageError("language should be added, for example, en, ru, es, ar, ca, cs, da, de, el, fi, fr, it, ko, nl, pl, pt, pt-br, ro, sk, uk, zh-cn")
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
