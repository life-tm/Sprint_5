import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators

class TestUserLogout:
    def test_successful_logout(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REG_BUTTON)).click()
        
        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        email_field.send_keys("existing_user@gmail.com")
        
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT))
        password_field.send_keys("Password123")
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.LOGIN_SUBMIT_BUTTON)).click()
        
        # Ждем, пока кнопка Выйти станет кликабельной
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGOUT_BUTTON)).click()
        
        login_btn_displayed = WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.LOGIN_REG_BUTTON)).is_displayed()
        
        assert login_btn_displayed is True
