import flet as ft

# Класс для представления виджета заголовка "Персональные данные"
class Header(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка отступов слева и сверху
        self.padding = ft.padding.only(left=21, top=16)
        # Установка ширины виджета
        self.width = 344
        # Установка высоты виджета
        self.height = 73
        # Создание строки с текстом заголовка
        self.content = ft.Row(
            [
                # Виджет текста заголовка
                ft.Text(
                    # Текст заголовка
                    "Персональные\nданные",
                    # Размер текста
                    size=20,
                    # Вес шрифта
                    weight=ft.FontWeight.W_500,
                    # Стиль текста
                    style=ft.TextStyle(
                        height=1.2
                    )
                )
            ],
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.START,
            # Выравнивание по вертикали
            vertical_alignment=ft.CrossAxisAlignment.START
        )