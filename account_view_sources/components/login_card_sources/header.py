import flet as ft


class Header(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(left=21, bottom=3)
        self.width = 344
        self.height = 45
        self.content = ft.Row(
            [
                ft.Text(
                    "Изменение логина",
                    size=20,
                    weight=ft.FontWeight.W_500
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.END
        )
