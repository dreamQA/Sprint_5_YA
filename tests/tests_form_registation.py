from selenium.webdriver.common.by import By
import time
from locators import *
from conftest import *

# Тест успешной регистрации
def test_successful_registration(driver,generate_random_name, generate_random_email, generate_random_password):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    name = generate_random_name
    email = generate_random_email
    password = generate_random_password

    driver.find_element(By.XPATH, name_input).send_keys(name)
    driver.find_element(By.XPATH, email_input).send_keys(email)
    driver.find_element(By.CSS_SELECTOR, password_input).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, register_button).click()

    time.sleep(2)
    driver.quit()

# Тест-кейс на получение ошибки некорректного пароля (меньше 6 символов)
def test_registration_incorrect_password_error(driver,generate_random_name, generate_random_email):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    name = generate_random_name
    email = generate_random_email
    short_password = "qwert"

    driver.find_element(By.XPATH, name_input).send_keys(name)
    driver.find_element(By.XPATH, email_input).send_keys(email)
    driver.find_element(By.CSS_SELECTOR, password_input).send_keys(short_password)
    driver.find_element(By.CSS_SELECTOR, register_button).click()

    time.sleep(5)
    error_message_element = driver.find_element(By.XPATH, error_message)
    error_message_text = error_message_element.text
    # Проверка, что сообщение об ошибке содержит текст "Некорректный пароль"
    assert "Некорректный пароль" in error_message_text

    driver.quit()
#