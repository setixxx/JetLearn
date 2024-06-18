import flet as ft
from account_view_sources.components.login_card_sources.header import Header
from account_view_sources.components.login_card_sources.button_change_login \
    import ButtonChangeLogin
from account_view_sources.components.login_card_sources \
    .change_login_field import ChangeLoginField


class LoginCard(ft.Card):
    def __init__(self, app_state):
        super().__init__()
        self.app_state = app_state
        self.change_login_field = ChangeLoginField()
        self.content = ft.Column(
            [
                Header(),
                self.change_login_field,
                ButtonChangeLogin(self.change_login_field,
                                  self.app_state),
            ],
            spacing=0,
            width=344,
            height=231,
        )
