# Импорт библиотеки flet
import flet as ft

# Импорт компонентов из подкаталогов
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from account_view_sources.components.account_header import AccountHeader
from settings_view_sources.components.profile_image import ProfileImage
from account_view_sources.components.login_card import LoginCard
from account_view_sources.components.email_card import EmailCard
from account_view_sources.components.password_card import PasswordCard


# Класс представления профиля пользователя
class AccountView(ft.View):
    # Инициализация представления
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        self.page = page
        # Установка маршрута
        self.title = "/main/settings/account"
        self.padding = 0
        # Создание списка элементов представления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Кнопка назад и логотип
                        ArrowBackAndLogo(
                            lambda e: self.page.go("/main/settings")
                        ),
                        # Картинка профиля
                        ProfileImage(),
                        # Заголовок профиля
                        AccountHeader(),
                        # Строка с информацией о пользователе
                        ft.Row(
                            [
                                # Столбец с логином и email
                                ft.Column(
                                    [
                                        LoginCard(app_state),
                                        EmailCard(app_state)
                                    ],
                                    spacing=23
                                ),
                                # Столбец с паролем
                                PasswordCard(app_state)
                            ],
                            spacing=23,
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            width=1500,
                            height=494,
                        ),
                    ],
                ),
                width=1500,
                height=800
            )
        ]