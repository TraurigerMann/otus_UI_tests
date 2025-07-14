from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ADMIN_LOGIN = "user"
ADMIN_PASSWORD = "bitnami"


def test_login_btn_is_visible(browser, base_url):
    browser.get(f"{base_url}/administration/")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),' Login')]")))


def test_username_input_is_visible(browser, base_url):
    browser.get(f"{base_url}/administration/")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'input-username')]")))


def test_password_input_is_visible(browser, base_url):
    browser.get(f"{base_url}/administration/")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id, 'input-password')]")))


def test_login_header_is_visible(browser, base_url):
    browser.get(f"{base_url}/administration/")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'card-header')]")))

