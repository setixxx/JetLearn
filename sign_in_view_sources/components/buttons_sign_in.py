import flet as ft
from database import DatabaseManager


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
        login_or_email = self.sign_in_fields.get_login_sign_in()
        password = self.sign_in_fields.get_password_sign_in()

        user_login = self.database.check_user_login(login_or_email)
        user_email = self.database.check_user_email(login_or_email)

        if user_login:
            check_password = self.database.check_user_password(login_or_email,
                                                               password)
            if check_password:
                self.sign_in_fields.set_login_error_sign_in(None)
                self.sign_in_fields.set_password_error_sign_in(None)
                self.app_state.set_login(login_or_email)
                find_email = self.database.find_email_by_login(login_or_email)
                self.app_state.set_email(find_email[0])
                self.app_state.set_password(password)
                self.set_tables(login_or_email)
                self.page.go("/main")
            else:
                self.sign_in_fields.set_login_error_sign_in(None)
                self.sign_in_fields.set_password_error_sign_in(
                    "Неправильный пароль")
        elif user_email:
            check_password = self.database.find_user_and_password_by_email(
                login_or_email, password)
            if check_password:
                self.sign_in_fields.set_login_error_sign_in(None)
                self.sign_in_fields.set_password_error_sign_in(None)
                find_email = self.database.find_login_by_email(login_or_email)
                self.app_state.set_login(find_email[0])
                self.app_state.set_email(login_or_email)
                self.app_state.set_password(password)
                self.set_tables(find_email[0])
                self.page.go("/main")
            else:
                self.sign_in_fields.set_login_error_sign_in(None)
                self.sign_in_fields.set_password_error_sign_in(
                    "Неправильный пароль")
        else:
            self.sign_in_fields.set_login_error_sign_in(
                "Пользователь не найден")
            self.sign_in_fields.set_password_error_sign_in(None)

    def set_tables(self, login):
        completed_theory = self.database.get_completed_theory_count(login)
        self.app_state.set_completed_theory(completed_theory)
        completed_tests = self.database.get_completed_tests_count(login)
        self.app_state.set_completed_tests(completed_tests)
        completed_practice_count, completed_practice_total \
            = self.database.get_completed_practice_count(login)
        self.app_state.set_completed_practice_count(completed_practice_count)
        self.app_state.set_completed_practice_total(completed_practice_total)
