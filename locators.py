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
    
    # Находим блок дропдауна, который идет сразу за текстом заголовка поля
    CATEGORY_DROPDOWN = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[1]/button/*[local-name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']")
    CITY_DROPDOWN = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[3]/div[1]/button/*[local-name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']")

    # Универсальный локатор для выбора первого появившегося элемента в открывшемся списке опций
    DROPDOWN_OPTION = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[2]/button[5]/span[text()='Технологии']")
    CITY_OPTION = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[3]/div[2]/button[3]/span[text()='Новосибирск']")

    CONDITION_RADIO = (By.CSS_SELECTOR, "input[type='radio'][value='Б/У']")
    PUBLISH_BUTTON = (By.XPATH, "//*[contains(text(), 'Опубликовать')]")
    PROFILE_LINK = (By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/button")
    MY_ADS_BLOCK = (By.XPATH, "//*[contains(text(), 'Мои объявления')]")
    MY_LAST_ADD = (By.XPATH, "//*[@id='root']/div/div[2]/div[4]/div/div[1]/div[3][last()]")