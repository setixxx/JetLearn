import flet as ft

# Импорт компонентов из подкаталогов
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo
from settings_view import ProfileImage
from account_view_sources.components.login_card import LoginCard
from account_view_sources.components.email_card import EmailCard
from account_view_sources.components.password_card import PasswordCard

# Класс заголовка "Персональные данные"
class AccountHeader(ft.Row):
    def __init__(self):
        super().__init__()
        # Выравнивание по центру
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        # Установка ширины и высоты
        self.width = 1500
        self.height = 44
        # Создание текста заголовка
        self.controls = [
            ft.Text(
                "Персональные данные",
                size=32,
                weight=ft.FontWeight.W_700
            )
        ]

# Класс представления профиля пользователя
class AccountView(ft.View):
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохраняем ссылку на страницу и объект состояния приложения
        self.page = page
        self.app_state = app_state
        # Устанавливаем маршрут
        self.title = "/main/settings/account"
        self.padding = 0

        # Создаем элементы представления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Кнопка назад и логотип
                        ArrowBackAndLogo(lambda e: self.page.go("/main/settings")),
                        # Картинка профиля
                        ProfileImage(),
                        # Заголовок профиля
                        AccountHeader(),
                        # Информация о пользователе
                        ft.Row(
                            [
                                # Логин и email
                                ft.Column(
                                    [
                                        LoginCard(app_state),
                                        EmailCard(app_state)
                                    ],
                                    spacing=23
                                ),
                                # Пароль
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