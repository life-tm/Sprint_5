import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators

class TestRegistrationInvalidEmail:
    def test_registration_with_invalid_email_mask(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REG_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BUTTON)).click()

        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        email_field.send_keys("invalid_email_mask")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthLocators.REG_SUBMIT_BUTTON)).click()

        error_msg_displayed = WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthLocators.ERROR_MESSAGE)).is_displayed()
        email_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthLocators.EMAIL_INPUT))
        parent_class = email_element.find_element(By.XPATH, "./..").get_attribute("class")

        assert error_msg_displayed is True
        assert "error" in parent_class or "Error" in parent_class
