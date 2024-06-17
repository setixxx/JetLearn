import flet as ft

class SignInFields(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 423
        self.height = 252
        self.alignment = ft.alignment.top_left
        self.login_field = ft.TextField(
            label="Логин или адрес эл. почты",
            text_size=16,
            text_vertical_align=-0.9,
            width=391,
            height=68,
            max_length=36,
        )
        self.password_field = ft.TextField(
            label="Пароль",
            text_size=16,
            text_vertical_align=-0.9,
            width=391,
            height=68,
            max_length=16,
            password=True,
        )
        self.content = ft.Column(
            [
                self.login_field,
                self.password_field,
            ],
            spacing=16,
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )

    def get_login_sign_in(self):
        return self.login_field.value

    def get_password_sign_in(self):
        return self.password_field.value

    def set_login_error_sign_in(self, error_text):
        self.login_field.error_text = error_text
        self.login_field.update()

    def set_password_error_sign_in(self, error_text):
        self.password_field.error_text = error_text
        self.password_field.update()
