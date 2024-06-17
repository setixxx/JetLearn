import flet as ft

class ChangePasswordTextField(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 344
        self.height = 228
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(top=16,
                                       left=32)
        self.content = ft.Column(
            [
                ft.TextField(
                    label="Старый пароль",
                    text_size=16,
                    width=280,
                    max_length=16,
                ),
                ft.TextField(
                    label="Новый пароль",
                    text_size=16,
                    width=280,
                    max_length=16,
                )
            ],
        )