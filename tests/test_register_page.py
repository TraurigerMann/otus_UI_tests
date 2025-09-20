import allure

from page_objects.registration_page import RegistrationPage


@allure.feature("Регистрация")
@allure.title("Проверка интерактивности кнопки 'Продолжить'")
def test_continue_btn_is_clickable(browser):
    RegistrationPage(browser).is_continue_btn_clikable()


@allure.feature("Регистрация")
@allure.title("Регистрация нового пользователя")
def test_register_new_account(browser):
    RegistrationPage(browser) \
        .write_first_name() \
        .write_last_name() \
        .write_email() \
        .write_password() \
        .activate_privacy_checkbox() \
        .click_continue_btn() \
        .check_registration_success()