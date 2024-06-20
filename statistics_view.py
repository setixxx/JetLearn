import flet as ft
from database import DatabaseManager
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from settings_view import ProfileImage

# Класс для представления виджета статистики по теории
class TheoryStatistics(ft.Card):
    def __init__(self, app_state):
        super().__init__()
        # Сохраняем ссылку на объект состояния приложения
        self.app_state = app_state

        # Создаем столбец с элементами статистики
        self.content = ft.Column(
            [
                # Заголовок "Теория"
                ft.Container(
                    ft.Text(
                        "Теория",
                        size=20,
                        weight=ft.FontWeight.W_500
                    ),
                    width=300,
                    height=45,
                    padding=ft.padding.only(left=32),
                    alignment=ft.alignment.bottom_left
                ),
                # Текст статистики по теории
                ft.Container(
                    ft.Text(
                        f"Пройдено теории:\n{self.app_state.get_formatted_theory_backslash()}",
                        size=16,
                        weight=ft.FontWeight.W_400
                    ),
                    width=300,
                    height=81,
                    padding=ft.padding.only(left=32, top=16, bottom=16),
                    alignment=ft.alignment.top_left
                )
            ],
            width=300,
            height=126,
            spacing=0
        )

# Класс для представления виджета статистики по тестам
class TestStatistics(ft.Card):
    def __init__(self, app_state):
        super().__init__()
        # Создаем объект базы данных
        self.database = DatabaseManager("users.sqlite")
        # Сохраняем ссылку на объект состояния приложения
        self.app_state = app_state
        # Получаем результаты и оценки по тестам из базы данных
        self.results, self.grades = self.database.get_test_results_and_grades(
            self.app_state.get_login())

        # Создаем столбец с элементами статистики
        self.content = ft.Column(
            [
                # Заголовок "Тесты"
                ft.Container(
                    ft.Text(
                        "Тесты",
                        size=20,
                        weight=ft.FontWeight.W_500
                    ),
                    width=300,
                    height=36,
                    padding=ft.padding.only(left=32),
                    alignment=ft.alignment.bottom_left
                ),
                # Таблица с результатами тестов
                ft.Container(
                    ft.Row(
                        [
                            # Номера тестов
                            ft.Text(
                                "Тест:\n" + "\n".join(
                                    [f"{i + 1}:" for i in range(8)]),
                                size=16,
                                weight=ft.FontWeight.W_400,
                                text_align=ft.TextAlign.LEFT
                            ),
                            # Результаты тестов
                            ft.Text(
                                "Результат:\n" + "\n".join(
                                    [f"{result}/5" for result in self.results]),
                                size=16,
                                weight=ft.FontWeight.W_400,
                                text_align=ft.TextAlign.LEFT
                            ),
                            # Оценки по тестам
                            ft.Text(
                                "Оценка:\n" + "\n".join(
                                    [str(grade) for grade in self.grades]),
                                size=16,
                                weight=ft.FontWeight.W_400,
                                text_align=ft.TextAlign.LEFT
                            )
                        ],
                        spacing=32
                    ),
                    width=300,
                    height=248,
                    padding=ft.padding.only(left=32, top=16, bottom=16, right=32),
                    alignment=ft.alignment.top_center
                )
            ],
            width=300,
            height=290,
            spacing=0
        )

class StatisticsHeader(ft.Row):
    def __init__(self):
        super().__init__()
        # Выравнивание по центру
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        # Установка ширины и высоты
        self.width = 1500
        self.height = 44
        # Создание текста заголовка
        self.controls = [
            ft.Text(
                "Статистика",
                size=32,
                weight=ft.FontWeight.W_700
            )
        ]

# Класс для представления виджета статистики по практике
class PracticeStatistics(ft.Card):
    def __init__(self, app_state):
        super().__init__()
        # Сохраняем ссылку на объект состояния приложения
        self.app_state = app_state

        # Создаем столбец с элементами статистики
        self.content = ft.Column(
            [
                # Заголовок "Тренажер"
                ft.Container(
                    ft.Text(
                        "Тренажер",
                        size=20,
                        weight=ft.FontWeight.W_500
                    ),
                    width=300,
                    height=45,
                    padding=ft.padding.only(left=32),
                    alignment=ft.alignment.bottom_left
                ),
                # Текст статистики по практике
                ft.Container(
                    ft.Text(
                        f"Правильно отвечено:\n{self.app_state.get_formatted_practice()}",
                        size=16,
                        weight=ft.FontWeight.W_400
                    ),
                    width=300,
                    height=81,
                    padding=ft.padding.only(left=32, top=16, bottom=16),
                    alignment=ft.alignment.top_left
                )
            ],
            width=300,
            height=126,
            spacing=0
        )


# Класс представления страницы "Статистика"
class StatisticsView(ft.View):
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохраняем ссылки на страницу и объект состояния приложения
        self.page = page
        self.app_state = app_state
        # Устанавливаем маршрут
        self.title = "/main/settings/statistics"
        self.padding = 0

        # Создаем элементы представления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Кнопка "Назад" и логотип
                        ArrowBackAndLogo(lambda e: self.page.go("/main/settings")),
                        # Изображение профиля
                        ProfileImage(),
                        # Заголовок "Статистика"
                        StatisticsHeader(),
                        # Карточки со статистикой
                        ft.Row(
                            [
                                # Статистика по теории и практике
                                ft.Column(
                                    [
                                        TheoryStatistics(app_state),
                                        PracticeStatistics(app_state)
                                    ],
                                    spacing=23
                                ),
                                # Статистика по тестам
                                TestStatistics(app_state)
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            width=1500,
                            height=284,
                        ),
                    ],
                ),
                width=1500,
                height=800
            )
        ]