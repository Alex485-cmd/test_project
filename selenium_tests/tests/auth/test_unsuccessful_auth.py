import allure
from allure import severity, severity_level
from locators.saucedemo_locators import LOCATORS
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@allure.suite("Авторизация")
@allure.label("feature", "login")
def test_unsuccessful_auth(driver, wait):
    with allure.step("Открыть страницу входа"):
        driver.get("https://www.saucedemo.com")

    with allure.step("Ввести неверные учетные данные"):
        driver.find_element(*LOCATORS["username"]).send_keys("wrong_user")
        driver.find_element(*LOCATORS["password"]).send_keys("wrong_pass")
        driver.find_element(*LOCATORS["login_button"]).click()

    with allure.step("Проверить отображение сообщения об ошибке"):
        error = wait.until(EC.presence_of_element_located(LOCATORS["error_message"]))
        assert "Epic sadface" in error.text
