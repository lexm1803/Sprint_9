from allure import step
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.url_bilder import UrlBilder
from locators.auth_page_locators import AuthPagesLocators


class AuthPage(BasePage):

    @step('Открыть страницу авторизации')
    def open(self):
        self.open_page(UrlBilder.AUTH_PAGE)
        return self
    
    @step('Заполнить имя пользователя {user_name}')
    def send_user_name(self, user_name):
        self.enter_text(AuthPagesLocators.INPUT_MAIL, user_name)
        return self
    
    @step('Заполнить поле пароля пользователя {password}')
    def send_password(self, password):
        self.enter_text(AuthPagesLocators.INPUT_PASSWORD, password)
        return self
    
    @step('Клик на кнопку "Войти"')
    def click_login_button(self):
        self.click_js(AuthPagesLocators.LOGIN_BUTTON)
        
    @step('Получить заголовок страницы')
    def get_title(self):
        return self.get_text(AuthPagesLocators.TITLE)
    
    @step('Проверить, что пользователь находится на странице авторизации')
    def is_on_page(self):
        cur = self.driver.current_url
        return cur == UrlBilder.AUTH_PAGE
    
    @step('Ожидание загрузки страницы')
    def loading_page(self):
        try:
            self.wait_to_text_to_be_present(AuthPagesLocators.TITLE, 'Войти на сайт')
        except TimeoutException as e:
            raise TimeoutException(f'Страница не загружена {e}')
        
    @step('Проверка отображения формы авторизации')
    def is_auth_form_visible(self):
        try:
            title = self.get_text(AuthPagesLocators.TITLE)
            self.find_visible_element(AuthPagesLocators.INPUT_MAIL)
            self.find_visible_element(AuthPagesLocators.INPUT_PASSWORD)
            self.find_visible_element(AuthPagesLocators.LOGIN_BUTTON)
            return True if title == 'Войти на сайт' else False
        except Exception:
            return False
        