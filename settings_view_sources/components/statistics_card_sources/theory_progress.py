import flet as ft


class TheoryProgress(ft.Container):
    def __init__(self, app_state):
        super().__init__()
        self.app_state = app_state
        self.padding = ft.padding.only(left=22)
        self.width = 344
        self.height = 79
        self.content = ft.Row(
            [
                ft.Container(
                    ft.Icon(
                        name=ft.icons.CLASS_OUTLINED,
                        color=ft.colors.ON_SURFACE
                    )
                ),
                ft.Column(
                    [
                        ft.Text(
                            "Пройденная теория",
                            size=14,
                            weight=ft.FontWeight.W_500
                        ),
                        ft.ProgressBar(
                            self.app_state.get_completed_theory(),
                            width=214,
                            height=4
                        ),
                        ft.Text(
                            f"Пройдено "
                            f"{self.app_state.get_formatted_theory()} "
                            f"разделов",
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
