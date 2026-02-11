from selenium.webdriver.common.by import By


class HeaderLocators:

    RECIPES = (By.XPATH, "//a[contains(@class, 'style_link__1kPh8 style_nav__link__2rAY6')]")
    LOGIN = (By.XPATH, "//a[contains(@class, 'style_link__1kPh8 styles_menuLink__3a59I')]")
    CREATE_ACCOUNT = (By.XPATH, "//a[contains(@class, 'style_link__1kPh8 styles_menuButton__1RUEF')]")
    
class AuthUserHeadersLocators:

    RECIPES = (By.CSS_SELECTOR, "ul a[href='/recipes']")
    SUBSCRIPTIONS = (By.CSS_SELECTOR, "ul a[href='/subscriptions']")
    CREATE_RECIPE = (By.CSS_SELECTOR, "ul a[href='/recipes/create']")
    FAVORITES = (By.CSS_SELECTOR, "ul a[href='/favorites']")
    SHOPPING_LIST = (By.CSS_SELECTOR, "ul a[href='/cart']")
    
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "ul a[href='/change-password']")
    EXIT = (By.XPATH, "//a[contains(@class, 'styles_menuLink__3a59I')][2]")