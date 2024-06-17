import flet as ft


class ButtonChangeLogin(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.bottom_right
        self.padding = ft.padding.only(right=32,
                                       bottom=32)
        self.width = 344
        self.height = 72
        self.content = ft.FilledButton(
            text="Изменить",
        )
