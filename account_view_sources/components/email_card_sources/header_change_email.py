import flet as ft


# Класс заголовка "Изменение адреса эл. почты"
class HeaderChangeEmail(ft.Container):
    # Инициализация заголовка
    def __init__(self):
        super().__init__()
        # Установка отступов
        self.padding = ft.padding.only(left=21, bottom=3)
        # Установка ширины и высоты
        self.width = 344
        self.height = 45
        # Создание строки с текстом заголовка
        self.content = ft.Row(
            [
                ft.Text(
                    "Изменение адреса эл. почты",
                    # Установка размера и веса шрифта
                    size=20,
                    weight=ft.FontWeight.W_500
                )
            ],
            # Выравнивание по левому краю
            alignment=ft.MainAxisAlignment.START,
            # Выравнивание по нижнему краю
            vertical_alignment=ft.CrossAxisAlignment.END
        )