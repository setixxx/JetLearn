import flet as ft

class TestProgress(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(left=22)
        self.width = 344
        self.height = 82
        self.content = ft.Row(
            [
                ft.Container(
                    ft.Icon(
                        name=ft.icons.BROWSE_GALLERY_OUTLINED,
                        color=ft.colors.ON_SURFACE
                    )
                ),
                ft.Column(
                    [
                        ft.Text(
                            "Пройденные тесты",
                            size=14,
                            weight=ft.FontWeight.W_500
                        ),
                        ft.ProgressBar(
                            0.8,
                            width=214,
                            height=4
                        ),
                        ft.Text(
                            "Пройдено 8 из 10 тестов",
                            size=12,
                            weight=ft.FontWeight.W_300
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )