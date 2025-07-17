from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_continue_btn_is_clickable(browser, base_url):
    browser.get(f"{base_url}/index.php?route=account/register")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Continue')]")))
    btn.click()