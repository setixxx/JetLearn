import flet as ft

# Класс для представления виджета заголовка "Статистика"
class Header(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка отступов слева и снизу
        self.padding = ft.padding.only(left=21, bottom=3)
        # Установка ширины виджета
        self.width = 344
        # Установка высоты виджета
        self.height = 45
        # Создание строки с текстом заголовка
        self.content = ft.Row(
            [
                # Виджет текста заголовка
                ft.Text(
                    # Текст заголовка
                    "Статистика",
                    # Размер текста
                    size=20,
                    # Вес шрифта
                    weight=ft.FontWeight.W_500
                )
            ],
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.START,
            # Выравнивание по вертикали
            vertical_alignment=ft.CrossAxisAlignment.END
        )