import flet as ft

# Класс для представления виджета поля ввода кода
class CodeField(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка ширины виджета
        self.width = 1104
        # Установка высоты виджета
        self.height = 120
        # Выравнивание по центру
        self.alignment = ft.alignment.top_center
        # Установка отступов сверху
        self.padding = ft.padding.only(top=16)
        # Создание виджета поля ввода текста
        self.content = ft.TextField(
            # Подпись поля
            label="Ваш код",
            # Ширина поля
            width=700,
            # Разрешение многострочного ввода
            multiline=True,
            # Максимальное количество строк
            max_lines=2
        )