import flet as ft


class SettingsHeader(ft.Row):
    def __init__(self):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 1500
        self.height = 44
        self.controls = [
            ft.Text(
                "Добро пожаловать, user!",
                size=32,
                weight=ft.FontWeight.W_700
            )
        ]
