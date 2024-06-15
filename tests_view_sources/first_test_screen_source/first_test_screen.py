import flet as ft

from theory_screens_sources.first_theory_screen_source.components.arrow_back_and_logo import ArrowBackAndLogo
from tests_view_sources.first_test_screen_source.components.test_text import create_test_text

class FirstTestView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = 0
        self.route = "/main/test_1"
        self.controls = [
            ft.Container(
                ft.Row(
                    [
                        ft.Column(
                            [
                                ArrowBackAndLogo(
                                    lambda e: self.page.go("/main")
                                )
                            ]
                        ),
                        ft.Column(
                            [
                                create_test_text(self.change_to_main_screen)
                            ],
                            scroll=ft.ScrollMode.AUTO
                        )
                    ]
                ),
                width=1500,
                height=800,
            )
        ]

    def change_to_main_screen(self, e):
        self.page.go("/main")