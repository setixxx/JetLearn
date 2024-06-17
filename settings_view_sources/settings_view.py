import flet as ft
from theory_view_sources.first_theory_screen_source.components.arrow_back_and_logo import ArrowBackAndLogo
from settings_view_sources.components.profile_image import ProfileImage
from settings_view_sources.components.settings_header import SettingsHeader
from settings_view_sources.components.settings_subheader import SettingsSubheader
from settings_view_sources.components.button_log_out import ButtonLogOut
from settings_view_sources.components.statistics_card import StatisticsCard
from settings_view_sources.components.account_card import AccountCard


class SettingsView(ft.View):
    def __init__(self, page: ft.Page, app_state):
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
                        SettingsHeader(app_state),
                        SettingsSubheader(),
                        ft.Row(
                            [
                                StatisticsCard(app_state),
                                AccountCard()
                            ],
                            spacing=23,
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

