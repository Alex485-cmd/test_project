from locators.saucedemo_locators import LOCATORS
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_unsuccessful_auth(driver, wait):
    driver.get("https://www.saucedemo.com")
    driver.find_element(*LOCATORS["username"]).send_keys("wrong_user")
    driver.find_element(*LOCATORS["password"]).send_keys("wrong_pass")
    driver.find_element(*LOCATORS["login_button"]).click()

    error = wait.until(EC.presence_of_element_located(LOCATORS["error_message"]))
    assert "Epic sadface" in error.text