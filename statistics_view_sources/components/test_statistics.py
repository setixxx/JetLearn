import flet as ft
from database import DatabaseManager


# Класс для представления виджета статистики по тестам
class TestStatistics(ft.Card):
    # Инициализация виджета
    def __init__(self, app_state):
        super().__init__()
        # Создание объекта базы данных
        self.database = DatabaseManager("users.sqlite")
        # Сохранение состояния приложения
        self.app_state = app_state
        # Получение результатов и оценок по тестам из базы данных
        self.results, self.grades = self.database.get_test_results_and_grades(
            self.app_state.get_login())

        # Создание столбца с элементами статистики
        self.content = ft.Column(
            [
                # Контейнер для заголовка "Тесты"
                ft.Container(
                    # Виджет текста заголовка
                    ft.Text(
                        # Текст заголовка
                        "Тесты",
                        # Размер текста
                        size=20,
                        # Вес шрифта
                        weight=ft.FontWeight.W_500
                    ),
                    # Ширина контейнера
                    width=300,
                    # Высота контейнера
                    height=36,
                    # Отступы слева
                    padding=ft.padding.only(left=32),
                    # Выравнивание по левому нижнему краю
                    alignment=ft.alignment.bottom_left
                ),
                # Контейнер для таблицы результатов
                ft.Container(
                    # Создание строки с колонками
                    ft.Row(
                        [
                            # Колонка с номерами тестов
                            ft.Text(
                                # Формирование текста с номерами тестов
                                "Тест:\n" + "\n".join(
                                    [f"{i + 1}:" for i in range(8)]),
                                # Размер текста
                                size=16,
                                # Вес шрифта
                                weight=ft.FontWeight.W_400,
                                # Выравнивание текста
                                text_align=ft.TextAlign.LEFT
                            ),
                            # Колонка с результатами тестов
                            ft.Text(
                                # Формирование текста с результатами тестов
                                "Результат:\n" + "\n".join(
                                    [f"{result}/5" for result in
                                     self.results]),
                                # Размер текста
                                size=16,
                                # Вес шрифта
                                weight=ft.FontWeight.W_400,
                                # Выравнивание текста
                                text_align=ft.TextAlign.LEFT
                            ),
                            # Колонка с оценками по тестам
                            ft.Text(
                                # Формирование текста с оценками по тестам
                                "Оценка:\n" + "\n".join(
                                    [str(grade) for grade in self.grades]),
                                # Размер текста
                                size=16,
                                # Вес шрифта
                                weight=ft.FontWeight.W_400,
                                # Выравнивание текста
                                text_align=ft.TextAlign.LEFT
                            )
                        ],
                        # Междуэлементный интервал
                        spacing=32
                    ),
                    # Ширина контейнера
                    width=300,
                    # Высота контейнера
                    height=248,
                    # Отступы
                    padding=ft.padding.only(left=32, top=16, bottom=16,
                                            right=32),
                    # Выравнивание по центру
                    alignment=ft.alignment.top_center
                )
            ],
            # Ширина карточки
            width=300,
            # Высота карточки
            height=290,
            # Междурядный интервал
            spacing=0
        )