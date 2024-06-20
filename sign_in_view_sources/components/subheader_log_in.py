import flet as ft


# Класс для представления виджета подзаголовка "Вход"
class SubheaderLogIn(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка ширины виджета
        self.width = 461
        # Установка высоты виджета
        self.height = 208
        # Выравнивание по левому верхнему краю
        self.alignment = ft.alignment.top_left
        # Установка отступов слева и сверху
        self.padding = ft.padding.only(left=28, top=12)
        # Создание виджета текста подзаголовка
        self.content = ft.Text(
            # Текст подзаголовка
            value="Используйте аккаунт JetBrains",
            # Вес шрифта
            weight=ft.FontWeight.W_400,
            # Размер текста
            size=16,
        )