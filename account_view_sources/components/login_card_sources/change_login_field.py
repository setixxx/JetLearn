import flet as ft


# Класс контейнера с полем ввода для изменения логина
class ChangeLoginField(ft.Container):
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
        # Создание поля ввода нового логина
        self.login_change_field = ft.TextField(
            # Установка подписи поля
            label="Новый логин",
            # Установка размера текста
            text_size=16,
            # Установка ширины поля
            width=280,
            # Установка максимальной длины ввода
            max_length=16,
        )
        # Установка поля ввода в качестве контента контейнера
        self.content = self.login_change_field

    # Метод получения значения поля ввода нового логина
    def get_login_change_field(self):
        return self.login_change_field.value

    # Метод получения текста ошибки поля ввода нового логина
    def get_login_change_error_text(self):
        return self.login_change_field.error_text

    # Метод установки текста ошибки поля ввода нового логина
    def set_login_error_change(self, error_text):
        self.login_change_field.error_text = error_text
        self.login_change_field.update()