import allure
from allure import severity, severity_level
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.saucedemo_locators import LOCATORS


@allure.suite("Корзина и оформление заказа")
@allure.label("feature", "cart")
class TestCart:

    @allure.title("Очистка корзины от товара")
    @severity(severity_level.NORMAL)
    def test_clear_cart(self, logged_in_user, wait):
        driver = logged_in_user

        with allure.step("Добавить первый товар в корзину"):
            wait.until(EC.element_to_be_clickable(LOCATORS["first_item_add"])).click()

        with allure.step("Перейти в корзину и удалить товар"):
            wait.until(EC.element_to_be_clickable(LOCATORS["cart_link"])).click()
            remove_btn = wait.until(EC.element_to_be_clickable(LOCATORS["remove_item"]))
            remove_btn.click()

        with allure.step("Убедиться, что корзина пуста"):
            wait.until(EC.invisibility_of_element_located(LOCATORS["cart_items"]))
            assert len(driver.find_elements(*LOCATORS["cart_items"])) == 0
