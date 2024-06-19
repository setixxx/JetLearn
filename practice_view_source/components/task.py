import flet as ft

class Task(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 1104
        self.height = 106
        self.padding = ft.padding.only(left=202)