import allure
from pages.auth_page import AuthPage
from pages.recipes_page import RecipesPage


class TestAuthorization:
    @allure.title('Проверка авторизации пользователя')
    def test_authorization_user(self, auth_page: AuthPage, recipes_page:RecipesPage, registred_user_data: dict):

        with allure.step('Заполнение формы авторизации'):
            (auth_page.open()
             .send_user_name(registred_user_data['user_name'])
             .send_password(registred_user_data['password']))
            
        with allure.step('Отправка формы авторизации'):
            auth_page.click_login_button()
            recipes_page.loading_page()

        with allure.step('Проверка отображения кнопки "Выход"'):
            assert recipes_page.get_title() == 'Рецепты'
            assert recipes_page.is_exit_button_visible()
