import flet as ft


class TheoryCard(ft.Container):
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


class TheoryCards(ft.Container):
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
                        TheoryCard("Введение \nв Jetpack\nCompose",
                                   "assets/images/jetpack_compose_logo.png",
                                   lambda e: self.page.go("/main/theory_1")),
                        TheoryCard("Компоненты Compose и @Composable",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/theory_2")),
                        TheoryCard("Состояние и перерисовка",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/theory_3")),
                        TheoryCard("Модификаторы и стили",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/theory_4")),
                    ],
                    spacing=40
                ),
                ft.Row(
                    [
                        TheoryCard("Макеты и расположение",
                                   "assets/images/rows.png",
                                   lambda e: self.page.go("/main/theory_5")),
                        TheoryCard("Списки и отображение данных",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/theory_6")),
                        TheoryCard("Изображения \nи ресурсы \nв Compose",
                                   "assets/images/unnamed.jpg",
                                   lambda e: self.page.go("/main/theory_7")),
                        TheoryCard("Тема оформления и Material Design",
                                   "assets/images/material_design.png",
                                   lambda e: self.page.go("/main/theory_8")),
                    ],
                    spacing=40
                )
            ],
            spacing=40
        )
