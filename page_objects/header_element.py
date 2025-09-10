from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HeaderElement(BasePage):
    new_currency = ""

    def _get_current_currency(self):
        return self.get_element((By.XPATH, "//*[contains(@class, 'float-start')]//strong")).text

    def click_currency_dropdown(self):
        self.click((By.XPATH, "//*[contains(@class, 'float-start')]//form"))
        return self

    def set_new_currency(self):
        currency = ["€", "$", "£"]

        for c in currency:
            if c != self._get_current_currency():
                self.new_currency = c
                return self.click((By.XPATH, f"//*[contains(@class, 'float-start')]//a[contains(text(), '{c}')]"))

        return self