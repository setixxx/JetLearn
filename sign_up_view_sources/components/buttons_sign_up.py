import flet as ft
from database import DatabaseManager
import re


# Класс для представления виджета с кнопками "Зарегистрироваться" и "Войти в существующий"
class ButtonsSignUp(ft.Container):
    # Инициализация виджета
    def __init__(self, sign_up_fields, app_state):
        super().__init__()
        # Создание объекта базы данных
        self.database = DatabaseManager("users.sqlite")
        # Сохранение виджета для ввода данных регистрации
        self.sign_up_fields = sign_up_fields
        # Сохранение состояния приложения
        self.app_state = app_state
        # Установка ширины виджета
        self.width = 635
        # Установка высоты виджета
        self.height = 82
        # Установка отступов снизу и справа
        self.padding = ft.padding.only(bottom=32, right=32)
        # Выравнивание по правому нижнему краю
        self.alignment = ft.alignment.bottom_right
        # Создание строки с кнопками
        self.content = ft.Row(
            [
                # Кнопка "Войти в существующий"
                ft.TextButton(
                    # Текст кнопки
                    "Войти в существующий",
                    # Обработчик события клика
                    on_click=lambda e: self.page.go("/sign_in")
                ),
                # Кнопка "Зарегистрироваться"
                ft.FilledButton(
                    # Текст кнопки
                    "Зарегистрироваться",
                    # Обработчик события клика
                    on_click=self.check_user_sign_up
                ),
            ],
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.END,
            # Междуэлементный интервал
            spacing=11
        )

    # Метод проверки данных регистрации
    def check_user_sign_up(self, e):
        # Получение данных из полей ввода
        login = self.sign_up_fields.get_login_sign_up()
        email = self.sign_up_fields.get_email_sign_up()
        password = self.sign_up_fields.get_password_sign_up()
        password_confirm = self.sign_up_fields.get_password_confirm_sign_up()
        # Проверка наличия логина в базе данных
        login_check = self.database.check_user_login(login)
        # Проверка наличия email в базе данных
        email_check = self.database.check_user_email(email)
        # Регулярное выражение для проверки формата email
        pattern_email = (
            re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))
        # Регулярное выражение для проверки формата пароля
        pattern_password = (
            re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%&]).+$'))

        # Проверка логина
        if login == "":
            # Установка ошибки поля ввода логина
            self.sign_up_fields.set_login_error_sign_up("Логин не "
                                                        "может быть "
                                                        "пустым")
        elif login_check:
            # Установка ошибки поля ввода логина
            self.sign_up_fields.set_login_error_sign_up("Логин занят")
        else:
            # Очистка ошибки поля ввода логина
            self.sign_up_fields.set_login_error_sign_up(None)

        # Проверка email
        if email == "":
            # Установка ошибки поля ввода email
            self.sign_up_fields.set_email_error_sign_up("Почта не может "
                                                        "быть пустой")
        elif not pattern_email.match(email):
            # Установка ошибки поля ввода email
            self.sign_up_fields.set_email_error_sign_up("Почта введена "
                                                        "неправильно")
        elif email_check:
            # Установка ошибки поля ввода email
            self.sign_up_fields.set_email_error_sign_up("Почта занята")
        else:
            # Очистка ошибки поля ввода email
            self.sign_up_fields.set_email_error_sign_up(None)

        # Проверка пароля
        if password == "":
            # Установка ошибки поля ввода пароля
            self.sign_up_fields.set_password_error_sign_up("Пароль не может "
                                                           "быть пустым")
        elif len(password) < 4:
            # Установка ошибки поля ввода пароля
            self.sign_up_fields.set_password_error_sign_up("Слишком короткий "
                                                           "пароль")
        elif not pattern_password.match(password):
            # Установка ошибки поля ввода пароля
            self.sign_up_fields.set_password_error_sign_up("Неправильный "
                                                           "формат пароля")
        else:
            # Очистка ошибки поля ввода пароля
            self.sign_up_fields.set_password_error_sign_up(None)

        # Проверка подтверждения пароля
        if password_confirm != password:
            # Установка ошибки поля ввода подтверждения пароля
            self.sign_up_fields.set_password_confirm_error_sign_up("Пароли не "
                                                                   "совпадают")
        else:
            # Очистка ошибки поля ввода подтверждения пароля
            self.sign_up_fields.set_password_confirm_error_sign_up(None)

        # Получение текста ошибок полей ввода
        login_error = self.sign_up_fields.get_login_error_text()
        email_error = self.sign_up_fields.get_email_error_text()
        password_error = self.sign_up_fields.get_password_error_text()
        password_confirm_error = (self.sign_up_fields.
                                  get_password_confirm_error_text())

        # Проверка на отсутствие ошибок
        if (
            (login_error == "" or login_error is None) and
            (email_error == "" or email_error is None) and
            (password_error == "" or password_error is None) and
            (password_confirm_error == "" or password_confirm_error is None)
        ):
            # Создание таблиц в базе данных
            self.create_tables(login)
            # Добавление нового пользователя в базу данных
            self.database.add_user(login, email, password)
            # Установка логина, email и пароля в состоянии приложения
            self.app_state.set_login(login)
            self.app_state.set_email(email)
            self.app_state.set_password(password)
            # Переход на главную страницу
            self.page.go("/main")

    # Метод создания таблиц в базе данных
    def create_tables(self, login):
        # Создание таблицы для хранения данных по теории
        self.database.create_table_theory()
        # Добавление записи о пройденной теории для нового пользователя
        self.database.add_new_theory(login)
        # Получение количества пройденных разделов теории
        completed_theory = self.database.get_completed_theory_count(login)
        # Установка количества пройденных разделов теории в состоянии приложения
        self.app_state.set_completed_theory(completed_theory)
        # Создание таблицы для хранения данных по тестам
        self.database.create_table_test()
        # Добавление записи о пройденных тестах для нового пользователя
        self.database.add_new_tests(login)
        # Получение количества пройденных тестов
        completed_tests = self.database.get_completed_tests_count(login)
        # Установка количества пройденных тестов в состоянии приложения
        self.app_state.set_completed_tests(completed_tests)
        # Создание таблицы для хранения данных по практике
        self.database.create_table_practice()
        # Добавление записи о пройденной практике для нового пользователя
        self.database.add_new_practice(login)
        # Получение статистики по практике
        completed_practice_count, completed_practice_total \
            = self.database.get_practice_stats(login)
        # Установка статистики по практике в состоянии приложения
        self.app_state.set_completed_practice_count(completed_practice_count)
        self.app_state.set_completed_practice_total(completed_practice_total)