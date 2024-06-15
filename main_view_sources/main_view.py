import flet as ft

from main_view_sources.components.navigation_rail import NavigationRail
from main_view_sources.components.accent_color_and_theme import \
    AccentColorAndTheme
from main_view_sources.components.settings_button import SettingsButton
from main_view_sources.components.logo import Logo
from main_view_sources.components.theory_cards import TheoryCards
from main_view_sources.components.test_cards import TestCards
from main_view_sources.components.practice_card import PracticeCards


class MainView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = 0
        self.route = "/main"
        self.navigation_rail = NavigationRail(self.change_view)
        self.theory_cards = TheoryCards(self.page)
        self.test_cards = TestCards(self.page)
        self.practice_card = PracticeCards(self.page)
        self.current_view = "Теория"
        self.update_view()

    def update_view(self):
        match self.current_view:
            case "Теория":
                cards = self.theory_cards
            case "Тесты":
                cards = self.test_cards
            case "Практика":
                cards = self.practice_card
            case _:
                cards = ft.Container()

        self.controls.clear()
        self.controls.append(
            ft.Container(
                ft.Row(
                    [
                        ft.Column(
                            [
                                Logo(),
                                self.navigation_rail,
                                AccentColorAndTheme()
                            ],
                            spacing=0
                        ),
                        ft.Column(
                            [
                                SettingsButton(self.page),
                                cards
                            ],
                            spacing=0
                        )
                    ],
                    spacing=0
                ),
                width=1500,
                height=800,
            )
        )
        self.page.update()

    def change_view(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            self.current_view = "Теория"
        elif selected_index == 1:
            self.current_view = "Тесты"
        elif selected_index == 2:
            self.current_view = "Практика"

        self.update_view()
