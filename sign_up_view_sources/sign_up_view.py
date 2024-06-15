import flet as ft

from sign_up_view_sources.components.header_email import HeaderEmail
from sign_up_view_sources.components.password_check_box import \
    PasswordCheckBox
from sign_up_view_sources.components.subheader_email import \
    SubheaderEmail
from sign_up_view_sources.components.nickname_and_email_text_field import \
    NicknameAndEmailTextField
from sign_up_view_sources.components.button_next_and_log_in import \
    ButtonNextAndLogIn

class SignUpView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.header_email = HeaderEmail()
        self.subheader_email = SubheaderEmail()
        self.nickname_and_email_text_field = NicknameAndEmailTextField()
        self.password_check_box = PasswordCheckBox(self.show_password)
        self.button_next_and_log_in = ButtonNextAndLogIn()
        self.route = "/sign_up"
        self.padding = 0
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            self.header_email,
                                            self.subheader_email,
                                        ],
                                        spacing=0
                                    ),
                                    ft.Column(
                                        [
                                            self.nickname_and_email_text_field,
                                            self.password_check_box,
                                            self.button_next_and_log_in,
                                        ],
                                        spacing=0
                                    )
                                ],
                                spacing=0
                            ),
                            margin=0,
                            padding=0,
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=22,
                        ),
                    ],
                    spacing=0,
                ),
                margin=ft.padding.only(left=198,
                                       right=198,
                                       top=150,
                                       bottom=150),
                width=1105,
                height=500,
            )
        ]

    def show_password(self, e):
        if self.password_check_box.content.controls[0].value:
            self.nickname_and_email_text_field.content.controls[1].controls[0].password = False
            self.nickname_and_email_text_field.content.controls[1].controls[1].password = False
        else:
            self.nickname_and_email_text_field.content.controls[1].controls[0].password = True
            self.nickname_and_email_text_field.content.controls[1].controls[1].password = True
        self.page.update()