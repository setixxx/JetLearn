import flet as ft
from theory_screens_sources.first_theory_screen_source.components.arrow_back_and_logo import ArrowBackAndLogo
from settings_view_sources.components.profile_image import ProfileImage
from settings_view_sources.components.settings_header import SettingsHeader
from settings_view_sources.components.settings_subheader import SettingsSubheader
from settings_view_sources.components.button_log_out import ButtonLogOut
from settings_view_sources.components.statistics_card import StatisticsCard
from settings_view_sources.components.account_card import AccountCard


class SettingsView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.title = "/main/settings"
        self.padding = 0
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        ArrowBackAndLogo(
                            lambda e: self.page.go("/main")
                        ),
                        ProfileImage(),
                        SettingsHeader(),
                        SettingsSubheader(),
                        ft.Row(
                            [
                                StatisticsCard(),
                                AccountCard()

                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            width=1500,
                            height=346,
                        ),
                        ButtonLogOut()
                    ],
                    spacing=8
                ),
                width=1500,
                height=800
            )
        ]

    def change_to_statistics_screen(self, e):
        self.page.go("/main/account/statistics")

