import pytest
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from urls import *


@pytest.fixture(scope="function")
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.quit()

#пользователь с майл и паролем
@pytest.fixture(scope="function")
def user():
    return {
        "email": "mail5@mail.ru",
        "password": "54321"
    }
