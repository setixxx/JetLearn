import flet as ft

# Класс для представления виджета задачи
class Task(ft.Container):
    # Инициализация виджета с текстом задачи
    def __init__(self, task_text):
        super().__init__()
        # Установка ширины виджета
        self.width = 1104
        # Установка высоты виджета
        self.height = 106
        # Выравнивание по левому верхнему краю
        self.alignment = ft.alignment.top_left
        # Установка отступов слева
        self.padding = ft.padding.only(left=202)
        # Создание виджета текста задачи
        self.task_text = ft.Text(task_text, size=16, weight=ft.FontWeight.W_400)
        # Создание столбца с элементами задачи
        self.content = ft.Column(
            [
                # Контейнер для заголовка "Ваше задание:"
                ft.Container(
                    # Виджет заголовка
                    ft.ListTile(
                        # Текст заголовка
                        title=ft.Text(
                            "Ваше задание:",
                            # Размер текста
                            size=20,
                            # Вес шрифта
                            weight=ft.FontWeight.W_400,
                        ),
                    ),
                    # Ширина контейнера
                    width=360,
                    # Высота контейнера
                    height=56
                ),
                # Контейнер для текста задачи
                ft.Container(
                    # Виджет текста задачи
                    ft.ListTile(
                        # Текст задачи
                        title=self.task_text,
                        # Иконка задачи
                        leading=ft.Icon(ft.icons.TASK_ALT),
                    ),
                    # Ширина контейнера
                    width=580,
                    # Высота контейнера
                    height=50
                )
            ],
            # Междурядный интервал
            spacing=0
        )

    # Метод обновления текста задачи
    def update_task(self, new_task_text):
        # Изменение текста задачи
        self.task_text.value = new_task_text
        # Обновление виджета текста
        self.task_text.update()