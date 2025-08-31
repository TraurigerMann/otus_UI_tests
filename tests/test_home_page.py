from page_objects.alert_element import AlertSuccessElement
from page_objects.header_element import HeaderElement
from page_objects.home_page import HomePage


def test_logo_is_visible(browser):
    HomePage(browser).get_logo()


def test_product_add_to_card_btn_is_visible(browser):
    HomePage(browser).get_add_to_cart_btn()



def test_cart_btn_is_visible(browser):
    HomePage(browser).get_cart_btn()


def test_search_btn_is_visible(browser):
    HomePage(browser).get_search_btn()


def test_product_link_is_clickable(browser):
    HomePage(browser).is_product_link_clickable()


def test_add_random_product_to_cart(browser):
    HomePage(browser) \
        .get_random_product_number() \
        .scroll_to_add_to_cart_btn() \
        .click_add_to_cart_btn() \
        .check_items_in_cart()
    AlertSuccessElement(browser)


def test_price_currency_changing(browser):
    HomePage(browser)
    HeaderElement(browser).click_currency_dropdown() \
        .set_new_currency()
    HomePage(browser).check_cart_items_currency()