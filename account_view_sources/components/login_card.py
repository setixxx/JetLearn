import flet as ft
from account_view_sources.components.login_card_sources.header import Header
from account_view_sources.components.login_card_sources.button_change_login \
    import ButtonChangeLogin
from account_view_sources.components.login_card_sources \
    .change_login_text_field import ChangeLoginTextField


class LoginCard(ft.Card):
    def __init__(self):
        super().__init__()
        self.content = ft.Column(
            [
                Header(),
                ChangeLoginTextField(),
                ButtonChangeLogin(),
            ],
            spacing=0,
            width=344,
            height=231,
        )
