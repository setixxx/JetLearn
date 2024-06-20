import flet as ft


# Класс для представления виджета кнопки "Перейти"
class ButtonGoToStatistics(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Выравнивание по правому нижнему краю
        self.alignment = ft.alignment.bottom_right
        # Установка отступов снизу и справа
        self.padding = ft.padding.only(bottom=22, right=22)
        # Установка ширины виджета
        self.width = 344
        # Установка высоты виджета
        self.height = 84
        # Создание виджета кнопки
        self.content = ft.FilledButton(
            # Текст кнопки
            "Перейти",
            # Обработчик события клика
            on_click=lambda e: self.page.go("/main/settings/statistics")
        )