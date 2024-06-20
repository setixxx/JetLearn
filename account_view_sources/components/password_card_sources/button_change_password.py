import flet as ft
from database import DatabaseManager
import re


# Класс кнопки "Изменить пароль"
class ButtonChangePassword(ft.Container):
    # Инициализация кнопки
    def __init__(self, change_password_field, app_state):
        super().__init__()
        # Создание объекта базы данных
        self.database = DatabaseManager("users.sqlite")
        # Сохранение поля ввода пароля и состояния приложения
        self.change_password_field = change_password_field
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
            on_click=self.check_password_change
        )

    # Метод проверки ввода пароля
    def check_password_change(self, e):
        # Получение введенных паролей
        old_password = (self.change_password_field.
                        get_old_password_change_field())
        new_password = (self.change_password_field.
                        get_new_password_change_field())
        # Проверка старого пароля
        old_password_check = self.database.check_user_password(
            self.app_state.get_login(), old_password
        )
        # Регулярное выражение для проверки нового пароля
        pattern_password = (
            re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%&]).+$'))
        # Проверка старого пароля
        if old_password_check is None:
            # Вывод ошибки в поле ввода старого пароля
            self.change_password_field.set_old_password_error_change(
                "Неправильный старый пароль"
            )
        else:
            # Очистка ошибки поля ввода старого пароля
            self.change_password_field.set_old_password_error_change(None)
        # Проверка нового пароля
        if new_password == old_password:
            # Вывод ошибки в поле ввода нового пароля
            self.change_password_field.set_new_password_error_change(
                "Новый пароль дублирует старый"
            )
        elif new_password == "":
            # Вывод ошибки в поле ввода нового пароля
            self.change_password_field.set_new_password_error_change(
                "Пароль не может быть пустой"
            )
        elif len(new_password) < 4:
            # Вывод ошибки в поле ввода нового пароля
            self.change_password_field.set_new_password_error_change(
                "Пароль слишком короткий"
            )
        elif not pattern_password.match(new_password):
            # Вывод ошибки в поле ввода нового пароля
            self.change_password_field.set_new_password_error_change(
                "Пароль должен содержать цифру,\nбукву и "
                "специальный символ"
            )
        else:
            # Очистка ошибки поля ввода нового пароля
            self.change_password_field.set_new_password_error_change(None)

        # Получение текста ошибок полей ввода
        old_password_error = (self.change_password_field.
                              get_old_password_change_error_text())
        new_password_error = (self.change_password_field.
                              get_new_password_change_error_text())

        # Проверка на отсутствие ошибок
        if ((old_password_error == "" or old_password_error is None) and
                (new_password_error == "" or new_password_error is None)):
            # Обновление пароля в базе данных
            self.database.update_user_password(self.app_state.get_login(),
                                               new_password)
            # Обновление пароля в состоянии приложения
            self.app_state.set_password(new_password)
            # Вывод сообщения об успешном изменении пароля
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Пароль успешно изменен!")
            )
            self.page.snack_bar.open = True
            self.page.update()