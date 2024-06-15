import flet as ft
from sign_in_view_sources.components.header_log_in import HeaderLogIn
from sign_in_view_sources.components.subheader_log_in import SubheaderLogIn
from sign_in_view_sources.components.login_and_password_text_field import \
    LoginAndPasswordTextField
from sign_in_view_sources.components.button_account_creation_and_log_in import \
    ButtonAccountCreationAndLogIn
from start_view_sources.components.github_link_and_image import \
    GitHubLinkAndImage


class SignInView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = "/sign_in"
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
                                            HeaderLogIn(),
                                            SubheaderLogIn()
                                        ],
                                        spacing=0
                                    ),
                                    ft.Column(
                                        [
                                            LoginAndPasswordTextField(),
                                            ButtonAccountCreationAndLogIn()
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
                        ft.Row(
                            [
                                GitHubLinkAndImage()
                            ],
                            width=884,
                            height=75,
                            alignment=ft.MainAxisAlignment.END,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                    ],
                    spacing=0,
                ),
                margin=ft.padding.only(top=203,
                                       left=308,
                                       right=308,
                                       bottom=255),
                width=884,
                height=417,
            )
        ]