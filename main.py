import flet as ft
from sign_up_view_sources.sign_up_view import SignUpView
from sign_in_view_sources.sign_in_view import SignInView
from main_view_sources.main_view import MainView
from start_view_sources.start_view import StartView
from theory_screens_sources.first_theory_screen_source.first_theory_view import \
    FirstTheoryView
from settings_view_sources.settings_view import SettingsView
from settings_view_sources.statistics_screen.statistics_screen import \
    StatisticsScreen
from tests_screens_sources.first_test_screen_source.first_test_screen import \
    FirstTestScreen
from practice_screens_sources.practice_screen_source.practice_screen import \
    PracticeScreen


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

    def route_change(route):
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(StartView(page))
            case "/sign_in":
                page.views.append(SignInView(page))
            case "/sign_up":
                page.views.append(SignUpView(page))
            case "/main":
                page.views.append(MainView(page))
            case "/main/settings":
                page.views.append(SettingsView(page))
            case "/main/account/statistics":
                statistics_screen = StatisticsScreen(page)
                page.views.append(statistics_screen.create_statistics_screen())
            case "/main/theory_1":
                first_theory_screen = FirstTheoryView(page)
                page.views.append(
                    first_theory_screen.create_first_theory_screen())
            case "/main/test_1":
                first_test_screen = FirstTestScreen(page)
                page.views.append(first_test_screen.create_first_test_screen())
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


ft.app(target=main, assets_dir='assets')
