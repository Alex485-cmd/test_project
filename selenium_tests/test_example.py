from locators.main_page import MainPageLocators
from fixtures.conftest import driver

def test_open_google(driver):
    driver.get("https://www.google.com")
    assert MainPageLocators.TITLE in driver.title
