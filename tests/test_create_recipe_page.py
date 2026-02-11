import allure
from pages.creating_recipe_page import CreatingRecipePage
from pages.recipes_page import RecipesPage
from utils.generators import GenerateRecipe


@allure.epic('Создание рецептов')
@allure.feature('Создание рецепта, проверка его валидности')
class TestCreateRecipe:

    @allure.title('Создание рецепта. Проверка карточки рецепта на странице рецептов')
    def test_creating_recipe(self, creating_recipe_page_for_auth_user: CreatingRecipePage, recipes_page: RecipesPage):

        with allure.step('Создание рецепта'):
            create = creating_recipe_page_for_auth_user
            data = GenerateRecipe.generate_recipe_data()
            create.send_title_recipe(data["title"])
            for ing, val in data["ingredients"]:
                create.send_ingredient(ing, str(val))
            create.send_cooking_time(data["time"])
            create.send_description(data["description"])
            create.uploading_defolt_image()
            create.click_creating_recipe_button()
            recipes_page.open()
            recipes_page.refresh_page()
            recipes_page.loading_page()
            
        with allure.step('Проверка отображения созданного рецепта на странице рецетов'):
            assert recipes_page.is_title_visible(data["title"])
            