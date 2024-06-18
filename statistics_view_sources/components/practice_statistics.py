import flet as ft

class PracticeStatistics(ft.Card):
    def __init__(self, app_state):
        super().__init__()
        self.app_state = app_state
        self.content = ft.Column(
            [
                ft.Container(
                    ft.Text(
                        "Тренажер",
                        size=20,
                        weight=ft.FontWeight.W_500
                    ),
                    width=300,
                    height=45,
                    padding=ft.padding.only(left=32),
                    alignment=ft.alignment.bottom_left
                ),
                ft.Container(
                    ft.Text(
                        f"Правильно отвечено:\n"
                        f"{self.app_state.get_formatted_practice()}",
                        size=16,
                        weight=ft.FontWeight.W_400
                    ),
                    width=300,
                    height=81,
                    padding=ft.padding.only(left=32,
                                            top=16,
                                            bottom=16),
                    alignment=ft.alignment.top_left
                )
            ],
            width=300,
            height=126,
            spacing=0
        )
