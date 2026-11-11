import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from locators import MainPageLocators, AuthLocators, AdCreationLocators

@pytest.fixture
def driver():
    chrome_service = Service(executable_path='./chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=chrome_service, options=options)
    yield driver
    driver.quit()

@pytest.fixture
def random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}@gmail.com"

# Вспомогательная фикстура для логина (чтобы не дублировать код в тестах объявления и logout)
@pytest.fixture
def login_user(driver):
    def _login(email="existing_user@gmail.com", password="Password123"):
        driver.get("https://qa-desk.education-services.ru/")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REG_BUTTON)).click()
        
        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        email_field.send_keys(email)
        
        # Заменяем обычные find_element на WebDriverWait, чтобы избежать случайных падений
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT))
        password_field.send_keys(password)
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.LOGIN_SUBMIT_BUTTON)).click()
    return _login
