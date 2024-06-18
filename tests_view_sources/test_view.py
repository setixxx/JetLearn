import flet as ft

from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from tests_view_sources.components.test_text import TestText

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
                        ft.Container(
                            ft.Column(
                                [
                                    TestText(self.change_to_main_screen)
                                ],
                                scroll=ft.ScrollMode.AUTO
                            ),
                            margin=ft.padding.only(top=76)
                        )
                    ]
                ),
                width=1500,
                height=800,
            )
        ]

    def change_to_main_screen(self, e):
        self.page.go("/main")