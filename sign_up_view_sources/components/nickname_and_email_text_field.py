import flet as ft


class NicknameAndEmailTextField(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 635
        self.height = 354
        self.padding = ft.padding.only(right=32)
        self.alignment = ft.alignment.bottom_right
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        ft.TextField(
                            label="Логин",
                            text_size=16,
                            # text_vertical_align=-0.9,
                            width=271,
                            max_length=16
                        ),
                        ft.TextField(
                            label="Адрес эл. почты",
                            text_size=16,
                            width=271,
                            max_length=36,
                        )
                    ],
                    spacing=16,
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                ),
                ft.Column(
                    [
                        ft.TextField(
                            label="Пароль",
                            password=True,
                            text_size=16,
                            width=271,
                            max_length=16
                        ),
                        ft.TextField(
                            label="Подтверждение пароля",
                            text_size=16,
                            width=271,
                            max_length=16,
                            password=True,
                        )
                    ],
                    spacing=16,
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                )
            ],
            spacing=32,
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.END
        )
