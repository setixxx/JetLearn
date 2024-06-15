import flet as ft
from theory_screens_sources.first_theory_screen_source.components \
    .arrow_back_and_logo import ArrowBackAndLogo
from account_view_sources.components.account_header import AccountHeader
from settings_view_sources.components.profile_image import ProfileImage
from account_view_sources.components.login_card import LoginCard


class AccountView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.title = "/main/settings/account"
        self.padding = 0
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        ArrowBackAndLogo(
                            lambda e: self.page.go("/main")
                        ),
                        ProfileImage(),
                        AccountHeader(),
                        ft.Row(
                            [
                                LoginCard(),

                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            width=1500,
                            height=346,
                        ),
                    ],
                    spacing=8
                ),
                width=1500,
                height=800
            )
        ]

