from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import random

def test_logo_is_visible(browser, base_url):
    browser.get(f"{base_url}/home")
    wait = WebDriverWait(browser, 3, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.ID, "logo")))


def test_product_add_to_card_btn_is_visible(browser,base_url):
    browser.get(f"{base_url}/home")
    wait = WebDriverWait(browser, 5, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//div[contains(@class, 'product-thumb')][1]/descendant::button[contains(@title, 'Add to Cart')]"
    )))



def test_cart_btn_is_visible(browser,base_url):
    browser.get(f"{base_url}/home")
    wait = WebDriverWait(browser, 3, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@id, 'header-cart')]/descendant::button")))


def test_search_btn_is_visible(browser,base_url):
    browser.get(f"{base_url}/home")
    wait = WebDriverWait(browser, 3, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@id, 'search')]/descendant::button")))


def test_product_link_is_clickable(browser, base_url):
    browser.get(f"{base_url}/home")
    wait = WebDriverWait(browser, 3, poll_frequency=1)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//div/descendant::a[text()='MacBook']")))


def test_add_random_product_to_cart(browser, base_url):
    browser.get(f"{base_url}/home")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    num_of_products = len(browser.find_elements(By.XPATH, "//*[@class='col mb-3']"))
    random_product_num = random.randint(1, num_of_products)

    add_to_cart_btn_home = wait.until(EC.visibility_of_element_located((
        By.XPATH, f"//*[@class='col mb-3'][{random_product_num}]//button[@title='Add to Cart']"
    )))

    add_to_cart_btn_home.location_once_scrolled_into_view
    sleep(1)
    add_to_cart_btn_home.click()

    cart_items = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header-cart']//button[contains(text(), ' 1 item(s)')]")))

    assert cart_items.text != " 0 item(s) - $0.00"
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'alert-success')]")))


def test_price_currency_changing(browser, base_url):
    browser.get(f"{base_url}/home")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'float-start')]//form"))).click()

    currency_eur = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'float-start')]//a[@href='EUR']")))

    currency_eur.click()

    cart_items = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='header-cart']//button[contains(text(), '€')]")))

    assert cart_items
