import flet as ft


class ButtonNextAndLogIn(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 635
        self.height = 82
        self.padding = ft.padding.only(bottom=32, right=32)
        self.alignment = ft.alignment.bottom_right
        self.content = ft.Row(
            [
                ft.TextButton(
                    "Войти в существующий",
                    on_click=lambda e: self.page.go("/sign_in")
                ),
                ft.FilledButton(
                    "Далее",
                    on_click=lambda e: self.page.go("/main")
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=11
        )
