from selenium.webdriver.common.by import By
import time
from locators import *
from conftest import *

# Тест успешного выхода из личного кабинета по кнопку "Выход"
def test_deauthorize_from_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
    driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
    driver.find_element(By.XPATH, login_button_authorization).click()

    driver.find_element(By.XPATH, personal_account_button).click()
    time.sleep(1)
    driver.find_element(By.XPATH, deauthorize_button).click()

    time.sleep(5)
    driver.quit()
#