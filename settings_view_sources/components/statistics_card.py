import flet as ft
from settings_view_sources.components.statistics_card_sources.header import Header
from settings_view_sources.components.statistics_card_sources.subheader import Subheader
from settings_view_sources.components.statistics_card_sources.theory_progress import TheoryProgress
from settings_view_sources.components.statistics_card_sources.test_progress import TestProgress
from settings_view_sources.components.statistics_card_sources.button_go_to_statistics import ButtonGoToStatistics


class StatisticsCard(ft.Card):
    def __init__(self, app_state):
        super().__init__()
        self.content = ft.Column(
            [
                Header(),
                Subheader(),
                TheoryProgress(app_state),
                TestProgress(),
                ButtonGoToStatistics(),
            ],
            spacing=0,
            width=344,
            height=346,
        )
