import flet as ft


class ResultsDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        self.modal = True
        self.title = ft.Text(
            "Результаты теста",
            weight=ft.FontWeight.W_600
        )
        self.content = TextResults()
        self.actions = [
            ft.TextButton(
                text="Закончить",
                on_click=lambda e: self.page.go("/main")
            ),
            ft.FilledButton(
                "Начать заново",
                on_click=self.close_results
            ),
        ]
        self.actions_alignment = ft.MainAxisAlignment.END

    def close_results(self, e):
        self.open = False
        self.page.update()


class TextResults(ft.Container):
    def __init__(self):
        super().__init__()
        self.height = 70
        self.content = ft.Column(
            [
                ft.Text(
                    "Отвечено правильно: 5/10",
                    size=16
                ),
                ft.Text(
                    "Ваша оценка: 3",
                    size=16
                )
            ]
        )



class Results(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(top=16, bottom=16)
        self.border_radius = 20
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.FilledButton(
                            "Закончить",
                            on_click=self.open_results
                        )

                    ],
                    spacing=16
                )
            ],
            alignment=ft.MainAxisAlignment.END
        )

    def open_results(self, e):
        self.page.dialog = ResultsDialog()
        self.page.dialog.open = True
        self.page.update()
