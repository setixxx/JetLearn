import flet as ft

# Класс для представления виджета кнопки "Перейти"
class ButtonGoToAccount(ft.Container):
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
        self.height = 149
        # Создание строки с кнопкой
        self.content = ft.Row(
            [
                # Кнопка "Перейти"
                ft.FilledButton(
                    # Текст кнопки
                    "Перейти",
                    # Обработчик события клика
                    on_click=lambda e: self.page.go("/main/settings/account")
                ),
            ],
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.END,
            # Выравнивание по вертикали
            vertical_alignment=ft.CrossAxisAlignment.END
        )