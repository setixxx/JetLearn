import flet as ft


# Класс для представления логотипа
class Logo(ft.Container):
    # Инициализация логотипа
    def __init__(self):
        super().__init__()
        # Установка ширины логотипа
        self.width = 200
        # Установка высоты логотипа
        self.height = 60
        # Выравнивание по левому краю
        self.alignment = ft.alignment.center_left
        # Установка отступов слева
        self.padding = ft.padding.only(left=24)
        # Создание виджета текста для логотипа
        self.content = ft.Text(
            # Текст логотипа
            "JetLearn",
            # Размер текста
            size=32,
            # Вес шрифта
            weight=ft.FontWeight.W_500
        )