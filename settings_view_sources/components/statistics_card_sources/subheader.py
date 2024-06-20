import flet as ft

# Класс для представления виджета подзаголовка
class Subheader(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка отступов слева
        self.padding = ft.padding.only(left=22)
        # Установка ширины виджета
        self.width = 344
        # Установка высоты виджета
        self.height = 56
        # Создание строки с текстом подзаголовка
        self.content = ft.Row(
            [
                # Виджет текста подзаголовка
                ft.Text(
                    # Текст подзаголовка
                    "Детальная информация о пройденных\n"
                    "вами, а также остальными,\n"
                    "пользователями тестах",
                    # Размер текста
                    size=14,
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
            vertical_alignment=ft.CrossAxisAlignment.END
        )