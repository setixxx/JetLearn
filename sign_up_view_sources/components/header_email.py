import flet as ft


class HeaderEmail(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 470
        self.height = 259
        self.alignment = ft.alignment.bottom_left
        self.padding = ft.padding.only(left=40)
        self.content = ft.Text(
            "Создать аккаунт\nJetLearn",
            text_align=ft.TextAlign.START,
            size=40,
            weight=ft.FontWeight.W_600,
            style=ft.TextStyle(
                height=1.2
            )
        )
