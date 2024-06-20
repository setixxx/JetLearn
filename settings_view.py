import flet as ft
from theory_view_sources.components.arrow_back_and_logo import ArrowBackAndLogo

# Класс для представления виджета прогресса по теории
class TheoryProgress(ft.Container):
    def __init__(self, app_state):
        super().__init__()
        # Сохраняем ссылку на объект состояния приложения
        self.app_state = app_state
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(left=22)
        self.width = 344
        self.height = 79
        # Создаем строку с элементами прогресса
        self.content = ft.Row(
            [
                # Иконка учебника
                ft.Container(
                    ft.Icon(
                        name=ft.icons.CLASS_OUTLINED,
                        color=ft.colors.ON_SURFACE
                    )
                ),
                # Текст и полоса прогресса
                ft.Column(
                    [
                        # Текст "Пройденная теория"
                        ft.Text(
                            "Пройденная теория",
                            size=14,
                            weight=ft.FontWeight.W_500
                        ),
                        # Полоса прогресса
                        ft.ProgressBar(
                            self.app_state.get_completed_theory(),
                            width=214,
                            height=4
                        ),
                        # Текст с описанием прогресса
                        ft.Text(
                            f"Пройдено {self.app_state.get_formatted_theory()} разделов",
                            size=12,
                            weight=ft.FontWeight.W_300
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

# Класс для представления виджета прогресса по тестам
class TestProgress(ft.Container):
    def __init__(self, app_state):
        super().__init__()
        # Сохраняем ссылку на объект состояния приложения
        self.app_state = app_state
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(left=22)
        self.width = 344
        self.height = 82
        # Создаем строку с элементами прогресса
        self.content = ft.Row(
            [
                # Иконка галереи
                ft.Container(
                    ft.Icon(
                        name=ft.icons.BROWSE_GALLERY_OUTLINED,
                        color=ft.colors.ON_SURFACE
                    )
                ),
                # Текст и полоса прогресса
                ft.Column(
                    [
                        # Текст "Пройденные тесты"
                        ft.Text(
                            "Пройденные тесты",
                            size=14,
                            weight=ft.FontWeight.W_500
                        ),
                        # Полоса прогресса
                        ft.ProgressBar(
                            self.app_state.get_completed_tests(),
                            width=214,
                            height=4
                        ),
                        # Текст с описанием прогресса
                        ft.Text(
                            f"Пройдено {self.app_state.get_formatted_tests()} тестов",
                            size=12,
                            weight=ft.FontWeight.W_300
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

class Subheader(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(left=22)
        self.width = 344
        self.height = 56
        # Создаем текст подзаголовка
        self.content = ft.Row(
            [
                ft.Text(
                    "Детальная информация о пройденных\n"
                    "вами, а также остальными,\n"
                    "пользователями тестах",
                    size=14,
                    weight=ft.FontWeight.W_500,
                    style=ft.TextStyle(
                        height=1.2
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.END
        )

# Класс для представления виджета кнопки "Перейти"
class ButtonGoToStatistics(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.alignment = ft.alignment.bottom_right
        self.padding = ft.padding.only(bottom=22, right=22)
        self.width = 344
        self.height = 84
        # Создаем кнопку "Перейти"
        self.content = ft.FilledButton(
            text="Перейти",
            on_click=lambda e: self.page.go("/main/settings/statistics")
        )

# Класс для представления виджета заголовка "Статистика"
class HeaderStatistics(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(left=21, bottom=3)
        self.width = 344
        self.height = 45
        # Создаем текст заголовка
        self.content = ft.Row(
            [
                ft.Text(
                    "Статистика",
                    size=20,
                    weight=ft.FontWeight.W_500
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.END
        )

# Класс карточки статистики
class StatisticsCard(ft.Card):
    def __init__(self, app_state):
        super().__init__()
        # Сохраняем ссылку на объект состояния приложения
        self.app_state = app_state
        # Создаем столбец с элементами карточки
        self.content = ft.Column(
            [
                # Заголовок карточки
                HeaderStatistics(),
                # Подзаголовок карточки
                Subheader(),
                # Прогресс по теории
                TheoryProgress(app_state),
                # Прогресс по тестам
                TestProgress(app_state),
                # Кнопка "Перейти"
                ButtonGoToStatistics(),
            ],
            spacing=0,
            width=344,
            height=346,
        )

# Класс для представления виджета кнопки "Перейти"
class ButtonGoToAccount(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.alignment = ft.alignment.bottom_right
        self.padding = ft.padding.only(bottom=22, right=22)
        self.width = 344
        self.height = 149
        # Создаем кнопку "Перейти"
        self.content = ft.Row(
            [
                ft.FilledButton(
                    text="Перейти",
                    on_click=lambda e: self.page.go("/main/settings/account")
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.END
        )

# Класс для представления виджета заголовка "Персональные данные"
class HeaderAccount(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(left=21, top=16)
        self.width = 344
        self.height = 73
        # Создаем текст заголовка
        self.content = ft.Row(
            [
                ft.Text(
                    "Персональные\nданные",
                    size=20,
                    weight=ft.FontWeight.W_500,
                    style=ft.TextStyle(
                        height=1.2
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START
        )

# Класс для представления виджета подзаголовка
class SubheaderSettings(ft.Container):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.padding = ft.padding.only(left=22, top=3)
        self.width = 344
        self.height = 124
        # Создаем текст подзаголовка
        self.content = ft.Row(
            [
                ft.Text(
                    "Информация о вашем аккаунте.\n"
                    "По желанию вы можете ее изменить.\n"
                    "Не забывайте обновлять эту информацию,\n"
                    "чтобы у вас всегда был доступ к аккаунту\n"
                    "JetLearn",
                    size=14,
                    weight=ft.FontWeight.W_500,
                    style=ft.TextStyle(
                        height=1.2
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START
        )

# Класс карточки "Аккаунт"
class AccountCard(ft.Card):
    def __init__(self):
        super().__init__()
        # Создаем столбец с элементами карточки
        self.content = ft.Column(
            [
                HeaderAccount(),
                SubheaderSettings(),
                ButtonGoToAccount()
            ],
            spacing=0,
            width=344,
            height=346,
        )

# Класс для представления диалогового окна подтверждения выхода
class ConfirmLogoutDialog(ft.AlertDialog):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили диалогового окна
        self.modal = True
        self.title = ft.Text("Подтверждение", weight=ft.FontWeight.W_600)
        self.content = ft.Text("Вы действительно хотите\nвыйти из аккаунта?")
        self.actions = [
            # Кнопка "Да"
            ft.TextButton(
                text="Да",
                on_click=lambda e: self.page.go("/sign_in")
            ),
            # Кнопка "Нет"
            ft.FilledButton(
                text="Нет",
                on_click=self.close_results
            ),
        ]
        self.actions_alignment = ft.MainAxisAlignment.END

    # Метод закрытия диалогового окна
    def close_results(self, e):
        self.open = False
        self.page.update()

# Класс для представления кнопки "Выйти из аккаунта"
class ButtonLogOut(ft.Row):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.alignment = ft.MainAxisAlignment.END
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 1500
        self.height = 178
        # Создаем кнопку "Выйти из аккаунта"
        self.controls = [
            ft.Container(
                ft.FilledButton(
                    "Выйти из аккаунта",
                    on_click=self.confirm_logout
                ),
                padding=ft.padding.only(right=32)
            )
        ]

    # Метод подтверждения выхода
    def confirm_logout(self, e):
        # Создаем диалоговое окно подтверждения выхода
        self.page.dialog = ConfirmLogoutDialog()
        self.page.dialog.open = True
        self.page.update()

# Класс для представления заголовка "Настройки"
class SettingsHeader(ft.Row):
    def __init__(self, app_state):
        super().__init__()
        # Сохраняем ссылку на объект состояния приложения
        self.app_state = app_state
        # Устанавливаем стили контейнера
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 1500
        self.height = 44
        # Создаем текст заголовка
        self.controls = [
            ft.Text(
                f"Добро пожаловать, {self.app_state.get_login()}!",
                size=32,
                weight=ft.FontWeight.W_700
            )
        ]

# Класс для представления подзаголовка "Настройки"
class SettingsSubheader(ft.Row):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 1500
        self.height = 44
        # Создаем текст подзаголовка
        self.controls = [
            ft.Text(
                "Здесь вы можете настроить данные своего аккаунта или ознакомиться с вашей\n"
                "персональной статистикой",
                text_align=ft.TextAlign.CENTER,
                size=14,
                weight=ft.FontWeight.W_500
            )
        ]

# Класс для представления изображения профиля
class ProfileImage(ft.Row):
    def __init__(self):
        super().__init__()
        # Устанавливаем стили контейнера
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 1500
        self.height = 100
        # Создаем контейнер для изображения
        self.controls = [
            ft.Container(
                bgcolor=ft.colors.PRIMARY,
                width=100,
                height=100,
                border_radius=100
            )
        ]

# Класс представления страницы "Настройки"
class SettingsView(ft.View):
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохраняем ссылки на страницу и состояние приложения
        self.page = page
        self.app_state = app_state
        # Устанавливаем маршрут
        self.title = "/main/settings"
        self.padding = 0

        # Создаем элементы представления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Кнопка "Назад" и логотип
                        ArrowBackAndLogo(lambda e: self.page.go("/main")),
                        # Изображение профиля
                        ProfileImage(),
                        # Заголовок "Настройки"
                        SettingsHeader(app_state),
                        # Подзаголовок "Аккаунт"
                        SettingsSubheader(),
                        # Карточки статистики и аккаунта
                        ft.Row(
                            [
                                StatisticsCard(app_state),
                                AccountCard()
                            ],
                            spacing=23,
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            width=1500,
                            height=346,
                        ),
                        # Кнопка "Выйти"
                        ButtonLogOut()
                    ],
                    spacing=8
                ),
                width=1500,
                height=800
            )
        ]