# Импорт библиотеки flet
import flet as ft

# Импорт компонентов из подкаталогов
from account_view_sources.components.login_card_sources \
    .header_change_login import HeaderChangeLogin
from account_view_sources.components.login_card_sources.button_change_login \
    import ButtonChangeLogin
from account_view_sources.components.login_card_sources \
    .change_login_field import ChangeLoginField


# Класс карточки смены логина
class LoginCard(ft.Card):
    # Инициализация карточки
    def __init__(self, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Создание поля ввода нового логина
        self.change_login_field = ChangeLoginField()
        # Создание столбца с элементами карточки
        self.content = ft.Column(
            [
                # Заголовок "Изменить логин"
                HeaderChangeLogin(),
                # Поле ввода нового логина
                self.change_login_field,
                # Кнопка "Изменить логин"
                ButtonChangeLogin(self.change_login_field,
                                  self.app_state),
            ],
            spacing=0,
            width=344,
            height=231,
        )