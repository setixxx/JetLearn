import flet as ft

# Класс для представления виджета с полями ввода для входа
class SignInFields(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка ширины виджета
        self.width = 423
        # Установка высоты виджета
        self.height = 252
        # Выравнивание по левому верхнему краю
        self.alignment = ft.alignment.top_left
        # Создание поля ввода логина или email
        self.login_field = ft.TextField(
            # Подпись поля
            label="Логин или адрес эл. почты",
            # Размер текста
            text_size=16,
            # Вертикальное выравнивание текста
            text_vertical_align=-0.9,
            # Ширина поля
            width=391,
            # Максимальная длина ввода
            max_length=36,
        )
        # Создание поля ввода пароля
        self.password_field = ft.TextField(
            # Подпись поля
            label="Пароль",
            # Размер текста
            text_size=16,
            # Вертикальное выравнивание текста
            text_vertical_align=-0.9,
            # Ширина поля
            width=391,
            # Максимальная длина ввода
            max_length=16,
            # Установка режима скрытия пароля
            password=True,
        )
        # Создание столбца с полями ввода
        self.content = ft.Column(
            [
                # Поле ввода логина или email
                self.login_field,
                # Поле ввода пароля
                self.password_field,
            ],
            # Междурядный интервал
            spacing=16,
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.END,
            # Выравнивание по вертикали
            horizontal_alignment=ft.CrossAxisAlignment.START
        )

    # Метод получения значения поля ввода логина
    def get_login_sign_in(self):
        return self.login_field.value

    # Метод получения значения поля ввода пароля
    def get_password_sign_in(self):
        return self.password_field.value

    # Метод установки текста ошибки поля ввода логина
    def set_login_error_sign_in(self, error_text):
        self.login_field.error_text = error_text
        self.login_field.update()

    # Метод установки текста ошибки поля ввода пароля
    def set_password_error_sign_in(self, error_text):
        self.password_field.error_text = error_text
        self.password_field.update()