import flet as ft
from theory_view_sources.components.code_theory import \
    CodeTheory
import json

json_file_path = 'theory.json'

# Функция для чтения данных из JSON файла
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data


class EighthTheoryText(ft.Container):
    def __init__(self, destination, page):
        super().__init__()
        self.destination = destination
        self.margin = ft.padding.only(right=39, bottom=32)
        self.alignment = ft.alignment.bottom_left
        self.width = 812
        self.height = 2200

        # Загрузка данных из JSON файла
        json_data = load_json_data(json_file_path)

        self.content = ft.Card(
            ft.Container(
                ft.Column(
                    [
                        ft.Text(
                            json_data[7]["title"],
                            size=28,
                            weight=ft.FontWeight.W_600
                        ),
                        ft.Text(
                            json_data[7]["content"][0],
                            size=20
                        ),
                        ft.Text(
                            json_data[7]["content"][1],
                            size=20
                        ),
                        ft.Text(
                            json_data[7]["content"][2],
                            size=20
                        ),
                        CodeTheory(json_data[7]["code_examples"][0], page),
                        ft.Text(
                            json_data[7]["content"][3],
                            size=20
                        ),
                        ft.Text(
                            json_data[7]["content"][4],
                            size=20
                        ),
                        ft.Text(
                            json_data[7]["content"][5],
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
                                        "Вперед"
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
