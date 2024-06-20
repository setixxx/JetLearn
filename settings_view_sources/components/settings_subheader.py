import flet as ft

# Класс для представления подзаголовка "Настройки"
class SettingsSubheader(ft.Row):
    # Инициализация подзаголовка
    def __init__(self):
        super().__init__()
        # Выравнивание по центру
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        # Установка ширины подзаголовка
        self.width = 1500
        # Установка высоты подзаголовка
        self.height = 44
        # Создание текста подзаголовка
        self.controls = [
            ft.Text(
                # Текст подзаголовка
                "Здесь вы можете настроить данные своего аккаунта или ознакомиться с вашей\n"
                "персональной статистикой",
                # Выравнивание текста по центру
                text_align=ft.TextAlign.CENTER,
                # Размер текста
                size=14,
                # Вес шрифта
                weight=ft.FontWeight.W_500
            )
        ]