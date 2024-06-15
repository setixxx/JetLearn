import flet as ft


class ButtonAccountCreationAndLogIn(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 423
        self.height = 90
        self.padding = ft.padding.only(bottom=32, right=32)
        self.alignment = ft.alignment.bottom_right
        self.content = ft.Row(
            [
                ft.TextButton(
                    "Создать аккаунт",
                    on_click=lambda e: self.page.go("/sign_up")
                ),
                ft.FilledButton(
                    "Войти",
                    on_click=lambda e: self.page.go("/main")
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=11
        )