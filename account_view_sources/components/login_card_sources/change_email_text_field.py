import flet as ft

class ChangeEmailTextField(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 344
        self.height = 104
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(top=16,
                                       left=32)
        self.content = ft.TextField(
            value="Логин",
            width=280
        )