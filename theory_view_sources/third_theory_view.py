import flet as ft
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from theory_view_sources.components.third_theory_text import ThirdTheoryText


class ThirdTheoryView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = "/main/theory_3"
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
                                    ThirdTheoryText(lambda e: self.page.go("/main/theory_2"),
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
