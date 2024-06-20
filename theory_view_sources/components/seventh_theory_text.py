import flet as ft
from theory_view_sources.components.code_theory import \
    CodeTheory
import json
from database import DatabaseManager


json_file_path = 'data/theory.json'

# Функция для чтения данных из JSON файла
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data

class SeventhTheoryText(ft.Container):
    def __init__(self, destination, page, app_state):
        super().__init__()
        self.page = page
        self.database = DatabaseManager("users.sqlite")
        self.app_state = app_state
        self.destination = destination
        self.margin = ft.padding.only(right=39, bottom=32)
        self.alignment = ft.alignment.bottom_left
        self.width = 812
        self.height = 1990

        # Загрузка данных из JSON файла
        json_data = load_json_data(json_file_path)

        self.content = ft.Card(
            ft.Container(
                ft.Column(
                    [
                        ft.Text(
                            json_data[6]["title"],
                            size=28,
                            weight=ft.FontWeight.W_600
                        ),
                        ft.Text(
                            json_data[6]["content"][0],
                            size=20
                        ),
                        ft.Text(
                            json_data[6]["content"][1],
                            size=20
                        ),
                        CodeTheory(json_data[6]["code_examples"][0], page),
                        ft.Text(
                            json_data[6]["content"][2],
                            size=20
                        ),
                        ft.Text(
                            json_data[6]["content"][3],
                            size=20
                        ),
                        CodeTheory(json_data[6]["code_examples"][1], page),
                        ft.Text(
                            json_data[6]["content"][4],
                            size=20
                        ),
                        ft.Text(
                            json_data[6]["content"][5],
                            size=20
                        ),
                        ft.Text(
                            json_data[6]["content"][6],
                            size=20
                        ),
                        ft.Text(
                            json_data[6]["content"][7],
                            size=20
                        ),
                        ft.Text(
                            json_data[6]["content"][8],
                            size=20
                        ),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.TextButton(
                                        "Назад",
                                        on_click=destination
                                    ),
                                    ft.FilledButton(
                                        "Вперед",
                                        on_click=lambda e:
                                        self.update_theory_state(
                                            self.app_state.get_login(),
                                            "THEORY_7"
                                        )
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                vertical_alignment=ft.CrossAxisAlignment.END
                            ),
                            padding=ft.padding.only(top=26),
                            width=773
                        )
                    ]
                ),
                padding=ft.padding.only(top=48, left=48, right=48),
            ),
            width=773
        )

    def update_theory_state(self, login, theory):
        self.database.update_theory(login, theory, True),
        completed_theory = self.database.get_completed_theory_count(login)
        self.app_state.set_completed_theory(completed_theory),
        self.page.go("/main/theory_8")
