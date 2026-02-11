from selenium.webdriver.common.by import By


class AuthPagesLocators:

    TITLE = (By.TAG_NAME, "h1")

    INPUT_MAIL = (By.XPATH, "//input[contains(@name, 'email')]")
    INPUT_PASSWORD = (By.XPATH, "//input[contains(@name, 'password')]")

    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'style_button__1FFWl')]")