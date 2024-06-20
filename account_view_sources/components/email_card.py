# Импорт библиотеки flet
import flet as ft
from database import DatabaseManager
import re


# Класс заголовка "Изменение адреса эл. почты"
class HeaderChangeEmail(ft.Container):
    # Инициализация заголовка
    def __init__(self):
        super().__init__()
        # Установка отступов
        self.padding = ft.padding.only(left=21, bottom=3)
        # Установка ширины и высоты
        self.width = 344
        self.height = 45
        # Создание строки с текстом заголовка
        self.content = ft.Row(
            [
                ft.Text(
                    "Изменение адреса эл. почты",
                    # Установка размера и веса шрифта
                    size=20,
                    weight=ft.FontWeight.W_500
                )
            ],
            # Выравнивание по левому краю
            alignment=ft.MainAxisAlignment.START,
            # Выравнивание по нижнему краю
            vertical_alignment=ft.CrossAxisAlignment.END
        )


# Класс контейнера с полем ввода для изменения email
class ChangeEmailField(ft.Container):
    # Инициализация контейнера
    def __init__(self):
        super().__init__()
        # Установка ширины и высоты
        self.width = 344
        self.height = 114
        # Выравнивание по левому верхнему краю
        self.alignment = ft.alignment.top_left
        # Установка отступов
        self.padding = ft.padding.only(top=16,
                                       left=32)
        # Создание поля ввода нового email
        self.email_change_field = ft.TextField(
            # Установка подписи поля
            label="Новый адрес эл. почты",
            # Установка размера текста
            text_size=16,
            # Установка ширины поля
            width=280,
            # Установка максимальной длины ввода
            max_length=36,
        )
        # Установка поля ввода в качестве контента контейнера
        self.content = self.email_change_field

    # Метод получения значения поля ввода нового email
    def get_email_change_field(self):
        return self.email_change_field.value

    # Метод получения текста ошибки поля ввода нового email
    def get_email_change_error_text(self):
        return self.email_change_field.error_text

    # Метод установки текста ошибки поля ввода нового email
    def set_email_error_change(self, error_text):
        self.email_change_field.error_text = error_text
        self.email_change_field.update()


# Класс кнопки "Изменить email"
class ButtonChangeEmail(ft.Container):
    # Инициализация кнопки
    def __init__(self, change_email_field, app_state):
        super().__init__()
        # Создание объекта базы данных
        self.database = DatabaseManager("users.sqlite")
        # Сохранение поля ввода email и состояния приложения
        self.change_email_field = change_email_field
        self.app_state = app_state
        # Выравнивание по правому нижнему краю
        self.alignment = ft.alignment.bottom_right
        # Установка отступов
        self.padding = ft.padding.only(right=32,
                                       bottom=32)
        # Установка ширины и высоты
        self.width = 344
        self.height = 72
        # Создание кнопки "Изменить"
        self.content = ft.FilledButton(
            # Установка текста кнопки
            text="Изменить",
            # Установка обработчика клика
            on_click=self.check_email_change
        )

    # Метод проверки ввода нового email
    def check_email_change(self, e):
        # Получение нового email
        email = self.change_email_field.get_email_change_field()
        # Проверка наличия нового email в базе данных
        email_check = self.database.check_user_email(email)
        # Регулярное выражение для проверки формата email
        pattern_email = (
            re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

        # Проверка ввода email
        if email == "":
            # Вывод ошибки в поле ввода email
            self.change_email_field.set_email_error_change("Почта не может "
                                                           "быть пустой")
        elif not pattern_email.match(email):
            # Вывод ошибки в поле ввода email
            self.change_email_field.set_email_error_change("Почта введена "
                                                           "неправильно")
        elif email_check:
            # Вывод ошибки в поле ввода email
            self.change_email_field.set_email_error_change("Почта занята")
        else:
            # Очистка ошибки поля ввода email
            self.change_email_field.set_email_error_change(None)

        # Получение текста ошибки поля ввода
        email_error = self.change_email_field.get_email_change_error_text()

        # Проверка на отсутствие ошибок
        if email_error == "" or email_error is None:
            # Обновление email в базе данных
            self.database.update_user_email(self.app_state.get_login(), email)
            # Поиск логина по новому email
            find_login = self.database.find_login_by_email(email)
            # Проверка, совпадает ли логин в состоянии приложения с найденным
            if self.app_state.get_login() == find_login[0]:
                # Обновление email в состоянии приложения
                self.app_state.set_email(email)
                # Вывод сообщения об успешном изменении email
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Почта успешно изменена!")
                )
                self.page.snack_bar.open = True
                self.page.update()
            else:
                # Вывод сообщения об ошибке
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Произошла ошибка!")
                )
                self.page.snack_bar.open = True
                self.page.update()


# Класс карточки смены email
class EmailCard(ft.Card):
    # Инициализация карточки
    def __init__(self, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Создание поля ввода нового email
        self.change_email_field = ChangeEmailField()
        # Создание столбца с элементами карточки
        self.content = ft.Column(
            [
                # Заголовок "Изменить email"
                HeaderChangeEmail(),
                # Поле ввода нового email
                self.change_email_field,
                # Кнопка "Изменить email"
                ButtonChangeEmail(self.change_email_field,
                                  self.app_state)
            ],
            spacing=0,
            width=344,
            height=231,
        )
