import flet as ft


class TableOfContents(ft.Container):
    def __init__(self):
        super().__init__()
        self.margin = ft.padding.only(top=76)
        self.alignment = ft.alignment.bottom_left
        self.width = 400
        self.height = 800
        self.content = ft.Column(
            [
                ft.Container(
                    ft.Row(
                        [
                            ft.Text(
                                "Модификаторы и визуальный\nинтерфейс",
                                size=16,
                                weight=ft.FontWeight.W_600,
                                text_align=ft.TextAlign.START
                            )
                        ]
                    ),
                    padding=ft.padding.only(left=16),
                    margin=ft.padding.only(bottom=8),
                    width=360,
                    height=56
                ),
                ft.Container(
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ARTICLE_OUTLINED),
                        title=ft.Text(
                            "Что такое модификаторы",
                            size=16,
                            weight=ft.FontWeight.W_500
                        ),
                        selected=False,
                    ),
                    width=360,
                    height=56
                ),
                ft.Container(
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ARTICLE_OUTLINED),
                        title=ft.Text(
                            "Установка цвета",
                            size=16,
                            weight=ft.FontWeight.W_500
                        ),
                        selected=False,
                    ),
                    width=360,
                    height=56
                ),
                ft.Container(
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ARTICLE_OUTLINED),
                        title=ft.Text(
                            "Установка размеров",
                            size=16,
                            weight=ft.FontWeight.W_500
                        ),
                        selected=False,
                    ),
                    width=360,
                    height=56
                )
            ],
            spacing=0
        )
