import flet as ft


# Класс для представления заголовка "Настройки"
class SettingsHeader(ft.Row):
    # Инициализация заголовка
    def __init__(self, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Выравнивание по центру
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        # Установка ширины заголовка
        self.width = 1500
        # Установка высоты заголовка
        self.height = 44
        # Создание текста заголовка
        self.controls = [
            ft.Text(
                # Формирование текста заголовка с использованием логина пользователя
                f"Добро пожаловать, {self.app_state.get_login()}!",
                # Размер текста
                size=32,
                # Вес шрифта
                weight=ft.FontWeight.W_700
            )
        ]