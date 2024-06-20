import flet as ft
from settings_view_sources.components.statistics_card_sources.header import Header
from settings_view_sources.components.statistics_card_sources.subheader import Subheader
from settings_view_sources.components.statistics_card_sources.theory_progress import TheoryProgress
from settings_view_sources.components.statistics_card_sources.test_progress import TestProgress
from settings_view_sources.components.statistics_card_sources.button_go_to_statistics import ButtonGoToStatistics


# Класс карточки статистики
class StatisticsCard(ft.Card):
    # Инициализация карточки
    def __init__(self, app_state):
        super().__init__()
        # Создание столбца с элементами карточки
        self.content = ft.Column(
            [
                # Заголовок карточки
                Header(),
                # Подзаголовок карточки
                Subheader(),
                # Виджет отображения прогресса по теории
                TheoryProgress(app_state),
                # Виджет отображения прогресса по тестам
                TestProgress(app_state),
                # Кнопка перехода к полной статистике
                ButtonGoToStatistics(),
            ],
            # Междурядный интервал
            spacing=0,
            # Ширина карточки
            width=344,
            # Высота карточки
            height=346,
        )