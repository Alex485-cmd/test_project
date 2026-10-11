
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from locators.saucedemo_locators import LOCATORS
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    opts = Options()
    
    # ГЛАВНОЕ: режим инкогнито. В нём Chrome не имеет доступа к сохранённым паролям,
    # поэтому проверка на утечки (leak detection) просто не запускается.
    opts.add_argument("--incognito")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "credential_manager_enabled": False,
        "profile.password_manager_prompts_enabled": False
    }
    opts.add_experimental_option("prefs", prefs)

    # Страховочные аргументы на случай, если Chrome решит проявить инициативу
    opts.add_argument("--disable-features=PasswordLeakDetection,PasswordImport,CredentialManager")
    opts.add_argument("--disable-password-leak-detection")

    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def logged_in_user(driver, wait):
    driver.get("https://www.saucedemo.com")
    
    username_input = driver.find_element(*LOCATORS["username"])
    password_input = driver.find_element(*LOCATORS["password"])
    login_btn = driver.find_element(*LOCATORS["login_button"])
    
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_btn.click()
    
    assert "inventory.html" in driver.current_url
    
    return driver