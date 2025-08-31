from page_objects.product_page import ProductPage


def test_price_is_visible(browser):
    ProductPage(browser).get_price()


def test_add_to_cart_btn_is_visible(browser):
    ProductPage(browser).get_add_to_cart_btn()


def test_review_tab_is_visible(browser):
    ProductPage(browser).scroll_to_review_tab()


def test_btn_add_to_wish_list_is_visible(browser):
    ProductPage(browser).get_add_to_wish_list_btn()


def test_main_image_is_visible(browser):
    ProductPage(browser).get_main_image()