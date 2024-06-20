import flet as ft
from database import DatabaseManager


# Класс для представления виджета с кнопками "Войти" и "Создать аккаунт"
class ButtonsSignIn(ft.Container):
    # Инициализация виджета
    def __init__(self, sign_in_fields, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Создание объекта базы данных
        self.database = DatabaseManager("users.sqlite")
        # Сохранение виджета для ввода данных входа
        self.sign_in_fields = sign_in_fields
        # Установка ширины виджета
        self.width = 423
        # Установка высоты виджета
        self.height = 90
        # Установка отступов снизу и справа
        self.padding = ft.padding.only(bottom=32, right=32)
        # Выравнивание по правому нижнему краю
        self.alignment = ft.alignment.bottom_right
        # Создание строки с кнопками
        self.content = ft.Row(
            [
                # Кнопка "Создать аккаунт"
                ft.TextButton(
                    # Текст кнопки
                    "Создать аккаунт",
                    # Обработчик события клика
                    on_click=lambda e: self.page.go("/sign_up")
                ),
                # Кнопка "Войти"
                ft.FilledButton(
                    # Текст кнопки
                    "Войти",
                    # Обработчик события клика
                    on_click=self.check_user
                ),
            ],
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.END,
            # Междуэлементный интервал
            spacing=11
        )

    # Метод проверки пользователя
    def check_user(self, e):
        # Получение логина или email
        login_or_email = self.sign_in_fields.get_login_sign_in()
        # Получение пароля
        password = self.sign_in_fields.get_password_sign_in()

        # Проверка наличия логина в базе данных
        user_login = self.database.check_user_login(login_or_email)
        # Проверка наличия email в базе данных
        user_email = self.database.check_user_email(login_or_email)

        # Проверка логина
        if user_login:
            # Проверка пароля
            check_password = self.database.check_user_password(login_or_email,
                                                               password)
            # Если пароль верный
            if check_password:
                # Очистка ошибок полей ввода
                self.sign_in_fields.set_login_error_sign_in(None)
                self.sign_in_fields.set_password_error_sign_in(None)
                # Установка логина и email в состоянии приложения
                self.app_state.set_login(login_or_email)
                find_email = self.database.find_email_by_login(login_or_email)
                self.app_state.set_email(find_email[0])
                # Установка пароля в состоянии приложения
                self.app_state.set_password(password)
                # Загрузка данных из базы данных
                self.set_tables(login_or_email)
                # Переход на главную страницу
                self.page.go("/main")
            # Если пароль неверный
            else:
                # Очистка ошибки поля ввода логина
                self.sign_in_fields.set_login_error_sign_in(None)
                # Установка ошибки поля ввода пароля
                self.sign_in_fields.set_password_error_sign_in(
                    "Неправильный пароль")
        # Проверка email
        elif user_email:
            # Проверка пароля
            check_password = self.database.find_user_and_password_by_email(
                login_or_email, password)
            # Если пароль верный
            if check_password:
                # Очистка ошибок полей ввода
                self.sign_in_fields.set_login_error_sign_in(None)
                self.sign_in_fields.set_password_error_sign_in(None)
                # Нахождение логина по email
                find_email = self.database.find_login_by_email(login_or_email)
                # Установка логина и email в состоянии приложения
                self.app_state.set_login(find_email[0])
                self.app_state.set_email(login_or_email)
                # Установка пароля в состоянии приложения
                self.app_state.set_password(password)
                # Загрузка данных из базы данных
                self.set_tables(find_email[0])
                # Переход на главную страницу
                self.page.go("/main")
            # Если пароль неверный
            else:
                # Очистка ошибки поля ввода логина
                self.sign_in_fields.set_login_error_sign_in(None)
                # Установка ошибки поля ввода пароля
                self.sign_in_fields.set_password_error_sign_in(
                    "Неправильный пароль")
        # Если пользователь не найден
        else:
            # Установка ошибки поля ввода логина
            self.sign_in_fields.set_login_error_sign_in(
                "Пользователь не найден")
            # Очистка ошибки поля ввода пароля
            self.sign_in_fields.set_password_error_sign_in(None)

    # Метод загрузки данных из базы данных
    def set_tables(self, login):
        # Получение количества пройденных разделов теории
        completed_theory = self.database.get_completed_theory_count(login)
        # Установка количества пройденных разделов теории в состоянии приложения
        self.app_state.set_completed_theory(completed_theory)
        # Получение количества пройденных тестов
        completed_tests = self.database.get_completed_tests_count(login)
        # Установка количества пройденных тестов в состоянии приложения
        self.app_state.set_completed_tests(completed_tests)
        # Получение статистики по практике
        completed_practice_count, completed_practice_total \
            = self.database.get_practice_stats(login)
        # Установка статистики по практике в состоянии приложения
        self.app_state.set_completed_practice_count(completed_practice_count)
        self.app_state.set_completed_practice_total(completed_practice_total)