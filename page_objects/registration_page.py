from faker import Faker
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage

faker = Faker()


class RegistrationPage(BasePage):
    FIRSTNAME = faker.first_name()
    LASTNAME = faker.last_name()
    EMAIL = faker.email()
    PASSWORD = faker.password()


    def __init__(self, browser):
        super().__init__(browser)
        self.open_registration_page()


    def open_registration_page(self):
        self.browser.get(f"{self.base_url}index.php?route=account/register")
        return self


    def is_continue_btn_clikable(self):
        self.get_clickable_element((By.XPATH, "//*[contains(text(),'Continue')]"))


    def write_first_name(self):
        self.input_value((By.XPATH, "//input[@name='firstname']"), self.FIRSTNAME)
        return self


    def write_last_name(self):
        self.input_value((By.XPATH, "//input[@name='lastname']"), self.LASTNAME)
        return self


    def write_email(self):
        self.input_value((By.XPATH, "//input[@name='email']"), self.EMAIL)
        return self


    def write_password(self):
        self.input_value((By.XPATH, "//input[@name='password']"), self.PASSWORD)
        return self


    def activate_privacy_checkbox(self):
        self.click((By.XPATH, "//input[@name='agree']"))
        return self


    def click_continue_btn(self):
        self.click((By.XPATH, "//button[contains(text(), 'Continue')]"))
        return self


    def check_registration_success(self):
        self.get_element((By.XPATH, "//h1[contains(text(), 'Your Account Has Been Created!')]"))
