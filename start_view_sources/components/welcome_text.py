import flet as ft


class WelcomeText(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 1200
        self.height = 228
        self.content = ft.Row(
            [
                ft.Text(
                    value="Добро пожаловать \nв JetLearn",
                    size=56,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    style=ft.TextStyle(
                        height=1.2,
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.END
        )
