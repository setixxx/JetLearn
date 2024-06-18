import flet as ft
from database import DatabaseManager
import re


class ButtonChangePassword(ft.Container):
    def __init__(self, change_password_field, app_state):
        super().__init__()
        self.database = DatabaseManager("users.sqlite")
        self.change_password_field = change_password_field
        self.app_state = app_state
        self.alignment = ft.alignment.bottom_right
        self.padding = ft.padding.only(right=32,
                                       bottom=32)
        self.width = 344
        self.height = 72
        self.content = ft.FilledButton(
            text="Изменить",
            on_click=self.check_password_change
        )

    def check_password_change(self, e):
        old_password = (self.change_password_field.
                        get_old_password_change_field())
        new_password = (self.change_password_field.
                        get_new_password_change_field())
        old_password_check = self.database.check_user_password(
            self.app_state.get_login(), old_password
        )
        pattern_password = (
            re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%&]).+$'))
        if old_password_check is None:
            self.change_password_field.set_old_password_error_change(
                "Неправильный старый пароль"
            )
        else:
            self.change_password_field.set_old_password_error_change(None)
        if new_password == old_password:
            self.change_password_field.set_new_password_error_change(
                "Новый пароль дублирует старый"
            )
        elif new_password == "":
            self.change_password_field.set_new_password_error_change(
                "Пароль не может быть пустой"
            )
        elif len(new_password) < 4:
            self.change_password_field.set_new_password_error_change(
                "Пароль слишком короткий"
            )
        elif not pattern_password.match(new_password):
            self.change_password_field.set_new_password_error_change(
                "Пароль должен содержать цифру,\nбукву и "
                "специальный символ"
            )
        else:
            self.change_password_field.set_new_password_error_change(None)

        old_password_error = (self.change_password_field.
                              get_old_password_change_error_text())
        new_password_error = (self.change_password_field.
                              get_new_password_change_error_text())

        if ((old_password_error == "" or old_password_error is None) and
                (new_password_error == "" or new_password_error is None)):
            self.database.update_user_password(self.app_state.get_login(),
                                               new_password)
            self.app_state.set_password(new_password)
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Пароль успешно изменен!")
            )
            self.page.snack_bar.open = True
            self.page.update()
