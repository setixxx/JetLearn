import flet as ft
from start_view_sources.components.welcome_text import WelcomeText
from start_view_sources.components.introduction_text import IntroductionText
from start_view_sources.components.button_start import ButtonStart
from start_view_sources.components.github_link_and_image import \
    GitHubLinkAndImage


# Класс представления начальной страницы
class StartView(ft.View):
    # Инициализация представления
    def __init__(self, page: ft.Page):
        super().__init__()
        # Сохранение ссылки на страницу
        self.page = page
        # Установка маршрута
        self.route = "/"
        # Установка отступов
        self.padding = 0

        # Создание списка элементов управления
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        # Контейнер для приветствия, введения и кнопки "Начать"
                        ft.Container(
                            ft.Column(
                                [
                                    # Виджет приветствия
                                    WelcomeText(),
                                    # Виджет введения
                                    IntroductionText(),
                                    # Кнопка "Начать"
                                    ButtonStart(),
                                ],
                                spacing=0
                            ),
                            # Отступы
                            margin=0,
                            # Фоновый цвет
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            # Радиус скругления
                            border_radius=40
                        ),
                        # Строка с ссылкой на GitHub
                        ft.Row(
                            [
                                # Виджет ссылки на GitHub
                                GitHubLinkAndImage()
                            ],
                            # Ширина строки
                            width=1200,
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
                margin=ft.padding.only(top=100,
                                       left=150,
                                       right=150,
                                       bottom=175),
                # Ширина контейнера
                width=1200,
                # Высота контейнера
                height=600,
            )
        ]