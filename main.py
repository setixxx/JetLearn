import flet as ft
from sign_up_view_sources.sign_up_view import SignUpView
from sign_in_view_sources.sign_in_view import SignInView
from main_view_sources.main_view import MainView
from start_view_sources.start_view import StartView
from theory_view_sources.first_theory_view import FirstTheoryView
from theory_view_sources.second_theory_view import SecondTheoryView
from theory_view_sources.third_theory_view import ThirdTheoryView
from theory_view_sources.fourth_theory_view import FourthTheoryView
from theory_view_sources.fifth_theory_view import FifthTheoryView
from theory_view_sources.sixth_theory_view import SixthTheoryView
from theory_view_sources.seventh_theory_view import SeventhTheoryView
from theory_view_sources.eighth_theory_view import EighthTheoryView
from settings_view_sources.settings_view import SettingsView
from statistics_view_sources.statistics_view import StatisticsView
from tests_view_sources.test_view import FirstTestView
from practice_screens_sources.practice_screen_source.practice_screen import PracticeScreen
from account_view_sources.account_view import AccountView
from database import DatabaseManager
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
                page.views.append(AccountView(page, app_state))
            case "/main/settings/statistics":
                page.views.append(StatisticsView(page, app_state))
            case "/main/theory_1":
                page.views.append(FirstTheoryView(page))
            case "/main/theory_2":
                page.views.append(SecondTheoryView(page))
            case "/main/theory_3":
                page.views.append(ThirdTheoryView(page))
            case "/main/theory_4":
                page.views.append(FourthTheoryView(page))
            case "/main/theory_5":
                page.views.append(FifthTheoryView(page))
            case "/main/theory_6":
                page.views.append(SixthTheoryView(page))
            case "/main/theory_7":
                page.views.append(SeventhTheoryView(page))
            case "/main/theory_8":
                page.views.append(EighthTheoryView(page))
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

    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()

    page.window_prevent_close = True
    page.on_window_event = window_event

    def click_exit(e):
        page.window_destroy()

    def click_stay(e):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(
            "Подтверждение",
            weight=ft.FontWeight.W_600
        ),
        content=ft.Text(
            "Вы действительно хотите выйти?",
            weight=ft.FontWeight.W_400
        ),
        actions=[
            ft.TextButton("Да", on_click=click_exit),
            ft.FilledButton("Нет", on_click=click_stay),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    database = DatabaseManager("users.sqlite")
    database.create_table_users()

ft.app(target=main, assets_dir='assets')
