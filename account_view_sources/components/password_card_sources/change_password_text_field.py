import flet as ft

# Класс контейнера с полями ввода для изменения пароля
class ChangePasswordField(ft.Container):
    # Инициализация контейнера
    def __init__(self):
        super().__init__()
        # Установка ширины и высоты
        self.width = 344
        self.height = 228
        # Выравнивание по левому верхнему краю
        self.alignment = ft.alignment.top_left
        # Установка отступов
        self.padding = ft.padding.only(top=16,
                                       left=32)
        # Создание поля ввода старого пароля
        self.old_password_change_field = ft.TextField(
            # Установка подписи поля
            label="Старый пароль",
            # Установка размера текста
            text_size=16,
            # Установка ширины поля
            width=280,
            # Установка максимальной длины ввода
            max_length=16,
        )
        # Создание поля ввода нового пароля
        self.new_password_change_field = ft.TextField(
            # Установка подписи поля
            label="Новый пароль",
            # Установка размера текста
            text_size=16,
            # Установка ширины поля
            width=280,
            # Установка максимальной длины ввода
            max_length=16,
        )
        # Создание столбца с полями ввода
        self.content = ft.Column(
            [
                # Поле ввода старого пароля
                self.old_password_change_field,
                # Поле ввода нового пароля
                self.new_password_change_field
            ],
        )

    # Метод получения значения поля ввода старого пароля
    def get_old_password_change_field(self):
        return self.old_password_change_field.value

    # Метод получения значения поля ввода нового пароля
    def get_new_password_change_field(self):
        return self.new_password_change_field.value

    # Метод получения текста ошибки поля ввода старого пароля
    def get_old_password_change_error_text(self):
        return self.old_password_change_field.error_text

    # Метод получения текста ошибки поля ввода нового пароля
    def get_new_password_change_error_text(self):
        return self.new_password_change_field.error_text

    # Метод установки текста ошибки поля ввода старого пароля
    def set_old_password_error_change(self, error_text):
        self.old_password_change_field.error_text = error_text
        self.old_password_change_field.update()

    # Метод установки текста ошибки поля ввода нового пароля
    def set_new_password_error_change(self, error_text):
        self.new_password_change_field.error_text = error_text
        self.new_password_change_field.update()