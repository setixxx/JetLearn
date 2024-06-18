import flet as ft
from database import DatabaseManager


class ButtonChangeLogin(ft.Container):
    def __init__(self, change_login_field, app_state):
        super().__init__()
        self.database = DatabaseManager("users.sqlite")
        self.change_login_field = change_login_field
        self.app_state = app_state
        self.alignment = ft.alignment.bottom_right
        self.padding = ft.padding.only(right=32,
                                       bottom=32)
        self.width = 344
        self.height = 72
        self.content = ft.FilledButton(
            text="Изменить",
            on_click=self.check_login_change
        )

    def check_login_change(self, e):
        login = self.change_login_field.get_login_change_field()
        login_check = self.database.check_user_login(login)

        if login == "":
            self.change_login_field.set_login_error_change("Логин не "
                                                           "может быть "
                                                           "пустым")
        elif login_check:
            self.change_login_field.set_login_error_change("Логин занят")
        else:
            self.change_login_field.set_login_error_change(None)

        login_error = self.change_login_field.get_login_change_error_text()

        if login_error == "" or login_error is None:
            self.database.update_user_login(self.app_state.get_login(),
                                            login)
            find_email = self.database.find_email_by_login(login)
            if self.app_state.get_email() == find_email[0]:
                self.app_state.set_login(login)
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Логин успешно изменен!")
                )
                self.page.snack_bar.open = True
                self.page.update()
            else:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Произошла ошибка!")
                )
                self.page.snack_bar.open = True
                self.page.update()
