import flet as ft
from settings_view_sources.components.account_card_sources.header import Header
from settings_view_sources.components.account_card_sources.subheader import \
    Subheader
from settings_view_sources.components.account_card_sources.button_go_to_account import \
    ButtonGoToAccount


class AccountCard(ft.Card):
    def __init__(self):
        super().__init__()
        self.content = ft.Column(
            [
                Header(),
                Subheader(),
                ButtonGoToAccount()
            ],
            spacing=0,
            width=344,
            height=346,
        )
