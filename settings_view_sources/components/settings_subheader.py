import flet as ft

class SettingsSubheader(ft.Row):
    def __init__(self):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 1500
        self.height = 44
        self.controls = [
            ft.Text(
                "Здесь вы можете настроить данные своего аккаунта или ознакомиться с вашей\n"
                "персональной статистикой",
                text_align=ft.TextAlign.CENTER,
                size=14,
                weight=ft.FontWeight.W_500
            )
        ]