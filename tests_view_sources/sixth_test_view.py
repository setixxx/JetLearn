import flet as ft
import json
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from tests_view_sources.components.sixth_test import SixthTest


class SixthTestView(ft.View):
    def __init__(self, page: ft.Page, db_manager, app_state):
        super().__init__()
        self.page = page
        self.db_manager = db_manager
        self.app_state = app_state
        self.padding = 0
        self.route = "/main/test_6"
        self.load_questions()

    def load_questions(self):
        with open("data/test.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            questions = data[5]["questions"]

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
                                    SixthTest(self.page, questions, self.restart_test, self.db_manager, self.app_state)
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

    def restart_test(self):
        self.load_questions()
        self.page.update()
