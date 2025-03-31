# Локаторы для тестов

# Поле для ввода имени на странице регистрации
name_input = "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input" # Поле "имя"

# Поле для ввода email на странице регистрации
email_input = "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input" # Поле "Email"

# Поле для ввода пароля на странице регистрации
password_input = "input[type='password']" # Поле "пароль"

# Кнопка регистрации на странице "регистрации"
register_button = "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa"

# Сообщение об ошибке
error_message = "//*[@id=\"root\"]/div/main/div/form/fieldset[3]/div/p" # Сообщение об ошибке ввода короткого пароля при регистрации

#Тесты входа через кнопки "войти" с разных областей веб-сайта

# Кнопка "войти в аккаунт" на главной странице
login_button_main = "//*[@id=\"root\"]/div/main/section[2]/div/button" # Кнопка "войти в аккаунт" на главной

# Поле "Email" на странице авторизации
login_email_input = "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input"

# Поле "Пароль" на странице авторизации
login_password_input = "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input"

# Кнопка "Войти" на странице авторизации
login_button_authorization = "//*[@id=\"root\"]/div/main/div/form/button"

#Кнопка "Личный кабинет" на главной странице
personal_account_button = "//*[@id=\"root\"]/div/header/nav/a/p"

# Кнопка "Войти" на странице регистрации
login_button_registration = "//*[@id=\"root\"]/div/main/div/div/p/a"

# Кнопка "Войти" на странице восстановления пароля
login_button_form_password_recovery = "//*[@id=\"root\"]/div/main/div/div/p/a"

# Тесты на переходы между разделами

# Тест успешного перехода в "личный кабинет" после успешной авторизации
#Используем personal_account_button = "//*[@id=\"root\"]/div/header/nav/a/p" т.к. путь не меняется

# Кнопка с наименованием "Конструктор" на главной странице
constructor_button = "//*[@id=\"root\"]/div/header/nav/ul/li[1]/a/p"

# Кнопка(логотип) Stellar Burger на главной странице
logo_button = "#root > div > header > nav > div > a > svg"

# Кнопка "выйти" в личном кабинете
deauthorize_button = "//*[@id=\"root\"]/div/main/div/nav/ul/li[3]/button"

# Раздел "Булки" раздела "Контсруктор"
buns_section = "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[1]"
# Раздел "Соусы" раздела "Контсруктор"
sauces_section = "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[2]"
# Раздел "Начинки" раздела "Контсруктор"
fillings_section = "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[3]"
#