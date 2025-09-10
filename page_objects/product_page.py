from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.open_product_page()


    def open_product_page(self):
        self.browser.get(f"{self.base_url}/product/desktops/mac/imac")
        return self


    def get_price(self):
        self.get_element((By.CSS_SELECTOR, ".price-new"))


    def get_add_to_cart_btn(self):
        self.get_element((By.XPATH, "//button[contains(@id, 'button-cart')]"))


    def get_add_to_wish_list_btn(self):
        self.get_element((By.XPATH, "//button[contains(@title, 'Add to Wish List')]"))


    def get_main_image(self):
        self.get_element((By.XPATH, "//img[contains(@title, 'iMac')]"))


    def scroll_to_review_tab(self):
        self.scroll((By.XPATH, "//a[contains(@href, '#tab-review')]"))