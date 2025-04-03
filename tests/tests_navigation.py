from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators import *

class TestNavigation:
# Тест успешного перехода в "Личный кабинет" авторизованным пользователем
    def test_navigate_to_personal_account_post_login(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.XPATH, login_email_input).send_keys("alexandergajdaj18a111@yandex.ru")
        driver.find_element(By.XPATH, login_password_input).send_keys("708n9gmuA")
        driver.find_element(By.XPATH, login_button_authorization).click()

        driver.find_element(By.XPATH, personal_account_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_changes("https://stellarburgers.nomoreparties.site/login")
        )
        current_url = driver.current_url
        print(f" Текущий URL: {current_url}")
        assert current_url == "https://stellarburgers.nomoreparties.site/account", "Переход в личный кабинет удался"

# Тест успешного перехода на страницу "Конструктор" из личного кабинета по кнопке
    def test_navigate_to_constructor_page(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.XPATH, constructor_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_changes("https://stellarburgers.nomoreparties.site/login")
        )
        current_url = driver.current_url
        print(f" Текущий URL: {current_url}")
        assert current_url == "https://stellarburgers.nomoreparties.site/", "Переход на страницу удался"

# Тест успешного перехода на главную странциу из личного кабинета по логотипу Stellar Burgers
    def test_navigate_to_constructor_page_by_logo_button(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.CSS_SELECTOR, logo_button).click()

        WebDriverWait(driver, 10).until(
            EC.url_changes("https://stellarburgers.nomoreparties.site/login")
        )
        current_url = driver.current_url
        print(f" Текущий URL: {current_url}")
        assert current_url == "https://stellarburgers.nomoreparties.site/", "Переход на главную страницу не удался"

# Тест успешного перехода в раздел "Булки" раздела "Коструктор"
    def test_navigate_to_buns_section(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, fillings_section).click()
        driver.find_element(By.XPATH, buns_section).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, fillings_section))
        )
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, buns_section))
        )

        assert driver.find_element(By.XPATH, buns_section), "Переход в раздел 'Соусы' удался"

# Тест успешного перехода в раздел "Соусы" раздела "Коструктор"
    def test_navigate_to_sauces_section(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, sauces_section))
        )
        time.sleep(1)
        driver.find_element(By.XPATH, sauces_section).click()

        # Проверка, что пользователь попал в раздел "Cоусы"
        assert driver.find_element(By.XPATH, sauces_section), "Переход в раздел 'Соусы' удался"

# Тест успешного перехода в раздел "Начинки" раздела "Коструктор"
    def test_navigate_to_fillings_section(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, fillings_section))
        )

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, fillings_section))
        )

        driver.find_element(By.XPATH, fillings_section).click()

        assert driver.find_element(By.XPATH, fillings_section), "Переход в раздел 'Начинки' удался"
