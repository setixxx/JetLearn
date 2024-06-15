import flet as ft


class SettingsButton(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.padding = ft.padding.only(top=16, right=24)
        self.height = 113
        self.width = 1300
        self.content = ft.Row(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.SETTINGS_OUTLINED,
                            icon_color=ft.colors.ON_SURFACE,
                            on_click=lambda e: self.page.go("/main/settings")
                        ),
                        ft.Container(
                            bgcolor="#006874",
                            width=40,
                            height=40,
                            border_radius=40
                        )
                    ],
                    spacing=8,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
            spacing=0,
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
