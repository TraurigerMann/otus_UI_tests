from page_objects.administation_login_page import AdminLoginPage
from page_objects.administration_page import AdminPage
from page_objects.alert_element import AlertSuccessElement

ADMIN_LOGIN = "user"
ADMIN_PASSWORD = "bitnami"
PRODUCT_NAME = "Test name"
TAG = "Test tag"
MODEL_NAME = "Model one"
SEO_URL = "abc-124"


def test_add_new_product(browser, product_cleanup):

    AdminLoginPage(browser) \
        .login(ADMIN_LOGIN, ADMIN_PASSWORD)
    AdminPage(browser) \
        .click_catalog_dropdown() \
        .click_catalog_item("Products") \
        .click_add_btn() \
        .write_product_name(PRODUCT_NAME) \
        .scroll_to_meta_tag_input() \
        .write_meta_tag(TAG) \
        .click_data_tab() \
        .write_model_name(MODEL_NAME) \
        .click_seo_tab() \
        .write_seo_url(SEO_URL) \
        .click_save_btn()
    AlertSuccessElement(browser)

    product_cleanup(PRODUCT_NAME)


def test_delete_product(browser, product_create):

    product_create(ADMIN_LOGIN, ADMIN_PASSWORD, PRODUCT_NAME, TAG, MODEL_NAME, SEO_URL)

    AdminPage(browser).click_back_btn() \
        .write_product_to_filter(PRODUCT_NAME) \
        .click_filter_btn() \
        .click_product_checkbox() \
        .click_delete_btn() \
        .alert_accept()
    AlertSuccessElement(browser)