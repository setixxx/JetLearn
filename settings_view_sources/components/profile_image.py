import flet as ft


# Класс для представления изображения профиля
class ProfileImage(ft.Row):
    # Инициализация изображения
    def __init__(self):
        super().__init__()
        # Выравнивание по центру
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        # Установка ширины изображения
        self.width = 1500
        # Установка высоты изображения
        self.height = 100
        # Создание виджета контейнера для изображения
        self.controls = [
            ft.Container(
                # Установка фонового цвета изображения
                bgcolor=ft.colors.PRIMARY,
                # Установка ширины изображения
                width=100,
                # Установка высоты изображения
                height=100,
                # Установка радиуса скругления изображения
                border_radius=100
            )
        ]