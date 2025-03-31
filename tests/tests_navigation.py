from selenium.webdriver.common.by import By
import time
from locators import *
from conftest import *

# Тест успешного перехода в "Личный кабинет" авторизованным пользователем
def test_navigate_to_personal_account_post_login(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
    driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
    driver.find_element(By.XPATH, login_button_authorization).click()

    driver.find_element(By.XPATH, personal_account_button).click()

    time.sleep(5)
    driver.quit()

# Тест успешного перехода на страницу "Конструктор" из личного кабинета по кнопке
def test_navigate_to_constructor_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, constructor_button).click()

    time.sleep(5)
    driver.quit()

# Тест успешного перехода на главную странциу из личного кабинета по логотипу Stellar Burgers
def test_navigate_to_constructor_page_by_logo_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.CSS_SELECTOR, logo_button).click()

    time.sleep(5)
    driver.quit()

# Тест успешного перехода в раздел "Булки" раздела "Коструктор"
def test_navigate_to_buns_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, fillings_section).click()
    time.sleep(1)
    driver.find_element(By.XPATH, buns_section).click()

    time.sleep(5)
    driver.quit()

# Тест успешного перехода в раздел "Соусы" раздела "Коструктор"
def test_navigate_to_sauces_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, sauces_section).click()

    time.sleep(5)
    driver.quit()

# Тест успешного перехода в раздел "Начинки" раздела "Коструктор"
def test_navigate_to_fillings_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, fillings_section).click()

    time.sleep(5)
    driver.quit()
#