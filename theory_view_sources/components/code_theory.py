import flet as ft

class CodeTheory(ft.Container):
    def __init__(self, code, page):
        super().__init__()
        self.page = page
        self.code = code
        self.padding = ft.padding.only(left=32, bottom=32, top=8, right=8)
        self.alignment = ft.alignment.top_left
        self.width = 773
        self.border_radius = 20
        self.bgcolor = ft.colors.ON_SURFACE
        self.content = ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.CONTENT_COPY,
                            on_click=self.copy_code
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    width=773
                ),
                ft.Row(
                    [
                        ft.Text(
                            self.code,
                            color=ft.colors.BACKGROUND
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            spacing=0
        )

    def copy_code(self, e):
        self.page.set_clipboard(self.code)
        self.page.snack_bar = ft.SnackBar(ft.Text("Текст скопирован в буфер обмена!"))
        self.page.snack_bar.open = True
        self.page.update()
