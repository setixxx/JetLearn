import flet as ft


class TestCard(ft.Container):
    def __init__(self, text, image, destination):
        super().__init__()
        self.destination = destination
        self.text = text
        self.image = image
        self.on_hover = self.on_hover_handler
        self.on_click = destination
        self.bgcolor = ft.colors.SECONDARY_CONTAINER
        self.border_radius = 12
        self.width = 231
        self.height = 303
        self.content = ft.Column(
            [
                ft.Image(
                    src=image,
                    width=231,
                    height=197,
                    border_radius=12,
                    fit=ft.ImageFit.COVER
                ),
                ft.Container(
                    ft.Text(
                        value=text,
                        size=24,
                        weight=ft.FontWeight.W_600,
                        text_align=ft.TextAlign.START,
                        style=ft.TextStyle(
                            height=1
                        ),
                    ),
                    width=231,
                    height=106,
                    alignment=ft.alignment.top_left,
                    padding=16
                )
            ],
            spacing=0
        )

    def on_hover_handler(self, e):
        self.bgcolor = ft.colors.GREY_400 if e.data == "true" \
            else ft.colors.SECONDARY_CONTAINER
        self.update()

class TestCards(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.padding = ft.padding.only(left=77)
        self.alignment = ft.alignment.top_left
        self.width = 1300
        self.height = 688
        self.content = ft.Column(
            [
                ft.Row(
                    [
                        TestCard("Тест по\nпервому модулю",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/test_1")),
                        TestCard("Тест по\nвторому\nмодулю",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/test_2")),
                        TestCard("Тест по\nтретьему модулю",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/test_3")),
                        TestCard("Тест по\nчетвертому модулю",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/test_4")),
                    ],
                    spacing=40
                ),
                ft.Row(
                    [
                        TestCard("Тест по\nпятому\nмодулю",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/test_5")),
                        TestCard("Тест по\nшестому\nмодулю",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/test_6")),
                        TestCard("Тест по\nседьмому модулю",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/test_7")),
                        TestCard("Тест по\nвосьмому модулю",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/test_8")),
                    ],
                    spacing=40
                )
            ],
            spacing=40
        )

