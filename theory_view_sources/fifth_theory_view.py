import flet as ft
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from theory_view_sources.components.fifth_theory_text import FifthTheoryText

class FifthTheoryView(ft.View):
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        self.page = page
        self.route = "/main/theory_5"
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
                                    FifthTheoryText(
                                        lambda e:
                                        self.page.go("/main/theory_4"),
                                        self.page,
                                        app_state)
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
