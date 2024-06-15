import flet as ft
from account_view_sources.components.login_card_sources.header import Header
from account_view_sources.components.login_card_sources.button_change_email \
    import ButtonChangeEmail
from account_view_sources.components.login_card_sources \
    .change_email_text_field import ChangeEmailTextField

class LoginCard(ft.Card):
    def __init__(self):
        super().__init__()
        self.content = ft.Column(
            [
                Header(),
                ChangeEmailTextField(),
                ButtonChangeEmail(),
            ],
            spacing=0,
            width=344,
            height=221,
        )
