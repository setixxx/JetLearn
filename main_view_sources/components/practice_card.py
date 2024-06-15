import flet as ft

class PracticeCard(ft.Container):
    def __init__(self, text, image, destination):
        super().__init__()
        self.destination = destination
        self.text = text
        self.image = image
        self.on_hover = self.on_hover_handler
        self.on_click = destination
        self.bgcolor = ft.colors.SECONDARY_CONTAINER
        self.border_radius = 12
        self.width = 435
        self.height = 625
        self.content = ft.Column(
            [
                ft.Image(
                    src=image,
                    width=435,
                    height=406,
                    border_radius=12,
                    fit=ft.ImageFit.COVER
                ),
                ft.Container(
                    ft.Text(
                        value=text,
                        size=48,
                        weight=ft.FontWeight.W_600,
                        text_align=ft.TextAlign.START,
                        style=ft.TextStyle(
                            height=1
                        ),
                    ),
                    width=435,
                    height=220,
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


class PracticeCards(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.padding = ft.padding.only(bottom=42)
        self.alignment = ft.alignment.center
        self.width = 1300
        self.height = 688
        self.content = ft.Column(
            [
                PracticeCard("Тренажер по\nвсему курсу",
                             f"assets/images/unnamed.jpg",
                             lambda e: self.page.go("/main/practice")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

