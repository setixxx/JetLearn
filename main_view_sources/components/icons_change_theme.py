import flet as ft
from main_view_sources.components.theme.accent_color_button import create_accent_color
class IconsChangeTheme(ft.Column):
    def __init__(self, translations, language):
        super().__init__()

        self.dark_light_text = ft.Text(
            "",
            weight=ft.FontWeight.W_600,
            size=16,
            text_align=ft.TextAlign.CENTER,
            style=ft.TextStyle(
                height=1.2
            )
        ),
        self.dark_light_icon = ft.IconButton(
            icon=ft.icons.DARK_MODE_OUTLINED,
            icon_color=ft.colors.ON_SURFACE,
            on_click=self.change_theme
        ),
        self.alignment = ft.MainAxisAlignment.CENTER,
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        self.spacing = 0
        self.translations = translations
        self.language = language

        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        ft.Column(
                            [
                                create_accent_color(),
                                ft.Text(
                                    "",
                                    weight=ft.FontWeight.W_600,
                                    size=16
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0
                        ),
                        IconsChangeTheme
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=ft.padding.only(bottom=42),
                width=100,
                height=370,
            )
        ]

    def change_theme(self, e):
        if self.page.theme_mode == 'dark':
            self.page.theme_mode = 'light'
            self.dark_light_icon.icon = ft.icons.DARK_MODE_OUTLINED
            self.dark_light_text.value = self.translations[self.language][
                "navigation_light_theme_button"]
        else:
            self.page.theme_mode = 'dark'
            self.dark_light_icon.icon = ft.icons.LIGHT_MODE_OUTLINED
            self.dark_light_text.value = self.translations[self.language][
                "navigation_dark_theme_button"]
        self.page.update()