import logging
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser, self.base_url, self.logging_state = browser
        self._config_logger()


    def _config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        if self.logging_state:
            os.makedirs("logs", exist_ok=True)
            module_logs_dir = os.path.join("logs", str(self.browser.test_page))
            os.makedirs(module_logs_dir, exist_ok=True)
            file_path = os.path.join(module_logs_dir, f"{self.browser.test_name}.log")
            file_handler = logging.FileHandler(file_path, mode='w', encoding='utf-8')
            file_handler.setFormatter(
                logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s]: %(message)s')
                )
            self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.browser.log_level)


    def _text_xpath(self, text):
        return f"//*[contains(text(), '{text}')]"


    def get_element(self, locator: tuple, timeout = 3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        


    def get_elements(self, locator: tuple, timeout = 3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))


    def get_clickable_element(self, locator: tuple, timeout = 3):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))


    def click(self, locator: tuple):
        self.logger.info(f"Clicked on {locator}")
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.4).click().perform()
        return self
    

    def input_value(self, locator: tuple, text: str):
        self.logger.info(f"Input text: '{text}' into {locator}")
        self.get_element(locator).click()
        self.get_element(locator).clear()

        for l in text:
            self.get_element(locator).send_keys(l)


    def scroll(self, locator: tuple):
        self.logger.info(f"Scrolled to {locator}")
        ActionChains(self.browser).scroll_to_element(self.get_element(locator)).perform()


    def alert_accept(self, timeout = 3):
        self.logger.info("Alert success shown")
        WebDriverWait(self.browser, timeout).until(EC.alert_is_present()).accept()


