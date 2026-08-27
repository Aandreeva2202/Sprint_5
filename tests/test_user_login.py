from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import DoskaLocators
from urls import *
from helpers import *

class TestUserLogin:
    def test_user_login(self, driver, user):
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Войти']")))
        driver.find_element(*DoskaLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*DoskaLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*DoskaLocators.LOGIN_BUTTON).click()
        user_name = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h3[text()='User.']")))
        avatar_element = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='circleSmall']")))
        current_url = driver.current_url
        assert current_url == url_login and user_name.text == "User." and avatar_element.is_displayed()

    def test_user_logout(self, driver, user):
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Войти']")))
        driver.find_element(*DoskaLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*DoskaLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*DoskaLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h3[text()='User.']")))
        driver.find_element(*DoskaLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Вход и регистрация"]')))
        login_and_registrtion = driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON)
        assert login_and_registrtion.text == 'Вход и регистрация'
