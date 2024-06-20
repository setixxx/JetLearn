import flet as ft
from main_view_sources.components.theme.accent_color_button import \
    AccentColorButton
from main_view_sources.components.theme.theme_button import ThemeButton


# Класс для представления контейнера с кнопками выбора цвета и темы
class AccentColorAndTheme(ft.Container):
    # Инициализация контейнера
    def __init__(self):
        super().__init__()
        # Установка отступов снизу
        self.padding = ft.padding.only(bottom=42)
        # Установка ширины контейнера
        self.width = 100
        # Установка высоты контейнера
        self.height = 370
        # Создание столбца с кнопками
        self.content = ft.Column(
            [
                # Кнопка выбора цвета
                AccentColorButton(),
                # Кнопка выбора темы
                ThemeButton(),
            ],
            # Выравнивание по правому краю
            alignment=ft.MainAxisAlignment.END,
            # Выравнивание по горизонтали по центру
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )