import flet as ft
import random

# Класс TestText представляет контейнер для одного вопроса теста с
# вариантами ответов
class TestText(ft.Container):
    def __init__(self, question, options, correct_answer):
        super().__init__()
        self.padding = 16  # Внутренние отступы контейнера
        self.bgcolor = ft.colors.SECONDARY_CONTAINER  # Фоновый цвет контейнера
        self.border_radius = 20  # Радиус границ контейнера
        self.correct_answer = correct_answer  # Правильный ответ на вопрос

        # Получение случайных вариантов ответов, включая правильный
        self.selected_options = self.get_random_options(options,
                                                        correct_answer)
        # Перемешивание вариантов ответов
        random.shuffle(self.selected_options)

        # Заголовок вопроса
        self.exercise_header = ft.Text(
            question,
            size=20,
            weight=ft.FontWeight.W_600,  # Полужирный текст
            max_lines=2  # Максимальное количество строк для заголовка
        )

        # Группа радиокнопок для выбора ответа
        self.exercise_text = ft.RadioGroup(
            content=ft.Column(
                [
                    # Создание радиокнопок для каждого варианта
                    ft.Radio(value=opt, label=opt)
                    for opt in self.selected_options
                ]
            )
        )

        # Установка содержимого контейнера
        self.content = ft.Row(
            [
                ft.Column(
                    [
                        self.exercise_header,  # Добавление заголовка вопроса
                        self.exercise_text  # Добавление группы радиокнопок
                    ]
                )
            ]
        )

    # Метод get_random_options возвращает случайные варианты ответов,
    # включая правильный
    def get_random_options(self, options, correct_answer):
        # Исключение правильного ответа из списка
        other_options = [opt for opt in options if opt != correct_answer]
        # Случайный выбор трех неправильных ответов
        selected_options = random.sample(other_options, 3)
        # Добавление правильного ответа
        selected_options.append(correct_answer)
        return selected_options

    # Метод check_answer проверяет, является ли выбранный ответ правильным
    def check_answer(self):
        # Получение выбранного значения
        selected_value = self.exercise_text.value
        # Сравнение выбранного значения с правильным ответом
        return selected_value == self.correct_answer
