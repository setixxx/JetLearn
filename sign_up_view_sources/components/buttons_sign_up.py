import flet as ft
from database import DatabaseManager
import re


class ButtonsSignUp(ft.Container):
    def __init__(self, sign_up_fields, app_state):
        super().__init__()
        self.database = DatabaseManager("users.sqlite")
        self.sign_up_fields = sign_up_fields
        self.app_state = app_state
        self.width = 635
        self.height = 82
        self.padding = ft.padding.only(bottom=32, right=32)
        self.alignment = ft.alignment.bottom_right
        self.content = ft.Row(
            [
                ft.TextButton(
                    "Войти в существующий",
                    on_click=lambda e: self.page.go("/sign_in")
                ),
                ft.FilledButton(
                    "Зарегистрироваться",
                    on_click=self.check_user_sign_up
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=11
        )

    def check_user_sign_up(self, e):
        login = self.sign_up_fields.get_login_sign_up()
        email = self.sign_up_fields.get_email_sign_up()
        password = self.sign_up_fields.get_password_sign_up()
        password_confirm = self.sign_up_fields.get_password_confirm_sign_up()
        login_check = self.database.check_user_login(login)
        email_check = self.database.check_user_email(email)
        pattern_email = (
            re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'))
        pattern_password = (
            re.compile(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%&]).+$'))

        if login == "":
            self.sign_up_fields.set_login_error_sign_up("Логин не "
                                                        "может быть "
                                                        "пустым")
        elif login_check:
            self.sign_up_fields.set_login_error_sign_up("Логин занят")
        else:
            self.sign_up_fields.set_login_error_sign_up(None)

        if email == "":
            self.sign_up_fields.set_email_error_sign_up("Почта не может "
                                                        "быть пустой")
        elif not pattern_email.match(email):
            self.sign_up_fields.set_email_error_sign_up("Почта введена "
                                                        "неправильно")
        elif email_check:
            self.sign_up_fields.set_email_error_sign_up("Почта занята")
        else:
            self.sign_up_fields.set_email_error_sign_up(None)

        if password == "":
            self.sign_up_fields.set_password_error_sign_up("Пароль не может "
                                                           "быть пустым")
        elif len(password) < 4:
            self.sign_up_fields.set_password_error_sign_up("Слишком короткий "
                                                           "пароль")
        elif not pattern_password.match(password):
            self.sign_up_fields.set_password_error_sign_up("Неправильный "
                                                           "формат пароля")
        else:
            self.sign_up_fields.set_password_error_sign_up(None)

        if password_confirm != password:
            self.sign_up_fields.set_password_confirm_error_sign_up("Пароли не "
                                                                   "совпадают")
        else:
            self.sign_up_fields.set_password_confirm_error_sign_up(None)

        login_error = self.sign_up_fields.get_login_error_text()
        email_error = self.sign_up_fields.get_email_error_text()
        password_error = self.sign_up_fields.get_password_error_text()
        password_confirm_error = (self.sign_up_fields.
                                  get_password_confirm_error_text())

        if (
            (login_error == "" or login_error is None) and
            (email_error == "" or email_error is None) and
            (password_error == "" or password_error is None) and
            (password_confirm_error == "" or password_confirm_error is None)
        ):
            self.create_tables(login)
            self.database.add_user(login, email, password)
            self.app_state.set_login(login)
            self.app_state.set_email(email)
            self.app_state.set_password(password)
            self.page.go("/main")

    def create_tables(self, login):
        self.database.create_table_theory()
        self.database.add_new_theory(login)
        completed_theory = self.database.get_completed_theory_count(login)
        self.app_state.set_completed_theory(completed_theory)
        self.database.create_table_test()
        self.database.add_new_tests(login)
        completed_tests = self.database.get_completed_tests_count(login)
        self.app_state.set_completed_tests(completed_tests)
        self.database.create_table_practice()
        self.database.add_new_practice(login)
        completed_practice_count, completed_practice_total \
            = self.database.get_completed_practice_count(login)
        self.app_state.set_completed_practice_count(completed_practice_count)
        self.app_state.set_completed_practice_total(completed_practice_total)


