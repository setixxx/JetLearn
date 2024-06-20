import flet as ft
from sign_in_view_sources.components.header_log_in import HeaderLogIn
from sign_in_view_sources.components.subheader_log_in import SubheaderLogIn
from sign_in_view_sources.components.sign_in_fields import SignInFields
from sign_in_view_sources.components.buttons_sign_in import ButtonsSignIn
from start_view_sources.components.github_link_and_image import GitHubLinkAndImage

# Класс представления страницы входа в систему
class SignInView(ft.View):
    # Инициализация представления
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Сохранение ссылки на страницу
        self.page = page
        # Установка маршрута
        self.route = "/sign_in"
        # Установка отступов
        self.padding = 0

        # Создание виджета для ввода данных входа
        self.sign_in_fields = SignInFields()

        # Создание списка элементов управления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Контейнер для заголовка и подзаголовка
                        ft.Container(
                            ft.Row(
                                [
                                    # Столбец для заголовка и подзаголовка
                                    ft.Column(
                                        [
                                            # Виджет заголовка
                                            HeaderLogIn(),
                                            # Виджет подзаголовка
                                            SubheaderLogIn()
                                        ],
                                        spacing=0
                                    ),
                                    # Столбец для полей ввода и кнопок
                                    ft.Column(
                                        [
                                            # Виджет для ввода данных входа
                                            self.sign_in_fields,
                                            # Виджет с кнопками "Войти" и "Забыли пароль?"
                                            ButtonsSignIn(
                                                self.sign_in_fields,
                                                self.app_state)
                                        ],
                                        spacing=0
                                    )
                                ],
                                spacing=0
                            ),
                            # Отступы
                            margin=0,
                            padding=0,
                            # Фоновый цвет
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            # Радиус скругления
                            border_radius=22,
                        ),
                        # Строка с ссылкой на GitHub
                        ft.Row(
                            [
                                # Виджет ссылки на GitHub
                                GitHubLinkAndImage()
                            ],
                            # Ширина строки
                            width=884,
                            # Высота строки
                            height=75,
                            # Выравнивание по горизонтали
                            alignment=ft.MainAxisAlignment.END,
                            # Выравнивание по вертикали
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                    ],
                    spacing=0,
                ),
                # Отступы вокруг контейнера
                margin=ft.padding.only(top=203, left=308, right=308, bottom=255),
                # Ширина контейнера
                width=884,
                # Высота контейнера
                height=417,
            )
        ]