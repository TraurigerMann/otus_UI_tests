import allure

from page_objects.administation_login_page import AdminLoginPage

ADMIN_LOGIN = "user"
ADMIN_PASSWORD = "bitnami"


@allure.title("Отображение поля ввода логина")
def test_username_input_is_visible(browser):
    AdminLoginPage(browser).get_login_input()


@allure.title("Отображение поля ввода пароля")
def test_password_input_is_visible(browser):
    AdminLoginPage(browser).get_password_input()


@allure.title("Отображение кнопки логина")
def test_login_btn_is_visible(browser):
    AdminLoginPage(browser).get_login_btn()


@allure.feature("Авторизация")
@allure.title("Авторизация в админ панель")
def test_admin_login(browser):
    AdminLoginPage(browser).login(ADMIN_LOGIN, ADMIN_PASSWORD) \
        .wait_logged_in()


@allure.feature("Авторизация")
@allure.title("Выход из админ панели")
def test_admin_logout(browser):
    AdminLoginPage(browser).login(ADMIN_LOGIN, ADMIN_PASSWORD) \
        .logout()
