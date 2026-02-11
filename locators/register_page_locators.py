from selenium.webdriver.common.by import By


class RegisterPageLocators:

    TITLE = (By.TAG_NAME, "h1")

    INPUT_NAME = (By.XPATH, "//input[contains(@name, 'first_name')]")
    INPUT_LAST_NAME = (By.XPATH, "//input[contains(@name, 'last_name')]")
    INPUT_USER_NAME = (By.XPATH, "//input[contains(@name, 'username')]")
    INPUT_EMAIL = (By.XPATH, "//input[contains(@name, 'email')]")
    INPUT_PASSWORD = (By.XPATH, "//input[contains(@name, 'password')]")

    REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'style_button__1FFWl')]")
    