import flet as ft

def create_modifier_first_code():
    return ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.CONTENT_COPY,
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
        ),
        padding=ft.padding.only(left=32, bottom=32, top=8, right=8),
        alignment=ft.alignment.top_left,
        width=773,
        border_radius=20,
        bgcolor=ft.colors.ON_SURFACE
    )