import flet as ft
from database import DatabaseManager


class TestStatistics(ft.Card):
    def __init__(self, app_state):
        super().__init__()
        self.database = DatabaseManager("users.sqlite")
        self.app_state = app_state
        self.results, self.grades = self.database.get_test_results_and_grades(
            self.app_state.get_login())

        self.content = ft.Column(
            [
                ft.Container(
                    ft.Text(
                        "Тесты",
                        size=20,
                        weight=ft.FontWeight.W_500
                    ),
                    width=300,
                    height=36,
                    padding=ft.padding.only(left=32),
                    alignment=ft.alignment.bottom_left
                ),
                ft.Container(
                    ft.Row(
                        [
                            ft.Text(
                                "Тест:\n" + "\n".join(
                                    [f"{i + 1}:" for i in range(8)]),
                                size=16,
                                weight=ft.FontWeight.W_400,
                                text_align=ft.TextAlign.LEFT
                            ),
                            ft.Text(
                                "Результат:\n" + "\n".join(
                                    [f"{result}/5" for result in
                                     self.results]),
                                size=16,
                                weight=ft.FontWeight.W_400,
                                text_align=ft.TextAlign.LEFT
                            ),
                            ft.Text(
                                "Оценка:\n" + "\n".join(
                                    [str(grade) for grade in self.grades]),
                                size=16,
                                weight=ft.FontWeight.W_400,
                                text_align=ft.TextAlign.LEFT
                            )
                        ],
                        spacing=32
                    ),
                    width=300,
                    height=248,
                    padding=ft.padding.only(left=32, top=16, bottom=16,
                                            right=32),
                    alignment=ft.alignment.top_center
                )
            ],
            width=300,
            height=290,
            spacing=0
        )
