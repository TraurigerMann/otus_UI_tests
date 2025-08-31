from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminLoginPage(BasePage):
    LOGIN_BTN = By.XPATH, "//*[contains(text(),' Login')]"
    LOGOUT_BTN = By.XPATH, "//li[contains(@id, 'nav-logout')]"

    LOGIN_INPUT = By.XPATH, "//input[contains(@id, 'input-username')]"
    PASSWORD_INPUT = By.XPATH, "//input[contains(@id, 'input-password')]"


    def __init__(self, browser):
        super().__init__(browser)
        self.open_admin_login_page()


    def open_admin_login_page(self):
        self.browser.get(f"{self.base_url}administration/")
        return self


    def get_login_btn(self):
        return self.get_element(self.LOGIN_BTN)


    def wait_logged_in(self):
        return self.get_element(self.LOGOUT_BTN)


    def get_login_input(self):
        return self.get_element(self.LOGIN_INPUT)


    def get_password_input(self):
        return self.get_element(self.PASSWORD_INPUT)


    def login(self, username, password):
        self.input_value(self.LOGIN_INPUT, username)
        self.input_value(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)
        return self


    def logout(self):
        self.click(self.LOGOUT_BTN)
        return self