import flet as ft
from theory_screens_sources.first_theory_screen_source.components.arrow_back_and_logo import ArrowBackAndLogo


class StatisticsView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = "/main/account/statistics"
        self.padding = 0
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        ArrowBackAndLogo(
                            lambda e: self.page.go("/main/account")
                        ),
                        ft.Row(
                            [
                                ft.Container(
                                    bgcolor="#006874",
                                    width=100,
                                    height=100,
                                    border_radius=100
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            width=1500,
                            height=100,
                        ),
                        ft.Row(
                            [
                                ft.Text(
                                    "Добро пожаловать, user!",
                                    size=32,
                                    weight=ft.FontWeight.W_700
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            width=1500,
                            height=44,
                        ),
                        ft.Row(
                            [
                                ft.Text(
                                    "Здесь вы можете настроить данные своего аккаунта или ознакомиться с вашей\n"
                                    "персональной статистикой",
                                    text_align=ft.TextAlign.CENTER,
                                    size=14,
                                    weight=ft.FontWeight.W_500
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            width=1500,
                            height=44,
                        ),
                        ft.Row(
                            [
                                # create_account_card()

                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            width=1500,
                            height=346,
                        )
                    ],
                    spacing=8
                ),
                width=1500,
                height=800
            )
        ]
