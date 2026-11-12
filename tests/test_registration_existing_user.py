import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators

class TestRegistrationExistingUser:
    def test_registration_already_existing_user(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REG_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        
        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        email_field.send_keys("existing_user@gmail.com")
        
        # Добавляем ожидания для полей паролей, чтобы избежать no such element
        pass_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT))
        pass_field.send_keys("Password123")
        
        confirm_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.CONFIRM_PASSWORD_INPUT))
        confirm_field.send_keys("Password123")
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.REG_SUBMIT_BUTTON)).click()
        
        error_msg_displayed = WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthLocators.ERROR_MESSAGE)).is_displayed()
        
        assert error_msg_displayed is True
