import flet as ft
from theory_screens_sources.first_theory_screen_source.components.arrow_back_and_logo import ArrowBackAndLogo
from theory_screens_sources.first_theory_screen_source.components.table_of_contents import create_table_of_contents
from theory_screens_sources.first_theory_screen_source.components.theory_text import create_theory_text

class FirstTheoryView:
    def __init__(self, page: ft.Page):
        self.page = page

    def create_first_theory_screen(self):
        return ft.View(
            "/main/theory_1",
            [
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
                                    create_theory_text(self.change_to_main_screen)
                                ],
                                scroll=ft.ScrollMode.AUTO
                            ),
                            ft.Column(
                                [
                                    create_table_of_contents()
                                ]
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