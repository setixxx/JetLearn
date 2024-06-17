import flet as ft
from theory_view_sources.first_theory_screen_source.components \
    .arrow_back_and_logo import ArrowBackAndLogo
from settings_view_sources.components.profile_image import ProfileImage
from statistics_view_sources.components.statistics_header \
    import StatisticsHeader


class StatisticsView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.title = "/main/settings/statistics"
        self.padding = 0
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        ArrowBackAndLogo(
                            lambda e: self.page.go("/main/settings")
                        ),
                        ProfileImage(),
                        StatisticsHeader(),
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        # LoginCard(),
                                        # EmailCard()
                                    ],
                                    spacing=23
                                ),
                                # PasswordCard()
                            ],
                            spacing=23,
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            width=1500,
                            height=494,
                        ),
                    ],
                ),
                width=1500,
                height=800
            )
        ]