import flet as ft

from sign_up_view_sources.components.header_email import HeaderEmail
from sign_up_view_sources.components.password_check_box import \
    PasswordCheckBox
from sign_up_view_sources.components.subheader_email import \
    SubheaderEmail
from sign_up_view_sources.components.sign_up_fields import \
    SignUpFields
from sign_up_view_sources.components.buttons_sign_up import \
    ButtonsSignUp

# Класс представления страницы регистрации
class SignUpView(ft.View):
    # Инициализация представления
    def __init__(self, page: ft.Page, app_state):
        super().__init__()
        # Сохранение состояния приложения
        self.app_state = app_state
        # Сохранение ссылки на страницу
        self.page = page
        # Создание виджета для ввода данных регистрации
        self.sign_up_fields = SignUpFields()
        # Создание виджета для отображения чекбокса "Показать пароль"
        self.password_check_box = PasswordCheckBox(self.show_password)
        # Установка маршрута
        self.route = "/sign_up"
        # Установка отступов
        self.padding = 0
        # Создание списка элементов управления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Контейнер для заголовка, подзаголовка и полей ввода
                        ft.Container(
                            ft.Row(
                                [
                                    # Столбец для заголовка и подзаголовка
                                    ft.Column(
                                        [
                                            # Виджет заголовка
                                            HeaderEmail(),
                                            # Виджет подзаголовка
                                            SubheaderEmail()
                                        ],
                                        spacing=0
                                    ),
                                    # Столбец для полей ввода и кнопок
                                    ft.Column(
                                        [
                                            # Виджет для ввода данных регистрации
                                            self.sign_up_fields,
                                            # Виджет чекбокса "Показать пароль"
                                            self.password_check_box,
                                            # Виджет с кнопками "Зарегистрироваться" и "Уже есть аккаунт?"
                                            ButtonsSignUp(self.sign_up_fields,
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
                    ],
                    spacing=0,
                ),
                # Отступы вокруг контейнера
                margin=ft.padding.only(left=198,
                                       right=198,
                                       top=150,
                                       bottom=150),
                # Ширина контейнера
                width=1105,
                # Высота контейнера
                height=500,
            )
        ]

    # Метод отображения/скрытия пароля
    def show_password(self, e):
        # Проверка состояния чекбокса
        if self.password_check_box.content.controls[0].value:
            # Отображение пароля
            self.sign_up_fields.content.controls[1].controls[0].password = False
            self.sign_up_fields.content.controls[1].controls[1].password = False
        else:
            # Скрытие пароля
            self.sign_up_fields.content.controls[1].controls[0].password = True
            self.sign_up_fields.content.controls[1].controls[1].password = True
        # Обновление страницы
        self.page.update()