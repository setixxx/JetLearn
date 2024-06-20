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
from tests_view_sources.first_test_view import FirstTestView
from tests_view_sources.second_test_view import SecondTestView
from tests_view_sources.third_test_view import ThirdTestView
from tests_view_sources.fourth_test_view import FourthTestView
from tests_view_sources.fifth_test_view import FifthTestView
from tests_view_sources.sixth_test_view import SixthTestView
from tests_view_sources.seventh_test_view import SeventhTestView
from tests_view_sources.eighth_test_view import EighthTestView
from practice_view_source.practice_view import PracticeView
from account_view_sources.account_view import AccountView
from database import DatabaseManager
from app_state import AppState

def main(page: ft.Page):
    # Настройка страницы приложения.
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

    # Инициализация состояния приложения и менеджера базы данных.
    app_state = AppState()
    db_manager = DatabaseManager("users.sqlite")

    # Функция для обработки изменения маршрута.
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
                page.views.append(MainView(page, app_state))
            case "/main/settings":
                page.views.append(SettingsView(page, app_state))
            case "/main/settings/account":
                page.views.append(AccountView(page, app_state))
            case "/main/settings/statistics":
                page.views.append(StatisticsView(page, app_state))
            case "/main/theory_1":
                page.views.append(FirstTheoryView(page, app_state))
            case "/main/theory_2":
                page.views.append(SecondTheoryView(page, app_state))
            case "/main/theory_3":
                page.views.append(ThirdTheoryView(page, app_state))
            case "/main/theory_4":
                page.views.append(FourthTheoryView(page, app_state))
            case "/main/theory_5":
                page.views.append(FifthTheoryView(page, app_state))
            case "/main/theory_6":
                page.views.append(SixthTheoryView(page, app_state))
            case "/main/theory_7":
                page.views.append(SeventhTheoryView(page, app_state))
            case "/main/theory_8":
                page.views.append(EighthTheoryView(page, app_state))
            case "/main/test_1":
                page.views.append(FirstTestView(page, db_manager, app_state))
            case "/main/test_2":
                page.views.append(SecondTestView(page, db_manager, app_state))
            case "/main/test_3":
                page.views.append(ThirdTestView(page, db_manager, app_state))
            case "/main/test_4":
                page.views.append(FourthTestView(page, db_manager, app_state))
            case "/main/test_5":
                page.views.append(FifthTestView(page, db_manager, app_state))
            case "/main/test_6":
                page.views.append(SixthTestView(page, db_manager, app_state))
            case "/main/test_7":
                page.views.append(SeventhTestView(page, db_manager, app_state))
            case "/main/test_8":
                page.views.append(EighthTestView(page, db_manager, app_state))
            case "/main/practice":
                page.views.append(PracticeView(page, app_state))
        page.update()

    # Функция для обработки события "назад" (view_pop).
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Устанавливаем обработчики событий для изменения маршрута и нажатия "назад".
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Загружаем начальный маршрут.
    page.go(page.route)

    # Обработчик события закрытия окна приложения.
    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()

    # Запрещаем закрытие окна без подтверждения.
    page.window_prevent_close = True
    page.on_window_event = window_event

    # Обработчики кликов по кнопкам в диалоге подтверждения.
    def click_exit(e):
        page.window_destroy()

    def click_stay(e):
        confirm_dialog.open = False
        page.update()

    # Создание диалога подтверждения.
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

    # Инициализация базы данных.
    database = DatabaseManager("users.sqlite")
    database.create_table_users()

    # Запуск приложения.
ft.app(target=main, assets_dir='assets')