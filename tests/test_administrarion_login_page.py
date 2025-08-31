from page_objects.administation_login_page import AdminLoginPage

ADMIN_LOGIN = "user"
ADMIN_PASSWORD = "bitnami"


def test_username_input_is_visible(browser):
    AdminLoginPage(browser).open_admin_login_page() \
        .get_login_input()


def test_password_input_is_visible(browser):
    AdminLoginPage(browser).open_admin_login_page() \
        .get_password_input()


def test_login_btn_is_visible(browser):
    AdminLoginPage(browser).open_admin_login_page() \
        .get_login_btn()


def test_admin_login(browser):
    AdminLoginPage(browser).open_admin_login_page() \
        .login(ADMIN_LOGIN, ADMIN_PASSWORD) \
        .wait_logged_in()


def test_admin_logout(browser):
    AdminLoginPage(browser).open_admin_login_page() \
        .login(ADMIN_LOGIN, ADMIN_PASSWORD) \
        .logout()
