import flet as ft
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from settings_view_sources.components.profile_image import ProfileImage
from statistics_view_sources.components.statistics_header \
    import StatisticsHeader
from statistics_view_sources.components.theory_statistics \
    import TheoryStatistics
from statistics_view_sources.components.practice_statistics import \
    PracticeStatistics
from statistics_view_sources.components.test_statistics import \
    TestStatistics


class StatisticsView(ft.View):
    def __init__(self, page: ft.Page, app_state):
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
                                        TheoryStatistics(app_state),
                                        PracticeStatistics(app_state)
                                    ],
                                    spacing=23
                                ),
                                TestStatistics(app_state)
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            width=1500,
                            height=284,
                        ),
                    ],
                ),
                width=1500,
                height=800
            )
        ]