import flet as ft


class IntroductionText(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 1200
        self.height = 85
        self.content = ft.Row(
            [
                ft.Text(
                    value="Начните своё путешествие в мир Jetpack Compose – "
                          "создавайте удивительные\nинтерфейсы"
                          "уже сегодня!",
                    size=16,
                    weight=ft.FontWeight.W_700,
                    text_align=ft.TextAlign.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
