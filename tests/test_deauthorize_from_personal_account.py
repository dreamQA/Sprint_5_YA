from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestPersonalAccount:

    # Тест успешного выхода из личного кабинета по кнопке "Выход"
    def test_deauthorize_from_personal_account(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
        driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
        driver.find_element(By.XPATH, login_button_authorization).click()
        driver.find_element(By.XPATH, personal_account_button).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, personal_account_button))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, deauthorize_button))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )

        assert "login" in driver.current_url, "Пользователь не вышел из личного кабинета"