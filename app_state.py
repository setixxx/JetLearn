class AppState:
    # Инициализация состояния приложения
    def __init__(self):
        # Инициализация атрибутов состояния
        self.user_login = None  # Логин пользователя
        self.user_email = None  # Электронная почта пользователя
        self.password = None  # Пароль пользователя
        self.completed_theory = None  # Количество пройденных теорий
        self.completed_practice_count = None  # Количество пройденных практик
        self.completed_practice_total = None  # Общее количество практик
        self.completed_tests = None  # Количество пройденных тестов

    # Установка логина пользователя
    def set_login(self, login):
        self.user_login = login

    # Получение логина пользователя
    def get_login(self):
        return self.user_login

    # Установка электронной почты пользователя
    def set_email(self, email):
        self.user_email = email

    # Получение электронной почты пользователя
    def get_email(self):
        return self.user_email

    # Установка пароля пользователя
    def set_password(self, password):
        self.password = password

    # Получение пароля пользователя
    def get_password(self):
        return self.password

    # Установка количества пройденных теорий
    def set_completed_theory(self, completed_theory):
        self.completed_theory = completed_theory

    # Получение количества пройденных теорий (в процентах)
    def get_completed_theory(self):
        return self.completed_theory / 8

    # Получение отформатированного количества пройденных теорий
    def get_formatted_theory(self):
        return f"{self.completed_theory} из 8"

    # Получение отформатированного количества пройденных теорий с разделителем "/"
    def get_formatted_theory_backslash(self):
        return f"{self.completed_theory} / 8"

    # Установка количества пройденных тестов
    def set_completed_tests(self, completed_tests):
        self.completed_tests = completed_tests

    # Получение количества пройденных тестов (в процентах)
    def get_completed_tests(self):
        return self.completed_tests / 8

    # Получение отформатированного количества пройденных тестов
    def get_formatted_tests(self):
        return f"{self.completed_tests} из 8"

    # Установка количества пройденных практик
    def set_completed_practice_count(self, completed_practice):
        self.completed_practice_count = completed_practice

    # Установка общего количества практик
    def set_completed_practice_total(self, completed_practice):
        self.completed_practice_total = completed_practice

    # Получение отформатированного количества пройденных практик
    def get_formatted_practice(self):
        return (f"{self.completed_practice_count} / "
                f"{self.completed_practice_total}")