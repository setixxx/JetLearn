import flet as ft
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from settings_view_sources.components.profile_image import ProfileImage
from settings_view_sources.components.settings_header import SettingsHeader
from settings_view_sources.components.settings_subheader import SettingsSubheader
from settings_view_sources.components.button_log_out import ButtonLogOut
from settings_view_sources.components.statistics_card import StatisticsCard
from settings_view_sources.components.account_card import AccountCard


# Класс представления страницы "Настройки"
class SettingsView(ft.View):
    # Инициализация представления
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохранение ссылки на страницу
        self.page = page
        # Установка маршрута
        self.title = "/main/settings"
        # Установка отступов
        self.padding = 0
        # Создание списка элементов управления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Кнопка "Назад" и логотип
                        ArrowBackAndLogo(
                            lambda e: self.page.go("/main")
                        ),
                        # Изображение профиля
                        ProfileImage(),
                        # Заголовок "Настройки"
                        SettingsHeader(app_state),
                        # Подзаголовок "Аккаунт"
                        SettingsSubheader(),
                        # Строка с карточками статистики и аккаунта
                        ft.Row(
                            [
                                # Карточка статистики
                                StatisticsCard(app_state),
                                # Карточка аккаунта
                                AccountCard()
                            ],
                            # Междуэлементный интервал
                            spacing=23,
                            # Выравнивание по горизонтали
                            alignment=ft.MainAxisAlignment.CENTER,
                            # Выравнивание по вертикали
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            # Ширина строки
                            width=1500,
                            # Высота строки
                            height=346,
                        ),
                        # Кнопка "Выйти"
                        ButtonLogOut()
                    ],
                    # Междурядный интервал
                    spacing=8
                ),
                # Ширина контейнера
                width=1500,
                # Высота контейнера
                height=800
            )
        ]