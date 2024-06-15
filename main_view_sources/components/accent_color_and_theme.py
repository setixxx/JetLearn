import flet as ft
from main_view_sources.components.theme.accent_color_button import \
    AccentColorButton
from main_view_sources.components.theme.theme_button import ThemeButton


class AccentColorAndTheme(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(bottom=42)
        self.width = 100
        self.height = 370
        self.content = ft.Column(
            [
                AccentColorButton(),
                ThemeButton(),
            ],
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
