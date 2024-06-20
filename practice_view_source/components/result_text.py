import flet as ft

# Класс для представления виджета текста результата
class ResultText(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка ширины виджета
        self.width = 1104
        # Установка высоты виджета
        self.height = 88
        # Выравнивание по центру
        self.alignment = ft.alignment.top_center
        # Создание виджета текста результата
        self.result_text = ft.Text(
            "",
            # Размер текста
            size=20,
            # Вес шрифта
            weight=ft.FontWeight.W_400
        )
        # Установка виджета текста в качестве содержимого контейнера
        self.content = self.result_text

    # Метод установки текста результата
    def set_result_text(self, result):
        # Изменение текста результата
        self.result_text.value = result
        # Обновление виджета текста
        self.result_text.update()