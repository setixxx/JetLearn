import flet as ft
import random

# Класс TestText представляет контейнер для одного вопроса теста с вариантами ответов
class TestText(ft.Container):
    def __init__(self, question, options, correct_answer):
        super().__init__()
        # Задаем стили контейнера
        self.padding = 16
        self.bgcolor = ft.colors.SECONDARY_CONTAINER
        self.border_radius = 20
        self.correct_answer = correct_answer

        # Получаем случайные варианты ответов, включая правильный
        self.selected_options = self.get_random_options(options, correct_answer)
        # Перемешиваем варианты ответов
        random.shuffle(self.selected_options)

        # Заголовок вопроса
        self.exercise_header = ft.Text(
            question,
            size=20,
            weight=ft.FontWeight.W_600,
            max_lines=2
        )

        # Группа радиокнопок для выбора ответа
        self.exercise_text = ft.RadioGroup(
            content=ft.Column(
                # Создаем радиокнопки для каждого варианта
                [
                    ft.Radio(value=opt, label=opt)
                    for opt in self.selected_options
                ]
            )
        )

        # Устанавливаем содержимое контейнера
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        self.exercise_header,
                        self.exercise_text
                    ]
                )
            ]
        )

    # Возвращает случайные варианты ответов, включая правильный
    def get_random_options(self, options, correct_answer):
        # Исключаем правильный ответ из списка
        other_options = [opt for opt in options if opt != correct_answer]
        # Случайно выбираем три неправильных ответа
        selected_options = random.sample(other_options, 3)
        # Добавляем правильный ответ
        selected_options.append(correct_answer)
        return selected_options

    # Проверяет, является ли выбранный ответ правильным
    def check_answer(self):
        # Получаем выбранное значение
        selected_value = self.exercise_text.value
        # Сравниваем выбранное значение с правильным ответом
        return selected_value == self.correct_answer