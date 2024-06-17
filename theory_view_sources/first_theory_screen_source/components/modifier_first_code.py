import flet as ft

class Code(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
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
                            "@Composable\n"
                            "fun Text(\n"
                            "   value: String,\n"
                            "   modifier: Modifier = Modifier,\n"
                            "\n"
                            "   //..... остальные параметры\n"
                            "\n"
                            "): @Composable Unit",
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
        code_to_copy = self.content.controls[1].controls[0].value
        self.page.set_clipboard(code_to_copy)
        self.page.snack_bar = ft.SnackBar(ft.Text("Текст скопирован в буфер обмена!"))
        self.page.snack_bar.open = True
        self.page.update()
