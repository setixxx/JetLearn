import flet as ft


# Класс для представления изображения профиля
class ProfileImageMain(ft.Container):
    # Инициализация изображения профиля
    def __init__(self):
        super().__init__()
        # Установка фонового цвета изображения
        self.bgcolor = ft.colors.PRIMARY
        # Установка ширины изображения
        self.width = 40
        # Установка высоты изображения
        self.height = 40
        # Установка радиуса скругления изображения
        self.border_radius = 40