import flet as ft
from database import DatabaseManager
import re

class ButtonChangeEmail(ft.Container):
    def __init__(self, change_email_field, app_state):
        super().__init__()
        self.database = DatabaseManager("users.sqlite")
        self.change_email_field = change_email_field
        self.app_state = app_state
        self.alignment = ft.alignment.bottom_right
        self.padding = ft.padding.only(right=32,
                                       bottom=32)
        self.width = 344
        self.height = 72
        self.content = ft.FilledButton(
            text="Изменить",
            on_click=self.check_email_change
        )

    def check_email_change(self, e):
        email = self.change_email_field.get_email_change_field()
        email_check = self.database.check_user_email(email)
        pattern_email = (
            re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))

        if email == "":
            self.change_email_field.set_email_error_change("Почта не может "
                                                        "быть пустой")
        elif not pattern_email.match(email):
            self.change_email_field.set_email_error_change("Почта введена "
                                                        "неправильно")
        elif email_check:
            self.change_email_field.set_email_error_change("Почта занята")
        else:
            self.change_email_field.set_email_error_change(None)

        email_error = self.change_email_field.get_email_change_error_text()

        if email_error == "" or email_error is None:
            self.database.update_user_email(self.app_state.get_login(), email)
            find_login = self.database.find_login_by_email(email)
            if self.app_state.get_login() == find_login[0]:
                self.app_state.set_email(email)
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Почта успешно изменена!")
                )
                self.page.snack_bar.open = True
                self.page.update()
            else:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Произошла ошибка!")
                )
                self.page.snack_bar.open = True
                self.page.update()
