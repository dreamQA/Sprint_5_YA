from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestRegistrationForm:
# Тест успешной регистрации
    def test_successful_registration(self,driver,generate_random_name, generate_random_email,generate_random_password):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        name = generate_random_name
        email = generate_random_email
        password = generate_random_password

        driver.find_element(By.XPATH, name_input).send_keys(name)
        driver.find_element(By.XPATH, email_input).send_keys(email)
        driver.find_element(By.XPATH, password_input).send_keys(password)
        driver.find_element(By.XPATH, register_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_changes("https://stellarburgers.nomoreparties.site/register")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Регистрация удалась"


# Тест-кейс на получение ошибки некорректного пароля (меньше 6 символов)
    def test_registration_incorrect_password_error(self,driver,generate_random_name, generate_random_email):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        name = generate_random_name
        email = generate_random_email
        short_password = "qwert"

        driver.find_element(By.XPATH, name_input).send_keys(name)
        driver.find_element(By.XPATH, email_input).send_keys(email)
        driver.find_element(By.XPATH, password_input).send_keys(short_password)
        driver.find_element(By.XPATH, register_button).click()

        error_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, error_message))
        )

        error_message_text = error_message_element.text
        # Проверка, что сообщение об ошибке содержит текст "Некорректный пароль"
        assert "Некорректный пароль" in error_message_text, "Сообщение об ошибке отображается"


