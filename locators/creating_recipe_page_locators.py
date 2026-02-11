from selenium.webdriver.common.by import By


class CreatingRecipePageLocators:

    TITLE = (By.TAG_NAME, "h1")

    INPUT_TITLE_RECIPE = (By.XPATH, "//div[contains(text(), 'Название рецепта')]/following-sibling::input")
    INPUT_TITLE_INGRIDIENTS = (By.XPATH, "//input[contains(@class, 'styles_ingredientsInput__1zzql')]")
    INPUT_LIST_INGRIDIENTS = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]/div")
    INPUT_QUANTITY_INGRIDIENTS = (By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue__2matT')]")
    BUTTON_ADD_INGRIDIENT = (By.XPATH, "//div[contains(@class, 'styles_ingredientAdd__3fc32')]")
    INPUT_COOKING_TIME = (By.XPATH, "//div[contains(text(), 'Время приготовления')]/following-sibling::input")
    INPUT_RECIPE_DESCRIPTION = (By.XPATH, "//textarea[contains(@class, 'styles_textareaField__1wfhC')]")
    BUTTON_UPLOADING_FILE = (By.XPATH, "//label[contains(text(), 'Загрузить фото')]/following-sibling::input[@type='file']")

    BUTTON_CREATING_RECIPE = (By.XPATH, "//button[contains(@class, 'style_button__1FFWl')]")
