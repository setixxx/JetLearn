import flet as ft
from database import DatabaseManager


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