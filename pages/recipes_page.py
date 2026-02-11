from allure import step
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.url_bilder import UrlBilder
from locators.recipes_page_locators import RecipesPageLocators
from locators.header_locators import AuthUserHeadersLocators


class RecipesPage(BasePage):

    @step('Открыть страницу рецептов')
    def open(self):
        self.open_page(UrlBilder.RESIPES_PAGE)

    @step('Получить заголовок страницы')
    def get_title(self):
        return self.get_text(RecipesPageLocators.TITLE)
    
    @step('Проверить, что пользователь находится на странице рецептов')
    def is_on_page(self):
        cur = self.driver.current_url
        return cur == UrlBilder.RESIPES_PAGE
    
    @step('Ожидание загрузки страницы')
    def loading_page(self):
        try:
            self.wait_to_text_to_be_present(RecipesPageLocators.TITLE, 'Рецепты')
        except TimeoutException as e:
            raise TimeoutException(f'Страница не загружена {e}')
    
    @step('Проверка наличия кнопки "Выход"')
    def is_exit_button_visible(self):
        try:
            self.find_visible_element(AuthUserHeadersLocators.EXIT)
            return True
        except Exception:
            return False
        
    @step('Клик на кнопку "Создать рецепт"')
    def click_creating_recipe_button(self):
        self.click_js(AuthUserHeadersLocators.CREATE_RECIPE)
        
    @step('Парсинг списка карточек рецептов')
    def get_list_card(self):
        elements = self.find_elements(RecipesPageLocators.CARD_TITLE_LIST)
        if not elements:
            raise ValueError('Список элементов пуст')
        return elements
    
    @step('Поиск заголовка {title} в карточках рецептов')
    def is_title_visible(self, title):
        try:
            self.get_card_by_title(title)
            return True
        except ValueError:
            return False
              
    @step('Поиск по заголовку "{title}" карточки в списке карточек рецептов')
    def get_card_by_title(self, title):
        self.find_visible_element(RecipesPageLocators.CARD_TITLE_LIST)
        self.find_element_by_text(RecipesPageLocators.CARD_TITLE_LIST, title)

        for el in self.find_elements(RecipesPageLocators.CARD_TITLE_LIST):
            if el.text.strip() == title:
                return el
        raise RuntimeError("Этого не должно быть")
