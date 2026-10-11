import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.saucedemo_locators import LOCATORS

def test_successful_purchase(logged_in_user, wait):
    driver = logged_in_user
    
    driver.find_element(*LOCATORS["first_item_add"]).click()
    driver.find_element(*LOCATORS["cart_link"]).click()
    
    checkout_btn = wait.until(EC.element_to_be_clickable(LOCATORS["checkout_button"]))
    checkout_btn.click()
    
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Alex")
    wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys("User")
    wait.until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys("12345")
    
    # Используем отдельный локатор для кнопки Continue
    continue_btn = wait.until(EC.element_to_be_clickable(LOCATORS["continue_button"]))
    continue_btn.click()
    
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    
    finish_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Finish']")))
    finish_btn.click()
    
    assert wait.until(EC.presence_of_element_located(LOCATORS["order_complete"])).text == "Thank you for your order!"
    assert "checkout-complete" in driver.current_url