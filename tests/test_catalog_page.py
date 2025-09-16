import allure

from page_objects.catalog_page import CatalogPage
from page_objects.header_element import HeaderElement


@allure.title("Отображение ссылки на продукт")
def test_product_link_is_visible(browser):
    CatalogPage(browser).get_product_link()


@allure.title("Отображение кнопки 'Сравнить'")
def test_compare_button_is_visible(browser):
    CatalogPage(browser).get_compare_btn()


@allure.title("Отображение кнопки 'Добавить в избранное'")
def test_product_add_to_wish_list_btn_is_visible(browser):
    CatalogPage(browser).get_add_to_wish_list_btn()


@allure.title("Отображение дропдауна сортировки")
def test_sort_dropdown_is_visible(browser):
    CatalogPage(browser).get_sort_dropdown()


@allure.title("Отображение кнопки 'Домой'")
def test_home_btn_is_visible(browser):
    CatalogPage(browser).get_home_btn()


@allure.title("Изменение отображаемой валюты")
def test_price_currency_changing(browser):
    CatalogPage(browser)
    HeaderElement(browser).click_currency_dropdown() \
        .set_new_currency()
    CatalogPage(browser).check_new_currency_applied()
