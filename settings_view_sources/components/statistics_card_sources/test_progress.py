import flet as ft

class TestProgress(ft.Container):
    def __init__(self, app_state):
        super().__init__()
        self.app_state = app_state
        self.padding = ft.padding.only(left=22)
        self.width = 344
        self.height = 82
        self.content = ft.Row(
            [
                ft.Container(
                    ft.Icon(
                        name=ft.icons.BROWSE_GALLERY_OUTLINED,
                        color=ft.colors.ON_SURFACE
                    )
                ),
                ft.Column(
                    [
                        ft.Text(
                            "Пройденные тесты",
                            size=14,
                            weight=ft.FontWeight.W_500
                        ),
                        ft.ProgressBar(
                            self.app_state.get_completed_tests(),
                            width=214,
                            height=4
                        ),
                        ft.Text(
                            f"Пройдено "
                            f"{self.app_state.get_formatted_tests()} "
                            f"тестов",
                            size=12,
                            weight=ft.FontWeight.W_300
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )