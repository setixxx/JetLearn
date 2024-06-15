import flet as ft


class PopupColorItem(ft.PopupMenuItem):
    def __init__(self, color, name):
        super().__init__()
        self.content = ft.Row(
            controls=[
                ft.Icon(name=ft.icons.COLOR_LENS_OUTLINED, color=color),
                ft.Text(name),
            ],
        )
        self.on_click = self.seed_color_changed
        self.data = color

    def seed_color_changed(self, e):
        self.page.theme = self.page.dark_theme = ft.theme.Theme(
            color_scheme_seed=self.data
        )
        self.page.update()


class AccentColorButton(ft.Column):
    def __init__(self):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 0
        self.controls = [
            ft.PopupMenuButton(
                icon_color=ft.colors.ON_SURFACE,
                icon=ft.icons.COLOR_LENS_OUTLINED,
                items=[
                    PopupColorItem(color="deeppurple",
                                   name="Темно-фиолетовый"),
                    PopupColorItem(color="indigo",
                                   name="Индиго"),
                    PopupColorItem(color="blue",
                                   name="Голубой (по умолчанию)"),
                    PopupColorItem(color="teal",
                                   name="Бирюзовый"),
                    PopupColorItem(color="green",
                                   name="Зеленый"),
                    PopupColorItem(color="yellow",
                                   name="Желтый"),
                    PopupColorItem(color="orange",
                                   name="Оранжевый"),
                    PopupColorItem(color="deeporange",
                                   name="Темно-оранжевый"),
                    PopupColorItem(color="pink",
                                   name="Розовый"),
                ]
            ),
            ft.Text(
                "Цвет",
                weight=ft.FontWeight.W_600,
                size=16
            )
        ]
