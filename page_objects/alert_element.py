import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertSuccessElement:
    SUCCESS_ALERT = By.CSS_SELECTOR, ".alert-success"
    LOGIN_LINK = By.LINK_TEXT, "login"
    SHOPPING_CART_LINK = By.LINK_TEXT, "shopping cart"
    COMPARISON_LINK = By.LINK_TEXT, "product comparison"

    def __init__(self, browser):
        self.browser = browser[0]
        self.alert = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located(self.SUCCESS_ALERT))


    @allure.step("Check access alert is presented")
    @property
    def success(self):
        return self.alert.find_element(*self.LOGIN_LINK)


    @allure.step("Check shopping cart link is presented in alert")
    @property
    def shopping_cart(self):
        return self.alert.find_element(*self.SHOPPING_CART_LINK)


    @allure.step("Check comparison link is presented in alert")
    @property
    def comparison(self):
        return self.alert.find_element(*self.COMPARISON_LINK)