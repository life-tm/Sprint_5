import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators

class TestUserRegistration:
    def test_successful_registration(self, driver, random_email):
        driver.get("https://qa-desk.education-services.ru/")
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REG_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        
        # Ожидаем появления полей ввода
        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        email_field.send_keys(random_email)
        
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT))
        password_field.send_keys("ValidPassword123")
        
        confirm_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.CONFIRM_PASSWORD_INPUT))
        confirm_field.send_keys("ValidPassword123")
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.REG_SUBMIT_BUTTON)).click()
        
        # Проверяем успешную авторизацию после регистрации
        avatar_displayed = WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.USER_AVATAR)).is_displayed()
        user_name_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.USER_NAME)).text
        
        assert avatar_displayed is True
        assert "User" in user_name_text
