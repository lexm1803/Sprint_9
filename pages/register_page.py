from allure import step
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.url_bilder import UrlBilder
from locators.register_page_locators import RegisterPageLocators


class RegisterPage(BasePage):

    @step('Открыть страницу регистрации')
    def open(self):
        self.open_page(UrlBilder.REGISTR_PAGE)
        return self
    
    @step('Заполнить имя {name}')
    def send_name(self, name):
        self.enter_text(RegisterPageLocators.INPUT_NAME, name)
        return self
    
    @step('Заполнить фамилию пользователя {last_name}')
    def send_last_name(self, last_name):
        self.enter_text(RegisterPageLocators.INPUT_LAST_NAME, last_name)
        return self
    
    @step('Заполнить имя пользователя {user_name}')
    def send_user_name(self, user_name):
        self.enter_text(RegisterPageLocators.INPUT_USER_NAME, user_name)
        return self
    
    @step('Заполнить почту пользователя {email}')
    def send_mail(self, email):
        self.enter_text(RegisterPageLocators.INPUT_EMAIL, email)
        return self
    
    @step('Заполнить поле пароля пользователя {password}')
    def send_password(self, password):
        self.enter_text(RegisterPageLocators.INPUT_PASSWORD, password)
        return self
    
    @step('Клик на кнопку "Создать аккаунт"')
    def click_register_button(self):
        self.click_js(RegisterPageLocators.REGISTER_BUTTON)
        
    @step('Получить заголовок страницы')
    def get_title(self):
        return self.get_text(RegisterPageLocators.TITLE)
    
    @step('Проверить, что пользователь находится на странице регистрации')
    def is_on_page(self):
        cur = self.driver.current_url
        return cur == UrlBilder.REGISTR_PAGE
    
    @step('Ожидание загрузки страницы')
    def loading_page(self):
        try:
            self.wait_to_text_to_be_present(RegisterPageLocators.TITLE, 'Регистрация')
        except TimeoutException as e:
            raise TimeoutException(f'Страница не загружена {e}')
        