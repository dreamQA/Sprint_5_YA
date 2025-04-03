from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestLogin:
#Тест успешной авторизации по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, login_button).click()

        driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
        driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
        driver.find_element(By.XPATH, login_button_authorization).click()

        WebDriverWait(driver, 10).until(
            EC.url_changes("https://stellarburgers.nomoreparties.site/")
        )
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Авторизация удалась"

# Тест успешной авторизации по кнопке "Личный кабинет" с главной страницы
    def test_login_from_button_personal_account(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, personal_account_button).click()

        driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
        driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
        driver.find_element(By.XPATH, login_button_authorization).click()

        WebDriverWait(driver, 10).until(
            EC.url_changes("https://stellarburgers.nomoreparties.site")
        )

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Авторизация удалась"

# Тест успешной авторизации через кнопку "Войти" в форме регистрации
    def test_login_from_button_form_registration(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, login_button_registration).click()

        driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
        driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
        driver.find_element(By.XPATH, login_button_authorization).click()

        WebDriverWait(driver, 10).until(
            EC.url_changes("https://stellarburgers.nomoreparties.site")
        )
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Авторизация удалась"

# Тест успешной авторизации через кнопку "Войти" в форме восстановления пароля
    def test_login_from_button_form_password_recovery_form(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.XPATH, login_button_form_password_recovery).click()

        driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
        driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
        driver.find_element(By.XPATH, login_button_authorization).click()

        WebDriverWait(driver, 10).until(
            EC.url_changes("https://stellarburgers.nomoreparties.site")
        )
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Авторизация удалась"
#