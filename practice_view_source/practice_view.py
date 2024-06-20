import flet as ft
import random
import json
import re  # импортируем библиотеку регулярных выражений

from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from practice_view_source.components.header import Header
from practice_view_source.components.code_field import CodeField
from practice_view_source.components.practice_buttons import PracticeButtons
from practice_view_source.components.result_text import ResultText
from practice_view_source.components.task import Task
from database import DatabaseManager


# Класс представления страницы практики
class PracticeView(ft.View):
    # Инициализация представления
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохранение ссылки на страницу
        self.page = page
        # Установка маршрута
        self.route = "/main/practice"
        # Установка отступов
        self.padding = 0
        # Создание виджета для отображения результата
        self.result_text = ResultText()
        # Инициализация текущей задачи
        self.current_task = None
        # Сохранение состояния приложения
        self.app_state = app_state
        # Создание объекта базы данных
        self.database = DatabaseManager("users.sqlite")

        # Генерация начальной задачи
        self.current_task = self.generate_task()
        # Создание виджета для отображения текста задачи
        self.task_text = Task(self.current_task["task"])
        # Создание виджета для ввода ответа
        self.user_input = CodeField()

        # Создание списка элементов управления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Кнопка "Назад" и логотип
                        ArrowBackAndLogo(
                            lambda e: self.page.go("/main")
                        ),
                        # Контейнер для элементов задачи
                        ft.Container(
                            ft.Column(
                                [
                                    # Заголовок "Практика"
                                    Header(),
                                    # Виджет текста задачи
                                    self.task_text,
                                    # Виджет для ввода ответа
                                    self.user_input,
                                    # Виджет для отображения результата
                                    self.result_text,
                                    # Виджет с кнопками "Проверить" и "Следующая задача"
                                    PracticeButtons(page,
                                                    self.result_text,
                                                    self.check_answer,
                                                    self.next_task)
                                ],
                                spacing=0
                            ),
                            # Отступы вокруг контейнера
                            margin=ft.padding.only(top=62,
                                                   left=198,
                                                   right=198),
                            # Ширина контейнера
                            width=1104,
                            # Высота контейнера
                            height=500,
                            # Радиус скругления
                            border_radius=22,
                            # Фоновый цвет
                            bgcolor=ft.colors.SECONDARY_CONTAINER
                        )
                    ],
                    spacing=0
                ),
                # Ширина контейнера
                width=1500,
                # Высота контейнера
                height=800,
            )
        ]

    # Метод генерации случайной задачи из файла
    def generate_task(self):
        # Открытие файла с задачами
        with open("data/practice.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
        # Выбор случайной задачи
        new_task = random.choice(tasks)
        # Проверка на дублирование задачи
        while new_task == self.current_task:
            new_task = random.choice(tasks)
        # Возвращение выбранной задачи
        return new_task

    # Метод нормализации кода перед проверкой
    def normalize_code(self, code):
        # Удаление лишних пробелов вокруг скобок и других символов
        code = re.sub(r'\s*([\(\)\{\};,])\s*', r'\1', code)
        # Удаление лишних пробелов
        code = re.sub(r'\s+', ' ', code).strip()
        # Возвращение нормализованного кода
        return code

    # Метод проверки ответа пользователя
    def check_answer(self, e):
        # Получение нормализованного ответа пользователя
        user_answer = self.normalize_code(self.user_input.content.value)
        # Получение нормализованного ожидаемого ответа
        expected_answer = self.normalize_code(self.current_task["expected"])

        # Увеличение количества попыток
        self.database.increment_total_attempts(self.app_state.get_login())

        # Проверка правильности ответа
        if user_answer == expected_answer:
            # Установка текста результата на "Правильно!"
            self.result_text.set_result_text("Правильно!")
            # Увеличение количества правильных попыток
            self.database.increment_correct_attempts(self.app_state.get_login())
        else:
            # Установка текста результата на "Неправильно. Попробуйте снова."
            self.result_text.set_result_text("Неправильно. Попробуйте снова.")

        # Обновление статистики пользователя
        correct_attempts, total_attempts = self.database.get_practice_stats(self.app_state.get_login())
        self.app_state.set_completed_practice_count(correct_attempts)
        self.app_state.set_completed_practice_total(total_attempts)

        # Обновление страницы
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
        # Обновление страницы
        self.page.update()