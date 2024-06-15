import flet as ft

class Subheader(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(left=22)
        self.width = 344
        self.height = 56
        self.content = ft.Row(
            [
                ft.Text(
                    "Детальная информация о пройденных\n"
                    "вами, а также остальными,\n"
                    "пользователями тестах",
                    size=14,
                    weight=ft.FontWeight.W_500,
                    style=ft.TextStyle(
                        height=1.2
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.END
        )