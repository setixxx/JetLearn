import flet as ft

# Класс для представления контейнера с кнопками "Проверить ответ" и "Следующее задание"
class PracticeButtons(ft.Container):
    # Инициализация контейнера
    def __init__(self, page, result_text, check_answer_callback, next_task_callback):
        super().__init__()
        # Сохранение ссылки на виджет результата
        self.result_text = result_text
        # Сохранение ссылки на страницу
        self.page = page
        # Установка ширины контейнера
        self.width = 1104
        # Установка высоты контейнера
        self.height = 86
        # Выравнивание по центру
        self.alignment = ft.alignment.top_center
        # Создание строки с кнопками
        self.content = ft.Row(
            [
                # Кнопка "Проверить ответ"
                ft.OutlinedButton(
                    # Текст кнопки
                    "Проверить ответ",
                    # Обработчик события клика
                    on_click=check_answer_callback
                ),
                # Кнопка "Следующее задание"
                ft.FilledButton(
                    # Текст кнопки
                    "Следующее задание",
                    # Обработчик события клика
                    on_click=next_task_callback
                )
            ],
            # Выравнивание по горизонтали
            alignment=ft.MainAxisAlignment.CENTER,
            # Выравнивание по вертикали
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            # Междуэлементный интервал
            spacing=8
        )