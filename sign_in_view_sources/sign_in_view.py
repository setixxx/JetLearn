import flet as ft
from sign_in_view_sources.components.header_log_in import HeaderLogIn
from sign_in_view_sources.components.subheader_log_in import SubheaderLogIn
from sign_in_view_sources.components.sign_in_fields import SignInFields
from sign_in_view_sources.components.buttons_sign_in import ButtonsSignIn
from start_view_sources.components.github_link_and_image import GitHubLinkAndImage

class SignInView(ft.View):
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        self.app_state = app_state
        self.page = page
        self.route = "/sign_in"
        self.padding = 0

        self.sign_in_fields = SignInFields()

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
                                            self.sign_in_fields,
                                            ButtonsSignIn(
                                                self.sign_in_fields,
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
                margin=ft.padding.only(top=203, left=308, right=308, bottom=255),
                width=884,
                height=417,
            )
        ]
