import allure

from page_objects.product_page import ProductPage


@allure.title("Отображение цены")
def test_price_is_visible(browser):
    ProductPage(browser).get_price()


@allure.title("Отображение кнопки 'Добавить в корзину'")
def test_add_to_cart_btn_is_visible(browser):
    ProductPage(browser).get_add_to_cart_btn()


@allure.title("Отображение кнопки 'Сравнить'")
def test_review_tab_is_visible(browser):
    ProductPage(browser).scroll_to_review_tab()


@allure.title("Отображение кнопки 'Добавить в избранное'")
def test_btn_add_to_wish_list_is_visible(browser):
    ProductPage(browser).get_add_to_wish_list_btn()


@allure.title("Отображение превью товара")
def test_main_image_is_visible(browser):
    ProductPage(browser).get_main_image()