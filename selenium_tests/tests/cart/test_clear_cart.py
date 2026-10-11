import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.saucedemo_locators import LOCATORS

def test_clear_cart(logged_in_user, wait):
    driver = logged_in_user
    
    wait.until(EC.element_to_be_clickable(LOCATORS["first_item_add"])).click()
    wait.until(EC.element_to_be_clickable(LOCATORS["cart_link"])).click()
    
    remove_btn = wait.until(EC.element_to_be_clickable(LOCATORS["remove_item"]))
    remove_btn.click()
    
    wait.until(EC.invisibility_of_element_located(LOCATORS["cart_items"]))
    
    assert len(driver.find_elements(*LOCATORS["cart_items"])) == 0