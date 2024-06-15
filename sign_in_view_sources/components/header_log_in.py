import flet as ft


class HeaderLogIn(ft.Container):
    def __init__(self):
        super().__init__()
        self.height = 134
        self.width = 461
        self.alignment = ft.alignment.bottom_left
        self.padding = ft.padding.only(left=24)
        self.content = ft.Text(
            value="Вход",
            weight=ft.FontWeight.W_600,
            size=40,
            style=ft.TextStyle(
                height=1.2
            )
        )
