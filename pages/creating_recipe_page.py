from allure import step
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from utils.url_bilder import UrlBilder
from locators.creating_recipe_page_locators import CreatingRecipePageLocators
from locators.header_locators import AuthUserHeadersLocators
from config import ASSETS_DIR
from selenium.common.exceptions import StaleElementReferenceException


class CreatingRecipePage(BasePage):

    @step('Открыть страницу создания рецептов')
    def open(self):
        self.open_page(UrlBilder.CREATING_RECIPE_PAGE)

    @step('Получить заголовок страницы')
    def get_title(self):
        return self.get_text(CreatingRecipePageLocators.TITLE)
    
    @step('Проверить, что пользователь находится на странице создания рецептов')
    def is_on_page(self):
        cur = self.driver.current_url
        return cur == UrlBilder.CREATING_RECIPE_PAGE
    
    @step('Ожидание загрузки страницы')
    def loading_page(self):
        try:
            self.wait_to_text_to_be_present(CreatingRecipePageLocators.TITLE, 'Создание рецепта')
        except TimeoutException as e:
            raise TimeoutException(f'Страница не загружена {e}')
        
    @step('Добавить название рецепта: {title}')
    def send_title_recipe(self, title):
        self.enter_text(CreatingRecipePageLocators.INPUT_TITLE_RECIPE, title)
        return self 
    
    @step('Добавить ингридиент: {ingredient} -{quantity} г')
    def send_ingredient(self, ingredient, quantity):
        self.enter_text(CreatingRecipePageLocators.INPUT_TITLE_INGRIDIENTS, ingredient)
        self.find_visible_element(CreatingRecipePageLocators.INPUT_LIST_INGRIDIENTS)
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.find_element(CreatingRecipePageLocators.INPUT_LIST_INGRIDIENTS).click()
                break
            except StaleElementReferenceException:
                if attempt == max_retries - 1:
                    raise ValueError('Не удалось выбрать ингредиент')
        self.enter_text(CreatingRecipePageLocators.INPUT_QUANTITY_INGRIDIENTS, quantity)
        self.click_js(CreatingRecipePageLocators.BUTTON_ADD_INGRIDIENT)
        return self

    @step('Добавить время приготовления {cooking_time}')
    def send_cooking_time(self, cooking_time):
        self.enter_text(CreatingRecipePageLocators.INPUT_COOKING_TIME, cooking_time)
        return self
    
    @step('Добавить описание рецепта {description}')
    def send_description(self, description):
        self.enter_text(CreatingRecipePageLocators.INPUT_RECIPE_DESCRIPTION, description)
        return self
    
    @step('Загрузить фото рецепта {img_file_name}')
    def uploading_img(self, img_file_name):
        full_path = ASSETS_DIR / img_file_name
        if not full_path.exists():
            raise FileNotFoundError(f'Файл {full_path} не найден')
        self.enter_file_path(CreatingRecipePageLocators.BUTTON_UPLOADING_FILE, str(full_path))
        return self
    
    @step('Добавить стандартное изображение рецепта')
    def uploading_defolt_image(self):
        return self.uploading_img('defolt.jpg')
    
    @step('Осуществить клик по кнопке "Создание рецепта"')
    def click_creating_recipe_button(self):
        self.click_js(CreatingRecipePageLocators.BUTTON_CREATING_RECIPE)
        