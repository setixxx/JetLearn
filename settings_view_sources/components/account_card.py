import flet as ft
from settings_view_sources.components.account_card_sources.header import Header
from settings_view_sources.components.account_card_sources.subheader import \
    Subheader
from settings_view_sources.components.account_card_sources.button_go_to_account import \
    ButtonGoToAccount


# Класс карточки "Аккаунт"
class AccountCard(ft.Card):
    # Инициализация карточки
    def __init__(self):
        super().__init__()
        # Создание столбца с элементами карточки
        self.content = ft.Column(
            [
                # Заголовок карточки
                Header(),
                # Подзаголовок карточки
                Subheader(),
                # Кнопка перехода к странице аккаунта
                ButtonGoToAccount()
            ],
            # Междурядный интервал
            spacing=0,
            # Ширина карточки
            width=344,
            # Высота карточки
            height=346,
        )