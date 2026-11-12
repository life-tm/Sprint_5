import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AdCreationLocators

class TestCreateAdUnauthorized:
    def test_create_ad_unauthorized_shows_modal(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.CREATE_AD_BUTTON)).click()
        
        modal_displayed = WebDriverWait(driver, 10).until(EC.presence_of_element_located(AdCreationLocators.MODAL_HEADER)).is_displayed()
        
        assert modal_displayed is True
