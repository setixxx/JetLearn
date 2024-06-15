import flet as ft


class LoginAndPasswordTextField(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 423
        self.height = 252
        self.alignment = ft.alignment.top_left
        self.content = ft.Column(
            [
                ft.TextField(
                    label="Логин или адрес эл. почты",
                    text_size=16,
                    text_vertical_align=-0.9,
                    width=391,
                    height=68,
                    max_length=36
                ),
                ft.TextField(
                    label="Пароль",
                    text_size=16,
                    text_vertical_align=-0.9,
                    width=391,
                    height=68,
                    max_length=16,
                    password=True,
                )
            ],
            spacing=16,
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )
