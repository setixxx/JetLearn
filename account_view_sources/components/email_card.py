# Импорт библиотеки flet
import flet as ft

# Импорт компонентов из подкаталогов
from account_view_sources.components.email_card_sources \
    .header_change_email import HeaderChangeEmail
from account_view_sources.components.email_card_sources.button_change_email \
    import ButtonChangeEmail
from account_view_sources.components.email_card_sources \
    .change_email_text_field import ChangeEmailField


# Класс карточки смены email
class EmailCard(ft.Card):
    # Инициализация карточки
    def __init__(self, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Создание поля ввода нового email
        self.change_email_field = ChangeEmailField()
        # Создание столбца с элементами карточки
        self.content = ft.Column(
            [
                # Заголовок "Изменить email"
                HeaderChangeEmail(),
                # Поле ввода нового email
                self.change_email_field,
                # Кнопка "Изменить email"
                ButtonChangeEmail(self.change_email_field,
                                  self.app_state)
            ],
            spacing=0,
            width=344,
            height=231,
        )