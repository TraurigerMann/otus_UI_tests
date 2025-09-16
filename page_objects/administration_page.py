import allure

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    CATALOG_DROPDOWN = By.XPATH, "//*[contains(text(), ' Catalog')]"
    CATALOG_ITEM_PRODUCTS = By.XPATH, "//*[contains(text(),'Continue')]"
    PRODUCT_NAME_INPUT = By.XPATH, "//*[contains(@name, 'product_description[1][name]')]"


    def _item_name(self, item_name):
        return By.XPATH, self._text_xpath(item_name)


    @allure.step("Click on catalog")
    def click_catalog_dropdown(self):
        if not self.get_element(self.CATALOG_DROPDOWN):
            self.click((By.XPATH, "//*[@class='fa-bars']/i"))
        self.click(self.CATALOG_DROPDOWN)
        return self


    @allure.step("Click on item in catalog")
    def click_catalog_item(self, item_name):
        self.click(self._item_name(item_name))
        return self

    
    @allure.step("Click on add new item button")
    def click_add_btn(self):
        self.click((By.XPATH, "//*[contains(@class, 'fa-plus')]"))
        return self


    @allure.step("Click on save button")
    def click_save_btn(self):
        self.click((By.XPATH, "//*[contains(@class, 'fa-floppy-disk')]"))
        return self


    @allure.step("Click on data tab")
    def click_data_tab(self):
        self.click((By.XPATH, "//a[contains(text(), 'Data')]"))
        return self

    @allure.step("Click on SEO tab")
    def click_seo_tab(self):
        self.click((By.XPATH, "//a[text()='SEO']"))
        return self


    @allure.step("Click on back button")
    def click_back_btn(self):
        self.click((By.XPATH, "//*[contains(@class, 'fa-reply')]"))
        return self


    @allure.step("Click on filter")
    def click_filter_btn(self):
        self.click((By.XPATH, "//*[contains(@id, 'button-filter')]"))
        return self


    @allure.step("Activate product checkbox")
    def click_product_checkbox(self):
        self.click((By.XPATH, "//*[contains(@name, 'selected[]')]"))
        return self


    @allure.step("Click on delete button")
    def click_delete_btn(self):
        self.click((By.XPATH, "//*[contains(@class, 'fa-trash-can')]"))
        return self


    @allure.step("Write product name: {product_name}")
    def write_product_name(self, product_name):
        self.input_value((By.XPATH, "//*[contains(@name, 'product_description[1][name]')]"), product_name)
        return self


    @allure.step("Write meta tag: {tag}")
    def write_meta_tag(self, tag):
        self.input_value((By.XPATH, "//*[contains(@name, 'product_description[1][meta_title]')]"), tag)
        return self


    @allure.step("Write model name: {model_name}")
    def write_model_name(self, model_name):
        self.input_value((By.XPATH, "//*[contains(@id, 'input-model')]"), model_name)
        return self


    @allure.step("Write SEO url: {seo_url}")
    def write_seo_url(self, seo_url):
        self.input_value((By.XPATH, "//input[@name='product_seo_url[0][1]']"), seo_url)
        return self


    @allure.step("Write product name in filter: {product_name}")
    def write_product_to_filter(self, product_name):
        self.input_value((By.XPATH, "//*[contains(@id, 'input-name')]"), product_name)
        return self


    @allure.step(f"Scroll to meta tag")
    def scroll_to_meta_tag_input(self):
        self.scroll((By.XPATH, "//*[contains(@name, 'product_description[1][meta_title]')]"))
        return self
