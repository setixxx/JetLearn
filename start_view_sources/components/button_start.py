import flet as ft


class ButtonStart(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(top=21)
        self.width = 1198
        self.height = 212
        self.content = ft.Row(
            [
                ft.FilledButton(
                    text="Начать обучение",
                    icon="TOKEN_OUTLINED",
                    width=238,
                    height=63,
                    on_click=lambda e: self.page.go("/sign_in")
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START
        )
