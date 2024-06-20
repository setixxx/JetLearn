import flet as ft


# Класс заголовка "Персональные данные"
class AccountHeader(ft.Row):
    # Инициализация заголовка
    def __init__(self):
        super().__init__()
        # Выравнивание по центру
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        # Установка ширины и высоты
        self.width = 1500
        self.height = 44
        # Создание текста заголовка
        self.controls = [
            ft.Text(
                "Персональные данные",
                # Установка размера и веса шрифта
                size=32,
                weight=ft.FontWeight.W_700
            )
        ]