import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators

class TestUserLogin:
    def test_successful_login(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        
        # Кликаем на кнопку "Вход и регистрация"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REG_BUTTON)).click()
        
        # Ожидаем появления и заполняем поле Email
        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        email_field.clear()
        email_field.send_keys("existing_user@gmail.com")
        
        # Ожидаем появления и заполняем поле Пароль
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT))
        password_field.clear()
        password_field.send_keys("Password123")
        
        # Кликаем на кнопку "Войти" через явное ожидание
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.LOGIN_SUBMIT_BUTTON)).click()
        
        # Проверяем успешный вход (аватар отображается, имя совпадает с учетом возможной точки)
        avatar_displayed = WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.USER_AVATAR)).is_displayed()
        user_name_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.USER_NAME)).text
        
        assert avatar_displayed is True
        assert "User" in user_name_text
