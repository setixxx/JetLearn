import flet as ft
from database_sources.database import DatabaseManager


class ButtonsSignIn(ft.Container):
    def __init__(self, sign_in_fields, app_state):
        super().__init__()
        self.app_state = app_state
        self.database = DatabaseManager("users.sqlite")
        self.sign_in_fields = sign_in_fields
        self.width = 423
        self.height = 90
        self.padding = ft.padding.only(bottom=32, right=32)
        self.alignment = ft.alignment.bottom_right
        self.content = ft.Row(
            [
                ft.TextButton(
                    "Создать аккаунт",
                    on_click=lambda e: self.page.go("/sign_up")
                ),
                ft.FilledButton(
                    "Войти",
                    on_click=self.check_user
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=11
        )

    def check_user(self, e):
        login = self.sign_in_fields.get_login_sign_in()
        password = self.sign_in_fields.get_password_sign_in()
        user = self.database.find_user(login)
        check_password = self.database.find_user_password(login, password)

        if user is None:
            self.sign_in_fields.set_login_error_sign_in(
                "Пользователь не найден")
            self.sign_in_fields.set_password_error_sign_in(None)
        elif check_password is None:
            self.sign_in_fields.set_login_error_sign_in(None)
            self.sign_in_fields.set_password_error_sign_in(
                "Неправильный пароль")
        else:
            self.sign_in_fields.set_login_error_sign_in(None)
            self.sign_in_fields.set_password_error_sign_in(None)
            self.app_state.set_login(login)
            self.page.go("/main")
