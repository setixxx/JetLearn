import flet as ft


class SupportTextLogIn(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 461
        self.height = 208
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(left=28, top=12)
        self.content = ft.Text(
            value="Используйте аккаунт JetBrains",
            weight=ft.FontWeight.W_400,
            size=16,
        )
