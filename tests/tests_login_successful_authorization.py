from selenium.webdriver.common.by import By
import time
from locators import *
from conftest import *

#Тест успешной авторизации по кнопке «Войти в аккаунт» на главной
def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, login_button_main).click()

    driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
    driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
    driver.find_element(By.XPATH, login_button_authorization).click()

    time.sleep(5)
    driver.quit()

# Тест успешной авторизации по кнопке "Личный кабинет" с главной страницы
def test_login_from_button_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, personal_account_button).click()

    driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
    driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
    driver.find_element(By.XPATH, login_button_authorization).click()

    time.sleep(5)
    driver.quit()

# Тест успешной авторизации через кнопку "Войти" в форме регистрации
def test_login_from_button_form_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, login_button_registration).click()

    driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
    driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
    driver.find_element(By.XPATH, login_button_authorization).click()

    time.sleep(5)
    driver.quit()

# Тест успешной авторизации через кнопку "Войти" в форме восстановления пароля
def test_login_from_button_form_password_recovery_form(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.XPATH, login_button_form_password_recovery).click()

    driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
    driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
    driver.find_element(By.XPATH, login_button_authorization).click()

    time.sleep(5)
    driver.quit()
#