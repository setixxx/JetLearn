import flet as ft

class ChangeLoginTextField(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 344
        self.height = 114
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(top=16,
                                       left=32)
        self.content = ft.TextField(
            label="Логин",
            text_size=16,
            width=280,
            max_length=16,
        )