import flet as ft
import json
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from tests_view_sources.results import Results
from tests_view_sources.test_text import TestText

# Класс FirstTest представляет контейнер для первого теста
class FirstTest(ft.Container):
    def __init__(self, page, questions, restart_test, db_manager, app_state):
        super().__init__()
        # Сохраняем ссылки на необходимые объекты
        self.page = page
        self.questions = questions
        self.restart_test = restart_test
        self.db_manager = db_manager
        self.app_state = app_state
        # Задаем стили контейнера
        self.margin = ft.padding.only(right=39, bottom=32)
        self.alignment = ft.alignment.bottom_left
        self.width = 812
        self.height = 1630
        self.test_texts = []

        # Создаем содержимое контейнера
        self.content = ft.Container(
            ft.Container(
                ft.Column(
                    [
                        # Верхняя часть контейнера с заголовком и инструкциями
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(
                                                "Тест по первому модулю",
                                                size=40,
                                                weight=ft.FontWeight.W_600
                                            ),
                                            ft.Text(
                                                'Заполните приведенные '
                                                'ниже поля и по завершении '
                                                'нажмите\nкнопку'
                                                ' "Закончить" для получения '
                                                'результата. Успехов!',
                                                size=16,
                                                weight=ft.FontWeight.W_600
                                            ),
                                        ]
                                    )
                                ]
                            ),
                        ),
                        # Создаем вопросы для теста
                        *self.create_test_texts(),
                        # Контейнер для отображения результатов теста
                        Results(self.page,
                                self.test_texts,
                                self.restart_test,
                                self.db_manager,
                                self.app_state,
                                "TESTS_1"),
                    ]
                ),
                padding=ft.padding.only(left=48, right=48),
            ),
            width=812
        )

    # Создает объекты TestText для каждого вопроса
    def create_test_texts(self):
        test_texts = []
        for question_data in self.questions:
            question = question_data["question"]
            options = question_data["options"]
            correct_answer = question_data["correct_answer"]
            # Создаем объект TestText для текущего вопроса
            test_text = TestText(question, options, correct_answer)
            test_texts.append(test_text)
        self.test_texts = test_texts
        return test_texts

# Класс FirstTestView представляет вид первого теста
class FirstTestView(ft.View):
    def __init__(self, page: ft.Page, db_manager, app_state):
        super().__init__()
        self.page = page
        # Менеджер базы данных и объект состояния приложения
        self.db_manager = db_manager
        self.app_state = app_state
        self.padding = 0
        # Маршрут для первого теста
        self.route = "/main/test_1"
        # Загрузка вопросов при инициализации
        self.load_questions()

    # Загружает вопросы из JSON-файла и создает интерфейс теста
    def load_questions(self):
        # Открытие файла с вопросами и загрузка данных
        with open("data/test.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            questions = data[0]["questions"]

        # Определение элементов интерфейса
        self.controls = [
            ft.Container(
                ft.Row(
                    [
                        # Левая колонка с кнопкой "Назад" и логотипом
                        ft.Column(
                            [
                                ArrowBackAndLogo(
                                    lambda e: self.page.go("/main")
                                )
                            ]
                        ),
                        # Правая колонка с тестом
                        ft.Container(
                            ft.Column(
                                [
                                    FirstTest(self.page,
                                              questions,
                                              self.restart_test,
                                              self.db_manager,
                                              self.app_state)
                                ],
                                scroll=ft.ScrollMode.AUTO
                            ),
                            margin=ft.padding.only(top=76)
                        )
                    ]
                ),
                width=1500,
                height=800,
            )
        ]

    # Перезагружает вопросы и обновляет страницу
    def restart_test(self):
        self.load_questions()
        self.page.update()