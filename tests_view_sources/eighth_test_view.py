import flet as ft
import json
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from tests_view_sources.components.eighth_test import EighthTest


class EighthTestView(ft.View):
    def __init__(self, page: ft.Page, db_manager, app_state):
        super().__init__()
        self.page = page
        self.db_manager = db_manager
        self.app_state = app_state
        self.padding = 0
        self.route = "/main/test_8"
        self.load_questions()

    def load_questions(self):
        with open("data/test.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            questions = data[7]["questions"]

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
                                    EighthTest(self.page, questions, self.restart_test, self.db_manager, self.app_state)
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
