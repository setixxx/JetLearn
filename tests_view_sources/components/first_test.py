import flet as ft
from tests_view_sources.results import Results
from tests_view_sources.components.test_text import TestText

# Класс FirstTest представляет контейнер для первого теста
class FirstTest(ft.Container):
    def __init__(self, page, questions, restart_test, db_manager, app_state):
        super().__init__()
        # Страница, на которой отображается тест
        self.page = page
        # Вопросы для теста
        self.questions = questions
        # Функция для перезапуска теста
        self.restart_test = restart_test
        # Менеджер базы данных для выполнения операций с БД
        self.db_manager = db_manager
        # Объект состояния приложения для хранения текущего состояния
        self.app_state = app_state
        # Отступы контейнера
        self.margin = ft.padding.only(right=39, bottom=32)
        # Выравнивание контейнера
        self.alignment = ft.alignment.bottom_left
        self.width = 812  # Ширина контейнера
        self.height = 1630  # Высота контейнера
        self.test_texts = []  # Список объектов TestText

        # Создание содержимого контейнера
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
                        # Создание вопросов для теста
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

    # Метод create_test_texts создает объекты TestText для каждого вопроса
    def create_test_texts(self):
        test_texts = []
        for question_data in self.questions:
            question = question_data["question"]  # Текст вопроса
            options = question_data["options"]  # Варианты ответов
            correct_answer = question_data["correct_answer"] # Правильный ответ
            # Создание объекта TestText для текущего вопроса
            test_text = TestText(question, options, correct_answer)
            test_texts.append(test_text)  # Добавление объекта в список
        self.test_texts = test_texts  # Сохранение списка объектов TestText
        return test_texts  # Возврат списка объектов TestText
