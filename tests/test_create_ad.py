import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthLocators, AdCreationLocators

class TestCreateAdAuthorized:
    def test_create_ad_by_authorized_user(self, driver):
        driver.get("https://qa-desk.education-services.ru/")
        
        # Авторизация пользователя
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_REG_BUTTON)).click()
        
        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        email_field.send_keys("existing_user@gmail.com")
        
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT))
        password_field.send_keys("Password123")
        
        # Надежная отправка формы авторизации через JS-клик
        login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(AuthLocators.LOGIN_SUBMIT_BUTTON))
        driver.execute_script("arguments[0].click();", login_btn)
        
        # Ожидаем появления аватара профиля — признак успешного входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.USER_AVATAR))
        
        # Нажимаем "Разместить объявление"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.CREATE_AD_BUTTON)).click()
        
        # Заполнение текстовых полей формы создания товара
        title_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AdCreationLocators.TITLE_INPUT))
        title_field.send_keys("Игровой ноутбук")
        
        desc_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AdCreationLocators.DESCRIPTION_INPUT))
        desc_field.send_keys("В отличном состоянии, пользовался год.")
        
        price_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AdCreationLocators.PRICE_INPUT))
        price_field.send_keys("55000")
        
        # Клик по выпадающему списку категорий и выбор первой опции
        category_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdCreationLocators.CATEGORY_DROPDOWN)
        )
        category_dropdown.click()

        category_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AdCreationLocators.DROPDOWN_OPTION))
        category_option.click()
        
        # Клик по выпадающему списку городов и выбор первой опции
        city_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdCreationLocators.CITY_DROPDOWN)
        )
        city_dropdown.click()
        
        city_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AdCreationLocators.CITY_OPTION))
        city_option.click()
        
        # Выбор RadioButton состояния товара через JS-клик
        radio_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(AdCreationLocators.CONDITION_RADIO))
        driver.execute_script("arguments[0].click();", radio_button)
        
        # Публикация объявления
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AdCreationLocators.PUBLISH_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(AdCreationLocators.PUBLISH_BUTTON))

        # Переход в личный профиль и финальная проверка
        click_profile = WebDriverWait(driver, 10).until(EC.presence_of_element_located(AdCreationLocators.PROFILE_LINK))
        driver.execute_script("arguments[0].click();", click_profile)
        my_ads_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located(AdCreationLocators.MY_ADS_BLOCK)).text
        my_last_add_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located(AdCreationLocators.MY_LAST_ADD)).text

        assert "Мои объявления" in my_ads_text and "Игровой ноутбук" in my_last_add_text
