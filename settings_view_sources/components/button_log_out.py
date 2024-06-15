import flet as ft


class ButtonLogOut(ft.Row):
    def __init__(self):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.END
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 1500
        self.height = 178
        self.controls = [
            ft.Container(
                ft.FilledButton(
                    "Выйти из аккаунта",
                    on_click=lambda e: self.page.go("/sign_in")
                ),
                padding=ft.padding.only(right=32)
            )
        ]
