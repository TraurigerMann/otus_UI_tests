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


def test_admin_login(browser, base_url):
    browser.get(f"{base_url}/administration/")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    login_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id, 'input-username')]")))
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id, 'input-password')]")))
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),' Login')]")))

    login_input.send_keys(ADMIN_LOGIN)
    password_input.send_keys(ADMIN_PASSWORD)

    login_btn.click()

    logout_btn = wait.until(EC.visibility_of_element_located((By.XPATH,"//li[contains(@id, 'nav-logout')]")))
    assert logout_btn, "Not logged as admin"


def test_admin_logout(browser, base_url):
    browser.get(f"{base_url}/administration/")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    login_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id, 'input-username')]")))
    password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id, 'input-password')]")))
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),' Login')]")))

    login_input.send_keys(ADMIN_LOGIN)
    password_input.send_keys(ADMIN_PASSWORD)

    login_btn.click()

    logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@id, 'nav-logout')]")))
    logout_btn.click()

