import flet as ft
import random
import json
import re

from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from database import DatabaseManager

# Класс для представления виджета задачи
class Task(ft.Container):
    def __init__(self, task_text):
        super().__init__()
        # Устанавливаем стили контейнера
        self.width = 1104
        self.height = 106
        self.alignment = ft.alignment.top_left
        self.padding = ft.padding.only(left=202)
        # Создаем текст задачи
        self.task_text = ft.Text(task_text, size=16, weight=ft.FontWeight.W_400)
        # Создаем столбец с элементами задачи
        self.content = ft.Column(
            [
                # Заголовок "Ваше задание:"
                ft.Container(
                    ft.ListTile(
                        title=ft.Text(
                            "Ваше задание:",
                            size=20,
                            weight=ft.FontWeight.W_400,
                        ),
                    ),
                    width=360,
                    height=56
                ),
                # Текст задачи
                ft.Container(
                    ft.ListTile(
                        title=self.task_text,
                        leading=ft.Icon(ft.icons.TASK_ALT),
                    ),
                    width=580,
                    height=50
                )
            ],
            spacing=0
        )

    # Метод обновления текста задачи
    def update_task(self, new_task_text):
        # Изменяем текст задачи
        self.task_text.value = new_task_text
        # Обновляем виджет текста
        self.task_text.update()

# Класс для представления виджета текста результата
class ResultText(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.width = 1104
        self.height = 88
        self.alignment = ft.alignment.top_center
        # Создаем текст результата
        self.result_text = ft.Text("", size=20, weight=ft.FontWeight.W_400)
        # Устанавливаем текст результата как содержимое контейнера
        self.content = self.result_text

    # Метод установки текста результата
    def set_result_text(self, result):
        # Изменяем текст результата
        self.result_text.value = result
        # Обновляем виджет текста
        self.result_text.update()

# Класс для представления контейнера с кнопками "Проверить ответ" и "Следующее задание"
class PracticeButtons(ft.Container):
    def __init__(self, page, result_text, check_answer_callback, next_task_callback):
        super().__init__()
        # Сохраняем ссылки на виджет результата, страницу и методы проверки ответа и генерации следующей задачи
        self.result_text = result_text
        self.page = page
        # Устанавливаем стили контейнера
        self.width = 1104
        self.height = 86
        self.alignment = ft.alignment.top_center
        # Создаем строку с кнопками
        self.content = ft.Row(
            [
                # Кнопка "Проверить ответ"
                ft.OutlinedButton(
                    "Проверить ответ",
                    on_click=check_answer_callback
                ),
                # Кнопка "Следующее задание"
                ft.FilledButton(
                    "Следующее задание",
                    on_click=next_task_callback
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8
        )

# Класс для представления виджета заголовка "Тренажер"
class Header(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.width = 1104
        self.height = 100
        self.padding = ft.padding.only(top=27)
        self.alignment = ft.alignment.top_center
        # Создаем текст заголовка
        self.content = ft.Text(
            "Тренажер",
            size=40,
            weight=ft.FontWeight.W_500
        )

# Класс для представления виджета поля ввода кода
class CodeField(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.width = 1104
        self.height = 120
        self.alignment = ft.alignment.top_center
        self.padding = ft.padding.only(top=16)
        # Создаем поле ввода текста
        self.content = ft.TextField(
            label="Ваш код",
            width=700,
            multiline=True,
            max_lines=2
        )

# Класс представления страницы практики
class PracticeView(ft.View):
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохраняем ссылки на страницу и объект состояния приложения
        self.page = page
        self.app_state = app_state
        # Устанавливаем маршрут
        self.route = "/main/practice"
        self.padding = 0
        # Создаем виджеты для результата, задачи, ввода ответа и базы данных
        self.result_text = ResultText()
        self.current_task = None
        self.database = DatabaseManager("users.sqlite")

        # Генерация начальной задачи
        self.current_task = self.generate_task()
        # Создаем виджеты для текста задачи и ввода ответа
        self.task_text = Task(self.current_task["task"])
        self.user_input = CodeField()

        # Создаем элементы представления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Кнопка "Назад" и логотип
                        ArrowBackAndLogo(lambda e: self.page.go("/main")),
                        # Контейнер для элементов задачи
                        ft.Container(
                            ft.Column(
                                [
                                    Header(),
                                    self.task_text,
                                    self.user_input,
                                    self.result_text,
                                    PracticeButtons(page,
                                                    self.result_text,
                                                    self.check_answer,
                                                    self.next_task)
                                ],
                                spacing=0
                            ),
                            margin=ft.padding.only(top=62, left=198, right=198),
                            width=1104,
                            height=500,
                            border_radius=22,
                            bgcolor=ft.colors.SECONDARY_CONTAINER
                        )
                    ],
                    spacing=0
                ),
                width=1500,
                height=800,
            )
        ]

    # Метод генерации случайной задачи из файла
    def generate_task(self):
        # Открываем файл с задачами
        with open("data/practice.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
        # Выбираем случайную задачу
        new_task = random.choice(tasks)
        # Проверяем на дублирование задачи
        while new_task == self.current_task:
            new_task = random.choice(tasks)
        # Возвращаем выбранную задачу
        return new_task

    # Метод нормализации кода перед проверкой
    def normalize_code(self, code):
        # Удаляем лишние пробелы вокруг скобок и других символов
        code = re.sub(r'\s*([\(\)\{\};,])\s*', r'\1', code)
        # Удаляем лишние пробелы
        code = re.sub(r'\s+', ' ', code).strip()
        # Возвращаем нормализованный код
        return code

    # Метод проверки ответа пользователя
    def check_answer(self, e):
        # Получаем нормализованный ответ пользователя и ожидаемый ответ
        user_answer = self.normalize_code(self.user_input.content.value)
        expected_answer = self.normalize_code(self.current_task["expected"])

        # Увеличиваем количество попыток
        self.database.increment_total_attempts(self.app_state.get_login())

        # Проверяем правильность ответа
        if user_answer == expected_answer:
            # Устанавливаем текст результата на "Правильно!"
            self.result_text.set_result_text("Правильно!")
            # Увеличиваем количество правильных попыток
            self.database.increment_correct_attempts(self.app_state.get_login())
        else:
            # Устанавливаем текст результата на "Неправильно. Попробуйте снова."
            self.result_text.set_result_text("Неправильно. Попробуйте снова.")

        # Обновляем статистику пользователя
        correct_attempts, total_attempts = self.database.get_practice_stats(self.app_state.get_login())
        self.app_state.set_completed_practice_count(correct_attempts)
        self.app_state.set_completed_practice_total(total_attempts)

        # Обновляем страницу
        self.page.update()

    # Метод перехода к следующей задаче
    def next_task(self, e):
        # Генерация новой задачи
        self.current_task = self.generate_task()
        # Обновление текста задачи
        self.task_text.update_task(self.current_task["task"])
        # Очистка поля ввода ответа
        self.user_input.content.value = ""
        # Очистка текста результата
        self.result_text.set_result_text("")
        # Обновляем страницу
        self.page.update()