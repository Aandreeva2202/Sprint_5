from selenium.webdriver.common.by import By


#локаторы XPATH
class DoskaLocators:
    #кнопка вход и регистрация
    LOGIN_AND_REGISTRATION_BUTTON = By.XPATH, './/button[text()="Вход и регистрация"]'
    #кнопка Создать аккаунт
    AD_BUTTON = By.XPATH, './/button[text()="Разместить объявление"]'
    #кнопка войти
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"
    #кнопка нет аккаунта
    NO_ACCAUNT_BUTTON = By.XPATH, ".//button[text()='Нет аккаунта']"
    # окно регистрации
    REGISTRATION_POPUP = By.XPATH, ".//h1[text()='Зарегистрироваться']"
    #поле Введите Email
    EMAIL_INPUT = By.XPATH, ".//input[@placeholder='Введите Email']"
    EMAIL_FIELD = By.XPATH, ".//input[@placeholder='Введите Email']/.."
    #поле Пароль
    PASSWORD_INPUT = By.XPATH, ".//input[@placeholder='Пароль']"
    PASSWORD_FIELD = By.XPATH, ".//input[@placeholder='Пароль']/.."
    #поле Повторите пароль
    SUBMIT_PASSWORD_INPUT = By.XPATH, ".//input[@placeholder='Повторите пароль']"
    SUBMIT_PASSWORD_FIELD = By.XPATH, ".//input[@placeholder='Повторите пароль']/.."
    #кнопка Создать аккаунт
    CREATE_ACCOUNT_BUTTON = By.XPATH, ".//button[text()='Создать аккаунт']"
    #кнопка Выйти
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выйти']"
    #текст Ошибка
    EMAIL_ERROR = By.XPATH, ".//span[text()='Ошибка']"
    #окно "Войти"
    LOGIN_POPUP = By.XPATH, ".//h1[text()='Войти']"
    #user на главной странице
    USER_NAME = By.XPATH, ".//h3[text()='User.']"
    #окно "Войти для создания объявления"
    LOGIN_AD_POPUP = By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']"
    #новое объявление
    NEW_AD_PAGE = By.XPATH, ".//h1[text()='Новое объявление']"
    #поля ввода создания объявления
    NAME_INPUT = By.XPATH, ".//input[@placeholder='Название']"
    DESCRIPT_INPUT = By.XPATH, ".//textarea[@name='description']"
    PRICE_INPUT = By.XPATH, ".//input[@placeholder='Стоимость']"
    CATEGORY_DROPDOWN = By.XPATH, ".//input[@name='category']/following-sibling::button"
    CATEGORY_INPUT = By.XPATH, ".//span[text()= 'Книги']"
    CITY_DROPDOWN = By.XPATH, ".//input[@name='city']/following-sibling::button"
    CITY_INPUT = By.XPATH, ".//span[text()= 'Казань']"
    CONDITION_INPUTRADIO = By.XPATH, ".//h3[text()='Состояние товара:']"
    CONDITION_NEW_ACTIV = ".//div[@class='radioUnput_shell__Wtdwe'][./input[@value='Новый']]//div[@class='radioUnput_inputActive__eC-HY']"
    CONDITION_NEW = ".//div[@class='radioUnput_shell__Wtdwe'][./input[@value='Новый']]//div[@class='radioUnput_inputRegular__FbVbr']"
    CONDITION_USED = ".//div[@class='radioUnput_shell__Wtdwe'][./input[@value='Б/У']]//div[@class='radioUnput_inputRegular__FbVbr']"
    #кнопка Опубликовать
    PUBLISH_BUTTON = By.XPATH, ".//button[text()='Опубликовать']"
    #переход на страницу пользователя
    USER_BUTTON = By.XPATH, ".//button[@class='circleSmall']"
    #последнее объявление
    CARD_LAST = By.XPATH, './/div[@class="card"][last()]//div[@class="about"]//h2'
    #футер
    FOOTER = By.XPATH, ".//div[@class='App_linkBlock__RGu0p']"
