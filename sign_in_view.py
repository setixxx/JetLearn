import flet as ft
from database import DatabaseManager
from start_view import GitHubLinkAndImage

# Класс для представления виджета с кнопками "Войти" и "Создать аккаунт"
class ButtonsSignIn(ft.Container):
    def __init__(self, sign_in_fields, app_state):
        super().__init__()
        # Сохраняем ссылки на объект состояния приложения, виджеты ввода данных и базу данных
        self.app_state = app_state
        self.database = DatabaseManager("users.sqlite")
        self.sign_in_fields = sign_in_fields
        # Устанавливаем стили контейнера
        self.width = 423
        self.height = 90
        self.padding = ft.padding.only(bottom=32, right=32)
        self.alignment = ft.alignment.bottom_right
        # Создаем строку с кнопками
        self.content = ft.Row(
            [
                # Кнопка "Создать аккаунт"
                ft.TextButton(
                    "Создать аккаунт",
                    on_click=lambda e: self.page.go("/sign_up")
                ),
                # Кнопка "Войти"
                ft.FilledButton(
                    "Войти",
                    on_click=self.check_user
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=11
        )

    # Метод проверки пользователя
    def check_user(self, e):
        # Получаем логин или email и пароль
        login_or_email = self.sign_in_fields.get_login_sign_in()
        password = self.sign_in_fields.get_password_sign_in()

        # Проверяем наличие логина или email в базе данных
        user_login = self.database.check_user_login(login_or_email)
        user_email = self.database.check_user_email(login_or_email)

        # Проверяем логин
        if user_login:
            # Проверяем пароль
            check_password = self.database.check_user_password(login_or_email, password)
            # Если пароль верный
            if check_password:
                # Очищаем ошибки полей ввода
                self.sign_in_fields.set_login_error_sign_in(None)
                self.sign_in_fields.set_password_error_sign_in(None)
                # Устанавливаем логин, email и пароль в состоянии приложения
                self.app_state.set_login(login_or_email)
                find_email = self.database.find_email_by_login(login_or_email)
                self.app_state.set_email(find_email[0])
                self.app_state.set_password(password)
                # Загружаем данные из базы данных
                self.set_tables(login_or_email)
                # Переходим на главную страницу
                self.page.go("/main")
            # Если пароль неверный
            else:
                # Очищаем ошибку поля ввода логина
                self.sign_in_fields.set_login_error_sign_in(None)
                # Устанавливаем ошибку поля ввода пароля
                self.sign_in_fields.set_password_error_sign_in("Неправильный пароль")
        # Проверяем email
        elif user_email:
            # Проверяем пароль
            check_password = self.database.find_user_and_password_by_email(login_or_email, password)
            # Если пароль верный
            if check_password:
                # Очищаем ошибки полей ввода
                self.sign_in_fields.set_login_error_sign_in(None)
                self.sign_in_fields.set_password_error_sign_in(None)
                # Находим логин по email
                find_login = self.database.find_login_by_email(login_or_email)
                # Устанавливаем логин, email и пароль в состоянии приложения
                self.app_state.set_login(find_login[0])
                self.app_state.set_email(login_or_email)
                self.app_state.set_password(password)
                # Загружаем данные из базы данных
                self.set_tables(find_login[0])
                # Переходим на главную страницу
                self.page.go("/main")
            # Если пароль неверный
            else:
                # Очищаем ошибку поля ввода логина
                self.sign_in_fields.set_login_error_sign_in(None)
                # Устанавливаем ошибку поля ввода пароля
                self.sign_in_fields.set_password_error_sign_in("Неправильный пароль")
        # Если пользователь не найден
        else:
            # Устанавливаем ошибку поля ввода логина
            self.sign_in_fields.set_login_error_sign_in("Пользователь не найден")
            # Очищаем ошибку поля ввода пароля
            self.sign_in_fields.set_password_error_sign_in(None)

    # Метод загрузки данных из базы данных
    def set_tables(self, login):
        # Получаем количество пройденных разделов теории
        completed_theory = self.database.get_completed_theory_count(login)
        # Устанавливаем количество пройденных разделов теории в состоянии приложения
        self.app_state.set_completed_theory(completed_theory)

        # Получаем количество пройденных тестов
        completed_tests = self.database.get_completed_tests_count(login)
        # Устанавливаем количество пройденных тестов в состоянии приложения
        self.app_state.set_completed_tests(completed_tests)

        # Получаем статистику по практике
        completed_practice_count, completed_practice_total = self.database.get_practice_stats(login)
        # Устанавливаем статистику по практике в состоянии приложения
        self.app_state.set_completed_practice_count(completed_practice_count)
        self.app_state.set_completed_practice_total(completed_practice_total)

class HeaderLogIn(ft.Container):
    def __init__(self):
        super().__init__()
        self.height = 134
        self.width = 461
        self.alignment = ft.alignment.bottom_left
        self.padding = ft.padding.only(left=24)
        self.content = ft.Text(
            value="Вход",
            weight=ft.FontWeight.W_600,
            size=40,
            style=ft.TextStyle(
                height=1.2
            )
        )


# Класс для представления виджета с полями ввода для входа
class SignInFields(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.width = 423
        self.height = 252
        self.alignment = ft.alignment.top_left
        # Создаем поля ввода
        self.login_field = ft.TextField(
            label="Логин или адрес эл. почты",
            text_size=16,
            text_vertical_align=-0.9,
            width=391,
            max_length=36,
        )
        self.password_field = ft.TextField(
            label="Пароль",
            text_size=16,
            text_vertical_align=-0.9,
            width=391,
            max_length=16,
            password=True,
        )
        # Создаем столбец с полями ввода
        self.content = ft.Column(
            [
                self.login_field,
                self.password_field,
            ],
            spacing=16,
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )

    # Методы для получения и установки значений полей ввода
    def get_login_sign_in(self):
        return self.login_field.value

    def get_password_sign_in(self):
        return self.password_field.value

    def set_login_error_sign_in(self, error_text):
        self.login_field.error_text = error_text
        self.login_field.update()

    def set_password_error_sign_in(self, error_text):
        self.password_field.error_text = error_text
        self.password_field.update()

# Класс для представления виджета подзаголовка "Вход"
class SubheaderLogIn(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.width = 461
        self.height = 208
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(left=28, top=12)
        # Создаем текст подзаголовка
        self.content = ft.Text(
            value="Используйте аккаунт JetBrains",
            weight=ft.FontWeight.W_400,
            size=16,
        )

# Класс представления страницы входа в систему
class SignInView(ft.View):
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохраняем ссылки на страницу и объект состояния приложения
        self.page = page
        self.app_state = app_state
        # Устанавливаем маршрут
        self.route = "/sign_in"
        self.padding = 0

        # Создаем виджет для ввода данных входа
        self.sign_in_fields = SignInFields()

        # Создаем элементы представления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Заголовок и подзаголовок
                        ft.Container(
                            ft.Row(
                                [
                                    # Заголовок и подзаголовок
                                    ft.Column(
                                        [
                                            HeaderLogIn(),
                                            SubheaderLogIn()
                                        ],
                                        spacing=0
                                    ),
                                    # Поля ввода и кнопки
                                    ft.Column(
                                        [
                                            self.sign_in_fields,
                                            ButtonsSignIn(self.sign_in_fields, self.app_state)
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
                        # Строка с ссылкой на GitHub
                        ft.Row(
                            [
                                GitHubLinkAndImage()
                            ],
                            width=884,
                            height=75,
                            alignment=ft.MainAxisAlignment.END,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                    ],
                    spacing=0,
                ),
                margin=ft.padding.only(top=203, left=308, right=308, bottom=255),
                width=884,
                height=417,
            )
        ]