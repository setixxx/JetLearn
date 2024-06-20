# Импорт библиотеки flet
import flet as ft

# Импорт компонентов из подкаталогов
from account_view_sources.components.password_card_sources \
    .header_change_password import HeaderChangePassword
from account_view_sources.components.password_card_sources \
    .button_change_password import ButtonChangePassword
from account_view_sources.components.password_card_sources \
    .change_password_text_field import ChangePasswordField


# Класс карточки смены пароля
class PasswordCard(ft.Card):
    # Инициализация карточки
    def __init__(self, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Создание поля ввода нового пароля
        self.change_password_field = ChangePasswordField()
        # Создание столбца с элементами карточки
        self.content = ft.Column(
            [
                # Заголовок "Изменить пароль"
                HeaderChangePassword(),
                # Поле ввода нового пароля
                self.change_password_field,
                # Кнопка "Изменить пароль"
                ButtonChangePassword(self.change_password_field,
                                     self.app_state)
            ],
            spacing=0,
            width=344,
            height=345,
        )