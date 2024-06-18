import flet as ft
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from theory_view_sources.components.theory_text import TheoryText

class TheoryView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = "/main/theory"
        self.padding = 0
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
                                    TheoryText(lambda e: self.page.go("/main"),
                                               self.page)
                                ],
                                scroll=ft.ScrollMode.AUTO
                            ),
                            margin=ft.padding.only(top=76)
                        ),
                    ]
                ),
                width=1500,
                height=800,
            )
        ]
