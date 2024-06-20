import flet as ft


# Класс для представления виджета кнопки "Начать обучение"
class ButtonStart(ft.Container):
    # Инициализация виджета
    def __init__(self):
        super().__init__()
        # Установка отступов сверху
        self.padding = ft.padding.only(top=21)
        # Установка ширины виджета
        self.width = 1198
        # Установка высоты виджета
        self.height = 212
        # Создание строки с кнопкой
        self.content = ft.Row(
            [
                # Кнопка "Начать обучение"
                ft.FilledButton(
                    # Текст кнопки
                    text="Начать обучение",
                    # Иконка кнопки
                    icon="TOKEN_OUTLINED",
                    # Ширина кнопки
                    width=238,
                    # Высота кнопки
                    height=63,
                    # Обработчик события клика
                    on_click=lambda e: self.page.go("/sign_in")
                )
            ],
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.CENTER,
            # Выравнивание по вертикали
            vertical_alignment=ft.CrossAxisAlignment.START
        )