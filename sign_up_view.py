import flet as ft
from database import DatabaseManager
import re

# Класс для представления виджета с кнопками "Зарегистрироваться" и "Войти в существующий"
class ButtonsSignUp(ft.Container):
    def __init__(self, sign_up_fields, app_state):
        super().__init__()
        # Создаем объект базы данных
        self.database = DatabaseManager("users.sqlite")
        # Сохраняем ссылки на виджеты ввода данных и состояние приложения
        self.sign_up_fields = sign_up_fields
        self.app_state = app_state
        # Устанавливаем стили контейнера
        self.width = 635
        self.height = 82
        self.padding = ft.padding.only(bottom=32, right=32)
        self.alignment = ft.alignment.bottom_right
        # Создаем строку с кнопками
        self.content = ft.Row(
            [
                # Кнопка "Войти в существующий"
                ft.TextButton(
                    "Войти в существующий",
                    on_click=lambda e: self.page.go("/sign_in")
                ),
                # Кнопка "Зарегистрироваться"
                ft.FilledButton(
                    "Зарегистрироваться",
                    on_click=self.check_user_sign_up
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=11
        )

    # Метод проверки данных регистрации
    def check_user_sign_up(self, e):
        # Получаем данные из полей ввода
        login = self.sign_up_fields.get_login_sign_up()
        email = self.sign_up_fields.get_email_sign_up()
        password = self.sign_up_fields.get_password_sign_up()
        password_confirm = self.sign_up_fields.get_password_confirm_sign_up()
        # Проверяем наличие логина и email в базе данных
        login_check = self.database.check_user_login(login)
        email_check = self.database.check_user_email(email)
        # Проверяем формат email и пароля
        pattern_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        pattern_password = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%&]).+$')

        # Проверяем логин
        if login == "":
            self.sign_up_fields.set_login_error_sign_up("Логин не может быть пустым")
        elif login_check:
            self.sign_up_fields.set_login_error_sign_up("Логин занят")
        else:
            self.sign_up_fields.set_login_error_sign_up(None)

        # Проверяем email
        if email == "":
            self.sign_up_fields.set_email_error_sign_up("Почта не может быть пустой")
        elif not pattern_email.match(email):
            self.sign_up_fields.set_email_error_sign_up("Почта введена неправильно")
        elif email_check:
            self.sign_up_fields.set_email_error_sign_up("Почта занята")
        else:
            self.sign_up_fields.set_email_error_sign_up(None)

        # Проверяем пароль
        if password == "":
            self.sign_up_fields.set_password_error_sign_up("Пароль не может быть пустым")
        elif len(password) < 4:
            self.sign_up_fields.set_password_error_sign_up("Слишком короткий пароль")
        elif not pattern_password.match(password):
            self.sign_up_fields.set_password_error_sign_up("Неправильный формат пароля")
        else:
            self.sign_up_fields.set_password_error_sign_up(None)

        # Проверяем подтверждение пароля
        if password_confirm != password:
            self.sign_up_fields.set_password_confirm_error_sign_up("Пароли не совпадают")
        else:
            self.sign_up_fields.set_password_confirm_error_sign_up(None)

        # Получаем текст ошибок полей ввода
        login_error = self.sign_up_fields.get_login_error_text()
        email_error = self.sign_up_fields.get_email_error_text()
        password_error = self.sign_up_fields.get_password_error_text()
        password_confirm_error = self.sign_up_fields.get_password_confirm_error_text()

        # Проверяем на отсутствие ошибок
        if (
            (login_error == "" or login_error is None) and
            (email_error == "" or email_error is None) and
            (password_error == "" or password_error is None) and
            (password_confirm_error == "" or password_confirm_error is None)
        ):
            # Создаем таблицы в базе данных
            self.create_tables(login)
            # Добавляем нового пользователя в базу данных
            self.database.add_user(login, email, password)
            # Устанавливаем логин, email и пароль в состоянии приложения
            self.app_state.set_login(login)
            self.app_state.set_email(email)
            self.app_state.set_password(password)
            # Переходим на главную страницу
            self.page.go("/main")

    # Метод создания таблиц в базе данных
    def create_tables(self, login):
        # Создаем таблицу для хранения данных по теории
        self.database.create_table_theory()
        # Добавляем запись о пройденной теории для нового пользователя
        self.database.add_new_theory(login)
        # Получаем количество пройденных разделов теории
        completed_theory = self.database.get_completed_theory_count(login)
        # Устанавливаем количество пройденных разделов теории в состоянии приложения
        self.app_state.set_completed_theory(completed_theory)

        # Создаем таблицу для хранения данных по тестам
        self.database.create_table_test()
        # Добавляем запись о пройденных тестах для нового пользователя
        self.database.add_new_tests(login)
        # Получаем количество пройденных тестов
        completed_tests = self.database.get_completed_tests_count(login)
        # Устанавливаем количество пройденных тестов в состоянии приложения
        self.app_state.set_completed_tests(completed_tests)

        # Создаем таблицу для хранения данных по практике
        self.database.create_table_practice()
        # Добавляем запись о пройденной практике для нового пользователя
        self.database.add_new_practice(login)
        # Получаем статистику по практике
        completed_practice_count, completed_practice_total = self.database.get_practice_stats(login)
        # Устанавливаем статистику по практике в состоянии приложения
        self.app_state.set_completed_practice_count(completed_practice_count)
        self.app_state.set_completed_practice_total(completed_practice_total)

class HeaderEmail(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 470
        self.height = 259
        self.alignment = ft.alignment.bottom_left
        self.padding = ft.padding.only(left=40)
        self.content = ft.Text(
            "Создать аккаунт\nJetLearn",
            text_align=ft.TextAlign.START,
            size=40,
            weight=ft.FontWeight.W_600,
            style=ft.TextStyle(
                height=1.2
            )
        )

class PasswordCheckBox(ft.Container):
    def __init__(self, show_password):
        super().__init__()
        self.width = 635
        self.height = 64
        self.padding = ft.padding.only(bottom=20, right=160)
        self.alignment = ft.alignment.bottom_right
        self.content = ft.Row(
            [
                ft.Checkbox(
                    label="Показать пароль",
                    value=False,
                    on_change=show_password
                )
            ],
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.END
        )

# Класс для представления виджета с полями ввода для регистрации
class SignUpFields(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.width = 635
        self.height = 354
        self.padding = ft.padding.only(right=32)
        self.alignment = ft.alignment.bottom_right
        # Создаем поля ввода
        self.login_field = ft.TextField(
            label="Логин",
            text_size=16,
            width=271,
            max_length=16,
            error_text=None
        )
        self.email_field = ft.TextField(
            label="Адрес эл. почты",
            text_size=16,
            width=271,
            max_length=36,
            error_text=None
        )
        self.password_field = ft.TextField(
            label="Пароль",
            password=True,
            text_size=16,
            width=271,
            max_length=16,
            error_text=None
        )
        self.password_confirm_field = ft.TextField(
            label="Подтверждение пароля",
            text_size=16,
            width=271,
            max_length=16,
            password=True,
            error_text=None
        )
        # Создаем строку с полями ввода
        self.content = ft.Row(
            [
                # Логин и email
                ft.Column(
                    [
                        self.login_field,
                        self.email_field
                    ],
                    spacing=16,
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                ),
                # Пароль и подтверждение пароля
                ft.Column(
                    [
                        self.password_field,
                        self.password_confirm_field
                    ],
                    spacing=16,
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                )
            ],
            spacing=32,
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.END
        )

    # Методы для получения и установки значений полей ввода
    def get_login_sign_up(self):
        return self.login_field.value

    def get_email_sign_up(self):
        return self.email_field.value

    def get_password_sign_up(self):
        return self.password_field.value

    def get_password_confirm_sign_up(self):
        return self.password_confirm_field.value

    def get_login_error_text(self):
        return self.login_field.error_text

    def get_email_error_text(self):
        return self.email_field.error_text

    def get_password_error_text(self):
        return self.password_field.error_text

    def get_password_confirm_error_text(self):
        return self.password_confirm_field.error_text

    def set_login_error_sign_up(self, error_text):
        self.login_field.error_text = error_text
        self.login_field.update()

    def set_email_error_sign_up(self, error_text):
        self.email_field.error_text = error_text
        self.email_field.update()

    def set_password_error_sign_up(self, error_text):
        self.password_field.error_text = error_text
        self.password_field.update()

    def set_password_confirm_error_sign_up(self, error_text):
        self.password_confirm_field.error_text = error_text
        self.password_confirm_field.update()

class SubheaderEmail(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 470
        self.height = 241
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(left=40, top=15)
        self.content = ft.Text(
            value="Введите свои данные и придумайте надежный\n"
                  "пароль, состоящий из букв, цифр и других \n"
                  "символов",
            weight=ft.FontWeight.W_400,
            size=16,
        )

# Класс представления страницы регистрации
class SignUpView(ft.View):
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохраняем ссылку на страницу и объект состояния приложения
        self.page = page
        self.app_state = app_state
        # Создаем виджеты для ввода данных и чекбокса
        self.sign_up_fields = SignUpFields()
        self.password_check_box = PasswordCheckBox(self.show_password)
        # Устанавливаем маршрут
        self.route = "/sign_up"
        self.padding = 0

        # Создаем элементы представления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Заголовок, подзаголовок и поля ввода
                        ft.Container(
                            ft.Row(
                                [
                                    # Заголовок и подзаголовок
                                    ft.Column(
                                        [
                                            HeaderEmail(),
                                            SubheaderEmail()
                                        ],
                                        spacing=0
                                    ),
                                    # Поля ввода и кнопки
                                    ft.Column(
                                        [
                                            self.sign_up_fields,
                                            self.password_check_box,
                                            ButtonsSignUp(self.sign_up_fields, self.app_state)
                                        ],
                                        spacing=0
                                    )
                                ],
                                spacing=0
                            ),
                            margin=0,
                            padding=0,
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=22,
                        ),
                    ],
                    spacing=0,
                ),
                margin=ft.padding.only(left=198, right=198, top=150, bottom=150),
                width=1105,
                height=500,
            )
        ]

    # Метод отображения/скрытия пароля
    def show_password(self, e):
        # Проверяем состояние чекбокса
        if self.password_check_box.content.controls[0].value:
            # Отображаем пароль
            self.sign_up_fields.content.controls[1].controls[0].password = False
            self.sign_up_fields.content.controls[1].controls[1].password = False
        else:
            # Скрываем пароль
            self.sign_up_fields.content.controls[1].controls[0].password = True
            self.sign_up_fields.content.controls[1].controls[1].password = True
        # Обновляем страницу
        self.page.update()