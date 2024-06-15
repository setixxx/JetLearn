import flet as ft


class PasswordCheckBox(ft.Container):
    def __init__(self, show_password):
        super().__init__()
        self.width = 635
        self.height = 64
        self.padding = ft.padding.only(bottom=20,
                                       right=160)
        self.alignment = ft.alignment.bottom_right
        self.content = ft.Row(
            [
                ft.Checkbox(
                    label="Показать пароль",
                    value=False,
                    on_change=show_password
                )
            ],
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.END
        )
