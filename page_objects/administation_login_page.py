import allure

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


    @allure.step("Open admin login page")
    def open_admin_login_page(self):
        self.browser.get(f"{self.base_url}administration/")
        self.logger.info("Opened admin page")
        return self


    @allure.step("See login button")
    def get_login_btn(self):
        return self.get_element(self.LOGIN_BTN)


    @allure.step("Wait to be logged in")
    def wait_logged_in(self):
        return self.get_element(self.LOGOUT_BTN)


    @allure.step("See login input")
    def get_login_input(self):
        return self.get_element(self.LOGIN_INPUT)


    @allure.step("See password input")
    def get_password_input(self):
        return self.get_element(self.PASSWORD_INPUT)

    @allure.step("Login into admin panel")
    def login(self, username, password):
        self.input_value(self.LOGIN_INPUT, username)
        self.input_value(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)
        self.logger.info("Logged in")
        return self

    @allure.step("Logout from admin panel")
    def logout(self):
        self.click(self.LOGOUT_BTN)
        self.logger.info("Logged out")
        return self