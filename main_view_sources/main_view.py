# Импортируем библиотеку flet
import flet as ft

# Импортируем компоненты из подкаталогов
from main_view_sources.components.navigation_rail import NavigationRail
from main_view_sources.components.accent_color_and_theme import \
    AccentColorAndTheme
from main_view_sources.components.settings_button import SettingsButton
from main_view_sources.components.logo import Logo
from main_view_sources.components.theory_cards import TheoryCards
from main_view_sources.components.test_cards import TestCards
from main_view_sources.components.practice_card import PracticeCards


# Класс основного представления
class MainView(ft.View):
    # Инициализация основного представления
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        self.app_state = app_state
        self.page = page
        self.padding = 0
        self.route = "/main"
        # Инициализация компонентов
        self.navigation_rail = NavigationRail(self.change_view)
        self.theory_cards = TheoryCards(self.page)
        self.test_cards = TestCards(self.page)
        self.practice_card = PracticeCards(self.page)
        self.current_view = "Теория"
        # Обновление представления
        self.update_view()

    # Метод обновления представления
    def update_view(self):
        # Выбор карточек в зависимости от текущего представления
        match self.current_view:
            case "Теория":
                cards = self.theory_cards
            case "Тесты":
                cards = self.test_cards
            case "Практика":
                cards = self.practice_card
            case _:
                cards = ft.Container()

        # Очистка и добавление элементов в представление
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
                                SettingsButton(self.page, self.app_state),
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
        # Обновление страницы
        self.page.update()

    # Метод обработки изменения представления
    def change_view(self, e):
        # Получение индекса выбранного элемента
        selected_index = e.control.selected_index
        # Обновление текущего представления в зависимости от индекса
        if selected_index == 0:
            self.current_view = "Теория"
        elif selected_index == 1:
            self.current_view = "Тесты"
        elif selected_index == 2:
            self.current_view = "Практика"

        # Обновление представления
        self.update_view()