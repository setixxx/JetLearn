import flet as ft

def create_set_sizes_code():
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
                            "package com.example.helloapp\n"
                            "import android.os.Bundle\n"
                            "import androidx.activity.ComponentActivity\n"
                            "import androidx.activity.compose.setContent\n"
                            "import androidx.compose.foundation.background\n"
                            "import androidx.compose.foundation.layout.height\n"
                            "import androidx.compose.foundation.layout.width\n"
                            "import androidx.compose.material3.Text\n"
                            "import androidx.compose.ui.Modifier\n"
                            "import androidx.compose.ui.graphics.Color\n"
                            "import androidx.compose.ui.unit.dp\n"
                            "import androidx.compose.ui.unit.sp\n"
                            "\n"
                            "class MainActivity : ComponentActivity() {\n"
                            "   override fun onCreate(savedInstanceState: Bundle?) {\n"
                            "       super.onCreate(savedInstanceState)\n"
                            "       setContent {\n"
                            '           Text(\n'
                            '               "Hello METANIT.COM",\n'
                            "               fontSize=28.sp,\n"
                            "               modifier = Modifier\n"
                            "                                   .background(color=Color.LightGray)\n"
                            "                                   .width(300.dp)\n"
                            "                                   .height(200.dp)\n"
                            "           )\n"
                            "       }\n"
                            "   }\n"
                            "}",
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