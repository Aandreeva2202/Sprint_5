from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import DoskaLocators
from urls import *
from helpers import *


class TestUserRegistration:
    def test_user_registration_success(self, driver):
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(DoskaLocators.LOGIN_POPUP))
        driver.find_element(*DoskaLocators.NO_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(DoskaLocators.REGISTRATION_POPUP))
        mail = random_mail()
        driver.find_element(*DoskaLocators.EMAIL_INPUT).send_keys(f'{mail}@example.com')
        driver.find_element(*DoskaLocators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*DoskaLocators.SUBMIT_PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*DoskaLocators.CREATE_ACCOUNT_BUTTON).click()
        user_name = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(DoskaLocators.USER_NAME))
        avatar_element = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(DoskaLocators.USER_BUTTON))
        current_url = driver.current_url
        assert current_url == url_regiatration and user_name.text == "User." and avatar_element.is_displayed()

    def test_user_registration_fail(self, driver):
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(DoskaLocators.LOGIN_POPUP))
        driver.find_element(*DoskaLocators.NO_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(DoskaLocators.REGISTRATION_POPUP))
        mail = random_mail()
        driver.find_element(*DoskaLocators.EMAIL_INPUT).send_keys(mail)
        driver.find_element(*DoskaLocators.CREATE_ACCOUNT_BUTTON).click()
        error_message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(DoskaLocators.EMAIL_ERROR))
        email_field = driver.find_element(*DoskaLocators.EMAIL_FIELD)
        password_field = driver.find_element(*DoskaLocators.PASSWORD_FIELD)
        submit_password_field = driver.find_element(*DoskaLocators.SUBMIT_PASSWORD_FIELD)
        color_email = email_field.value_of_css_property("border")
        color_password = password_field.value_of_css_property("border")
        color_submit_password = submit_password_field.value_of_css_property("border")
        assert "rgb(255, 105, 114)" in color_email and "rgb(255, 105, 114)" in color_password and "rgb(255, 105, 114)" in color_submit_password and error_message.text == "Ошибка"

    def test_user_registration_existing(self, driver, user):
        driver.find_element(*DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(DoskaLocators.LOGIN_POPUP))
        driver.find_element(*DoskaLocators.NO_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(DoskaLocators.REGISTRATION_POPUP))
        driver.find_element(*DoskaLocators.EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*DoskaLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*DoskaLocators.SUBMIT_PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*DoskaLocators.CREATE_ACCOUNT_BUTTON).click()
        error_message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(DoskaLocators.EMAIL_ERROR))
        email_field = driver.find_element(*DoskaLocators.EMAIL_FIELD)
        password_field = driver.find_element(*DoskaLocators.PASSWORD_FIELD)
        submit_password_field = driver.find_element(*DoskaLocators.SUBMIT_PASSWORD_FIELD)
        color_email = email_field.value_of_css_property("border")
        color_password = password_field.value_of_css_property("border")
        color_submit_password = submit_password_field.value_of_css_property("border")
        assert "rgb(255, 105, 114)" in color_email and "rgb(255, 105, 114)" in color_password and "rgb(255, 105, 114)" in color_submit_password and error_message.text == "Ошибка"
