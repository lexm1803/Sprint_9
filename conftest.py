import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from utils.generators import user_data_generator
from pages.register_page import RegisterPage
from pages.auth_page import AuthPage
from pages.recipes_page import RecipesPage
from pages.creating_recipe_page import CreatingRecipePage
from config import (
    BROWSER,
    HEADLESS,
    SELENIUM_MODE
)


@pytest.fixture
def driver():
    if BROWSER == 'chrome':
        options = ChromeOptions()
        if HEADLESS:
            options.add_argument('--headless=new')

        # Основные аргументы для стабильности
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)

        # для Docker/CI
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument('--disable-accelerated-2d-canvas')
        options.add_argument('--disable-accelerated-jpeg-decoding')

    elif BROWSER == 'firefox':
        options = FirefoxOptions()

        if HEADLESS:
            options.add_argument('--headless')

        # preferences для Firefox:
        options.set_preference('dom.webnotifications.enabled', False)
        options.set_preference('media.volume_scale', '0.0')

    else:
        raise RuntimeError('Этого не должно было произойти. (Проверь файл config.py)')

    if SELENIUM_MODE == 'remote':
        driver = webdriver.Remote(
            command_executor = 'http://localhost:4444/wd/hub',
            options = options,
        )
    else:
        if BROWSER == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service = service, options = options)
        else:
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service = service, options = options)
    
    driver.set_window_size(1920, 1080)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)
    yield driver 
    driver.quit()
    
@pytest.fixture
def user_data():
    return user_data_generator()

@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)

@pytest.fixture
def auth_page(driver):
    return AuthPage(driver)

@pytest.fixture
def recipes_page(driver):
    return RecipesPage(driver)

@pytest.fixture
def creating_recipe_page(driver):
    return CreatingRecipePage(driver)

@pytest.fixture
def registred_user_data(register_page, user_data):
    (register_page.open()
     .send_name(user_data['name'])
     .send_last_name(user_data['last_name'])
     .send_user_name(user_data['user_name'])
     .send_mail(user_data['email'])
     .send_password(user_data['password'])
     .click_register_button())
    return {
        'user_name': user_data['user_name'],
        'password': user_data['password']
    }

@pytest.fixture
def authorization_user(auth_page, registred_user_data, recipes_page):
    (auth_page.open()
     .send_user_name(registred_user_data['user_name'])
     .send_password(registred_user_data['password'])
     .click_login_button())
    recipes_page.loading_page()
    return recipes_page

@pytest.fixture
def creating_recipe_page_for_auth_user(authorization_user, creating_recipe_page):
    authorization_user.click_creating_recipe_button()
    creating_recipe_page.loading_page()
    return creating_recipe_page
