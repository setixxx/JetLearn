import flet as ft

from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from practice_view_source.components.header import Header

class PracticeView(ft.View):
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        self.page = page
        self.route = "/main/practice"
        self.padding = 0
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        ArrowBackAndLogo(
                            lambda e: self.page.go("/main")
                        ),
                        ft.Container(
                            ft.Column(
                                [
                                    Header(),

                                ]
                            ),
                            margin=ft.padding.only(top=62,
                                                   left=198,
                                                   right=198),
                            width=1104,
                            height=500,
                            border_radius=22,
                            bgcolor=ft.colors.SECONDARY_CONTAINER
                        )
                    ],
                    spacing=0
                ),
                width=1500,
                height=800,
            )
        ]

    def change_to_main_screen(self, e):
        self.page.go("/main")