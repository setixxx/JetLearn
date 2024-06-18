import flet as ft
from account_view_sources.components.email_card_sources.header import Header
from account_view_sources.components.email_card_sources.button_change_email \
    import ButtonChangeEmail
from account_view_sources.components.email_card_sources \
    .change_email_text_field import ChangeEmailField


class EmailCard(ft.Card):
    def __init__(self, app_state):
        super().__init__()
        self.app_state = app_state
        self.change_email_field = ChangeEmailField()
        self.content = ft.Column(
            [
                Header(),
                self.change_email_field,
                ButtonChangeEmail(self.change_email_field,
                                  self.app_state)
            ],
            spacing=0,
            width=344,
            height=231,
        )
