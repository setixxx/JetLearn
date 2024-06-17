import flet as ft
from sign_up_view_sources.sign_up_view import SignUpView
from sign_in_view_sources.sign_in_view import SignInView
from main_view_sources.main_view import MainView
from start_view_sources.start_view import StartView
from theory_view_sources.first_theory_screen_source.first_theory_view \
    import FirstTheoryView

from settings_view_sources.settings_view import SettingsView
from statistics_view_sources.statistics_view import \
    StatisticsView
from tests_view_sources.first_test_screen_source.first_test_screen import \
    FirstTestView
from practice_screens_sources.practice_screen_source.practice_screen import \
    PracticeScreen
from account_view_sources.account_view import AccountView
from database_sources.database import DatabaseManager
from app_state import AppState


def main(page: ft.Page):
    page.title = "JetLearn"
    page.window_width = 1516
    page.window_height = 839
    page.window_center()
    page.window_maximizable = False
    page.window_resizable = False
    page.theme_mode = 'light'
    page.theme = ft.Theme(
        color_scheme_seed="blue",
    )

    app_state = AppState()

    def route_change(route):
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(StartView(page))
            case "/sign_in":
                page.views.append(SignInView(page, app_state))
            case "/sign_up":
                page.views.append(SignUpView(page, app_state))
            case "/main":
                page.views.append(MainView(page))
            case "/main/settings":
                page.views.append(SettingsView(page, app_state))
            case "/main/settings/account":
                page.views.append(AccountView(page))
            case "/main/settings/statistics":
                page.views.append(StatisticsView(page))
            case "/main/theory":
                page.views.append(FirstTheoryView(page))
            case "/main/test_1":
                page.views.append(FirstTestView(page))
            case "/main/practice":
                practice_screen = PracticeScreen(page)
                page.views.append(practice_screen.create_practice_screen())
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    database = DatabaseManager("users.sqlite")
    database.create_table()

ft.app(target=main, assets_dir='assets')
