import flet as ft
from account_view_sources.components.password_card_sources.header import Header
from account_view_sources.components.password_card_sources \
    .button_change_password import ButtonChangePassword
from account_view_sources.components.password_card_sources \
    .change_password_text_field import ChangePasswordTextField


class PasswordCard(ft.Card):
    def __init__(self):
        super().__init__()
        self.content = ft.Column(
            [
                Header(),
                ChangePasswordTextField(),
                ButtonChangePassword()
            ],
            spacing=0,
            width=344,
            height=345,
        )
