import allure
from allure import severity, severity_level
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.saucedemo_locators import LOCATORS


@allure.suite("Корзина и оформление заказа")
@allure.label("feature", "checkout")
class TestCheckout:

    @allure.title("Успешная покупка товара")
    @severity(severity_level.CRITICAL)
    def test_successful_purchase(self, logged_in_user, wait):
        driver = logged_in_user

        with allure.step("Добавить товар в корзину и перейти к оформлению"):
            driver.find_element(*LOCATORS["first_item_add"]).click()
            driver.find_element(*LOCATORS["cart_link"]).click()

        with allure.step("Нажать кнопку Checkout"):
            checkout_btn = wait.until(EC.element_to_be_clickable(LOCATORS["checkout_button"]))
            checkout_btn.click()

        with allure.step("Заполнить данные покупателя"):
            wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Alex")
            wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys("User")
            wait.until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys("12345")

        with allure.step("Подтвердить данные и перейти к финальному экрану"):
            continue_btn = wait.until(EC.element_to_be_clickable(LOCATORS["continue_button"]))
            continue_btn.click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))

        with allure.step("Завершить покупку"):
            finish_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Finish']")))
            finish_btn.click()

        with allure.step("Проверить успешное завершение заказа"):
            assert wait.until(EC.presence_of_element_located(LOCATORS["order_complete"])).text == "Thank you for your order!"
            assert "checkout-complete" in driver.current_url
