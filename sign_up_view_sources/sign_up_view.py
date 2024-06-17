import flet as ft

from sign_up_view_sources.components.header_email import HeaderEmail
from sign_up_view_sources.components.password_check_box import \
    PasswordCheckBox
from sign_up_view_sources.components.subheader_email import \
    SubheaderEmail
from sign_up_view_sources.components.sign_up_fields import \
    SignUpFields
from sign_up_view_sources.components.buttons_sign_up import \
    ButtonsSignUp

class SignUpView(ft.View):
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        self.app_state = app_state
        self.page = page
        self.sign_up_fields = SignUpFields()
        self.password_check_box = PasswordCheckBox(self.show_password)
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
                                            HeaderEmail(),
                                            SubheaderEmail()
                                        ],
                                        spacing=0
                                    ),
                                    ft.Column(
                                        [
                                            self.sign_up_fields,
                                            self.password_check_box,
                                            ButtonsSignUp(self.sign_up_fields,
                                                          self.app_state)
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
            self.sign_up_fields.content.controls[1].controls[0].password = False
            self.sign_up_fields.content.controls[1].controls[1].password = False
        else:
            self.sign_up_fields.content.controls[1].controls[0].password = True
            self.sign_up_fields.content.controls[1].controls[1].password = True
        self.page.update()