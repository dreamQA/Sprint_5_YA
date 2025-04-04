# Локаторы для тестов

# Поле для ввода имени на странице регистрации
name_input = "//label[text()='Имя']/ancestor::fieldset//input[@class='text input__textfield text_type_main-default']" # Поле "имя"

# Поле для ввода email на странице регистрации
email_input =  "//label[text()='Email']/following-sibling::input[@class='text input__textfield text_type_main-default']" # Поле "Email"

# Поле для ввода пароля на странице регистрации
password_input = "//label[text()='Пароль']/following-sibling::input[@class='text input__textfield text_type_main-default' and @type='password']" # Поле "пароль"

# Кнопка регистрации на странице "регистрации"
register_button = "//button[text()='Зарегистрироваться' and contains(@class, 'button_button__33qZ0')]"

# Сообщение об ошибке
error_message = "//p[text()='Некорректный пароль']" # Сообщение об ошибке ввода короткого пароля при регистрации

#Тесты входа через кнопки "войти" с разных областей веб-сайта

# Кнопка "войти в аккаунт" на главной странице
# Локатор для кнопки "Войти в аккаунт"
login_button = "//button[text()='Войти в аккаунт']" # Кнопка "войти в аккаунт" на главной

# Поле "Email" на странице авторизации
login_email_input = "//input[@type='text' and @name='name']"

# Поле "Пароль" на странице авторизации
login_password_input = "//input[@type='password' and @name='Пароль']"

# Кнопка "Войти" на странице авторизации
login_button_authorization = "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']"

#Кнопка "Личный кабинет" на главной странице
personal_account_button = "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']"

# Кнопка "Войти" на странице регистрации
login_button_registration = "//a[@href='/login']"

# Кнопка "Войти" на странице восстановления пароля
login_button_form_password_recovery = "//a[@href='/login']"

# Тесты на переходы между разделами

# Тест успешного перехода в "личный кабинет" после успешной авторизации
#Используем personal_account_button = "//*[@id=\"root\"]/div/header/nav/a/p" т.к. путь не меняется

# Кнопка с наименованием "Конструктор" на главной странице
constructor_button = "//p[text()='Конструктор']"

# Кнопка(логотип) Stellar Burger на главной странице
# "//div/header/nav/div/a/svg[@xmlns='http://www.w3.org/2000/svg']" написал,и разные другие атрибуты через высоту и ширину, не определяется элемент, оставляю как есть работающий локатор
logo_button = "#root > div > header > nav > div > a > svg"

# Кнопка "выйти" в личном кабинете
deauthorize_button = "//button[@type='button' and contains(@class, 'Account_button__14Yp3') and text()='Выход']"

# Раздел "Булки" раздела "Контсруктор"
buns_section = "//span[@class='text text_type_main-default' and text()='Булки']"
# Раздел "Соусы" раздела "Контсруктор"
sauces_section = "//span[@class='text text_type_main-default' and text()='Соусы']"
# Раздел "Начинки" раздела "Контсруктор"
fillings_section = "//span[@class='text text_type_main-default' and text()='Начинки']"
#