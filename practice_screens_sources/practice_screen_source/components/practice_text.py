import flet as ft


def create_practice_text(go_back):
    return ft.Container(
        ft.Container(
            ft.Container(
                ft.Column(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(
                                                "Тренажер",
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
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.FilledButton(
                                                "Закончить",
                                            )

                                        ],
                                        spacing=16
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END
                            ),
                            padding=ft.padding.only(top=16, bottom=16),
                            border_radius=20
                        ),
                    ]
                ),
                padding=ft.padding.only(top=48, left=48, right=48),
            ),
            width=812
        ),
        margin=ft.padding.only(top=36, right=39, bottom=32),
        alignment=ft.alignment.bottom_left,
        width=812,
        height=1000,
    )
