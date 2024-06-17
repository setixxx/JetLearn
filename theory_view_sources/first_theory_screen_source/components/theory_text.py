import flet as ft
from theory_view_sources.first_theory_screen_source.components.modifier_first_code import \
    Code
from theory_view_sources.first_theory_screen_source.components.set_colore_code_first import \
    create_set_colore_code_first
from theory_view_sources.first_theory_screen_source.components.set_color_code_second import \
    create_set_color_code_second
from theory_view_sources.first_theory_screen_source.components.set_sizes_code import \
    create_set_sizes_code


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
                        Code(page),
                        ft.Text(
                            "Установка цвета",
                            size=28,
                            weight=ft.FontWeight.W_600
                        ),
                        ft.Text(
                            "Для установки фонового цвета применяется модификатор \n"
                            "background(). Есть две версии этой функции. Первая версия:",
                            size=20
                        ),
                        create_set_colore_code_first(),
                        ft.Text(
                            "   • color: значение цвета в виде объекта Color\n"
                            "   • shape: закрашиваемая форма - объект Shape. \n"
                            "По умолчанию это прямоугольная форма\n"
                            "Вторя версия:",
                            size=20
                        ),
                        create_set_color_code_second(),
                        ft.Text(
                            "   • brush: применяемая для покрытия цветом кисть "
                            "в виде объекта Brush\n"
                            "   • shape: закрашиваемая форма - объект Shape. По умолчанию "
                            "это    прямоугольная форма\n"
                            "   • alpha: значение прозрачности. Оно должно находится в диапазоне "
                            "от 0 (полностью прозрачно) до 1 (отсутствие прозрачности)\n"
                            "В данном случае разберем только установку цвета.",
                            size=20
                        ),
                        ft.Text(
                            "Установка размеров",
                            size=28,
                            weight=ft.FontWeight.W_600
                        ),
                        ft.Text(
                            "Для установки размеров компонентов в Jetpack Compose определен целый "
                            "ряд модификаторов: \n   • Modifier.height(): устанавливает высоту\n"
                            "   • Modifier.width(): устанавливает ширину\n"
                            "   • Modifier.fillMaxHeight(): растягивает компонент по всей длине контейнера\n"
                            "   • Modifier.heightIn(): устанавливает минимальную и максимальную высоту\n"
                            "   • Modifier.widthIn(): устанавливает минимальную и максимальную ширину\n"
                            "   • Modifier.size(): устанавливает размер\n"
                            "   • Modifier.sizeIn(): устанавливает минимальный и максимальный размер\n"
                            "Для установки применяются единицы dp (device-independent pixels/density-independent "
                            "pixels или независимые от устройства/плотности пиксели).\n"
                            "Например, установим для компонента Text высоту и ширину:",
                            size=20
                        ),
                        create_set_sizes_code(),
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
