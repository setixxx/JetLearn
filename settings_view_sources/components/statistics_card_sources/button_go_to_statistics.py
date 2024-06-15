import flet as ft


class ButtonGoToStatistics(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.bottom_right
        self.padding = ft.padding.only(bottom=22, right=22)
        self.width = 344
        self.height = 84
        self.content = ft.FilledButton(
            "Перейти",
            on_click=lambda e: self.page.go(
                "/main/settings/statistic")
        )
