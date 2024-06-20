import flet as ft
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from settings_view_sources.components.profile_image import ProfileImage
from statistics_view_sources.components.statistics_header \
    import StatisticsHeader
from statistics_view_sources.components.theory_statistics \
    import TheoryStatistics
from statistics_view_sources.components.practice_statistics import \
    PracticeStatistics
from statistics_view_sources.components.test_statistics import \
    TestStatistics


# Класс представления страницы "Статистика"
class StatisticsView(ft.View):
    # Инициализация представления
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохранение ссылки на страницу
        self.page = page
        # Установка маршрута
        self.title = "/main/settings/statistics"
        # Установка отступов
        self.padding = 0
        # Создание списка элементов управления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Кнопка "Назад" и логотип
                        ArrowBackAndLogo(
                            lambda e: self.page.go("/main/settings")
                        ),
                        # Изображение профиля
                        ProfileImage(),
                        # Заголовок "Статистика"
                        StatisticsHeader(),
                        # Строка с карточками статистики
                        ft.Row(
                            [
                                # Столбец для статистики по теории и практике
                                ft.Column(
                                    [
                                        # Виджет статистики по теории
                                        TheoryStatistics(app_state),
                                        # Виджет статистики по практике
                                        PracticeStatistics(app_state)
                                    ],
                                    # Междурядный интервал
                                    spacing=23
                                ),
                                # Виджет статистики по тестам
                                TestStatistics(app_state)
                            ],
                            # Междуэлементный интервал
                            spacing=20,
                            # Выравнивание по горизонтали
                            alignment=ft.MainAxisAlignment.CENTER,
                            # Выравнивание по вертикали
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            # Ширина строки
                            width=1500,
                            # Высота строки
                            height=284,
                        ),
                    ],
                ),
                # Ширина контейнера
                width=1500,
                # Высота контейнера
                height=800
            )
        ]