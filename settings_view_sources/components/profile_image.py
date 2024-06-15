import flet as ft


class ProfileImage(ft.Row):
    def __init__(self):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 1500
        self.height = 100
        self.controls = [
            ft.Container(
                bgcolor="#006874",
                width=100,
                height=100,
                border_radius=100
            )
        ]
