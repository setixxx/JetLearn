import flet as ft
from sign_in_view_sources.components.header_text_log_in import HeaderTextLogIn
from sign_in_view_sources.components.support_text_log_in import SupportTextLogIn
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

        self.header_text_log_in = HeaderTextLogIn()
        self.support_text_log_in = SupportTextLogIn()
        self.login_and_pass_text_field = LoginAndPasswordTextField()
        self.button_account_creation_and_log_in = ButtonAccountCreationAndLogIn()

        self.github_link_and_image = GitHubLinkAndImage()

        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            self.header_text_log_in,
                                            self.support_text_log_in,
                                        ],
                                        spacing=0
                                    ),
                                    ft.Column(
                                        [
                                            self.login_and_pass_text_field,
                                            self.button_account_creation_and_log_in
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
                                self.github_link_and_image
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