import pytest
import random
import string
from selenium import webdriver


@pytest.fixture
    # Генерируем случайное "имя"
def generate_random_name():
    name_length = random.randint(5, 10)
    name = ''.join(random.choices(string.ascii_letters, k=name_length)).capitalize()
    return name

@pytest.fixture
    # Генерируем случайный "email"
def generate_random_email():
    username_length = random.randint(6, 16)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits , k=username_length))
    return f"{username}@yandex.ru"

@pytest.fixture
    # Гененрируем случаный пароль
def generate_random_password():
    password_length = 8
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=password_length))
    return password

@pytest.fixture
    # Фикстура для запуска и завершения работы веб-браузера
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
#