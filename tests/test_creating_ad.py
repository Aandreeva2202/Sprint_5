import random


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import DoskaLocators
from urls import *
from helpers import *


class TestUserLogin:
    def test_ad_no_user(self, driver):
        driver.find_element(*DoskaLocators.AD_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(DoskaLocators.LOGIN_AD_POPUP))
        popup = driver.find_element(*DoskaLocators.LOGIN_AD_POPUP)
        assert popup.text == "Чтобы разместить объявление, авторизуйтесь"

    def test_ad_success(self, driver, user):
        #Авторизоваться под заранее созданным пользователем.
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(DoskaLocators.LOGIN_POPUP))
        driver.find_element(*DoskaLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*DoskaLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*DoskaLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(DoskaLocators.USER_NAME))
        driver.find_element(*DoskaLocators.AD_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(DoskaLocators.NEW_AD_PAGE))
        #Заполнить все поля формы: «Название», «Описание товара», «Стоимость»
        new_name = f"Тест{random.randint(100, 999)}"
        driver.find_element(*DoskaLocators.NAME_INPUT).send_keys(new_name)
        driver.find_element(*DoskaLocators.DESCRIPT_INPUT).send_keys('Спринт 5')
        driver.find_element(*DoskaLocators.PRICE_INPUT).send_keys(100)
        #выбираем категорию из выпадающего списка
        category_list = driver.find_element(*DoskaLocators.CATEGORY_DROPDOWN)
        category_list.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(DoskaLocators.DROPDOWN))
        category_input = driver.find_element(*DoskaLocators.CATEGORY_INPUT)
        category_input.click()
        #выбираем город из выпадающего списка
        city_list = driver.find_element(*DoskaLocators.CITY_DROPDOWN)
        city_list.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(DoskaLocators.DROPDOWN))
        city_input = driver.find_element(*DoskaLocators.CITY_INPUT)
        city_input.click()
        #Выбрать RabioButton «Состояние товара».
        conditions = [
            {"value": "Новый", "xpath": DoskaLocators.CONDITION_NEW},
            {"value": "Б/У", "xpath": DoskaLocators.CONDITION_USED}
        ]
        driver.find_element(By.XPATH, DoskaLocators.CONDITION_NEW_ACTIV).click()   #выключаем новый, который был включен по умолчанию
        selected_condition = random.choice(conditions)
        radio_button = driver.find_element(By.XPATH, selected_condition['xpath'])
        radio_button.click()
        #Нажать кнопку «Опубликовать».
        driver.find_element(*DoskaLocators.PUBLISH_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(DoskaLocators.HOME_PAGE))
        #Перейти в профиль пользователя.
        driver.find_element(*DoskaLocators.USER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(DoskaLocators.PROFILE_PAGE))
        footer = driver.find_element(*DoskaLocators.FOOTER)
        driver.execute_script("arguments[0].scrollIntoView();", footer)
        card_last = driver.find_element(*DoskaLocators.CARD_LAST)
        card_after = card_last.text
        assert new_name == card_after
