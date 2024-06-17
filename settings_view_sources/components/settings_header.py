import flet as ft


class SettingsHeader(ft.Row):
    def __init__(self, app_state):
        super().__init__()
        self.app_state = app_state
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 1500
        self.height = 44
        self.controls = [
            ft.Text(
                f"Добро пожаловать, {self.app_state.get_login()}!",
                size=32,
                weight=ft.FontWeight.W_700
            )
        ]
