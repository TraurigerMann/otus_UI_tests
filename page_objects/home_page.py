from selenium.webdriver.common.by import By

import random

from page_objects.base_page import BasePage
from page_objects.header_element import HeaderElement


class HomePage(BasePage):
    random_product_num = 0

    def __init__(self, browser):
        super().__init__(browser)
        self.open_home_page()


    def open_home_page(self):
        self.browser.get(f"{self.base_url}/home")
        return self


    def get_logo(self):
        self.get_element((By.ID, "logo"))


    def get_add_to_cart_btn(self):
        self.get_element((
        By.XPATH,
        "//div[contains(@class, 'product-thumb')][1]/descendant::button[contains(@title, 'Add to Cart')]"
    ))


    def get_cart_btn(self):
        self.get_element((By.XPATH, "//div[contains(@id, 'header-cart')]/descendant::button"))


    def get_search_btn(self):
        self.get_element((By.XPATH, "//div[contains(@id, 'search')]/descendant::button"))


    def get_products_list(self):
        return len(self.get_elements((By.XPATH, "//*[@class='col mb-3']")))


    def get_random_product_number(self):
        self.random_product_num = random.randint(1, self.get_products_list())
        return self


    def get_cart_items(self):
        return self.get_element((By.XPATH, "//*[@id='header-cart']//button[contains(text(), ' 1 item(s)')]")).text


    def is_product_link_clickable(self):
        self.get_clickable_element((By.XPATH, "//div/descendant::a[text()='MacBook']"))


    def click_add_to_cart_btn(self):
        self.click((
            By.XPATH, f"//*[@class='col mb-3'][{self.random_product_num}]//button[@title='Add to Cart']"
        ))
        return self

    def scroll_to_add_to_cart_btn(self):
        self.scroll((
            By.XPATH, f"//*[@class='col mb-3'][{self.random_product_num}]//button[@title='Add to Cart']"
        ))
        return self


    def check_items_in_cart(self):
        assert self.get_cart_items() != " 0 item(s) - $0.00"
        return self


    def check_cart_items_currency(self):
        self.get_element((By.XPATH, f"//*[@id='header-cart']//button[contains(text(), '{HeaderElement.new_currency}')]"))




