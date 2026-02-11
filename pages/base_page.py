from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver: WebDriver, timeout=50):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver = driver, timeout = timeout)

    def open_page(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def click_js(self, locator):
        element = self.find_visible_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return elements
    
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def enter_file_path(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def is_element_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False
        
    def get_text(self, locator):
        return self.find_element(locator).text
    
    def wait_to_text_to_be_present(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element(locator, text))
            
    def find_element_by_text(self, locator, text):
        try:
            self.wait.until(lambda _: any(
                    text == el.text.strip()
                    for el in self.find_elements(locator)
                    if el.text.strip()
                ))
        
        except TimeoutException:
            all_texts = [el.text for el in self.find_elements(locator)]
            print(f"Все тексты на странице: {all_texts}")
            raise ValueError(f'Заголовок "{text}" не найден. Доступные: {all_texts}')