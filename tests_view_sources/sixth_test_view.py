import flet as ft
import json
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from tests_view_sources.results import Results
from tests_view_sources.test_text import TestText


class SixthTest(ft.Container):
    def __init__(self, page, questions, restart_test, db_manager, app_state):
        super().__init__()
        self.page = page
        self.questions = questions
        self.restart_test = restart_test
        self.db_manager = db_manager
        self.app_state = app_state
        self.margin = ft.padding.only(right=39, bottom=32)
        self.alignment = ft.alignment.bottom_left
        self.width = 812
        self.height = 1700
        self.test_texts = []
        self.content = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(
                                                "Тест по шестому модулю",
                                                size=40,
                                                weight=ft.FontWeight.W_600
                                            ),
                                            ft.Text(
                                                'Заполните приведенные ниже поля и по завершении нажмите\nкнопку'
                                                ' "Закончить" для получения результата. Успехов!',
                                                size=16,
                                                weight=ft.FontWeight.W_600
                                            ),
                                        ]
                                    )
                                ]
                            ),
                        ),
                        *self.create_test_texts(),
                        Results(self.page,
                                self.test_texts,
                                self.restart_test,
                                self.db_manager,
                                self.app_state,
                                "TESTS_5"),
                    ]
                ),
                padding=ft.padding.only(left=48, right=48),
            ),
            width=812
        )

    def create_test_texts(self):
        test_texts = []
        for question_data in self.questions:
            question = question_data["question"]
            options = question_data["options"]
            correct_answer = question_data["correct_answer"]
            test_text = TestText(question, options, correct_answer)
            test_texts.append(test_text)
        self.test_texts = test_texts
        return test_texts


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
