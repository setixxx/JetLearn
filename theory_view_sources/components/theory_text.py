import flet as ft
from theory_view_sources.components.code_theory import \
    CodeTheory

class TheoryText(ft.Container):
    def __init__(self, destination, page):
        super().__init__()
        self.destination = destination
        self.margin = ft.padding.only(right=39, bottom=32)
        self.alignment = ft.alignment.bottom_left
        self.width = 812
        self.height = 2870
        self.content = ft.Card(
            ft.Container(
                ft.Column(
                    [
                        ft.Text(
                            "Что такое модификаторы",
                            size=28,
                            weight=ft.FontWeight.W_600
                        ),
                        ft.Text(
                            "Для настройки внешнего вида и стилизации большинства\n"
                            "встроенных компонентов в Jetpack Compose применяются так\n"
                            "называемые модификаторы. Модификаторы представляют\n"
                            "функции, которые задают какой-то отдельный аспект для\n"
                            "компонентов (или иными словами «модифицируют» внешний вид\n"
                            "компонента), например, установка размеров компонента или его\n"
                            "фонового цвета и т.д.\n"
                            "Большинство встронных компонентов поддерживают применение\n"
                            "модификаторов через параметр modifier. Например, возьмем ранее\n"
                            "встречавшийся простой компонент Text, который выводит\n"
                            "некоторый текст. Данный компонент, как и другие компоненты в\n"
                            "Jetpack Compose, определен в виде функции с\n"
                            "аннотацией @Compose, которая имеет ряд параметров:",
                            size=20
                        ),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.TextButton(
                                        "Назад",
                                        on_click=destination
                                    ),
                                    ft.FilledButton(
                                        "Вперед"
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                vertical_alignment=ft.CrossAxisAlignment.END
                            ),
                            padding=ft.padding.only(top=26),
                            width=773
                        )
                    ]
                ),
                padding=ft.padding.only(top=48, left=48, right=48),
            ),
            width=773
        )
