import flet as ft


# Класс для представления виджета с полями ввода для регистрации
class SignUpFields(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка ширины виджета
        self.width = 635
        # Установка высоты виджета
        self.height = 354
        # Установка отступов справа
        self.padding = ft.padding.only(right=32)
        # Выравнивание по правому нижнему краю
        self.alignment = ft.alignment.bottom_right
        # Создание поля ввода логина
        self.login_field = ft.TextField(
            # Подпись поля
            label="Логин",
            # Размер текста
            text_size=16,
            # Ширина поля
            width=271,
            # Максимальная длина ввода
            max_length=16,
            # Очистка текста ошибки
            error_text=None
        )
        # Создание поля ввода email
        self.email_field = ft.TextField(
            # Подпись поля
            label="Адрес эл. почты",
            # Размер текста
            text_size=16,
            # Ширина поля
            width=271,
            # Максимальная длина ввода
            max_length=36,
            # Очистка текста ошибки
            error_text=None
        )
        # Создание поля ввода пароля
        self.password_field = ft.TextField(
            # Подпись поля
            label="Пароль",
            # Скрытие пароля
            password=True,
            # Размер текста
            text_size=16,
            # Ширина поля
            width=271,
            # Максимальная длина ввода
            max_length=16,
            # Очистка текста ошибки
            error_text=None
        )
        # Создание поля ввода подтверждения пароля
        self.password_confirm_field = ft.TextField(
            # Подпись поля
            label="Подтверждение пароля",
            # Размер текста
            text_size=16,
            # Ширина поля
            width=271,
            # Максимальная длина ввода
            max_length=16,
            # Скрытие пароля
            password=True,
            # Очистка текста ошибки
            error_text=None
        )
        # Создание строки с полями ввода
        self.content = ft.Row(
            [
                # Столбец для логина и email
                ft.Column(
                    [
                        # Поле ввода логина
                        self.login_field,
                        # Поле ввода email
                        self.email_field
                    ],
                    # Междурядный интервал
                    spacing=16,
                    # Выравнивание по горизонтали
                    alignment=ft.MainAxisAlignment.END,
                    # Выравнивание по вертикали
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                ),
                # Столбец для пароля и подтверждения пароля
                ft.Column(
                    [
                        # Поле ввода пароля
                        self.password_field,
                        # Поле ввода подтверждения пароля
                        self.password_confirm_field
                    ],
                    # Междурядный интервал
                    spacing=16,
                    # Выравнивание по горизонтали
                    alignment=ft.MainAxisAlignment.END,
                    # Выравнивание по вертикали
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                )
            ],
            # Междуэлементный интервал
            spacing=32,
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.END,
            # Выравнивание по вертикали
            vertical_alignment=ft.CrossAxisAlignment.END
        )

    # Метод получения значения поля ввода логина
    def get_login_sign_up(self):
        return self.login_field.value

    # Метод получения значения поля ввода email
    def get_email_sign_up(self):
        return self.email_field.value

    # Метод получения значения поля ввода пароля
    def get_password_sign_up(self):
        return self.password_field.value

    # Метод получения значения поля ввода подтверждения пароля
    def get_password_confirm_sign_up(self):
        return self.password_confirm_field.value

    # Метод получения текста ошибки поля ввода логина
    def get_login_error_text(self):
        return self.login_field.error_text

    # Метод получения текста ошибки поля ввода email
    def get_email_error_text(self):
        return self.email_field.error_text

    # Метод получения текста ошибки поля ввода пароля
    def get_password_error_text(self):
        return self.password_field.error_text

    # Метод получения текста ошибки поля ввода подтверждения пароля
    def get_password_confirm_error_text(self):
        return self.password_confirm_field.error_text

    # Метод установки текста ошибки поля ввода логина
    def set_login_error_sign_up(self, error_text):
        self.login_field.error_text = error_text
        self.login_field.update()

    # Метод установки текста ошибки поля ввода email
    def set_email_error_sign_up(self, error_text):
        self.email_field.error_text = error_text
        self.email_field.update()

    # Метод установки текста ошибки поля ввода пароля
    def set_password_error_sign_up(self, error_text):
        self.password_field.error_text = error_text
        self.password_field.update()

    # Метод установки текста ошибки поля ввода подтверждения пароля
    def set_password_confirm_error_sign_up(self, error_text):
        self.password_confirm_field.error_text = error_text
        self.password_confirm_field.update()