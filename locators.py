from selenium.webdriver.common.by import By

class MainPageLocators:
    # Ищем кнопки по тексту (с учетом регистра и возможных пробелов)
    LOGIN_REG_BUTTON = (By.XPATH, "//*[contains(text(), 'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//*[contains(text(), 'Разместить объявление')]")
    USER_AVATAR = (By.XPATH, "//img[contains(@class, 'avatar')] | //*[contains(@class, 'profile')] | //*[contains(@class, 'avatar')] | //img[@alt='avatar']") 
    USER_NAME = (By.XPATH, "//*[text()='User' or contains(text(), 'User')]")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(text(), 'Выйти')]")

class AuthLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(text(), 'Нет аккаунта')]")

    # Поля ввода на обеих формах (обычно тип email/password или name одинаковый)
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email'], input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'], input[name='password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Повторите пароль']")
    
    REG_SUBMIT_BUTTON = (By.XPATH, "//*[contains(text(), 'Создать аккаунт')]")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//form//button[contains(text(), 'Войти')] | //div[contains(@class, 'modal')]//button[contains(text(), 'Войти')]")
    
    ERROR_MESSAGE = (By.XPATH, "//*[text()='Ошибка' or contains(text(), 'Ошибка')]")
    
class AdCreationLocators:
    MODAL_HEADER = (By.XPATH, "//*[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    TITLE_INPUT = (By.CSS_SELECTOR, "input[name='title'], input[placeholder*='Название']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description'], textarea")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[type='number'], input[name='price']")
    
    # Находим блоки дропдауна
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")

    # Локаторы для выбора нужного элемента в открывшемся списке опций
    DROPDOWN_OPTION = (By.XPATH, "//button[.//span[text()='Технологии']]")
    CITY_OPTION = (By.XPATH, "//button[.//span[text()='Новосибирск']]")

    CONDITION_RADIO = (By.CSS_SELECTOR, "input[type='radio'][value='Б/У']")
    PUBLISH_BUTTON = (By.XPATH, "//*[contains(text(), 'Опубликовать')]")
    PROFILE_LINK = (By.CSS_SELECTOR, "button.circleSmall")
    MY_ADS_BLOCK = (By.XPATH, "//*[contains(text(), 'Мои объявления')]")
    MY_LAST_ADD = (By.XPATH, "//h2[@class='h2' and text()='Игровой ноутбук']")
