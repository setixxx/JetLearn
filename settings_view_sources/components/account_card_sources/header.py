import flet as ft

class Header(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(left=21, top=16)
        self.width = 344
        self.height = 73
        self.content = ft.Row(
            [
                ft.Text(
                    "Персональные\nданные",
                    size=20,
                    weight=ft.FontWeight.W_500,
                    style=ft.TextStyle(
                        height=1.2
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START
        )