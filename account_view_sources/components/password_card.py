import flet as ft
from database import DatabaseManager
import re


# Класс кнопки "Изменить пароль"
class ButtonChangePassword(ft.Container):
    def __init__(self, change_password_field, app_state):
        super().__init__()
        # Создаем объект базы данных
        self.database = DatabaseManager("users.sqlite")
        # Сохраняем ссылки на поле ввода пароля и состояние приложения
        self.change_password_field = change_password_field
        self.app_state = app_state
        # Устанавливаем стили контейнера
        self.alignment = ft.alignment.bottom_right
        self.padding = ft.padding.only(right=32, bottom=32)
        self.width = 344
        self.height = 72
        # Создаем кнопку "Изменить"
        self.content = ft.FilledButton(
            text="Изменить",
            on_click=self.check_password_change
        )

    # Метод проверки ввода пароля
    def check_password_change(self, e):
        # Получаем введенные пароли
        old_password = self.change_password_field.get_old_password_change_field()
        new_password = self.change_password_field.get_new_password_change_field()
        # Проверяем старый пароль
        old_password_check = self.database.check_user_password(
            self.app_state.get_login(), old_password
        )
        # Проверяем новый пароль
        pattern_password = re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%&]).+$')
        # Проверяем старый пароль
        if old_password_check is None:
            self.change_password_field.set_old_password_error_change(
                "Неправильный старый пароль"
            )
        else:
            self.change_password_field.set_old_password_error_change(None)
        # Проверяем новый пароль
        if new_password == old_password:
            self.change_password_field.set_new_password_error_change(
                "Новый пароль дублирует старый"
            )
        elif new_password == "":
            self.change_password_field.set_new_password_error_change(
                "Пароль не может быть пустым"
            )
        elif len(new_password) < 4:
            self.change_password_field.set_new_password_error_change(
                "Пароль слишком короткий"
            )
        elif not pattern_password.match(new_password):
            self.change_password_field.set_new_password_error_change(
                "Пароль должен содержать цифру,\nбукву и специальный символ"
            )
        else:
            self.change_password_field.set_new_password_error_change(None)

        # Получаем текст ошибок полей ввода
        old_password_error = self.change_password_field.get_old_password_change_error_text()
        new_password_error = self.change_password_field.get_new_password_change_error_text()

        # Проверяем на отсутствие ошибок
        if ((old_password_error == "" or old_password_error is None) and
                (new_password_error == "" or new_password_error is None)):
            # Обновляем пароль в базе данных
            self.database.update_user_password(self.app_state.get_login(), new_password)
            # Обновляем пароль в состоянии приложения
            self.app_state.set_password(new_password)
            # Выводим сообщение об успешном изменении пароля
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Пароль успешно изменен!")
            )
            self.page.snack_bar.open = True
            self.page.update()

# Класс заголовка "Изменение пароля"
class HeaderChangePassword(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(left=21, bottom=3)
        self.width = 344
        self.height = 45
        # Создаем текст заголовка
        self.content = ft.Row(
            [
                ft.Text(
                    "Изменение пароля",
                    size=20,
                    weight=ft.FontWeight.W_500
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.END
        )

class ChangePasswordField(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.width = 344
        self.height = 228
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(top=16, left=32)
        # Создаем поля ввода
        self.old_password_change_field = ft.TextField(
            label="Старый пароль",
            text_size=16,
            width=280,
            max_length=16,
        )
        self.new_password_change_field = ft.TextField(
            label="Новый пароль",
            text_size=16,
            width=280,
            max_length=16,
        )
        # Создаем столбец с полями ввода
        self.content = ft.Column(
            [
                self.old_password_change_field,
                self.new_password_change_field
            ],
        )

    # Методы для получения и установки значений полей ввода
    def get_old_password_change_field(self):
        return self.old_password_change_field.value

    def get_new_password_change_field(self):
        return self.new_password_change_field.value

    def get_old_password_change_error_text(self):
        return self.old_password_change_field.error_text

    def get_new_password_change_error_text(self):
        return self.new_password_change_field.error_text

    def set_old_password_error_change(self, error_text):
        self.old_password_change_field.error_text = error_text
        self.old_password_change_field.update()

    def set_new_password_error_change(self, error_text):
        self.new_password_change_field.error_text = error_text
        self.new_password_change_field.update()

# Класс карточки смены пароля
class PasswordCard(ft.Card):
    def __init__(self, app_state):
        super().__init__()
        # Сохраняем ссылку на объект состояния приложения
        self.app_state = app_state
        # Создаем поле ввода нового пароля
        self.change_password_field = ChangePasswordField()
        # Создаем столбец с элементами карточки
        self.content = ft.Column(
            [
                HeaderChangePassword(),
                self.change_password_field,
                ButtonChangePassword(self.change_password_field, self.app_state)
            ],
            spacing=0,
            width=344,
            height=345,
        )