import flet as ft


class Logo(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 200
        self.height = 60
        self.alignment = ft.alignment.center_left
        self.padding = ft.padding.only(left=24)
        self.content = ft.Text(
            "JetLearn",
            size=32,
            weight=ft.FontWeight.W_500
        )
