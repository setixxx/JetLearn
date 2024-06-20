import flet as ft

# Класс для представления виджета заголовка "Тренажер"
class Header(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка ширины виджета
        self.width = 1104
        # Установка высоты виджета
        self.height = 100
        # Установка отступов сверху
        self.padding = ft.padding.only(top=27)
        # Выравнивание по центру
        self.alignment = ft.alignment.top_center
        # Создание виджета текста заголовка
        self.content = ft.Text(
            # Текст заголовка
            "Тренажер",
            # Размер текста
            size=40,
            # Вес шрифта
            weight=ft.FontWeight.W_500
        )