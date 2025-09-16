import logging
import os
import pytest
import allure

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from page_objects.administation_login_page import AdminLoginPage
from page_objects.administration_page import AdminPage
from page_objects.alert_element import AlertSuccessElement


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
    parser.addoption(
        "--logging_state",
        default="False",
        help="State of logging service: True = enabled; False = disabled",
    )


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--base_url")
    logging_state = request.config.getoption("--logging_state")

    if browser == "chrome":
        service = Service()
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.test_name = request.node.name
    driver.test_page = os.path.splitext(os.path.basename(str(request.node.fspath)))[0]
    driver.log_level = logging.DEBUG

    def teardown():
        driver.quit()
    
    request.addfinalizer(teardown)


    return driver, url, logging_state


@pytest.fixture
def product_cleanup(browser):

    def _cleanup(product_to_delete):
        AdminPage(browser).click_back_btn() \
            .write_product_to_filter(product_to_delete) \
            .click_filter_btn() \
            .click_product_checkbox() \
            .click_delete_btn() \
            .alert_accept()
        AlertSuccessElement(browser)

    return _cleanup


@pytest.fixture
def product_create(browser):

    def _create(admin_login, admin_password, product_name, tag, model_name, seo_url):
        AdminLoginPage(browser).open_admin_login_page() \
            .login(admin_login, admin_password)
        AdminPage(browser).click_catalog_dropdown() \
            .click_catalog_item("Products") \
            .click_add_btn() \
            .write_product_name(product_name) \
            .scroll_to_meta_tag_input() \
            .write_meta_tag(tag) \
            .click_data_tab() \
            .write_model_name(model_name) \
            .click_seo_tab() \
            .write_seo_url(seo_url) \
            .click_save_btn()
        AlertSuccessElement(browser)

    return _create