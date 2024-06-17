import flet as ft

from theory_view_sources.first_theory_screen_source.components.arrow_back_and_logo import ArrowBackAndLogo
from practice_screens_sources.practice_screen_source.components.practice_text import create_practice_text

class PracticeScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def create_practice_screen(self):
        return ft.View(
            "/main/practice",
            [
                ft.Container(
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ArrowBackAndLogo(
                                        lambda e: self.page.go("/main")
                                    ),
                                ]
                            ),
                            ft.Column(
                                [
                                    create_practice_text(self.change_to_main_screen)
                                ],
                                scroll=ft.ScrollMode.AUTO
                            )
                        ]
                    ),
                    width=1500,
                    height=800,
                ),
            ],
            padding=0
        )

    def change_to_main_screen(self, e):
        self.page.go("/main")