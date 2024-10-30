import pytest
from selenium import webdriver
from .page_objects import LoginPage, RegistrationPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def registration_page(driver, login_page):
    login_page.load()
    login_page.click_sign_in()
    login_page.click_register()
    return RegistrationPage(driver)