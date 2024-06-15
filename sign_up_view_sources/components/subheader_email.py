import flet as ft


class SubheaderEmail(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 470
        self.height = 241
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(left=40, top=15)
        self.content = ft.Text(
            value="Введите свои данные и придумайте надежный\n"
                  "пароль, состоящий из букв, цифр и других \n"
                  "символов",
            weight=ft.FontWeight.W_400,
            size=16,
        )
