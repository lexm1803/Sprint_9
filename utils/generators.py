import random
import string


def user_data_generator():
    name = ''.join(random.choices(string.ascii_lowercase, k = 8)).capitalize()
    last_name = ''.join(random.choices(string.ascii_lowercase, k = 5)).capitalize()
    user_name = ''.join(random.choices(string.ascii_lowercase, k = 6)).capitalize()
    email = ''.join(random.choices(string.ascii_lowercase, k = 4)) + '@example.com'
    password = ''.join(random.choices(string.ascii_letters + string.digits, k = 12))

    return {
        "name": name,
        "last_name": last_name,
        "user_name": user_name,
        "email": email,
        "password": password,
    }

class GenerateRecipe:
    
    TITLES = [
        "Паста с томатами", "Овощной суп", "Курица по-домашнему",
        "Греческий салат", "Блинчики с творогом", "Тушёная капуста",
        "Запечённая рыба", "Гречка с грибами", "Омлет с сыром",
        "Морковные котлеты"
    ]

    DESCRIPTIONS = [
        "Простое и вкусное блюдо, которое можно приготовить за 20 минут.",
        "Идеально подходит для здорового питания и диеты.",
        "Отличный выбор для семейного ужина.",
        "Блюдо готовится из доступных ингредиентов.",
        "Подходит как для повседневного меню, так и для гостей."
    ]

    INGREDIENTS = [
        "картофель", "морковь", "лук", "чеснок", "помидоры", "огурцы",
        "курица", "говядина", "рыба", "яйца", "молоко", "сыр",
        "мука", "рис", "гречка", "макароны", "масло растительное",
        "масло сливочное", "соль", "перец", "зелень", "укроп", "петрушка"
    ]

    @staticmethod
    def generate_title():
        base = random.choice(GenerateRecipe.TITLES)
        suffix = ''.join(random.choices(string.ascii_lowercase, k=3))
        return f'{base} {suffix}'
    
    @staticmethod
    def generate_description():
        return random.choice(GenerateRecipe.DESCRIPTIONS)
    
    @staticmethod
    def generate_time():
        return str(random.randint(10, 120))
    
    @staticmethod
    def generate_ingredients(count = 2):
        select = random.sample(GenerateRecipe.INGREDIENTS, count)
        return [(ings, random.randint(50, 500)) for ings in select]
    
    @staticmethod
    def generate_recipe_data():
        ings = GenerateRecipe.generate_ingredients()
        return {
            "title": GenerateRecipe.generate_title(),
            "description": GenerateRecipe.generate_description(),
            "time": GenerateRecipe.generate_time(),
            "ingredients": ings,
        }
    