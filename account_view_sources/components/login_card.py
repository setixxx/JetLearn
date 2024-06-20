# Импорт библиотеки flet
import flet as ft
from database import DatabaseManager

# Класс заголовка "Изменение логина"
class HeaderChangeLogin(ft.Container):
    # Инициализация заголовка
    def __init__(self):
        super().__init__()
        # Установка отступов
        self.padding = ft.padding.only(left=21, bottom=3)
        # Установка ширины и высоты
        self.width = 344
        self.height = 45
        # Создание строки с текстом заголовка
        self.content = ft.Row(
            [
                ft.Text(
                    "Изменение логина",
                    # Установка размера и веса шрифта
                    size=20,
                    weight=ft.FontWeight.W_500
                )
            ],
            # Выравнивание по левому краю
            alignment=ft.MainAxisAlignment.START,
            # Выравнивание по нижнему краю
            vertical_alignment=ft.CrossAxisAlignment.END
        )

# Класс контейнера с полем ввода для изменения логина
class ChangeLoginField(ft.Container):
    # Инициализация контейнера
    def __init__(self):
        super().__init__()
        # Установка ширины и высоты
        self.width = 344
        self.height = 114
        # Выравнивание по левому верхнему краю
        self.alignment = ft.alignment.top_left
        # Установка отступов
        self.padding = ft.padding.only(top=16,
                                       left=32)
        # Создание поля ввода нового логина
        self.login_change_field = ft.TextField(
            # Установка подписи поля
            label="Новый логин",
            # Установка размера текста
            text_size=16,
            # Установка ширины поля
            width=280,
            # Установка максимальной длины ввода
            max_length=16,
        )
        # Установка поля ввода в качестве контента контейнера
        self.content = self.login_change_field

    # Метод получения значения поля ввода нового логина
    def get_login_change_field(self):
        return self.login_change_field.value

    # Метод получения текста ошибки поля ввода нового логина
    def get_login_change_error_text(self):
        return self.login_change_field.error_text

    # Метод установки текста ошибки поля ввода нового логина
    def set_login_error_change(self, error_text):
        self.login_change_field.error_text = error_text
        self.login_change_field.update()

# Класс кнопки "Изменить логин"
class ButtonChangeLogin(ft.Container):
    # Инициализация кнопки
    def __init__(self, change_login_field, app_state):
        super().__init__()
        # Создание объекта базы данных
        self.database = DatabaseManager("users.sqlite")
        # Сохранение поля ввода логина и состояния приложения
        self.change_login_field = change_login_field
        self.app_state = app_state
        # Выравнивание по правому нижнему краю
        self.alignment = ft.alignment.bottom_right
        # Установка отступов
        self.padding = ft.padding.only(right=32,
                                       bottom=32)
        # Установка ширины и высоты
        self.width = 344
        self.height = 72
        # Создание кнопки "Изменить"
        self.content = ft.FilledButton(
            # Установка текста кнопки
            text="Изменить",
            # Установка обработчика клика
            on_click=self.check_login_change
        )

    # Метод проверки ввода нового логина
    def check_login_change(self, e):
        # Получение нового логина
        login = self.change_login_field.get_login_change_field()
        # Проверка наличия нового логина в базе данных
        login_check = self.database.check_user_login(login)

        # Проверка ввода логина
        if login == "":
            # Вывод ошибки в поле ввода логина
            self.change_login_field.set_login_error_change("Логин не "
                                                           "может быть "
                                                           "пустым")
        elif login_check:
            # Вывод ошибки в поле ввода логина
            self.change_login_field.set_login_error_change("Логин занят")
        else:
            # Очистка ошибки поля ввода логина
            self.change_login_field.set_login_error_change(None)

        # Получение текста ошибки поля ввода
        login_error = self.change_login_field.get_login_change_error_text()

        # Проверка на отсутствие ошибок
        if login_error == "" or login_error is None:
            # Обновление логина в базе данных
            self.database.update_user_login(self.app_state.get_login(),
                                            login)
            # Поиск email по новому логину
            find_email = self.database.find_email_by_login(login)
            # Проверка, совпадает ли email в состоянии приложения с найденным
            if self.app_state.get_email() == find_email[0]:
                # Обновление логина в состоянии приложения
                self.app_state.set_login(login)
                # Вывод сообщения об успешном изменении логина
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Логин успешно изменен!")
                )
                self.page.snack_bar.open = True
                self.page.update()
            else:
                # Вывод сообщения об ошибке
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Произошла ошибка!")
                )
                self.page.snack_bar.open = True
                self.page.update()


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