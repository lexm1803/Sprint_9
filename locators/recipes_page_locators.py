from selenium.webdriver.common.by import By


class RecipesPageLocators:

    TITLE = (By.TAG_NAME, "h1")

    CARD_TITLE_LIST = (By.XPATH, "//div[contains(@class, 'style_card__body')]//a[contains(@class, 'style_card__title')]")
    