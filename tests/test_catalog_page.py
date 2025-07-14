from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_link_is_visible(browser, base_url):
    browser.get(f"{base_url}/catalog/desktops/mac")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='iMac']")))


def test_compare_button_is_visible(browser, base_url):
    browser.get(f"{base_url}/catalog/desktops/mac")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//div[contains(@id, 'display-control')]/descendant::a[contains(@id, 'compare-total')]"
    )))

def test_product_add_to_wish_list_btn_is_visible(browser, base_url):
    browser.get(f"{base_url}/catalog/desktops/mac")
    wait = WebDriverWait(browser, 5, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//div[contains(@class, 'product-thumb')][1]/descendant::button[contains(@title, 'Add to Wish List')]"
    )))

def test_sort_dropdown_is_visible(browser, base_url):
    browser.get(f"{base_url}/catalog/desktops/mac")
    wait = WebDriverWait(browser, 3, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@id, 'input-sort')]")))


def test_home_btn_is_visible(browser, base_url):
    browser.get(f"{base_url}/catalog/desktops/mac")
    wait = WebDriverWait(browser, 3, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//ul[contains(@class, 'breadcrumb')]/descendant::a[substring-before(@href, 'home')]"
    )))


def test_price_currency_changing(browser, base_url):
    browser.get(f"{base_url}/catalog/desktops/mac")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'float-start')]//form"))).click()

    currency_eur = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'float-start')]//a[@href='EUR']")))

    currency_eur.click()

    product_price = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class='description']//span[@class='price-new']")))

    assert "€" in product_price.text
