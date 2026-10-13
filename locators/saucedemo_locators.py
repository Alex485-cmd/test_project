from selenium.webdriver.common.by import By

LOCATORS = {
    "username": (By.ID, "user-name"),
    "password": (By.ID, "password"),
    "login_button": (By.ID, "login-button"),
    "error_message": (By.CSS_SELECTOR, ".error-message-container"),
    "first_item_add": (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_primary"),
    "cart_link": (By.CSS_SELECTOR, ".shopping_cart_container"),
    "cart_items": (By.CSS_SELECTOR, ".cart_item"),
    "remove_item": (By.CSS_SELECTOR, ".cart_button"),
    "checkout_button": (By.CSS_SELECTOR, ".checkout_button"),
    "continue_button": (By.CSS_SELECTOR, ".cart_button"),
    "order_complete": (By.CSS_SELECTOR, ".complete-header")
}