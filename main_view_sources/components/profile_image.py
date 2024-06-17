import flet as ft


class ProfileImage(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = ft.colors.PRIMARY
        self.width = 40
        self.height = 40
        self.border_radius = 40
