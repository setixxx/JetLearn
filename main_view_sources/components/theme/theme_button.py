import flet as ft


class ThemeButton(ft.Column):
    def __init__(self):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 0
        self.controls = [
            ft.IconButton(
                icon=ft.icons.DARK_MODE_OUTLINED,
                icon_color=ft.colors.ON_SURFACE,
                on_click=self.change_theme
            ),
            ft.Text(
                value="Светлая тема",
                weight=ft.FontWeight.W_600,
                size=16,
                text_align=ft.TextAlign.CENTER,
                style=ft.TextStyle(
                    height=1.2
                )
            )
        ]

    def change_theme(self, e):
        if self.page.theme_mode == 'dark':
            self.page.theme_mode = 'light'
            self.controls[0].icon = ft.icons.DARK_MODE_OUTLINED
            self.controls[1].value = "Светлая\nтема"
        else:
            self.page.theme_mode = 'dark'
            self.controls[0].icon = ft.icons.LIGHT_MODE_OUTLINED
            self.controls[1].value = "Темная\nтема"
        self.page.update()
