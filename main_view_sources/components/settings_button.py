import flet as ft
from main_view_sources.components.profile_image import ProfileImage

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
                        ProfileImage()
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
