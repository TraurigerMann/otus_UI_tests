import allure

from faker import Faker
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage

faker = Faker()


class RegistrationPage(BasePage):


    def __init__(self, browser):
        super().__init__(browser)
        self.open_registration_page()


    @allure.step("Open registration page")
    def open_registration_page(self):
        self.browser.get(f"{self.base_url}index.php?route=account/register")
        self.logger.info("Opened registration page")
        return self


    @allure.step("Check if continue button is clickable")
    def is_continue_btn_clikable(self):
        self.get_clickable_element((By.XPATH, "//*[contains(text(),'Continue')]"))


    @allure.step("Write firstname")
    def write_first_name(self, name=faker.first_name()):
        self.input_value((By.XPATH, "//input[@name='firstname']"), name)
        return self


    @allure.step("Write lastname")
    def write_last_name(self, last_name=faker.last_name()):
        self.input_value((By.XPATH, "//input[@name='lastname']"), last_name)
        return self


    @allure.step("Write email")
    def write_email(self, email=faker.email()):
        self.input_value((By.XPATH, "//input[@name='email']"), email)
        return self


    @allure.step("Write password")
    def write_password(self, password=faker.password()):
        self.input_value((By.XPATH, "//input[@name='password']"), password)
        return self


    @allure.step("Activate privacy checkbox")
    def activate_privacy_checkbox(self):
        self.click((By.XPATH, "//input[@name='agree']"))
        return self


    @allure.step("Click on continue button")
    def click_continue_btn(self):
        self.click((By.XPATH, "//button[contains(text(), 'Continue')]"))
        return self


    @allure.step("Check registration successful status")
    def check_registration_success(self):
        self.get_element((By.XPATH, "//h1[contains(text(), 'Your Account Has Been Created!')]"))
