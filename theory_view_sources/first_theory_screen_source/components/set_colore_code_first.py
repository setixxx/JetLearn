import flet as ft

def create_set_colore_code_first():
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
                            "fun Modifier.background(\n"
                            "                                   color: Color,\n"
                            "                                   shape: Shape = RectangleShape\n"
                            "): Modifier",
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