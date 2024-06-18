import flet as ft
from tests_view_sources.results import Results


class TestText(ft.Container):
    def __init__(self, destination):
        super().__init__()
        self.destination = destination
        self.margin = ft.padding.only(right=39, bottom=32)
        self.alignment = ft.alignment.bottom_left
        self.width = 812
        self.height = 1000
        self.content = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(
                                                "Тест по первому модулю",
                                                size=40,
                                                weight=ft.FontWeight.W_600
                                            ),
                                            ft.Text(
                                                'Заполните приведенные ниже поля и по завершении нажмите\nкнопку'
                                                ' "Закончить" для получения результата. Успехов!',
                                                size=16,
                                                weight=ft.FontWeight.W_600
                                            ),

                                        ]
                                    )
                                ]
                            ),
                            padding=16,
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=20
                        ),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(
                                                'Здесь будет первый вопрос',
                                                size=20,
                                                weight=ft.FontWeight.W_600
                                            ),
                                            ft.TextField(
                                                label="Your answer",
                                                width=500
                                            )

                                        ],
                                        spacing=16
                                    )
                                ]
                            ),
                            padding=16,
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=20
                        ),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(
                                                'Здесь будет второй вопрос',
                                                size=20,
                                                weight=ft.FontWeight.W_600
                                            ),
                                            ft.TextField(
                                                label="Your answer",
                                                width=500
                                            )

                                        ],
                                        spacing=16
                                    )
                                ]
                            ),
                            padding=16,
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=20
                        ),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(
                                                'Здесь будет третий вопрос',
                                                size=20,
                                                weight=ft.FontWeight.W_600
                                            ),
                                            ft.TextField(
                                                label="Your answer",
                                                width=500
                                            )

                                        ],
                                        spacing=16
                                    )
                                ]
                            ),
                            padding=16,
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=20
                        ),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(
                                                'Здесь будет четвертый вопрос',
                                                size=20,
                                                weight=ft.FontWeight.W_600
                                            ),
                                            ft.TextField(
                                                label="Your answer",
                                                width=500
                                            )

                                        ],
                                        spacing=16
                                    )
                                ]
                            ),
                            padding=16,
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=20
                        ),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(
                                                'Здесь будет пятый вопрос',
                                                size=20,
                                                weight=ft.FontWeight.W_600
                                            ),
                                            ft.TextField(
                                                label="Your answer",
                                                width=500
                                            )

                                        ],
                                        spacing=16
                                    )
                                ]
                            ),
                            padding=16,
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=20
                        ),
                        Results(),
                    ]
                ),
                padding=ft.padding.only(left=48, right=48),
            ),
            width=812
        )
