from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser, self.base_url = browser


    def _text_xpath(self, text):
        return f"//*[contains(text(), '{text}')]"


    def get_element(self, locator: tuple, timeout = 3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))


    def get_elements(self, locator: tuple, timeout = 3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))


    def get_clickable_element(self, locator: tuple, timeout = 3):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))


    def click(self, locator: tuple):
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.4).click().perform()
        return self


    def input_value(self, locator: tuple, text: str):
        self.get_element(locator).click()
        self.get_element(locator).clear()

        for l in text:
            self.get_element(locator).send_keys(l)


    def scroll(self, locator: tuple):
        ActionChains(self.browser).scroll_to_element(self.get_element(locator)).perform()


    def alert_accept(self, timeout = 3):
        WebDriverWait(self.browser, timeout).until(EC.alert_is_present()).accept()


