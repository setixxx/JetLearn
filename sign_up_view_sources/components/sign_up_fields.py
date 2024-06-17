import flet as ft


class SignUpFields(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 635
        self.height = 354
        self.padding = ft.padding.only(right=32)
        self.alignment = ft.alignment.bottom_right
        self.login_field = ft.TextField(
            label="Логин",
            text_size=16,
            width=271,
            max_length=16,
            error_text=None
        )
        self.email_field = ft.TextField(
            label="Адрес эл. почты",
            text_size=16,
            width=271,
            max_length=36,
            error_text=None
        )
        self.password_field = ft.TextField(
            label="Пароль",
            password=True,
            text_size=16,
            width=271,
            max_length=16,
            error_text=None
        )
        self.password_confirm_field = ft.TextField(
            label="Подтверждение пароля",
            text_size=16,
            width=271,
            max_length=16,
            password=True,
            error_text=None
        )
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        self.login_field,
                        self.email_field
                    ],
                    spacing=16,
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                ),
                ft.Column(
                    [
                        self.password_field,
                        self.password_confirm_field
                    ],
                    spacing=16,
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                )
            ],
            spacing=32,
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.END
        )

    def get_login_sign_up(self):
        return self.login_field.value

    def get_email_sign_up(self):
        return self.email_field.value

    def get_password_sign_up(self):
        return self.password_field.value

    def get_password_confirm_sign_up(self):
        return self.password_confirm_field.value

    def get_login_error_text(self):
        return self.login_field.error_text

    def get_email_error_text(self):
        return self.email_field.error_text

    def get_password_error_text(self):
        return self.password_field.error_text

    def get_password_confirm_error_text(self):
        return self.password_confirm_field.error_text

    def set_login_error_sign_up(self, error_text):
        self.login_field.error_text = error_text
        self.login_field.update()

    def set_email_error_sign_up(self, error_text):
        self.email_field.error_text = error_text
        self.email_field.update()

    def set_password_error_sign_up(self, error_text):
        self.password_field.error_text = error_text
        self.password_field.update()

    def set_password_confirm_error_sign_up(self, error_text):
        self.password_confirm_field.error_text = error_text
        self.password_confirm_field.update()





