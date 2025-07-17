import pytest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="This is browser to interact with selenium"
    )
    parser.addoption(
        "--base_url",
        default="http://localhost:8081/",
        help="This is base url of OpenCart service",
    )


@pytest.fixture
def base_url(request):

    return request.config.getoption("--base_url")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        service = Service()
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox()

    return driver
