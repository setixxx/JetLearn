import flet as ft


class ArrowBackAndLogo(ft.Container):
    def __init__(self, destination):
        super().__init__()
        self.destination = destination
        self.padding = ft.padding.only(left=16)
        self.width = 245
        self.height = 88
        self.content = ft.Row(
            [
                ft.Container(
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=destination,
                    ),
                ),
                ft.Container(
                    ft.Text(
                        "JetLearn",
                        size=32,
                        weight=ft.FontWeight.W_500
                    ),
                    alignment=ft.alignment.center,
                    width=160,
                    height=76,
                )
            ],
            spacing=0,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
