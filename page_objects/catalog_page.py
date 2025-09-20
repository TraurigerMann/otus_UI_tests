import allure

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.header_element import HeaderElement


class CatalogPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.open_catalog_page()


    @allure.step("Open catalog page")
    def open_catalog_page(self):
        self.browser.get(f"{self.base_url}/catalog/desktops/mac")
        self.logger.info("Opened catalog page")
        return self


    @allure.step("See product link")
    def get_product_link(self):
        self.get_element((By.XPATH, "//*[text()='iMac']"))



    @allure.step("See compare button")
    def get_compare_btn(self):
        self.get_element((By.XPATH,
        "//div[contains(@id, 'display-control')]/descendant::a[contains(@id, 'compare-total')]"
    ))


    @allure.step("See add to wishlist button")
    def get_add_to_wish_list_btn(self):
        self.get_element((
        By.XPATH,
        "//div[contains(@class, 'product-thumb')][1]/descendant::button[contains(@title, 'Add to Wish List')]"
    ))


    @allure.step("See sort dropdown")
    def get_sort_dropdown(self):
        self.get_element((By.XPATH, "//select[contains(@id, 'input-sort')]"))



    @allure.step("See home button")
    def get_home_btn(self):
        self.get_element((
        By.XPATH,
        "//ul[contains(@class, 'breadcrumb')]/descendant::a[substring-before(@href, 'home')]"
    ))


    @allure.step("See product price")
    def get_product_price(self):
        return self.get_element((By.XPATH, "//*[@class='description']//span[@class='price-new']"))


    @allure.step("Check for new currency in product price")
    def check_new_currency_applied(self):
        assert HeaderElement.new_currency in self.get_product_price().text


