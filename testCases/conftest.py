from selenium import webdriver
import pytest

@pytest.fixture()
def driver_setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox")
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()    
def browser(request):
    return request.config.getoption("--browser")
