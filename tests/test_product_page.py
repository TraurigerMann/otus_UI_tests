from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_price_is_visible(browser, base_url):
    browser.get(f"{base_url}/product/desktops/mac/imac")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price-new")))


def test_add_to_cart_btn_is_visible(browser, base_url):
    browser.get(f"{base_url}/product/desktops/mac/macbook")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@id, 'button-cart')]")))


def test_specification_tab_is_visible(browser, base_url):
    browser.get(f"{base_url}/product/desktops/mac/macbook")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '#tab-specification')]")))


def test_btn_add_to_wish_list_is_visible(browser, base_url):
    browser.get(f"{base_url}/product/desktops/mac/macbook")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@title, 'Add to Wish List')]")))


def test_main_image_is_visible(browser, base_url):
    browser.get(f"{base_url}/product/desktops/mac/macbook")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@title, 'MacBook')]")))