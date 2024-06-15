import flet as ft


class NavigationRail(ft.Container):
    def __init__(self, change_view_callback):
        super().__init__()
        self.alignment = ft.alignment.top_left
        self.width = 200
        self.height = 370
        self.content = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            height=364,
            width=100,
            group_alignment=-1.0,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.BOOK_OUTLINED,
                    selected_icon=ft.icons.BOOK,
                    label_content=ft.Text(
                        "Теория",
                        size=16,
                        weight=ft.FontWeight.W_600
                    ),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.BROWSE_GALLERY_OUTLINED,
                    selected_icon=ft.icons.BROWSE_GALLERY,
                    label_content=ft.Text(
                        "Тесты",
                        size=16,
                        weight=ft.FontWeight.W_600
                    )
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.VIEW_IN_AR_OUTLINED,
                    selected_icon=ft.icons.VIEW_IN_AR,
                    label_content=ft.Text(
                        "Тренажер",
                        size=16,
                        weight=ft.FontWeight.W_600
                    )
                )
            ],
            on_change=change_view_callback
        )


