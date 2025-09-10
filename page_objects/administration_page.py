from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    CATALOG_DROPDOWN = By.XPATH, "//*[contains(text(), ' Catalog')]"
    CATALOG_ITEM_PRODUCTS = By.XPATH, "//*[contains(text(),'Continue')]"
    PRODUCT_NAME_INPUT = By.XPATH, "//*[contains(@name, 'product_description[1][name]')]"


    def _item_name(self, item_name):
        return By.XPATH, self._text_xpath(item_name)


    def click_catalog_dropdown(self):
        self.click(self.CATALOG_DROPDOWN)
        return self


    def click_catalog_item(self, item_name):
        self.click(self._item_name(item_name))
        return self


    def click_add_btn(self):
        self.click((By.XPATH, "//*[contains(@class, 'fa-plus')]"))
        return self


    def click_save_btn(self):
        self.click((By.XPATH, "//*[contains(@class, 'fa-floppy-disk')]"))
        return self


    def click_data_tab(self):
        self.click((By.XPATH, "//a[contains(text(), 'Data')]"))
        return self

    def click_seo_tab(self):
        self.click((By.XPATH, "//a[text()='SEO']"))
        return self

    def click_back_btn(self):
        self.click((By.XPATH, "//*[contains(@class, 'fa-reply')]"))
        return self

    def click_filter_btn(self):
        self.click((By.XPATH, "//*[contains(@id, 'button-filter')]"))
        return self


    def click_product_checkbox(self):
        self.click((By.XPATH, "//*[contains(@name, 'selected[]')]"))
        return self

    def click_delete_btn(self):
        self.click((By.XPATH, "//*[contains(@class, 'fa-trash-can')]"))
        return self


    def write_product_name(self, product_name):
        self.input_value((By.XPATH, "//*[contains(@name, 'product_description[1][name]')]"), product_name)
        return self


    def write_meta_tag(self, tag):
        self.input_value((By.XPATH, "//*[contains(@name, 'product_description[1][meta_title]')]"), tag)
        return self

    def write_model_name(self, model_name):
        self.input_value((By.XPATH, "//*[contains(@id, 'input-model')]"), model_name)
        return self

    def write_seo_url(self, seo_url):
        self.input_value((By.XPATH, "//input[@name='product_seo_url[0][1]']"), seo_url)
        return self

    def write_product_to_filter(self, product_name):
        self.input_value((By.XPATH, "//*[contains(@id, 'input-name')]"), product_name)
        return self


    def scroll_to_meta_tag_input(self):
        self.scroll((By.XPATH, "//*[contains(@name, 'product_description[1][meta_title]')]"))
        return self
