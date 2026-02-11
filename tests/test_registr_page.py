import allure
from pages.auth_page import AuthPage
from pages.register_page import RegisterPage


@allure.epic('Регистрация')
@allure.feature('Проверки аутентификации. Регистрация.')
class TestAuthentication:

    @allure.title('Проверка регистрации пользователя')
    def test_register_user(self, register_page: RegisterPage, auth_page: AuthPage, user_data: dict):

        with allure.step('Заполнение формы регистрации'):
            (register_page.open()
             .send_name(user_data['name'])
             .send_last_name(user_data['last_name'])
             .send_user_name(user_data['user_name'])
             .send_mail(user_data['email'])
             .send_password(user_data['password']))
            
        with allure.step('Отправка формы регистрации'):
            register_page.click_register_button()
            auth_page.loading_page()

        with allure.step('Проверка отображения страницы авторизации'):
            assert auth_page.is_auth_form_visible()
