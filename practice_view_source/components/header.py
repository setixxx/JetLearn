import flet as ft

class Header(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 1104
        self.height = 100
        self.padding = ft.padding.only(top=27)
        self.alignment = ft.alignment.top_center
        self.content = ft.Text(
            "Тренажер",
            size=40,
            weight=ft.FontWeight.W_500
        )