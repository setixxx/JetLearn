import flet as ft

class ButtonGoToAccount(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.bottom_right
        self.padding = ft.padding.only(bottom=22, right=22)
        self.width = 344
        self.height = 149
        self.content = ft.Row(
            [
                ft.FilledButton(
                    "Перейти",
                    on_click=lambda e: self.page.go("/main/settings/account")
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.END
        )